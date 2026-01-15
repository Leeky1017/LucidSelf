"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596957
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
    semantic_id="qtbj_v1.0.0_2__四季土的喜忌_细论_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2四季土的喜忌细论(SemanticEntry):
    """
    - **原文（source_text）**：
  生于春月，其势虚浮，喜火生扶，恶木太过，忌水泛滥。喜土比助，得金而制木为祥。金太多仍盗土气。
  
  夏月之土，其势燥烈，得盛水滋润成功，忌旺火煅炼...
    """
    
    original_text: str = """- **原文（source_text）**：
  生于春月，其势虚浮，喜火生扶，恶木太过，忌水泛滥。喜土比助，得金而制木为祥。金太多仍盗土气。
  
  夏月之土，其势燥烈，得盛水滋润成功，忌旺火煅炼焦坼。木助火炎，水克无碍。金生水泛，妻才有益，见比肩蹇滞不通。如太过又宜木克。
  
  秋月之土，子旺母衰，金多而秏盗其气，木盛须制伏纯良，火重重而不厌，水泛泛而不祥，得比肩则能助力，至霜降不比无妨。
  
  冬月之土，外寒内温，水旺才丰，金多子秀，火盛有荣，木多无咎，再加比肩扶助为隹，更喜身主康强足寿。

- **分字分词释义**：
  - **势虚浮**：气势虚浮不实 / 春土 / 身弱
  - **喜火生扶**：喜欢火来生扶土 / 火为印星 / 生身
  - **恶木太过**：厌恶木太过克土 / 木为官杀 / 过克
  - **忌水泛滥**：忌水太多冲刷土 / 水为财星 / 漂泊
  - **燥烈**：极其干燥炽烈 / 夏土 / 燥象
  - **盛水滋润**：以大量水滋润燥土 / 水润土 / 调候
  - **焦坼**：焦干龟裂 / 火煅土 / 病象
  - **子旺母衰**：子星太旺母体衰弱 / 金旺土衰 / 泄气
  - **外寒内温**：外表寒冷内里温暖 / 冬土 / 纳火之性
  - **水旺才丰**：水旺则财多 / 水为财 / 富象
  - **金多子秀**：金多子息聪秀 / 金为食伤 / 子秀
  - **身主康强足寿**：日主体健气足 / 土旺有根 / 寿命长

- **规范化释义（primary_lang_explained）**：
  土生于春月（寅卯辰），木旺土虚，土势虚浮，喜欢火来生扶，厌恶木太过（克土），忌讳水泛滥（土流）。喜欢土比肩帮助，得到金来制木（食伤制杀）为吉祥。但金太多仍然会盗泄土的气。
  
  夏天的土（巳午未），火旺土相，气势燥烈，得到盛大的水滋润才能成功，忌讳旺火煅炼导致焦裂。木助长火势（不好），水克火无碍（反喜）。金生水泛，妻财（水）有益，见到比肩（土）则蹇塞停滞不通（土更燥）。如果土太强，又适宜木来克制（疏通）。
  
  秋天的土（申酉戌），金旺土虚，子（金）旺母（土）衰，金多消耗盗泄土气，木盛（官杀）必须有制伏才纯良（食神制杀）。火（印）重重出现也不厌恶（生身制金），水（财）泛滥就不吉祥（身弱财多）。得到比肩就能助力，到了霜降（戌月）土旺，没有比肩也无妨。
  
  冬天的土（亥子丑），外寒内温（土能纳火），水旺财丰，金多子秀（食伤），火盛有荣耀（暖局），木多无咎（杀印相生/火泄），再加比肩扶助为佳，更喜日主康强足以长寿。

- **完整对等诠释（secondary_lang_full）**：
  Earth born in Spring: Its momentum is hollow and floating. It likes Fire support, detests excessive Wood, and dreads flooding Water. It likes Earth assistance; obtaining Metal to control Wood is auspicious. Excessive Metal still steals Earth's Qi.
  
  Earth in Summer: Its momentum is dry and intense. Obtaining abundant Water for nourishment leads to success; dreads intense Fire calcining it to cracks. Wood aids Fire's blaze; Water controlling Fire is no hindrance. Metal generating Water overflow makes Wife/Wealth beneficial; seeing Parallel Shoulders causes obstruction. If Earth is excessive, Wood control is suitable.
  
  Earth in Autumn: Child (Metal) is prosperous, Mother (Earth) is weak. Abundant Metal steals its Qi. Prosperous Wood must be controlled to be pure. Heavy Fire is not disliked. Flooding Water is inauspicious. Obtaining Parallels helps; by Frost Descent (Xu Month), lack of Parallels is fine.
  
  Earth in Winter: Cold outside, warm inside. Prosperous Water means abundant Wealth; abundant Metal means elegant Children; prosperous Fire brings glory; abundant Wood brings no blame. Adding Parallels for support is excellent; it especially likes a strong Self for longevity.

- **核心要点**：
  - **春土**：虚浮。喜火（印）生，金（食伤）制木。忌水（财）多。
  - **夏土**：燥烈。喜水（财）润。忌火（印）焦。
  - **秋土**：泄气。喜火（印）生。忌水（财）多。
  - **冬土**：湿寒。喜火（印）暖，比劫帮身。

- **详细解说**：
  - 春土怕木（官杀），故喜金（食伤）制杀。
  - 夏土怕火（印），故喜水（财）坏印润局。
  - 秋土怕金（食伤），故喜火（印）制食伤生身。
  - 冬土怕水（财），故喜火（印）生身暖局，或土（比劫）帮身胜财。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_297]` `[trigger: 春月之土]` `[factor_trigger: season_spring AND tiangan_earth AND tiangan_huo AND tiangan_mu AND tiangan_shui AND spring_earth_hollow]` `[role: 主干]` 生于春月，其势虚浮，喜火生扶，恶木太过，忌水泛滥。 → 《穷通宝鉴·论土总论》#20.2
  - `[ns_qttbj_298]` `[trigger: 夏月燥土喜水]` `[factor_trigger: season_summer AND tiangan_earth AND tiangan_huo_multiple AND tiangan_shui AND summer_earth_dry]` `[role: 主干]` 夏月之土，其势燥烈，得盛水滋润成功，忌旺火煅炼焦坼。 → 《穷通宝鉴·论土总论》#20.2
  - `[ns_qttbj_299]` `[trigger: 冬月之土]` `[factor_trigger: season_winter AND tiangan_earth AND tiangan_shui AND tiangan_jin AND tiangan_huo AND winter_earth_cold_warm]` `[role: 主干]` 冬月之土，外寒内温，水旺才丰，金多子秀，火盛有荣，木多无咎，再加比肩扶助为隹，更喜身主康强足寿。 → 《穷通宝鉴·论土总论》#20.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 四季土的喜忌（细论）"
    factor_refs: list = ['hollow_floating', 'scorched_cracked', 'child_strong_mother_weak']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_2__四季土的喜忌_细论_001_L1",
    )
    version: str = "1.0.0"
