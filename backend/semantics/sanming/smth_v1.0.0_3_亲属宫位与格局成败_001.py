"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066707
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
    semantic_id="smth_v1.0.0_3_亲属宫位与格局成败_001",
    book_id="sanming",
    engine_id="bazi"
)
class 3亲属宫位与格局成败(SemanticEntry):
    """
    - 原文（source_text）：
  兄弟破财，财得用；煞官欺主，主须从。
  一马在厩，人不敢逐；一马在野，人共逐之。
  财临生库破生宫，兼奉两家宗嗣。
  身坐比肩成比局，当为几度新郎。
 ...
    """
    
    original_text: str = """- 原文（source_text）：
  兄弟破财，财得用；煞官欺主，主须从。
  一马在厩，人不敢逐；一马在野，人共逐之。
  财临生库破生宫，兼奉两家宗嗣。
  身坐比肩成比局，当为几度新郎。
  父母一离一合，须知印绶临财。
  夫妻随娶随伤，盖为比肩伏马。
  子位子填，孤嗟伯道；妻宫妻守，贤齐孟光。
  入库伤官，阴生阳死；帮身羊刃，喜合嫌冲。
  权刃复行权刃，刀药亡身；财官再遇财官，贪污罢职。
  禄到长生原有印，清任加官；马行帝旺旧无伤，宦途进爵。
  财旺身衰，逢生即死；刃强财薄，见煞生官。

- 分字分词释义：
  - **兄弟破财**：比劫去财（若财为忌，如从煞格，去财为喜？注云：比劫冲破财宫，财为我用。如辛酉日冲卯财）。
  - **马在厩/野**：财透干无根或有库为厩（保护），财露无根或被比劫围困为野。
  - **子位子填**：时支（子位）被官煞（子星）填实（若官煞为忌或太多，反无子）。
  - **妻宫妻守**：日支坐财（妻），无刑冲。
  - **权刃**：煞（权）刃。

- **规范化释义（primary_lang_explained）**：
  比劫（兄弟）若能冲破忌神财星（或冲出财星），则财为我用。官煞太旺欺主，日主必须从煞。
  财星（马）若在地支有库或根深（在厩），比劫不敢争夺；若财星虚浮无根（在野），比劫必争。
  财星临长生或墓库，又被冲破，主过继或双挑（兼奉两家）。
  日主坐比肩（如己未、癸亥），地支又成比劫局，主克妻，多婚。
  印绶（母）临财（父），财印相克，父母离异或不和。
  比肩藏在财星之下（伏马），或财坐比劫，主克妻。
  时柱（子位）被官煞（子星）填实（忌神），或伤官填实，主无子。日支（妻宫）坐财（妻星），主妻贤。
  伤官入库，阴干（如乙木伤官在戌）为生，阳干（如甲木伤官在丑）为死。羊刃帮身，喜合（如丙日刃在午，喜戌合），嫌冲（子冲午）。
  原命煞刃重，行运再遇煞刃，主凶死。原命财官旺，行运再遇财官，主贪污罢职（物极必反）。
  禄临长生且有印，主清贵加官。财星（马）行帝旺运且无伤，主进爵。
  财旺身衰（从财？），若逢印比生身（逆势），反主死灾。羊刃强财星薄，若见七煞制刃，反能生官（煞印相生或煞制刃护财生官）。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Family Positions and Pattern Success-Failure" from the Six Spirits Chapter:

  - One Horse in stable, people dare not chase; one Horse in wild, people together chase—Wealth protected vs exposed.
  - Body sits Parallel forms Parallel pattern, should be several-times new-groom—克妻多婚.
  - Father-mother one-离one-合, must know Seal approaches Wealth—父母不和.
  - Power-Blade再行 Power-Blade, knife-medicine亡body; Wealth-Official再遇 Wealth-Official, greedy-corrupt罢position.
  - Key: Horse in stable (protected Wealth) vs Horse in wild (exposed Wealth); family relations reflect five element interactions.

- 核心要点：
  - **财星保护**：喜藏忌露（在野）。
  - **六亲刑克**：比劫克妻，财印相碍。
  - **物极必反**：财官太旺反罢职。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_021]` `[trigger: 马在厩野]` `[factor_trigger: mazai_jiuye AND bijie_zhengduo]` `[role: 主干]` 一马在厩，人不敢逐；一马在野，人共逐之。 → 《三命通会》卷十一#亲属宫位与格局成败
  - `[ns_smth_11_022]` `[trigger: 比肩克妻]` `[factor_trigger: bijian_keqi AND jidu_xinlang]` `[role: 主干依赖]` 身坐比肩成比局，当为几度新郎。 → 《三命通会》卷十一#亲属宫位与格局成败
  - `[ns_smth_11_023]` `[trigger: 权刃亡身]` `[factor_trigger: quanren_wangshen AND caiguan_bazhi]` `[role: 条件分支]` 权刃复行权刃，刀药亡身；财官再遇财官，贪污罢职。 → 《三命通会》卷十一#亲属宫位与格局成败
  - `[ns_smth_11_024]` `[trigger: 见煞生官]` `[factor_trigger: jiansha_shengguan AND renqiang_caibo]` `[role: 总结]` 刃强财薄，见煞生官。 → 《三命通会》卷十一#亲属宫位与格局成败"""
    normalized_text_zh: str = """"""
    subject: str = "3 亲属宫位与格局成败"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_11', 'bazi_semantic', 'bazi_structure_factor_12', 'bazi_semantic', 'bazi_relation_factor_15', 'bazi_semantic', 'bazi_relation_factor_16', 'bazi_semantic', 'bazi_state_factor_54', 'bazi_semantic', 'bazi_condition_factor_9', 'bazi_semantic', 'source_ref', 'rel_smth_11_016', 'liuqin_guanxi', 'rel_smth_11_017', 'wuji_bifan', 'rel_smth_11_018', 'quanren_chongfeng', 'evi_smth_11_016', 'caiyin_xiangai', 'rule_caiyin_xiangai1', 'evi_smth_11_017', 'wuji_bifan', 'rule_wuji_bifan1', 'evi_smth_11_018', 'quanren_chongfeng', 'rule_quanren_chongfeng1', 'map_smth_11_011', 'map_smth_11_012']
    
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
        l1_anchor="smth_v1.0.0_3_亲属宫位与格局成败_001_L1",
    )
    version: str = "1.0.0"
