"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994641
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
    semantic_id="pt_v1.0.0_card_19__the_sun_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Card19TheSun(SemanticEntry):
    """
    ### Joy, Simplicity, Lucidity

#### Key Term Analysis

| Term | Definition | Significance |
|------|...
    """
    
    original_text: str = """### Joy, Simplicity, Lucidity

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Number 19 | 9+1 wisdom+force | Hermit transformed |
| Lucid | Filled with light | Enlightenment |
| Naked Child | Innocence regained | Holy child |
| Eden Regained | Garden within | Never lost |

**Source Text**: By accepting Moon's fearful images we bring energy outside, giving all life radiance. Under the Sun everything becomes simple, joyous, physical. Light of unconscious brought into daily life. Enlightenment is experience, not idea. Person feels struck by burst of light, world seen as spiritual and eternal. The sunstruck person feels sense of wisdom, seeing everything with total clarity. 'Lucid' literally means 'filled with light'.

**English Paraphrase**:

**The Sun** = **Joy**, **Clarity**, **Childlike Wonder** — energy externalized, world radiant, Eden regained.

**Core Symbolism**:
- **Number 19**: 1+9=10 (Wheel vision now internal), 19=9 (Hermit) + 1 (Magician) = wisdom + force united
- **Sun's light**: Own light (vs. Moon reflects), knowledge, life-giving

**Visual**:
- **Naked child** on white horse = innocence regained, holy child (body adult but spirit child)
- **Red banner** = vitality, freedom
- **Stone wall** = past narrow life escaped
- **Sunflowers** (four) = heliotropism, four elements
- **Garden** = Eden within, never lost

**vs. Moon**: Active energized (Moon passive surrender), joy after test

**Enlightenment universal**: Burst of light (yod drops colored), world spiritual/eternal, childlike joy beyond child's fear (traveled through darkness), wisdom/clarity, "lucid" = filled with light

**Number**: 19 = Hermit lantern bursts forth (Abulafia's ecstatic third level), Hermit transformed into open child. 1+9=10 (Wheel external vision→Sun internal vision)

**完整中文诠释**:
**太阳**=**喜悦**、**清澈**、**赤子奇迹**——能量外化、世界辉映、伊甸重获。**数字19**：1+9=10（轮之愿景现内在），19=9（隐者）+1（魔术师）=智慧+力量统一；**太阳光**：自身之光（vs月亮反射）、知识、赋生。**图像**（RWS牌）：白马上**裸童**=纯真重获、圣婴（身体成人但灵性孩童）；**红旗**=生命力、自由；**石墙**=狭隘过往生命逃脱；**向日葵**（四朵）=向日性、四元素；**花园**=内在伊甸、从未失落。**vs月亮**：主动活力（月亮被动臣服），考验后喜悦。**普世开悟**：光爆（yod滴彩色），世界灵性/永恒，超越孩童恐惧之童真（穿越黑暗后），智慧/清澈，"lucid"（澄明）=充满光。**数字**：19=隐者灯笼爆发（阿布拉菲亚狂喜第三层），隐者转化为开放孩童。1+9=10（轮外在愿景→太阳内在愿景）。通过接受月亮恐惧图像我们将能量带出，赋予所有生命辉映。太阳下一切变简单、喜悦、实体。无意识之光带入日常生活。开悟是体验，非理念。人感被光爆击中，世界被见为灵性与永恒。太阳击中之人感智慧感，以全然清澈见一切。'Lucid'字面意义'充满光'。

**Narrative Snippets**:
- `[ns_78deg_163]` `[trigger: sun_major]` `[factor_trigger: tarot_major_sun AND sequence_moon_sun AND state_lucid AND tarot_number_19 AND symbol_naked_child AND symbol_sun_light]` `[role: 主干]` The Sun represents joy and clarity after Moon's fears—energy brought outside, world seen as spiritual and eternal; enlightenment as experience. → English Paraphrase
- `[ns_78deg_164]` `[trigger: celestial_sun_ruling]` `[factor_trigger: celestial_sun]` `[role: 主干]` Sun emits its own light (unlike Moon's reflection)—knowledge, life-giving, illumination; the source of consciousness and clarity. → English Paraphrase
- `[ns_78deg_353]` `[trigger: naked_child_sun]` `[factor_trigger: tarot_major_sun AND symbol_child]` `[role: 条件分支]` Naked child on white horse—innocence regained, holy child (body adult but spirit child); red banner of vitality and freedom; stone wall marking past narrow life escaped. → Visual Elements
- `[ns_78deg_354]` `[trigger: lucid_filled_light]` `[factor_trigger: tarot_major_sun AND state_lucidity]` `[role: 条件分支]` 'Lucid' literally means 'filled with light'—sunstruck person feels burst of light, world seen as spiritual and eternal, seeing everything with total clarity. → Source Text
- `[ns_78deg_355]` `[trigger: sun_number_19]` `[factor_trigger: tarot_major_sun AND number_19]` `[role: 条件分支]` Number 19 = 9 (Hermit) + 1 (Magician) = wisdom + force united; Hermit's lantern bursts forth; 1+9=10 (Wheel's external vision becomes Sun's internal). → Core Symbolism
- `[ns_78deg_356]` `[trigger: eden_regained]` `[factor_trigger: tarot_major_sun AND symbol_garden AND state_eden_regained]` `[role: 条件分支]` Four sunflowers = heliotropism, four elements turning to light; Garden = Eden within, never lost; childlike joy beyond child's fear (traveled through darkness). → Visual Elements
- `[ns_78deg_357]` `[trigger: sun_vs_moon]` `[factor_trigger: tarot_major_sun AND tarot_major_moon]` `[role: 总结]` Sun vs Moon: active/energized (vs passive/surrender), joy after test; enlightenment not as idea but experience; Moon's fears accepted and transformed into radiance. → vs. Moon
- `[ns_78deg_475]` `[trigger: hermit_transformed]` `[factor_trigger: tarot_major_sun AND tarot_major_hermit]` `[role: 条件分支]` Hermit transformed into open child—the lantern bursts forth; solitary wisdom becomes radiant joy shared with all; inner light now visible to the world. → Number Symbolism
- `[ns_78deg_505]` `[trigger: simplicity_under_sun]` `[factor_trigger: tarot_major_sun AND state_simplicity]` `[role: 条件分支]` Under the Sun everything becomes simple, joyous, physical—complexity dissolves in light; the tangled becomes clear; no shadow remains to confuse. → Source Text

---"""
    normalized_text_zh: str = """"""
    subject: str = "Card 19: The Sun"
    factor_refs: list = ['tarot_major_sun', 'tarot_number_19', 'state_lucid', 'symbol_naked_child', 'state_eden_regained']
    
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
        book_id="pollack_tarot",
        chapter="",
        l1_anchor="pt_v1.0.0_card_19__the_sun_001_L1",
    )
    version: str = "1.0.0"
