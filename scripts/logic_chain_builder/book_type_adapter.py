"""
BookTypeAdapter - 根据典籍类型调整构建策略

根据书籍类型（命理、占卜、梦学、西方占星）提供不同的入口节点识别策略和论证模式。

**Validates: Requirements 11.1, 11.2, 11.3, 11.4, 11.5**
"""

from enum import Enum
from typing import Callable, Dict, List, Optional, Set

from scripts.logic_chain_builder.models import LogicNode, SnippetRole
from scripts.logic_chain_builder.constants import TARGET_BOOKS
from scripts.logic_chain_builder.logging_config import get_logger


logger = get_logger(__name__)


class BookType(str, Enum):
    """书籍类型枚举"""
    MINGLI = "命理"           # Chinese fate calculation
    DIVINATION = "占卜"       # Divination (I Ching, Tarot)
    DREAM = "梦学"            # Dream interpretation
    WESTERN_ASTROLOGY = "西方占星"  # Western astrology


# Book type classification mapping - all 21 books
BOOK_TYPE_MAP: Dict[BookType, List[str]] = {
    BookType.MINGLI: [
        "滴天髓",
        "子平真诠",
        "穷通宝鉴",
        "渊海子平",
        "三命通会",
        "紫微斗数全书",
    ],
    BookType.DIVINATION: [
        "周易",
        "the_book_of_thoth",
        "78_degrees_of_wisdom",
        "waite_pictorial_key_to_the_tarot",
        "learning_the_tarot",
    ],
    BookType.DREAM: [
        "周公解梦",
        "the_interpretation_of_dreams",
        "llewellyns_complete_dictionary_of_dreams",
        "the_archetypes_and_the_collective_unconscious",
    ],
    BookType.WESTERN_ASTROLOGY: [
        "the_inner_sky",
        "planets_in_transit",
        "the_astrological_houses",
        "astrology_of_personality",
        "tetrabiblos",
        "christian_astrology,_vol._1_and_2",
    ],
}

# Reverse mapping: book_id -> BookType
_BOOK_TO_TYPE_MAP: Dict[str, BookType] = {}
for book_type, books in BOOK_TYPE_MAP.items():
    for book_id in books:
        _BOOK_TO_TYPE_MAP[book_id] = book_type


# Argument patterns for each book type
ARGUMENT_PATTERNS: Dict[BookType, str] = {
    BookType.MINGLI: "格局→用神→吉凶",
    BookType.DIVINATION: "符号→意象→诠释",
    BookType.DREAM: "象征→心理→解析",
    BookType.WESTERN_ASTROLOGY: "星体→宫位→相位→诠释",
}


# Entry node keywords for each book type
ENTRY_NODE_KEYWORDS: Dict[BookType, List[str]] = {
    BookType.MINGLI: ["格局", "日主", "月令", "八字", "命局", "命盘"],
    BookType.DIVINATION: ["符号", "卦", "卦象", "爻", "牌", "大阿卡纳", "小阿卡纳"],
    BookType.DREAM: ["象征", "梦境", "符号", "意象", "潜意识"],
    BookType.WESTERN_ASTROLOGY: ["星体", "行星", "宫位", "星座", "太阳", "月亮", "上升"],
}


class BookTypeAdapter:
    """
    根据典籍类型调整构建策略
    
    Provides book type classification and type-specific heuristics for:
    - Entry node identification
    - Argument pattern recognition
    
    **Validates: Requirements 11.1, 11.2, 11.3, 11.4, 11.5**
    """
    
    def __init__(self):
        """Initialize the adapter."""
        self._book_to_type = _BOOK_TO_TYPE_MAP.copy()
    
    def get_book_type(self, book_id: str) -> Optional[BookType]:
        """
        获取书籍类型
        
        Maps a book_id to one of the four book types:
        - 命理 (mingli): Chinese fate calculation
        - 占卜 (divination): Divination systems
        - 梦学 (dream): Dream interpretation
        - 西方占星 (western_astrology): Western astrology
        
        Args:
            book_id: 书籍标识符
            
        Returns:
            BookType enum value, or None if book_id is not recognized
            
        **Validates: Requirements 11.1**
        """
        return self._book_to_type.get(book_id)
    
    def get_book_type_str(self, book_id: str) -> str:
        """
        获取书籍类型字符串
        
        Args:
            book_id: 书籍标识符
            
        Returns:
            书籍类型字符串，未知书籍返回 "unknown"
        """
        book_type = self.get_book_type(book_id)
        return book_type.value if book_type else "unknown"
    
    def is_valid_book(self, book_id: str) -> bool:
        """
        检查书籍是否在21本目标书籍中
        
        Args:
            book_id: 书籍标识符
            
        Returns:
            True if book_id is one of the 21 target books
        """
        return book_id in self._book_to_type
    
    def get_all_books_for_type(self, book_type: BookType) -> List[str]:
        """
        获取指定类型的所有书籍
        
        Args:
            book_type: 书籍类型
            
        Returns:
            该类型下的所有书籍ID列表
        """
        return BOOK_TYPE_MAP.get(book_type, [])
    
    def get_argument_pattern(self, book_id: str) -> str:
        """
        获取书籍的论证模式
        
        Args:
            book_id: 书籍标识符
            
        Returns:
            论证模式字符串，如 "格局→用神→吉凶"
            
        **Validates: Requirements 11.2, 11.3, 11.4**
        """
        book_type = self.get_book_type(book_id)
        if book_type:
            return ARGUMENT_PATTERNS.get(book_type, "通用")
        return "通用"
    
    def get_entry_node_keywords(self, book_id: str) -> List[str]:
        """
        获取入口节点识别关键词
        
        Args:
            book_id: 书籍标识符
            
        Returns:
            入口节点关键词列表
        """
        book_type = self.get_book_type(book_id)
        if book_type:
            return ENTRY_NODE_KEYWORDS.get(book_type, [])
        return []
    
    def get_entry_node_heuristic(
        self, 
        book_id: str
    ) -> Callable[[LogicNode], float]:
        """
        获取入口节点识别启发式函数
        
        Returns a scoring function that evaluates how likely a node is to be
        an entry node based on book-type-specific heuristics.
        
        Args:
            book_id: 书籍标识符
            
        Returns:
            评分函数 (LogicNode) -> float，分数越高越可能是入口节点
            
        **Validates: Requirements 11.2, 11.3, 11.4, 11.5**
        """
        book_type = self.get_book_type(book_id)
        keywords = self.get_entry_node_keywords(book_id)
        
        def score_node(node: LogicNode) -> float:
            """Score a node for entry node candidacy."""
            score = 0.0
            
            # Base score from role
            if node.role == SnippetRole.MAIN:
                score += 1.0
            
            # Keyword matching in summary
            summary_lower = node.summary.lower() if node.summary else ""
            for keyword in keywords:
                if keyword.lower() in summary_lower or keyword in node.summary:
                    score += 0.5
                    break  # Only count once
            
            return score
        
        return score_node
    
    def score_entry_node(self, node: LogicNode, book_id: str) -> float:
        """
        评估节点作为入口节点的得分
        
        Convenience method that applies the entry node heuristic.
        
        Args:
            node: 待评估的节点
            book_id: 书籍标识符
            
        Returns:
            入口节点得分 (0.0 - 1.5+)
            
        **Validates: Requirements 11.2, 11.3, 11.4, 11.5**
        """
        heuristic = self.get_entry_node_heuristic(book_id)
        return heuristic(node)
    
    def is_entry_node_candidate(
        self, 
        node: LogicNode, 
        book_id: str,
        threshold: float = 0.5
    ) -> bool:
        """
        判断节点是否为入口节点候选
        
        Args:
            node: 待判断的节点
            book_id: 书籍标识符
            threshold: 得分阈值，默认0.5
            
        Returns:
            True if node scores above threshold
        """
        return self.score_entry_node(node, book_id) >= threshold
    
    def get_argument_pattern_stages(self, book_id: str) -> List[str]:
        """
        获取论证模式的各阶段
        
        Parses the argument pattern string into individual stages.
        
        Args:
            book_id: 书籍标识符
            
        Returns:
            论证阶段列表，如 ["格局", "用神", "吉凶"]
            
        **Validates: Requirements 11.2, 11.3, 11.4**
        """
        pattern = self.get_argument_pattern(book_id)
        if pattern == "通用":
            return []
        return [stage.strip() for stage in pattern.split("→")]
    
    def classify_node_by_argument_stage(
        self, 
        node: LogicNode, 
        book_id: str
    ) -> Optional[str]:
        """
        根据论证模式阶段分类节点
        
        Attempts to classify a node into one of the argument pattern stages
        based on keyword matching in the node summary.
        
        Args:
            node: 待分类的节点
            book_id: 书籍标识符
            
        Returns:
            匹配的论证阶段，如 "格局"，无匹配返回 None
        """
        stages = self.get_argument_pattern_stages(book_id)
        if not stages:
            return None
        
        summary = node.summary or ""
        
        # Check each stage for keyword match
        for stage in stages:
            if stage in summary:
                return stage
        
        return None


def get_book_type_adapter() -> BookTypeAdapter:
    """
    获取BookTypeAdapter单例
    
    Returns:
        BookTypeAdapter instance
    """
    return BookTypeAdapter()
