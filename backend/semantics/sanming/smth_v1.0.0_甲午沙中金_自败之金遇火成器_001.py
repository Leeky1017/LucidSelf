"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228568
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
    semantic_id="smth_v1.0.0_甲午沙中金_自败之金遇火成器_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲午沙中金自败之金遇火成器(SemanticEntry):
    """
    - **原文（source_text）**：
  甲午自败之金，亦曰强悍之金，遇火生旺，其器乃成。忌丁卯、丁酉、戊子之火，凶。五行要论云：甲午金为进神魁气，具刚明之德，秋冬则吉，春夏或凶，入贵格，建统...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲午自败之金，亦曰强悍之金，遇火生旺，其器乃成。忌丁卯、丁酉、戊子之火，凶。五行要论云：甲午金为进神魁气，具刚明之德，秋冬则吉，春夏或凶，入贵格，建统众之功。非时带煞，则暴戾克忍，寡恩少义。

- **分字分词释义**：
  - **自败之金**：自己败落的金。
  - **强悍之金**：强悍刚烈的金。
  - **遇火生旺**：遇到旺火。
  - **其器乃成**：其器物才能成就。
  - **进神魁气**：进取的魁首之气。
  - **刚明之德**：刚强明达的德性。
  - **统众之功**：统率众人的功业。
  - **暴戾克忍**：暴虐苛刻。
  - **寡恩少义**：少恩薄义。

- **规范化释义（primary_lang_explained）**：
  甲午是自败的金，又叫强悍之金，遇到旺火，其器物才能成就。忌讳丁卯、丁酉、戊子的火，遇之则凶。五行要论说：甲午金为进神魁气，具有刚强明达的德性，秋冬则吉，春夏或凶。如果入贵格，能建立统率众人的功业。如果非时带煞，则暴虐苛刻，少恩薄义。

- **完整对等诠释（secondary_lang_full）**：
  Jiawu is self-defeated metal, also called strong-fierce metal. Encountering Fire born-prosperous, its vessel then forms. Avoids Dingmao, Dingyou, Wuzi Fire—inauspicious. Five Elements Essential Discourse says: Jiawu Metal as advancing-spirit chief-energy, possesses firm-bright virtue. Autumn-winter auspicious, spring-summer perhaps inauspicious. Entering noble pattern establishes commanding-multitude achievement. Wrong-time carrying sha, then violent-oppressive harsh, lacking-kindness scarce-righteousness.

- **核心要点**：
  - 甲午为沙中金，自败之金
  - 又称强悍之金
  - 遇火生旺才成器
  - 忌特定火凶
  - 进神魁气，秋冬吉春夏凶
  - 入贵则统众，非时则暴戾

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_229]` `[trigger: 甲午金性质]` `[factor_trigger: jiawu_strong_fierce_metal AND advancing_spirit_chief AND autumn_winter_auspicious]` `[role: 主干]` 甲午自败之金，亦曰强悍之金，遇火生旺，其器乃成。忌丁卯、丁酉、戊子之火，凶。五行要论云：甲午金为进神魁气，具刚明之德，秋冬则吉，春夏或凶，入贵格，建统众之功。非时带煞，则暴戾克忍，寡恩少义。 → 《三命通会》卷一#甲午金性质

- **详细解说**：
  此条详论甲午（沙中金）的性质与格局。甲午是自败的金（午为金败地），又称强悍之金，需要旺火锻炼才能成器（火炼金），但忌丁卯（炉中火）、丁酉（山下火）、戊子（霹雳火）等特定火。五行要论指出甲午金为进神魁气，刚明有德，秋冬吉（金旺季）、春夏凶（金衰季）。入贵格能统众建功，非时带煞则暴戾寡义。这是论述败金的锻炼与季节格局。

- **校勘与字词辨析（双语）**：
  - **中文**："自败"指午为金败地。"强悍"指性格刚烈。"进神"指进取之神。"魁气"指魁首之气。"统众"指统率众人。
  - **English**: "Self-defeated" means Wu is metal's defeat position. "Strong-fierce" means strong and fierce character. "Advancing-spirit" means progressive spirit. "Chief-energy" means leader's energy. "Commanding-multitude" means leading people."""
    normalized_text_zh: str = """"""
    subject: str = "甲午沙中金：自败之金遇火成器"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_甲午沙中金_自败之金遇火成器_001_L1",
    )
    version: str = "1.0.0"
