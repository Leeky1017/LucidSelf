"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.541749
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
    semantic_id="acu_v1.0.0_section_2__unconscious_as_moth_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class Section2UnconsciousAsMoth(SemanticEntry):
    """
    **Source Text** (¶501-503, Lines 7795-7822):

> [501] The primitive "perils of the soul" consist mai...
    """
    
    original_text: str = """**Source Text** (¶501-503, Lines 7795-7822):

> [501] The primitive "perils of the soul" consist mainly of dangers to consciousness. Fascination, bewitchment, "loss of soul," possession, etc. are obviously phenomena of the dissociation and suppression of consciousness caused by unconscious contents. Even civilized man is not yet entirely free of the darkness of primeval times. The unconscious is the mother of consciousness.
>
> [503] As I have said, there is little hope of our finding in the unconscious an order equivalent to that of the ego. It certainly does not look as if we were likely to discover an unconscious ego-personality... Just as a human mother can only produce a human child, whose deepest nature lay hidden during its potential existence within her, so we are practically compelled to believe that the unconscious cannot be an entirely chaotic accumulation of instincts and images. There must be something to hold it together and give expression to the whole. Its centre cannot possibly be the ego, since the ego was born out of it into consciousness.

**English Paraphrase**: Perils of the soul = dangers to consciousness (fascination, possession = unconscious dissociating consciousness). Unconscious = mother of consciousness. No ego-order in unconscious, but not entirely chaotic either. Something holds it together. Centre cannot be ego (ego born FROM unconscious into consciousness).

**中文诠释**: 灵魂的危险=意识的危险（迷惑、附身=无意识分离意识）。无意识=意识之母。无意识中无自我秩序，但也非完全混乱。有东西将其维系。中心不可能是自我（自我从无意识中诞生进入意识）。

**Narrative Snippets**:
- `[ns_cw9i_VIII_003]` `[trigger: mother_consciousness]` `[factor_trigger: jung_unconscious AND jung_ego]` `[role: 主干]` Unconscious is the mother of consciousness—ego was born out of it. → ¶501-503"""
    normalized_text_zh: str = """"""
    subject: str = "Section 2: Unconscious as Mother of Consciousness (¶501-503)"
    factor_refs: list = ['unconscious_mother', 'perils_of_soul', 'non_chaotic']
    
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
        l1_anchor="acu_v1.0.0_section_2__unconscious_as_moth_001_L1",
    )
    version: str = "1.0.0"
