"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251565
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
    semantic_id="pit_v1.0.0_saturn_return__ages_29_30__58__001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SaturnReturnAges293058(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "Saturn return occurs when transiting Saturn returns to i...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "Saturn return occurs when transiting Saturn returns to its natal position, completing one full 29.5-year cycle. This marks major life restructuring: the first return (ages 29-30) ends youth and demands adult responsibility; the second return (ages 58-60) brings legacy questions and elder wisdom."

**English Paraphrase (Primary Language)**:
**Saturn return** is the most significant milestone in the Saturn cycle: the moment when transiting Saturn returns to its exact natal position. This occurs approximately every 29.5 years—first return around ages 29-30, second return around ages 58-60. Hand emphasizes that Saturn returns are **reality testing points** where everything you've built is examined for authenticity and durability. The **first Saturn return** (late 20s) is the classic "end of youth" moment—you can no longer hide behind youthful excuses; you must accept adult responsibility for your life. Structures that lack foundation crumble; authentic structures strengthen. The **second Saturn return** (late 50s) shifts focus from "building" to "legacy"—what have you created that's worth leaving behind? What needs to be released? Both returns are psychologically intense because Saturn demands honesty about what's real.

**Complete Chinese Interpretation (Secondary Language)**:
**土星回归**是土星周期中最重要的里程碑：行运土星回到其精确本命位置的时刻。这大约每 29.5 年发生一次——第一次回归约在 29–30 岁，第二次回归约在 58–60 岁。汉德强调土星回归是**现实考验点**，你建立的一切都被审视其真实性和耐久性。**第一次土星回归**（20 多岁末）是经典的"青春结束"时刻——你不能再躲在青年借口后面；你必须为自己的人生承担成人责任。缺乏基础的结构会崩塌；真实的结构会加强。**第二次土星回归**（50 多岁末）将焦点从"建立"转向"遗产"——你创造了什么值得留下？什么需要被释放？两次回归在心理上都很强烈，因为土星要求对什么是真实的诚实。

**Key Term Analysis**:
- **Saturn Return**: `natal position return` / `29.5-year cycle completion` / `reality testing`
- **First Return**: `ages 29-30` / `end of youth` / `adult responsibility`
- **Second Return**: `ages 58-60` / `legacy questions` / `elder wisdom`

**Core Points** (decomposed, no upper limit):
- Saturn return = transiting Saturn returns to natal position
- Occurs approximately every 29.5 years
- First return: ages 29-30
- Second return: ages 58-60
- Major life restructuring point
- Reality testing: what's authentic strengthens, what's false crumbles
- First return: end of youth, begin adult responsibility
- Second return: legacy questions, elder wisdom
- Psychologically intense period
- Demands honesty about what's real

**Detailed Explanation**:
Saturn returns are nature's exams. The first return tests whether you've built a life on authentic foundations or on fantasy. The second return tests whether your life has meaning and legacy value. Both are humbling moments that separate the real from the illusory.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_035]` `[trigger: saturn_return_definition]` `[factor_trigger: astro_saturn_return]` `[role: 主干]` Saturn return occurs when transiting Saturn returns to natal position, completing one cycle. → Source Text
- `[ns_hand_pit_036]` `[trigger: first_return]` `[factor_trigger: astro_first_return]` `[role: 主干依赖]` First return (29-30) ends youth and demands adult responsibility. → Source Text
- `[ns_hand_pit_037]` `[trigger: second_return]` `[factor_trigger: astro_second_return]` `[role: 主干依赖]` Second return (58-60) brings legacy questions and elder wisdom. → Source Text
- `[ns_hand_pit_038]` `[trigger: reality_testing]` `[factor_trigger: astro_reality_testing]` `[role: 总结]` Saturn returns test authenticity: false structures crumble, real structures strengthen. → English Paraphrase

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A: Single authoritative source (Hand's "Planets in Transit" 1976). Saturn returns are standard in modern predictive astrology.
- **中文**: 无版本差异：单一权威来源（Hand《行运中的行星》1976）。土星回归在现代预测占星中是标准的。"""
    normalized_text_zh: str = """"""
    subject: str = "Saturn Return (Ages 29-30, 58-60) (土星回归)"
    factor_refs: list = ['astro_saturn_return', 'astro_first_return', 'astro_second_return', 'astro_reality_testing']
    
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_saturn_return__ages_29_30__58__001_L1",
    )
    version: str = "1.0.0"
