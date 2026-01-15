"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523729
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
    semantic_id="zpzq_v1.0.0_其性情何也_盖既有配合_必有向背_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 其性情何也盖既有配合必有向背(SemanticEntry):
    """
    - **原文（source_text）**：

  其性情何也？盖既有配合，必有向背。如甲用辛官，透丙作合，而官非其官；甲用癸印，透戊作合，而印非其印；甲用己财，己与别位之甲作合，而财非其财。如年己月...
    """
    
    original_text: str = """- **原文（source_text）**：

  其性情何也？盖既有配合，必有向背。如甲用辛官，透丙作合，而官非其官；甲用癸印，透戊作合，而印非其印；甲用己财，己与别位之甲作合，而财非其财。如年己月甲，年上之财，被月合去，而日主之甲乙无分；年甲月己，月上之财，被年合去，而日主之甲乙不与是也。甲用丙食与辛作合，而非其食，此四喜神因合而无用者也。盖有所合，则有所忌，逢吉不为吉，逢凶不为凶。即以六亲言之，如男以财为妻，而被别干合去，财妻岂能亲其夫乎？女以官为夫，而被他干合去，官夫岂能爱其妻乎？此谓配合之性情，因向背而殊也。

- 原注（原文注解）：
  　　此段由“十干合化”的数理结构，转入“性情与向背”的层面，指出：
  - 合化并非一律为吉；
  - 喜神若被别干合去，反而无用；
  - 忌神若被合化，反有转吉之机；
  - 关键在“向谁而合”“为谁而合”。

- 分字分词释义：
  - 性情：此处指十干配合时的“情向”与“态度”，即站在哪一边。
  - 向背：向着谁、背着谁，站在日主一边还是站在他干一边。
  - 甲用辛官：以辛金为正官，用来克制日主甲木之刚。
  - 透丙作合，而官非其官：丙辛相合，辛金之官性被丙牵走，不再专属甲日主。
  - 甲用癸印，透戊作合，而印非其印：癸印被戊土合去，甲失印助。
  - 甲用己财，己与别位之甲作合，而财非其财：财星己土被别处之甲合走，日主甲失其财。
  - 年己月甲 / 年甲月己：说明财星在年干或月干位置时，被对方合去的情形。
  - 四喜神因合而无用：官、印、财、食等喜神，因被别干合去而失去“为我服务”的用处。
  - 逢吉不为吉，逢凶不为凶：表面是吉神，合去则不吉；表面是凶神，合化则不凶。

- **规范化释义（primary_lang_explained）**：
  前文讲十干如何合化成五行，这里进一步追问一个问题：这些合化，在“性情”上到底向着谁？同样是一组合，可能替甲木办事，也可能替别的干办事；向谁“站队”，结果大不相同。比如甲日用辛为正官，如果丙火透出与辛相合，辛就被丙牵去化水，成了丙的官，不再是甲的官了；甲日用癸为印，如果戊土透出把癸合去，癸印就变成戊的合化之神，甲日反而失去印生；甲日用己为财，如果己土又与别位的甲相合，财就偏向那一位甲，而不是日主这位甲。年干为己、月干为甲时，是年上的财被月合去，日主甲乙无分；年干为甲、月干为己时，则是月上之财被年合去，日主也不沾光。甚至连甲用丙为食神时，若丙去与辛相合，丙也不再是甲的食神了。这四类本来是喜用之神，却因为“合去”而变得对日主无用。

 - 同样的道理，也可以用六亲来比喻：男命以财为妻，如果财被别干合去，这个“妻星”就好比被别人挟去，难以亲近日主；女命以官为夫，如果官被他干合去，这个“夫星”也难以真正在她身上发挥作用。这就是所谓“配合之性情”：看合化时，不单看“有没有合”，更要看合向何方、背离何方。

- **完整对等诠释（secondary_lang_full）**：  
  This subsection shifts from structure to temperament and allegiance. Whenever stems combine, we must ask on whose behalf the resulting qi actually acts. The very same conjunction may either serve the Day Master or be pulled over to work for some other stem. In the examples, Jia Day uses Xin as Direct Officer, but once Bing Fire appears and combines with Xin, the authority of Xin is drawn toward Bing and no longer functions as Jia's own Officer. If Jia uses Gui as Resource and Wu Earth comes out to combine with Gui, the nourishing power of Gui is diverted into supporting Wu instead, leaving Jia without that protection. If Jia uses Ji Earth as Wealth and another Jia in a different pillar combines with Ji, that Wealth now inclines toward the other Jia rather than toward the Day Master. Year‑stem and month‑stem arrangements can likewise leave Wealth present in form but already "spoken for" by someone else. Even Food God can be lost in this way if the Fire that represents it goes off to combine with Metal. In all such cases the chart seems to contain helpful stars, yet from the Day Master's standpoint they have been led away and no longer act on his behalf.

  The text illustrates this with family metaphors. In a male chart, Wealth stands for the wife: if the Wealth star is combined away by another stem, it is as if the wife has been taken into someone else's household and cannot truly be close to the husband. In a female chart, Officer stands for the husband: if that Officer is combined away by another stem, it can no longer fully devote itself to her. This is what is meant by the "disposition" of combinations: when reading conjunctions we must not only ask whether there is a combination, but also see clearly whom it favours and whom it abandons.

- 详细解说：
  - 合化的关键不在“是否发生”，而在“站在谁那一边”，这是“性情与向背”的核心。
  - 喜神被合去，比没有喜神更糟，因为肉眼看去似有其神，实际上却不为日主所用，容易误判。
  - 忌神若被合化走，反成为“有祸不及身”，是“逢凶不为凶”的重要机制之一，与后文“因成得败、因败得成”相呼应。

- 核心要点：
  - 分析合化时，必须从日主立场出发，问：此神究竟是“为我而合”，还是“被合而去”？
  - 对喜神：看它是否被合走、合偏，导致“名存实亡”。
  - 对忌神：看是否通过合化被牵制、被转用，从而减弱其凶性。

- 应用推演：
  1) 先辨用神与忌神，明确哪些神“本应为我所用”，哪些“本来为凶”。
  2) 再看合化方向：是否发生在用神与日主之间，还是用神被别干合走。
  3) 在六亲层面，对照财星（妻）、官星（夫）等，看“是否被别人合去”。
  4) 综合判断“逢吉不为吉、逢凶不为凶”的具体场景。

- 反例与边界：
  - 见财星就说“有妻”，不看财是否被他干合去，容易误判婚姻状况。
  - 见官星就说“有夫贵”，不察官星是否被合走，忽略“官夫岂能爱其妻乎”的警示。

- 小例（示意）：
  - 甲日主，用辛官；若命局中再见丙辛合水，辛已为丙所用，甲失其官，虽有官星而官不为己。

- 校勘与字词辨析：
  - “甲用丙食与辛作合，而非其食”：今依文脉解为“丙去合辛化水，则不再是甲之食神”，与前文“官非其官、印非其印、财非其财”同一结构。

---




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_205]` `[trigger: 气候调候]` `[factor_trigger: yongshen_pei_qihou AND hannuan_zaoshi_xude_yi]` `[role: 主干]` 用神配气候，寒暖燥湿须得宜。 → 《子平真诠·论用神配气候得失》#调候
  - `[ns_zpzy_206]` `[trigger: 寒暖燥湿]` `[factor_trigger: qihou_type IN (han, nuan, zao, shi) AND sishi_tiaohou_zhi_yao]` `[role: 主干]` 寒暖燥湿，四时调候之要。 → 《子平真诠·论用神配气候得失》#四时
  - `[ns_zpzy_207]` `[trigger: 寒暖要求]` `[factor_trigger: (dongsheng AND yi_huo_nuan) OR (xiasheng AND yi_shui_run)]` `[role: 主干]` 冬生宜火暖，夏生宜水润。 → 《子平真诠·论用神配气候得失》#寒暖
  - `[ns_zpzy_208]` `[trigger: 调候优先]` `[factor_trigger: geju_sui_hao AND qihou_bu_tiao AND result=nan_fa]` `[role: 主干]` 格局虽好，气候不调则难发。 → 《子平真诠·论用神配气候得失》#优先
  - `[ns_zpzy_209]` `[trigger: 冲克之害]` `[factor_trigger: chongke_taiguo=true AND result=poge_baiju]` `[role: 主干]` 冲克太过，破格败局。 → 《子平真诠》#上卷
  - `[ns_zpzy_210]` `[trigger: 用神为纲]` `[factor_trigger: bazi_yongshen AND zhuanqiu_yueling]` `[role: 主干]` 八字用神，专求月令。 → 《子平真诠》#论用神
  - `[ns_zpzy_211]` `[trigger: 月令司权]` `[factor_trigger: yueling_siquan AND tigang_zhi_fu]` `[role: 主干]` 月令司权，提纲之府。 → 《子平真诠》#论用神
  - `[ns_zpzy_212]` `[trigger: 用神取法]` `[factor_trigger: yongshen_qufa AND yi_yueling_wei_zhu]` `[role: 主干]` 用神取法，以月令为主。 → 《子平真诠》#论用神
  - `[ns_zpzy_213]` `[trigger: 食神制煞]` `[factor_trigger: shishen_zhisha AND geju=wugui]` `[role: 主干]` 食神制煞，武贵之格。 → 《子平真诠》#上卷
  - `[ns_zpzy_214]` `[trigger: 伤官见官]` `[factor_trigger: shangguan_jianguan AND result=huohuan_baiduan]` `[role: 主干]` 伤官见官，祸患百端。 → 《子平真诠》#上卷
  - `[ns_zpzy_215]` `[trigger: 喜神来助]` `[factor_trigger: xishen_laizhu=true AND result=shishi_shunsui]` `[role: 主干]` 喜神来助，事事顺遂。 → 《子平真诠》#上卷
  - `[ns_zpzy_216]` `[trigger: 天干主动]` `[factor_trigger: tiangan_zhudong AND ying_su_er_xian]` `[role: 主干]` 天干主动，应速而显。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "其性情何也？盖既有配合，必有向背"
    factor_refs: list = ['xiangbei', 'xishen_hequ', 'jishen_hehua', 'mingcun_shiwang', 'guancai_hequ', 'engine_id', 'xishen_hequ_flag', 'bazi_rule_engine', 'hehua_direction', 'bazi_rule_engine', 'spouse_hequ', 'bazi_rule_engine', 'hehua_net_effect', 'bazi_rule_engine', 'hehua_impact_level', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_049', 'xiangbei', 'rel_zpzq_050', 'xishen_hequ', 'evi_zpzq_049', 'xiangbei', 'rule_hehua_allegiance', 'evi_zpzq_050', 'xishen_hequ', 'rule_xishen_hequ', 'concept_allegiance', 'concept_nominal_loss']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_其性情何也_盖既有配合_必有向背_001_L1",
    )
    version: str = "1.0.0"
