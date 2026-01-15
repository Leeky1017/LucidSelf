"""
Auto-generated semantic module for waite_tarot
Generated at: 2025-12-05T13:30:19.952795
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
    semantic_id="wt_v1.0.0_the_sun__太阳_001",
    book_id="waite_tarot",
    engine_id="tarot"
)
class TheSun太阳(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Direct Light | Spiritual not reflected | Antithesis of Moon |
| Self-Knowing Spirit | Dawned consciousness | Above natural mind |
| Childlike Wisdom | Simplicity = wisdom | Restored world |
| Animal Conformity | Perfect alignment | Mind leads nature |

**Number**: XIX | **Element**: Sun | **Path**: Hod to Yesod

**Source Text** (condensed):
> "Naked child on white horse with red standard... transit from manifest light of this world to light of world to come, typified by heart of a child. The sun is that of consciousness in the spirit - the direct as antithesis of reflected light. Humanity has become a little child--simplicity and innocence in sense of wisdom. When self-knowing spirit has dawned in consciousness above natural mind, that mind leads forth animal nature in perfect conformity."

**Core**: **Direct Light & Self-Knowing Spirit** – Direct (not reflected) spiritual light, childlike wisdom, restored world, animal nature in perfect conformity.

**Chinese**: **太阳（直接之光与自知灵性）**——直接灵性之光（对比月亮反射光），孩童简单即智慧，自知灵性破晓，心智完美引导动物本性。

**Bilingual Terms**: Direct vs Reflected Light (直接vs反射光) | Self-Knowing Spirit Dawned (自知灵性破晓) | Restored World (恢复的世界)

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Waite's key contrast: Sun's direct light vs Moon's reflected light. "Self-knowing spirit has dawned in consciousness above natural mind." Childlike simplicity = wisdom. "Mind leads forth animal nature in perfect conformity."
- **中文**: 韦特关键对比：太阳直接光vs月亮反射光。"自知灵性在自然心智之上的意识中破晓"。孩童简单=智慧。"心智完美引导动物本性"。

**Narrative Snippets**:
- `[ns_waite_073]` `[trigger: sun_direct]` `[factor_trigger: tarot_sun AND direct_light]` `[role: 主干]` The sun is that of consciousness in the spirit—the direct as antithesis of reflected light; what Moon cannot reveal, Sun illuminates directly. → Core
- `[ns_waite_074]` `[trigger: sun_spirit]` `[factor_trigger: tarot_sun AND self_knowing]` `[role: 条件分支]` When self-knowing spirit has dawned in consciousness above the natural mind, that mind leads forth animal nature in perfect conformity. → Achievement
- `[ns_waite_075]` `[trigger: sun_childlike]` `[factor_trigger: tarot_sun AND childlike_wisdom]` `[role: 条件分支]` Simplicity and innocence in the sense of wisdom; the restored world—highest perfection attained through childlike purity. → Wisdom"""
    normalized_text_zh: str = """"""
    subject: str = "The Sun (太阳)"
    factor_refs: list = ['tarot_sun', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tarot_sun', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'new_candidate', 'tarot_semantic', 'source_ref', 'rel_waite_055', 'tarot_sun', 'opposing', 'rel_waite_056', 'tarot_sun', 'elevating', 'rel_waite_057', 'tarot_sun', 'harmonizing', 'evi_waite_037', 'tarot_sun', 'rule_waite_sun_direct', 'evi_waite_038', 'tarot_sun', 'rule_waite_sun_conformity', 'concept_direct_light', 'bing_fire_direct', 'self_realization', 'concept_childlike_wisdom', 'child_dream']
    
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
        l1_anchor="wt_v1.0.0_the_sun__太阳_001_L1",
    )
    version: str = "1.0.0"
