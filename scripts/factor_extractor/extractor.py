"""Factor Extractor - 因子提取器

从精校Markdown文档中提取因子表格，支持中英文文档格式。
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .models import (
    DivinationSystem,
    ExtractionResult,
    FactorCandidate,
    FactorExtractionReport,
)


class FactorExtractor:
    """因子提取器
    
    从精校Markdown文档中提取FACTOR_BEGIN到FACTOR_END之间的因子表格。
    """
    
    # 因子块标记
    FACTOR_BEGIN = "<!-- FACTOR_BEGIN -->"
    FACTOR_END = "<!-- FACTOR_END -->"
    
    # 表头列名映射（中英文）
    COLUMN_MAPPINGS = {
        # 中文列名
        "因子类型": "factor_type",
        "因子标签（人话）": "factor_label",
        "因子标签": "factor_label",
        "因子ID（如已存在）": "factor_id",
        "因子ID": "factor_id",
        "因子来源": "factor_source",
        "角色/位置": "role_position",
        "角色": "role_position",
        "位置": "role_position",
        "取值/约束": "value_constraints",
        "取值": "value_constraints",
        "约束": "value_constraints",
        "engine_id": "engine_id",
        "备注": "notes",
        # 英文列名
        "Factor Type": "factor_type",
        "Factor Label": "factor_label",
        "Factor Label (Human-readable)": "factor_label",
        "Factor ID": "factor_id",
        "Factor ID (if exists)": "factor_id",
        "Factor Source": "factor_source",
        "Role/Position": "role_position",
        "Role": "role_position",
        "Position": "role_position",
        "Value/Constraints": "value_constraints",
        "Value": "value_constraints",
        "Constraints": "value_constraints",
        "Notes": "notes",
    }
    
    def __init__(self, verbose: bool = False):
        """初始化提取器
        
        Args:
            verbose: 是否输出详细日志
        """
        self.verbose = verbose
    
    def extract_from_file(self, md_path: Path) -> ExtractionResult:
        """从单个文件提取因子
        
        Args:
            md_path: Markdown文件路径
            
        Returns:
            ExtractionResult: 提取结果
        """
        result = ExtractionResult(file_path=str(md_path))
        
        try:
            content = md_path.read_text(encoding="utf-8")
        except Exception as e:
            result.parse_errors.append(f"读取文件失败: {e}")
            return result
        
        # 查找所有因子块
        blocks = self._find_factor_blocks(content)
        result.block_count = len(blocks)
        
        for block_idx, (start, end, block_content) in enumerate(blocks):
            try:
                factors = self._parse_factor_block(block_content, str(md_path), block_idx)
                for factor in factors:
                    result.add_factor(factor)
            except Exception as e:
                result.parse_errors.append(
                    f"解析因子块{block_idx}失败 (行{start}): {e}"
                )
        
        return result
    
    def extract_all(self, root_dir: Path) -> FactorExtractionReport:
        """扫描目录下所有精校文档，提取因子
        
        Args:
            root_dir: 根目录
            
        Returns:
            FactorExtractionReport: 提取报告
        """
        report = FactorExtractionReport()
        report.root_directory = str(root_dir)
        report.extraction_time = datetime.now().isoformat()
        
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
            
            if self.verbose:
                print(f"处理: {md_path}")
            
            result = self.extract_from_file(md_path)
            report.add_result(result)
        
        return report
    
    def classify_by_status(
        self, factors: List[FactorCandidate]
    ) -> Dict[str, List[FactorCandidate]]:
        """按状态分类因子
        
        Args:
            factors: 因子列表
            
        Returns:
            Dict: 按状态分类的因子字典
        """
        classified = {
            "existing": [],
            "new_candidate": [],
        }
        
        for factor in factors:
            if factor.is_existing:
                classified["existing"].append(factor)
            else:
                classified["new_candidate"].append(factor)
        
        return classified
    
    def classify_by_system(
        self, factors: List[FactorCandidate]
    ) -> Dict[str, List[FactorCandidate]]:
        """按术数体系分类因子
        
        Args:
            factors: 因子列表
            
        Returns:
            Dict: 按体系分类的因子字典
        """
        classified: Dict[str, List[FactorCandidate]] = {}
        
        for factor in factors:
            system = factor.infer_system().value
            if system not in classified:
                classified[system] = []
            classified[system].append(factor)
        
        return classified
    
    def _find_factor_blocks(self, content: str) -> List[Tuple[int, int, str]]:
        """查找所有因子块
        
        Args:
            content: 文件内容
            
        Returns:
            List[Tuple[int, int, str]]: (起始行号, 结束行号, 块内容) 列表
        """
        blocks = []
        lines = content.split("\n")
        
        in_block = False
        block_start = 0
        block_lines = []
        
        for i, line in enumerate(lines):
            if self.FACTOR_BEGIN in line:
                in_block = True
                block_start = i + 1
                block_lines = []
            elif self.FACTOR_END in line:
                if in_block:
                    blocks.append((block_start, i + 1, "\n".join(block_lines)))
                in_block = False
                block_lines = []
            elif in_block:
                block_lines.append(line)
        
        return blocks
    
    def _parse_factor_block(
        self, block_content: str, source_file: str, block_index: int
    ) -> List[FactorCandidate]:
        """解析因子块
        
        Args:
            block_content: 因子块内容
            source_file: 源文件路径
            block_index: 块索引
            
        Returns:
            List[FactorCandidate]: 解析出的因子列表
        """
        factors = []
        lines = block_content.strip().split("\n")
        
        if len(lines) < 2:
            return factors
        
        # 查找表头行
        header_line = None
        header_idx = 0
        for i, line in enumerate(lines):
            if "|" in line and ("因子" in line or "Factor" in line):
                header_line = line
                header_idx = i
                break
        
        if not header_line:
            return factors
        
        # 解析表头
        column_indices = self._parse_header(header_line)
        if not column_indices:
            return factors
        
        # 跳过分隔线
        data_start = header_idx + 2
        
        # 解析数据行
        for i, line in enumerate(lines[data_start:], start=data_start):
            if not line.strip() or line.strip().startswith("|--"):
                continue
            
            factor = self._parse_row(line, column_indices, source_file, block_index, i)
            if factor:
                factors.append(factor)
        
        return factors
    
    def _parse_header(self, header_line: str) -> Dict[str, int]:
        """解析表头，获取列索引
        
        Args:
            header_line: 表头行
            
        Returns:
            Dict[str, int]: 字段名到列索引的映射
        """
        cells = [c.strip() for c in header_line.split("|")]
        cells = [c for c in cells if c]  # 移除空单元格
        
        column_indices = {}
        for i, cell in enumerate(cells):
            # 尝试匹配已知列名
            for known_name, field_name in self.COLUMN_MAPPINGS.items():
                if known_name.lower() in cell.lower() or cell.lower() in known_name.lower():
                    column_indices[field_name] = i
                    break
        
        return column_indices
    
    def _parse_row(
        self,
        row_line: str,
        column_indices: Dict[str, int],
        source_file: str,
        block_index: int,
        line_offset: int,
    ) -> Optional[FactorCandidate]:
        """解析数据行
        
        Args:
            row_line: 数据行
            column_indices: 列索引映射
            source_file: 源文件
            block_index: 块索引
            line_offset: 行偏移
            
        Returns:
            Optional[FactorCandidate]: 解析出的因子，解析失败返回None
        """
        cells = [c.strip() for c in row_line.split("|")]
        cells = [c for c in cells if c or cells.index(c) == 0]  # 保留空单元格结构
        
        # 移除首尾空单元格
        if cells and not cells[0]:
            cells = cells[1:]
        if cells and not cells[-1]:
            cells = cells[:-1]
        
        def get_cell(field: str) -> Optional[str]:
            idx = column_indices.get(field)
            if idx is not None and idx < len(cells):
                val = cells[idx].strip()
                return val if val else None
            return None
        
        # 必填字段检查
        factor_type = get_cell("factor_type")
        factor_label = get_cell("factor_label")
        factor_source = get_cell("factor_source")
        
        if not factor_type or not factor_label or not factor_source:
            return None
        
        return FactorCandidate(
            factor_type=factor_type,
            factor_label=factor_label,
            factor_source=factor_source,
            factor_id=get_cell("factor_id"),
            role_position=get_cell("role_position"),
            value_constraints=get_cell("value_constraints"),
            engine_id=get_cell("engine_id"),
            notes=get_cell("notes"),
            source_file=source_file,
            line_number=line_offset,
            block_index=block_index,
        )
