"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042443
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
    semantic_id="smth_v1.0.0_寅木_建春阳聚与南奔之戒_001",
    book_id="sanming",
    engine_id="bazi"
)
class 寅木建春阳聚与南奔之戒(SemanticEntry):
    """
    - **原文（source_text）**：
  寅建于春，气聚之阳，有丙火生焉。寅刑巳，巳合申并旺而为贵客；旺于卯，库于未，同类则为一家。至午则火光辉，而有超凡入圣之美。见申则寅受冲，而有破禄伤提之...
    """
    
    original_text: str = """- **原文（source_text）**：
  寅建于春，气聚之阳，有丙火生焉。寅刑巳，巳合申并旺而为贵客；旺于卯，库于未，同类则为一家。至午则火光辉，而有超凡入圣之美。见申则寅受冲，而有破禄伤提之忧。若四柱火多，则又不可入南方火地。经云：「木不南奔」。

- **分字分词释义**：
  - **建于春，气聚之阳**：立春之后阳气初聚，寅为阳木与丙火并生之地。
  - **旺于卯，库于未**：与同类木气相合则气势连成一片。
  - **木不南奔**：木火过盛则有自焚之患，需防南方火地过旺。

- **规范化释义（primary_lang_explained）**：
  寅为建春之支，阳气聚集，其中已含丙火，木火并生。与巳刑、与申合，有时成贵局，有时成冲克，要看整体结构：旺于卯、库于未时，木火同类相聚，易成文采、权柄之象；至午则火光极盛，可显「超凡入圣」的一面。但若再见申冲寅，则有破禄伤月令之忧，四柱火多时再行南方火地，更是「木不南奔」，反致焚身。

- **完整对等诠释（secondary_lang_full）**：
  Yin marks the opening of spring, when yang energy first gathers and Bing Fire is already budding inside the rising Wood. Within this branch, Wood and Fire grow together: under supportive patterns where Mao is strong and Wei stores the surplus, this stream of qi links into a continuous band that easily shows up as learning, talent, and authority, and by the time it reaches Wu the blaze can look almost transcendent. Yet the same structure turns risky when Shen clashes with Yin or when Fire is already too concentrated: then the text warns of damaged stipend and wounded mandate, and invokes the maxim that "wood must not rush south" to describe self‑burning from pushing ever deeper into fire lands. In reading a chart, Yin Wood therefore symbolises the very first phase of upward charge and initiative; whether it matures into lasting achievement or burns out depends on the presence of Metal and Water as moderating forces, and on whether the person knows when to consolidate instead of endlessly accelerating."""
    normalized_text_zh: str = """"""
    subject: str = "寅木：建春阳聚与南奔之戒"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_yin_presence', 'bazi_calculator', 'yin_wu_xu_combo', 'bazi_calculator', 'tiangan_bing_presence', 'bazi_calculator', 'seasonal_phase', 'spring', 'wood_fire_balance', 'bazi_calculator', 'jia_yi_spring_window', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator', 'source_ref', 'rel_smth_02_051', 'dizhi_yin_presence', 'rel_smth_02_052', 'dizhi_yin_presence', 'rel_smth_02_053', 'wood_fire_balance', 'evi_smth_02_047', 'yin_wu_xu_combo', 'rule_yin_wu_xu_fire', 'evi_smth_02_048', 'dizhi_shen_presence', 'rule_yin_shen_clash', 'evi_smth_02_049', 'wood_fire_balance', 'rule_wood_avoid_south', 'map_smth_02_035', 'map_smth_02_036']
    
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
        l1_anchor="smth_v1.0.0_寅木_建春阳聚与南奔之戒_001_L1",
    )
    version: str = "1.0.0"
