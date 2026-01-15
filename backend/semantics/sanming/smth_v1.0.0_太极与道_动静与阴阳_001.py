"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227350
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
    semantic_id="smth_v1.0.0_太极与道_动静与阴阳_001",
    book_id="sanming",
    engine_id="bazi"
)
class 太极与道动静与阴阳(SemanticEntry):
    """
    - **原文（source_text）**：
  庄子以道在太极之先，所谓太极，乃是指天、地、人三者气形已具而未判者之名，而道又别是一悬空底物，在太极之先。不知道即太极，太极即道，以其理之通行者言，则...
    """
    
    original_text: str = """- **原文（source_text）**：
  庄子以道在太极之先，所谓太极，乃是指天、地、人三者气形已具而未判者之名，而道又别是一悬空底物，在太极之先。不知道即太极，太极即道，以其理之通行者言，则曰道，以其理之极至者言，则曰太极，又何尝有二邪？向非周子启其秘，朱子阐而明之，孰知太极之为理，而与气自不相离也哉？所谓太极者，乃阴阳动静之本体，不离于形气，而实无声臭，不穷于变化，而实有准则。故一动一静，互为其根，分阴分阳，两仪立焉。仪者，物也。凡物未始无对，而亦未尝独立。天以生覆而依乎地，地以形载而附乎天。有理斯有气，阴阳之谓也；有气斯有形，天地之谓也。天地不生于天地，而生于阴阳；阴阳不生于阴阳，而生于动静；动静不生于动静，而生于太极。盖太极者，本然之妙也；动静者，所乘之机也；阴阳者，所生之本也。太极，形而上，道也；阴阳，形而下，器也。动静无端，阴阳无始，此造化所由立焉。柏齐何子曰：天，阳之动者也，果何时动极而静子？地，阴之静者也，果何时静极而动乎？天不能生地，水不能生火，无智愚皆知之，乃谓阴阳相生，不亦误乎？天地水火，虽浑然不可离，实灿然不可乱。故阴之与阳，谓之相依则可，谓之相生则不可；谓之互藏其宅则可，谓之互藏相生则不可。此言的。有见也。

- **分字分词释义**：
  - **道即太极**：从「理」的角度看，太极与道是同一件事的不同名称。
  - **动静**：气机运行的两端，一动一静互为其根。
  - **阴阳**：就动静、升降、刚柔所显出的两类性格，是一切分化之纲。
  - **相依/相生**：作者主张阴阳「相依」而非彼此「相生」，以避免误解为物质性的生殖关系。

- **规范化释义（primary_lang_explained）**：
  这一段先回应「道在太极之先」的看法，指出：若从理的角度看，道与太极其实是一回事，只是一个偏重「通行无所不在」，一个偏重「极至之体」。太极是阴阳动静的本体，不离形气，又超出一切有声有臭的具体事物。动静互根，则阴阳分位；阴阳分位，则天地万物得以显形。阴阳之间是「互相依存」而不是「彼此生出彼此」，天不能生地，水不能生火，只能说「同在大气机中，各有所职」。

- **完整对等诠释（secondary_lang_full）**：

  This section answers the claim that Dao stands "before" Taiji by arguing that, from the standpoint of principle, they are simply two names for the same reality: Dao emphasises all-pervading operation, Taiji emphasises ultimate ground. Taiji is the underlying body of movement and stillness, never leaving concrete qi and form yet not reducible to any particular thing. From the alternation of movement and rest arise the positions of Yin and Yang, and from the differentiation of Yin and Yang the manifest heaven, earth and myriad beings. Crucially, Yin and Yang are described as mutually dependent rather than literally producing one another: heaven does not give birth to earth, water does not give birth to fire. Instead they share a single field of qi in which each plays its appointed role. When we read a chart, we are therefore mapping how this one field polarises into complementary poles, not treating Yin and Yang as two independent substances that manufacture one another.

- **核心要点**：
  - 命理上的阴阳，不是简单的「谁生谁、谁克谁」，而是动静升降、刚柔进退的整体系统；
  - 任何命局的分析，不可把阴阳看成两个可以互相「生造」的东西，而应看作一个系统中彼此依赖的两端。

- **应用推演（操作顺序）：
  1) 观命局全盘，先从阴阳动静入手：看日主及用神所处之位，是偏于动（多冲合、刑害、临驿马、行奔走之运），还是偏于静（多根气、坐库、守印绶）；
  2) 将“道/太极”的层次落地为“总的生活方向与价值观”：分析一个命局时，先问其根本取向（道）是否稳定，再看阴阳动静的用法是否与之相协；
  3) 判断“相依”而非“相生”：在解释干支关系时，不以“阴生阳”“阳生阴”为机械因果，而看两者是否在同一气机体系内互为依凭（如财官印比的配合，而非孤立的生克）；
  4) 设计修正策略时，以“太极不动、动静为用”为原则：保全命局中最能代表“本体”的那部分（根、印、用神之源），而在行运与选择上调整动静与阴阳的节奏。

- **反例与边界**：
  - 以“阳生阴、阴生阳”来类比男女生殖，或以为某一支可以凭空生出另一支，这是把哲学层面的阴阳错读成物理繁殖；
  - 在解命时，只看到某星“来生我”或“我生某星”，而不看其在全局中的动静位次（是否主线、是否有根、有无节制），导致结论非常机械；
  - 把“太极即道”理解成“只要讲玄理就好”，于是拒绝任何具体的结构分析、格局区分，这会让命理变成空谈；
  - 反向的误区则是：只认格局、全凭十神组合打分，不愿承认其上还有“本体—动静—阴阳”的更高一层结构，导致系统难以解释复杂反例。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_010]` `[trigger: 道与太极关系]` `[factor_trigger: dao=taiji]` `[role: 主干]` 道即太极，太极即道。 → 《三命通会》卷一#太极与道条
  - `[ns_smth_011]` `[trigger: 动静互根]` `[factor_trigger: movement_stillness=mutual_root]` `[role: 主干依赖]` 一动一静，互为其根。 → 《三命通会》卷一#太极与道条
  - `[ns_smth_012]` `[trigger: 阴阳相依]` `[factor_trigger: yinyang_relation=interdependence]` `[role: 主干依赖]` 谓之相依则可，谓之相生则不可。 → 《三命通会》卷一#太极与道条
  - `[ns_smth_013]` `[trigger: 批判相生]` `[factor_trigger: yinyang_generation=false]` `[role: 例外处理]` 天不能生地，水不能生火。 → 《三命通会》卷一#太极与道条
  - `[ns_smth_550]` `[trigger: 财官并透]` `[factor_trigger: caiguan_bingtou]` `[role: 条件分支]` 财官并透主富贵。 → 《三命通会》卷一
  - `[ns_smth_551]` `[trigger: 财官不破]` `[factor_trigger: caiguan_bupo]` `[role: 条件分支]` 财官不破主福禄。 → 《三命通会》卷一
  - `[ns_smth_552]` `[trigger: 财官成格]` `[factor_trigger: caiguan_chengge]` `[role: 条件分支]` 财官成格主大贵。 → 《三命通会》卷一
  - `[ns_smth_553]` `[trigger: 财官得位]` `[factor_trigger: caiguan_dewei]` `[role: 条件分支]` 财官得位主尊荣。 → 《三命通会》卷一
  - `[ns_smth_554]` `[trigger: 财官得用]` `[factor_trigger: caiguan_deyong]` `[role: 条件分支]` 财官得用主富贵。 → 《三命通会》卷一
  - `[ns_smth_555]` `[trigger: 财官格组合类型]` `[factor_trigger: caiguan_ge_zuhe_leixing]` `[role: 条件分支]` 财官格组合类型定格局高低。 → 《三命通会》卷一
  - `[ns_smth_556]` `[trigger: 财官强度]` `[factor_trigger: caiguan_qiangdu]` `[role: 条件分支]` 财官强度高主大富贵。 → 《三命通会》卷一
  - `[ns_smth_557]` `[trigger: 财官全美]` `[factor_trigger: caiguan_quanmei]` `[role: 条件分支]` 财官全美主大贵。 → 《三命通会》卷一
  - `[ns_smth_558]` `[trigger: 财官生印]` `[factor_trigger: caiguan_shengyin]` `[role: 条件分支]` 财官生印主富贵双全。 → 《三命通会》卷一
  - `[ns_smth_559]` `[trigger: 财官透出]` `[factor_trigger: caiguan_touchu]` `[role: 条件分支]` 财官透出主显达。 → 《三命通会》卷一
  - `[ns_smth_560]` `[trigger: 财官印三奇]` `[factor_trigger: caiguan_yin_sanqi]` `[role: 条件分支]` 财官印三奇主大贵。 → 《三命通会》卷一
  - `[ns_smth_561]` `[trigger: 财官印透]` `[factor_trigger: caiguan_yin_tou]` `[role: 条件分支]` 财官印透主贵显。 → 《三命通会》卷一
  - `[ns_smth_562]` `[trigger: 财官支撑]` `[factor_trigger: caiguan_zhicheng]` `[role: 条件分支]` 财官支撑主富贵有根。 → 《三命通会》卷一
  - `[ns_smth_563]` `[trigger: 财旺生官]` `[factor_trigger: caiwang_shengguan]` `[role: 条件分支]` 财旺生官主富贵。 → 《三命通会》卷一
  - `[ns_smth_564]` `[trigger: 财旺生杀]` `[factor_trigger: caiwang_shengsha]` `[role: 条件分支]` 财旺生杀身弱主凶。 → 《三命通会》卷一
  - `[ns_smth_565]` `[trigger: 财星得位]` `[factor_trigger: caixing_dewei]` `[role: 条件分支]` 财星得位主富。 → 《三命通会》卷一
  - `[ns_smth_566]` `[trigger: 财星配置]` `[factor_trigger: caixing_peizhi]` `[role: 条件分支]` 财星配置合理主发财。 → 《三命通会》卷一
  - `[ns_smth_567]` `[trigger: 财星强度]` `[factor_trigger: caixing_qiangdu]` `[role: 条件分支]` 财星强度高主大富。 → 《三命通会》卷一
  - `[ns_smth_568]` `[trigger: 财运连绵]` `[factor_trigger: caiyun_lianmian]` `[role: 结果]` 财运连绵主持续发达。 → 《三命通会》卷一
  - `[ns_smth_569]` `[trigger: 财源广进]` `[factor_trigger: caiyuan_guangjin]` `[role: 结果]` 财源广进主财运亨通。 → 《三命通会》卷一
  - `[ns_smth_570]` `[trigger: 沉静禄马]` `[factor_trigger: chenjing_luma]` `[role: 条件分支]` 沉静禄马主稳定发达。 → 《三命通会》卷一
  - `[ns_smth_571]` `[trigger: 乘旺入墓]` `[factor_trigger: chengwang_rumu]` `[role: 条件分支]` 乘旺入墓主收藏。 → 《三命通会》卷一
  - `[ns_smth_572]` `[trigger: 冲合效应]` `[factor_trigger: chonghe_xiaoying]` `[role: 条件分支]` 冲合效应决定动静。 → 《三命通会》卷一
  - `[ns_smth_573]` `[trigger: 冲克危害]` `[factor_trigger: chongke_weihai]` `[role: 条件分支]` 冲克危害大主灾厄。 → 《三命通会》卷一
  - `[ns_smth_574]` `[trigger: 冲破效应]` `[factor_trigger: chongpo_xiaoying]` `[role: 条件分支]` 冲破效应决定成败。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "太极与道、动静与阴阳"
    factor_refs: list = ['bazi_semantic', 'new_candidate', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'dao', 'taiji', 'movement_stillness', 'yinyang', 'yinyang_interdependence']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_太极与道_动静与阴阳_001_L1",
    )
    version: str = "1.0.0"
