"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.465674
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
    semantic_id="zpzq_v1.0.0_宫分与用神_六亲配位的两条路径_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 宫分与用神六亲配位的两条路径(SemanticEntry):
    """
    - **原文（source_text）**：
  二十三、论宫分用神配六亲。
  人有六亲，配之八字，亦存于命.

  其由宫分配之者，则年月日时，自上而下，祖父妻子，亦自上而下。以地相配，适得其宜，...
    """
    
    original_text: str = """- **原文（source_text）**：
  二十三、论宫分用神配六亲。
  人有六亲，配之八字，亦存于命.

  其由宫分配之者，则年月日时，自上而下，祖父妻子，亦自上而下。以地相配，适得其宜，不易之位也.

  其由用神配之者，则正印也母，身所自出，取其生我也。若偏财受我克制，何反为父？偏财者，母之正夫也，正印为母，则偏财为父矣。正财为妻，受我克制，夫为妻纲，妻则从夫。若官煞则克制乎我，何以反为子女也？官煞者，财所生也，财为妻妾，则官煞为子女矣。至于比肩为兄弟，又理之显然者.

  其间有无得力，或吉或凶，则以四柱所存或年月或日时财官伤刃，系是何物，然后以六亲配之用神。局中作何喜忌，参而配之，可以了然矣.

- 原注（原文注解）：
  　　本章简要交代了六亲在八字中的两种配法：
  - 一是“宫分配”：
    - 以年月日时四柱自上而下，配“祖、父、妻、子”等；
    - 这是从“地分与宫位”的角度，按位置来理解六亲；
  - 二是“用神配”：
    - 以正印为母，取其“生我”之义；
    - 以偏财为父，取其“母之正夫”之象：正印为母，则偏财为父；
    - 以正财为妻：财受我克，为妻受夫纲制之象，所以正财为妻；
    - 以官煞为子女：官煞克我，而又为财所生，财为妻则官煞为子女；
    - 以比肩为兄弟：同类并立之象最为明显.
  - 最后一段提醒：
    - 六亲只是配位的一个“标签体系”；
    - 真正决定六亲吉凶的，是这些用神在命局中“有无得力”：
      - 比如母星印若根气充足又得护，则母多有力；
      - 父星偏财若被重重克制或合去，则父多有损；
    - 因此，看完六亲配位之后，还必须回到整个命局中，从财官伤刃等喜忌来判断六亲的强弱与吉凶.

- 分字分词释义：
  - 六亲：父母、妻（夫）、子女、兄弟等，与命主直接相关的亲属系统.
  - 宫分：以四柱所在之宫位（年、月、日、时）来对应祖父、父母、配偶、子女等.
  - 以地相配：按地支所在宫位来配六亲位置.
  - 正印为母：印星生身，如母生子.
  - 偏财为父：偏财为正印之夫，印为母，则偏财为父.
  - 正财为妻：财星受我克制，象征妻从夫纲.
  - 官煞为子女：官煞为财星所生，财为妻妾，则官煞为子女.
  - 比肩为兄弟：同类相并，最符合兄弟之象.
  - 得力：有根、有生、有护，能发挥其作用.
  - 财官伤刃：泛指命局中与六亲相关的财星、官星、伤官、刃等十神.

- **规范化释义（primary_lang_explained）**：
  作者指出：六亲配八字，主要有两条路线：一条是从“宫分”来配，一条是从“用神”来配.

  宫分之配，大致是：
  - 年柱偏向上辈（祖父母、家族根源）；
  - 月柱偏向父母与成长环境；
  - 日柱偏向自身与配偶（尤其日支为妻宫）；
  - 时柱偏向子女与晚年.
  这种配法更多是从“位置”角度理解六亲，与地支宫位配合使用，适合看六亲在命局中所处的大致“位势”.

  用神之配，则更偏向“象义与十神”：
  - 印生身，最像母亲，所以以正印为母；
  - 偏财是印之夫，印为母，则偏财自然为父；
  - 正财受我克，为妻受夫纲制之象，所以正财为妻；
  - 官煞克我，而又为财所生，财为妻则官煞为子女；
  - 比肩与日主同性同类，最像兄弟.

  但作者并不在此展开各种细枝末节，而是提醒：
  - 六亲只是配位的一个“标签体系”；
  - 真正决定六亲吉凶的，是这些用神在命局中“有无得力”：
    - 比如母星印若根气充足又得护，则母多有力；
    - 父星偏财若被重重克制或合去，则父多有损；
  - 因此，看完六亲配位之后，还必须回到整个命局中，从财官伤刃等喜忌来判断六亲的强弱与吉凶.

- 详细解说：
 - **完整对等诠释（secondary_lang_full）**：  
  The six close relations are traced in two ways: by palace positions—Year, Month, Day and Hour broadly corresponding to ancestors, parents, spouse and children—and by the useful gods that stand in for them, with Resource representing the mother, Indirect Wealth the father, Direct Wealth the spouse, Officer or Seven Killings the children, and Peers or Rob Wealth the siblings. What truly decides their fortune is whether these representative gods are strong, rooted and well supported within the overall pattern, not the mere presence of a star labelled "mother" or "child".

  - 六亲配位只是命理应用层的一个“投影”：
    - 宫分给出的是“六亲占据的位置”；
    - 用神给出的是“六亲代表的十神”；
    - 真正的吉凶，则和整体用神格局同一体系.
  - 本章与后文“论妻子”等章节相衔接：
    - 先总论六亲配位的原则；
    - 再具体展开妻宫、子息等细部.

- 核心要点：
  - 六亲判断三要素：
    1) 宫分位置（年、月、日、时）；
    2) 对应十神（印、财、官、比等）作为六亲用神；
    3) 这些用神在命局中的得力与否（根气、受克、会合等）。
  - 不可只看“某星为父母、某星为子女”而不论其得力与否；
  - 更不可只看星辰（天喜、红鸾等）而不顾六亲用神的实际强弱.

- 应用推演：
  1) 先按宫分大致定位六亲所在柱位（年、月、日、时）；
  2) 再按用神体系确定父母、妻子、子女、兄弟所对应的十神；
  3) 检查这些十神在命局中的得力程度：有无根、有无护、是否多受克；
  4) 结合前文用神喜忌理论，归纳各六亲的吉凶与有无；
  5) 在运势预测中，再看行运是否增强或损害这些六亲用神.

- 反例与边界：
  - 只用“宫分”看六亲而不看十神本身的强弱，导致结论偏粗；
  - 只看十神名称，不配合宫位与得力，忽略六亲出现的“场景”；
  - 把星辰系统（如天喜、天德）当作六亲判断主依据，而不回到用神.

- 小例（示意）：
  - 一命中印星得禄通根、又坐月柱，母亲多为成长环境中重要且有力之人；
  - 另一命偏财为父星，却逢重重劫比，且年柱偏财受冲，父亲形象多有起伏或缺位，这是“六亲用神无力”的典型.

- 校勘与字词辨析：
  - “偏财者，母之正夫也，正印为母，则偏财为父矣”一句，是本章“父星=偏财”配法之来源，本精校保持原句，仅在释义中展开.
  - “夫为妻纲，妻则从夫”“官煞者，财所生也，财为妻妾，则官煞为子女矣”等句，多本一致，本精校在白话中以现代语言说明其逻辑意涵.


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_392]` `[trigger: 四吉亦破]` `[factor_trigger: caiguan_yinshi IN sijishen AND yong_zhi_bu_dang AND yi_po_ge]` `[role: 主干]` 财官印食四吉神，用之不当亦破格。 → 《子平真诠·论四吉神能破格》#四吉
  - `[ns_zpzy_393]` `[trigger: 吉神破格例]` `[factor_trigger: (shishen_daisha_toucai_weihai) OR (chunmu_huowang_jianguan_yi_ji)]` `[role: 主干]` 食神带煞透财为害，春木火旺见官亦忌。 → 《子平真诠·论四吉神能破格》#破格例
  - `[ns_zpzy_394]` `[trigger: 配合得宜]` `[factor_trigger: jishen_xu_peihe_deyi AND guo_ze_fan_hai AND buzu_ze_wuli]` `[role: 主干]` 吉神须配合得宜，过则反害，不足则无力。 → 《子平真诠·论四吉神能破格》#配合
  - `[ns_zpzy_395]` `[trigger: 宫位配亲]` `[factor_trigger: nian_yue_ri_shi AND ge_pei_liuqin]` `[role: 主干]` 年月日时，各配六亲。 → 《子平真诠》#中卷
  - `[ns_zpzy_396]` `[trigger: 辰戌丑未]` `[factor_trigger: branch IN (chen, xu, chou, wei) AND simu_ku]` `[role: 主干]` 辰戌丑未为四墓库。 → 《子平真诠》#中卷
  - `[ns_zpzy_397]` `[trigger: 冲开库门]` `[factor_trigger: chong_kai_kumen AND caiguan_shi_xian]` `[role: 主干]` 冲开库门，财官始显。 → 《子平真诠》#中卷
  - `[ns_zpzy_398]` `[trigger: 库中藏干]` `[factor_trigger: kuzhong_canggan AND tougan_fang_yong]` `[role: 主干]` 库中藏干，透干方用。 → 《子平真诠》#中卷
  - `[ns_zpzy_399]` `[trigger: 印多克子]` `[factor_trigger: yin_duo_ke_shi AND zixi_jiannan]` `[role: 主干]` 印多克食，子息艰难。 → 《子平真诠》#中卷
  - `[ns_zpzy_400]` `[trigger: 食多克官]` `[factor_trigger: shi_duo_ke_guan AND shitu_bushun]` `[role: 主干]` 食多克官，仕途不顺。 → 《子平真诠》#中卷
  - `[ns_zpzy_401]` `[trigger: 比旺争财]` `[factor_trigger: bi_wang_zheng_cai AND shouzu_zhengdou]` `[role: 主干]` 比旺争财，手足争斗。 → 《子平真诠》#中卷
  - `[ns_zpzy_402]` `[trigger: 劫旺夺财]` `[factor_trigger: jie_wang_duo_cai AND qicai_buju]` `[role: 主干]` 劫旺夺财，妻财不聚。 → 《子平真诠》#中卷
  - `[ns_zpzy_403]` `[trigger: 先后有别]` `[factor_trigger: shengke_xianhou AND jiongxiong_jiongyi]` `[role: 主干]` 生克先后，吉凶迥异。 → 《子平真诠》#中卷
  - `[ns_zpzy_404]` `[trigger: 病重药重]` `[factor_trigger: (bingzhong AND yaozhong) OR (bingqing AND yaoliang)]` `[role: 主干]` 病重药重，病轻药轻。 → 《子平真诠》#中卷
  - `[ns_zpzy_405]` `[trigger: 干支一体]` `[factor_trigger: ganzhi_yiti AND tongcan_helun]` `[role: 主干]` 干支一体，统参合论。 → 《子平真诠》#中卷"""
    normalized_text_zh: str = """"""
    subject: str = "宫分与用神：六亲配位的两条路径"
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_宫分与用神_六亲配位的两条路径_001_L1",
    )
    version: str = "1.0.0"
