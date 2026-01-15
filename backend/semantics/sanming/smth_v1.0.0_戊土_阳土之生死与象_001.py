"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042315
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
    semantic_id="smth_v1.0.0_戊土_阳土之生死与象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊土阳土之生死与象(SemanticEntry):
    """
    - **原文（source_text）**：
  戊土洪濛未判，抱一守中，天地既分，厚载万物，聚于中央，散于四维；在天为雾，在地为山，谓之阳土。其禄在巳，巳为炉冶之火，锻炼成器，叩之有声，其性刚猛，难...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊土洪濛未判，抱一守中，天地既分，厚载万物，聚于中央，散于四维；在天为雾，在地为山，谓之阳土。其禄在巳，巳为炉冶之火，锻炼成器，叩之有声，其性刚猛，难以触犯。喜阳火相生，畏阴金盗气。阳火者，丙火也，丙生于寅，寅属艮，艮为山，山为刚土，即戊土也，赖丙火而生焉。至于酉地，酉属兑，金耗盗戊土之气，乃金盛土虚，母衰子旺，又金击石碎，岂能延寿？故戊土生于寅而死于酉。经云：「土虚则崩」，正此谓也。

- **分字分词释义**：
  - **阳土 / 山岳之土**：主高厚、持重，有承载与屏障之象。
  - **抱一守中**：居中央而统四方，重在中正不偏。
  - **金耗土虚**：金过盛则耗损土气，形成「母衰子旺」。

- **规范化释义（primary_lang_explained）**：
  戊土象大地山岳，为天地之间厚载万物的阳土之体。它得丙火温养，在寅位渐成高山之势，于巳得禄，如岩石坚凝可用。若金气太盛，反来耗土、击碎岩石，使本应稳重的阳土失去承载力，变成「土虚则崩」，难以久持。

- **完整对等诠释（secondary_lang_full）**：
  Wu Earth represents primordial undifferentiated mass, embracing unity and守ing center. After heaven-earth separation, it bears all things thickly, gathering at center and散ing to four corners; in heaven as mist, on earth as mountains, embodying yang earth. Its official position reaches Si where furnace fire forges into器, striking produces sound, its nature fierce and hard to offend. It delights in yang fire mutual generation, fears yin metal stealing qi. Yang fire being Bing Fire born in Yin belonging to Gen (mountain), Gen as mountain as firm earth—Wu Earth itself—relying on Bing Fire for birth. Reaching You position belonging to Dui, metal drains Wu Earth's qi causing metal prosperous earth hollow, mother weak child strong, plus metal striking stone shatters—how can longevity extend? Thus Wu Earth born in Yin dies in You. The classic "earth hollow then collapses" refers precisely to this."""
    normalized_text_zh: str = """"""
    subject: str = "戊土：阳土之生死与象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tiangan_wu_presence', 'bazi_calculator', 'dizhi_yin_si_you_set', 'bazi_calculator', 'tu_platform_profile', 'bazi_semantic', 'tu_expansion_vs_digest', 'bazi_semantic', 'earth_fire_metal_balance', 'bazi_calculator', 'geng_xin_yun_flag', 'bazi_calculator', 'earth_hollow_collapse_risk', 'bazi_rule_engine', 'source_ref', 'rel_smth_02_027', 'tiangan_wu_presence', 'rel_smth_02_028', 'tiangan_bing_presence', 'rel_smth_02_029', 'earth_hollow_collapse_risk', 'evi_smth_02_023', 'tiangan_bing_presence', 'rule_bing_generate_wu', 'evi_smth_02_024', 'earth_hollow_collapse_risk', 'rule_wu_metal_drain', 'evi_smth_02_025', 'earth_fire_metal_balance', 'rule_wu_child_drain_mother', 'map_smth_02_019', 'map_smth_02_020']
    
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
        l1_anchor="smth_v1.0.0_戊土_阳土之生死与象_001_L1",
    )
    version: str = "1.0.0"
