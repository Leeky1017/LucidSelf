"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491549
Version: 1.0.0

对照 Requirements 6.4 - 带 @SemanticRegistry.register 装饰器的 Python 模块
"""

from backend.semantics.core.base import SemanticEntry, SemanticRegistry, NarrativeSnippetExtended
from backend.core.contracts import (
    SnippetRole,
    SourceMetadata,
    ConfigRelation,
    EvidenceChainEntry,
    RelationType,
    EffectDirection,
    ConfidenceLevel,
)


@SemanticRegistry.register(
    semantic_id="acu_v1.0.0_0_mother_complex_foundation____001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 0MotherComplexFoundation(SemanticEntry):
    """
    **Source Text** (¶161, Lines 2584-2593):

> [161] The mother archetype forms the foundation of the s...
    """
    
    original_text: str = """**Source Text** (¶161, Lines 2584-2593):

> [161] The mother archetype forms the foundation of the so-called mother-complex. In any event, the child's instincts are disturbed, and this constellates archetypes which produce fantasies that come between the child and its mother as an alien and often frightening element. Thus, if children of an overanxious mother regularly dream that she is a terrifying animal or a witch, these experiences point to a split in the child's psyche that predisposes it to neurosis.

**English Paraphrase**: Mother archetype = foundation of mother-complex. Disturbed instincts → constellate archetypes → fantasies come between child and mother. Terrifying animal/witch dreams = split in psyche → predisposition to neurosis.

**中文诠释**: 母亲原型 = 母亲情结的基础。受扰本能 → 激活原型 → 幻想介入孩子与母亲之间。恐怖动物/女巫梦 = 心灵分裂 → 神经症倾向。

**Narrative Snippets**:
- `[ns_cw9i_III_161]` `[trigger: mother_complex]` `[factor_trigger: jung_mother AND jung_complex]` `[role: 主干]` Mother archetype is foundation of mother-complex—disturbed instincts constellate archetypes that come between child and mother. → ¶161"""
    normalized_text_zh: str = """"""
    subject: str = "0 Mother-Complex Foundation (¶161)"
    factor_refs: list = []
    
    # 叙事素材（包含 trigger_human）
    narrative_snippets: list = [

    ]
    
    # L2.5 因子关系
    related_semantics: list = [

    ]
    
    # L2.5 证据链
    evidence_refs: list = [

    ]
    
    metadata: SourceMetadata = SourceMetadata(
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_0_mother_complex_foundation____001_L1",
    )
    version: str = "1.0.0"
