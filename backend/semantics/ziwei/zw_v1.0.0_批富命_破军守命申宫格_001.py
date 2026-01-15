"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.739969
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
    semantic_id="zw_v1.0.0_批富命_破军守命申宫格_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 批富命破军守命申宫格(SemanticEntry):
    """
    - 分字分词释义：

  - **破军申宫守命**：破军星在申宫守命，主智慧刚傲。
  - **瞏琏器**：《论语》典故，喻大器之材、君子品格。
  - **克己存仁**：克制自己、保存仁心，不畏王侯...
    """
    
    original_text: str = """- 分字分词释义：

  - **破军申宫守命**：破军星在申宫守命，主智慧刚傲。
  - **瞏琏器**：《论语》典故，喻大器之材、君子品格。
  - **克己存仁**：克制自己、保存仁心，不畏王侯却能济贫扶弱。
  - **趒穷恤匮**：扶贫济困的善行，富命的德行特征。
  - **金星居旺地**：金性星曜（武曲/天府）在旺地，助财致富。
  - **七九古稀忘俗世**：七十九岁寿终，忘却尘俗的理想归宿。
  - **王侯也不避**：破军守命之人性情刚傲，不畏权贵。

- **原文（source_text）**：  
  破军守命人智慧，性气傲刚强。王侯也不避，克己以存仁，赒穷而恤匮，功名正路不堪啚，君子人欤瑚琏器。命居申地水之宫，喜得金星居旺地。妻宫劫忌与空亡，鱼水难同戏。儿女宫中见天刑，东败于齐君丁记。传芳分内有双双，应有超群多出类。且道十五童庚满，血光寒暑宜调定。年过二十渐亨通，造化自然多获利。某年某限某宫星，卓尔施为毋自弃。一由命使半由人，当圹先人之大志。有斯命也有斯人，斯德相资当富贵。只愁四八六七傍，须见克伤荆与桂。天眷安然，某星临到此，买田并置地。发福从来果不难，生才运泰诚然易。执守应当福寿全，七九古稀忘俗世。

- **规范化释义（primary_lang_explained）**：  
  此为批断「破军守命于申宫」富命的标准套语。开篇定性：破军守命之人智慧过人、性情刚傲，不畏王侯，却能克己存仁、赒穷恤匮，是「君子人欤瑚琏器」（大器之材）。命居申地（水宫），喜得金星居旺地助财。套语论述六亲（妻宫劫空难偕、子宫天刑艰难但终有传芳）、早年童庚血光、二十后渐亨通、限运买田置地、七九古稀寿终。

- **完整对等诠释（secondary_lang_full）**：  
  This template interprets the "Po Jun Guarding Life in Shen Palace" wealth pattern. Opening characterization: Po Jun guarding Life indicates exceptional wisdom and proud, strong temperament, unafraid of nobles yet capable of self-restraint and benevolence—a "gentleman of ceremonial vessel quality". Life resides in Shen (Water palace), fortunate to have Metal star in prosperity assisting wealth. The template discusses Six Relations (spouse difficult, children challenging but eventually producing heirs), early tribulations, gradual prosperity after twenty, land acquisition, and death at seventy-nine.

- **核心要点**：  
  1. 格局特点：破军申宫守命，金星旺地助财。  
  2. 性情特征：智慧刚傲、不畏王侯、克己存仁。  
  3. 六亲特点：妻宫劫空（婚姻艰难）、子宫天刑（先艰后得）。"""
    normalized_text_zh: str = """"""
    subject: str = "批富命·破军守命申宫格"
    factor_refs: list = ['star_pojun_shengong', 'allusion_hulianqi', 'trait_keji_cunren', 'trait_zhouqiong_xukui', 'pattern_jinxing_wangdi', 'source_ref', 'rel_vol7_13_001', 'star_pojun_shengong', 'rel_vol7_13_002', 'pattern_jinxing_wangdi', 'rel_vol7_13_003', 'trait_zhouqiong_xukui', 'evi_vol7_13_001', 'rule_pojun_shen_junzi', 'evi_vol7_13_002', 'pattern_jinxing_wangdi', 'rule_jinxing_wangdi_fuming', 'evi_vol7_13_003', 'result_pojun_fuming', 'rule_fushouquan_guxi', 'concept_proud_wisdom', 'concept_gentleman_vessel', 'concept_charitable_wealthy']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_批富命_破军守命申宫格_001_L1",
    )
    version: str = "1.0.0"
