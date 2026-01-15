"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228620
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
    semantic_id="smth_v1.0.0_壬寅癸卯金箔金_虚薄之金仁柔义刚_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬寅癸卯金箔金虚薄之金仁柔义刚(SemanticEntry):
    """
    - **原文（source_text）**：
  壬寅自绝之金，癸卯气散之金，若见众火则丧气，惟水土朝之则吉。五行要论云：壬寅、癸卯为虚薄之金，具仁柔义刚之德，秋冬刚健无凶，凶为吉兆；春夏则内凶外吉，...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬寅自绝之金，癸卯气散之金，若见众火则丧气，惟水土朝之则吉。五行要论云：壬寅、癸卯为虚薄之金，具仁柔义刚之德，秋冬刚健无凶，凶为吉兆；春夏则内凶外吉，吉乃先凶。入贵格则志节英明，带煞则凶暴，不能终也。三命纂局云：癸卯自胎之金，若逢丙寅、丁卯，炉中之火，不为鬼，以胎金炉中成器故也。

- **分字分词释义**：
  - **自绝之金**：自己绝灭的金。
  - **气散之金**：气分散的金。
  - **丧气**：丧失气势。
  - **水土朝之**：水土来朝拜。
  - **虚薄之金**：虚弱单薄的金。
  - **仁柔义刚**：仁爱柔和而道义刚强。
  - **刚健无凶**：刚健有力没有凶险。
  - **志节英明**：志向节操英明。
  - **自胎之金**：自己在胎位的金。

- **规范化释义（primary_lang_explained）**：
  壬寅是自绝的金，癸卯是气散的金，如果见到众多火就丧失气势，只有水土来朝拜才吉利。五行要论说：壬寅、癸卯是虚薄的金，具有仁爱柔和而道义刚强的德性，秋冬刚健有力没有凶险，凶反而是吉兆；春夏则内凶外吉，吉反而先有凶。如果入贵格则志节英明，带煞则凶暴，不能善终。三命纂局说：癸卯是自胎的金，如果遇到丙寅、丁卯炉中火，不为鬼，因为胎金在炉中成器的缘故。

- **完整对等诠释（secondary_lang_full）**：
  Renyin is self-extinct metal, Guimao is energy-dispersed metal. If seeing many Fires then loses vitality, only Water-Earth paying-court then auspicious. Five Elements Essential Discourse says: Renyin, Guimao are insubstantial-thin metal, possessing benevolence-gentle righteousness-firm virtue. Autumn-winter vigorous-healthy without misfortune, misfortune becomes auspicious-omen; spring-summer internally-inauspicious externally-auspicious, auspiciousness preceded-by-inauspiciousness. Entering noble pattern then integrity-principle brilliant-bright, carrying sha then violent-fierce, cannot end-well. Three-Destinies Compiled-Records says: Guimao self-embryo metal, if encountering Bingyin, Dingmao furnace-within fire, not as ghost, since embryo-metal furnace-within forms-vessel therefore.

- **核心要点**：
  - 壬寅癸卯为金箔金，自绝气散
  - 见众火丧气，水土朝吉
  - 虚薄之金、仁柔义刚
  - 秋冬刚健、春夏内凶外吉
  - 入贵志节英明、带煞凶暴
  - 癸卯胎金遇炉火成器不为鬼

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_235]` `[trigger: 壬寅癸卯金性质]` `[factor_trigger: renyin_guimao_insubstantial_metal AND benevolence_gentle_righteousness_firm AND embryo_metal_furnace_forms_vessel]` `[role: 主干]` 壬寅自绝之金，癸卯气散之金，若见众火则丧气，惟水土朝之则吉。五行要论云：壬寅、癸卯为虚薄之金，具仁柔义刚之德，秋冬刚健无凶，凶为吉兆；春夏则内凶外吉，吉乃先凶。入贵格则志节英明，带煞则凶暴，不能终也。三命纂局云：癸卯自胎之金，若逢丙寅、丁卯，炉中之火，不为鬼，以胎金炉中成器故也。 → 《三命通会》卷一#壬寅癸卯金性质

- **详细解说**：
  此条详论壬寅、癸卯（金箔金）的性质。壬寅自绝（寅为金绝地），癸卯气散（卯为金死地），见众火丧气，需水土相助。五行要论强调二金虚薄，仁柔义刚，秋冬刚健无凶、春夏内凶外吉。入贵格志节英明，带煞凶暴不终。三命纂局特别指出癸卯胎金遇炉火不为鬼，因胎金在炉中成器。这是论述虚薄金的特殊性与成器原理。

- **校勘与字词辨析（双语）**：
  - **中文**："自绝"指寅为金绝地。"气散"指金气分散。"仁柔义刚"指外柔内刚。"自胎"指卯为金胎地。"炉中成器"指火炼金成器。
  - **English**: "Self-extinct" means Yin is metal's extinction position. "Energy-dispersed" means metal energy dispersed. "Benevolence-gentle righteousness-firm" means gentle outside firm inside. "Self-embryo" means Mao is metal's embryo position. "Furnace-within forms-vessel" means fire refines metal into vessel."""
    normalized_text_zh: str = """"""
    subject: str = "壬寅癸卯金箔金：虚薄之金仁柔义刚"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_壬寅癸卯金箔金_虚薄之金仁柔义刚_001_L1",
    )
    version: str = "1.0.0"
