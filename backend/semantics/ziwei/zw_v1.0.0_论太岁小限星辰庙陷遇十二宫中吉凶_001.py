"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755858
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
    semantic_id="zw_v1.0.0_论太岁小限星辰庙陷遇十二宫中吉凶_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论太岁小限星辰庙陷遇十二宫中吉凶(SemanticEntry):
    """
    - 分字分词释义：

  - **太岁并小限**：流年太岁与小限同临某宫，该年主舞台所在，影响尤为集中。
  - **星辰庙陷**：星曜落在有利（庙旺）或不利（陷地）宫位的状态，决定化吉或化凶。
  ...
    """
    
    original_text: str = """- 分字分词释义：

  - **太岁并小限**：流年太岁与小限同临某宫，该年主舞台所在，影响尤为集中。
  - **星辰庙陷**：星曜落在有利（庙旺）或不利（陷地）宫位的状态，决定化吉或化凶。
  - **入庙化吉**：太岁小限所到宫位星曜在庙旺之地，该年易得财官双美、家道兴隆。
  - **不入庙化凶**：太岁小限所到宫位星曜陷地，该年易招官非、破财、灾悔、病患。
  - **所值吉星组合**：某年太岁所在宫三方有利星曜组合，遇吉星多者财禄进益、喜事重重。
  - **所值凶星组合**：某年太岁所在宫三方不利星曜组合，遇凶星多者财耗孝服、官灾口舌。
  - **减半论之**：凶象并非绝对，有上下浮动空间，需结合整体格局与现实环境综合判断。
  - **年度加权表**：本条可视为一份按十二地支年份展开的年度吉凶加权查询表。

- 原文（断句）（节要）：

  论太岁小限：

  星辰庙陷，遇十二宫中吉凶，依此判断，人行年灾患，响应如神。子年太岁并小限到子宫，入庙化吉，七杀破军在子宫守岁限……子年太岁并小限到子宫，不入庙化凶，紫微在子宫守命及岁限……子年太岁所值吉凶星：禄存、天机、天同、太阴、昌曲、辅弼、破军、天相、廉贞、武曲、天府、巨门、七杀，可断其年人财两美……若遇贪狼、紫微、天梁、忌星、太阳擎羊，便断人财耗散，官灾孝服口舌，本身灾悔，减半论之。

  丑年至亥年，逐一说明：太岁并小限到某宫时，若入庙化吉，则列出对何干支之人生财官双美、家道兴隆；若不入庙化凶，则列出招官非、破财、灾悔、病患等情形。又分别列出各年太岁所值之吉星与凶星组合：遇吉星多者，其年财禄进益、喜事重重；遇凶星与忌曜多者，其年财耗孝服、官灾口舌，本身疾病，往往「减半论之」，表示凶应虽重，但仍依格局强弱与现实选择有所浮动。

- 规范化释义（primary_lang_explained）：

  本条可以视作上一条「太岁逢吉凶星杀」的扩展表格版，从子年到亥年，将太岁与小限同临某宫时「入庙」与「不入庙」的情况，以及该年太岁所会吉凶星的组合一一列举。其核心逻辑有三：第一，看太岁并小限所到宫位本身的星曜是否在庙旺之地；第二，看该宫内主星与三方四正中吉星与凶星的多寡；第三，把这些信息与具体年干支与命主本局结合，来判断「财官双美」「多灾多悔」等不同年度主题。原文大量例举「某星在某宫，某干支出生者发福」「若某年太岁见某星与忌曜，则破财官非」等语句，本质上是将实践经验浓缩为一份「太岁小限用星表」。

  值得注意的是，经文中频繁出现「减半论之」之类表述，意味着这些凶象本身并非绝对，而是要结合整体格局、命主行为与现实环境综合判断。若太岁、小限虽到不利之宫，却同时会集强力吉星，且命主所在大限整体向上，则当年的坏事多半以「有惊无险」「破小财免大灾」的形式应验；反之，若本局与大限已偏凶，再加上太岁小限落陷、见多忌曜与恶杀，则同样一句「财耗官灾」在现实中可能表现为截然不同的等级。本条的价值在于：提供一套逐年逐宫的「权重表」，使占者在判断年度运势时，能系统地评估太岁、小限、星辰庙陷的综合影响。

- 完整对等诠释（secondary_lang_full）：

  This extended section is essentially a look-up table for the annual ruler and
  minor period across the twelve branch years. For each year from Zi through Hai
  it describes what happens when Tai Sui and the minor limit fall into a given
  house in dignity versus debility, and which combinations of stars around them
  count as especially helpful or harmful. The language is concrete—naming
  specific stems, houses and stars for which "fortune rises and wealth grows"
  versus those where lawsuits, losses, illness and mourning are more likely.

  For modern readers the repeated phrase "judge it at half strength" is a key
  signal that these descriptions are meant as weighted tendencies, not fixed
  sentences. The table can be treated as an annual weighting layer on top of the
  natal chart and major periods: if a given year’s Tai Sui is strong, supported
  by benefics and resonant with a good major period, opportunities are easier to
  seize; if it is weak, surrounded by malefics and echoing a harsh decade, the
  same year calls for caution, simpler plans and stronger safeguards. In this
  way the text invites practitioners to think in terms of probabilities and
  leverage points rather than absolute fates.

- 核心要点：

  1. 以子年至亥年为序，逐年列出太岁与小限同临某宫时，入庙化吉与不入庙化凶的不同结果。
  2. 为每一太岁年标明其「所值吉星组合」与「所值凶星组合」，据以判断当年的财官、婚姻、疾病等主题。
  3. 「减半论之」说明凶象有上下浮动空间，不能机械地等同于极端灾祸。
  4. 此条应与前条「流年太岁逢吉凶星杀」与大限、小限整体趋势合参，而非孤立使用。
  5. 现代实务中可将本条视为一份「年度加权表」，帮助把抽象的太岁位置转化为更具操作性的年度风险评分。"""
    normalized_text_zh: str = """"""
    subject: str = "论太岁小限星辰庙陷遇十二宫中吉凶"
    factor_refs: list = ['state_rumiao', 'state_taisuibingxiaoxian', 'group_suozhijixing', 'group_suozhixiongxing', 'modifier_jianbanlunzhi', 'source_ref', 'rel_taixiao_001', 'state_taisuibingxiaoxian', 'rel_taixiao_002', 'group_suozhijixing', 'rel_taixiao_003', 'modifier_jianbanlunzhi', 'evi_taixiao_001', 'state_rumiao', 'rule_taixiao_rumiao', 'evi_taixiao_002', 'modifier_jianbanlunzhi', 'rule_taixiao_jianban', 'concept_annual_table', 'concept_flexibility']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_论太岁小限星辰庙陷遇十二宫中吉凶_001_L1",
    )
    version: str = "1.0.0"
