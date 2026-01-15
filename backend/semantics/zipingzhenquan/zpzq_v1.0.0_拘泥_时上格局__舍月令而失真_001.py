"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492197
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
    semantic_id="zpzq_v1.0.0_拘泥_时上格局__舍月令而失真_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 拘泥时上格局舍月令而失真(SemanticEntry):
    """
    - **原文（source_text）**：
  二十九、论时说拘泥格局。
  八字用神专凭月令，月无用神，乃寻格局。月令，本也；外格，末也。今人不知轻重，拘泥格局，执假失真。

  故戊生甲寅之月，...
    """
    
    original_text: str = """- **原文（source_text）**：
  二十九、论时说拘泥格局。
  八字用神专凭月令，月无用神，乃寻格局。月令，本也；外格，末也。今人不知轻重，拘泥格局，执假失真。

  故戊生甲寅之月，时上庚甲，不以为明煞有制，而以为专食之格，逢甲减福。

  丙生子月，时逢巳禄，不以为正官之格，归禄帮身，而以为日禄归时，逢官破局。

  辛日透丙，时遇戊子，不以为辛日得官逢印，而以为朝阳之格，因丙无成。

  财逢时煞，不以为生煞攻身，而以为时上偏官。

  癸生巳月，时遇甲寅，不以为暗官受破，而以为刑合成格。

  癸生冬月，酉日亥时，透戊坐戌，不以为月劫建禄，用官通根，而以为拱戌之格，填实不利。辛日坐丑，寅年，亥月，卯时，不以为正财之格，而以为填实拱贵。

  乙逢寅月，时遇丙子，不以为木火通明，而以为格成鼠贵。

  如此谬论，百无一是，此皆由不知命理，妄为评断。

- 原注（原文注解）：
  　　本章严厉批评一种常见偏差：**不以月令用神为本，而一味拘泥“时上某格”的说法，用时柱格名替代真正的格局分析。**
  - 开头重申原则：
    - “八字用神专凭月令”：用神、格局首先看月令提纲；
    - “月无用神，乃寻格局”：只有在月令确实无用时，才考虑外格；
    - “月令，本也；外格，末也”：月令是根本，外格只是末节；
    - 今人颠倒主次，“拘泥格局”，结果是“执假失真”。

  后文列举数例，皆是舍本逐末的典型：
  1) **戊生甲寅月，时上庚甲**：
     - 本可论“明煞有制”：甲寅为七煞，庚为制煞之神；
     - 却不看月令与全局，只认定“时上专食之格”，还说“逢甲减福”，完全倒因为果。
  2) **丙生子月，时逢巳禄**：
     - 本是“正官之格，归禄帮身”：子中癸官，巳为丙之禄地；
     - 却不论官格与帮身，只拿“日禄归时”当论点，又硬加“逢官破局”。
  3) **辛日透丙，时遇戊子**：
     - 本应是“辛日得官逢印”：丙为官、戊为印；
     - 却只看“朝阳格”名目，以“因丙无成”为由否定官印格局。
  4) **财逢时煞**：
     - 正理是“生煞攻身”，需看煞用与制煞；
     - 却只用“时上偏官”四字概括，完全不问格局与用神。
  5) **癸生巳月，时遇甲寅**：
     - 实为“暗官受破”：巳中丙戊庚、甲寅又来刑破；
     - 却说“刑合成格”，以“刑合”之名掩盖官破之实.
  6) **癸生冬月，酉日亥时，透戊坐戌** 等例：
     - 原可论“月劫建禄，用官通根”或“正财之格”；
     - 反而硬说“拱戌格填实不利”“填实拱贵”，完全忽略月令与用神体系.
  7) **乙逢寅月，时遇丙子**：
     - 本是“木火通明”的经典格局之一；
     - 却偏要称作“格成鼠贵”，只因时上见子，挂一“鼠”名号.

  结语直言：“如此谬论，百无一是”，根源在“不知命理，妄为评断”。

- 分字分词释义：
  - 时说：专以时柱为据的各种格名与口诀.
  - 拘泥格局：死抓某种格局之名，而不顾全局用神与月令.
  - 专食之格：只见时上食神，便以为成“专食格”。
  - 日禄归时：以日主之禄落于时支为吉象的说法.
  - 朝阳之格：以时上火明照为“朝阳”的外格名目.
  - 时上偏官：以时支偏官为主格，不顾全局.
  - 刑合成格：以刑合关系硬说成格局之成.
  - 拱戌之格、填实拱贵：以多个支拱合某支为“贵格”的说法.
  - 木火通明：木火相生、官印相辉的佳象.
  - 鼠贵：以子（水鼠）相关格局为贵格的俗称.

- **规范化释义（primary_lang_explained）**：
  本章可以看作对“只看时柱格名”的总批判.

  子平原法的顺序是：
  1) 先看月令：定用神、定格局大方向；
  2) 再看四柱干支如何围绕月令展开；
  3) 若月令实在无用，再考虑外格与特例.

  而作者批评的，是一种倒置：
  - 不先看月令与全局，只盯着时柱某个组合；
  - 一见“时上食神”“日禄归时”“朝阳”“时上偏官”“刑合”“拱贵”“鼠贵”等字眼，便草率判定格局；
  - 甚至不顾明显的官煞制化、生克得失，只认格名不认结构.

  这些做法有几个共同问题：
  - **舍本逐末**：把以月令为本的体系丢掉，以时柱格名取代；
 - **完整对等诠释（secondary_lang_full）**：  
  Obsession with time-pillar pattern names reflects a complete reversal of priorities: instead of beginning from the Month and the overall structure, one stares at a single combination on the Hour pillar and rushes to declare “Pure Food God格”, “Day-Lu归时格”, “朝阳格”, “Hour Seven Killing格” and so on. In doing so, one ignores whether the Month has already established a usable structure, how Officer and Killing are actually controlled, and whether the supposed pattern even fits the real flow of生克.

  The proper order is clear: first settle the Month令 and the useful-god system for the whole chart, then, only when the Month truly holds no usable spirit, consider special names based on the Hour. Pattern labels can at best describe certain surface configurations; they can never replace analysis of real五行 relations. Treating these names as shortcuts instead of annotations is precisely to abandon the root and chase the tips.

  - **详细解说**：
    - **以名代实**：只认“某某格”这几个字，不问实际五行生克、用神喜忌；
    - **不顾反证**：明明可以从正统用神系统解释，却硬搬格名.

- **校勘与字词辨析（双语）**：
  - **中文**：本稿据通行本，经文用字保持原貌，标点现代化处理.
  - **English**: Based on standard edition. Original text preserved, punctuation modernized.

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_470]` `[trigger: 阳刃论]` `[factor_trigger: yangren_wei_jie AND xu_guansha_zhi_zhi_fang_gui]` `[role: 主干]` 阳刃为劫，须官煞制之方贵。 → 《子平真诠》#下卷第43章
  - `[ns_zpzy_471]` `[trigger: 支会之力]` `[factor_trigger: xishen_hui_zhi AND liliang_shenhou]` `[role: 主干]` 喜神会支，力量深厚。 → 《子平真诠》#下卷
  - `[ns_zpzy_472]` `[trigger: 建禄之格]` `[factor_trigger: jianlu_wuge AND xu_bie_xun_yongshen]` `[role: 主干]` 建禄无格，须别寻用神。 → 《子平真诠》#下卷
  - `[ns_zpzy_473]` `[trigger: 食神泄秀]` `[factor_trigger: shishen_xiexiu AND caihua_hengyi]` `[role: 主干]` 食神泄秀，才华横溢。 → 《子平真诠》#下卷
  - `[ns_zpzy_474]` `[trigger: 七煞有制]` `[factor_trigger: sha_feng_shi_zhi AND quanwei_xianhe]` `[role: 主干]` 煞逢食制，权威显赫。 → 《子平真诠》#下卷
  - `[ns_zpzy_475]` `[trigger: 刃运逢煞]` `[factor_trigger: renyun_feng_sha AND zhangbing_quanzhong]` `[role: 主干]` 刃运逢煞，掌兵权重。 → 《子平真诠》#下卷
  - `[ns_zpzy_476]` `[trigger: 禄运逢官]` `[factor_trigger: luyun_feng_guan AND shitu_hengtong]` `[role: 主干]` 禄运逢官，仕途亨通。 → 《子平真诠》#下卷
  - `[ns_zpzy_477]` `[trigger: 从财行运]` `[factor_trigger: congcai_ge AND xi_caiwang_zhiyun]` `[role: 主干]` 从财格喜财旺之运。 → 《子平真诠》#下卷
  - `[ns_zpzy_478]` `[trigger: 从官行运]` `[factor_trigger: congguan_ge AND xi_guanwang_zhiyun]` `[role: 主干]` 从官格喜官旺之运。 → 《子平真诠》#下卷
  - `[ns_zpzy_479]` `[trigger: 寒暖燥湿]` `[factor_trigger: hannuan_zaoshi AND tiaohou_weixian]` `[role: 主干]` 寒暖燥湿，调候为先。 → 《子平真诠》#下卷
  - `[ns_zpzy_480]` `[trigger: 喜神来助]` `[factor_trigger: xishen_laizhu=true AND result=shishi_shunsui]` `[role: 主干]` 喜神来助，事事顺遂。 → 《子平真诠》#下卷
  - `[ns_zpzy_481]` `[trigger: 天干主动]` `[factor_trigger: tiangan_zhu_dong AND ying_su_er_xian]` `[role: 主干]` 天干主动，应速而显。 → 《子平真诠》#下卷"""
    normalized_text_zh: str = """"""
    subject: str = "拘泥“时上格局”，舍月令而失真"
    factor_refs: list = ['juni_geju', 'huokan', 'shishuo', 'yueling_weiben', 'engine_id', 'yuezhi_zhuzhou', 'bazi_rule_engine', 'yueling_yongshen', 'bazi_rule_engine', 'waige_yongfa', 'bazi_rule_engine', 'shishuo_quanzhong', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_138', 'yueling_yongshen', 'rel_zpzq_139', 'shishuo_quanzhong', 'evi_zpzq_124', 'yueling_yongshen', 'rule_yueling_youxian', 'evi_zpzq_125', 'waige_yongfa', 'rule_waige_cixu', 'concept_root', 'concept_flexibility']
    
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
        l1_anchor="zpzq_v1.0.0_拘泥_时上格局__舍月令而失真_001_L1",
    )
    version: str = "1.0.0"
