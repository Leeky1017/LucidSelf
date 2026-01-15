"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134366
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
    semantic_id="tis_v1.0.0_time_of_birth__houses__and_cha_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class TimeOfBirthHousesAndCha(SemanticEntry):
    """
    **Source Text**:
When the Englishman in our sample birthchart was born, it was six-thirty in the eve...
    """
    
    original_text: str = """**Source Text**:
When the Englishman in our sample birthchart was born, it was six-thirty in the evening on the ninth day of October. At that time the sun is in Libra—we know that from the date alone. The sun stays in Libra until around October 21. The sun’s sign position is not affected by the time of day, but knowing that the clocks read six-thirty in the evening does tell us something significant: that Libran sun had just set. In other words, it lies in the sixth house.
Had the Englishman been born a few hours later, the sun would have been much farther below the horizon. The sun would still be in Libra. But now it would lie in the fourth house instead of in the sixth. During that short period of time, the sun’s motion through the signs is inconsequential. But its motion through the houses is enough to completely alter the shape of the birthchart.
That is why the time of birth is such a critical factor in astrology. The date alone would be enough to establish the relationship of signs to planets, but we need the time in order to add the crucial birthchart element of the houses.
...
Some people confuse signs and houses at first. A good way to keep them separated in your mind is to remember that houses are linked to the local horizon, while signs are linked to space itself.

**Key Term Analysis**:
- `time of birth as critical factor`: the role of clock time in determining house positions and chart shape.
- `sign vs house position`: sign positions depend on date; house positions depend on local time and horizon.
- `chart shape`: the overall distribution of planets across houses, altered by changes in birth time.
- `local horizon`: the observer’s horizon that anchors the house system to a specific place and moment.

**English Paraphrase (Primary Language)**:
Forrest uses an example chart to show why birth time matters so much. The date alone tells us that the sun is in Libra; that sign position would be the same all day. But knowing it was six‑thirty in the evening tells us something entirely different: the Libra sun had just set and therefore lies in the sixth house. If the same person had been born a few hours later, the sun would still be in Libra but would have rotated farther below the horizon into the fourth house. In a few hours, the sign stays constant while the house position—and thus the overall shape of the chart—changes dramatically.

This is why time of birth is a critical input in astrology. The date establishes the relationship of signs to planets, but only the exact time and location anchor those symbols to the local horizon, creating the houses. Signs belong to space itself; houses belong to the observer’s viewpoint on earth. Forgetting this distinction leads people to confuse sign meanings with house meanings. Remembering that houses are tied to the horizon while signs are tied to the ecliptic keeps the map clear.

**Complete Chinese Interpretation (Secondary Language)**:
Forrest 通过样例命盘来说明「出生时间」为什么如此关键。同一天里，太阳都会待在天秤座——日期足以确定它的星座位置，这一点不会因为早晨或晚上而改变。但当我们知道那一刻是晚上六点半时，信息立刻不同了：那颗天秤座太阳刚刚落下地平线，因此它位于第六宫。如果同一个人在几小时之后才出生，太阳仍然在天秤座，却会沿着地球自转路径进一步沉入地平线之下，落入第四宫。短短几个小时内，星座位置几乎不变，但宫位位置却改变了整张命盘的形状。

这就是为什么「出生时间」在占星中是一个决定性的输入。仅靠日期，我们只能建立行星与星座之间的关系；只有加上精确的时间与地点，才能把这些符号固定到具体的「地方视角」，也就是本地地平线与宫位结构。星座属于空间本身，与黄道运行相关；宫位则属于观察者的视角，与地平线和自转节奏相关。若忽略这种区分，就很容易在解读时把星座含义与宫位含义混在一起。记住「星座连着天空，宫位连着地平线」，命盘这张地图才不会被看乱。

**Core Points**:
- Date alone fixes sign positions; birth time determines house positions and chart shape.
- The same sun in Libra can lie in different houses depending on time of day.
- Houses are linked to the local horizon and observer’s viewpoint, unlike signs.
- Time of birth is essential for adding the house dimension to the chart.

**Detailed Explanation**:
This passage clarifies a technical but crucial distinction for both students and engine designers. Signs track a planet’s motion along the ecliptic over weeks and months; houses track its apparent motion through the sky over hours. The date tells us "where" a planet is in the zodiac, but not where it was relative to the horizon at the moment of birth. Because houses describe life arenas, a shift in birth time can redirect the same symbolic energy into very different fields—home versus work, private versus public, inner versus outer.

For calibration work, this implies that any serious interpretation must treat birth time as non‑optional. Without it, we can speak only in broad, sign‑level generalities. With it, we gain a much higher resolution map that can distinguish people born on the same day but at different times and places. This "chart resolution" concept is vital for understanding why accurate data and precise house calculations matter.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The key sentences about the sun still being in Libra while moving from the sixth to the fourth house are preserved in substance, since they carry the core teaching. The language about "completely alter the shape of the birthchart" is kept conceptually to motivate why time of birth is critical.
- **中文**：译文中用「星座几乎不变、宫位剧烈变化」来凸显时间的作用，并用「命盘形状」对应 chart shape 的概念，以方便后续在因子层引入「分辨率/精度」一类设计。对「linked to the local horizon」则译为「连着本地地平线」，保持直观空间感。

**Narrative Snippets**:
- `[ns_innersky_063]` `[trigger: birth_time_importance]` `[factor_trigger: astro_time AND astro_chart]` `[role: 主干]` Time of birth is a critical factor—it completely alters the shape of the birthchart. → Source Text
- `[ns_innersky_064]` `[trigger: sign_vs_house]` `[factor_trigger: astro_sign AND astro_house]` `[role: 主干依赖]` The sun's sign position is not affected by time of day, but house position changes dramatically in hours. → Source Text
- `[ns_innersky_065]` `[trigger: houses_horizon]` `[factor_trigger: astro_house AND astro_horizon]` `[role: 条件分支]` Houses are linked to the local horizon, while signs are linked to space itself—a good way to keep them separated. → Source Text
- `[ns_innersky_066]` `[trigger: chart_resolution]` `[factor_trigger: astro_time AND astro_resolution]` `[role: 总结]` The date establishes signs to planets; we need the exact time to add the crucial element of houses. → Source Text
- `[ns_innersky_067]` `[trigger: same_sign_different_house]` `[factor_trigger: astro_sign AND astro_house]` `[role: 主干]` Same Libra sun could lie in the sixth house or fourth house depending on birth time. → Source Text"""
    normalized_text_zh: str = """"""
    subject: str = "Time of Birth, Houses, and Chart Resolution"
    factor_refs: list = ['source_ref', 'rel_inner_sky_time_001', 'birth_time_accuracy', 'evi_inner_sky_time_001', 'rule_birth_time_critical', 'concept_chart_precision', 'shichen_jingdu', 'dream_timing_precision']
    
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
        l1_anchor="tis_v1.0.0_time_of_birth__houses__and_cha_001_L1",
    )
    version: str = "1.0.0"
