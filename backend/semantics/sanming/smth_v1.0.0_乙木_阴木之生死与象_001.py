"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042275
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
    semantic_id="smth_v1.0.0_乙木_阴木之生死与象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 乙木阴木之生死与象(SemanticEntry):
    """
    - **原文（source_text）**：
  乙木继甲之后，发育万物，生生不已；在天为风，在地为树，谓之阴木。其禄到卯，卯为树木，根深叶茂，谓之活木。活木者，柔木也，惧阳金斫伐为患，畏秋至木落凋零...
    """
    
    original_text: str = """- **原文（source_text）**：
  乙木继甲之后，发育万物，生生不已；在天为风，在地为树，谓之阴木。其禄到卯，卯为树木，根深叶茂，谓之活木。活木者，柔木也，惧阳金斫伐为患，畏秋至木落凋零，欲润土而培其根，利活水而滋其枝叶。活水者，癸水也，即天之雨露，地之泉源；润土者，己土也，如耕耨之土，成稼穑之功。己禄在午，午乃六阳消尽，一阴复生，故稻花开于午时，乙木生于午地。十月建亥，亥乃纯阴司令，壬禄到亥当权，死水泛滥，土薄根虚，有失培养，故乙木死于亥。经云：「水泛木浮」，正此谓也。

- **分字分词释义**：
  - **阴木 / 活木**：多象枝叶花木、藤萝之类，重在柔顺、生生不息。
  - **润土培根**：需有适量之土承载根系，不致根浮、根弱。
  - **活水与死水**：癸水为雨露、泉源之活水，可滋养枝叶；壬水偏为浩荡之潮流，易致水泛木浮。

- **规范化释义（primary_lang_explained）**：
  乙木承接甲木之后，偏向柔顺、缠绕、生发的形态，在天为风，在地为众木之枝叶。其禄在卯，根深叶茂，最怕金斧斫伐与秋令肃杀，因此必须以湿润之土固根，以活水滋养枝叶：癸水如雨露泉源，己土如精耕细作之田土。乙木借午中一阴复生之机得以舒展；至冬十月亥水司令，壬水势大而泛，若土薄根虚，则枝叶被漂，根本失养，遂成「水泛木浮」，故乙木死于亥。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood follows Jia Wood, emphasizing flexible and continuous growth patterns like branches, leaves, and vines. In heaven it manifests as wind, on earth as numerous trees' foliage. Its official position (Lu) resides in Mao where roots deepen and leaves flourish, most fearing metal axes and autumn's killing frost. Therefore it requires moist earth (Ji Earth) to anchor roots and living water (Gui Water as rain-dew and springs) to nourish branches. Yi Wood borrows Wu's moment of yin resurgence to extend; but by winter's tenth month when Hai water governs and Ren Water floods, if earth is thin and roots weak, branches drift and foundations lose support, becoming "water floods wood floats"—thus Yi Wood dies in Hai."""
    normalized_text_zh: str = """"""
    subject: str = "乙木：阴木之生死与象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tiangan_yi_presence', 'bazi_calculator', 'dizhi_mao_wu_hai_set', 'bazi_calculator', 'mu_vitality_vs_control', 'bazi_semantic', 'wood_water_earth_balance', 'bazi_calculator', 'spring_season_window', 'bazi_calculator', 'mu_quality_loss_flag', 'bazi_semantic', 'water_flood_wood_float_risk', 'bazi_rule_engine', 'gui_water_ji_earth_config', 'bazi_rule_engine', 'source_ref', 'rel_smth_02_018', 'gui_water_ji_earth_config', 'rel_smth_02_019', 'water_flood_wood_float_risk', 'rel_smth_02_020', 'tiangan_yi_presence', 'evi_smth_02_014', 'gui_water_ji_earth_config', 'rule_yi_gui_ji_nourish', 'evi_smth_02_015', 'water_flood_wood_float_risk', 'rule_yi_ren_flood', 'evi_smth_02_016', 'dizhi_mao_wu_hai_set', 'rule_yi_hai_death', 'map_smth_02_013', 'map_smth_02_014']
    
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
        l1_anchor="smth_v1.0.0_乙木_阴木之生死与象_001_L1",
    )
    version: str = "1.0.0"
