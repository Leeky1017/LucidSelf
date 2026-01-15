"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.080832
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
    semantic_id="smth_v1.0.0_1_五行生克与太过不及_001",
    book_id="sanming",
    engine_id="bazi"
)
class 1五行生克与太过不及(SemanticEntry):
    """
    - 原文（source_text）：
  元一气生五行，统三才周万物。发乾坤之妙用，剖阴阳之枢机。在乎推四方，分其贵贱；得其中道，八字一定荣枯。是以强明其生克制化，清浊贵贱，寿夭贤愚。
  金赖土生，...
    """
    
    original_text: str = """- 原文（source_text）：
  元一气生五行，统三才周万物。发乾坤之妙用，剖阴阳之枢机。在乎推四方，分其贵贱；得其中道，八字一定荣枯。是以强明其生克制化，清浊贵贱，寿夭贤愚。
  金赖土生，土多金埋；土赖火生，火多土焦；火赖木生，木多火炽；木赖水生，水多木漂；水赖金生，金多水浊。
  金能生水，水多金沉；水能生木，木盛水缩；木能生火，火多木焚；火能生土，土多火晦；土能生金，金多土变。
  金能克木，木坚金缺；木能克土，土重木折；土能克水，水多土流；水能克火，火炎水热；火能克金，金多火熄。
  金衰遇火，必见销镕；火弱逢水，必为熄灭；水弱逢土，必为淤塞；土衰遇木，必遭倾陷；木弱逢金，必为砍折。
  强金得水，方挫其锋；强水得木，方泄其势；强木得火，方化其顽；强火得土，方止其焰；强土得金，方制其害。

- 分字分词释义：
  - **元一气**：太极元气。
  - **中道**：中和之道。
  - **太过**：母慈灭子（如土多金埋），子旺母衰（如木盛水缩），反克（如木坚金缺）。
  - **强金得水**：旺金喜食伤泄秀。

- 规范化释义（primary_lang_explained）：  
  本节从“元一气生五行，统三才周万物”立纲，强调命理推断必须先看到一个整体的五行系统，而不是零散的干支点数。太极元气分化为金木水火土，分别在天地人三才中承担生、克、泄、承受的不同角色；若其中任何一行太过或不及，都会破坏“中道”，在清浊贵贱、寿夭贤愚上体现为明显偏差。因此，真正的推命工作，不只是背诵生克口诀，而是观察整盘命局的能量流向：谁在生谁，谁在克谁，谁被泄耗，谁又承担压力。  
  赋文用三组条目具体展示失衡的样貌：第一组是“母子相生”的太过之害，如土多金埋、水盛木漂，说明过度供给反而会压制受生者的发挥；第二组是泄耗过甚导致的衰竭，如金生水而水多金沉、火生土而土重火晦，提醒我们过度付出同样会耗干自身根基；第三组是相克失衡与反侮，如木坚金缺、土重木折、水冲土流，指出被克一方若过强，就会反伤克星。最后，“强金得水”“强木得火”“强火得土”等句，把调候原则总结为一句话：五行太强者宜泄宜制，太弱者宜扶宜护；只有在生克制化各得其所时，命局才算真正接近“中和为贵”。  

- 完整对等诠释（secondary_lang_full）：  
  This opening passage establishes a cosmological framework for chart reading. From a single primordial qi arise the Five Elements, which in turn structure Heaven, Earth and Humanity. Metal, Wood, Water, Fire and Earth do not simply coexist; they constantly generate, control, drain and support one another. Any element that becomes excessively strong or excessively weak will disturb this balance of "the middle way" and will show up in life as distortions of status, lifespan or character. To interpret a chart, then, is to trace the circulation of energy through this fivefold system rather than to add up isolated points of how much Metal or how much Wood there are.  
  The text illustrates imbalance through three contrasting sets. The first concerns overindulgent generation: Earth that is too abundant buries Metal, over‑flowing Water makes Wood drift, and so on—gifts that turn into burdens. The second treats excessive draining, where giving away too much of oneself leads to exhaustion: Metal that endlessly produces Water sinks, Fire that continually births Earth loses its brightness. The third examines lopsided control and backlash, such as Wood so firm that it damages Metal, or Water so overwhelming that it washes away Earth; here the controlled element no longer yields but strikes back. The closing lines, in which strong Metal "needs" Water, strong Wood "needs" Fire, and so forth, state a practical rule for adjustment: what is too strong must be guided through leakage and restraint, what is too weak must be nourished and protected. A chart approaches true harmony only when all five are allowed to work within reasonable bounds, neither smothered nor left to run wild.  

- 核心要点：
  - **生克相对**：生多为害，克多反侮。
  - **强弱喜忌**：强喜泄制，弱喜生扶。
  - **中和为贵**：五行不可偏枯。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_001]` `[trigger: 元一气生]` `[factor_trigger: yuanyiqi_sheng AND tongsan_zhouwan]` `[role: 主干]` 元一气生五行，统三才周万物。发乾坤之妙用，剖阴阳之枢机。 → 《三命通会》卷十二#五行生克与太过不及
  - `[ns_smth_12_002]` `[trigger: 土多金埋]` `[factor_trigger: tuduo_jinmai AND shuisheng_mupiao]` `[role: 主干依赖]` 金赖土生，土多金埋；土赖火生，火多土焦；火赖木生，木多火炽。 → 《三命通会》卷十二#五行生克与太过不及
  - `[ns_smth_12_003]` `[trigger: 木坚金缺]` `[factor_trigger: mujian_jinque AND fangke_fanwu]` `[role: 条件分支]` 金能克木，木坚金缺；木能克土，土重木折；土能克水，水多土流。 → 《三命通会》卷十二#五行生克与太过不及
  - `[ns_smth_12_004]` `[trigger: 强金得水]` `[factor_trigger: qiangjin_deshui AND cuoqi_feng]` `[role: 总结]` 强金得水，方挫其锋；强水得木，方泄其势；强木得火，方化其顽。 → 《三命通会》卷十二#五行生克与太过不及"""
    normalized_text_zh: str = """"""
    subject: str = "1 五行生克与太过不及"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_wuxing', 'bazi_semantic', 'bazi_state_state_4', 'bazi_semantic', 'bazi_state_zi_zi', 'bazi_semantic', 'bazi_relation_geju', 'bazi_semantic', 'bazi_unnamed', 'bazi_semantic', 'bazi_wuxing_3', 'bazi_semantic', 'source_ref', 'rel_smth_12_001', 'core_factor', 'rel_smth_12_002', 'cond_factor', 'rel_smth_12_003', 'risk_factor', 'evi_smth_12_001', 'core_factor', 'rule_name1', 'evi_smth_12_002', 'cond_factor', 'rule_name2', 'evi_smth_12_003', 'risk_factor', 'rule_name3', 'map_smth_12_001', 'map_smth_12_002']
    
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
        l1_anchor="smth_v1.0.0_1_五行生克与太过不及_001_L1",
    )
    version: str = "1.0.0"
