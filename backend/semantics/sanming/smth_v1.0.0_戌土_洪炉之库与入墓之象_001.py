"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042534
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
    semantic_id="smth_v1.0.0_戌土_洪炉之库与入墓之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戌土洪炉之库与入墓之象(SemanticEntry):
    """
    - **原文（source_text）**：
  戌乃洪炉之库，钝铁顽金，赖以炼成。见辰龙则冲出壬水，而雨露生焉；见寅虎则会起丙火，而文章出焉。然火命逢之则为入墓，宁能免于不伤哉？

- **分字分词...
    """
    
    original_text: str = """- **原文（source_text）**：
  戌乃洪炉之库，钝铁顽金，赖以炼成。见辰龙则冲出壬水，而雨露生焉；见寅虎则会起丙火，而文章出焉。然火命逢之则为入墓，宁能免于不伤哉？

- **分字分词释义**：
  - **洪炉之库**：戌为火库，可聚火气以炼金铁。
  - **冲出壬水、会起丙火**：与辰冲可出水，与寅合可起火，各有不同之用。
  - **入墓**：火命遇戌，多为气入墓库之地。

- **规范化释义（primary_lang_explained）**：
  戌象洪炉之库，是钝铁顽金赖以炼成之处。见辰如龙，则冲开库门，壬水得出，如雨露普降；见寅如虎，则与丙火会合，起文章之火光。对火命而言，戌又是入墓之地，火气被收束在库中，难免有损耗受制之象。

- **完整对等诠释（secondary_lang_full）**：
  Xu is portrayed as the storehouse of the great furnace, the chamber in which dull iron and stubborn Metal are held for smelting. When it clashes with Chen, the dragon‑earth, the vault is shaken open so that the hidden Ren Water can emerge as nourishing rain; when it meets Yin, the tiger, it links with Bing Fire and raises a literary, expressive flame. For charts whose main qi is Fire, however, Xu also functions as the tomb: entering this dry earth marks a phase where fiery momentum is boxed in and must accept loss and rest. Whether Xu operates more as a refining kiln, a controlled storage vault, or a stifling grave depends on the presence and quality of these clash‑and‑combination channels and on how much Fire, Metal, and Water the chart can safely circulate. In practice this section reminds us that periods of being “put into the furnace” or “sealed in the warehouse” may either support reorganisation and upgrade or slide into long‑term suffocation, and that we should judge Xu by the available outlets rather than by the word “tomb” alone."""
    normalized_text_zh: str = """"""
    subject: str = "戌土：洪炉之库与入墓之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_xu_presence', 'bazi_calculator', 'chen_xu_chong', 'bazi_calculator', 'yin_wu_xu_combo', 'bazi_calculator', 'seasonal_phase', 'bazi_calculator', 'fire_earth_metal_water_balance', 'bazi_calculator', 'fire_expression_profile', 'bazi_semantic', 'wu_ji_transition_window', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator', 'source_ref', 'rel_smth_02_075', 'dizhi_xu_presence', 'rel_smth_02_076', 'chen_xu_chong', 'rel_smth_02_077', 'fire_expression_profile', 'evi_smth_02_071', 'chen_xu_chong', 'rule_chen_xu_water', 'evi_smth_02_072', 'yin_wu_xu_combo', 'rule_yin_xu_fire', 'evi_smth_02_073', 'fire_expression_profile', 'rule_fire_tomb_xu', 'map_smth_02_051', 'map_smth_02_052']
    
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
        l1_anchor="smth_v1.0.0_戌土_洪炉之库与入墓之象_001_L1",
    )
    version: str = "1.0.0"
