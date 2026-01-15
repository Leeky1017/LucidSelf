"""
ConflictResolver - 冲突解决器

Feature: cross-book-knowledge-graph
Requirement Refs: Req 3.6, Req 13.1, Req 13.2, Req 13.3, Req 13.4, Req 13.5, Req 13.6
Design Refs: Design.md#冲突输出接口, Design.md#ConflictResolver
"""

import logging
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from scripts.knowledge_graph_builder.models import (
    ConceptNode,
    ConflictOutput,
    ConflictType,
    ResolutionStrategy,
    SemanticEdge,
)
from scripts.knowledge_graph_builder.models.conflict import ConceptSummary

logger = logging.getLogger(__name__)


# 冲突模板
DEFAULT_TEMPLATES = {
    "direct_contradiction": {
        "zh": "关于{dimension}，{book_a}认为「{conclusion_a}」，而{book_b}则认为「{conclusion_b}」。",
        "en": "Regarding {dimension}, {book_a} suggests '{conclusion_a}', while {book_b} indicates '{conclusion_b}'.",
    },
    "conditional_exception": {
        "zh": "一般情况下{conclusion_a}，但在{condition}条件下{conclusion_b}。",
        "en": "Generally {conclusion_a}, but under {condition} condition, {conclusion_b}.",
    },
    "scope_difference": {
        "zh": "{book_a}从{scope_a}角度认为{conclusion_a}，{book_b}从{scope_b}角度认为{conclusion_b}。",
        "en": "{book_a} from {scope_a} perspective suggests {conclusion_a}; {book_b} from {scope_b} perspective suggests {conclusion_b}.",
    },
    "cross_system_divergence": {
        "zh": "{system_a}体系认为{conclusion_a}，{system_b}体系则认为{conclusion_b}，这反映了不同占卜体系的视角差异。",
        "en": "The {system_a} system suggests {conclusion_a}, while the {system_b} system indicates {conclusion_b}, reflecting different perspectives across divination systems.",
    },
}


class ConflictResolver:
    """
    冲突解决器 - 生成可消费的冲突输出
    
    功能：
    - 根据conflict_type选择resolution_strategy
    - 加载并渲染冲突模板
    - 生成resolution_hint
    - 支持zh/en双语输出
    """
    
    def __init__(
        self,
        templates_path: Optional[Path] = None,
    ):
        self.templates_path = templates_path or Path(
            'data/knowledge_graph/conflict_templates.yaml'
        )
        self._templates: Optional[Dict] = None
    
    @property
    def templates(self) -> Dict:
        """懒加载模板"""
        if self._templates is None:
            self._templates = self._load_templates()
        return self._templates
    
    def _load_templates(self) -> Dict:
        """加载冲突模板"""
        if self.templates_path.exists():
            with open(self.templates_path, 'r', encoding='utf-8') as f:
                loaded = yaml.safe_load(f)
                if loaded and 'templates' in loaded:
                    # 将list格式转换为dict格式 {conflict_type: {zh, en}}
                    templates_list = loaded['templates']
                    result = {}
                    for tpl in templates_list:
                        conflict_type = tpl.get('conflict_type', 'direct_contradiction')
                        result[conflict_type] = {
                            'zh': tpl.get('template_zh', ''),
                            'en': tpl.get('template_en', ''),
                        }
                    return result
        return DEFAULT_TEMPLATES
    
    def resolve(
        self,
        edge: SemanticEdge,
        concept_a: ConceptNode,
        concept_b: ConceptNode,
    ) -> ConflictOutput:
        """
        解决冲突，生成ConflictOutput
        
        Args:
            edge: 冲突边
            concept_a: 冲突方A
            concept_b: 冲突方B
            
        Returns:
            ConflictOutput: 供叙事层消费的冲突输出
        """
        # 确定冲突类型
        conflict_type = edge.conflict_type or ConflictType.DIRECT_CONTRADICTION
        
        # 选择解决策略
        strategy = self._select_strategy(conflict_type, concept_a, concept_b)
        
        # 生成提示
        hint = self._generate_hint(strategy, concept_a, concept_b)
        
        # 渲染模板
        template_zh, template_en = self._render_templates(
            conflict_type, concept_a, concept_b
        )
        
        # 确定模板ID
        template_id = f"template_{conflict_type.value}"
        
        return ConflictOutput(
            viewpoint_a=ConceptSummary(
                concept_id=concept_a.concept_id,
                label_zh=concept_a.canonical_label_zh,
                book_source=concept_a.source_nodes[0].book_id if concept_a.source_nodes else "",
                authority_score=concept_a.authority_score,
            ),
            viewpoint_b=ConceptSummary(
                concept_id=concept_b.concept_id,
                label_zh=concept_b.canonical_label_zh,
                book_source=concept_b.source_nodes[0].book_id if concept_b.source_nodes else "",
                authority_score=concept_b.authority_score,
            ),
            conflict_type=conflict_type,
            dimension=concept_a.dimension.value if concept_a.dimension else "general",
            resolution_strategy=strategy,
            resolution_template_id=template_id,
            resolution_hint=hint,
            rendered_template_zh=template_zh,
            rendered_template_en=template_en,
        )
    
    def _select_strategy(
        self,
        conflict_type: ConflictType,
        concept_a: ConceptNode,
        concept_b: ConceptNode,
    ) -> ResolutionStrategy:
        """选择解决策略"""
        # 跨体系分歧 -> 呈现双方
        if conflict_type == ConflictType.CROSS_SYSTEM_DIVERGENCE:
            return ResolutionStrategy.PRESENT_BOTH
        
        # 权威性差距大 -> 权威性优先
        if abs(concept_a.authority_score - concept_b.authority_score) > 0.2:
            return ResolutionStrategy.AUTHORITY_BASED
        
        # 条件例外 -> 条件选择
        if conflict_type == ConflictType.CONDITIONAL_EXCEPTION:
            return ResolutionStrategy.CONDITION_BASED
        
        # 默认 -> 综合
        return ResolutionStrategy.SYNTHESIS
    
    def _generate_hint(
        self,
        strategy: ResolutionStrategy,
        concept_a: ConceptNode,
        concept_b: ConceptNode,
    ) -> str:
        """生成解决提示"""
        if strategy == ResolutionStrategy.AUTHORITY_BASED:
            higher = concept_a if concept_a.authority_score > concept_b.authority_score else concept_b
            source = higher.source_nodes[0].book_id if higher.source_nodes else "高权威来源"
            return f"建议以{source}为准，权威性更高"
        
        elif strategy == ResolutionStrategy.PRESENT_BOTH:
            return "建议同时呈现双方观点，体现不同体系的视角差异"
        
        elif strategy == ResolutionStrategy.CONDITION_BASED:
            return "建议根据条件差异分别采纳，不同条件下结论不同"
        
        else:  # SYNTHESIS
            return "建议综合双方观点，辩证理解"
    
    def _render_templates(
        self,
        conflict_type: ConflictType,
        concept_a: ConceptNode,
        concept_b: ConceptNode,
    ) -> tuple[str, str]:
        """渲染双语模板"""
        template_key = conflict_type.value
        templates = self.templates.get(template_key, DEFAULT_TEMPLATES.get(template_key, {}))
        
        # 准备渲染变量
        book_a = concept_a.source_nodes[0].book_id if concept_a.source_nodes else "来源A"
        book_b = concept_b.source_nodes[0].book_id if concept_b.source_nodes else "来源B"
        
        variables = {
            "book_a": book_a,
            "book_b": book_b,
            "conclusion_a": concept_a.canonical_label_zh,
            "conclusion_b": concept_b.canonical_label_zh,
            "dimension": concept_a.dimension.value if concept_a.dimension else "general",
            "system_a": concept_a.divination_system.value,
            "system_b": concept_b.divination_system.value,
            "condition": "特定条件",
            "scope_a": "整体",
            "scope_b": "局部",
        }
        
        # 渲染中文
        template_zh = templates.get("zh", "")
        try:
            rendered_zh = template_zh.format(**variables) if template_zh else ""
        except KeyError:
            rendered_zh = template_zh
        
        # 渲染英文
        template_en = templates.get("en", "")
        try:
            rendered_en = template_en.format(**variables) if template_en else ""
        except KeyError:
            rendered_en = template_en
        
        return rendered_zh, rendered_en
    
    def resolve_batch(
        self,
        conflicts: List[tuple[SemanticEdge, ConceptNode, ConceptNode]],
    ) -> List[ConflictOutput]:
        """批量解决冲突"""
        return [
            self.resolve(edge, concept_a, concept_b)
            for edge, concept_a, concept_b in conflicts
        ]
