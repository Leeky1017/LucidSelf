"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492147
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
    semantic_id="zpzq_v1.0.0_运能_成格_亦能_变格__重于一般喜忌_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 运能成格亦能变格重于一般喜忌(SemanticEntry):
    """
    - **原文（source_text）**：
  二十六、论行运成格变格。
  命之格局，成于八字，然配之以运，亦有成格变格之要权。其成格变格，较之喜忌祸福尤重。

  何为成格？本命用神，成而未全，...
    """
    
    original_text: str = """- **原文（source_text）**：
  二十六、论行运成格变格。
  命之格局，成于八字，然配之以运，亦有成格变格之要权。其成格变格，较之喜忌祸福尤重。

  何为成格？本命用神，成而未全，从而就之者是也。如丁生辰月，透壬为官，而运逢申子以会之；乙生辰月，或申或子会印成局，而运逢壬癸以透之。如此之类，皆成格也。

  何为变格？如丁生辰月，透壬为官，而运逢戌，透出辰中伤官；壬生戌月，丁己并透，而支又会寅会午，作财旺生官矣，而运逢戊土，透出戌中七煞；壬生亥月，透己为用，作建禄用官矣，而运逢卯未，会亥成本，又化建禄为伤。如此之类，皆变格也。

  然亦有逢成格而不喜者，何也？如壬生午月，运透己官，而本命有甲乙之类是也。

  又有逢变格而不忌者，何也？如丁生辰月，透壬用官，逢戊而命有甲；壬生亥月，透己用官，运逢卯未，而命有庚辛之类是也。

  成格变格，关系甚大，取运者其细详之。

- 原注（原文注解）：
  　　本章在“行运总论”之上，更进一步说明：
  - 行运不仅能令喜忌之力增减，更能在关键时刻直接 **成就某格或摧毁原格**；
  - 因此，“成格/变格”之权，有时比一般“喜忌祸福”更为重大。

  首句指出：格局之成，本在八字；
  - 但配合大运流年之后，运来之字可能：
    - 把原本“尚未完全成局”的用神格局补全，形成“成格”；
    - 也可能把原本清纯之格搅杂或反转，形成“变格”。

  “何为成格”一段，给出典型例子：
  - 丁生辰月，透壬为官，而命中尚欠水局；
    - 若运逢申子，会成水局，以申子会辰，官格得根，格局圆满，即为“运来成格”；
  - 乙生辰月，或申或子已会印成局，而运逢壬癸透出，印星明透，则印格告成；
  - 共通之处在于：**原局用神已有其势，惟欠一二处以全形，行运恰好补上缺口**。

  “何为变格”一段，则说明运来之字如何使原格变质：
  - 丁生辰月，透壬为官，本可用官；
    - 运逢戌，透出辰中伤官，使“官中藏伤”被提出，变成官伤并见；
  - 壬生戌月，丁己并透，支又会寅午，本作“财旺生官”，
    - 运逢戊土，透出戌中七煞，原本财生官局中夹入七煞，格局由清转险；
  - 壬生亥月，透己为用，作建禄用官，
    - 运逢卯未，会亥成木局，亥水化为木，原本建禄用官之格转成伤官格.
  - 这些都是：
    - 运来之字，把“原本藏于地支的另一重结构”引发出来；
    - 或会合、或透出，使原格之性与用神体系发生改变，即为“变格”。

  但作者随即指出两种例外：
  - 逢成格而不喜：
    - 如壬生午月，运透己官，本似成官格之善；
    - 然命中若已有甲乙等木字，则官被合去、制去，成格反不为美；
  - 逢变格而不忌：
    - 如丁生辰月，透壬用官，运逢戊而命有甲，
      - 甲木可制戊土七煞，化险为夷；
    - 壬生亥月，透己用官，运逢卯未，而命有庚辛，
      - 庚辛制木，使“成伤”之势不能尽成，变格之害被削弱.
  - 结语强调：成格与变格的判断，关乎一生走势之大局，取运者必须细加推究，不可草率。

- 分字分词释义：
  - 成格：原局格局已具雏形，而运来之字补足其所缺，使格局完备。
  - 变格：原局已有格局，而运来之字触发另一重结构或引出藏干，使原有格局性质改变。
  - 成而未全：已有用神与大势，但在根气、透出或会局上尚欠一环。
  - 从而就之：行运补上这一环，使之“就位”。
  - 透壬为官、透己为用：指壬水或己土明透天干而为用神.
  - 会印成局：地支会成印绶之局，如申子辰会水印等。
  - 透出辰中伤官、戌中七煞：从四库藏干中透出伤官或七煞之意.
  - 建禄用官：日主建禄得位，以官星为用的格局.

- **规范化释义（primary_lang_explained）**：
  若把命局比作一个“基础程序”，行运就像不断加载的“补丁”：
  - 有的补丁把原程序关键模块补全，使其功能完整，这是“成格”；
  - 有的补丁却替换了核心模块，使程序逻辑改变，这是“变格”。

  本章说明的，就是这两种极端情形：
  1) 原格已具，却欠“会局、透干、植根”等条件；
     - 大运或流年来补齐这一块，于是本来只是“可用之势”，升级为“名副其实之格局”；
  2) 原格清纯，而藏干或会局中另有一重结构潜伏；
     - 运来一字，触发此结构，使原格混煞或变成他格。

  重要的是：
  - 成格不一定都值得欢喜，要看新成之格是否真为命局所能承受、是否与原局用神体系相容；
  - 变格也不一定必定惧怕，要看命局中是否另有制衡之力（如甲制戊、庚辛制木），能把“变”的危机转换为“变中有救”。

- **完整对等诠释（secondary_lang_full）**：  
  Luck periods can "establish a pattern" when they supply the missing stems, roots or assemblies that turn a half-formed configuration into a complete structure, and they can "alter a pattern" when they activate hidden combinations or buried stars that overturn the original framework. In both cases, what changes is not only the strength of certain gods, but the very layout of the game board: which spirits count as useful, which become problematic, and what name the chart should be called by.

  Because of this, one cannot simply rejoice whenever a period appears to complete a pattern, nor panic whenever a period seems to transform it. If the newly formed pattern exceeds what the native chart can actually carry, or conflicts with its underlying useful-god system, a "forming" luck can become a burden rather than a blessing. Conversely, when strong balancing forces already exist in the natal chart, a "transforming" luck may expose dangers early and open up a new, more appropriate track instead of pure ruin. In the author's view, such years of forming or transforming patterns weigh more heavily than ordinary auspicious or inauspicious luck, because they rewrite the rules of play for the whole structure rather than merely adjusting numerical strength.

- **详细解说**：
  - 与上一章“行运一般喜忌”相比，本章把重心放在“结构层级的变化”：
    - 一般喜忌，是在原格不变前提下谈“运助用神或助忌神”；
    - 成格变格，则是运来之后，连“原用神体系与格局名称”都可能改变.
  - 对命运路径而言：
    - 成格的年份，往往是“终于成其所为”的关节点，如科举高中、事业定型；
    - 变格的年份，则常是“身份、轨道、价值定位”被迫转向之时.
  - 作者强调“较之喜忌祸福尤重”，是提醒读者：
    - 不要只停留在“这步运吉/凶”的层级；
    - 更要看这步运是否在“重写整个局的玩法”。

- **校勘与字词辨析（双语）**：
  - **中文**：本稿据通行本，经文用字保持原貌，标点现代化处理。
  - **English**: Based on standard edition. Original text preserved, punctuation modernized.

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_434]` `[trigger: 禄劫取运]` `[factor_trigger: lujie_ge_quyun AND shi_yongshen_er_ding]` `[role: 主干]` 禄劫格取运，视用神而定。 → 《子平真诠》#下卷第46章
  - `[ns_zpzy_435]` `[trigger: 成格之运]` `[factor_trigger: yun_neng_cheng_ge AND geju_yugao]` `[role: 主干]` 运能成格，格局愈高。 → 《子平真诠》#下卷
  - `[ns_zpzy_436]` `[trigger: 伤官之用]` `[factor_trigger: shangguan_shengcai AND fugui_zilai]` `[role: 主干]` 伤官生财，富贵自来。 → 《子平真诠》#下卷
  - `[ns_zpzy_437]` `[trigger: 运能变格]` `[factor_trigger: yun_neng_bian_ge AND jiongxiong_zhuanhuan]` `[role: 主干]` 运能变格，吉凶转换。 → 《子平真诠》#下卷
  - `[ns_zpzy_438]` `[trigger: 干透之验]` `[factor_trigger: xishen_tougan AND yingyan_sujie]` `[role: 主干]` 喜神透干，应验速捷。 → 《子平真诠》#下卷
  - `[ns_zpzy_439]` `[trigger: 官运逢印]` `[factor_trigger: guanyun_feng_yin AND shitu_shunsui]` `[role: 主干]` 官运逢印，仕途顺遂。 → 《子平真诠》#下卷
  - `[ns_zpzy_440]` `[trigger: 财运逢食]` `[factor_trigger: caiyun_feng_shi AND caiyuan_guangjin]` `[role: 主干]` 财运逢食，财源广进。 → 《子平真诠》#下卷
  - `[ns_zpzy_441]` `[trigger: 印格行运]` `[factor_trigger: yin_ge AND xi_guansha_shengyin_yun]` `[role: 主干]` 印格喜官煞生印运。 → 《子平真诠》#下卷
  - `[ns_zpzy_442]` `[trigger: 食格行运]` `[factor_trigger: shi_ge AND xi_caixing_xiexiu_yun]` `[role: 主干]` 食格喜财星泄秀运。 → 《子平真诠》#下卷
  - `[ns_zpzy_443]` `[trigger: 干支配合]` `[factor_trigger: ganzhi_peihe AND shengke_youqing]` `[role: 主干]` 干支配合，生克有情。 → 《子平真诠》#下卷
  - `[ns_zpzy_444]` `[trigger: 用神有力]` `[factor_trigger: yongshen_youli=true AND result=fugui_keqi]` `[role: 主干]` 用神有力，富贵可期。 → 《子平真诠》#下卷
  - `[ns_zpzy_445]` `[trigger: 月令当权]` `[factor_trigger: yueling_dangquan AND yongshen_zhi_fu]` `[role: 条件分支]` 月令当权，用神之府。 → 《子平真诠》#下卷"""
    normalized_text_zh: str = """"""
    subject: str = "运能“成格”亦能“变格”：重于一般喜忌"
    factor_refs: list = ['chengge_yun', 'biange_yun', 'poge_yun', 'chengbiange_quan', 'engine_id', 'jichu_geju', 'bazi_rule_engine', 'yun_zhu_yongshen', 'bazi_rule_engine', 'yun_chufa_yincang', 'bazi_rule_engine', 'chengge_qianli', 'bazi_rule_engine', 'biange_fengxian', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_132', 'jichu_geju', 'rel_zpzq_133', 'yun_chufa_yincang', 'evi_zpzq_119', 'chengbiange_quan', 'rule_chengbiange_quan', 'evi_zpzq_120', 'chengge_qianli', 'rule_chengbiange_zhongyao', 'concept_formation', 'concept_transformation']
    
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
        l1_anchor="zpzq_v1.0.0_运能_成格_亦能_变格__重于一般喜忌_001_L1",
    )
    version: str = "1.0.0"
