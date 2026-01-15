"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227292
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
    semantic_id="smth_v1.0.0_无名有名与太易太初_001",
    book_id="sanming",
    engine_id="bazi"
)
class 无名有名与太易太初(SemanticEntry):
    """
    - **原文（source_text）**：
  老子日：无名，天地之始；有名，万物之毋。有物混成，先天地生。列圉寇日：有形生于无形。天地之初，有太易，有太初，有太始，有太素。太易者，未见气；太初者，...
    """
    
    original_text: str = """- **原文（source_text）**：
  老子日：无名，天地之始；有名，万物之毋。有物混成，先天地生。列圉寇日：有形生于无形。天地之初，有太易，有太初，有太始，有太素。太易者，未见气；太初者，气之始；太始者，形之始；太素者，质之始。气与形质合而未离，曰浑沦。

- **分字分词释义**：
  - **无名**：不可名状之道体 / 天地之始 / 本体层最高概念
  - **有名**：可指称之万物与诸像 / 万物之母 / 展开层起点
  - **太易**：气未见 / 混然而未判 / 宇宙演化第一阶段
  - **太初**：气之始动 / 有气未形 / 宇宙演化第二阶段
  - **太始**：形之始 / 有形未质 / 宇宙演化第三阶段
  - **太素**：质之始 / 形质具而阴阳未分 / 宇宙演化第四阶段
  - **有形生于无形**：万物有形皆本于无形之道与元气 / 本体论基础命题
  - **浑沦**：气与形未分 / 浑成一团之状态 / 混沌未判

- **规范化释义（primary_lang_explained）**：
  本段先引《老子》《列子》，说明：在天地未分之先，只是一个不可名状的「道」，从无名之道生出有名之万物。有物混成、先于天地而生；其时只见一团浑沦未判的元气。后来才依次出现太易、太初、太始、太素几个阶段：由气未显，到气动、形起、质具，渐渐走向「可以指称的世界」。宇宙的起点并不是具体的水火金木，而是这一团难以区分理、气、形、质的混沌之气。

- **完整对等诠释（secondary_lang_full）**：
  Drawing on Laozi and Liezi, this paragraph portrays a pre-cosmic phase in which only an unnameable Dao exists; from this nameless source all later, nameable beings arise. Before heaven and earth are separated there is merely a mixed, undivided mass of primordial qi. Only afterwards does it differentiate step by step into stages later called Taiyi, Taichu, Taishi and Taisu: first qi stirs, then form appears, then substantial quality is established. The point for destiny study is that water, fire, metal, wood and every later structure are late products of this unfolding. A birth chart is therefore a cross-section of how that one original qi has been divided and arranged at a particular moment, not an arbitrary numerical pattern detached from this deeper ontological process.

- **核心要点**：
  - 一切命局之成，追本必归于「一气混成」的宇宙观，而非孤立的五行数字
  - 五行只是后起的分化层面，背后有更高一层的「道/无名」作为根源
  - 太易→太初→太始→太素构成宇宙演化的四阶段模型
  - 命局只是这一演化链条中较后端的一个截面

- **详细解说**：
  本条确立了命理学的本体论基础。古人不把五行当作宇宙的起点，而是把它们放在「道→太极→阴阳→五行→干支」的分化链条中理解。这意味着：任何命局分析都应先有「整体气机」的意识，再落到具体五行与干支的层面。工程化命理时，也应把「宇宙论层次」当作最顶层约束，使规则库的结构与经典中的层次一一对应。

- **校勘与字词辨析（双语）**：
  - **中文**：「日」古本多作「曰」，此处据电子底本仍录作「日」；「毋」义当作「母」；「列圉寇」当作「列御寇」，为传写讹字。
  - **English**：The character "日" in classical texts often appears as "曰"; "毋" should be understood as "母" (mother); "列圉寇" is a scribal error for "列御寇" (Lie Yukou), author of Liezi.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_001]` `[trigger: 论命理本体]` `[factor_trigger: ontology_level=cosmology]` `[role: 主干]` 无名，天地之始；有名，万物之母。 → 《三命通会》卷一#无名有名条
  - `[ns_smth_002]` `[trigger: 宇宙演化阶段]` `[factor_trigger: cosmic_stage IN (taiyi,taichu,taishi,taisu)]` `[role: 主干依赖]` 太易者，未见气；太初者，气之始；太始者，形之始；太素者，质之始。 → 《三命通会》卷一#无名有名条
  - `[ns_smth_003]` `[trigger: 混沌状态]` `[factor_trigger: qi_state=hunlun]` `[role: 条件分支]` 气与形质合而未离，曰浑沦。 → 《三命通会》卷一#无名有名条
  - `[ns_smth_004]` `[trigger: 五行定位]` `[factor_trigger: wuxing_level=derived]` `[role: 总结]` 五行只是后起的分化层面，背后有更高一层的「道/无名」作为根源。 → 《三命通会》卷一#无名有名条
  - `[ns_smth_500]` `[trigger: 暗鬼消神]` `[factor_trigger: an_gui_xiaoshen]` `[role: 条件分支]` 暗鬼消神，主暗中耗损。 → 《三命通会》卷一
  - `[ns_smth_501]` `[trigger: 暗财强度]` `[factor_trigger: ancai_qiangdu]` `[role: 条件分支]` 暗财强度高主偏财旺。 → 《三命通会》卷一
  - `[ns_smth_502]` `[trigger: 暗冲气用]` `[factor_trigger: anchong_qiyong_score]` `[role: 条件分支]` 暗冲气用分数高主动荡。 → 《三命通会》卷一
  - `[ns_smth_503]` `[trigger: 暗官]` `[factor_trigger: anguan]` `[role: 条件分支]` 暗官透出主权柄。 → 《三命通会》卷一
  - `[ns_smth_504]` `[trigger: 暗合机遇]` `[factor_trigger: anhe_jiyu_score]` `[role: 条件分支]` 暗合机遇分数高主暗中助力。 → 《三命通会》卷一
  - `[ns_smth_505]` `[trigger: 暗静守分]` `[factor_trigger: anjing_shoufen]` `[role: 条件分支]` 暗静守分主平稳。 → 《三命通会》卷一
  - `[ns_smth_506]` `[trigger: 暗禄合处路径]` `[factor_trigger: anlu_hechu_lujing]` `[role: 条件分支]` 暗禄合处路径主财源。 → 《三命通会》卷一
  - `[ns_smth_507]` `[trigger: 秋金火炼]` `[factor_trigger: autumn_metal_fire_forge]` `[role: 条件分支]` 秋金火炼成器。 → 《三命通会》卷一
  - `[ns_smth_508]` `[trigger: 八卦方位丙位]` `[factor_trigger: bagua_fangwei_bingwei]` `[role: 条件分支]` 八卦方位丙位主南方。 → 《三命通会》卷一
  - `[ns_smth_509]` `[trigger: 白帝克木风险]` `[factor_trigger: baidi_kemu_risk]` `[role: 条件分支]` 白帝克木有风险。 → 《三命通会》卷一
  - `[ns_smth_510]` `[trigger: 白虎鬼山]` `[factor_trigger: baihu_guishan]` `[role: 条件分支]` 白虎鬼山主凶险。 → 《三命通会》卷一
  - `[ns_smth_511]` `[trigger: 白虎持势]` `[factor_trigger: baihuchishi_presence]` `[role: 条件分支]` 白虎持势主凶。 → 《三命通会》卷一
  - `[ns_smth_512]` `[trigger: 百中逢印]` `[factor_trigger: baizhong_fengyin]` `[role: 条件分支]` 百中逢印主贵。 → 《三命通会》卷一
  - `[ns_smth_513]` `[trigger: 半禄沉雅]` `[factor_trigger: banlu_chenya]` `[role: 条件分支]` 半禄沉雅主平常。 → 《三命通会》卷一
  - `[ns_smth_514]` `[trigger: 保护机制]` `[factor_trigger: baohu_jizhi]` `[role: 条件分支]` 保护机制完善主吉。 → 《三命通会》卷一
  - `[ns_smth_515]` `[trigger: 八专类型]` `[factor_trigger: bazhuan_leixing]` `[role: 条件分支]` 八专日主刚毅。 → 《三命通会》卷一
  - `[ns_smth_516]` `[trigger: 八专禄旺]` `[factor_trigger: bazhuanluwang_presence]` `[role: 条件分支]` 八专禄旺主权柄。 → 《三命通会》卷一
  - `[ns_smth_517]` `[trigger: 背禄类型]` `[factor_trigger: beilu_leixing]` `[role: 条件分支]` 背禄主失禄。 → 《三命通会》卷一
  - `[ns_smth_518]` `[trigger: 背禄逐马风险]` `[factor_trigger: beilu_zhuma_risk]` `[role: 条件分支]` 背禄逐马主凶险。 → 《三命通会》卷一
  - `[ns_smth_519]` `[trigger: 本命核心]` `[factor_trigger: benben_hexin]` `[role: 主干]` 本命核心为日主。 → 《三命通会》卷一
  - `[ns_smth_520]` `[trigger: 比肩分福]` `[factor_trigger: bijian_fenfu]` `[role: 条件分支]` 比肩分福主分争。 → 《三命通会》卷一
  - `[ns_smth_521]` `[trigger: 比肩克亲风险]` `[factor_trigger: bijian_keqin_risk]` `[role: 条件分支]` 比肩克亲有风险。 → 《三命通会》卷一
  - `[ns_smth_522]` `[trigger: 比肩伤劫风险]` `[factor_trigger: bijian_shangjie_risk]` `[role: 条件分支]` 比肩伤劫有风险。 → 《三命通会》卷一
  - `[ns_smth_523]` `[trigger: 比肩同宫]` `[factor_trigger: bijian_tonggong]` `[role: 条件分支]` 比肩同宫主争竞。 → 《三命通会》卷一
  - `[ns_smth_524]` `[trigger: 比肩同禄]` `[factor_trigger: bijian_tonglu]` `[role: 条件分支]` 比肩同禄主分禄。 → 《三命通会》卷一
  - `[ns_smth_525]` `[trigger: 阴阳]` `[factor_trigger: yinyang]` `[role: 主干]` 阴阳为天地之本，万物之根，太极动静所生。 → 《三命通会》卷一#太极元气条
  - `[ns_smth_526]` `[trigger: 四象]` `[factor_trigger: si_xiang]` `[role: 主干]` 四象为阴阳再分所生，太阳太阴少阳少阴，化生万物。 → 《三命通会》卷一#太极元气条
  - `[ns_smth_527]` `[trigger: 八卦]` `[factor_trigger: ba_gua]` `[role: 主干]` 八卦为四象再分，乾坤艮巽震离坎兑，定方位吉凶。 → 《三命通会》卷一#太极元气条
  - `[ns_smth_528]` `[trigger: 门冲驷马]` `[factor_trigger: mencho ng_siuma]` `[role: 条件分支]` 门冲驷马为神煞组合，主奔波动荡。 → 《三命通会·卷十一》#运途得失与神煞吉凶
  - `[ns_smth_529]` `[trigger: 比劫夺财]` `[factor_trigger: bijie_duocai]` `[role: 条件分支]` 比劫夺财为比肩劫财争夺财星，主财运受损。 → 《三命通会·卷八》#六甲日戊辰时
  - `[ns_smth_530]` `[trigger: 比劫夺财风险]` `[factor_trigger: bijie_duocai_risk]` `[role: 条件分支]` 比劫夺财风险为比劫争财的危险程度。 → 《三命通会·卷六》#论正财
  - `[ns_smth_531]` `[trigger: 比劫分夺风险]` `[factor_trigger: bijie_fenduo_risk]` `[role: 条件分支]` 比劫分夺风险为比劫分夺的危险程度。 → 《三命通会·卷六》#论偏财
  - `[ns_smth_532]` `[trigger: 比劫分禄风险]` `[factor_trigger: bijie_fenlu_risk]` `[role: 条件分支]` 比劫分禄风险为比劫分禄的危险程度。 → 《三命通会·卷六》#日禄归时
  - `[ns_smth_533]` `[trigger: 比劫过重]` `[factor_trigger: bijie_guozhong]` `[role: 条件分支]` 比劫过重为比肩劫财太旺的状态。 → 《三命通会·卷六》#论建禄
  - `[ns_smth_534]` `[trigger: 比劫劫夺风险]` `[factor_trigger: bijie_jieduo_risk]` `[role: 条件分支]` 比劫劫夺风险为比劫劫财的危险程度。 → 《三命通会·卷六》#天元坐财
  - `[ns_smth_535]` `[trigger: 并冲力度]` `[factor_trigger: bingchong_lidu]` `[role: 条件分支]` 并冲力度为同时冲击的强度。 → 《三命通会·卷六》#冲禄
  - `[ns_smth_536]` `[trigger: 并冲力度非驰]` `[factor_trigger: bingchong_lidu_feichi]` `[role: 条件分支]` 并冲力度非驰为并冲力度的特殊状态。 → 《三命通会·卷六》#飞天禄马
  - `[ns_smth_537]` `[trigger: 丙申]` `[factor_trigger: bingshen]` `[role: 条件分支]` 丙申为丙火坐申金。 → 《三命通会·卷九》#六己日丁卯时
  - `[ns_smth_538]` `[trigger: 丙午制杀]` `[factor_trigger: bingwu_zhisha]` `[role: 条件分支]` 丙午制杀为丙午克制七杀。 → 《三命通会·卷八》#六甲日壬申时
  - `[ns_smth_539]` `[trigger: 丙戊辛生福连]` `[factor_trigger: bingwuxin_shengfu_lian]` `[role: 条件分支]` 丙戊辛生福连为丙戊辛相生的吉配。 → 《三命通会·卷六》#六阴朝阳
  - `[ns_smth_540]` `[trigger: 不见财官无冲破]` `[factor_trigger: bujian_caiguan_wu_chongpo]` `[role: 条件分支]` 不见财官无冲破为无财官且无冲破。 → 《三命通会·卷九》#六壬日辛亥时
  - `[ns_smth_541]` `[trigger: 不见庚辛]` `[factor_trigger: bujian_gengxin]` `[role: 条件分支]` 不见庚辛为命局无庚辛金。 → 《三命通会》
  - `[ns_smth_542]` `[trigger: 不见官星惹帮]` `[factor_trigger: bujian_guanxing_rebang]` `[role: 条件分支]` 不见官星惹帮为无官星且有比劫。 → 《三命通会》
  - `[ns_smth_543]` `[trigger: 不壬不乙]` `[factor_trigger: buren_buyi]` `[role: 条件分支]` 不壬不乙为命局无壬水乙木。 → 《三命通会》
  - `[ns_smth_544]` `[trigger: 财印扶持]` `[factor_trigger: cai_yin_fuchi]` `[role: 条件分支]` 财印扶持为财星印星相互扶持。 → 《三命通会》
  - `[ns_smth_545]` `[trigger: 财印支持分]` `[factor_trigger: cai_yin_support_score]` `[role: 条件分支]` 财印支持分为财印配置的强度评分。 → 《三命通会》
  - `[ns_smth_546]` `[trigger: 财印中介配置]` `[factor_trigger: cai_yin_zhongjie_config]` `[role: 条件分支]` 财印中介配置为财印调停的格局配置。 → 《三命通会》
  - `[ns_smth_547]` `[trigger: 财帛聚散]` `[factor_trigger: caibo_jusan]` `[role: 条件分支]` 财帛聚散为财运聚散的程度。 → 《三命通会》
  - `[ns_smth_548]` `[trigger: 财藏禄程度]` `[factor_trigger: caicanglu_chengdu]` `[role: 条件分支]` 财藏禄程度为财星与禄的藏匿程度。 → 《三命通会》
  - `[ns_smth_549]` `[trigger: 财格分型]` `[factor_trigger: caige_fenxing]` `[role: 条件分支]` 财格分型为财格的细分类型。 → 《三命通会》
  - `[ns_smth_550]` `[trigger: 财格强度]` `[factor_trigger: caige_qiangdu]` `[role: 条件分支]` 财格强度为财格的旺衰程度。 → 《三命通会》
  - `[ns_smth_551]` `[trigger: 财格组合类型]` `[factor_trigger: caige_zuhe_leixing]` `[role: 条件分支]` 财格组合类型为财格与他格的组合模式。 → 《三命通会》
  - `[ns_smth_552]` `[trigger: 财官暗藏]` `[factor_trigger: caiguan_ancang]` `[role: 条件分支]` 财官暗藏为财官藏于地支的状态。 → 《三命通会》
  - `[ns_smth_553]` `[trigger: 财官并见]` `[factor_trigger: caiguan_bingjian]` `[role: 条件分支]` 财官并见为财星官星同时出现。 → 《三命通会》"""
    normalized_text_zh: str = """"""
    subject: str = "无名有名与太易太初"
    factor_refs: list = ['cosmology_wuming', 'cosmology_youming', 'cosmic_stage_taiyi', 'cosmic_stage_taichu', 'cosmic_stage_taishi', 'cosmic_stage_taisu', 'qi_state_hunlun', 'yuanqi']
    
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
        l1_anchor="smth_v1.0.0_无名有名与太易太初_001_L1",
    )
    version: str = "1.0.0"
