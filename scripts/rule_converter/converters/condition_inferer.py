"""
Condition Inferer

从 factor_refs 推断规则触发条件。

Feature: rule-converter
Requirement Refs: Req 4.1-4.8
"""

import logging
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union

from scripts.rule_converter.loaders.factor_ontology import FactorDef, FactorOntology
from scripts.rule_converter.loaders.logic_chain_loader import LogicChainNode

logger = logging.getLogger(__name__)


@dataclass
class RuleCondition:
    """
    单个规则条件
    
    对应 backend/core/contracts/config_models.py 中的 RuleCondition
    """
    factor_id: str
    operator: str  # ==, !=, >, <, >=, <=, in, not_in, exists, not_exists, between
    value: Any = None
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        result = {
            "factor_id": self.factor_id,
            "operator": self.operator,
        }
        if self.value is not None:
            result["value"] = self.value
        return result


@dataclass
class LogicalExpression:
    """
    复合逻辑表达式
    
    对应 backend/core/contracts/config_models.py 中的 LogicalExpression
    """
    operator: str  # AND, OR, NOT
    conditions: List[Union["RuleCondition", "LogicalExpression"]]
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            "operator": self.operator,
            "conditions": [
                c.to_dict() if hasattr(c, "to_dict") else c
                for c in self.conditions
            ],
        }


@dataclass
class InferenceResult:
    """推断结果"""
    condition: Optional[Union[RuleCondition, LogicalExpression]]
    confidence: float
    reason: str


class ConditionInferer:
    """
    条件推断器
    
    从 LogicChainNode 的 factor_refs 推断规则的触发条件。
    
    推断策略：
    1. 如果节点有显式 condition，直接使用（confidence=1.0）
    2. 如果只有单个 factor_ref，生成简单条件（confidence=0.8）
    3. 如果有多个 factor_refs，生成 AND 组合（confidence=0.7）
    4. 根据因子的 value_type 选择合适的 operator
    
    Requirement Refs: Req 4.1-4.8
    """
    
    def __init__(self, ontology: FactorOntology):
        self.ontology = ontology
    
    def infer(self, node: LogicChainNode) -> InferenceResult:
        """
        从节点推断条件
        
        Args:
            node: LogicChain 节点
            
        Returns:
            InferenceResult
        """
        # 1. 如果有显式 condition，直接使用
        if node.condition:
            # TODO: 解析显式 condition 为结构化表达式
            # 目前作为占位符，返回 exists 条件
            return InferenceResult(
                condition=None,  # 显式 condition 需要特殊处理
                confidence=1.0,
                reason="显式条件需要人工转换",
            )
        
        # 2. 检查 factor_refs
        if not node.factor_refs:
            return InferenceResult(
                condition=None,
                confidence=0.0,
                reason="无 factor_refs，无法推断条件",
            )
        
        # 3. 单个因子
        if len(node.factor_refs) == 1:
            factor_id = node.factor_refs[0]
            condition = self._infer_single_factor(factor_id)
            
            # 检查因子是否在本体中
            if self.ontology.is_valid(factor_id):
                return InferenceResult(
                    condition=condition,
                    confidence=0.8,
                    reason=f"单因子推断: {factor_id}",
                )
            else:
                return InferenceResult(
                    condition=condition,
                    confidence=0.6,
                    reason=f"单因子推断(未认证因子): {factor_id}",
                )
        
        # 4. 多个因子 → AND 组合
        conditions = []
        all_valid = True
        
        for factor_id in node.factor_refs:
            condition = self._infer_single_factor(factor_id)
            conditions.append(condition)
            
            if not self.ontology.is_valid(factor_id):
                all_valid = False
        
        logical_expr = LogicalExpression(
            operator="AND",
            conditions=conditions,
        )
        
        confidence = 0.7 if all_valid else 0.5
        reason = f"多因子AND组合: {len(conditions)}个因子"
        if not all_valid:
            reason += " (部分因子未认证)"
        
        return InferenceResult(
            condition=logical_expr,
            confidence=confidence,
            reason=reason,
        )
    
    def _infer_single_factor(self, factor_id: str) -> RuleCondition:
        """
        为单个因子推断条件
        
        根据因子的 value_type 选择合适的 operator:
        - boolean → == True
        - numeric → exists (无法推断具体值)
        - enum → exists (无法推断具体值)
        - 未知 → exists
        """
        factor_def = self.ontology.get(factor_id)
        
        if factor_def is None:
            # 因子未定义，使用 exists
            return RuleCondition(
                factor_id=factor_id,
                operator="exists",
            )
        
        if factor_def.is_boolean:
            # 布尔类型，假设为 True
            return RuleCondition(
                factor_id=factor_id,
                operator="==",
                value=True,
            )
        
        if factor_def.is_numeric:
            # 数值类型，只能判断存在性
            # 如果需要具体值，需要从上下文推断
            return RuleCondition(
                factor_id=factor_id,
                operator="exists",
            )
        
        if factor_def.is_enum:
            # 枚举类型，只能判断存在性
            # 如果需要具体值，需要从上下文推断
            return RuleCondition(
                factor_id=factor_id,
                operator="exists",
            )
        
        # 默认使用 exists
        return RuleCondition(
            factor_id=factor_id,
            operator="exists",
        )
    
    def infer_with_context(
        self,
        node: LogicChainNode,
        snippet_content: Optional[str] = None,
    ) -> InferenceResult:
        """
        带上下文的条件推断
        
        尝试从节点 summary 或 snippet 内容中推断具体的条件值。
        
        Args:
            node: LogicChain 节点
            snippet_content: 关联的 snippet 内容
            
        Returns:
            InferenceResult
        """
        # 基础推断
        result = self.infer(node)
        
        if result.condition is None:
            return result
        
        # TODO: 使用 NLP 或规则从 summary/snippet_content 中提取具体值
        # 例如：如果 summary 包含 "甲木"，可以推断 day_master == "甲"
        
        return result
