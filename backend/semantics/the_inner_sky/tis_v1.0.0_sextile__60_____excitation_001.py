"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.109931
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
    semantic_id="tis_v1.0.0_sextile__60_____excitation_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class Sextile60Excitation(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Sextile | 60° aspect, compatible elements | Excitation and vitality |
| Excitation | Mutual stimulation | Energizing dynamic |
| Fleeting | Transient enthusiasm | Sextile's challenge |

#### Source Text

"Sextiles produce excitation. They are intense, colorful, dynamic. Both planets are stimulated and enlivened. When two planets are joined by a sextile, it is as if they were a pair of teenagers falling in love for the first time. There is magic. There is humor. There is high energy. But there is little restfulness or stability."

#### English Paraphrase (Primary Language)

The **sextile** (60°) creates **excitation**: two planetary energies that stimulate and enliven each other. Unlike the trine's restful harmony, sextiles are **dynamic and colorful**—"like teenagers falling in love."

**The energy**: Sextiles produce magic, humor, high energy—but also instability. The enthusiasm can **flare up and subside** before much comes of it.

**Compatible elements**: Sextiles connect compatible but different elements (Fire-Air, Earth-Water), creating stimulating exchange rather than fusion.

#### Complete Chinese Interpretation (Secondary Language)

**六分相**（60度）创造**兴奋**：两种行星能量相互刺激和活化。不同于三分相的安逸和谐，六分相是**动态和多彩的**——"像青少年初次坠入爱河"。

**能量**：六分相产生魔力、幽默、高能量——但也有不稳定性。热情可能**突然爆发又消退**，还没产生什么就结束了。

**兼容元素**：六分相连接兼容但不同的元素（火-风、土-水），创造刺激交流而非融合。

#### Core Points

- **60° aspect**: Compatible but different elements
- **Excitation dynamic**: Mutual stimulation and vitality
- **High energy, low stability**: Magic but fleeting
- **Sustainment challenge**: Must direct the excitement productively

#### Detailed Explanation

The sextile connects planets in **compatible but different elements**—Fire with Air, Earth with Water. Unlike the trine's same-element ease, the sextile creates **stimulating difference**. The planets excite each other, generating vitality and magic through their complementary natures.

Forrest's key distinction from the trine: where trines rest in comfortable harmony, sextiles **spark and stimulate**. Fire and Air feed each other—ideas (Air) ignite action (Fire), and action generates new ideas. Earth and Water nourish each other—feelings (Water) ground in practical expression (Earth), and practical work evokes deeper feeling.

**Instability** is the sextile's challenge. The magic is real but fleeting—excitement tends to dissipate unless consciously directed. Sextiles often correlate with brilliant starts that fizzle, wonderful ideas that never materialize, relationships that burn bright then fade. The energy is there but requires **channeling and sustainment**.

The developmental task is to **harness the excitation** into productive expression. The sextile's vitality can accomplish much when disciplined—but without that discipline, it remains a series of exciting potentials that never quite manifest. The magic must be grounded.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Forrest distinguishes sextile from trine sharply: trine is restful harmony, sextile is exciting stimulation. This prevents conflating all "good" aspects.
- **中文**: Forrest明确区分六分相与三分相：三分相是安逸和谐，六分相是令人兴奋的刺激。这防止混淆所有"好"相位。

**Narrative Snippets**:
- `[ns_forrest_asp_009]` `[trigger: sextile]` `[factor_trigger: sextile AND stimulation]` `[role: 主干]` The sextile produces excitation—like teenagers falling in love: magic, humor, high energy, but little stability. → Source Text
- `[ns_forrest_asp_010]` `[trigger: excitation]` `[factor_trigger: aspect_sextile AND aspect_stimulation]` `[role: 主干依赖]` Sextile enthusiasm can flare up and subside before much comes of it—the challenge is sustainment. → English Paraphrase
- `[ns_forrest_asp_019]` `[trigger: compatible_elements]` `[factor_trigger: aspect_sextile AND element_compatible]` `[role: 条件分支]` Sextiles connect compatible but different elements (Fire-Air, Earth-Water), creating stimulating exchange rather than fusion. → Element
- `[ns_forrest_asp_020]` `[trigger: sextile_channeling]` `[factor_trigger: aspect_sextile AND aspect_direction]` `[role: 条件分支]` The sextile's vitality can accomplish much when disciplined—but without channeling, it remains exciting potential that never manifests. → Development"""
    normalized_text_zh: str = """"""
    subject: str = "Sextile (60°) - Excitation"
    factor_refs: list = ['aspect_sextile', 'new_candidate', 'new_candidate', 'engine_id', 'aspect_sextile', 'astro_semantic', 'new_candidate', 'astro_semantic', 'new_candidate', 'astro_semantic', 'source_ref', 'rel_forrest_sex_001', 'aspect_sextile', 'energizing', 'rel_forrest_sex_002', 'sextile', 'sustaining', 'evi_forrest_sex_001', 'rule_aspect_sextile', 'concept_sextile', 'liuhe_combination', 'excitement_dream']
    
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_sextile__60_____excitation_001_L1",
    )
    version: str = "1.0.0"
