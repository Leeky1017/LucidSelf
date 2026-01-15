"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042431
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
    semantic_id="smth_v1.0.0_丑土_隆冬暖土与金库_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丑土隆冬暖土与金库(SemanticEntry):
    """
    - **原文（source_text）**：
  丑虽隆冬，有冰霜之可怯，但天时已转二阳，是以丑中己土之暖能生万物，辛金养地，岂只深藏？见戌则刑，见未则冲，库地最宜，刑冲不为无用。见巳、酉三合，会起金...
    """
    
    original_text: str = """- **原文（source_text）**：
  丑虽隆冬，有冰霜之可怯，但天时已转二阳，是以丑中己土之暖能生万物，辛金养地，岂只深藏？见戌则刑，见未则冲，库地最宜，刑冲不为无用。见巳、酉三合，会起金局。若人命生于丑月，而日时多见水木，必侧行巽离之地，而土方不衰耳。

- **分字分词释义**：
  - **二阳已转**：虽仍在冬季，但阳气已萌动，并非纯寒之地。
  - **己土之暖**：丑中己土微温，可孕育万物之根，非全然坚冰。
  - **库地最宜**：丑为金水之库，能蓄养辛金与湿土之气。

- **规范化释义（primary_lang_explained）**：
  丑月在隆冬之际，表面冰霜严寒，实则阳气已转为「二阳」，丑中己土带着暖意，可以孕育来春根芽；其中辛金不只是深藏不见，也是养地之金。丑与戌相刑、与未相冲，这类刑冲对库地未必全是坏事，往往是「开库用物」之机；与巳酉三合，则成金局。若人命生于丑月而日时多水木，多主生活与环境偏向东南风火之地，正好避免土气过衰。

- **完整对等诠释（secondary_lang_full）**：
  Chou lies in the depth of winter, where the surface looks icy and forbidding, yet the calendar has already turned so that a second degree of yang has begun to rise. The Ji Earth inside Chou carries this hidden warmth: it can nurse the roots that will sprout in spring, even while the ground appears frozen. The Xin Metal stored there is not merely locked away; it works like ore laid in the fields, strengthening and enriching the soil itself. As a storehouse earth for Metal and Water, Chou often needs刑 and冲 from Xu or Wei: these impacts are less pure damage than the action of a key on a vault, opening the door so that what has been kept can be used. When Chou meets Si and You to form a Metal Bureau, the image is of a cold but well‑built treasury, where resources, skills, and tools are forged and accumulated. For a person born in Chou month whose day and hour are heavy in Water and Wood, life circumstances often tilt toward the windy, fiery south‑east; this helps to prevent the earth quality from becoming stagnant or over‑drained and turns Chou into a winter foundation preparing for the next cycle, rather than a place of dead, unusable frost."""
    normalized_text_zh: str = """"""
    subject: str = "丑土：隆冬暖土与金库"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_chou_presence', 'bazi_calculator', 'si_you_chou_combo', 'bazi_calculator', 'chou_xu_xing_chou_wei_chong', 'bazi_calculator', 'seasonal_phase', 'bazi_calculator', 'earth_metal_water_balance', 'bazi_calculator', 'wu_ji_transition_window', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator', 'source_ref', 'rel_smth_02_048', 'dizhi_chou_presence', 'rel_smth_02_049', 'chou_xu_xing_chou_wei_chong', 'rel_smth_02_050', 'dizhi_chou_presence', 'evi_smth_02_044', 'si_you_chou_combo', 'rule_si_you_chou_metal', 'evi_smth_02_045', 'chou_xu_xing_chou_wei_chong', 'rule_chou_open_treasury', 'evi_smth_02_046', 'seasonal_phase', 'rule_chou_warm_earth', 'map_smth_02_033', 'map_smth_02_034']
    
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
        l1_anchor="smth_v1.0.0_丑土_隆冬暖土与金库_001_L1",
    )
    version: str = "1.0.0"
