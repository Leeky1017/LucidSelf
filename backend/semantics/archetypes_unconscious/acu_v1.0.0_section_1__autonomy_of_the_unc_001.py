"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.541733
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
    semantic_id="acu_v1.0.0_section_1__autonomy_of_the_unc_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class Section1AutonomyOfTheUnc(SemanticEntry):
    """
    **Source Text** (¶496-500, Lines 7713-7776):

> [496] Such cases indicate that under certain conditi...
    """
    
    original_text: str = """**Source Text** (¶496-500, Lines 7713-7776):

> [496] Such cases indicate that under certain conditions the unconscious is capable of taking over the role of the ego. The consequence of this exchange is insanity and confusion, because the unconscious is not a second personality with organized and centralized functions but in all probability a decentralized congeries of psychic processes.
>
> [497] The autonomy of the unconscious therefore begins where emotions are generated. Emotions are instinctive, involuntary reactions which upset the rational order of consciousness by their elemental outbursts.
>
> [498] We call the unconscious "nothing," and yet it is a reality in potentia. The thought we shall think, the deed we shall do, even the fate we shall lament tomorrow, all lie unconscious in our today.
>
> [499] Dreams have been regarded, in all previous ages, less as historical regressions than as anticipations of the future, and rightly so... Whereas we think in periods of years, the unconscious thinks and lives in terms of millennia.

**English Paraphrase**: Unconscious can take over ego's role → insanity (unconscious = decentralized congeries, not organized personality). Autonomy begins with emotions—instinctive, involuntary, upsetting rational consciousness. Unconscious = "nothing" yet reality in potentia: tomorrow's thoughts, deeds, fate lie unconscious today. Dreams = anticipations of future. Conscious thinks in years; unconscious thinks in millennia.

**中文诠释**: 无意识可接管自我角色→精神错乱（无意识=去中心化聚合体，非有组织人格）。自主始于情感——本能的、非自愿的、扰乱理性意识。无意识="无"却是潜在现实：明天的思想、行为、命运今天潜伏于无意识中。梦=对未来的预期。意识以年计；无意识以千年计。

**Narrative Snippets**:
- `[ns_cw9i_VIII_001]` `[trigger: emotion_autonomy]` `[factor_trigger: jung_unconscious AND jung_emotion]` `[role: 主干]` Autonomy of unconscious begins with emotions—instinctive, involuntary, upsetting rational order. → ¶497
- `[ns_cw9i_VIII_002]` `[trigger: potentia_millennia]` `[factor_trigger: jung_unconscious AND jung_time]` `[role: 主干依赖]` Unconscious = reality in potentia; conscious thinks in years, unconscious in millennia. → ¶498-499"""
    normalized_text_zh: str = """"""
    subject: str = "Section 1: Autonomy of the Unconscious (¶496-500)"
    factor_refs: list = ['unconscious_autonomy', 'unconscious_potentia', 'millennia_thinking']
    
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
        l1_anchor="acu_v1.0.0_section_1__autonomy_of_the_unc_001_L1",
    )
    version: str = "1.0.0"
