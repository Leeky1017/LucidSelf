"""
Factor Ontology Accessor

加载和访问认证因子本体。

Feature: rule-converter
Requirement Refs: Req 3.1-3.12
"""

import logging
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import yaml

logger = logging.getLogger(__name__)


@dataclass
class FactorDef:
    """
    因子定义
    
    对应 data/factor_ontology/certified/*.yaml 中的因子条目
    """
    id: str
    status: str = "existing"
    display_zh: str = ""
    display_en: Optional[str] = None
    description_zh: Optional[str] = None
    category: str = ""
    value_type: str = "boolean"  # boolean/numeric/enum
    value_range: Optional[Union[List[str], List[float]]] = None
    applicable_systems: List[str] = field(default_factory=list)
    
    @property
    def is_boolean(self) -> bool:
        return self.value_type == "boolean"
    
    @property
    def is_numeric(self) -> bool:
        return self.value_type == "numeric"
    
    @property
    def is_enum(self) -> bool:
        return self.value_type == "enum"
    
    def get_numeric_range(self) -> Optional[tuple]:
        """获取数值范围 (min, max)"""
        if self.is_numeric and self.value_range:
            if isinstance(self.value_range, list) and len(self.value_range) >= 2:
                return (self.value_range[0], self.value_range[1])
        return None
    
    def get_enum_values(self) -> Optional[List[str]]:
        """获取枚举值列表"""
        if self.is_enum and self.value_range:
            if isinstance(self.value_range, str):
                # 处理 "辰戌/丑未" 格式
                return self.value_range.split("/")
            elif isinstance(self.value_range, list):
                return [str(v) for v in self.value_range]
        return None


class FactorOntology:
    """
    因子本体访问器
    
    加载认证因子本体，提供因子查询和验证接口。
    
    数据源优先级：
    1. data/factor_ontology/certified/*.yaml（认证因子）
    2. 典籍/因子本体/*/*.yaml（基础定义，作为 fallback）
    
    Requirement Refs: Req 3.1-3.12
    """
    
    CERTIFIED_DIR = Path("data/factor_ontology/certified")
    BASE_DIR = Path("典籍/因子本体")
    SCHEMA_PATH = Path("data/factor_ontology/factor_schema.yaml")
    
    def __init__(
        self,
        certified_dir: Optional[Path] = None,
        base_dir: Optional[Path] = None,
    ):
        self.certified_dir = Path(certified_dir) if certified_dir else self.CERTIFIED_DIR
        self.base_dir = Path(base_dir) if base_dir else self.BASE_DIR
        
        self._factors: Dict[str, FactorDef] = {}
        self._by_system: Dict[str, List[str]] = defaultdict(list)
        self._by_category: Dict[str, List[str]] = defaultdict(list)
        self._loaded = False
        
        self._stats: Dict[str, int] = {
            "total_factors": 0,
            "certified_factors": 0,
            "base_factors": 0,
            "factors_by_system": {},
            "factors_by_category": {},
        }
    
    def load(self) -> None:
        """
        加载所有因子定义
        
        先加载认证因子，再加载基础定义（作为补充）
        """
        self._factors.clear()
        self._by_system.clear()
        self._by_category.clear()
        
        # 1. 加载认证因子（主要数据源）
        if self.certified_dir.exists():
            for yaml_file in self.certified_dir.glob("*_certified.yaml"):
                try:
                    self._load_certified_file(yaml_file)
                except Exception as e:
                    logger.warning(f"Failed to load certified file {yaml_file}: {e}")
        else:
            logger.warning(f"Certified directory not found: {self.certified_dir}")
        
        # 2. 加载基础定义（fallback）
        if self.base_dir.exists():
            for yaml_file in self.base_dir.glob("*/*.yaml"):
                try:
                    self._load_base_file(yaml_file)
                except Exception as e:
                    logger.warning(f"Failed to load base file {yaml_file}: {e}")
        
        self._update_stats()
        self._loaded = True
        
        logger.info(
            f"Loaded {self._stats['total_factors']} factors "
            f"({self._stats['certified_factors']} certified, "
            f"{self._stats['base_factors']} base)"
        )
    
    def _load_certified_file(self, path: Path) -> None:
        """
        解析认证因子文件
        
        结构：
        ```yaml
        system: bazi
        certified_time: '2025-12-05T00:07:50'
        total_certified: 10675
        by_category:
          relation:
            - id: xxx
              status: existing
              ...
        ```
        """
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not data:
            return
        
        system = data.get("system", path.stem.replace("_certified", ""))
        
        by_category = data.get("by_category", {})
        for category, factors in by_category.items():
            if not isinstance(factors, list):
                continue
            
            for f in factors:
                if not isinstance(f, dict) or "id" not in f:
                    continue
                
                factor_id = f["id"]
                
                # 跳过已存在的（保留先加载的）
                if factor_id in self._factors:
                    continue
                
                # 解析 value_range
                value_range = f.get("value_range")
                if value_range and not isinstance(value_range, list):
                    # 可能是字符串格式，如 "辰戌/丑未"
                    value_range = str(value_range)
                
                factor_def = FactorDef(
                    id=factor_id,
                    status=f.get("status", "existing"),
                    display_zh=f.get("display_zh", factor_id),
                    display_en=f.get("display_en"),
                    description_zh=f.get("description_zh"),
                    category=category,
                    value_type=f.get("value_type", "boolean"),
                    value_range=value_range,
                    applicable_systems=f.get("applicable_systems", [system]),
                )
                
                self._add_factor(factor_def, is_certified=True)
    
    def _load_base_file(self, path: Path) -> None:
        """
        解析基础因子定义文件
        
        结构：
        ```yaml
        factors:
          - id: day_master
            status: existing
            display_zh: 日主
            ...
        ```
        """
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not data:
            return
        
        # 从路径推断体系
        # 典籍/因子本体/{system}/{category}.yaml
        parts = path.parts
        system = None
        for i, part in enumerate(parts):
            if part == "因子本体" and i + 1 < len(parts):
                system = parts[i + 1]
                break
        
        category = path.stem  # 文件名作为 category
        
        factors = data.get("factors", [])
        for f in factors:
            if not isinstance(f, dict) or "id" not in f:
                continue
            
            factor_id = f["id"]
            
            # 跳过已存在的（认证因子优先）
            if factor_id in self._factors:
                continue
            
            factor_def = FactorDef(
                id=factor_id,
                status=f.get("status", "existing"),
                display_zh=f.get("display_zh", factor_id),
                display_en=f.get("display_en"),
                description_zh=f.get("description_zh"),
                category=f.get("category", category),
                value_type=f.get("value_type", "boolean"),
                value_range=f.get("value_range"),
                applicable_systems=f.get("applicable_systems", [system] if system else []),
            )
            
            self._add_factor(factor_def, is_certified=False)
    
    def _add_factor(self, factor: FactorDef, is_certified: bool = False) -> None:
        """添加因子到索引"""
        self._factors[factor.id] = factor
        
        # 按体系索引
        for system in factor.applicable_systems:
            self._by_system[system].append(factor.id)
        
        # 按分类索引
        if factor.category:
            self._by_category[factor.category].append(factor.id)
        
        # 更新统计
        if is_certified:
            self._stats["certified_factors"] = self._stats.get("certified_factors", 0) + 1
        else:
            self._stats["base_factors"] = self._stats.get("base_factors", 0) + 1
    
    def _update_stats(self) -> None:
        """更新统计信息"""
        self._stats["total_factors"] = len(self._factors)
        self._stats["factors_by_system"] = {
            system: len(ids) for system, ids in self._by_system.items()
        }
        self._stats["factors_by_category"] = {
            cat: len(ids) for cat, ids in self._by_category.items()
        }
    
    def _ensure_loaded(self) -> None:
        """确保数据已加载"""
        if not self._loaded:
            self.load()
    
    def get(self, factor_id: str) -> Optional[FactorDef]:
        """
        获取因子定义
        
        Args:
            factor_id: 因子ID
            
        Returns:
            FactorDef 或 None
        """
        self._ensure_loaded()
        return self._factors.get(factor_id)
    
    def is_valid(self, factor_id: str) -> bool:
        """
        验证因子ID是否有效
        
        Args:
            factor_id: 因子ID
            
        Returns:
            是否有效
        """
        self._ensure_loaded()
        return factor_id in self._factors
    
    def get_system(self, factor_id: str) -> Optional[str]:
        """
        获取因子所属的主要体系
        
        Args:
            factor_id: 因子ID
            
        Returns:
            体系名称或 None
        """
        self._ensure_loaded()
        factor = self._factors.get(factor_id)
        if factor and factor.applicable_systems:
            return factor.applicable_systems[0]
        return None
    
    def get_by_system(self, system: str) -> List[FactorDef]:
        """获取指定体系的所有因子"""
        self._ensure_loaded()
        factor_ids = self._by_system.get(system, [])
        return [self._factors[fid] for fid in factor_ids]
    
    def get_by_category(self, category: str) -> List[FactorDef]:
        """获取指定分类的所有因子"""
        self._ensure_loaded()
        factor_ids = self._by_category.get(category, [])
        return [self._factors[fid] for fid in factor_ids]
    
    def validate_all(self, factor_ids: List[str]) -> tuple:
        """
        批量验证因子ID
        
        Args:
            factor_ids: 因子ID列表
            
        Returns:
            (valid_ids, invalid_ids)
        """
        self._ensure_loaded()
        valid = []
        invalid = []
        for fid in factor_ids:
            if fid in self._factors:
                valid.append(fid)
            else:
                invalid.append(fid)
        return valid, invalid
    
    @property
    def stats(self) -> Dict[str, Any]:
        """获取统计信息"""
        self._ensure_loaded()
        return self._stats.copy()
    
    @property
    def systems(self) -> List[str]:
        """获取所有体系列表"""
        self._ensure_loaded()
        return list(self._by_system.keys())
    
    @property
    def categories(self) -> List[str]:
        """获取所有分类列表"""
        self._ensure_loaded()
        return list(self._by_category.keys())
    
    def __len__(self) -> int:
        self._ensure_loaded()
        return len(self._factors)
    
    def __contains__(self, factor_id: str) -> bool:
        return self.is_valid(factor_id)
