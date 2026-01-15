"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042420
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
    semantic_id="smth_v1.0.0_子水_十二支之魁_001",
    book_id="sanming",
    engine_id="bazi"
)
class 子水十二支之魁(SemanticEntry):
    """
    - **原文（source_text）**：
  子十二支之魁，溪涧江洋之水，乃戊土旺地，然必过大雪之期，一阳来复之后，方能成旺。辛金所生，亦必于阳回水暖而后能生也。与午相冲，与卯相刑，与申辰三合。若...
    """
    
    original_text: str = """- **原文（source_text）**：
  子十二支之魁，溪涧江洋之水，乃戊土旺地，然必过大雪之期，一阳来复之后，方能成旺。辛金所生，亦必于阳回水暖而后能生也。与午相冲，与卯相刑，与申辰三合。若申、子、辰全，会起水局，即成江海，发波涛之声也。

- **分字分词释义**：
  - **十二支之魁**：为地支之首，主一轮子午卯酉之起点。
  - **戊土旺地**：子中藏癸水而地属北方，仍赖戊土为堤岸之根基。
  - **大雪、一阳来复**：指节气转折点，阳气初动，子水始真旺。

- **规范化释义（primary_lang_explained）**：
  子为北方之水，是十二支之首，如溪涧江洋之水聚于一处，但要到大雪之后，一阳来复，才是真正的旺水之时。子中虽主癸水，却须戊土为堤，辛金为源，待阳回水暖方能生化。与午相冲，与卯相刑，与申辰三合，申子辰全则成大水局，如江海翻腾。

- **完整对等诠释（secondary_lang_full）**：
  Zi represents Northern Water and serves as the leader of the Twelve Earthly Branches, embodying streams, rivers, and vast ocean waters gathered at a single point. Though Zi contains Gui Water and belongs to the Northern direction, it fundamentally relies on Wu Earth as embankment foundation. However, true water prosperity only manifests after the Great Snow solar term when "the return of one Yang" initiates. Water generated from Xin Metal likewise requires the warmth of returning Yang energy to truly activate generative capacity. Zi clashes with Wu, punishes Mao, and forms triple harmony with Shen and Chen. When Shen-Zi-Chen all appear together, they establish a complete Water Bureau, manifesting as surging oceans generating the sound of crashing waves. This configuration represents concentrated fluidity and information flow, requiring proper containment through Earth embankments to channel productive movement rather than chaotic overflow."""
    normalized_text_zh: str = """"""
    subject: str = "子水：十二支之魁"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_zi_presence', 'bazi_calculator', 'shen_zi_chen_combo', 'bazi_calculator', 'seasonal_phase', 'winter', 'water_earth_metal_balance', 'bazi_calculator', 'yinyang_balance_score', 'bazi_calculator', 'ren_gui_winter_window', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator', 'source_ref', 'rel_smth_02_045', 'dizhi_zi_presence', 'rel_smth_02_046', 'dizhi_zi_presence', 'rel_smth_02_047', 'tiangan_wu_presence', 'evi_smth_02_041', 'shen_zi_chen_combo', 'rule_shen_zi_chen_water', 'evi_smth_02_042', 'dizhi_wu_presence', 'rule_zi_wu_clash', 'evi_smth_02_043', 'seasonal_phase', 'rule_zi_winter_peak', 'map_smth_02_031', 'map_smth_02_032']
    
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
        l1_anchor="smth_v1.0.0_子水_十二支之魁_001_L1",
    )
    version: str = "1.0.0"
