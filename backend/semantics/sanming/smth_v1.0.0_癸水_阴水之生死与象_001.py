"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042393
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
    semantic_id="smth_v1.0.0_癸水_阴水之生死与象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 癸水阴水之生死与象(SemanticEntry):
    """
    - **原文（source_text）**：
  癸水继壬之后，乃天干一周阴阳之气，成于终而反于始之渐，故其为水清浊以分，散诸四方，有润下助土之功，滋生万物之德；在天为雨露，在地为泉脉，谓之阴水。其禄...
    """
    
    original_text: str = """- **原文（source_text）**：
  癸水继壬之后，乃天干一周阴阳之气，成于终而反于始之渐，故其为水清浊以分，散诸四方，有润下助土之功，滋生万物之德；在天为雨露，在地为泉脉，谓之阴水。其禄在子，子乃阴极阳生之地，辛生庚死之垣。癸为活水，活水者，柔水也，喜阴金而生，畏阳金而滞，欲阴木行其根，则能疏通阴土；阴土既通于地脉，则能流畅。二月建卯，为花果树木，木旺土屋，癸水方得通达。至于申地，三阴用事，否卦司权，天地不交，万物不通，申中坤土、庚金遂成围堰，使癸水不能流畅，困于池沼，无所施设，岂再生物？故癸水生于卯而死于申。经云：「水不西流」，正谓此也。

- **分字分词释义**：
  - **阴水 / 活水**：较壬水为柔，重在润物、潜滋暗长。
  - **润下助土**：既滋养土气，又借土以导其流向。
  - **围堰困水**：土金成堰，使水不得通行。

- **规范化释义（primary_lang_explained）**：
  癸水是雨露与泉脉之水，擅长细润万物，兼具清浊分判的功能。它喜阴金为源，喜阴木疏土，使水路通达；在卯木旺地，根系穿透土壤，泉脉得以贯通。若至申位，坤土与庚金成堤，反把活水围困在池沼之中，只能停滞不前，失去「润物无声」的作用。

- **完整对等诠释（secondary_lang_full）**：
  Gui Water follows Ren Water, being heavenly stems' one-cycle yin-yang qi, accomplished at ending returning to beginning gradually; thus its water clarity-turbidity divides, scattering to four directions, having moisten-descend assist-earth merit and nourish-generate myriad-things virtue; in heaven as rain-dew, on earth as spring-veins, embodying yin water. Its official position reaches Zi being yin-extreme yang-born place, Xin-born Geng-dies rampart. Gui as living water being soft water delights in yin metal for birth, fears yang metal stagnation, desires yin wood moving roots then can unblock yin earth; yin earth already penetrated to earth veins then can flow smoothly. Second month builds Mao as flowers-fruits-trees, wood prosperous earth house, Gui Water just obtains penetration. Reaching Shen position three-yin govern, Obstruction hexagram rules, heaven-earth not communicate, myriad things not penetrate—Shen's Kun earth Geng metal become surrounding embankment making Gui Water cannot flow smoothly, trapped in pond-swamp, nowhere to implement—how could again generate things? Thus Gui Water born in Mao dies in Shen. The classic "water not westward flow" refers precisely to this."""
    normalized_text_zh: str = """"""
    subject: str = "癸水：阴水之生死与象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tiangan_gui_presence', 'bazi_calculator', 'dizhi_mao_zi_shen_set', 'bazi_calculator', 'shui_role_profile', 'bazi_semantic', 'shui_outer_vs_inner_axis', 'bazi_semantic', 'water_wood_earth_balance', 'bazi_calculator', 'season_alignment_score', 'bazi_calculator', 'ren_gui_winter_window', 'bazi_calculator', 'embankment_traps_water_risk', 'bazi_rule_engine', 'source_ref', 'rel_smth_02_042', 'tiangan_gui_presence', 'rel_smth_02_043', 'tiangan_yi_presence', 'rel_smth_02_044', 'embankment_traps_water_risk', 'evi_smth_02_038', 'tiangan_yi_presence', 'rule_yi_unblock_gui', 'evi_smth_02_039', 'embankment_traps_water_risk', 'rule_gui_shen_trap', 'evi_smth_02_040', 'dizhi_mao_zi_shen_set', 'rule_gui_avoid_west', 'map_smth_02_029', 'map_smth_02_030']
    
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
        l1_anchor="smth_v1.0.0_癸水_阴水之生死与象_001_L1",
    )
    version: str = "1.0.0"
