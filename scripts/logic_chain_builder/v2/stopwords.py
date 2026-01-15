"""
StopwordsFilter - L1 停用词过滤器

过滤逻辑操作符和无意义词，确保只保留有意义的因子。
"""

from typing import FrozenSet, Set

from scripts.logic_chain_builder.logging_config import get_logger

logger = get_logger(__name__)


class StopwordsFilter:
    """
    停用词过滤器 (L1)
    
    过滤英文和中文停用词，确保因子集合只包含有意义的内容。
    """
    
    ENGLISH_STOPWORDS: FrozenSet[str] = frozenset({
        # Logical operators (both cases)
        "and", "or", "not", "if", "then", "but", "nor", "yet", "so",
        "AND", "OR", "NOT", "IF", "THEN",
        # Articles
        "the", "a", "an",
        # Prepositions
        "in", "on", "of", "to", "for", "with", "at", "by", "from",
        "into", "through", "as",
        # Verbs
        "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did",
        "will", "would", "could", "should", "may", "might", "must", "shall",
        # Pronouns
        "it", "its", "this", "that", "these", "those",
        # Other
        "when", "where", "which", "who", "whom", "whose", "what", "how",
    })
    
    CHINESE_STOPWORDS: FrozenSet[str] = frozenset({
        "和", "或", "如果", "则", "不", "的", "是", "在", "有", "为",
        "与", "及", "而", "但", "却", "若", "虽", "因", "故", "所以",
        "以及", "并且", "或者", "之", "者", "也",
        "这", "那", "其", "此", "彼",
    })
    
    def __init__(
        self,
        additional_english: Set[str] = None,
        additional_chinese: Set[str] = None
    ):
        """
        初始化停用词过滤器
        
        Args:
            additional_english: 额外的英文停用词
            additional_chinese: 额外的中文停用词
        """
        self._english = self.ENGLISH_STOPWORDS | (additional_english or set())
        self._chinese = self.CHINESE_STOPWORDS | (additional_chinese or set())
    
    def is_stopword(self, word: str) -> bool:
        """
        检查词是否为停用词
        
        Args:
            word: 要检查的词
            
        Returns:
            True如果是停用词
        """
        if not word:
            return True
        
        word_stripped = word.strip()
        
        # 空字符串或单字符视为停用词
        if len(word_stripped) <= 1:
            return True
        
        # 检查英文停用词（大小写不敏感）
        if word_stripped in self._english or word_stripped.lower() in self._english:
            return True
        
        # 检查中文停用词
        if word_stripped in self._chinese:
            return True
        
        return False
    
    def filter_factors(self, factors: Set[str]) -> Set[str]:
        """
        过滤掉停用词，只保留有意义的因子
        
        Args:
            factors: 原始因子集合
            
        Returns:
            过滤后的因子集合
        """
        return {f for f in factors if not self.is_stopword(f)}
    
    def has_meaningful_factors(self, factors: Set[str]) -> bool:
        """
        检查因子集合是否包含至少一个有意义的因子
        
        Args:
            factors: 因子集合
            
        Returns:
            True如果包含至少一个非停用词因子
        """
        return len(self.filter_factors(factors)) > 0


# 导出
__all__ = ["StopwordsFilter"]
