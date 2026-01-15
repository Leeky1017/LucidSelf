"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.080920
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
    semantic_id="smth_v1.0.0_3_其他贵格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 3其他贵格(SemanticEntry):
    """
    - 原文（source_text）：
  甲乙若遇乾宫，会辰龙而必贵。
  木神如逢壬癸，得巳午以为佳。
  庚遇壬癸，坐煞印而周瑜位重。
  龟蛇持剑，兼金刃而贾复名高。
  庚辛重而时见巳亥，虎啸...
    """
    
    original_text: str = """- 原文（source_text）：
  甲乙若遇乾宫，会辰龙而必贵。
  木神如逢壬癸，得巳午以为佳。
  庚遇壬癸，坐煞印而周瑜位重。
  龟蛇持剑，兼金刃而贾复名高。
  庚辛重而时见巳亥，虎啸风生；得戊己以相资，官居极品。
  一气相生，称五行之顺食，位近三台。
  金神带刃，遇火地之炎明，官居内阁。
  时上偏官，喜劫刃印财而居岁月。
  父传子道，兼文武将相而显朝廷。
  伤官透而正官隐，运煞印而位重权高。
  地天交而阴阳感，得戊己而三台八座。
  木盛金繁，得离明而公忠正直。
  金白水清，遇长生而聪明出众。
  火明木秀，逢土现而早占鳌头。
  水木在春生，遇土金而作公侯之贵。
  金逢火炼，早年出仕；木得金裁，幼岁成名。
  金多失火，嗟性地之凶顽；木盛无金，叹功名之不遂。
  土重而无木疏通，困苦奔波之辈；水盛而无土制伏，破家淫荡之人。
  火盛而无水济，死而无悔之暴夫；木衰火盛变灰飞，功名迟而难逃夭折。
  金白水清被枭害，文章秀而莫永天年。
  金白水清脱枭神，而文章益显。
  煞官两露，遇二德而爵位崇高。
  财资七煞，子仪司将相之高权。
  金神带煞，寇准擅庙堂之大器。
  岁德逢财，煞栽根，早登显仕；更加印刃，无妒合，预擢高科。
  月七煞而时岁食，肃宪府风霜之号令。
  月煞印而时伤官，受凤阁龙楼之厚宠。
  日丙火而时入亥宫，丽乎天而文明四海。
  干阳荧而时逢己丑，出乎地而照耀山川。
  时辛亥而日逢丁，乃时三奇而科名早中。
  月建申而岁时遇子，为坤坎顺而将相可期。
  时离岁巽，日阴金透甲乙，为三台之贵。
  木秀火明春秉令，入斯象夺榜眼之魁。
  食神带刃，结局而位至三公；食神带刃，坐官而勋高一品。
  官星带刃，班超万里封侯；岁月得时，周勃特然入相。
  财官双美，透财印而居台省之尊；运至比肩，更刑冲抱守株之拙。
  财官生旺，天干透露为奇，而曳紫拖朱。
  财旺生官，印刃相扶为妙，而三台八座。
  干食神而时骑禄马，初年题虎榜之荣名。
  透印绶而格得财官，早岁镇边隅之重任。
  日干健旺而印刃相扶，龚胜尽汉家之死节。
  官星带刃而印绶带煞，元龄步唐代之瀛洲。
  三公之任，在乎煞刃司权；各遇长生，更得财资极贵。
  司要枢，总戎政，因劫带印以资官。
  伸枉抑，理冤愆，为财生煞而助印。
  进直言，趋金阙，因煞刃两露于天干。
  居翰苑而掌丝纶，为正官归禄于四柱。
  年正印而月正官，居国监翰林之任。
  格清奇而时得令，唱鸿胪玉殿之名。
  平邦国，统六师，赖官星变为天德。
  理阴阳，登宰辅，因禄马又带长生。
  格局纯和而日干自弱，览泉石而好幽栖。
  格局薄弱而用神轻微，纵资生而无过小职。
  土重而支神厚载，畏元武而喜青龙，格局苟逢，必膺大贵。
  木盛而土厚逢荧，顺东方而行坤地，柱运顺和，定显功名。
  土多而居坤艮之上，则天道下济而光明。
  刃逢禄马三奇，得令透财，为公侯一品之贵。
  柱会水火二局，露金藏土，为龟蛇持剑之形。
  财星变德而坐煞，李靖兼文武全材。
  煞刃得印以相资，汲黯作朝廷之耳目。
  伤带财印兼生旺，而持纲持纪。
  柱均火土，逢木气而为国为民。
  王曾魁众士，因官印带食以相扶。
  叶正占鳌头，赖印星自官而自禄。
  身旺无财官之辅，非技艺而必僧流。
  女人犯二德之纯，受宠章而沾凤诰。

- 分字分词释义：
  - **龟蛇持剑**：水火二局，露金（剑）藏土（制）。
  - **父传子道**：乙日壬午时（乙生午，壬生乙，木火通明）。
  - **地天交**：亥（天）申（地）。
  - **金白水清**：庚辛生秋月，见水。
  - **木秀火明**：甲乙生春月，见火。
  - **财星变德**：财星与二德同宫。

- **核心要点**：
  - **龟蛇持剑**：水火金三才武贵。
  - **金白水清**：秋金见水文贵。
  - **煞刃司权**：三公之任。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_013]` `[trigger: 龟蛇持剑]` `[factor_trigger: guishe_chijian AND shuihuo_erjiu]` `[role: 主干]` 龟蛇持剑，兼金刃而贾复名高。柱会水火二局，露金藏土，为龟蛇持剑之形。 → 《三命通会》卷十二#其他贵格
  - `[ns_smth_12_014]` `[trigger: 金白水清]` `[factor_trigger: jinbai_shuiqing AND congming_chuzhong]` `[role: 主干依赖]` 金白水清，遇长生而聪明出众。金白水清脱枭神，而文章益显。 → 《三命通会》卷十二#其他贵格
  - `[ns_smth_12_015]` `[trigger: 三公之任]` `[factor_trigger: sangong_zhiren AND sharen_siquan]` `[role: 条件分支]` 三公之任，在乎煞刃司权；各遇长生，更得财资极贵。 → 《三命通会》卷十二#其他贵格
  - `[ns_smth_12_016]` `[trigger: 身旺无财官]` `[factor_trigger: shenwang_wucaiguan AND jiyi_sengdao]` `[role: 总结]` 身旺无财官之辅，非技艺而必僧流。 → 《三命通会》卷十二#其他贵格"""
    normalized_text_zh: str = """"""
    subject: str = "3 其他贵格"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_water_fire', 'water_fire_with_metal_sword', 'bazi_structure_geju', 'sequential_stem_generation', 'bazi_state_metal_water_wood_fire', 'bazi_semantic', 'bazi_relation_factor_40', 'bazi_semantic', 'bazi_relation_unnamed', 'bazi_semantic', 'bazi_relation_factor_41', 'favoured_consort', 'source_ref', 'rel_smth_12_013', 'core_factor', 'rel_smth_12_014', 'cond_factor', 'rel_smth_12_015', 'risk_factor', 'evi_smth_12_013', 'core_factor', 'rule_name13', 'evi_smth_12_014', 'cond_factor', 'rule_name14', 'evi_smth_12_015', 'risk_factor', 'rule_name15', 'map_smth_12_009', 'map_smth_12_010']
    
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
        l1_anchor="smth_v1.0.0_3_其他贵格_001_L1",
    )
    version: str = "1.0.0"
