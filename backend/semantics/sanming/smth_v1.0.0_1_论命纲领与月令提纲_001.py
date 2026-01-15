"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066777
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
    semantic_id="smth_v1.0.0_1_论命纲领与月令提纲_001",
    book_id="sanming",
    engine_id="bazi"
)
class 1论命纲领与月令提纲(SemanticEntry):
    """
    - **原文（source_text）**：
  四柱排定，三才次分。专以日上天元，配合八字支干。有见不见之形，无时不有；神煞相绊，轻重较量。
  若乃时逢七煞，见之未必为凶；月制干强，其煞反为权印。...
    """
    
    original_text: str = """- **原文（source_text）**：
  四柱排定，三才次分。专以日上天元，配合八字支干。有见不见之形，无时不有；神煞相绊，轻重较量。
  若乃时逢七煞，见之未必为凶；月制干强，其煞反为权印。
  财官印绶全备，藏蓄于四季之中。
  官星财气长生，镇居于寅申巳亥。
  阳水叠逢辰位，是壬骑龙背之乡；阴木独遇子时，为六乙鼠贵之地。
  庚日全逢润下，忌壬癸巳午之方；时遇子申，其福减半。
  若逢伤官月建，如凶处未必为凶；内有正倒禄飞，忌官星亦嫌羁绊。

- 分字分词释义：
  - **时逢七煞**：时上一位贵格。
  - **四季**：辰戌丑未（杂气财官印）。
  - **长生**：寅申巳亥（四生）。
  - **食神干旺**：专食合禄格（戊日庚申时，庚合乙官）。
  - **遇而不遇**：遇贵格而被填实冲破（甲丙卯寅破戊日庚申格）。
  - **月生日干**：月令印绶。
  - **日禄归时**：归禄格。
  - **壬骑龙背**：壬辰日多辰。
  - **六乙鼠贵**：乙日子时。
  - **润下**：井栏叉格（庚日申子辰全）。
  - **正倒禄飞**：飞天禄马、倒冲禄马。

- **规范化释义（primary_lang_explained）**：
  排定四柱，分清天地人三才。专以日干为主，配合八字干支进行分析。
  明见之形与不见之形（虚邀），无时无刻不存在。神煞相互羁绊，要较量轻重。
  时柱若逢七煞，未必是凶，如果月令有制伏且日干强旺，七煞反而化为权力和印信（威权）。
  财官印绶若全备，多藏在辰戌丑未四季土中（杂气财官印）。官星财气的长生之地，多在寅申巳亥四生之方。
  戊日逢庚申时，庚金食神干旺，合乙木官星。若岁月见甲（煞）、丙（枭）、卯（官）、寅（煞长生），则破格，遇而不遇。
  月令生助日干且天干无财星坏印，是标准的印绶格。日主禄神在时支且无官星填实，叫日禄归时，主青云得路。
  壬水日主多逢辰字，是壬骑龙背格。乙木日主独遇子时（无官煞），是六乙鼠贵格。
  庚日地支全逢申子辰水局（润下），忌见壬癸（透出则非井栏叉，为伤官）、巳午（官煞填实）。若时支遇子或申（归禄或刃），福气减半（井栏叉喜申时，子时亦可，此处指填实或冲破？注云：时遇丙子则偏官，甲申则归禄，难成井栏叉）。
  若月建是伤官，看似凶险，其实未必。其中可能有飞天禄马、倒冲禄马等格（如庚日生子月，冲午官），此时忌见官星填实，也嫌合神羁绊。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Fate Analysis Principles and Month令Outline" from the Xi-Ji Chapter:

  - Four Pillars排定, Three Talents次分. Specialize日上天元, match八字支干.
  - Time逢Seven Killing, see之未必凶; month制干强, its Killing反为权印.
  - Wealth-Official-Seal全备, hidden蓄于四季中 (Chen-Xu-Chou-Wei).
  - Ren骑Dragon-Back (Ren-Chen多辰); Six-Yi鼠贵 (Yi-Day子时).
  - Key: Special patterns (壬骑龙背, 六乙鼠贵, 井栏叉, 飞天禄马) require specific conditions; filling in breaks pattern.

- 核心要点：
  - **时煞有制**：化为权印。
  - **杂气财官**：辰戌丑未。
  - **特殊格局**：专食、归禄、龙背、鼠贵、井栏叉、飞天。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_033]` `[trigger: 时煞有制]` `[factor_trigger: shisha_youzhi AND huawei_quanyin]` `[role: 主干]` 若乃时逢七煞，见之未必为凶；月制干强，其煞反为权印。 → 《三命通会》卷十一#论命纲领与月令提纲
  - `[ns_smth_11_034]` `[trigger: 杂气财官]` `[factor_trigger: zaqi_caiguan AND siji_cangxu]` `[role: 主干依赖]` 财官印绶全备，藏蓄于四季之中。官星财气长生，镇居于寅申巳亥。 → 《三命通会》卷十一#论命纲领与月令提纲
  - `[ns_smth_11_035]` `[trigger: 壬骑龙背]` `[factor_trigger: renqi_longbei AND liuyi_shugui]` `[role: 条件分支]` 阳水叠逢辰位，是壬骑龙背之乡；阴木独遇子时，为六乙鼠贵之地。 → 《三命通会》卷十一#论命纲领与月令提纲
  - `[ns_smth_11_036]` `[trigger: 伤官禄飞]` `[factor_trigger: shangguan_lufei AND jiguan_xianjiban]` `[role: 总结]` 若逢伤官月建，如凶处未必为凶；内有正倒禄飞，忌官星亦嫌羁绊。 → 《三命通会》卷十一#论命纲领与月令提纲"""
    normalized_text_zh: str = """"""
    subject: str = "1 论命纲领与月令提纲"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_state_factor_215', 'bazi_semantic', 'bazi_state_ren', 'bazi_semantic', 'bazi_structure_yi_1', 'bazi_semantic', 'bazi_structure_factor_28', 'bazi_semantic', 'bazi_state_factor_77', 'bazi_semantic', 'bazi_condition_factor_13', 'bazi_semantic', 'source_ref', 'rel_smth_11_034', 'core_factor', 'rel_smth_11_035', 'cond_factor', 'rel_smth_11_036', 'risk_factor', 'evi_smth_11_034', 'core_factor', 'rule_name34', 'evi_smth_11_035', 'cond_factor', 'rule_name35', 'evi_smth_11_036', 'risk_factor', 'rule_name36', 'map_smth_11_023', 'map_smth_11_024']
    
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
        l1_anchor="smth_v1.0.0_1_论命纲领与月令提纲_001_L1",
    )
    version: str = "1.0.0"
