"""
SemanticCodeGenerator - 语义代码生成器

将精校 Markdown 编译为 Python SemanticEntry 模块。
对照 semantic-core spec Requirements 6.1-6.6

核心功能:
- 解析 L1/L2/L2.5 Markdown 块
- 处理 trigger 和 factor_trigger 双字段
- 生成带 @SemanticRegistry.register 装饰器的 Python 模块
- 支持增量编译和错误报告
"""

from __future__ import annotations

import concurrent.futures
import hashlib
import json
import logging
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from scripts.codegen.engine_mapping import (
    ENGINE_BOOK_MAPPING,
    SOURCE_PATH_MAPPING,
    BOOK_ABBR,
    get_book_abbr,
    infer_engine_id as mapping_infer_engine_id,
    infer_primary_lang as mapping_infer_primary_lang,
)

from scripts.codegen.base import BaseCodeGenerator
from scripts.codegen.exceptions import CompilationError, ValidationError

from backend.core.contracts import (
    FACTOR_ID_PATTERN,
    SNIPPET_ID_PATTERN,
    SnippetRole,
)

logger = logging.getLogger(__name__)


class SemanticCodeGenerator(BaseCodeGenerator):
    """
    语义代码生成器
    
    对照 Requirements 6.1-6.6
    
    输入: 精校 Markdown（L1/L2/L2.5 结构）
    输出: Python SemanticEntry 模块（带 @SemanticRegistry.register 装饰器）
    """
    
    OUTPUT_DIR = Path("backend/semantics")
    MANIFEST_FILE = ".codegen_manifest.json"
    
    # -------------------------------------------------------------------------
    # Markdown 解析正则 (Task 13.3-13.6)
    # 支持两种格式:
    # 1. ## L1 / ## L2 / ## L2.5 (标题格式)
    # 2. <!-- L1_BEGIN --> / <!-- L1_END --> (注释格式)
    # -------------------------------------------------------------------------
    
    # L1 区块 - 格式1: ## L1 原文 ... (直到 ## L2 或 ## L2.5)
    L1_BLOCK_PATTERN_HEADER = re.compile(
        r'## L1[^\n]*\n(.*?)(?=## L2|## L2\.5|---|\Z)',
        re.DOTALL
    )
    # L1 区块 - 格式2: <!-- L1_BEGIN --> ... <!-- L1_END -->
    L1_BLOCK_PATTERN_COMMENT = re.compile(
        r'<!-- L1_BEGIN -->(.*?)<!-- L1_END -->',
        re.DOTALL
    )
    
    # L2 区块 - 格式1: ## L2 语义 ... (直到 ## L2.5 或结束)
    L2_BLOCK_PATTERN_HEADER = re.compile(
        r'## L2[^\n]*\n(.*?)(?=## L2\.5|---|\Z)',
        re.DOTALL
    )
    # L2 区块 - 格式2: <!-- L2_BEGIN --> ... <!-- L2_END -->
    L2_BLOCK_PATTERN_COMMENT = re.compile(
        r'<!-- L2_BEGIN -->(.*?)<!-- L2_END -->',
        re.DOTALL
    )
    
    # L2.5 区块 - 格式1: ## L2.5 桥接层 ...
    L25_BLOCK_PATTERN_HEADER = re.compile(
        r'(?:## L2\.5|#### L2\.5)[^\n]*\n(.*?)(?=---|\Z|###\s+\d+\.)',
        re.DOTALL
    )
    # L2.5 区块 - 格式2: <!-- L25_BEGIN --> ... <!-- L25_END -->
    L25_BLOCK_PATTERN_COMMENT = re.compile(
        r'<!-- L25_BEGIN -->(.*?)<!-- L25_END -->',
        re.DOTALL
    )
    
    # 叙事素材正则 (Task 13.6)
    # 格式: [ns_xxx_001] [trigger: 人话] [factor_trigger: factor_id] [role: 角色] 文本 → 来源
    NARRATIVE_SNIPPET_PATTERN = re.compile(
        r'\[([a-z][a-z0-9_]*_\d{3})\]\s*'
        r'(?:\[trigger:\s*([^\]]*)\]\s*)?'
        r'(?:\[factor_trigger:\s*([^\]]*)\]\s*)?'
        r'\[role:\s*([^\]]+)\]\s*'
        r'(.+?)\s*→\s*(.+?)$',
        re.MULTILINE
    )
    
    # 因子表正则
    FACTOR_TABLE_PATTERN = re.compile(
        r'\|\s*([a-z][a-z0-9_]*)\s*\|',
        re.MULTILINE
    )
    
    # 因子关系表正则
    RELATION_TABLE_PATTERN = re.compile(
        r'\|\s*(rel_[a-z0-9_]+_\d{3})\s*\|\s*([a-z][a-z0-9_]*)\s*\|\s*'
        r'([a-z][a-z0-9_]*)\s*\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|',
        re.MULTILINE
    )
    
    # 证据链表正则
    EVIDENCE_TABLE_PATTERN = re.compile(
        r'\|\s*(evi_[a-z0-9_]+_\d{3})\s*\|\s*([^\|]+)\s*\|\s*([^\|]+)\s*\|\s*([高中低])\s*\|',
        re.MULTILINE
    )
    
    # 因子本体缓存
    _factor_ontology: Optional[Set[str]] = None
    
    def __init__(self, output_dir: Optional[Path] = None):
        if output_dir is None:
            output_dir = self.OUTPUT_DIR
        super().__init__(output_dir)
        self._manifest: Dict[str, str] = {}
        self._errors: List[CompilationError] = []
        self._load_manifest()
    
    # -------------------------------------------------------------------------
    # Manifest 管理 (Task 13.2)
    # -------------------------------------------------------------------------
    
    def _load_manifest(self) -> None:
        """加载编译清单"""
        manifest_path = self.output_dir / self.MANIFEST_FILE
        if manifest_path.exists():
            try:
                with open(manifest_path, encoding="utf-8") as f:
                    self._manifest = json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load manifest: {e}")
                self._manifest = {}
    
    def _save_manifest(self) -> None:
        """保存编译清单"""
        manifest_path = self.output_dir / self.MANIFEST_FILE
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(self._manifest, f, indent=2)
    
    def _compute_hash(self, content: str) -> str:
        """计算内容哈希"""
        return hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]
    
    # -------------------------------------------------------------------------
    # 因子本体验证 (Task 13.9-13.10)
    # -------------------------------------------------------------------------
    
    @classmethod
    def _load_factor_ontology(cls) -> Set[str]:
        """
        加载因子本体用于验证
        
        优先从 data/factor_ontology/certified/ 加载，支持 by_category 格式
        """
        if cls._factor_ontology is not None:
            return cls._factor_ontology
        
        cls._factor_ontology = set()
        certified_path = Path("data/factor_ontology/certified")
        
        # 从 certified 目录加载 (by_category 格式)
        if certified_path.exists():
            import yaml
            for yaml_file in certified_path.glob("**/*.yaml"):
                try:
                    with open(yaml_file, encoding="utf-8") as f:
                        data = yaml.safe_load(f)
                    
                    if not isinstance(data, dict):
                        continue
                    
                    # by_category 格式
                    if "by_category" in data:
                        for category, factors in data["by_category"].items():
                            if isinstance(factors, list):
                                for factor in factors:
                                    if isinstance(factor, dict) and "id" in factor:
                                        cls._factor_ontology.add(factor["id"])
                except Exception as e:
                    logger.warning(f"Failed to load factor ontology from {yaml_file}: {e}")
        
        # 备用: 从旧格式文件加载
        if not cls._factor_ontology:
            ontology_path = Path("典籍/因子本体_总览_v1.md")
            if ontology_path.exists():
                try:
                    content = ontology_path.read_text(encoding="utf-8")
                    factor_pattern = re.compile(r'\|\s*([a-z][a-z0-9_]*)\s*\|')
                    cls._factor_ontology = set(factor_pattern.findall(content))
                except Exception as e:
                    logger.warning(f"Failed to load factor ontology: {e}")
        
        if cls._factor_ontology:
            logger.info(f"Loaded {len(cls._factor_ontology)} factors from ontology")
        else:
            logger.warning("Factor ontology not found, skipping validation")
        
        return cls._factor_ontology
    
    def _validate_factor_id(self, factor_id: str, file_path: str) -> bool:
        """验证 factor_id 格式和存在性"""
        # 格式验证
        if not re.match(FACTOR_ID_PATTERN, factor_id):
            self._errors.append(CompilationError(
                error_type="FORMAT_ERROR",
                message=f"Invalid factor_id format: {factor_id}",
                details={"file": file_path, "suggestion": f"Must match: {FACTOR_ID_PATTERN}"}
            ))
            return False
        
        # 因子本体验证 (Req 9.3)
        ontology = self._load_factor_ontology()
        if ontology and factor_id not in ontology:
            logger.warning(
                f"[{file_path}] factor_id '{factor_id}' not in ontology (new_candidate)"
            )
        
        return True
    
    # -------------------------------------------------------------------------
    # BaseCodeGenerator 接口实现
    # -------------------------------------------------------------------------
    
    def validate(self, source: Dict[str, Any]) -> List[str]:
        """校验语义配置"""
        errors = []
        for field in ["l1", "l2"]:
            if field not in source:
                errors.append(f"Missing required field: {field}")
        return errors
    
    def compile(self, source: Dict[str, Any]) -> str:
        """编译解析后的数据为 Python 代码"""
        return self._generate_python_module(
            source,
            source.get("book_id", "unknown"),
            source.get("engine_id", "bazi"),
            source.get("version", "1.0.0"),
        )
    
    # -------------------------------------------------------------------------
    # 编译入口 (Task 14.1)
    # -------------------------------------------------------------------------
    
    def compile_file(
        self,
        md_path: Path,
        book_id: str,
        engine_id: Optional[str] = None,
        version: str = "1.0.0",
        entry_counters: Optional[Dict[Tuple[str, str, str], int]] = None,
    ) -> Tuple[Optional[str], List[CompilationError]]:
        """
        编译单个 Markdown 文件
        
        对照 Requirements 6.6
        
        Args:
            md_path: Markdown 文件路径
            book_id: 书籍 ID
            engine_id: 引擎 ID（可选，自动推断）
            version: 版本号
        
        Returns:
            (生成的 Python 代码, 错误列表)
        """
        self._errors = []
        
        content = md_path.read_text(encoding="utf-8")
        
        # 检查是否需要重新编译（增量编译）
        content_hash = self._compute_hash(content)
        if str(md_path) in self._manifest and self._manifest[str(md_path)] == content_hash:
            logger.info(f"Skipping {md_path} (unchanged)")
            return None, []
        
        # 推断 engine_id
        if engine_id is None:
            engine_id = self._infer_engine_id(book_id)
        
        # 解析 Markdown
        parsed = self._parse_markdown(content, str(md_path))
        parsed["book_id"] = book_id
        parsed["engine_id"] = engine_id
        parsed["version"] = version
        
        if self._errors:
            return None, self._errors
        
        # 生成语义 ID 与 Python 代码
        semantic_id = self._next_semantic_id(
            book_id=book_id,
            version=version,
            subject=parsed.get("subject", "topic"),
            counters=entry_counters or {},
        )
        code = self._generate_python_module(parsed, book_id, engine_id, version, semantic_id)
        
        # 更新清单
        self._manifest[str(md_path)] = content_hash
        
        return code, self._errors
    
    def compile_file_multi_entry(
        self,
        md_path: Path,
        book_id: str,
        engine_id: Optional[str] = None,
        version: str = "1.0.0",
        entry_counters: Optional[Dict[Tuple[str, str, str], int]] = None,
        dry_run: bool = False,
    ) -> Tuple[List[Tuple[str, str]], List[CompilationError]]:
        """
        编译包含多条目的 Markdown 文件
        
        Args:
            md_path: Markdown 文件路径
            book_id: 书籍 ID
            engine_id: 引擎 ID（可选，自动推断）
            version: 版本号
        
        Returns:
            ([(entry_id, code), ...], 错误列表)
        """
        self._errors = []
        results: List[Tuple[str, str]] = []
        entry_counters = entry_counters or {}
        
        try:
            content = md_path.read_text(encoding="utf-8")
        except Exception as e:
            self._errors.append(CompilationError(
                error_type="READ_ERROR",
                message=str(e),
                details={"file": str(md_path)},
            ))
            return [], self._errors
        
        content_hash = self._compute_hash(content)
        manifest_key = str(md_path)
        
        if not dry_run and manifest_key in self._manifest and self._manifest[manifest_key] == content_hash:
            logger.info(f"Skipping {md_path} (unchanged)")
            return [], []
        
        # 推断 engine_id
        if engine_id is None:
            engine_id = self._infer_engine_id(book_id)
        
        # 多条目解析
        entries = self._parse_markdown_multi_entry(content, str(md_path))
        
        if not entries:
            logger.warning(f"No entries found in {md_path}")
            if not dry_run:
                self._manifest[manifest_key] = content_hash
            return [], self._errors
        
        logger.info(f"  Found {len(entries)} entries in {md_path.name}")
        
        for entry in entries:
            entry["book_id"] = book_id
            entry["engine_id"] = engine_id
            entry["version"] = version
            
            semantic_id = self._next_semantic_id(
                book_id=book_id,
                version=version,
                subject=entry.get("subject", "topic"),
                counters=entry_counters,
            )
            
            # 生成 Python 代码
            code = self._generate_python_module(entry, book_id, engine_id, version, semantic_id)
            entry_id = semantic_id
            results.append((entry_id, None if dry_run else code))
        
        if not dry_run:
            self._manifest[manifest_key] = content_hash
        
        return results, self._errors
    
    def _infer_engine_id(self, book_id: str) -> str:
        """根据 book_id 推断 engine_id (Task 14.4)"""
        return mapping_infer_engine_id(book_id)
    
    def _next_semantic_id(
        self,
        book_id: str,
        version: str,
        subject: str,
        counters: Dict[Tuple[str, str, str], int],
    ) -> str:
        """
        生成下一个 semantic_id (P3 修复)
        
        格式: {book_abbr}_v{version}_{theme}_{seq:03d}
        例如: wt_v1.0.0_the_fool_001
        
        Args:
            book_id: 书籍 ID
            version: 版本号 (x.y.z)
            subject: 条目主题
            counters: (book_abbr, version, theme) -> 计数器
        
        Returns:
            符合规范的 semantic_id
        """
        book_abbr = get_book_abbr(book_id)
        theme = self._sanitize_topic(subject)
        
        # 生成计数器键
        counter_key = (book_abbr, version, theme)
        
        # 获取并递增序号
        seq = counters.get(counter_key, 0) + 1
        counters[counter_key] = seq
        
        return f"{book_abbr}_v{version}_{theme}_{seq:03d}"
    
    # -------------------------------------------------------------------------
    # Markdown 解析 (Task 13.3-13.6)
    # -------------------------------------------------------------------------
    
    # 条目拆分正则 - 基于 L1_BEGIN 标记
    # 每个 <!-- L1_BEGIN --> 标记一个独立条目的开始
    L1_ENTRY_SPLIT_PATTERN = re.compile(
        r'(?=<!--\s*L1_BEGIN\s*-->)',
        re.MULTILINE | re.IGNORECASE
    )
    
    # 标题提取 - 向前搜索最近的 ##/###/#### 标题
    # 支持格式：
    #   ### 1. 标题
    #   ## I. The Magician (魔术师)
    #   ## Ch1 – Why Bother?
    #   ### 六己日甲子时
    #   #### 1. People Can Change
    # 排除：L1/L2/L2.5/Key Term Analysis 等技术标题
    ENTRY_TITLE_PATTERN = re.compile(
        r'^#{2,4}\s+(?:(?:\d+|[IVXLC]+|Ch\d+)[.\s–\-]+)?(.+?)$',
        re.MULTILINE
    )
    
    # 技术标题（非条目标题）
    SKIP_TITLE_PATTERNS = {
        'L1', 'L2', 'L2.5', 'Key Term Analysis', 'Core Points',
        'Detailed Explanation', 'Textual Criticism', 'Bridge Layer',
        'Semantic Extraction', '桥接层', '因子', '关系', '证据链',
    }
    
    def _parse_markdown(self, content: str, file_path: str) -> Dict[str, Any]:
        """
        解析 Markdown 内容（单条目模式，向后兼容）
        
        对照 Requirements 6.1
        支持两种格式: 标题格式 (## L1) 和 注释格式 (<!-- L1_BEGIN -->)
        """
        result: Dict[str, Any] = {
            "l1": {},
            "l2": {},
            "l25": {},
            "narrative_snippets": [],
            "factor_refs": [],
        }
        
        # 解析 L1 区块 (Task 13.3) - 支持两种格式
        l1_match = self.L1_BLOCK_PATTERN_COMMENT.search(content)
        if not l1_match:
            l1_match = self.L1_BLOCK_PATTERN_HEADER.search(content)
        
        # 容错处理：如果有 L1_BEGIN 但没有 L1_END，提取到 L2_BEGIN 或文件末尾
        if not l1_match and "<!-- L1_BEGIN -->" in content:
            l1_start = content.find("<!-- L1_BEGIN -->") + len("<!-- L1_BEGIN -->")
            # 找到下一个分隔符
            l2_start = content.find("<!-- L2_BEGIN -->", l1_start)
            l1_end_alt = content.find("<!-- L1_END -->", l1_start)
            
            if l2_start > 0:
                l1_content = content[l1_start:l2_start]
            elif l1_end_alt > 0:
                l1_content = content[l1_start:l1_end_alt]
            else:
                l1_content = content[l1_start:]
            
            result["l1"] = self._parse_l1_block(l1_content)
        elif l1_match:
            result["l1"] = self._parse_l1_block(l1_match.group(1))
        
        # 解析 L2 区块 (Task 13.4) - 支持两种格式
        l2_match = self.L2_BLOCK_PATTERN_COMMENT.search(content)
        if not l2_match:
            l2_match = self.L2_BLOCK_PATTERN_HEADER.search(content)
        
        # 容错处理：如果有 L2_BEGIN 但没有 L2_END
        if not l2_match and "<!-- L2_BEGIN -->" in content:
            l2_start = content.find("<!-- L2_BEGIN -->") + len("<!-- L2_BEGIN -->")
            l2_end_alt = content.find("<!-- L2_END -->", l2_start)
            l25_start = content.find("#### L2.5", l2_start)
            next_l1 = content.find("<!-- L1_BEGIN -->", l2_start)
            
            # 找到最近的结束位置
            end_pos = len(content)
            for pos in [l2_end_alt, l25_start, next_l1]:
                if pos > 0 and pos < end_pos:
                    end_pos = pos
            
            l2_content = content[l2_start:end_pos]
            l2_data = self._parse_l2_block(l2_content, file_path)
            result["l2"] = l2_data
            result["factor_refs"] = l2_data.get("factors", [])
        elif l2_match:
            l2_data = self._parse_l2_block(l2_match.group(1), file_path)
            result["l2"] = l2_data
            result["factor_refs"] = l2_data.get("factors", [])
        
        # 解析 L2.5 区块 (Task 13.5) - 支持两种格式
        l25_match = self.L25_BLOCK_PATTERN_COMMENT.search(content)
        if not l25_match:
            l25_match = self.L25_BLOCK_PATTERN_HEADER.search(content)
        if l25_match:
            result["l25"] = self._parse_l25_block(l25_match.group(1), file_path)
        
        # 解析叙事素材 (Task 13.6)
        result["narrative_snippets"] = self._parse_narrative_snippets(content, file_path)
        
        # 提取主题
        result["subject"] = self._extract_subject(content)
        
        return result
    
    def _parse_markdown_multi_entry(self, content: str, file_path: str) -> List[Dict[str, Any]]:
        """
        解析 Markdown 内容 - 多条目模式
        
        精校文件格式：每个 <!-- L1_BEGIN --> 标记一个独立条目的开始
        向前搜索最近的 ### 标题作为条目名称
        
        Returns:
            条目列表，每个条目包含 subject, l1, l2, l25, narrative_snippets, factor_refs
        """
        entries: List[Dict[str, Any]] = []
        
        # 找到所有 L1_BEGIN 的位置
        l1_starts = [m.start() for m in re.finditer(r'<!--\s*L1_BEGIN\s*-->', content, re.IGNORECASE)]
        
        if not l1_starts:
            # 无 L1_BEGIN，尝试旧格式解析
            single = self._parse_markdown(content, file_path)
            if single["l1"].get("original_text") or single["l2"].get("normalized_text_zh"):
                entries.append(single)
            return entries
        
        # 找到所有 ### 标题的位置和内容
        title_matches = list(self.ENTRY_TITLE_PATTERN.finditer(content))
        
        for i, l1_pos in enumerate(l1_starts):
            # 确定条目结束位置：下一个 L1_BEGIN 或文件末尾
            end_pos = l1_starts[i + 1] if i + 1 < len(l1_starts) else len(content)
            
            # 提取条目内容
            entry_content = content[l1_pos:end_pos]
            
            # 找到 L1_BEGIN 之前最近的有效标题（跳过技术标题）
            entry_title = ""
            for tm in reversed(title_matches):
                if tm.start() < l1_pos:
                    candidate = tm.group(1).strip()
                    # 跳过技术标题
                    if not any(skip in candidate for skip in self.SKIP_TITLE_PATTERNS):
                        entry_title = candidate
                        break
            
            # 如果没找到前置标题，尝试从条目内容中提取（跳过技术标题）
            if not entry_title:
                for tm in self.ENTRY_TITLE_PATTERN.finditer(entry_content):
                    candidate = tm.group(1).strip()
                    if not any(skip in candidate for skip in self.SKIP_TITLE_PATTERNS):
                        entry_title = candidate
                        break
            
            # 解析单条目
            entry = self._parse_markdown(entry_content, file_path)
            entry["subject"] = entry_title or entry.get("subject", f"entry_{i+1}")
            
            if entry["l1"].get("original_text") or entry["l2"].get("normalized_text_zh"):
                entries.append(entry)
        
        return entries
    
    def _parse_l1_block(self, content: str) -> Dict[str, Any]:
        """解析 L1 区块 (Task 13.3)"""
        return {"original_text": content.strip()}
    
    def _parse_l2_block(self, content: str, file_path: str) -> Dict[str, Any]:
        """解析 L2 区块 (Task 13.4)"""
        result: Dict[str, Any] = {"normalized_text_zh": "", "factors": []}
        
        # 提取释义
        lines = content.split("\n")
        for i, line in enumerate(lines):
            if "释义" in line or "**释义**" in line:
                # 取下一行或 : 后的内容
                if ":" in line:
                    result["normalized_text_zh"] = line.split(":", 1)[1].strip()
                elif i + 1 < len(lines):
                    result["normalized_text_zh"] = lines[i + 1].strip()
                break
        
        # 提取因子表
        factors = self.FACTOR_TABLE_PATTERN.findall(content)
        for factor_id in factors:
            if factor_id not in ("factor_id", "说明"):  # 跳过表头
                if self._validate_factor_id(factor_id, file_path):
                    result["factors"].append(factor_id)
        
        return result
    
    def _parse_l25_block(self, content: str, file_path: str) -> Dict[str, Any]:
        """解析 L2.5 区块 (Task 13.5)"""
        result: Dict[str, Any] = {"relations": [], "evidence": [], "cross_system": []}
        
        # 因子关系表
        for match in self.RELATION_TABLE_PATTERN.finditer(content):
            try:
                result["relations"].append({
                    "relation_id": match.group(1),
                    "factor_a": match.group(2),
                    "factor_b": match.group(3),
                    "relation_nature": match.group(4).strip(),
                    "effect_direction": match.group(5).strip(),
                })
            except Exception as e:
                self._errors.append(CompilationError(
                    error_type="PARSE_ERROR",
                    message=f"Failed to parse relation: {e}",
                    details={"file": file_path}
                ))
        
        # 证据链表
        for match in self.EVIDENCE_TABLE_PATTERN.finditer(content):
            try:
                factors = [f.strip() for f in match.group(3).split(",")]
                result["evidence"].append({
                    "evidence_id": match.group(1),
                    "l1_anchor": match.group(2).strip(),
                    "involved_factors": factors,
                    "confidence": match.group(4).strip(),
                })
            except Exception as e:
                self._errors.append(CompilationError(
                    error_type="PARSE_ERROR",
                    message=f"Failed to parse evidence: {e}",
                    details={"file": file_path}
                ))
        
        return result
    
    def _parse_narrative_snippets(
        self, content: str, file_path: str
    ) -> List[Dict[str, Any]]:
        """
        解析叙事素材 (Task 13.6)
        
        对照 Requirements 6.3 - 处理 trigger 和 factor_trigger 双字段
        """
        snippets: List[Dict[str, Any]] = []
        
        for match in self.NARRATIVE_SNIPPET_PATTERN.finditer(content):
            snippet_id = match.group(1)
            trigger_human = match.group(2) or ""
            factor_trigger = match.group(3) or ""
            role_str = match.group(4).strip()
            snippet_text = match.group(5).strip()
            source_ref = match.group(6).strip()
            
            # 验证 snippet_id 格式
            if not re.match(SNIPPET_ID_PATTERN, snippet_id):
                self._errors.append(CompilationError(
                    error_type="FORMAT_ERROR",
                    message=f"Invalid snippet_id: {snippet_id}",
                    details={"file": file_path}
                ))
                continue
            
            # 验证 role
            try:
                role = SnippetRole(role_str)
            except ValueError:
                self._errors.append(CompilationError(
                    error_type="ENUM_ERROR",
                    message=f"Invalid role: {role_str}",
                    details={"file": file_path, "valid_roles": [r.value for r in SnippetRole]}
                ))
                continue
            
            # 处理 trigger 和 factor_trigger 双字段 (Req 6.3)
            trigger_condition = factor_trigger
            if not factor_trigger and trigger_human:
                logger.warning(
                    f"[{snippet_id}] factor_trigger empty, trigger_human='{trigger_human}'"
                )
                trigger_condition = ""
            
            # 提取 related_factors
            related_factors = []
            if factor_trigger:
                related_factors = re.findall(r"[a-z][a-z0-9_]*", factor_trigger.lower())
            
            snippets.append({
                "snippet_id": snippet_id,
                "trigger_human": trigger_human,
                "trigger_condition": trigger_condition,
                "role": role,
                "snippet_text": snippet_text,
                "source_ref": source_ref,
                "related_factors": related_factors,
            })
        
        return snippets
    
    def _extract_subject(self, content: str) -> str:
        """从内容提取主题"""
        # 尝试从 # 标题提取
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        return "unknown_topic"
    
    # -------------------------------------------------------------------------
    # Python 代码生成 (Task 13.11-13.14)
    # -------------------------------------------------------------------------
    
    def _generate_python_module(
        self,
        parsed: Dict[str, Any],
        book_id: str,
        engine_id: str,
        version: str,
        semantic_id: str,
    ) -> str:
        """
        生成 Python 模块代码
        
        对照 Requirements 6.4
        """
        topic = self._sanitize_topic(parsed.get("subject", "topic"))
        
        # 生成叙事素材代码
        snippets_code = self._generate_snippets_code(
            parsed.get("narrative_snippets", []), book_id, engine_id, version
        )
        
        # 生成 L2.5 关系代码
        relations_code = self._generate_relations_code(
            parsed.get("l25", {}).get("relations", []), book_id, engine_id, version
        )
        
        # 生成证据链代码
        evidence_code = self._generate_evidence_code(
            parsed.get("l25", {}).get("evidence", []), book_id, engine_id, version
        )
        
        # 转义原文中的三引号
        original_text = parsed.get("l1", {}).get("original_text", "").replace('"""', '\\"\\"\\"')
        normalized_text = parsed.get("l2", {}).get("normalized_text_zh", "").replace('"""', '\\"\\"\\"')
        
        class_name = self._to_class_name(topic)
        
        code = f'''"""
Auto-generated semantic module for {book_id}
Generated at: {datetime.now().isoformat()}
Version: {version}

对照 Requirements 6.4 - 带 @SemanticRegistry.register 装饰器的 Python 模块
"""

from backend.semantics.core.base import SemanticEntry, SemanticRegistry, NarrativeSnippetExtended
from backend.core.contracts import (
    SnippetRole,
    SourceMetadata,
    ConfigRelation,
    EvidenceChainEntry,
    RelationType,
    EffectDirection,
    ConfidenceLevel,
)


@SemanticRegistry.register(
    semantic_id="{semantic_id}",
    book_id="{book_id}",
    engine_id="{engine_id}"
)
class {class_name}(SemanticEntry):
    """
    {original_text[:100]}...
    """
    
    original_text: str = """{original_text}"""
    normalized_text_zh: str = """{normalized_text}"""
    subject: str = "{parsed.get('subject', topic)}"
    factor_refs: list = {parsed.get("factor_refs", [])!r}
    
    # 叙事素材（包含 trigger_human）
    narrative_snippets: list = [
{snippets_code}
    ]
    
    # L2.5 因子关系
    related_semantics: list = [
{relations_code}
    ]
    
    # L2.5 证据链
    evidence_refs: list = [
{evidence_code}
    ]
    
    metadata: SourceMetadata = SourceMetadata(
        book_id="{book_id}",
        chapter="",
        l1_anchor="{semantic_id}_L1",
    )
    version: str = "{version}"
'''
        return code
    
    def _generate_snippets_code(
        self, snippets: List[Dict], book_id: str, engine_id: str, version: str
    ) -> str:
        """生成叙事素材代码 (Task 13.12)"""
        lines = []
        for s in snippets:
            role_name = s["role"].name if hasattr(s["role"], "name") else str(s["role"])
            lines.append(f'''        NarrativeSnippetExtended(
            snippet_id="{s['snippet_id']}",
            trigger_condition="{s['trigger_condition']}",
            trigger_human="{s.get('trigger_human', '')}",
            role=SnippetRole.{role_name},
            primary_lang="zh-CN",
            snippet_text="{s['snippet_text']}",
            source_ref="{s['source_ref']}",
            related_factors={s.get('related_factors', [])!r},
            metadata=SourceMetadata(book_id="{book_id}", chapter="", l1_anchor=""),
            version="{version}",
            engine_id="{engine_id}",
        ),''')
        return "\n".join(lines)
    
    def _generate_relations_code(
        self, relations: List[Dict], book_id: str, engine_id: str, version: str
    ) -> str:
        """生成 L2.5 因子关系代码 (Task 13.13)"""
        effect_map = {
            "增益": "BENEFICIAL", "损害": "HARMFUL", "限制": "RESTRICTIVE",
            "中性": "NEUTRAL", "混合": "MIXED"
        }
        lines = []
        for rel in relations:
            effect = effect_map.get(rel.get("effect_direction", "中性"), "NEUTRAL")
            lines.append(f'''        ConfigRelation(
            relation_id="{rel['relation_id']}",
            relation_type=RelationType.WUXING_SHENGKE,
            factor_a="{rel['factor_a']}",
            factor_b="{rel['factor_b']}",
            relation_nature="{rel['relation_nature']}",
            effect_direction=EffectDirection.{effect},
            source_ref="《{book_id}》",
            metadata=SourceMetadata(book_id="{book_id}", chapter="", l1_anchor=""),
            version="{version}",
            engine_id="{engine_id}",
        ),''')
        return "\n".join(lines)
    
    def _generate_evidence_code(
        self, evidence: List[Dict], book_id: str, engine_id: str, version: str
    ) -> str:
        """生成 L2.5 证据链代码 (Task 13.14)"""
        conf_map = {"高": "HIGH", "中": "MEDIUM", "低": "LOW"}
        lines = []
        for evi in evidence:
            conf = conf_map.get(evi.get("confidence", "中"), "MEDIUM")
            lines.append(f'''        EvidenceChainEntry(
            evidence_id="{evi['evidence_id']}",
            l1_anchor="{evi['l1_anchor']}",
            involved_factors={evi['involved_factors']!r},
            reasoning_step="",
            conclusion_direction="",
            confidence=ConfidenceLevel.{conf},
            can_generate_rule=False,
            source_ref="《{book_id}》",
            metadata=SourceMetadata(book_id="{book_id}", chapter="", l1_anchor=""),
            version="{version}",
            engine_id="{engine_id}",
        ),''')
        return "\n".join(lines)
    
    def _sanitize_topic(self, topic: str) -> str:
        """清理主题名为有效标识符"""
        # 移除非字母数字字符，转小写
        sanitized = re.sub(r"[^a-zA-Z0-9_\u4e00-\u9fff]", "_", topic)
        sanitized = sanitized.lower().strip("_")
        return sanitized[:30] if sanitized else "topic"
    
    def _to_class_name(self, topic: str) -> str:
        """转换为类名"""
        # 拼音转换或直接使用英文
        words = topic.replace("_", " ").split()
        return "".join(word.capitalize() for word in words) or "SemanticTopic"
    
    # -------------------------------------------------------------------------
    # 批量编译 (Task 14.2-14.3)
    # -------------------------------------------------------------------------
    
    # 排除的目录和文件模式
    EXCLUDE_DIRS = {"原文", "archive", "备份", "backup", "旧版", "old"}
    EXCLUDE_FILE_PATTERNS = {"_原文", "_raw", "_backup", "_old"}
    EXCLUDE_FILE_NAMES = {"README.md", "readme.md", "INDEX.md", "index.md", "TODO.md", "CHANGELOG.md"}
    
    def compile_book(
        self,
        book_id: str,
        source_dir: Path,
        primary_lang: str = "zh-CN",
    ) -> Tuple[int, int, List[CompilationError]]:
        """
        编译整本书 - 多条目模式 (Task 14.2)
        
        Args:
            book_id: 书籍 ID
            source_dir: 源文件目录
            primary_lang: 主语言 (Task 18.2: "zh-CN" 或 "en-US")
        
        Returns:
            (总条目数, 成功条目数, 错误列表)
        """
        all_errors: List[CompilationError] = []
        total_entries = 0
        success_entries = 0
        
        for md_file in source_dir.glob("**/*.md"):
            # 跳过以 _ 开头的文件
            if md_file.name.startswith("_"):
                continue
            
            # 跳过排除目录
            if any(exclude in md_file.parts for exclude in self.EXCLUDE_DIRS):
                logger.debug(f"Skipping excluded dir: {md_file}")
                continue
            
            # 跳过排除文件模式
            if any(pattern in md_file.name for pattern in self.EXCLUDE_FILE_PATTERNS):
                logger.debug(f"Skipping excluded file: {md_file}")
                continue
            
            # 跳过排除文件名
            if md_file.name in self.EXCLUDE_FILE_NAMES:
                logger.debug(f"Skipping excluded filename: {md_file}")
                continue
            
            # 检查是否为精校文件（包含 L1_BEGIN 或 ## L1）
            try:
                content = md_file.read_text(encoding="utf-8")
                if "<!-- L1_BEGIN -->" not in content and "## L1" not in content:
                    logger.debug(f"Skipping non-refined file: {md_file}")
                    continue
            except Exception as e:
                logger.warning(f"Error reading {md_file}: {e}")
                continue
            
            # 多条目编译
            results, errors = self.compile_file_multi_entry(
                md_file,
                book_id=book_id,
                engine_id=self._infer_engine_id(book_id),
            )
            all_errors.extend(errors)
            
            for entry_id, code in results:
                total_entries += 1
                if code:
                    output_path = self.output_dir / book_id / f"{entry_id}.py"
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    output_path.write_text(code, encoding="utf-8")
                    success_entries += 1
                    logger.debug(f"Generated: {output_path}")
        
        self._save_manifest()
        logger.info(f"  {book_id}: {success_entries}/{total_entries} entries generated")
        return total_entries, success_entries, all_errors
    
    def compile_all(self) -> Dict[str, List[CompilationError]]:
        """编译所有 25 本典籍 (Task 14.3)"""
        results: Dict[str, List[CompilationError]] = {}
        
        # 中文典籍 (Task 18.2: primary_lang="zh-CN")
        zh_base = Path("典籍/中文典籍")
        if zh_base.exists():
            for book_dir in zh_base.iterdir():
                if book_dir.is_dir() and not book_dir.name.startswith("_"):
                    book_id = book_dir.name
                    results[book_id] = self.compile_book(book_id, book_dir, primary_lang="zh-CN")
        
        # 英文典籍 (Task 18.2: primary_lang="en-US")
        en_base = Path("典籍/texts")
        if en_base.exists():
            for book_dir in en_base.iterdir():
                if book_dir.is_dir() and not book_dir.name.startswith("_"):
                    book_id = book_dir.name.lower().replace(" ", "_")
                    results[book_id] = self.compile_book(book_id, book_dir, primary_lang="en-US")
        
        return results
    
    # -------------------------------------------------------------------------
    # 向后兼容接口 (保持 CLI 兼容)
    # -------------------------------------------------------------------------
    
    def compile_markdown_file(
        self,
        md_path: Path,
        semantic_id: str,
        engine_id: str,
        version: str = "1.0.0",
    ) -> str:
        """
        从 Markdown 文件编译语义模块（向后兼容接口）
        
        这是为保持与 cli.py 兼容而保留的旧接口。
        新代码应使用 compile_file() 方法。
        
        Args:
            md_path: Markdown 文件路径
            semantic_id: 语义 ID（现映射为 book_id 前缀）
            engine_id: 引擎 ID
            version: 版本号
        
        Returns:
            生成的 Python 代码
        """
        # 从 semantic_id 推断 book_id
        book_id = semantic_id.split("_")[0] if "_" in semantic_id else semantic_id
        
        code, errors = self.compile_file(md_path, book_id, engine_id, version)
        
        if errors:
            logger.warning(f"Compilation warnings for {md_path}: {len(errors)} error(s)")
            for err in errors:
                logger.warning(f"  - {err}")
        
        # 如果增量编译跳过（返回 None），重新强制编译
        if code is None:
            # 清除该文件的 manifest 记录，强制重新编译
            self._manifest.pop(str(md_path), None)
            code, errors = self.compile_file(md_path, book_id, engine_id, version)
        
        return code or ""
    
    # -------------------------------------------------------------------------
    # 反编译 (Task 14.5)
    # -------------------------------------------------------------------------
    
    def decompile(self, python_module_path: Path) -> str:
        """
        从 Python SemanticEntry 类提取数据，输出为 Markdown
        
        对照 Requirements 10.3
        """
        import importlib.util
        
        spec = importlib.util.spec_from_file_location("module", python_module_path)
        if spec is None or spec.loader is None:
            return ""
        
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # 导入 SemanticEntry 类型检查
        from backend.semantics.core.base import SemanticEntry as SEBase
        
        for name, obj in vars(module).items():
            if isinstance(obj, type) and issubclass(obj, SEBase) and obj is not SEBase:
                instance = obj()
                return instance.to_markdown()
        
        return ""


# -----------------------------------------------------------------------------
# SemanticMigrationTool - 语义迁移工具 (Task 1.5, tasks.md)
# -----------------------------------------------------------------------------

class SemanticMigrationTool:
    """
    语义迁移工具 - CLI 接口
    
    对齐 design.md Components and Interfaces §1, tasks.md 1.5
    
    用法:
    - python -m scripts.codegen.semantic_generator migrate --book <book_id>
    - python -m scripts.codegen.semantic_generator migrate --engine <engine_id>
    - python -m scripts.codegen.semantic_generator migrate --all
    """
    
    def __init__(self):
        from scripts.codegen.engine_mapping import (
            ENGINE_BOOK_MAPPING,
            SOURCE_PATH_MAPPING,
            infer_engine_id,
            infer_primary_lang,
        )
        from scripts.codegen.models import (
            MigrationResult,
            MigrationStatus,
            ValidationErrorModel,
            create_migration_result,
        )
        from scripts.codegen.reporter import MigrationReporter
        from scripts.codegen.validation import MigrationValidator
        
        self.generator = SemanticCodeGenerator()
        self.validator = MigrationValidator()
        self.reporter = MigrationReporter()
        
        # 缓存导入
        self._ENGINE_BOOK_MAPPING = ENGINE_BOOK_MAPPING
        self._SOURCE_PATH_MAPPING = SOURCE_PATH_MAPPING
        self._infer_engine_id = infer_engine_id
        self._infer_primary_lang = infer_primary_lang
        self._MigrationResult = MigrationResult
        self._MigrationStatus = MigrationStatus
        self._ValidationErrorModel = ValidationErrorModel
        self._create_migration_result = create_migration_result
    
    def migrate_book(
        self,
        book_id: str,
        dry_run: bool = False,
    ) -> "MigrationResult":
        """
        迁移单本书籍 - 多条目模式
        
        Args:
            book_id: 书籍 ID
            dry_run: 仅验证不生成文件
        
        Returns:
            MigrationResult
        """
        import time
        start_time = time.time()
        
        source_path_str = self._SOURCE_PATH_MAPPING.get(book_id)
        if not source_path_str:
            logger.error(f"Unknown book_id: {book_id}")
            return self._create_migration_result(
                book_id=book_id,
                engine_id="unknown",
                entries_total=0,
                entries_success=0,
                entries_failed=0,
            )
        
        source_path = Path(source_path_str)
        if not source_path.exists():
            logger.error(f"Source path not found: {source_path}")
            return self._create_migration_result(
                book_id=book_id,
                engine_id=self._infer_engine_id(book_id),
                entries_total=0,
                entries_success=0,
                entries_failed=0,
            )
        
        engine_id = self._infer_engine_id(book_id)
        primary_lang = self._infer_primary_lang(book_id)
        
        logger.info(f"Migrating {book_id} (engine={engine_id}, lang={primary_lang})")
        
        errors: List[self._ValidationErrorModel] = []
        warnings: List[str] = []
        output_files: List[str] = []
        
        if dry_run:
            # dry-run 模式：使用多条目解析统计
            entries_total = 0
            entries_success = 0
            entries_failed = 0
            
            for md_file in source_path.glob("**/*.md"):
                if md_file.name.startswith("_"):
                    continue
                if any(exclude in md_file.parts for exclude in self.generator.EXCLUDE_DIRS):
                    continue
                if any(pattern in md_file.name for pattern in self.generator.EXCLUDE_FILE_PATTERNS):
                    continue
                if md_file.name in self.generator.EXCLUDE_FILE_NAMES:
                    continue
                
                try:
                    content = md_file.read_text(encoding="utf-8")
                    if "<!-- L1_BEGIN -->" not in content and "## L1" not in content:
                        continue
                    
                    # 多条目解析
                    parsed_entries = self.generator._parse_markdown_multi_entry(content, str(md_file))
                    
                    for entry in parsed_entries:
                        entries_total += 1
                        entry["book_id"] = book_id
                        entry["engine_id"] = engine_id
                        
                        entry_errors = self.validator.validate_entry(entry, str(md_file))
                        
                        if any(e.severity == "ERROR" for e in entry_errors):
                            entries_failed += 1
                            for e in entry_errors:
                                if e.severity == "ERROR":
                                    errors.append(self._ValidationErrorModel(
                                        file=e.file, line=e.line, column=e.column,
                                        error_type=e.error_type, message=e.message,
                                        suggestion=e.suggestion, severity=e.severity,
                                    ))
                        else:
                            entries_success += 1
                            for e in entry_errors:
                                if e.severity == "WARNING":
                                    warnings.append(str(e))
                except Exception as e:
                    entries_failed += 1
                    errors.append(self._ValidationErrorModel(
                        file=str(md_file), line=1, column=1,
                        error_type="EXCEPTION", message=str(e),
                        suggestion="请检查文件格式", severity="ERROR",
                    ))
        else:
            # 实际编译：使用 compile_book 方法
            entries_total, entries_success, comp_errors = self.generator.compile_book(
                book_id, source_path, primary_lang
            )
            entries_failed = entries_total - entries_success
            
            for e in comp_errors:
                errors.append(self._ValidationErrorModel(
                    file="", line=1, column=1,
                    error_type=e.error_type, message=e.message,
                    suggestion=e.details.get("suggestion", "") if e.details else "",
                    severity="ERROR",
                ))
        
        duration_ms = (time.time() - start_time) * 1000
        
        result = self._create_migration_result(
            book_id=book_id,
            engine_id=engine_id,
            entries_total=entries_total,
            entries_success=entries_success,
            entries_failed=entries_failed,
            errors=errors,
            warnings=warnings,
            output_files=output_files,
            duration_ms=duration_ms,
        )
        
        self.reporter.add_result(result)
        return result
    
    def migrate_engine(
        self,
        engine_id: str,
        dry_run: bool = False,
    ) -> Dict[str, "MigrationResult"]:
        """
        迁移整个体系
        
        Args:
            engine_id: 引擎 ID
            dry_run: 仅验证不生成文件
        
        Returns:
            {book_id: MigrationResult}
        """
        books = self._ENGINE_BOOK_MAPPING.get(engine_id, [])
        if not books:
            logger.error(f"Unknown engine_id: {engine_id}")
            return {}
        
        results: Dict[str, "MigrationResult"] = {}
        for book_id in books:
            results[book_id] = self.migrate_book(book_id, dry_run=dry_run)
        
        return results
    
    def migrate_all(
        self,
        dry_run: bool = False,
        parallel: int = 1,
    ) -> Dict[str, "MigrationResult"]:
        """
        迁移所有 24 本典籍
        
        Args:
            dry_run: 仅验证不生成文件
            parallel: 并行度 (1=串行, >1=并行)
        
        Returns:
            {book_id: MigrationResult}
        """
        # 从 SOURCE_PATH_MAPPING 获取书籍列表
        book_ids = list(SOURCE_PATH_MAPPING.keys())
        results: Dict[str, "MigrationResult"] = {}
        
        if parallel <= 1:
            # 串行模式
            for book_id in book_ids:
                results[book_id] = self.migrate_book(book_id, dry_run=dry_run)
        else:
            # 并行模式
            with concurrent.futures.ThreadPoolExecutor(max_workers=parallel) as executor:
                future_to_book = {
                    executor.submit(self.migrate_book, book_id, dry_run): book_id
                    for book_id in book_ids
                }
                for future in concurrent.futures.as_completed(future_to_book):
                    book_id = future_to_book[future]
                    try:
                        results[book_id] = future.result()
                    except Exception as e:
                        logger.error(f"Error migrating {book_id}: {e}")
                        results[book_id] = MigrationResult(
                            book_id=book_id,
                            status="failed",
                            files_total=0,
                            files_success=0,
                            files_failed=1,
                            entries_total=0,
                            entries_success=0,
                            entries_failed=0,
                            errors=[str(e)],
                            warnings=[],
                            output_files=[],
                            duration_ms=0,
                        )
        
        return results
    
    def get_report(self) -> "MigrationReport":
        """获取迁移报告"""
        return self.reporter.generate_report()
    
    def print_report(self) -> None:
        """打印迁移报告"""
        report = self.get_report()
        print(self.reporter.format_report(report))


# =============================================================================
# CLI 入口 (P1 修复)
# =============================================================================

def main() -> None:
    """
    CLI 入口点
    
    用法:
        python -m scripts.codegen.semantic_generator migrate --book waite_tarot
        python -m scripts.codegen.semantic_generator migrate --engine tarot
        python -m scripts.codegen.semantic_generator migrate --all
        python -m scripts.codegen.semantic_generator migrate --all --parallel 4
        python -m scripts.codegen.semantic_generator migrate --book dts --dry-run
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Semantic Layer 代码生成器 - 将精校 Markdown 编译为 Python SemanticEntry 模块",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s migrate --book waite_tarot           # 迁移单本书
  %(prog)s migrate --engine tarot               # 迁移整个体系
  %(prog)s migrate --all                        # 迁移全部 24 本
  %(prog)s migrate --all --parallel 4           # 并行迁移（4线程）
  %(prog)s migrate --book dts --dry-run         # 干运行（仅验证）
        """,
    )
    
    subparsers = parser.add_subparsers(dest="command", help="子命令")
    
    # migrate 子命令
    migrate_parser = subparsers.add_parser(
        "migrate",
        help="迁移精校典籍到 Python 模块",
        description="将 Markdown 精校典籍编译为 Python SemanticEntry 模块",
    )
    
    # 互斥参数组: --book, --engine, --all
    scope_group = migrate_parser.add_mutually_exclusive_group(required=True)
    scope_group.add_argument(
        "--book",
        type=str,
        metavar="BOOK_ID",
        help="迁移单本书 (如: waite_tarot, dts, sanming)",
    )
    scope_group.add_argument(
        "--engine",
        type=str,
        metavar="ENGINE_ID",
        help="迁移整个体系 (如: bazi, tarot, astro, dream, ziwei, yijing, psych)",
    )
    scope_group.add_argument(
        "--all",
        action="store_true",
        help="迁移全部 24 本典籍",
    )
    
    # 可选参数
    migrate_parser.add_argument(
        "--dry-run",
        action="store_true",
        dest="dry_run",
        help="干运行模式：仅验证不生成文件",
    )
    migrate_parser.add_argument(
        "--parallel",
        type=int,
        default=1,
        metavar="N",
        help="并行度 (默认: 1，串行执行)",
    )
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        return
    
    if args.command == "migrate":
        # 配置日志
        logging.basicConfig(
            level=logging.INFO,
            format="%(levelname)-5s: %(message)s",
        )
        
        tool = SemanticMigrationTool()
        
        if args.book:
            # 迁移单本书
            if args.book not in SOURCE_PATH_MAPPING:
                logger.error(f"Unknown book_id: {args.book}")
                logger.info(f"Available books: {', '.join(SOURCE_PATH_MAPPING.keys())}")
                return
            result = tool.migrate_book(args.book, dry_run=args.dry_run)
            tool.reporter.add_result(result)
            
        elif args.engine:
            # 迁移整个体系
            if args.engine not in ENGINE_BOOK_MAPPING:
                logger.error(f"Unknown engine_id: {args.engine}")
                logger.info(f"Available engines: {', '.join(ENGINE_BOOK_MAPPING.keys())}")
                return
            results = tool.migrate_engine(args.engine, dry_run=args.dry_run)
            
        elif args.all:
            # 迁移全部
            results = tool.migrate_all(dry_run=args.dry_run, parallel=args.parallel)
        
        # 打印报告
        tool.print_report()


if __name__ == "__main__":
    main()
