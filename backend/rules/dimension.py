"""
Dimension Mapper - 维度标准化映射器

对照 Task 11: Dimension Standardization
对照 Requirement 16: Dimension Standardization

.. deprecated::
    此模块已被 `backend.core.contracts.unified_dimensions` 取代。
    请迁移到 `DimensionRegistry` 统一接口。
    
    新代码应使用::
    
        from backend.core.contracts.unified_dimensions import (
            AnalysisDimension,
            DimensionRegistry,
            LifeDomain,
        )
"""

from __future__ import annotations

import logging
import warnings
from pathlib import Path
from typing import Dict, List, Optional, Set

import yaml

logger = logging.getLogger(__name__)

# 发出弃用警告
warnings.warn(
    "dimension.py 已弃用，请迁移到 backend.core.contracts.unified_dimensions 模块的 DimensionRegistry",
    DeprecationWarning,
    stacklevel=2
)



# 标准维度定义 (10 个)
STANDARD_DIMENSIONS = [
    "career",       # 事业
    "health",       # 健康
    "marriage",     # 婚姻
    "wealth",       # 财富
    "personality",  # 性格
    "fortune",      # 运势
    "omen",         # 预兆
    "guidance",     # 指引
    "unconscious",  # 潜意识
    "general",      # 通用
]

# 中英文映射
DIMENSION_LABELS = {
    "career": {"zh": "事业", "en": "Career"},
    "health": {"zh": "健康", "en": "Health"},
    "marriage": {"zh": "婚姻", "en": "Marriage"},
    "wealth": {"zh": "财富", "en": "Wealth"},
    "personality": {"zh": "性格", "en": "Personality"},
    "fortune": {"zh": "运势", "en": "Fortune"},
    "omen": {"zh": "预兆", "en": "Omen"},
    "guidance": {"zh": "指引", "en": "Guidance"},
    "unconscious": {"zh": "潜意识", "en": "Unconscious"},
    "general": {"zh": "通用", "en": "General"},
}

# 中文到英文映射
ZH_TO_EN = {v["zh"]: k for k, v in DIMENSION_LABELS.items()}


class DimensionMapper:
    """
    维度标准化映射器
    
    将体系特定的维度映射到标准维度。
    """
    
    # 默认配置路径
    DEFAULT_CONFIG_PATH = Path("data/knowledge_graph/dimension_config.yaml")
    
    def __init__(self, config_path: Optional[Path] = None):
        """初始化映射器"""
        self.config_path = config_path or self.DEFAULT_CONFIG_PATH
        self._config: Dict = {}
        self._system_dimensions: Dict[str, Set[str]] = {}
        self._load_config()
    
    def _load_config(self) -> None:
        """加载维度配置"""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    self._config = yaml.safe_load(f) or {}
                self._build_index()
            except Exception as e:
                logger.warning(f"Failed to load dimension config: {e}")
    
    def _build_index(self) -> None:
        """构建索引"""
        system_dims = self._config.get("system_dimensions", {})
        for system, data in system_dims.items():
            dims = data.get("dimensions", [])
            self._system_dimensions[system] = set(dims)
    
    def normalize(self, dimension: str) -> str:
        """
        标准化维度名称
        
        Args:
            dimension: 输入维度（中文或英文）
        
        Returns:
            标准英文维度名
        """
        # 已经是标准英文
        if dimension.lower() in STANDARD_DIMENSIONS:
            return dimension.lower()
        
        # 中文转英文
        if dimension in ZH_TO_EN:
            return ZH_TO_EN[dimension]
        
        # 未知维度返回 general
        logger.debug(f"Unknown dimension '{dimension}', defaulting to 'general'")
        return "general"
    
    def is_valid_for_system(self, dimension: str, system: str) -> bool:
        """
        检查维度是否对指定体系有效
        
        Args:
            dimension: 维度名称
            system: 体系名称 (bazi, ziwei, etc.)
        
        Returns:
            是否有效
        """
        if system not in self._system_dimensions:
            return True  # 未配置的体系允许所有维度
        
        # 标准化维度
        zh_dim = DIMENSION_LABELS.get(dimension.lower(), {}).get("zh", dimension)
        return zh_dim in self._system_dimensions[system]
    
    def get_system_dimensions(self, system: str) -> List[str]:
        """
        获取体系支持的维度列表
        
        Args:
            system: 体系名称
        
        Returns:
            维度列表（中文）
        """
        return list(self._system_dimensions.get(system, set()))
    
    def get_all_standard_dimensions(self) -> List[str]:
        """获取所有标准维度"""
        return STANDARD_DIMENSIONS.copy()
    
    def get_label(self, dimension: str, lang: str = "zh") -> str:
        """
        获取维度标签
        
        Args:
            dimension: 标准维度名
            lang: 语言 (zh/en)
        
        Returns:
            标签文本
        """
        dim = dimension.lower()
        if dim in DIMENSION_LABELS:
            return DIMENSION_LABELS[dim].get(lang, dimension)
        return dimension


# 单例实例
_mapper: Optional[DimensionMapper] = None


def get_dimension_mapper() -> DimensionMapper:
    """获取维度映射器单例"""
    global _mapper
    if _mapper is None:
        _mapper = DimensionMapper()
    return _mapper
