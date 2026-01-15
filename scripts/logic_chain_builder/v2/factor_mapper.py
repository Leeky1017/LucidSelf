"""
FactorMapper - L1 统一因子映射器

统一factor_trigger与relation.factor_a/b的映射，确保因子命名规范化。
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import yaml

from scripts.logic_chain_builder.logging_config import get_logger
from scripts.logic_chain_builder.v2.stopwords import StopwordsFilter
from scripts.schema_extractor.models import ConfigRelation

logger = get_logger(__name__)


class FactorOntology:
    """因子本体定义"""
    
    def __init__(self, ontology_path: str = None):
        """
        加载因子本体
        
        Args:
            ontology_path: 本体文件路径
        """
        self.namespaces: Dict[str, Dict] = {}
        self.stopwords: Dict[str, List[str]] = {}
        
        if ontology_path:
            self._load_from_file(ontology_path)
        else:
            self._use_default_ontology()
    
    def _load_from_file(self, path: str):
        """从文件加载本体"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            self.namespaces = data.get('namespaces', {})
            self.stopwords = data.get('stopwords', {})
        except FileNotFoundError:
            logger.warning(f"Ontology file not found: {path}, using defaults")
            self._use_default_ontology()
        except Exception as e:
            logger.error(f"Failed to load ontology: {e}")
            self._use_default_ontology()
    
    def _use_default_ontology(self):
        """使用默认本体"""
        self.namespaces = {
            "star_": {
                "patterns": ["星", "star", "planet", "曜"],
                "examples": ["ziwei", "taiyang", "mars", "saturn", "紫微", "太阳"],
            },
            "palace_": {
                "patterns": ["宫", "palace", "house"],
                "examples": ["life", "siblings", "1st", "10th", "命宫", "兄弟宫"],
            },
            "state_": {
                "patterns": ["旺", "陷", "庙", "exalted", "debilitated", "得令", "失令"],
                "examples": ["miaowang", "luoxian"],
            },
            "group_": {
                "patterns": ["组", "group", "六煞", "四化"],
                "examples": ["liusha", "sihua"],
            },
            "effect_": {
                "patterns": ["效", "effect", "吉", "凶"],
                "examples": ["beneficial", "malefic"],
            },
            "sign_": {
                "patterns": ["sign", "座", "宫位"],
                "examples": ["aries", "taurus", "白羊", "金牛"],
            },
            "aspect_": {
                "patterns": ["aspect", "相位", "合", "冲", "刑"],
                "examples": ["conjunction", "opposition", "trine"],
            },
            "card_": {
                "patterns": ["card", "牌", "arcana"],
                "examples": ["fool", "magician", "愚者", "魔术师"],
            },
            "symbol_": {
                "patterns": ["symbol", "象征", "符号"],
                "examples": ["water", "fire", "水", "火"],
            },
        }


class FactorMapper:
    """
    统一因子映射器 (L1)
    
    负责:
    - 从factor_trigger提取因子
    - 规范化因子命名
    - 过滤停用词
    - 映射relation到节点
    """
    
    DEFAULT_ONTOLOGY_PATH = "data/factor_ontology/namespace.yaml"
    
    def __init__(self, ontology_path: str = None):
        """
        初始化因子映射器
        
        Args:
            ontology_path: 本体文件路径
        """
        self.ontology = FactorOntology(ontology_path or self.DEFAULT_ONTOLOGY_PATH)
        self.stopwords_filter = StopwordsFilter()
    
    def extract_factors(self, factor_trigger: str) -> Set[str]:
        """
        从factor_trigger提取因子，过滤停用词
        
        Args:
            factor_trigger: 原始因子触发字符串
            
        Returns:
            规范化的非停用词因子集合
        """
        if not factor_trigger:
            return set()
        
        # 提取所有因子
        raw_factors = self._parse_factor_trigger(factor_trigger)
        
        # 过滤停用词
        filtered = self.stopwords_filter.filter_factors(raw_factors)
        
        # 规范化命名
        normalized = {self._normalize_factor(f) for f in filtered}
        
        # 再次过滤空字符串
        return {f for f in normalized if f}
    
    def _parse_factor_trigger(self, factor_trigger: str) -> Set[str]:
        """
        解析factor_trigger字符串
        
        处理格式如:
        - star_ziwei AND palace_life
        - star_ziwei AND (star_zuofu OR star_youbi)
        - gender_female AND star_ziwei
        
        Args:
            factor_trigger: factor_trigger字符串
            
        Returns:
            原始因子集合
        """
        # 移除逻辑操作符和括号
        cleaned = factor_trigger
        for op in ['AND', 'OR', 'NOT', 'and', 'or', 'not', '(', ')']:
            cleaned = cleaned.replace(op, ' ')
        
        # 分割并清理
        tokens = cleaned.split()
        factors = set()
        
        for token in tokens:
            t = token.strip()
            if t and len(t) > 1:
                factors.add(t)
        
        return factors
    
    def _normalize_factor(self, factor: str) -> str:
        """
        规范化因子命名
        
        使用ontology中的namespace前缀:
        - star_: 星曜类
        - palace_: 宫位类
        - state_: 状态类
        - group_: 星组类
        - effect_: 效应类
        
        Args:
            factor: 原始因子
            
        Returns:
            规范化后的因子
        """
        if not factor:
            return ""
        
        factor_lower = factor.lower().strip()
        
        # 如果已经有namespace前缀，保持原样
        for namespace in self.ontology.namespaces.keys():
            if factor_lower.startswith(namespace):
                return factor_lower
        
        # 尝试根据patterns匹配namespace
        for namespace, config in self.ontology.namespaces.items():
            patterns = config.get("patterns", [])
            for pattern in patterns:
                if pattern.lower() in factor_lower:
                    return f"{namespace}{factor_lower}"
        
        # 未匹配到namespace，保持原样
        return factor_lower
    
    def map_relation_to_nodes(
        self,
        relation: ConfigRelation,
        node_factor_map: Dict[str, Set[str]]
    ) -> List[Tuple[str, str]]:
        """
        将relation映射到节点对
        
        Args:
            relation: 配置关系
            node_factor_map: node_id -> factor_ids映射
            
        Returns:
            (from_node_id, to_node_id)元组列表
        """
        # 规范化relation的factor
        factor_a_normalized = self._normalize_factor(relation.factor_a)
        factor_b_normalized = self._normalize_factor(relation.factor_b)
        
        # 查找包含factor_a的节点
        from_nodes = []
        for node_id, factors in node_factor_map.items():
            if self._factor_matches(factor_a_normalized, factors):
                from_nodes.append(node_id)
        
        # 查找包含factor_b的节点
        to_nodes = []
        for node_id, factors in node_factor_map.items():
            if self._factor_matches(factor_b_normalized, factors):
                to_nodes.append(node_id)
        
        # 创建所有from->to对（排除自环）
        pairs = [
            (f, t) for f in from_nodes for t in to_nodes
            if f != t
        ]
        
        return pairs
    
    def _factor_matches(self, target: str, factors: Set[str]) -> bool:
        """
        检查target是否匹配factors中的任何一个
        
        Args:
            target: 目标因子
            factors: 因子集合
            
        Returns:
            是否匹配
        """
        if not target:
            return False
        
        target_lower = target.lower()
        
        for factor in factors:
            factor_lower = factor.lower()
            # 精确匹配
            if target_lower == factor_lower:
                return True
            # 部分匹配
            if target_lower in factor_lower or factor_lower in target_lower:
                return True
        
        return False
    
    def build_node_factor_map(
        self,
        nodes: List,
        snippets: List
    ) -> Dict[str, Set[str]]:
        """
        构建节点->因子映射
        
        Args:
            nodes: LogicNode列表
            snippets: NarrativeSnippet列表
            
        Returns:
            node_id -> factor_set映射
        """
        # 构建snippet_id -> snippet映射
        snippet_map = {s.snippet_id: s for s in snippets}
        
        node_factor_map: Dict[str, Set[str]] = {}
        
        for node in nodes:
            factors = set()
            for snippet_id in node.snippet_ids:
                snippet = snippet_map.get(snippet_id)
                if snippet and snippet.factor_trigger:
                    extracted = self.extract_factors(snippet.factor_trigger)
                    factors.update(extracted)
            node_factor_map[node.node_id] = factors
        
        return node_factor_map


# 导出
__all__ = ["FactorMapper", "FactorOntology"]
