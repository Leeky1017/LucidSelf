"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042327
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
    semantic_id="smth_v1.0.0_己土_阴土之生死与象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 己土阴土之生死与象(SemanticEntry):
    """
    - **原文（source_text）**：
  己土继戊之后，乃天之元气，地之真土。清气上升，冲和天地；浊气下降，聚生万物，谓之阴土。天地人三才皆不可缺此土，如乾坤中一媒妁，阴阳失此，岂能配偶？故于...
    """
    
    original_text: str = """- **原文（source_text）**：
  己土继戊之后，乃天之元气，地之真土。清气上升，冲和天地；浊气下降，聚生万物，谓之阴土。天地人三才皆不可缺此土，如乾坤中一媒妁，阴阳失此，岂能配偶？故于四行无不在，于四时则寄旺焉，乃真土也。喜丁火而生，畏阳火而燥。其禄到午，午中丁火能生己土，被乙木盗其栽培之气。至于酉地，丁火而生，丁火既生，己土亦能生也；至寅用事，木火司权，锻炼己土，遂成磁石，反失中和之气，岂有不损之理？故己土生于酉而死于寅。经云：「火燥土裂」，正此谓也。

- **分字分词释义**：
  - **阴土 / 真土**：多象田园、膏腴之土，重在滋养与调和。
  - **媒妁之土**：比喻其在阴阳之间起撮合与缓冲的作用。
  - **喜丁畏丙**：宜温润之丁火，不宜烈燥之丙火。

- **规范化释义（primary_lang_explained）**：
  己土是可耕可植的田园之土，负责承载、滋养、调和，是天地、人事之间的「媒妁」。它喜丁火温暖而生机流动，怕丙火过烈而干裂；得午地之禄，则田土温暖而可耕。若木火过盛，己土被反覆锻炼成「磁石」，虽有特殊用处，却失去中和之德，难以广泛滋养。

- **完整对等诠释（secondary_lang_full）**：
  Ji Earth follows Wu Earth, being heaven's primordial qi and earth's true soil. Clear qi ascends harmonizing heaven-earth; turbid qi descends gathering to generate myriad things, embodying yin earth. Heaven-earth-human three powers cannot lack this earth, like a matchmaker between Qian-Kun—how could yin-yang mate without it? Thus present in all four elements, seasonally prospering in transitions, being true earth. Delights in Ding Fire for birth, fears yang fire scorching. Its official position reaches Wu where Ding Fire generates Ji Earth, yet Yi Wood steals its nurturing qi. Reaching You position Ding Fire is born, Ji Earth also born; reaching Yin in power when Wood-Fire govern, forging Ji Earth into magnetite, losing harmonious qi—how could damage not occur? Thus Ji Earth born in You dies in Yin. The classic "fire scorches earth cracks" refers precisely to this."""
    normalized_text_zh: str = """"""
    subject: str = "己土：阴土之生死与象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'tiangan_ji_presence', 'bazi_calculator', 'dizhi_wu_you_yin_set', 'bazi_calculator', 'tu_platform_profile', 'bazi_semantic', 'tu_expansion_vs_digest', 'bazi_semantic', 'earth_fire_wood_balance', 'bazi_calculator', 'wu_ji_transition_window', 'bazi_calculator', 'bing_ding_yun_flag', 'bazi_calculator', 'fire_scorches_earth_risk', 'bazi_rule_engine', 'source_ref', 'rel_smth_02_030', 'tiangan_ji_presence', 'rel_smth_02_031', 'tiangan_ding_presence', 'rel_smth_02_032', 'fire_scorches_earth_risk', 'evi_smth_02_026', 'tiangan_ding_presence', 'rule_ding_generate_ji', 'evi_smth_02_027', 'fire_scorches_earth_risk', 'rule_ji_fear_bing', 'evi_smth_02_028', 'tu_platform_profile', 'rule_ji_mediator', 'map_smth_02_021', 'map_smth_02_022']
    
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
        l1_anchor="smth_v1.0.0_己土_阴土之生死与象_001_L1",
    )
    version: str = "1.0.0"
