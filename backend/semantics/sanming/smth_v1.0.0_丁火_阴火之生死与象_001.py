"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042303
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
    semantic_id="smth_v1.0.0_丁火_阴火之生死与象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丁火阴火之生死与象(SemanticEntry):
    """
    - **原文（source_text）**：
  丁火继丙之后，为万物之精，文明之象；在天为列星，在地为灯火，谓之阴火。其禄到午，乃六阴之首，内有乙木，能生丁火。乙为活木，丁为活火。活火者，柔火也，丁...
    """
    
    original_text: str = """- **原文（source_text）**：
  丁火继丙之后，为万物之精，文明之象；在天为列星，在地为灯火，谓之阴火。其禄到午，乃六阴之首，内有乙木，能生丁火。乙为活木，丁为活火。活火者，柔火也，丁喜乙木而生，乃阴生阴也，如世人用菜油麻油为灯烛之义，夫油乃乙木之膏也。至于酉时，四阴司权，灯火则能辉煌，列星则能灿烂，故丁生于酉；至于寅地，三阳当合，阳火而生，阴火而退，如日东升，列星隐耀，灯虽有焰，不显其光，故丁生于酉而死于寅也。经云：「火明则灭」，正此谓也。

- **分字分词释义**：
  - **阴火 / 活火**：多象星光、灯烛之火，柔和而细腻，偏向内在文明与精神之光。
  - **禄在午、生于酉、死于寅**：午为灯火用事之地，酉为星火显耀之时，寅则为阳火主事、阴火退藏之处。
  - **乙木之膏**：以油脂喻乙木所化之精华，用以点燃丁火。

- **规范化释义（primary_lang_explained）**：
  丁火不似丙火那样烈烈当空，而偏向星光、灯烛之类的阴火，主文明、文采与心性的照亮。它需要乙木这种细致、柔和的「油脂」来供养，所以最怕根基枯槁。丁火得午地为禄，光明稳定；在酉位生时星光灿烂；到了寅位，阳火当权，阴火反而不显，好比天亮之后星光自动隐去。

- **完整对等诠释（secondary_lang_full）**：
  Ding Fire follows Bing Fire, representing the essence of all things and symbol of civilization: in heaven as scattered stars, on earth as lamp fire, embodying yin fire. Its official position reaches Wu, the first of six yin, containing Yi Wood that generates Ding Fire. Yi as living wood, Ding as living fire—living fire being gentle fire. Ding delights in Yi Wood for birth (yin generates yin), like people using vegetable or sesame oil for lamps and candles—oil being Yi Wood's essence. By You hour when four yin govern, lamp fire shines brilliantly and stars glitter splendidly, thus Ding is born in You; reaching Yin position when three yang converge, yang fire rises and yin fire retreats, like the sun rising east making stars hide their radiance and lamps losing visibility despite having flames—thus Ding dies in Yin. The classic "fire bright then extinguished" refers precisely to this."""
    normalized_text_zh: str = """"""
    subject: str = "丁火：阴火之生死与象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tiangan_ding_presence', 'bazi_calculator', 'dizhi_you_wu_yin_set', 'bazi_calculator', 'huo_expression_profile', 'bazi_semantic', 'huo_visibility_vs_warmth', 'bazi_semantic', 'fire_earth_wood_balance', 'bazi_calculator', 'ding_transparency_level', 'bazi_calculator', 'bing_ding_yun_flag', 'bazi_calculator', 'fire_bright_then_dims_risk', 'bazi_rule_engine', 'source_ref', 'rel_smth_02_024', 'tiangan_ding_presence', 'rel_smth_02_025', 'tiangan_yi_presence', 'rel_smth_02_026', 'tiangan_bing_presence', 'evi_smth_02_020', 'tiangan_yi_presence', 'rule_yi_fuel_ding', 'evi_smth_02_021', 'fire_bright_then_dims_risk', 'rule_ding_hide_under_bing', 'evi_smth_02_022', 'dizhi_you_wu_yin_set', 'rule_ding_you_shine', 'map_smth_02_017', 'map_smth_02_018']
    
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
        l1_anchor="smth_v1.0.0_丁火_阴火之生死与象_001_L1",
    )
    version: str = "1.0.0"
