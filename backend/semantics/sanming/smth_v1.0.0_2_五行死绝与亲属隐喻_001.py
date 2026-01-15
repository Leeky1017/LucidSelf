"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066651
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
    semantic_id="smth_v1.0.0_2_五行死绝与亲属隐喻_001",
    book_id="sanming",
    engine_id="bazi"
)
class 2五行死绝与亲属隐喻(SemanticEntry):
    """
    - 原文（source_text）：
  五行绝处，禄马扶身；四柱奇中，比肩分福。
  阴阳固有刚柔，干支岂无颠倒。虽聘妻不识其夫，本有子不顾其母。
  父无子而不独，子有父而反孤。
  生尚可以再生...
    """
    
    original_text: str = """- 原文（source_text）：
  五行绝处，禄马扶身；四柱奇中，比肩分福。
  阴阳固有刚柔，干支岂无颠倒。虽聘妻不识其夫，本有子不顾其母。
  父无子而不独，子有父而反孤。
  生尚可以再生，死不可以复死。既死亦非为鬼，逢生又不成人。
  子多母病，如佃甫田；母多子病，如临深渊。

- 分字分词释义：
  - **绝处**：五行长生十二宫之绝地（如木绝于申）。
  - **禄马扶身**：绝处逢生（如木在申，申中壬水长生，为印；庚金为官，戊土为财，财官印俱全）。
  - **比肩分福**：财官虽奇，见比肩争夺则减福。
  - **妻不识夫**：如乙木用庚金为夫，中间丙火隔断，或庚坐子败死之地。
  - **子不顾母**：如甲用丙为子，丙被辛合，贪合忘母。
  - **子多母病**：食伤重泄身。
  - **母多子病**：印重克食伤（枭神夺食），或印多母慈灭子。

- **规范化释义（primary_lang_explained）**：
  五行虽处绝地，但若地支暗藏财官印绶（禄马）扶身，反为吉兆（绝处逢生）。四柱虽有奇仪财官，若比肩重重分夺，福气减半。
  阴阳有刚柔，干支有颠倒。有时虽然有妻星，却配不到夫星（被合或受克）；本来有子星，却不顾母亲（贪合）。
  五行生旺处再遇生旺，是锦上添花（再生）；死绝处再遇死绝，还是死（不可复死，意即已到底）。
  子（食伤）太多，母（日主）泄气病重，如耕种过多的田地，力不从心。母（印绶）太多，子（食伤或日主）受克或被埋没，如临深渊般危险。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Five Elements Extinction and Family Metaphors" from the Qi-Xiang Chapter:

  - Five Elements at extinction place, Salary-Horse supports body; Four Pillars wonders inside, Parallels divide fortune.
  - Wife engaged not knowing husband, originally has child not caring mother—indicates combinations/clashes disrupting family relations.
  - Child-many mother-sick, like farming too much land; mother-many child-sick, like approaching deep abyss.
  - Key: Extinction place meets life (hidden Seal); balance between generating and draining; family metaphors for five element relationships.

- 核心要点：
  - **绝处逢生**：看支藏人元。
  - **六亲关系**：贪合忘亲，多不如少。
  - **母子之道**：泄多身弱，印多坏子。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_005]` `[trigger: 绝处逢生]` `[factor_trigger: juechu_fengsheng AND luma_fushen]` `[role: 主干]` 五行绝处，禄马扶身；四柱奇中，比肩分福。 → 《三命通会》卷十一#五行死绝与亲属隐喻
  - `[ns_smth_11_006]` `[trigger: 妻不识夫]` `[factor_trigger: qi_bushi_fu AND tanhe_wangmu]` `[role: 主干依赖]` 虽聘妻不识其夫，本有子不顾其母。 → 《三命通会》卷十一#五行死绝与亲属隐喻
  - `[ns_smth_11_007]` `[trigger: 子多母病]` `[factor_trigger: ziduo_mubing AND diantian_licong]` `[role: 条件分支]` 子多母病，如佃甫田；母多子病，如临深渊。 → 《三命通会》卷十一#五行死绝与亲属隐喻
  - `[ns_smth_11_008]` `[trigger: 再生复死]` `[factor_trigger: zaisheng_fusi AND shengjue_bianhua]` `[role: 总结]` 生尚可以再生，死不可以复死。既死亦非为鬼，逢生又不成人。 → 《三命通会》卷十一#五行死绝与亲属隐喻"""
    normalized_text_zh: str = """"""
    subject: str = "2 五行死绝与亲属隐喻"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_7', 'bazi_semantic', 'bazi_relation_zi', 'bazi_semantic', 'bazi_relation_zi_1', 'bazi_semantic', 'bazi_state_bijian', 'bazi_semantic', 'bazi_condition_factor_6', 'bazi_semantic', 'bazi_factor_22', 'bazi_semantic', 'source_ref', 'rel_smth_11_004', 'wuxing_sijue', 'rel_smth_11_005', 'bijian_fenfu', 'rel_smth_11_006', 'luma_fushen', 'evi_smth_11_004', 'liuqin_yunshu', 'rule_liuqin_yunshu1', 'evi_smth_11_005', 'bijian_fenfu', 'rule_bijian_fenfu1', 'evi_smth_11_006', 'luma_fushen', 'rule_luma_fushen1', 'map_smth_11_003', 'map_smth_11_004']
    
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
        l1_anchor="smth_v1.0.0_2_五行死绝与亲属隐喻_001_L1",
    )
    version: str = "1.0.0"
