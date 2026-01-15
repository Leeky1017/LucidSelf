"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523415
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
    semantic_id="zpzq_v1.0.0_天地之间_一气而已_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 天地之间一气而已(SemanticEntry):
    """
    - **原文（source_text）：
  天地之间，一气而已。惟有动静，遂分阴阳。有老少，遂分四象。老者极动静之时，是为太阳太阴；少者初动初静之际，是为少阳少阴。有是四象，而五行具于其中矣。水者，...
    """
    
    original_text: str = """- **原文（source_text）：
  天地之间，一气而已。惟有动静，遂分阴阳。有老少，遂分四象。老者极动静之时，是为太阳太阴；少者初动初静之际，是为少阳少阴。有是四象，而五行具于其中矣。水者，太阴也；火者，太阳也；木者，少阳也；金者，少阴也；土者，阴阳老少、木火金水冲气所结也。

- 原注（原文注解）：
  　　此段总提“气—阴阳—四象—五行”的生成次第，为全书论干支与用神之总纲，原书无单列夹注。

- 分字分词释义：
  - 一气而已：只有一团元气，本无分别。
  - 动静：气机之动与静，是阴阳分化的最初根源。
  - 阴阳：动为阳，静为阴，是一气两端。
  - 四象：太阳、太阴、少阳、少阴，是阴阳再分为“老少”后的四种状态。
  - 老少：指气机运行到“极”与“初”的两个阶段：极动极静为“老”，初动初静为“少”。
  - 五行具于其中：五行不是外加的五个东西，而是四象展开后的五种功能形态。
  - 水者太阴：水属太阴之象，重在收敛、下行、藏纳。
  - 火者太阳：火属太阳之象，重在发散、上升、照耀。
  - 木者少阳：木为少阳，重在发生、条达、生长。
  - 金者少阴：金为少阴，重在敛聚、收成、肃杀。
  - 土者阴阳老少冲气所结：土为阴阳老少与四行冲激所结成的中和之质，承载与调剂诸行。

- **规范化释义（primary_lang_explained）**：
  天地之间，本来只有一团元气，没有细分。只是因为气机有动有静，才分出了阴阳；又在阴阳之中分出“老”与“少”的阶段，就成了太阳、太阴、少阳、少阴四象。有了这四象，五行之理也就全在其中了：水属太阴，主收敛与下行；火属太阳，主发散与上升；木属少阳，主发生与生长；金属少阴，主敛聚与收成；至于土，则是阴阳老少和木火金水相互冲激后凝结出来的中和之质，负责承载与调剂诸行。
- **完整对等诠释（secondary_lang_full）**：  
  Between Heaven and Earth there is originally only one undivided current of qi. Because this life-breath can either move or come to rest, it differentiates into yang and yin. When it reaches extreme movement or extreme stillness it forms Greater Yang and Greater Yin; when it first begins to move or first becomes still it forms Lesser Yang and Lesser Yin. Once these Four Images are in place, the Five Elements are already contained within them. Water corresponds to Greater Yin and emphasizes gathering in, descending and storing. Fire corresponds to Greater Yang and emphasizes radiating, rising and illuminating. Wood corresponds to Lesser Yang and emphasizes sprouting, expansion and growth. Metal corresponds to Lesser Yin and emphasizes contraction, harvesting and cutting back. Earth is the medium that crystallizes out of the interaction of yin and yang in their older and younger phases together with the four active elements; it bears and regulates the others. This passage therefore sets out a sequence from primordial qi through yin and yang to the Four Images and finally to the Five Elements, and treats the elements not as five separate substances but as five functional modes of the same original qi.

- 详细解说：
  - 一切格局推演都不能脱离这一层“气—阴阳—四象—五行”的次第，否则仅是在五行字面上打转。
  - 五行不是孤立的“元素”，而是气机不同阶段的功能化呈现，需联系四象来理解其性情。
  - 土为中和之行，是阴阳老少与四行交互之后的产物，是“承与调”的关键。

- 核心要点：
  - 以“一气”为源，阴阳四象为桥，五行为用。
  - 木火金水各有所宗，土居中为承载与调候。
  - 论命若只言五行，而不明其与阴阳四象的内在关系，易流于标签化。

- 应用推演：
  1) 观整体气机：先问局中“气性”偏寒偏热、偏升偏降，而不只数五行个数。
  2) 判阴阳与四象：结合日主、月令与全局，判断“何象当令”（如太阴偏重、水气聚、则以收敛为本）。
  3) 再看五行具体用法：在“象”的基础上，才谈生克制化与用神取舍。

- 反例与边界：
  - 只按“五行多少”断“喜金忌木”等，而不顾气机动静与四象节奏，常与实际人事不符。
  - 把土简单当成“厚重、迟缓”，不见其“承载与调剂”的中和角色。

- 小例（示意）：
  - 冬局水太阴气盛，而无火与土调候，纵有金多也只是助寒，应先从“气机太阴”入手，再谈金水之用与木火之补。

- 校勘与字词辨析（双语）：
  - **中文**：“土者，阴阳老少、木火金水冲气所结也”：各本大体相同，个别本把“冲气”作“冲激之气”，义同，今仍从今本。
  - **English**: The sentence "Earth is what is formed from the interacting qi of old and young yin-yang and of Wood, Fire, Metal and Water" is essentially stable across editions. A few texts gloss "chongqi" as "chongji zhi qi" (冲激之气, agitated qi), which is close in meaning; we follow the wording of the present base text.
 
- **叙事素材（narrative_snippets）**：
 - **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_054]` `[trigger: 五行基础]` `[factor_trigger: cosmology_yiqi AND dongjing_fen_yinyang AND laoshao_cheng_sixiang AND wuxing_ju_qizhong]` `[role: 主干]` 天地一气，动静分阴阳，老少成四象，五行具于其中。 → 《子平真诠·论十干十二支》#总纲
  - `[ns_zpzy_055]` `[trigger: 水行特性]` `[factor_trigger: element=shui AND sixiang=taiyin AND function=(shoulian, xiaxing, cangna)]` `[role: 主干依赖]` 水者太阴，收敛下行藏纳。 → 《子平真诠·论十干十二支》#水行
  - `[ns_zpzy_056]` `[trigger: 火行特性]` `[factor_trigger: element=huo AND sixiang=taiyang AND function=(fasan, shangsheng, zhaoyao)]` `[role: 主干依赖]` 火者太阳，发散上升照耀。 → 《子平真诠·论十干十二支》#火行
  - `[ns_zpzy_057]` `[trigger: 木行特性]` `[factor_trigger: element=mu AND sixiang=shaoyang AND function=(fasheng, tiaoda, shengzhang)]` `[role: 主干依赖]` 木者少阳，发生条达生长。 → 《子平真诠·论十干十二支》#木行
  - `[ns_zpzy_058]` `[trigger: 金行特性]` `[factor_trigger: element=jin AND sixiang=shaoyin AND function=(lianju, shoucheng, susha)]` `[role: 主干依赖]` 金者少阴，敛聚收成肃杀。 → 《子平真诠·论十干十二支》#金行
  - `[ns_zpzy_059]` `[trigger: 土行特性]` `[factor_trigger: element=tu AND sixiang=zhonghe AND function=(chengzai, tiaoji_zhuxing)]` `[role: 主干依赖]` 土者阴阳老少冲气所结，承载调剂诸行。 → 《子平真诠·论十干十二支》#土行
  - `[ns_zpzy_060]` `[trigger: 论命要领]` `[factor_trigger: lunming_step1=qiji_dongjing AND lunming_step2=sixiang_jiezou AND lunming_step3=wuxing_yongfa]` `[role: 主干依赖]` 论命先观气机动静，再判四象节奏，后谈五行用法。 → 《子平真诠·论十干十二支》#方法论
  - `[ns_zpzy_061]` `[trigger: 天干地支]` `[factor_trigger: tiangan_dizhi AND yinyang_xiang]` `[role: 主干依赖]` 天干地支，阴阳之象也。 → 《子平真诠》#论十干十二支
  - `[ns_zpzy_062]` `[trigger: 干支配合]` `[factor_trigger: ganzhi_peihe AND shengke_zhihua_li]` `[role: 主干依赖]` 干支配合，生克制化之理。 → 《子平真诠》#论十干十二支
  - `[ns_zpzy_063]` `[trigger: 甲乙属木]` `[factor_trigger: (jiayi=mu) AND (bingding=huo) AND (wuji=tu) AND (gengxin=jin) AND (rengui=shui)]` `[role: 条件分支]` 甲乙属木，丙丁属火，戊己属土，庚辛属金，壬癸属水。 → 《子平真诠》#论十干十二支
  - `[ns_zpzy_064]` `[trigger: 夏火司权]` `[factor_trigger: season=xia AND huo_siquan AND huo_wang_tu_xiang]` `[role: 条件分支]` 夏火司权，火旺土相。 → 《子平真诠》#上卷
  - `[ns_zpzy_065]` `[trigger: 秋金主事]` `[factor_trigger: season=qiu AND jin_zhushi AND jin_wang_shui_xiang]` `[role: 条件分支]` 秋金主事，金旺水相。 → 《子平真诠》#上卷
  - `[ns_zpzy_066]` `[trigger: 扶抑为常]` `[factor_trigger: fuyi_weichang AND pingheng_yinyang]` `[role: 总结]` 扶抑为常，平衡阴阳。 → 《子平真诠》#上卷
  - `[ns_zpzy_067]` `[trigger: 病药为贵]` `[factor_trigger: bingyao_weigui AND youbing_deyao]` `[role: 总结]` 病药为贵，有病得药。 → 《子平真诠》#上卷
  - `[ns_zpzy_068]` `[trigger: 真神得用]` `[factor_trigger: zhenshen_deyong AND geju_qingchun]` `[role: 总结]` 真神得用，格局清纯。 → 《子平真诠》#上卷
  - `[ns_zpzy_069]` `[trigger: 阴阳调和]` `[factor_trigger: yinyang_tiaohe AND zhonghe_weigui]` `[role: 总结]` 阴阳调和，中和为贵。 → 《子平真诠》#上卷
  - `[ns_zpzy_070]` `[trigger: 相神得用]` `[factor_trigger: xiangshen_deyong AND fuge_yougong]` `[role: 主干依赖]` 相神得用，辅格有功。 → 《子平真诠》#上卷
  - `[ns_zpzy_071]` `[trigger: 时柱归宿]` `[factor_trigger: pillar=shi AND role=guisu_zixi]` `[role: 条件分支]` 时柱归宿，子息之宫。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "天地之间，一气而已"
    factor_refs: list = ['yiqi', 'sixiang', 'wuxing', 'taiyang', 'taiyin', 'shaoyang', 'shaoyin', 'chongqi']
    
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
        l1_anchor="zpzq_v1.0.0_天地之间_一气而已_001_L1",
    )
    version: str = "1.0.0"
