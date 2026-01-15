"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412964
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
    semantic_id="smth_v1.0.0_还魂借气与死绝回生_001",
    book_id="sanming",
    engine_id="bazi"
)
class 还魂借气与死绝回生(SemanticEntry):
    """
    - 原文（source_text）：

  五行自死绝而有救，递相还者。如木绝在申，而遇甲申；金绝在寅，而遇戊寅之类。最吉，有福神次之，无则下。

- 分字分词释义：

  - **五行自死绝而有救*...
    """
    
    original_text: str = """- 原文（source_text）：

  五行自死绝而有救，递相还者。如木绝在申，而遇甲申；金绝在寅，而遇戊寅之类。最吉，有福神次之，无则下。

- 分字分词释义：

  - **五行自死绝而有救**：依十二长生论，五行行至“死、绝”之地，本应气尽，若遇特别配置仍可得救。
  - **递相还**：递，交接；还，归还、回转。指在绝地处，另有同类之气来接续，使本已将绝之气再度归来。
  - **木绝在申，而遇甲申**：申为木气绝地，若日柱成甲申，则木在绝地而得甲木自临，象枯木旁仍接上根源。
  - **金绝在寅，而遇戊寅**：寅为金之绝地，戊寅内藏丙戊甲，虽示金绝，却仍留有土火相生之机，可视为绝中存生。
  - **最吉，有福神次之，无则下**：有还魂借气之象者为最吉；若再兼贵人禄马等福神，则次一等；全无者则格局偏下。

- **规范化释义（primary_lang_explained）**：

  还魂借气格，专讲五行行至“死绝”之地，却因命局中另有同类之气接续，使原本该绝之势得以回生。就像树木行至枯极之境，本应无枝可发，却忽然因根部仍有活水相连，而在枝头再见新芽。

  原文以“木绝在申而遇甲申”“金绝在寅而遇戊寅”为例提示：只要在死绝之位上，仍有与之同气或能相生之干支出现，就可以视为“借气还魂”。若这样的结构恰好又与用神相合，并得到岁运扶持，则往往能在极端困局中屡逢转机；若只是微弱接续，且再受刑冲，则难成上格，只可视作由“全绝”转为“略有根基”。

- 核心要点：

  - 观察十二长生中的“死、绝”之地，是否另有同类或相生之气来承接。
  - 还魂借气是加分条件，关键仍在全局喜忌与用神选取，不可仅凭一处“借气”即言大贵。
  - 借气部位若落在用神之上，并配合有利行运，则“绝处逢生”的力度最强。

- 详细解说：

  在实务中，常见命局表面看似“行到绝地”，例如日主或格局用神落在死绝之支，容易产生“后力不继”的判断。但若细察支中所藏，并参看干支组合与岁运，常会发现仍有暗中接续之气。例如甲申日，申为木绝，却因甲木自临而不至全绝；又如戊寅中含丙戊甲，可为金留生机。

  这类还魂借气的象，往往对应现实中在逆境中反复“跌而复起”的人生轨迹：少年或早年经历重挫，然而凭借隐含资源、人脉或自身某种“底气”，在关键处仍能扭转局面。但若命局其余部分反而多见刑冲、耗泄，则这股借来的气容易被很快消耗，形成数次反复之后终归平常的结果。

- **校勘与字词辨析（双语）**：

  - 原文只举“木绝在申、金绝在寅”两例，本稿保持示例的开放性，不额外列举，以免与他本异文混杂。
  - “最吉，有福神次之，无则下”一句，本稿理解为对格局层次的相对评估，而非生硬三等分级，实占仍需兼看全局强弱。
  - “还魂”“借气”两词，本稿统一处理为对气势衰极复生的形象比喻，不作玄秘灵异解释。
  - **English**：
    - Metaphorical interpretation; avoids mystical or supernatural explanations.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_229]` `[trigger: 还魂借气]` `[factor_trigger: huanhun_jieqi AND sijue_youjiu]` `[role: 主干]` 五行自死绝而有救，递相还者。 → 《三命通会》卷六#还魂借气
  - `[ns_smth_06_230]` `[trigger: 木绝申甲申]` `[factor_trigger: mu_jue_shen AND jiashen_yu]` `[role: 主干依赖]` 如木绝在申，而遇甲申。 → 《三命通会》卷六#还魂借气
  - `[ns_smth_06_231]` `[trigger: 最吉有福]` `[factor_trigger: zuiji_youshen AND cizhixia]` `[role: 条件分支]` 最吉，有福神次之，无则下。 → 《三命通会》卷六#还魂借气
  - `[ns_smth_06_232]` `[trigger: 绝处逢生]` `[factor_trigger: juechu_fengsheng AND huisheng]` `[role: 总结]` 象枯木旁仍接上根源。 → 《三命通会》卷六#还魂借气"""
    normalized_text_zh: str = """"""
    subject: str = "还魂借气与死绝回生"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_51', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_degree_41', 'bazi_semantic', 'bazi_state_factor_38', 'bazi_semantic', 'bazi_condition_factor_220', 'bazi_semantic', 'bazi_condition_factor_221', 'bazi_semantic', 'source_ref', 'rel_smth_06_199', 'huanhunjieqi_presence', 'rel_smth_06_200', 'zhishen_shenghua', 'rel_smth_06_201', 'xingchong_poduo_risk', 'evi_smth_06_199', 'huanhunjieqi_presence', 'rule_huanhun', 'evi_smth_06_200', 'zhishen_shenghua', 'rule_caiguanyinshi', 'evi_smth_06_201', 'xingchong_poduo_risk', 'rule_xingchong', 'map_smth_06_133', 'map_smth_06_134']
    
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
        l1_anchor="smth_v1.0.0_还魂借气与死绝回生_001_L1",
    )
    version: str = "1.0.0"
