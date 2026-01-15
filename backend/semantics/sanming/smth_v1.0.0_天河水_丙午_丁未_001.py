"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227749
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
    semantic_id="smth_v1.0.0_天河水_丙午_丁未_001",
    book_id="sanming",
    engine_id="bazi"
)
class 天河水丙午丁未(SemanticEntry):
    """
    - **原文（source_text）**：
  丙午丁未，气当升降，在高明火位，有水沛然作霖，以济火中之水，惟天上乃有，故曰天河水。

- 分字分词释义：
  - **天河水**：指天上银河与骤雨之...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙午丁未，气当升降，在高明火位，有水沛然作霖，以济火中之水，惟天上乃有，故曰天河水。

- 分字分词释义：
  - **天河水**：指天上银河与骤雨之水，来处高远。
  - **作霖以济火**：在火旺之地降雨，以济旱救炎。

- **规范化释义（primary_lang_explained）**：
  丙午、丁未之水，如高空银河化雨：在火势正盛之时自天而降，既能济旱、亦能解燥。象征来自高处或外界的援助、启发与调剂。

- **完整对等诠释（secondary_lang_full）**：

  Bing Wu and Ding Wei form "Heaven‑River Water". Their water comes from above, like the Milky Way turning into rain: it descends into places where Fire is strongest, bringing moisture to relieve drought and cool excessive heat. This image points to aid, inspiration and adjustment that arrive from high ground or from outside the immediate system—policies, patrons, capital, timely advice, sudden insight. Properly used, such top‑down water moderates excess and rescues what would otherwise burn out; mis‑handled, it can either drown the fire’s useful light or foster dependence on rescue from above. In destiny work, Tianhe Water highlights the role of exceptional external interventions and calls for discernment about when to welcome them and how not to lean on them entirely.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_tianhe_001]` `[trigger: 天河水]` `[factor_trigger: bingwu_dingwei AND tianhe_shui]` `[role: 主干]` 丙午丁未，气当升降，在高明火位，有水油然作霖，以济火中之水，惟天上乃有，故曰天河水。 → 《三命通会》卷一#天河水
  - `[ns_smth_01_tianhe_002]` `[trigger: 高空霖雨]` `[factor_trigger: gaokong_linyu AND ji_huowang]` `[role: 主干依赖]` 在火势正盛之时自天而降，既能济旱、亦能解燥。 → 《三命通会》卷一#天河水
  - `[ns_smth_01_tianhe_003]` `[trigger: 外部输入]` `[factor_trigger: waili_yuanzhu AND jiuji_huaxian]` `[role: 条件分支]` 象征来自高处或外界的援助、启发与调剂。 → 《三命通会》卷一#天河水
  - `[ns_smth_01_tianhe_004]` `[trigger: 济火不灭]` `[factor_trigger: jihuo_bumie AND diaoji_shihen]` `[role: 总结]` 济火而不灭火：理想状态是缓解过热而非彻底冲毁原有结构。 → 《三命通会》卷一#天河水"""
    normalized_text_zh: str = """"""
    subject: str = "天河水（丙午、丁未）"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_天河水_丙午_丁未_001_L1",
    )
    version: str = "1.0.0"
