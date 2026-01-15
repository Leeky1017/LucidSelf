"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492182
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
    semantic_id="zpzq_v1.0.0_支中喜忌_透清_之后才真正见用_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 支中喜忌透清之后才真正见用(SemanticEntry):
    """
    - **原文（source_text）**：
  二十八、论支中喜忌逢运透清。
  支中喜忌，固与干有别矣，而运逢透清，则静而待用者，正得其用，而喜忌之验，于此乃见。何谓透清？如甲用酉官，逢辰未即为财...
    """
    
    original_text: str = """- **原文（source_text）**：
  二十八、论支中喜忌逢运透清。
  支中喜忌，固与干有别矣，而运逢透清，则静而待用者，正得其用，而喜忌之验，于此乃见。何谓透清？如甲用酉官，逢辰未即为财，而运透戊，逢午未即为伤，而运透丁之类是也。

  若命与运二支会局，亦作清论。如甲用酉官，本命有午，而运逢寅戌之类。然在年则重，在日次之，至于时生于午，而运逢寅戌会局，则缓而不急矣。虽格之成败高低，八字已有定论，与命中原有者不同，而此五年中，亦能炒其祸福。若月令之物，而运中透清，则与命中原有者，不甚相悬，即前篇所谓行运成格变格是也。

  故凡一八字到手，必须逐干逐支，上下统看。支为干之生地，干为支之发用。如命中有一甲字，则统观四支，有寅亥卯未等字否，有一字，皆甲木之根也。有一亥字，则统观四支，有壬甲二字否。有壬，则亥为壬禄，以壬水用；用甲，则亥为甲长生，以甲木用；用壬甲俱全，则一以禄为根，一以长生为根，二者并用。取运亦用此术，将本命八字，逐干支配之而已。

- 原注（原文注解）：
  　　本章承接“干支喜忌有别”与“成格变格”两篇，说明：
  - 地支中所藏的喜忌之神，平时多“静而待用”；
  - 一旦行运之天干把它“透清”，或行运之地支与之会局成势，便会转为现实中的祸福；
  - 因此，支中喜忌之验，往往在“逢运透清”时才显现.

  首段以“甲用酉官”作例：
  - 命局中辰未本为财之根，午未本为伤之根；
  - 单有辰未、午未在支中，尚属“静根”，只是潜在的财与伤；
  - 当运透戊，则辰未之财“透清”为天干；
  - 当运透丁，则午未之伤“透清”为天干；
  - 如此，原本“藏于支中”的财、伤才真正成为可用或可忌之力.

  次段说明“命与运二支会局”的情况：
  - 若甲用酉官，本命已有午，运再逢寅戌，会成寅午戌火局；
  - 此时，火局成势，足以伤金官，故亦视为“透清”；
  - 但须分年、日、时所居之不同：
    - 若火局在年上则为“重”，影响及祖上与早年环境；
    - 在日柱则居中；
    - 在时柱则多见于晚景与子息方面，且“缓而不急”.

  作者特别指出：
  - 尽管格局成败高低，八字原局早有定论；
  - 但在“这五年”会局之内，仍能对祸福起明显推动作用.

  再下一段回归总法：
  - 看一命，须“逐干逐支，上下统看”：
    - 支为干之生地，是根源；
    - 干为支之发用，是表现；
  - 例如命中有一甲字：
    - 就要反观四支是否有寅亥卯未等木根；
    - 有一亥字，则再看四干是否有壬甲：
      - 用壬，则亥为壬禄；
      - 用甲，则亥为甲长生；
      - 壬甲俱全，则一以禄为根，一以长生为根，二者并用.
  - 取运亦同此法：
    - 把运来之干支当作“新加入的一对干支”；
    - 逐一配对本命干支，观察其会合、透出与生克.

- 分字分词释义：
  - 支中喜忌：藏于地支中的喜用神与忌神.
  - 透清：从地支藏干中明透到天干，或通过会局使其属性清晰可见.
  - 静而待用：潜伏不动，尚未形成现实事件的力量.
  - 财：在例中多指戊土偏财.
  - 伤：在例中多指丁火伤官.
  - 会局：若干地支会合成一气，如寅午戌火局等.
-  - 生地 / 发用：地支为根气之地，天干为其发挥作用之处.
  - 禄：长生帝旺系统中的“禄位”，主力量集中之处.
  - 长生：十二长生中的起始位，主生发之源.

- **规范化释义（primary_lang_explained）**：
  本章要我们改掉一个习惯性的“平面思维”：
  - 不仅要看“表面有无某神”，还要看“支里藏着什么”以及“什么时候会被激活”。

  核心逻辑有三层：
  1) 支中藏神先看清：
     - 例如辰未中土为财、午未中火为伤；
     - 在静态命局中，它们只是“潜力值”。
  2) 运来“透清”或“会局”的年份，是潜伏力量转为现实的关键点：
     - 运干透戊，则财星从支中翻到台面；
     - 运干透丁，则伤官从支中翻到台面；
     - 运支成局，则某一五行气势成团出击.
  3) 这些年内，虽然格局高低已由原命决定，但祸福起伏会特别集中显现：
     - 有时是“原本便该好的运”在此处具体兑现；
     - 有时是“原本潜藏的病处”在此处集中爆发.

- **完整对等诠释（secondary_lang_full）**：  
  Many of the chart’s true joys and hates lie buried in the branches, waiting for the right triggers. When luck-stems draw out hidden stems from the branches, or when luck-branches help complete a局, these latent codes are brought to the surface: what used to be quiet roots become moving manifestations. Years in which such structures are clarified tend to concentrate both blessings and troubles, even though the ultimate level of nobility or baseness has already been set by the natal pattern.

  This is why we must distinguish between “potential” and “already active” forces. A configuration may look peaceful for many years simply because certain harms have not yet been fully exposed, while its basic dignity is already present in the background. Only when luck透清 or completes a局 do we see delayed rewards come due or long-hidden weaknesses burst forth. Compared with the general discussion of喜忌 and of stem–branch differences, this chapter emphasizes that reading luck is above all reading when the codes hidden in the branches are finally triggered.

- 详细解说：
  - 与“行运总论”和“干支有别”相比，本章更强调：
    - **行运是读取“支中潜代码”的事件触发器**；
    - 没有行运透清或会局，很多潜力不会被完全显化.
  - 它也提醒我们：
    - 命局分析若只停留在“看天干”和“看月令”，则对许多支中喜忌的理解会大打折扣；
    - 真正精细的判断，要把“支中根气 + 行运透清”当作一个整体系统看.

- **校勘与字词辨析（双语）**：
  - **中文**：本稿据通行本，经文用字保持原貌，标点现代化处理。
  - **English**: Based on standard edition. Original text preserved, punctuation modernized.

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_458]` `[trigger: 刃格取运]` `[factor_trigger: renge_quyun AND xi_guansha_ji_caixing]` `[role: 主干]` 刃格取运，喜官煞忌财星。 → 《子平真诠》#下卷第44章
  - `[ns_zpzy_459]` `[trigger: 干透之妙]` `[factor_trigger: xishen_tougan AND yingyan_sujie]` `[role: 主干]` 喜神透干，应验速捷。 → 《子平真诠》#下卷
  - `[ns_zpzy_460]` `[trigger: 阳刃之用]` `[factor_trigger: yangren_he_sha AND quanwei_xianhe]` `[role: 主干]` 阳刃合煞，权威显赫。 → 《子平真诠》#下卷
  - `[ns_zpzy_461]` `[trigger: 财旺生官]` `[factor_trigger: cai_wang_sheng_guan AND fugui_shuangquan]` `[role: 主干]` 财旺生官，富贵双全。 → 《子平真诠》#下卷
  - `[ns_zpzy_462]` `[trigger: 印绶生身]` `[factor_trigger: yinshou_sheng_shen AND xueye_youcheng]` `[role: 主干]` 印绶生身，学业有成。 → 《子平真诠》#下卷
  - `[ns_zpzy_463]` `[trigger: 煞运逢食]` `[factor_trigger: shayun_feng_shi AND quanwei_xianhe]` `[role: 主干]` 煞运逢食，权威显赫。 → 《子平真诠》#下卷
  - `[ns_zpzy_464]` `[trigger: 伤运逢财]` `[factor_trigger: shangyun_feng_cai AND jiyi_shengcai]` `[role: 主干]` 伤运逢财，技艺生财。 → 《子平真诠》#下卷
  - `[ns_zpzy_465]` `[trigger: 刃格行运]` `[factor_trigger: ren_ge AND xi_guansha_zhiren_yun]` `[role: 主干]` 刃格喜官煞制刃运。 → 《子平真诠》#下卷
  - `[ns_zpzy_466]` `[trigger: 禄格行运]` `[factor_trigger: lu_ge AND sui_yongshen_er_ding_yun]` `[role: 主干]` 禄格随用神而定运。 → 《子平真诠》#下卷
  - `[ns_zpzy_467]` `[trigger: 阴阳调和]` `[factor_trigger: yinyang_tiaohe AND zhonghe_weigui]` `[role: 主干]` 阴阳调和，中和为贵。 → 《子平真诠》#下卷
  - `[ns_zpzy_468]` `[trigger: 相神得用]` `[factor_trigger: xiangshen_deyong=true AND fuge_yougong]` `[role: 主干]` 相神得用，辅格有功。 → 《子平真诠》#下卷
  - `[ns_zpzy_469]` `[trigger: 时柱归宿]` `[factor_trigger: shizhu_guisu AND zixi_zhigong]` `[role: 主干]` 时柱归宿，子息之宫。 → 《子平真诠》#下卷"""
    normalized_text_zh: str = """"""
    subject: str = "支中喜忌“透清”之后才真正见用"
    factor_refs: list = ['touqing', 'zhizhong_xiji', 'yuntou', 'huiju_jihuo', 'engine_id', 'zhicang_xiji', 'bazi_rule_engine', 'yun_touqing', 'bazi_rule_engine', 'yun_huiju', 'bazi_rule_engine', 'cangshen_jihuo', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_136', 'yun_touqing', 'rel_zpzq_137', 'yun_huiju', 'evi_zpzq_122', 'yun_touqing', 'rule_touqing_shibie', 'evi_zpzq_123', 'yun_huiju', 'rule_huiju_jihuo', 'concept_activation', 'concept_latent']
    
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
        l1_anchor="zpzq_v1.0.0_支中喜忌_透清_之后才真正见用_001_L1",
    )
    version: str = "1.0.0"
