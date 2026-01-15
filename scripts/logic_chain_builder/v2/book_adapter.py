"""
BookTypeAdapter - L5 领域特定适配器

为不同类型的书籍提供特定的处理策略。
"""

from typing import Callable, Dict, List

from scripts.logic_chain_builder.models import LogicNode
from scripts.logic_chain_builder.logging_config import get_logger

logger = get_logger(__name__)


class BaseAdapter:
    """适配器基类"""
    
    def get_entry_node_heuristics(self) -> Callable[[LogicNode], float]:
        """入口节点识别启发式"""
        return lambda node: 1.0 if node.role.value == "主干" else 0.0
    
    def get_argument_pattern(self) -> str:
        """论证模式"""
        return "通用"
    
    def get_factor_patterns(self) -> List[str]:
        """领域特定因子模式"""
        return []


class BaziAdapter(BaseAdapter):
    """八字适配器"""
    
    def get_entry_node_heuristics(self) -> Callable[[LogicNode], float]:
        return lambda node: 1.0 if "格局" in node.summary or node.role.value == "主干" else 0.0
    
    def get_argument_pattern(self) -> str:
        return "格局→用神→吉凶"
    
    def get_factor_patterns(self) -> List[str]:
        return ["干支", "十神", "格局", "用神", "喜忌", "日主", "月令"]


class ZiweiAdapter(BaseAdapter):
    """紫微适配器"""
    
    def get_entry_node_heuristics(self) -> Callable[[LogicNode], float]:
        return lambda node: 1.0 if "星" in node.summary or node.role.value == "主干" else 0.0
    
    def get_argument_pattern(self) -> str:
        return "星曜→宫位→四化→吉凶"
    
    def get_factor_patterns(self) -> List[str]:
        return ["星曜", "宫位", "四化", "庙旺", "落陷", "化禄", "化权"]


class AstrologyAdapter(BaseAdapter):
    """占星适配器"""
    
    def get_entry_node_heuristics(self) -> Callable[[LogicNode], float]:
        def heuristic(node: LogicNode) -> float:
            summary_lower = node.summary.lower()
            if "planet" in summary_lower or "sun" in summary_lower or "moon" in summary_lower:
                return 1.0
            return 0.0 if node.role.value != "主干" else 0.5
        return heuristic
    
    def get_argument_pattern(self) -> str:
        return "planet→sign→house→aspect→interpretation"
    
    def get_factor_patterns(self) -> List[str]:
        return ["planet", "sign", "house", "aspect", "transit", "natal"]


class TarotAdapter(BaseAdapter):
    """塔罗适配器"""
    
    def get_entry_node_heuristics(self) -> Callable[[LogicNode], float]:
        def heuristic(node: LogicNode) -> float:
            summary_lower = node.summary.lower()
            if "card" in summary_lower or "arcana" in summary_lower or "牌" in node.summary:
                return 1.0
            return 0.0 if node.role.value != "主干" else 0.5
        return heuristic
    
    def get_argument_pattern(self) -> str:
        return "牌面→象征→诠释"
    
    def get_factor_patterns(self) -> List[str]:
        return ["card", "arcana", "suit", "spread", "symbol", "meaning"]


class DreamAdapter(BaseAdapter):
    """解梦适配器"""
    
    def get_entry_node_heuristics(self) -> Callable[[LogicNode], float]:
        def heuristic(node: LogicNode) -> float:
            summary_lower = node.summary.lower()
            if "symbol" in summary_lower or "梦" in node.summary or "象" in node.summary:
                return 1.0
            return 0.0 if node.role.value != "主干" else 0.5
        return heuristic
    
    def get_argument_pattern(self) -> str:
        return "符号→情境→心理→解析"
    
    def get_factor_patterns(self) -> List[str]:
        return ["symbol", "archetype", "unconscious", "interpretation"]


class YijingAdapter(BaseAdapter):
    """周易适配器"""
    
    def get_entry_node_heuristics(self) -> Callable[[LogicNode], float]:
        def heuristic(node: LogicNode) -> float:
            if "卦" in node.summary or "爻" in node.summary:
                return 1.0
            return 0.0 if node.role.value != "主干" else 0.5
        return heuristic
    
    def get_argument_pattern(self) -> str:
        return "卦象→爻辞→传文→应用"
    
    def get_factor_patterns(self) -> List[str]:
        return ["卦", "爻", "象", "辞", "变卦", "互卦"]


class DefaultAdapter(BaseAdapter):
    """默认适配器"""
    pass


class BookTypeAdapter:
    """
    领域特定适配器管理器 (L5)
    
    根据书籍类型返回相应的适配器。
    """
    
    BOOK_TYPE_MAPPING = {
        "bazi": ["滴天髓", "子平真诠", "穷通宝鉴", "渊海子平", "三命通会"],
        "ziwei": ["紫微斗数全书"],
        "astrology": [
            "the_inner_sky", "planets_in_transit", "the_astrological_houses",
            "astrology_of_personality", "tetrabiblos", "christian_astrology,_vol._1_and_2"
        ],
        "tarot": [
            "the_book_of_thoth", "78_degrees_of_wisdom",
            "waite_pictorial_key_to_the_tarot", "learning_the_tarot"
        ],
        "dream": [
            "周公解梦", "the_interpretation_of_dreams",
            "llewellyns_complete_dictionary_of_dreams",
            "the_archetypes_and_the_collective_unconscious"
        ],
        "yijing": ["周易"],
    }
    
    ADAPTER_MAP = {
        "bazi": BaziAdapter,
        "ziwei": ZiweiAdapter,
        "astrology": AstrologyAdapter,
        "tarot": TarotAdapter,
        "dream": DreamAdapter,
        "yijing": YijingAdapter,
    }
    
    def get_book_type(self, book_id: str) -> str:
        """获取书籍类型"""
        for book_type, books in self.BOOK_TYPE_MAPPING.items():
            if book_id in books:
                return book_type
        return "unknown"
    
    def get_adapter(self, book_id: str) -> BaseAdapter:
        """获取领域适配器"""
        book_type = self.get_book_type(book_id)
        adapter_class = self.ADAPTER_MAP.get(book_type, DefaultAdapter)
        return adapter_class()
    
    def get_factor_patterns(self, book_id: str) -> List[str]:
        """获取领域特定的因子模式"""
        adapter = self.get_adapter(book_id)
        return adapter.get_factor_patterns()


# 导出
__all__ = [
    "BookTypeAdapter",
    "BaseAdapter",
    "BaziAdapter",
    "ZiweiAdapter",
    "AstrologyAdapter",
    "TarotAdapter",
    "DreamAdapter",
    "YijingAdapter",
    "DefaultAdapter",
]
