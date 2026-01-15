"""Factor Updater - 精校文档因子状态更新工具

批量将精校文档中的 new_candidate 更新为 existing，并填充正式的 factor_id。
"""

import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import yaml


@dataclass
class UpdateResult:
    """更新结果"""
    file_path: str
    blocks_updated: int = 0
    factors_updated: int = 0
    errors: List[str] = field(default_factory=list)


@dataclass 
class UpdateReport:
    """更新报告"""
    total_files: int = 0
    files_updated: int = 0
    total_blocks: int = 0
    total_factors_updated: int = 0
    results: List[UpdateResult] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)


class FactorUpdater:
    """精校文档因子更新器
    
    将 new_candidate 因子更新为 existing 状态。
    """
    
    FACTOR_BEGIN = "<!-- FACTOR_BEGIN -->"
    FACTOR_END = "<!-- FACTOR_END -->"
    
    def __init__(self, certified_dir: Path, dry_run: bool = False):
        """初始化更新器
        
        Args:
            certified_dir: 认证因子目录
            dry_run: 是否只模拟运行，不实际修改文件
        """
        self.certified_dir = certified_dir
        self.dry_run = dry_run
        self.factor_mapping: Dict[str, Dict] = {}  # label -> certified factor
        
        # 加载认证因子映射
        self._load_certified_factors()
    
    def _load_certified_factors(self):
        """加载认证因子，建立标签到因子的映射"""
        for yaml_file in self.certified_dir.glob("*_certified.yaml"):
            try:
                with open(yaml_file, encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                
                if not data or "by_category" not in data:
                    continue
                
                system = data.get("system", "unknown")
                
                for category, factors in data["by_category"].items():
                    for factor in factors:
                        label = factor.get("display_zh", "")
                        if label:
                            # 使用 (label, system) 作为键避免跨体系冲突
                            key = f"{label}|{system}"
                            self.factor_mapping[key] = factor
                            # 也用纯标签作为备用
                            if label not in self.factor_mapping:
                                self.factor_mapping[label] = factor
            except Exception as e:
                print(f"警告: 加载 {yaml_file} 失败: {e}")
    
    def update_file(self, md_path: Path) -> UpdateResult:
        """更新单个文件
        
        Args:
            md_path: Markdown文件路径
            
        Returns:
            UpdateResult: 更新结果
        """
        result = UpdateResult(file_path=str(md_path))
        
        try:
            content = md_path.read_text(encoding="utf-8")
        except Exception as e:
            result.errors.append(f"读取文件失败: {e}")
            return result
        
        # 查找并更新因子块
        updated_content, blocks_count, factors_count = self._update_factor_blocks(
            content, md_path
        )
        
        result.blocks_updated = blocks_count
        result.factors_updated = factors_count
        
        # 写入更新后的内容
        if factors_count > 0 and not self.dry_run:
            try:
                md_path.write_text(updated_content, encoding="utf-8")
            except Exception as e:
                result.errors.append(f"写入文件失败: {e}")
        
        return result
    
    def update_all(self, root_dir: Path) -> UpdateReport:
        """更新目录下所有精校文档
        
        Args:
            root_dir: 根目录
            
        Returns:
            UpdateReport: 更新报告
        """
        report = UpdateReport()
        
        # 查找所有Markdown文件
        md_files = list(root_dir.rglob("*.md"))
        report.total_files = len(md_files)
        
        for md_path in md_files:
            # 跳过非编辑目录的文件
            if "编辑" not in str(md_path) and "edit" not in str(md_path).lower():
                continue
            
            # 检查文件是否包含因子标记
            try:
                content = md_path.read_text(encoding="utf-8")
                if self.FACTOR_BEGIN not in content:
                    continue
            except Exception:
                continue
            
            result = self.update_file(md_path)
            report.results.append(result)
            
            if result.factors_updated > 0:
                report.files_updated += 1
            
            report.total_blocks += result.blocks_updated
            report.total_factors_updated += result.factors_updated
            
            if result.errors:
                report.errors.extend(result.errors)
        
        return report
    
    def _update_factor_blocks(
        self, content: str, md_path: Path
    ) -> Tuple[str, int, int]:
        """更新文件中的因子块
        
        Args:
            content: 文件内容
            md_path: 文件路径（用于推断体系）
            
        Returns:
            Tuple[str, int, int]: (更新后内容, 块数, 更新因子数)
        """
        lines = content.split("\n")
        updated_lines = []
        
        in_block = False
        block_lines = []
        blocks_count = 0
        total_factors_updated = 0
        
        # 推断体系
        system = self._infer_system(str(md_path))
        
        for line in lines:
            if self.FACTOR_BEGIN in line:
                in_block = True
                block_lines = [line]
                blocks_count += 1
            elif self.FACTOR_END in line:
                if in_block:
                    block_lines.append(line)
                    # 更新块内容
                    updated_block, factors_updated = self._update_block(
                        block_lines, system
                    )
                    updated_lines.extend(updated_block)
                    total_factors_updated += factors_updated
                else:
                    updated_lines.append(line)
                in_block = False
                block_lines = []
            elif in_block:
                block_lines.append(line)
            else:
                updated_lines.append(line)
        
        return "\n".join(updated_lines), blocks_count, total_factors_updated
    
    def _update_block(
        self, block_lines: List[str], system: str
    ) -> Tuple[List[str], int]:
        """更新因子块
        
        Args:
            block_lines: 块内容行
            system: 术数体系
            
        Returns:
            Tuple[List[str], int]: (更新后的行, 更新因子数)
        """
        updated_lines = []
        factors_updated = 0
        
        header_found = False
        header_idx = -1
        
        for i, line in enumerate(block_lines):
            # 检查是否是表头行
            if not header_found and "|" in line and ("因子" in line or "Factor" in line):
                header_found = True
                header_idx = i
                updated_lines.append(line)
                continue
            
            # 跳过分隔线
            if header_found and i == header_idx + 1 and line.strip().startswith("|--"):
                updated_lines.append(line)
                continue
            
            # 更新数据行
            if header_found and "|" in line and "new_candidate" in line:
                updated_line, updated = self._update_row(line, system)
                updated_lines.append(updated_line)
                if updated:
                    factors_updated += 1
            else:
                updated_lines.append(line)
        
        return updated_lines, factors_updated
    
    def _update_row(self, row: str, system: str) -> Tuple[str, bool]:
        """更新数据行
        
        Args:
            row: 数据行
            system: 术数体系
            
        Returns:
            Tuple[str, bool]: (更新后的行, 是否更新)
        """
        if "new_candidate" not in row:
            return row, False
        
        # 解析单元格
        cells = row.split("|")
        if len(cells) < 5:
            return row, False
        
        # 查找标签列（通常是第2列）
        label = None
        label_idx = -1
        for i, cell in enumerate(cells):
            cell_stripped = cell.strip()
            if cell_stripped and i > 0 and i < len(cells) - 1:
                # 跳过因子类型列
                if any(t in cell_stripped for t in ["类", "Type", "类型"]):
                    continue
                # 跳过因子来源列
                if cell_stripped in ["existing", "new_candidate"]:
                    continue
                # 可能是标签
                if label is None:
                    label = cell_stripped
                    label_idx = i
                    break
        
        if not label:
            return row, False
        
        # 查找认证因子
        key = f"{label}|{system}"
        certified = self.factor_mapping.get(key) or self.factor_mapping.get(label)
        
        if not certified:
            return row, False
        
        # 更新因子来源和ID
        new_cells = []
        for i, cell in enumerate(cells):
            cell_stripped = cell.strip()
            if cell_stripped == "new_candidate":
                new_cells.append(" existing ")
            elif i == label_idx + 1 and not cell_stripped:
                # 填充factor_id到下一个空单元格
                new_cells.append(f" {certified['id']} ")
            else:
                new_cells.append(cell)
        
        return "|".join(new_cells), True
    
    def _infer_system(self, path: str) -> str:
        """推断术数体系"""
        path_lower = path.lower()
        
        if "中文典籍" in path_lower:
            if "三命通会" in path_lower or "滴天髓" in path_lower or \
               "渊海子平" in path_lower or "子平真诠" in path_lower or \
               "穷通宝鉴" in path_lower:
                return "bazi"
            if "紫微" in path_lower:
                return "ziwei"
            if "周易" in path_lower:
                return "yijing"
            if "解梦" in path_lower or "梦林" in path_lower:
                return "dream"
        elif "texts" in path_lower:
            if "astro" in path_lower or "inner sky" in path_lower or \
               "tetrabiblos" in path_lower or "planets in transit" in path_lower or \
               "christian astrology" in path_lower:
                return "astro"
            if "tarot" in path_lower or "thoth" in path_lower or \
               "78 degrees" in path_lower:
                return "tarot"
            if "dream" in path_lower or "freud" in path_lower or \
               "jung" in path_lower:
                return "dream"
        
        return "unknown"
