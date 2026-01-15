"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192659
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
    semantic_id="tb_v1.0.0_the_parents__chapter_v_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheParentsChapterV(SemanticEntry):
    """
    **Source Text** (Lines 4980-5060):
> In conformity with nature, the Sun and Saturn are allotted to t...
    """
    
    original_text: str = """**Source Text** (Lines 4980-5060):
> In conformity with nature, the Sun and Saturn are allotted to the person of the father; and the Moon and Venus to that of the mother... the degree of their fortune and wealth will be indicated by the doryphory, or attendants of the luminaries. If the luminaries be accompanied by the benefics, a conspicuous and brilliant fortune is presaged... If Jupiter or Venus be configurated with the Sun or Saturn, the father will live long; if Mars be elevated above or ascend in succession to the Sun, the father will die suddenly or receive injury.

**English Paraphrase (Primary Language)**:
Ptolemy assigns **significators for parents**:
- **Father**: Sun (primary) + Saturn (secondary)
- **Mother**: Moon (primary) + Venus (secondary)

**Fortune indicators**: The "doryphory" (bodyguard planets attending the luminaries) shows parental wealth:
- Benefics attending = brilliant fortune
- Malefics attending = humble circumstances
- Mixed = vicissitudes

**Longevity of Father**: Jupiter/Venus aspecting Sun/Saturn = long life; Mars in elevation = sudden death or injury.

**Longevity of Mother**: Jupiter/Venus aspecting Moon/Venus = long life; Mars/Saturn afflicting Moon = death by disease or childbirth.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密分配了**父母的征象星**：
- **父亲**：太阳（主要）+ 土星（次要）
- **母亲**：月亮（主要）+ 金星（次要）

**财富指标**："护卫星"（随行发光体的行星）显示父母财富：
- 吉星随行 = 显赫财富
- 凶星随行 = 卑微处境
- 混合 = 起伏

**父亲寿命**：木星/金星相位太阳/土星 = 长寿；火星高居 = 突然死亡或受伤。

**Core Points**:
- Sun/Saturn = father significators; Moon/Venus = mother significators
- Doryphory (attendant planets) indicates parental fortune
- Benefics = prosperity; Malefics = hardship
- Mars elevated over Sun/Saturn = father's sudden death
- Saturn/Mars afflicting Moon = mother's health problems

**Narrative Snippets**:
- `[ns_tetra_iii011]` `[trigger: parent_significators]` `[factor_trigger: astro_sun_father OR astro_moon_mother]` `[role: 主干]` Sun and Saturn signify the father; Moon and Venus signify the mother. → Source Text III.5
- `[ns_tetra_iii012]` `[trigger: doryphory_fortune]` `[factor_trigger: astro_planet_attendants]` `[role: 条件分支]` The doryphory (attendant planets) of the luminaries indicates parental fortune and status. → Source Text III.5
- `[ns_ptolemy_iii_030]` `[trigger: father_longevity]` `[factor_trigger: astro_sun_saturn AND astro_mars]` `[role: 条件分支]` Jupiter/Venus aspecting Sun/Saturn indicates father's long life; Mars elevated = sudden death. → Longevity
- `[ns_tetra_iii_ff]` `[trigger: father_fortune]` `[factor_trigger: father_fortune]` `[role: 效果]` Father's fortune determined by planets attending Sun/Saturn: benefics = eminence, malefics = humble condition. → Source Text III.5
- `[ns_tetra_iii_mf]` `[trigger: mother_fortune]` `[factor_trigger: mother_fortune]` `[role: 效果]` Mother's fortune determined by planets attending Moon/Venus: benefics = prosperity, malefics = obscurity. → Source Text III.5
- `[ns_tetra_iii_fs]` `[trigger: father_sig]` `[factor_trigger: father_sig]` `[role: 条件分支]` Father significators are Sun (diurnal) and Saturn (nocturnal)—examined for paternal fortune and longevity. → Source Text III.5
- `[ns_tetra_iii_mothersig]` `[trigger: mother_sig]` `[factor_trigger: mother_sig]` `[role: 条件分支]` Mother significators are Moon (diurnal) and Venus (nocturnal)—examined for maternal fortune and longevity. → Source Text III.5

**Textual Criticism**: N/A: Standard significator assignment in classical tradition."""
    normalized_text_zh: str = """"""
    subject: str = "The Parents (Chapter V)"
    factor_refs: list = ['parent_sig', 'doryphory']
    
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
        l1_anchor="tb_v1.0.0_the_parents__chapter_v_001_L1",
    )
    version: str = "1.0.0"
