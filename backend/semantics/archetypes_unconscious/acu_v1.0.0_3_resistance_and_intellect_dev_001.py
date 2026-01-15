"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491591
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
    semantic_id="acu_v1.0.0_3_resistance_and_intellect_dev_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 3ResistanceAndIntellectDev(SemanticEntry):
    """
    **Source Text** (¶171, Lines 2764-2771):

> [171] Resistance to the mother can sometimes result in a...
    """
    
    original_text: str = """**Source Text** (¶171, Lines 2764-2771):

> [171] Resistance to the mother can sometimes result in a spontaneous development of intellect for the purpose of creating a sphere of interest in which the mother has no place. This development springs from the daughter's own needs and not at all for the sake of a man whom she would like to impress. Its real purpose is to break the mother's power by intellectual criticism and superior knowledge, so as to enumerate to her all her stupidities, mistakes in logic, and educational shortcomings. Intellectual development is often accompanied by the emergence of masculine traits in general.

**English Paraphrase**: Resistance to mother → spontaneous intellect development. Creates sphere where mother has no place. Purpose = break mother's power by intellectual criticism. Accompanied by masculine traits.

**中文诠释**: 对母亲的抵抗 → 自发智力发展。创造母亲无处容身的领域。目的 = 用智力批评打破母亲权力。伴随男性特质出现。

**Narrative Snippets**:
- `[ns_cw9i_III_171]` `[trigger: resistance_intellect]` `[factor_trigger: jung_mother AND jung_intellect]` `[role: 主干]` Resistance to mother can result in spontaneous intellect development—to break mother's power by criticism. → ¶171"""
    normalized_text_zh: str = """"""
    subject: str = "3 Resistance and Intellect Development (¶171)"
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
        l1_anchor="acu_v1.0.0_3_resistance_and_intellect_dev_001_L1",
    )
    version: str = "1.0.0"
