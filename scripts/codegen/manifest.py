"""
CodegenManifest - 代码生成清单管理

追踪已生成的文件，支持增量编译和孤儿清理。
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field

from scripts.codegen.exceptions import ManifestError

logger = logging.getLogger(__name__)

GeneratorType = Literal["rule", "factor", "semantic"]


class ManifestEntry(BaseModel):
    """清单条目"""
    
    source_file: str = Field(..., description="源文件路径")
    output_file: str = Field(..., description="输出文件路径")
    source_hash: str = Field(..., description="源文件SHA256哈希")
    output_hash: str = Field(..., description="输出文件SHA256哈希")
    generator_type: GeneratorType = Field(..., description="生成器类型")
    engine_id: str = Field(..., description="引擎ID")
    version: str = Field(..., description="版本号")
    compiled_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="编译时间"
    )
    
    def is_stale(self, current_source_hash: str) -> bool:
        """检查是否需要重新编译"""
        return self.source_hash != current_source_hash


class CodegenManifest:
    """
    代码生成清单
    
    追踪源文件到生成文件的映射，支持：
    - 增量编译（只编译变更的文件）
    - 孤儿清理（删除不再需要的生成文件）
    - 状态查询
    """
    
    MANIFEST_FILENAME = ".codegen_manifest.json"
    
    def __init__(self, generated_dir: Path):
        self.generated_dir = Path(generated_dir)
        self.manifest_path = self.generated_dir / self.MANIFEST_FILENAME
        self._entries: Dict[str, ManifestEntry] = {}
        self._load()
    
    def _load(self) -> None:
        """加载清单文件"""
        if not self.manifest_path.exists():
            self._entries = {}
            return
        
        try:
            data = json.loads(self.manifest_path.read_text(encoding="utf-8"))
            self._entries = {
                k: ManifestEntry(**v) for k, v in data.get("entries", {}).items()
            }
        except (json.JSONDecodeError, ValueError) as e:
            logger.warning(f"Failed to load manifest: {e}")
            self._entries = {}
    
    def _save(self) -> None:
        """保存清单文件"""
        self.generated_dir.mkdir(parents=True, exist_ok=True)
        
        data = {
            "version": "1.0.0",
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "entries": {
                k: v.model_dump(mode="json") for k, v in self._entries.items()
            }
        }
        
        self.manifest_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
    
    def add_entry(
        self,
        source_file: str,
        output_file: str,
        source_hash: str,
        output_hash: str,
        generator_type: GeneratorType,
        engine_id: str,
        version: str,
    ) -> ManifestEntry:
        """添加或更新清单条目"""
        entry = ManifestEntry(
            source_file=source_file,
            output_file=output_file,
            source_hash=source_hash,
            output_hash=output_hash,
            generator_type=generator_type,
            engine_id=engine_id,
            version=version,
        )
        
        self._entries[source_file] = entry
        self._save()
        
        return entry
    
    def get_entry(self, source_file: str) -> Optional[ManifestEntry]:
        """获取清单条目"""
        return self._entries.get(source_file)
    
    def remove_entry(self, source_file: str) -> bool:
        """移除清单条目"""
        if source_file in self._entries:
            del self._entries[source_file]
            self._save()
            return True
        return False
    
    def get_all_entries(self) -> Dict[str, ManifestEntry]:
        """获取所有条目"""
        return self._entries.copy()
    
    def get_entries_by_type(self, generator_type: GeneratorType) -> List[ManifestEntry]:
        """按类型获取条目"""
        return [e for e in self._entries.values() if e.generator_type == generator_type]
    
    def get_entries_by_engine(self, engine_id: str) -> List[ManifestEntry]:
        """按引擎获取条目"""
        return [e for e in self._entries.values() if e.engine_id == engine_id]
    
    def needs_recompile(self, source_file: str, current_hash: str) -> bool:
        """检查是否需要重新编译"""
        entry = self._entries.get(source_file)
        if not entry:
            return True
        return entry.is_stale(current_hash)
    
    def find_orphans(self) -> List[Path]:
        """
        查找孤儿文件（不在清单中的生成文件）
        
        Returns:
            孤儿文件路径列表
        """
        orphans = []
        
        # 遍历生成目录
        for subdir in ["rules", "factors", "semantics"]:
            dir_path = self.generated_dir / subdir
            if not dir_path.exists():
                continue
            
            for py_file in dir_path.glob("*.py"):
                if py_file.name.startswith("_"):
                    continue
                
                # 检查是否在清单中
                rel_path = str(py_file.relative_to(self.generated_dir))
                is_tracked = any(
                    e.output_file == rel_path or e.output_file.endswith(py_file.name)
                    for e in self._entries.values()
                )
                
                if not is_tracked:
                    orphans.append(py_file)
        
        return orphans
    
    def clean_orphans(self, dry_run: bool = True) -> List[Path]:
        """
        清理孤儿文件
        
        Args:
            dry_run: True 时只返回列表不删除
        
        Returns:
            清理的文件列表
        """
        orphans = self.find_orphans()
        
        if not dry_run:
            for orphan in orphans:
                orphan.unlink()
                logger.info(f"Deleted orphan: {orphan}")
        
        return orphans
    
    def get_status(self) -> Dict[str, Any]:
        """获取清单状态"""
        return {
            "total_entries": len(self._entries),
            "by_type": {
                "rule": len(self.get_entries_by_type("rule")),
                "factor": len(self.get_entries_by_type("factor")),
                "semantic": len(self.get_entries_by_type("semantic")),
            },
            "manifest_path": str(self.manifest_path),
            "orphans": len(self.find_orphans()),
        }
