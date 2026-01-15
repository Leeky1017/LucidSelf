"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.541775
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
    semantic_id="acu_v1.0.0_section_2_5__unconscious_super_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class Section25UnconsciousSuper(SemanticEntry):
    """
    **Source Text** (¶504-510, Lines 7828-7898):

> [504] Unfortunately, the facts show the exact opposi...
    """
    
    original_text: str = """**Source Text** (¶504-510, Lines 7828-7898):

> [504] Unfortunately, the facts show the exact opposite: consciousness succumbs all too easily to unconscious influences, and these are often truer and wiser than our conscious thinking. Also, it frequently happens that unconscious motives overrule our conscious decisions, especially in matters of vital importance. Indeed, the fate of the individual is largely dependent on unconscious factors. I have defined intuition as "perception via the unconscious."
>
> [505] Normally the unconscious collaborates with the conscious without friction or disturbance. But when an individual or a social group deviates too far from their instinctual foundations, they experience the full impact of unconscious forces. The collaboration of the unconscious is intelligent and purposive, and even when it acts in opposition to consciousness its expression is still compensatory in an intelligent way, as if trying to restore the lost balance.
>
> [506] Some dreams and visions are so impressive that people prefer to assume they derive from a "superconsciousness." This "higher" consciousness in Indian philosophy corresponds to what we in the West call the "unconscious." But if we assume a consciousness in the unconscious, we face the difficulty that no consciousness can exist without a subject, an ego.
>
> [507-508] I could never discover in the unconscious anything like a personality comparable with the ego. But the manifestations of the unconscious show traces of personalities. If such fragments have personality, the whole from which they were broken off must have personality to an even higher degree. Personality need not imply consciousness—it can be dormant or dreaming.
>
> [509-510] The general aspect of unconscious manifestations is chaotic and irrational, despite symptoms of intelligence and purposiveness. It seems to be a personality that was never awake and never conscious of its own continuity. I am convinced that evidence exists for more complete hidden personalities.

**English Paraphrase**:
- Consciousness succumbs to unconscious influences—often truer and wiser
- Fate largely dependent on unconscious factors
- Intuition = "perception via the unconscious"
- Unconscious collaboration: intelligent, purposive, compensatory
- "Superconsciousness" (Indian) = Western "unconscious"
- No consciousness without ego—but unconscious fragments have personality
- If fragments have personality → whole must have personality (dormant/dreaming)

**中文诠释**：
- 意识容易屈服于无意识影响——常更真实更智慧
- 命运大部分依赖无意识因素
- 直觉 = "通过无意识的知觉"
- 无意识合作：智能、有目的、补偿性
- 印度的"超意识" = 西方的"无意识"
- 无意识没有可比于自我的人格，但片段有人格痕迹
- 片段有人格 → 整体必有更高人格（休眠/做梦）

**Narrative Snippets**:
- `[ns_cw9i_VIII_504]` `[trigger: fate_unconscious]` `[factor_trigger: jung_fate AND jung_unconscious]` `[role: 主干]` Unconscious influences often truer and wiser than conscious thinking; fate largely dependent on unconscious. → ¶504
- `[ns_cw9i_VIII_505]` `[trigger: unc_balance]` `[factor_trigger: jung_unconscious AND jung_balance]` `[role: 主干依赖]` Unconscious collaboration is intelligent, purposive, compensatory—restoring lost balance. → ¶505
- `[ns_cw9i_VIII_508]` `[trigger: whole_personality]` `[factor_trigger: jung_self AND jung_personality]` `[role: 条件分支]` If fragments have personality, the whole must have personality—dormant or dreaming. → ¶508"""
    normalized_text_zh: str = """"""
    subject: str = "Section 2.5: Unconscious Superiority and Compensatory Function (¶504-510)"
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
        l1_anchor="acu_v1.0.0_section_2_5__unconscious_super_001_L1",
    )
    version: str = "1.0.0"
