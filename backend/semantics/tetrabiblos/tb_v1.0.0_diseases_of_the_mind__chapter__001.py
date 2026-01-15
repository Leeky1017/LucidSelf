"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192644
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
    semantic_id="tb_v1.0.0_diseases_of_the_mind__chapter__001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class DiseasesOfTheMindChapter(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Diseases of mind | Mental afflictions | Psychological pathology |
| Afflicted Mercury | Mercury under malefic influence | Rational dysfunction |
| Afflicted Moon | Moon under malefic influence | Emotional disturbance |

#### Source Text

"When Mercury and the Moon are afflicted by Saturn, and are neither in aspect to each other nor to the benefics, the native will be liable to diseases of the mind: such as melancholy, if Saturn be the afflicting planet; epilepsy, if Mars be the afflicting planet; and various forms of mania, if both malefics afflict."

#### English Paraphrase (Primary Language)

Mental afflictions arise when Mercury and Moon are:
1. **Afflicted by malefics** (Saturn or Mars)
2. **Not in aspect to each other** (disconnected reason and emotion)
3. **Not supported by benefics** (no moderating influence)

**Saturn affliction** produces melancholy, depression, excessive coldness—the native's mind becomes too contracted and heavy.

**Mars affliction** produces epilepsy, sudden eruptions, violence—the mind becomes too hot and unstable.

**Both malefics** produces complex mania—the mind is both contracted and explosive.

**Protective factors**: Jupiter or Venus aspects to Mercury/Moon moderate these tendencies.

#### Complete Chinese Interpretation (Secondary Language)

心理疾病在以下情况下产生：
1. **被凶星刑克**（土星或火星）
2. **彼此无相位**（理性和情感断开）
3. **无吉星支持**（无调和影响）

**土星刑克**产生忧郁、抑郁、过度冷漠——原命的心智变得过于收缩和沉重。

**火星刑克**产生癫痫、突然爆发、暴力——心智变得过热和不稳定。

**双凶星**产生复杂躁狂——心智既收缩又爆发性。

**保护因素**：木星或金星与水星/月亮的相位调和这些倾向。

#### Core Points

- **Dual affliction required**: Both Mercury and Moon affected
- **Saturn = melancholy**: Cold, contracted, depressive
- **Mars = epilepsy**: Hot, explosive, unstable
- **Both = mania**: Complex mental disturbance
- **Benefic protection**: Jupiter/Venus moderate afflictions

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Ptolemy's humoral approach to mental illness reflects Greco-Roman medical theory. Modern astrology interprets these symbolically rather than literally diagnosing conditions.
- **中文**: 托勒密对精神疾病的体液方法反映了希腊-罗马医学理论。现代占星术象征性地诠释这些而非字面诊断病症。

**Narrative Snippets**:
- `[ns_ptolemy_iii_009]` `[trigger: mental_disease]` `[factor_trigger: astro_mental_disease AND astro_affliction]` `[role: 主干]` Mental diseases arise when Mercury and Moon are afflicted by malefics without benefic support. → Source Text
- `[ns_ptolemy_iii_010]` `[trigger: saturn_affliction]` `[factor_trigger: astro_saturn AND astro_mars_affliction]` `[role: 条件分支]` Saturn affliction produces melancholy; Mars produces epilepsy; both produce mania. → Source Text
- `[ns_tetra_iii_sc]` `[trigger: saturn_cold]` `[factor_trigger: saturn_cold]` `[role: 条件分支]` Saturn's cold nature afflicting Mercury-Moon produces melancholy—contracted, depressive, cold mental states. → Ptolemy III
- `[ns_tetra_iii_mh]` `[trigger: mars_hot]` `[factor_trigger: mars_hot]` `[role: 条件分支]` Mars's hot nature afflicting Mercury-Moon produces epilepsy—explosive, eruptive, unstable mental states. → Ptolemy III"""
    normalized_text_zh: str = """"""
    subject: str = "Diseases of the Mind (Chapter XIX)"
    factor_refs: list = ['mental_disease', 'new_candidate', 'new_candidate']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_diseases_of_the_mind__chapter__001_L1",
    )
    version: str = "1.0.0"
