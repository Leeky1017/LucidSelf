"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066817
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
    semantic_id="smth_v1.0.0_2_格局成败与神煞吉凶_001",
    book_id="sanming",
    engine_id="bazi"
)
class 2格局成败与神煞吉凶(SemanticEntry):
    """
    - 原文（source_text）：
  六壬生临午位，号曰禄马同乡；癸日坐向巳宫，乃是财官双美。
  财多身弱，正为富屋贫人；以煞化权，定显寒门贵客。
  登科甲第，官星临无破之官；纳粟奏名，财库居...
    """
    
    original_text: str = """- 原文（source_text）：
  六壬生临午位，号曰禄马同乡；癸日坐向巳宫，乃是财官双美。
  财多身弱，正为富屋贫人；以煞化权，定显寒门贵客。
  登科甲第，官星临无破之官；纳粟奏名，财库居生旺之地。
  官贵太盛，才临旺处必倾；印绶被伤，倘若荣华不久。
  有官有印无破，作廊庙之材；无印无官有格，乃朝廷之用。
  名题金榜，须还身旺逢官；得佐圣君，贵在冲官逢合。
  非格非局，见之焉得为奇；身弱遇官，得后徒然费力。
  小人命内，亦有正印官星；君子格中，也犯七煞羊刃。
  生平少病，日主高强；一世安然，财命有气。
  官刑不犯，印绶与天德同宫；少乐多忧，盖缘日主自弱。
  身强煞浅，假煞为权；煞重身轻，终身有损。
  衰则变官为鬼，旺则化鬼为官。

- 分字分词释义：
  - **禄马同乡**：壬午日（丁己同宫）。
  - **财官双美**：癸巳日（丙戊同宫）。
  - **富屋贫人**：财多身弱，不能任财。
  - **以煞化权**：杀印相生或食神制杀。
  - **冲官逢合**：如飞天禄马冲官，又见合神（未必吉，古注解释不一，或指冲出官星被合住为我用）。
  - **财命有气**：财星与日主皆有气。

- **规范化释义（primary_lang_explained）**：
  六壬日生于午时（或日），叫禄马同乡；六癸日坐巳宫，叫财官双美。
  财多身弱，好比富屋里的贫人（看得到吃不到）。以煞化权（制化得宜），定是寒门出身的贵客。
  考中科甲，是因为官星无破。捐官（纳粟），是因为财库生旺。
  官星太盛（官多变鬼），又行财旺运，必倾败。印绶被财伤，即使荣华也不长久。
  有官有印且无破，是国家的栋梁之材。无官无印但成别格（如食伤、从格等），也能为朝廷所用。
  金榜题名，必须身旺逢官。辅佐圣君，贵在冲官（如飞天）或逢合（官星被合为用）。
  不成格局，哪有什么奇特？身弱遇官，得到了也费力难守。
  小人命里也有正印官星（但可能被破或无根）；君子格中也有七煞羊刃（但有制化）。
  生平少病，是因为日主高强。一世安然，是因为财星和日主都有气。
  不犯官刑，是因为印绶与天德贵人同宫。少乐多忧，是因为日主太弱。
  身强煞浅，煞可化为权柄。煞重身轻，终身受损。
  日主衰弱，官星也会变成鬼（克身）；日主旺相，鬼（煞）也能化为官（权）。

- 核心要点：
  - **身财平衡**：忌财多身弱。
  - **身煞平衡**：忌煞重身轻。
  - **格局纯杂**：君子小人看制化。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_049]` `[trigger: 禄马同乡]` `[factor_trigger: luma_tongxiang AND caiguan_shuangmei]` `[role: 主干]` 六壬生临午位，号曰禄马同乡；癸日坐向巳宫，乃是财官双美。 → 《三命通会》卷十一#格局成败与神煞吉凶
  - `[ns_smth_11_050]` `[trigger: 富屋贫人]` `[factor_trigger: fuwu_pinren AND caibuo_shenruo]` `[role: 主干依赖]` 财多身弱，正为富屋贫人；以煞化权，定显寒门贵客。 → 《三命通会》卷十一#格局成败与神煞吉凶
  - `[ns_smth_11_051]` `[trigger: 登科纳粟]` `[factor_trigger: dengke_nashu AND guanxing_wupo]` `[role: 条件分支]` 登科甲第，官星临无破之官；纳粟奏名，财库居生旺之地。 → 《三命通会》卷十一#格局成败与神煞吉凶
  - `[ns_smth_11_052]` `[trigger: 官鬼转化]` `[factor_trigger: bianguan_weigui AND huagui_weiguan]` `[role: 条件分支]` 衰则变官为鬼，旺则化鬼为官。 → 《三命通会》卷十一#格局成败与神煞吉凶
  - `[ns_smth_11_053]` `[trigger: 身强煞浅]` `[factor_trigger: shenqiang_shaqian AND jiesha_weiquan]` `[role: 总结]` 身强煞浅，假煞为权；煞重身轻，终身有损。 → 《三命通会》卷十一#格局成败与神煞吉凶"""
    normalized_text_zh: str = """"""
    subject: str = "2 格局成败与神煞吉凶"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_33', 'bazi_semantic', 'bazi_state_factor_89', 'bazi_semantic', 'bazi_state_huaquan', 'bazi_semantic', 'bazi_relation_factor_33', 'bazi_semantic', 'bazi_state_factor_173', 'bazi_semantic', 'bazi_condition_factor_18', 'bazi_semantic', 'source_ref', 'rel_smth_11_046', 'core_factor', 'rel_smth_11_047', 'cond_factor', 'rel_smth_11_048', 'risk_factor', 'evi_smth_11_046', 'core_factor', 'rule_name46', 'evi_smth_11_047', 'cond_factor', 'rule_name47', 'evi_smth_11_048', 'risk_factor', 'rule_name48', 'map_smth_11_031', 'map_smth_11_032']
    
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
        l1_anchor="smth_v1.0.0_2_格局成败与神煞吉凶_001_L1",
    )
    version: str = "1.0.0"
