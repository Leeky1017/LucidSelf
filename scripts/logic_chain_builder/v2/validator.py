"""
SourceDataValidator - L0 源数据完整性校验器

校验snippets和relations数据的完整性，识别数据质量问题。
"""

from typing import List, Set

from scripts.logic_chain_builder.loader import SchemaLoader
from scripts.logic_chain_builder.logging_config import get_logger
from scripts.logic_chain_builder.v2.models import (
    DataQualityIssue,
    ValidationReport,
)
from scripts.schema_extractor.models import ConfigRelation, NarrativeSnippet

logger = get_logger(__name__)


class SourceDataValidator:
    """
    源数据完整性校验器 (L0)
    
    负责校验:
    - snippet覆盖率
    - orphan relations检测
    - 缺失章节识别
    """
    
    MIN_SNIPPETS_THRESHOLD = 50  # 低于此数量标记为incomplete
    
    def __init__(self, loader: SchemaLoader = None):
        """
        初始化校验器
        
        Args:
            loader: SchemaLoader实例，用于加载数据
        """
        self.loader = loader or SchemaLoader()
    
    def validate_book(self, book_id: str) -> ValidationReport:
        """
        校验单本书籍数据完整性
        
        Args:
            book_id: 书籍ID
            
        Returns:
            ValidationReport，包含校验结果和问题列表
        """
        issues: List[DataQualityIssue] = []
        orphan_relations: List[str] = []
        missing_chapters: List[str] = []
        
        # 加载数据
        try:
            snippets = self.loader.load_snippets(book_id)
        except FileNotFoundError:
            snippets = []
            issues.append(DataQualityIssue(
                type="missing_snippets_file",
                description=f"Snippets file not found for {book_id}",
                remediation=f"Run schema_extractor for {book_id}"
            ))
        
        try:
            relations = self.loader.load_relations(book_id)
        except FileNotFoundError:
            relations = []
            issues.append(DataQualityIssue(
                type="missing_relations_file",
                description=f"Relations file not found for {book_id}",
                remediation=f"Run schema_extractor for {book_id}"
            ))
        
        snippet_count = len(snippets)
        relation_count = len(relations)
        
        # 检查snippet数量阈值
        if snippet_count < self.MIN_SNIPPETS_THRESHOLD and relation_count > 0:
            issues.append(DataQualityIssue(
                type="incomplete_extraction",
                description=f"Only {snippet_count} snippets but {relation_count} relations. Expected >= {self.MIN_SNIPPETS_THRESHOLD} snippets.",
                remediation=f"Re-run schema_extractor for {book_id} with all chapters"
            ))
        
        # 检查orphan relations
        if snippets and relations:
            orphan_relations = self._detect_orphan_relations(snippets, relations)
            if orphan_relations:
                issues.append(DataQualityIssue(
                    type="orphan_relations",
                    description=f"Found {len(orphan_relations)} orphan relations (factors not in any snippet)",
                    remediation="Review relation definitions or re-extract snippets"
                ))
        
        # 检测缺失章节
        if snippets and relations:
            missing_chapters = self.detect_missing_chapters(snippets, relations)
            if missing_chapters:
                issues.append(DataQualityIssue(
                    type="missing_chapters",
                    description=f"Found {len(missing_chapters)} chapters with relations but no snippets: {missing_chapters[:5]}...",
                    remediation="Re-extract missing chapters"
                ))
        
        # 确定是否完整
        is_complete = (
            snippet_count >= self.MIN_SNIPPETS_THRESHOLD and
            len(orphan_relations) == 0 and
            len(missing_chapters) == 0
        )
        
        # 如果snippet很少但relation很多，明确标记为不完整
        if snippet_count < self.MIN_SNIPPETS_THRESHOLD and relation_count > 100:
            is_complete = False
        
        report = ValidationReport(
            book_id=book_id,
            is_complete=is_complete,
            snippet_count=snippet_count,
            relation_count=relation_count,
            missing_chapters=missing_chapters,
            orphan_relations=orphan_relations,
            issues=issues,
        )
        
        logger.info(
            f"Validated {book_id}: complete={is_complete}, "
            f"snippets={snippet_count}, relations={relation_count}, "
            f"issues={len(issues)}"
        )
        
        return report
    
    def _detect_orphan_relations(
        self,
        snippets: List[NarrativeSnippet],
        relations: List[ConfigRelation]
    ) -> List[str]:
        """
        检测孤儿关系（factor_a/b不在任何snippet中）
        
        Args:
            snippets: snippet列表
            relations: relation列表
            
        Returns:
            orphan relation描述列表
        """
        # 提取所有snippet中的factor
        snippet_factors = self._extract_all_factors(snippets)
        
        orphan_relations = []
        for rel in relations:
            factor_a_found = self._factor_exists(rel.factor_a, snippet_factors)
            factor_b_found = self._factor_exists(rel.factor_b, snippet_factors)
            
            if not factor_a_found:
                orphan_relations.append(f"{rel.relation_id}: factor_a={rel.factor_a} not found")
            if not factor_b_found:
                orphan_relations.append(f"{rel.relation_id}: factor_b={rel.factor_b} not found")
        
        return orphan_relations
    
    def _extract_all_factors(self, snippets: List[NarrativeSnippet]) -> Set[str]:
        """
        从所有snippet中提取factor
        
        Args:
            snippets: snippet列表
            
        Returns:
            factor集合
        """
        factors = set()
        for snippet in snippets:
            if snippet.factor_trigger:
                # 解析factor_trigger字段
                extracted = self._parse_factor_trigger(snippet.factor_trigger)
                factors.update(extracted)
        return factors
    
    def _parse_factor_trigger(self, factor_trigger: str) -> Set[str]:
        """
        解析factor_trigger字符串，提取因子
        
        处理格式如:
        - star_ziwei AND palace_life
        - star_ziwei AND (star_zuofu OR star_youbi)
        
        Args:
            factor_trigger: factor_trigger字符串
            
        Returns:
            因子集合
        """
        import re
        
        # 移除逻辑操作符和括号
        cleaned = factor_trigger
        for op in ['AND', 'OR', 'NOT', 'and', 'or', 'not', '(', ')']:
            cleaned = cleaned.replace(op, ' ')
        
        # 分割并清理
        tokens = cleaned.split()
        factors = {t.strip() for t in tokens if t.strip() and len(t.strip()) > 1}
        
        return factors
    
    def _factor_exists(self, factor: str, snippet_factors: Set[str]) -> bool:
        """
        检查factor是否存在于snippet_factors中
        
        支持部分匹配和规范化匹配
        
        Args:
            factor: 要查找的factor
            snippet_factors: snippet中的所有factor
            
        Returns:
            是否找到匹配
        """
        if not factor:
            return True  # 空factor视为存在
        
        factor_lower = factor.lower().strip()
        
        # 精确匹配
        if factor in snippet_factors or factor_lower in {f.lower() for f in snippet_factors}:
            return True
        
        # 部分匹配（factor可能是snippet_factor的一部分或反之）
        for sf in snippet_factors:
            sf_lower = sf.lower()
            if factor_lower in sf_lower or sf_lower in factor_lower:
                return True
        
        return False
    
    def detect_missing_chapters(
        self,
        snippets: List[NarrativeSnippet],
        relations: List[ConfigRelation]
    ) -> List[str]:
        """
        检测有relations但无snippets的章节
        
        Args:
            snippets: snippet列表
            relations: relation列表
            
        Returns:
            缺失章节列表
        """
        # 提取snippet中的章节
        snippet_chapters: Set[str] = set()
        for s in snippets:
            if s.source_ref:
                snippet_chapters.add(s.source_ref)
        
        # 提取relation中的章节
        relation_chapters: Set[str] = set()
        for rel in relations:
            if rel.source_ref:
                relation_chapters.add(rel.source_ref)
        
        # 找出缺失章节
        missing = relation_chapters - snippet_chapters
        
        return sorted(list(missing))


# 导出
__all__ = [
    "SourceDataValidator",
    "ValidationReport",
    "DataQualityIssue",
]
