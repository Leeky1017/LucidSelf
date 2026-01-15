"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042544
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
    semantic_id="smth_v1.0.0_亥水_六阴水乡与和暖之寻_001",
    book_id="sanming",
    engine_id="bazi"
)
class 亥水六阴水乡与和暖之寻(SemanticEntry):
    """
    - **原文（source_text）**：
  亥地六阴，雨雪载途，土至此而不暖，金至此而生寒。其象若五湖之归聚，其用在三合之有心。是故欲识乾坤和暖之处，即从艮、震、巽、离之地而寻之也。

- **...
    """
    
    original_text: str = """- **原文（source_text）**：
  亥地六阴，雨雪载途，土至此而不暖，金至此而生寒。其象若五湖之归聚，其用在三合之有心。是故欲识乾坤和暖之处，即从艮、震、巽、离之地而寻之也。

- **分字分词释义**：
  - **六阴**：亥为十二支之末，阴气极盛。
  - **五湖归聚**：喻亥水广阔会聚，如众水所归。
  - **三合之有心**：指亥卯未三合木局等合局之用意所在。

- **规范化释义（primary_lang_explained）**：
  亥地阴气极盛，如雨雪满途之象，土至此不暖，金至此生寒，整体气候偏冷。如同五湖之水汇聚于一处，水势深广，其真正的用途往往体现在与卯未等支三合成局之时。作者提醒：若要寻找乾坤和暖之处，应向艮、震、巽、离等东方、东南、南方的木火之地去，不可误以亥水之地为暖土。

- **完整对等诠释（secondary_lang_full）**：
  Hai represents the extreme of yin: a landscape of cold rain and snow where earth will not warm and Metal grows chilled. It is likened to the place where the waters of many lakes gather, vast and deep, so that Water qi pools rather than rushes forward. On its own this environment is not a source of comfort but of accumulation and enclosure. The text stresses that the real use of Hai lies in its role within larger formations such as the Hai–Mao–Wei Wood Three‑Harmony Bureau, where the stored cold can be channelled into growth and creativity. Anyone seeking warmth, balance, and renewal should therefore look toward the gen, zhen, xun, and li quadrants—mountain, thunder, gentle wind, and bright fire in the east and south—rather than expecting Hai itself to provide a cosy harbour. Interpreted psychologically, Hai Water points to deep reservoirs of feeling and imagination that require Wood–Fire pathways to be transformed into life, instead of being left as isolated, freezing depths."""
    normalized_text_zh: str = """"""
    subject: str = "亥水：六阴水乡与和暖之寻"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_hai_presence', 'bazi_calculator', 'hai_mao_wei_combo', 'bazi_calculator', 'shen_zi_chen_combo', 'bazi_calculator', 'seasonal_phase', 'winter', 'water_earth_wood_fire_balance', 'bazi_calculator', 'water_role_profile', 'bazi_semantic', 'ren_gui_winter_window', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator', 'source_ref', 'rel_smth_02_078', 'dizhi_hai_presence', 'rel_smth_02_079', 'water_earth_wood_fire_balance', 'rel_smth_02_080', 'water_role_profile', 'evi_smth_02_074', 'hai_mao_wei_combo', 'rule_hai_mao_wei_wood', 'evi_smth_02_075', 'water_earth_wood_fire_balance', 'rule_hai_seek_warmth', 'evi_smth_02_076', 'water_role_profile', 'rule_hai_cold_nature', 'map_smth_02_053', 'map_smth_02_054']
    
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
        l1_anchor="smth_v1.0.0_亥水_六阴水乡与和暖之寻_001_L1",
    )
    version: str = "1.0.0"
