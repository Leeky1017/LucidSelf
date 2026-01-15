"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238012
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
    semantic_id="ap_v1.0.0_entry_5__houses_and_zodiac_ind_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry5HousesAndZodiacInd(SemanticEntry):
    """
    **Source Text** (Lines 6154-6258):
> In astrological symbolism this axial rotation of the Earth is c...
    """
    
    original_text: str = """**Source Text** (Lines 6154-6258):
> In astrological symbolism this axial rotation of the Earth is charted by means of the circle or wheel of houses. The twelve houses are twelve phases of this daily motion of the Earth... the circle of houses should be understood more specifically as the dial of a clock...
>
> The zodiac gives us therefore first of all a picture of the cyclic unfoldment of the life-force, both in nature and in man; then it also provides us with a background for the development of the complex pattern of inter-planetary... relationships...
>
> The zodiac becomes thus a series of points of references which enables us to plot accurately the position of all planets and of the Sun in relation to the orbital motion of the Earth.

**Key Term Analysis**:
- **Houses (12)**: `axial rotation charted` / `dial of clock` / `sequential development of individual selfhood`
- **Zodiac**: `cyclic unfoldment of life-force` / `background for planetary relationships` / `orbital motion reference`
- **Horizon (horizontal axis)**: `dualism of consciousness` / `subjective-objective, self-others`
- **Meridian (vertical axis)**: `noon-point` / `solar sustainment` / `connection with universal vitalizing forces`

**English Paraphrase (Primary Language)**:
**Houses** = 12 phases of daily (axial) motion, "dial of a clock," charting individual selfhood development. **Zodiac** = cyclic unfoldment of life-force, background for planetary relationships, tied to orbital revolution (collective).

The **horizontal axis (horizon)** = dualism of consciousness (subjective/objective). The **vertical axis (meridian)** = point of solar sustainment, connection with universal forces. The Ascendant particularizes; the Mid-Heaven universalizes.

**Complete Chinese Interpretation (Secondary Language)**:
**宫位** = 日（轴向）运动的12个阶段，"时钟表盘"，描绘个体自性发展。**黄道带** = 生命力的周期性展开，行星关系的背景，与轨道公转（集体）相关。

**水平轴（地平线）** = 意识的二元性（主观/客观）。**垂直轴（子午线）** = 太阳维持点，与宇宙活化力量的连接。上升点使之特殊化；中天使之普遍化。

**Narrative Snippets**:
- `[ns_aop_142]` `[trigger: houses_dial]` `[factor_trigger: astro_houses_as_dial AND astro_cycles_7 AND astro_houses_zodiac]` `[role: 主干]` Houses: 12 phases of daily motion, dial of clock, individual selfhood development. → L6154-6160
- `[ns_aop_143]` `[trigger: zodiac_lifeforce]` `[factor_trigger: astro_zodiac_lifeforce]` `[role: 主干依赖]` Zodiac: cyclic unfoldment of life-force, planetary relationship background, collective. → L6250-6258
- `[ns_aop_144]` `[trigger: two_axes]` `[factor_trigger: astro_chart_axes AND astro_conjunction]` `[role: 总结]` Horizontal axis = consciousness dualism; Vertical axis = solar sustainment. → L6212-6224"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 5: Houses and Zodiac—Individual and Collective Symbols"
    factor_refs: list = ['houses_circle', 'zodiac', 'axis_horizon', 'axis_meridian']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_5__houses_and_zodiac_ind_001_L1",
    )
    version: str = "1.0.0"
