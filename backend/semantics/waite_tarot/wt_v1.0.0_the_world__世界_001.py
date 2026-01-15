"""
Auto-generated semantic module for waite_tarot
Generated at: 2025-12-05T13:30:19.952820
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
    semantic_id="wt_v1.0.0_the_world__世界_001",
    book_id="waite_tarot",
    engine_id="tarot"
)
class TheWorld世界(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Universe in God | Self-understanding | Cosmic rapture |
| Divine Vision | Soul's consciousness | Reflected from spirit |
| Morning Stars Sang | Job 38:7 | Original joy |
| Restored World | Highest perfection | Manifestation law |

**Number**: XXI | **Element**: Earth | **Path**: Yesod to Malkuth

**Source Text** (condensed):
> "Final message of Major Trumps. Perfection and end of Cosmos, secret within it, rapture of universe when it understands itself in God. State of soul in consciousness of Divine Vision, reflected from self-knowing spirit. Restored world when law of manifestation carried to highest natural perfection. Story of past: day all declared good, morning stars sang, Sons of God shouted for joy (Job 38:7)."

**Core**: **Cosmic Completion & Divine Vision** – Universe understanding itself in God, soul's Divine Vision, restored world, Creation's original joy.

**Chinese**: **世界（宇宙完成与神圣异象）**——宇宙在神中理解自己的狂喜，灵魂的神圣异象，恢复世界达到最高自然完美，创造的原初欢乐（伯38:7）。

**Bilingual Terms**: Universe Understanding Itself in God (宇宙在神中理解自己) | Divine Vision (神圣异象) | Morning Stars Sang (晨星歌唱-伯38:7)

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Waite: "Final message of Major Trumps." "Rapture of universe when it understands itself in God." "Soul in consciousness of Divine Vision, reflected from self-knowing spirit." "Morning stars sang, Sons of God shouted for joy" (Job 38:7).
- **中文**: 韦特："大塔罗的最终信息"。"宇宙在神中理解自己时的狂喜"。"灵魂在神圣异象意识中，从自知灵性反射"。"晨星歌唱，神子欢呼"(伯38:7)。

**Narrative Snippets**:
- `[ns_waite_079]` `[trigger: world_rapture]` `[factor_trigger: tarot_world AND cosmic_understanding]` `[role: 主干]` Rapture of the universe when it understands itself in God—perfection and end of the Cosmos, the secret within it. → Core
- `[ns_waite_080]` `[trigger: world_vision]` `[factor_trigger: tarot_world AND divine_vision]` `[role: 条件分支]` State of the soul in consciousness of Divine Vision, reflected from the self-knowing spirit. → Vision
- `[ns_waite_081]` `[trigger: world_morning]` `[factor_trigger: tarot_world AND original_joy]` `[role: 条件分支]` Story of the past when day all declared good, morning stars sang, Sons of God shouted for joy (Job 38:7). → Origin"""
    normalized_text_zh: str = """"""
    subject: str = "The World (世界)"
    factor_refs: list = ['tarot_world', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tarot_world', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'source_ref', 'rel_waite_061', 'tarot_world', 'completing', 'rel_waite_062', 'tarot_world', 'unifying', 'rel_waite_063', 'tarot_world', 'restoring', 'evi_waite_041', 'tarot_world', 'rule_waite_world_rapture', 'evi_waite_042', 'tarot_world', 'rule_waite_world_creation', 'concept_cosmic_completion', 'individuation_complete', 'concept_original_joy', 'paradise_dream']
    
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
        book_id="waite_tarot",
        chapter="",
        l1_anchor="wt_v1.0.0_the_world__世界_001_L1",
    )
    version: str = "1.0.0"
