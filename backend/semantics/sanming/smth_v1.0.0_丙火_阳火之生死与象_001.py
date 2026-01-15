"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042289
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
    semantic_id="smth_v1.0.0_丙火_阳火之生死与象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丙火阳火之生死与象(SemanticEntry):
    """
    - **原文（source_text）**：
  丙火丽乎中天，普照六合；在天为日为电，在地为炉为冶，谓之阳火。其禄在巳，巳为炉冶之火，谓之死火。死火者，刚火也，喜死木发生其焰，恶金、土掩其光。死木者...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙火丽乎中天，普照六合；在天为日为电，在地为炉为冶，谓之阳火。其禄在巳，巳为炉冶之火，谓之死火。死火者，刚火也，喜死木发生其焰，恶金、土掩其光。死木者，甲木也，甲禄在寅，寅乃阳木之垣，木盛火生，隐于木石之间，非人用之，不能生发，故五阳皆出乎自然而为先天，五阴皆系乎人事而为后天。丙火生于寅，其理甚明。如太阳之火自东而升，至西而没；且酉属兑，兑为泽，己土生金，金气盛，掩息丙火之光，不能显辉，故丙火生于寅而死于酉。经云：「火无西向」，正此谓也。

- **分字分词释义**：
  - **阳火**：在天为日电，在地为炉冶之火，主光明、显露与造作之功。
  - **长生于寅，禄在巳，死于酉**：寅为东方木，助火之生；巳为炉火旺地；酉为西方金，火势将尽之处。
  - **死木助焰**：甲木成材之后供丙火燃烧，使其焰势旺盛。

- **规范化释义（primary_lang_explained）**：
  丙火象征正午烈日之光，在天为日电，在地为炉冶之火，有照耀与炼成之象。其长生在寅，如太阳自东方升起；禄在巳，如炉火正炽；死于酉，如日入西方、光辉渐歇。丙火需借甲木等「死木」为薪，得以大放光明，但一旦金气太盛、土生金而反掩火光，便转为晦滞，不得显露。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire symbolizes the scorching midday sun, manifesting in heaven as sun and lightning, on earth as furnace and forge fire, embodying illumination and forging power. It finds longevity in Yin like the sun rising from the east; reaches official position in Si like furnace fire blazing; dies in You like the sun setting west and brilliance fading. Bing Fire needs Jia Wood and other "dead wood" as fuel to shine brightly, but once Metal qi becomes too strong and Earth generates Metal to cover fire's light, it turns dim and cannot reveal itself. The classic saying "fire does not go west" refers precisely to this trajectory from eastern rise through midday peak to western decline."""
    normalized_text_zh: str = """"""
    subject: str = "丙火：阳火之生死与象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tiangan_bing_presence', 'bazi_calculator', 'dizhi_yin_si_you_set', 'bazi_calculator', 'huo_expression_profile', 'bazi_semantic', 'huo_visibility_vs_warmth', 'bazi_semantic', 'fire_dominance_score', 'bazi_calculator', 'bing_transparency_level', 'bazi_calculator', 'bing_ding_yun_flag', 'bazi_calculator', 'fire_not_westward_risk', 'bazi_rule_engine', 'source_ref', 'rel_smth_02_021', 'tiangan_bing_presence', 'rel_smth_02_022', 'tiangan_jia_presence', 'rel_smth_02_023', 'fire_not_westward_risk', 'evi_smth_02_017', 'dizhi_yin_si_you_set', 'rule_bing_yin_rise', 'evi_smth_02_018', 'fire_not_westward_risk', 'rule_fire_avoid_west', 'evi_smth_02_019', 'tiangan_jia_presence', 'rule_jia_fuel_bing', 'map_smth_02_015', 'map_smth_02_016']
    
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
        l1_anchor="smth_v1.0.0_丙火_阳火之生死与象_001_L1",
    )
    version: str = "1.0.0"
