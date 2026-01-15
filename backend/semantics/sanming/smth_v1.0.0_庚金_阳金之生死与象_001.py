"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042339
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
    semantic_id="smth_v1.0.0_庚金_阳金之生死与象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 庚金阳金之生死与象(SemanticEntry):
    """
    - **原文（source_text）**：
  庚金掌天地肃杀之权，主人间兵革之变；在天为风霜，在地为金铁，谓之阳金。其禄到申，申乃刚金，喜戊土而生，畏癸水而溺。长生于巳，巳中戊土能生庚金，乃阳生阳...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚金掌天地肃杀之权，主人间兵革之变；在天为风霜，在地为金铁，谓之阳金。其禄到申，申乃刚金，喜戊土而生，畏癸水而溺。长生于巳，巳中戊土能生庚金，乃阳生阳也。巳为炉冶之火，锻炼庚金，遂成钟鼎之器，叩之有声；若遇水土沉埋，则无声也，所谓「金实无声」。至于子地，水旺之乡，金寒水冷，子旺母衰，亦遭沉溺之患，岂能复生？故庚金生于巳而死于子。经云：「金沉水底」，正此谓也。

- **分字分词释义**：
  - **阳金 / 刚金**：多象刀兵、器械之金，重在刚猛、决断。
  - **金实无声**：好金在沉埋之中不发声，比喻潜藏不露或才智被压抑。
  - **生于巳、禄在申、死于子**：先经火炼而成器，于申当权，用事至子则为水寒所没。

- **规范化释义（primary_lang_explained）**：
  庚金代表军旅之金、决断之气，在火炉中锻炼成器后方能发挥作用。得巳火、戊土之炼与生，方有「钟鼎之材」；在申为禄时，权柄在手；若落入子水旺地，则金寒水冷、沉在水底，有志难伸，甚至被情势所没。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal commands heaven-earth's authority of purging and killing, governs human realm's military revolution; in heaven as wind-frost, on earth as metal-iron, embodying yang metal. Its official position reaches Shen being hard metal, delighting in Wu Earth for birth, fearing Gui Water drowning. Born in Si where Wu Earth generates Geng Metal being yang-generates-yang. Si as furnace fire forges Geng Metal into bell-vessel tools, striking produces sound; if water-earth buries it becomes soundless, so-called "solid metal silent". Reaching Zi position water-prosperous land, metal cold water freezing, child prosperous mother weak, also suffers drowning affliction—how could longevity extend? Thus Geng Metal born in Si dies in Zi. The classic "metal sinks water bottom" refers precisely to this."""
    normalized_text_zh: str = """"""
    subject: str = "庚金：阳金之生死与象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tiangan_geng_presence', 'bazi_calculator', 'dizhi_si_shen_zi_set', 'bazi_calculator', 'jin_reform_profile', 'bazi_semantic', 'jin_cut_vs_polish_axis', 'bazi_semantic', 'metal_fire_earth_balance', 'bazi_calculator', 'season_alignment_score', 'bazi_calculator', 'geng_xin_yun_flag', 'bazi_calculator', 'metal_sinks_water_risk', 'bazi_rule_engine', 'source_ref', 'rel_smth_02_033', 'tiangan_geng_presence', 'rel_smth_02_034', 'tiangan_wu_presence', 'rel_smth_02_035', 'metal_sinks_water_risk', 'evi_smth_02_029', 'tiangan_wu_presence', 'rule_wu_generate_geng', 'evi_smth_02_030', 'metal_sinks_water_risk', 'rule_geng_zi_sink', 'evi_smth_02_031', 'jin_reform_profile', 'rule_geng_fire_forge', 'map_smth_02_023', 'map_smth_02_024']
    
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
        l1_anchor="smth_v1.0.0_庚金_阳金之生死与象_001_L1",
    )
    version: str = "1.0.0"
