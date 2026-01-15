"""
Result Builder

从 snippet 内容构建规则结果。

Feature: rule-converter
Requirement Refs: Req 5.1-5.10
"""

import logging
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set

from scripts.rule_converter.loaders.logic_chain_loader import LogicChainNode
from scripts.rule_converter.loaders.snippet_store import Snippet, SnippetStore

logger = logging.getLogger(__name__)


@dataclass
class ConfigRuleResult:
    """
    规则结果配置
    
    对应 backend/core/contracts/config_models.py 中的 ConfigRuleResult
    """
    dimension: str
    level: str  # 大吉/吉/中等/凶/大凶
    conclusion_template_zh: str
    weight: float = 1.0
    confidence: float = 0.7
    tags: List[str] = field(default_factory=list)
    evidence_factors: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "dimension": self.dimension,
            "level": self.level,
            "conclusion_template_zh": self.conclusion_template_zh,
            "weight": self.weight,
            "confidence": self.confidence,
            "tags": self.tags,
            "evidence_factors": self.evidence_factors,
        }


class ResultBuilder:
    """
    结果构建器
    
    从 LogicChainNode 关联的 snippet 内容构建规则结果。
    
    功能：
    1. 从 snippet 内容推断 dimension（维度）
    2. 从 snippet 内容推断 level（吉凶等级）
    3. 构建 conclusion_template_zh（结论模板）
    4. 计算 weight（权重）
    5. 提取 tags（标签）
    
    Requirement Refs: Req 5.1-5.10
    """
    
    # 维度关键词映射
    DIMENSION_PATTERNS: Dict[str, List[str]] = {
        "career": ["事业", "功名", "官", "职", "仕途", "工作", "禄", "官禄"],
        "wealth": ["财", "富", "钱", "金", "财帛", "正财", "偏财", "财运"],
        "marriage": ["婚", "姻", "夫", "妻", "情", "夫妻", "配偶", "伴侣"],
        "health": ["病", "疾", "健康", "寿", "身体", "疾厄", "疾病"],
        "personality": ["性格", "品性", "心性", "个性", "性情", "气质"],
        "guidance": ["运", "吉凶", "时机", "行运", "流年", "大运", "运势"],
    }
    
    # 吉凶等级关键词映射（对齐 ConfigRuleResult.level 枚举）
    # 注意：检测顺序很重要，要先检测更具体的词
    LEVEL_PATTERNS: Dict[str, List[str]] = {
        "大吉": ["大利", "大吉", "极佳", "大成", "大贵", "大富", "极好"],
        "大凶": ["大凶", "极凶", "夭折", "亡", "大忌", "大害"],
        "中等": ["普通", "平常", "一般"],  # "普通" 要在 "通" 之前
        "凶": ["不利", "凶", "忌", "损伤", "破", "害", "克", "刑", "冲"],  # "不利" 要在 "利" 之前
        "吉": ["利", "吉", "好", "佳", "宜", "善", "美", "贵", "富", "顺利", "亨通"],  # "顺利" 和 "亨通" 而不是单字
    }
    
    # 角色权重映射
    ROLE_WEIGHTS: Dict[str, float] = {
        "主干": 2.0,
        "主干依赖": 1.5,
        "条件分支": 1.2,
        "例外处理": 1.0,
        "总结": 1.8,
    }
    
    DEFAULT_DIMENSION = "guidance"
    DEFAULT_LEVEL = "中等"
    DEFAULT_WEIGHT = 1.0
    DEFAULT_CONFIDENCE = 0.7
    
    def __init__(self, snippet_store: Optional[SnippetStore] = None):
        self.snippet_store = snippet_store
    
    def build(
        self,
        node: LogicChainNode,
        snippets: Optional[List[Snippet]] = None,
    ) -> ConfigRuleResult:
        """
        从节点构建规则结果
        
        Args:
            node: LogicChain 节点
            snippets: 已解析的 snippet 列表（可选，如果不提供则从 store 获取）
            
        Returns:
            ConfigRuleResult
        """
        # 获取 snippets
        if snippets is None and self.snippet_store:
            snippets = self.snippet_store.get_batch(node.snippet_ids)
        
        if not snippets:
            snippets = []
        
        # 合并所有 snippet 内容
        full_text = " ".join(s.content for s in snippets)
        
        # 推断维度
        dimension = self._infer_dimension(full_text)
        
        # 推断吉凶等级
        level = self._infer_level(full_text)
        
        # 构建结论模板
        conclusion_template = self._build_conclusion_template(snippets, node)
        
        # 计算权重
        weight = self._compute_weight(node.role, len(snippets))
        
        # 提取标签
        tags = self._extract_tags(full_text, dimension, level)
        
        return ConfigRuleResult(
            dimension=dimension,
            level=level,
            conclusion_template_zh=conclusion_template,
            weight=weight,
            confidence=self.DEFAULT_CONFIDENCE,
            tags=tags,
            evidence_factors=node.factor_refs.copy() if node.factor_refs else [],
        )
    
    def _infer_dimension(self, text: str) -> str:
        """
        从文本推断维度
        
        策略：统计各维度关键词出现次数，选择最高的
        """
        if not text:
            return self.DEFAULT_DIMENSION
        
        dimension_scores: Dict[str, int] = {}
        
        for dimension, keywords in self.DIMENSION_PATTERNS.items():
            score = sum(text.count(kw) for kw in keywords)
            if score > 0:
                dimension_scores[dimension] = score
        
        if not dimension_scores:
            return self.DEFAULT_DIMENSION
        
        # 返回得分最高的维度
        return max(dimension_scores, key=dimension_scores.get)
    
    def _infer_level(self, text: str) -> str:
        """
        从文本推断吉凶等级
        
        策略：
        1. 先检测 "大吉" 和 "大凶" 级别的强关键词
        2. 再检测 "凶"（在 "吉" 之前，避免 "不利" 被 "利" 匹配）
        3. 再检测 "吉"
        4. 默认为 "中等"
        """
        if not text:
            return self.DEFAULT_LEVEL
        
        # 检测顺序：大吉 > 大凶 > 中等 > 凶 > 吉
        # 注意：中等要在吉之前（避免"普通"的"通"匹配）；凶要在吉之前（避免"不利"匹配"利"）
        level_priority = ["大吉", "大凶", "中等", "凶", "吉"]
        
        for level in level_priority:
            keywords = self.LEVEL_PATTERNS.get(level, [])
            for kw in keywords:
                if kw in text:
                    return level
        
        return self.DEFAULT_LEVEL
    
    def _build_conclusion_template(
        self,
        snippets: List[Snippet],
        node: LogicChainNode,
    ) -> str:
        """
        构建结论模板
        
        策略：
        1. 优先使用第一个主干角色的 snippet
        2. 如果没有，使用第一个 snippet
        3. 如果都没有，使用 node.summary
        """
        if not snippets:
            return node.summary or "（规则结论待补充）"
        
        # 找主干 snippet
        for snippet in snippets:
            if snippet.role == "主干":
                return snippet.content
        
        # 使用第一个 snippet
        return snippets[0].content
    
    def _compute_weight(self, role: str, snippet_count: int) -> float:
        """
        计算权重
        
        基于角色和 snippet 数量
        """
        base_weight = self.ROLE_WEIGHTS.get(role, self.DEFAULT_WEIGHT)
        
        # snippet 数量加成（每多一个增加 0.1，最多增加 0.5）
        snippet_bonus = min(0.5, (snippet_count - 1) * 0.1)
        
        return round(base_weight + snippet_bonus, 2)
    
    def _extract_tags(self, text: str, dimension: str, level: str) -> List[str]:
        """
        提取标签
        
        从文本中提取关键词作为标签
        """
        tags: Set[str] = set()
        
        # 添加维度作为标签
        tags.add(dimension)
        
        # 添加吉凶等级
        if level != "中等":
            tags.add(level)
        
        # 从文本中提取常见命理术语作为标签
        common_terms = [
            "正官", "七杀", "正印", "偏印", "比肩", "劫财",
            "食神", "伤官", "正财", "偏财",
            "日主", "月令", "用神", "喜神", "忌神",
            "身强", "身弱", "得令", "失令",
            "三合", "六合", "六冲", "刑",
        ]
        
        for term in common_terms:
            if term in text:
                tags.add(term)
        
        return list(tags)[:10]  # 最多 10 个标签
