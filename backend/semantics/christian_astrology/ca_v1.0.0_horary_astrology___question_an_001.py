"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147242
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
    semantic_id="ca_v1.0.0_horary_astrology___question_an_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class HoraryAstrologyQuestionAn(SemanticEntry):
    """
    #### Source Text

"Horary Questions are such Doubts and Queries whereof men and women require resolu...
    """
    
    original_text: str = """#### Source Text

"Horary Questions are such Doubts and Queries whereof men and women require resolution, which being propounded to the Astrologian, he shall, by Erecting a Figure upon that Question or Querie propounded, give a true and rationall Answer to the Propoundor. The Chart of Heaven must be framed exactly for the houre and minute of the time wherein the Question is propounded; for as wel in the very time of receiving the Question, as in the Radicall intention of him that asks, does the success or not success of the thing demanded depend."

#### Key Term Analysis

- **Horary (from Latin hora)**: "Of the hour"—astrology based on the exact moment a question is understood, not birth
- **Propounded/Propoundor**: Lilly's terms for question being asked and person asking; formal 17th-century legal language
- **Radicall Intention**: The genuine, sincere concern behind a question; "radical" = from root, essential
- **Figure**: The horoscope chart; "erecting a figure" = casting a chart for specific moment

#### English Paraphrase (Primary Language)

**Horary Astrology** (from Latin "hora" = hour) is the branch of astrology answering **specific questions** by casting a chart for the **exact moment** the astrologer comprehends the question. Unlike natal astrology examining lifelong character, horary delivers **one question, one chart, one answer**—focused predictions about specific outcomes.

**The core principle**: The heavens at the moment of inquiry **mirror the nature and outcome** of the matter questioned. This is **synchronicity** (Jung's term, though Lilly predates it)—meaningful coincidence between inner concern and outer celestial pattern.

**How it works**:
1. **Question formulated**: Querent (questioner) has specific, sincere concern
2. **Chart cast**: For moment astrologer understands question (not when querent first thought it)
3. **Significators assigned**: Planets representing querent and quesited (thing asked about)
4. **Judgment rendered**: Based on planetary relationships, aspects, houses, dignity
5. **Answer delivered**: Yes/no, timing, advice on action

**Question types** Lilly addresses:
- **7th house**: Will marriage occur? Is partner faithful? Success of lawsuit?
- **2nd house**: Will I recover debt? Find treasure? Gain wealth?
- **10th house**: Will I get job? Achieve honor? Succeed in career?
- **4th house**: Should I buy property? Where is hidden thing? Father's condition?
- **Lost objects**: Which house contains thing, timing of recovery

**Timing principles**:
- **Degrees to aspect**: Each degree = time unit (context determines if days, weeks, months)
- **Planetary speed**: Fast planet (Moon, Mercury) = quick; slow planet (Saturn) = delayed
- **Sign type**: Cardinal = fast, Fixed = slow, Mutable = moderate
- **Retrograde**: Delays, reversals, things coming back

**Distinction from natal astrology**:
- **Natal**: "Who am I?" (character, lifelong themes)
- **Horary**: "Will X happen?" (specific outcome, timing)
- **Chart moment**: Birth vs question understood
- **Scope**: Entire life vs one matter
- **Method**: Psychological analysis vs concrete prediction

**East-West parallel**: Horary closely parallels Chinese **六爻** (liuyao, six-line divination)—both answer specific questions using moment-based symbolic system, both use houses/lines for life areas, both predict timing.

#### Complete Chinese Interpretation (Secondary Language)

**卜卦占星**(Horary Astrology，源自拉丁语"hora"=小时)是占星学分支，通过为占星师理解问题的**精确时刻**起盘回答**具体问题**。不同于本命盘占星检查终生性格，卜卦提供**一个问题、一张盘、一个答案**——关于特定结果的聚焦预测。

**核心原则**：提问时刻的天象**镜像所询之事的性质和结果**。这是**同步性**(Jung术语，虽然Lilly早于它)——内在关切与外在天体模式之间有意义的巧合。

**如何运作**：(1)**问题成形**：问者有具体、真诚的关切；(2)**起盘**：为占星师理解问题的时刻(非问者首次想到时)；(3)**征象星分配**：代表问者和所问之事的行星；(4)**判断作出**：基于行星关系、相位、宫位、尊贵；(5)**答案交付**：是/否、时间、行动建议。

**问题类型** Lilly处理：第7宫(婚姻发生？伴侣忠诚？诉讼成功？)；第2宫(收回债务？找到宝藏？获得财富？)；第10宫(得到工作？获得荣誉？事业成功？)；第4宫(应买房产？隐藏物在哪？父亲状况？)；遗失物品(在哪宫、何时找回)。

**时间原则**：到相位的度数(每度=时间单位，语境决定是日/周/月)；行星速度(快行星如月亮/水星=快速；慢行星如土星=延迟)；星座类型(基本=快，固定=慢，变动=中等)；逆行(延迟、逆转、事情回来)。

**与本命占星区别**：本命盘"我是谁？"(性格、终生主题) vs 卜卦"X会发生吗？"(特定结果、时间)；盘的时刻：出生 vs 问题理解；范围：整个生命 vs 一个事项；方法：心理分析 vs 具体预测。

**东西对照**：卜卦占星密切对应中国**六爻**——两者都通过基于时刻的象征系统回答具体问题，都用宫位/爻位代表生活领域，都预测时间。

#### Core Points

- **Moment-based**: Chart cast for exact time astrologer understands question
- **Specific questions**: One question, one answer, concrete prediction
- **Synchronicity**: Heaven mirrors querent's situation at inquiry moment
- **Significators**: Planets represent querent and thing asked about
- **Judgment method**: Aspect relationships + house + dignity = answer
- **Timing prediction**: Degrees, planetary speed, sign type determine when
- **East-West parallel**: Similar to 六爻 (liuyao) question-focused divination

#### Detailed Explanation

William Lilly's "Christian Astrology" (1659) is the **foundational English text** on horary practice, still used by modern practitioners. Unlike earlier texts emphasizing theory, Lilly provides **systematic methodology** applicable to real questions.

**Historical context**: 17th century England, astrology at peak of respectability. Lilly consulted by nobility, clergy, common folk. His hundreds of documented case studies demonstrate method's applicability. "Christian" in title = acceptable to church (claimed divine sanction for astrological knowledge).

**Why it works** (Lilly's view): God created cosmos as unified whole. Celestial patterns aren't causes but **signs** (like smoke indicates fire). When person formulates genuine question, their concern "ripens" at moment astrologer receives it—that moment's chart symbolically encodes answer.

**Modern psychological view**: Horary chart externalizes querent's unconscious knowledge. Through symbolic system, intuition becomes conscious. Similar to Tarot—random-seeming selection actually reflects inner state.

**Question radicality** (readability): Some questions can't be read:
- **Early Ascendant** (<3°): Question premature, situation unformed
- **Late Ascendant** (>27°): Question too late, outcome already decided
- **Saturn/Mars on angles**: Heavy obstruction or violence
- **Via Combusta** (15° Libra - 15° Scorpio): Combusted zone, unclear judgment
- **Moon void of course**: No outcome, matter dissolves

**Ethical considerations**: Lilly insists on **sincere questions**. Testing astrologer produces unreadable charts. Questions about divine matters (salvation, prayer efficacy) deemed inappropriate—astrology for worldly concerns only.

**Practical application today**: Modern horary astrologers use Lilly's methods largely unchanged. Some additions: outer planets (Uranus, Neptune, Pluto) as rulers of modern concerns, computer chart calculation. Core principles remain: significators, aspects, houses, dignity, timing.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Lilly's "Christian Astrology" (1647/1659) is the first comprehensive English horary text, superseding Latin manuscripts. The title "Christian" was strategic—distancing from occultism during Puritan era. Lilly preserves Arabic-period techniques (via Bonatti, Guido) while adapting to English Protestant context. Modern Traditional Revival (since 1980s) returned to Lilly as authoritative source, often preferring him over later simplifications.
- **中文**: Lilly的《基督教占星学》(1647/1659)是第一部全面的英语占星学文本，取代了拉丁手稿。"基督教"标题是策略性的——在清教徒时代与神秘主义保持距离。Lilly保留了阿拉伯时期技术（通过Bonatti、Guido），同时适应英国新教语境。现代传统复兴（1980年代起）回归Lilly作为权威来源，常偏好他而非后来的简化版本。

**Narrative Snippets**:
- `[ns_lilly_001]` `[trigger: horary_definition]` `[factor_trigger: astro_horary AND astro_definition AND astro_question_answer AND astro_cosmic_mirror AND astro_binary_outcome AND astro_cross_system_parallel]` `[role: 主干]` Horary questions are doubts whereof men require resolution; erect a figure for the hour and give a true answer. → Source Text
- `[ns_lilly_002]` `[trigger: chart_moment]` `[factor_trigger: astro_chart AND astro_moment]` `[role: 主干依赖]` The chart must be framed exactly for the hour the question is propounded—success depends on this moment. → Source Text
- `[ns_lilly_003]` `[trigger: radicall_intention]` `[factor_trigger: astro_radical AND astro_intention AND astro_chart_validity AND astro_judgment_validity]` `[role: 条件分支]` Both the time of receiving the question and the radicall intention of the asker determine the outcome. → Source Text
- `[ns_lilly_004]` `[trigger: synchronicity]` `[factor_trigger: astro_synchronicity AND astro_inquiry AND astro_cosmic_mirror]` `[role: 总结]` The heavens at the moment of inquiry mirror the nature and outcome of the matter questioned. → English Paraphrase
- `[ns_lilly_005]` `[trigger: one_question_one_answer]` `[factor_trigger: astro_question AND astro_answer AND astro_binary_outcome]` `[role: 主干]` One question, one chart, one answer—horary delivers focused prediction about specific outcomes. → English Paraphrase
- `[ns_lilly_006]` `[trigger: liuyao_parallel]` `[factor_trigger: astro_horary AND bazi_liuyao AND astro_cross_system_parallel]` `[role: 主干依赖]` Horary closely parallels Chinese 六爻—both use moment-based symbolic systems for specific questions. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Horary Astrology - Question-Answering System"
    factor_refs: list = []
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_horary_astrology___question_an_001_L1",
    )
    version: str = "1.0.0"
