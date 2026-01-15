"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066827
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
    semantic_id="smth_v1.0.0_3_岁运喜忌与性情疾厄_001",
    book_id="sanming",
    engine_id="bazi"
)
class 3岁运喜忌与性情疾厄(SemanticEntry):
    """
    - 原文（source_text）：
  月生日干，运行不喜财乡；日主无依，却喜运行财地。
  时归日禄，生平不喜官星；阴若朝阳，切忌丙丁离位。
  太岁乃众煞之主，入命未必为殃；若遇战斗之乡，必主刑...
    """
    
    original_text: str = """- 原文（source_text）：
  月生日干，运行不喜财乡；日主无依，却喜运行财地。
  时归日禄，生平不喜官星；阴若朝阳，切忌丙丁离位。
  太岁乃众煞之主，入命未必为殃；若遇战斗之乡，必主刑于本命。
  岁伤日干，有祸必轻；日犯岁君，灾殃必重。
  五行有救，其年反必为财；四柱无情，故论名为克岁。
  庚辛来伤甲乙，丙丁先见无危；丙丁反克庚辛，壬癸遇之不畏。
  戊己愁逢甲乙，干头须要庚辛；壬癸虑遭戊己，甲乙临之有救。
  壬来克丙，须要戊字当头；癸去伤丁，却喜己来相助。
  庚得壬男制丙，夭作长年；甲以乙妹妻庚，凶为吉兆。
  天元虽旺，若无依倚是常人；日主太柔，纵遇财官为寒士。
  女人无煞，带二德作两国之封；男命身强，遇三奇为一品之贵。
  甲逢己而生旺，定怀中正之心；丁遇壬而太过，必犯淫讹之乱。
  金弱遇火炎之地，血疾无疑；土虚逢木旺之乡，脾伤定论。
  筋疼骨痛，皆因木被金伤；眼暗目昏，必是火遭水克。
  金木交争刑战，仁义俱无；水火递互相伤，是非日有。
  是以五行不可偏枯，务禀中和之气。更能绝虑忘思，鉴命无差无误。

- 分字分词释义：
  - **月生日干**：印绶格。
  - **日主无依**：弃命从财（或从煞）。
  - **时归日禄**：日禄归时格，忌官。
  - **阴若朝阳**：六阴朝阳格，忌丙丁午。
  - **岁伤日干**：岁君（流年）克日主。
  - **日犯岁君**：日主克岁君。
  - **乙妹妻庚**：乙庚合（和亲政策）。
  - **二德**：天月二德。
  - **三奇**：财官印或天上三奇。

- **规范化释义（primary_lang_explained）**：
  月令印绶生身，行运不喜见财（财坏印）。日主孤立无依（从格），却喜行财地（从财）。
  日禄归时格，生平不喜见官星（填实）。六阴朝阳格，切忌见丙丁午火（填实冲子）。
  太岁是众煞之主，入命未必有灾（如岁运并临喜用神）。但若与日时发生战斗（刑冲），必主本命受刑。
  流年克日干（上克下），祸患较轻（顺克）。日干克流年（下犯上），灾殃必重（逆克）。
  若五行有救（如食神制煞），日犯岁君反而发财。若四柱无情（无制化），才论为克岁之灾。
  金克木，若有火制金，无危。火克金，若有水制火，不畏。土怕木，干头有金制木。水怕土，有木制土有救。
  水克火（壬克丙），若有戊土制壬，反吉。癸克丁，喜己土制癸。
  庚金被丙火克，若有壬水（食神）制丙，可转夭为寿。甲木被庚金克，若有乙木合庚（贪合忘克），凶为吉兆。
  日主虽旺，若无财官印食倚托，只是常人。日主太弱，纵然财官旺，也是寒士（不能胜任）。
  女命无七煞，且带天月二德，主受封诰（两国之封）。男命身强，遇三奇（财官印），主一品之贵。
  甲己合而生旺，心地中正。丁壬合而太过（无制或多合），主淫乱。
  金弱遇火旺，主血疾（肺金受克）。土虚遇木旺，主脾胃伤。
  木被金伤，主筋骨痛。火遭水克，主眼目昏。
  金木交战，主无仁无义。水火相战，主是非不断。
  所以，五行不可偏枯，必须中和。推命者若能绝虑忘思，静心体悟，鉴命就不会有差误。

- 核心要点：
  - **岁运法则**：日犯岁君重，有救反吉。
  - **制化之妙**：食神制煞，贪合忘克。
  - **性情疾厄**：五行太过的病理。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_054]` `[trigger: 岁日关系]` `[factor_trigger: sui_ri_guanxi AND suishang_rigan]` `[role: 主干]` 岁伤日干，有祸必轻；日犯岁君，灾殃必重。 → 《三命通会》卷十一#岁运喜忌与性情疾厄
  - `[ns_smth_11_055]` `[trigger: 五行有救]` `[factor_trigger: wuxing_youjiu AND fanwei_weicai]` `[role: 主干依赖]` 五行有救，其年反必为财；四柱无情，故论名为克岁。 → 《三命通会》卷十一#岁运喜忌与性情疾厄
  - `[ns_smth_11_056]` `[trigger: 乙妹妻庚]` `[factor_trigger: yimei_qigeng AND tanhe_wangke]` `[role: 条件分支]` 甲以乙妹妻庚，凶为吉兆。 → 《三命通会》卷十一#岁运喜忌与性情疾厄
  - `[ns_smth_11_057]` `[trigger: 五行疾病]` `[factor_trigger: wuxing_jibing AND jinruo_huoyan]` `[role: 条件分支]` 金弱遇火炎之地，血疾无疑；土虚逢木旺之乡，脾伤定论。筋疼骨痛，皆因木被金伤；眼暗目昏，必是火遭水克。 → 《三命通会》卷十一#岁运喜忌与性情疾厄
  - `[ns_smth_11_058]` `[trigger: 中和之气]` `[factor_trigger: zhonghe_zhiqi AND wuxing_buke_pianku]` `[role: 总结]` 是以五行不可偏枯，务禀中和之气。更能绝虑忘思，鉴命无差无误。 → 《三命通会》卷十一#岁运喜忌与性情疾厄"""
    normalized_text_zh: str = """"""
    subject: str = "3 岁运喜忌与性情疾厄"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_relation_factor_35', 'bazi_semantic', 'bazi_relation_factor_36', 'bazi_semantic', 'bazi_condition_wuxing_1', 'bazi_semantic', 'bazi_state_metal_fire', 'bazi_semantic', 'bazi_state_wood_metal', 'bazi_semantic', 'bazi_factor_26', 'bazi_semantic', 'source_ref', 'rel_smth_11_049', 'core_factor', 'rel_smth_11_050', 'cond_factor', 'rel_smth_11_051', 'risk_factor', 'evi_smth_11_049', 'core_factor', 'rule_name49', 'evi_smth_11_050', 'cond_factor', 'rule_name50', 'evi_smth_11_051', 'risk_factor', 'rule_name51', 'map_smth_11_033', 'map_smth_11_034']
    
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
        l1_anchor="smth_v1.0.0_3_岁运喜忌与性情疾厄_001_L1",
    )
    version: str = "1.0.0"
