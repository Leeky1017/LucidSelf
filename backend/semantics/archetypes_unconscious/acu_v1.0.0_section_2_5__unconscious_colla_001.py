"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.541762
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
    semantic_id="acu_v1.0.0_section_2_5__unconscious_colla_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class Section25UnconsciousColla(SemanticEntry):
    """
    **Source Text** (¶504-510, Lines 7828-7898):

> [504] Unfortunately, the facts show the exact opposi...
    """
    
    original_text: str = """**Source Text** (¶504-510, Lines 7828-7898):

> [504] Unfortunately, the facts show the exact opposite: consciousness succumbs all too easily to unconscious influences, and these are often truer and wiser than our conscious thinking. Indeed, the fate of the individual is largely dependent on unconscious factors.
>
> [505] Normally the unconscious collaborates with the conscious without friction. But when an individual or social group deviates too far from their instinctual foundations, they experience the full impact of unconscious forces. The collaboration of the unconscious is intelligent and purposive, and even when it acts in opposition to consciousness its expression is still compensatory.
>
> [506] Some people prefer to assume that impressive dreams derive from a "superconsciousness." This "higher" consciousness corresponds to what we in the West call the "unconscious."
>
> [507-508] I was never able to discover in the unconscious anything like a personality comparable with the ego. But if fragments have personality, the whole from which they were broken off must have personality to an even higher degree. Personality need not imply consciousness—it can be dormant or dreaming.

**English Paraphrase**:
- Consciousness succumbs to unconscious—often truer and wiser
- Fate largely depends on unconscious factors
- Unconscious collaboration: intelligent, purposive, compensatory
- "Superconsciousness" (East) = "unconscious" (West)
- No ego-personality in unconscious, but if fragments have personality, whole must too
- Personality can be dormant or dreaming

**中文诠释**：
- 意识屈服于无意识——往往更真实更智慧
- 命运很大程度取决于无意识因素
- 无意识协作：智能的、有目的的、补偿性的
- "超意识"（东方）="无意识"（西方）
- 无意识中无自我人格，但碎片有人格则整体更有
- 人格可以休眠或做梦

**Narrative Snippets**:
- `[ns_cw9i_VIII_003a]` `[trigger: unconscious_wisdom]` `[factor_trigger: jung_unconscious AND jung_wisdom]` `[role: 主干]` Unconscious often truer and wiser than conscious; fate depends on it. → ¶504
- `[ns_cw9i_VIII_003b]` `[trigger: unconscious_collaboration]` `[factor_trigger: jung_unconscious AND jung_compensation]` `[role: 主干依赖]` Unconscious collaboration is intelligent, purposive, compensatory. → ¶505
- `[ns_cw9i_VIII_003c]` `[trigger: fragment_personality]` `[factor_trigger: jung_personality AND jung_self]` `[role: 条件分支]` If fragments have personality, the whole must have it to higher degree. → ¶508"""
    normalized_text_zh: str = """"""
    subject: str = "Section 2.5: Unconscious Collaboration (¶504-510)"
    factor_refs: list = ['unc_wisdom', 'unc_collaboration', 'dormant_personality']
    
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
        l1_anchor="acu_v1.0.0_section_2_5__unconscious_colla_001_L1",
    )
    version: str = "1.0.0"
