"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228172
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
    semantic_id="smth_v1.0.0_石榴木与平地木_001",
    book_id="sanming",
    engine_id="bazi"
)
class 石榴木与平地木(SemanticEntry):
    """
    - **原文（source_text）**：
  庚申辛酉，五行属金，而纳音属木，以相克取之。盖木性辛者，唯石榴木。申酉气归静肃，物渐成实，米居金地，其味成辛，故曰石榴木。观他木至午而死，惟此木至午而...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚申辛酉，五行属金，而纳音属木，以相克取之。盖木性辛者，唯石榴木。申酉气归静肃，物渐成实，米居金地，其味成辛，故曰石榴木。观他木至午而死，惟此木至午而旺，取其性之偏也。戊戌己亥，气归藏伏，阴阳闭塞，木气归根，伏乎土中，故曰平地木也。

- **分字分词释义**：
  - **以相克取之**：用相克的关系来取象。
  - **木性辛者**：木的性质辛辣的。
  - **石榴木**：石榴树的木。
  - **气归静肃**：气归于安静肃穆。
  - **物渐成实**：植物逐渐成熟结实。
  - **米居金地**：果实处在金旺之地。
  - **其味成辛**：其味道成为辛辣。
  - **取其性之偏**：取其性质的特别。
  - **气归藏伏**：气归于藏伏状态。
  - **阴阳闭塞**：阴阳闭塞不通。
  - **木气归根**：木的气归回根部。
  - **伏乎土中**：伏藏在土中。

- **规范化释义（primary_lang_explained）**：
  庚申辛酉，五行属金，但纳音属木，用相克的关系来取象。因为木的性质辛辣的，只有石榴木。申酉之气归于安静肃穆，植物逐渐成熟结实，果实处在金旺之地，其味道成为辛辣，所以叫石榴木。观察其他木到午位就死，只有这种木到午位反而旺盛，取其性质的特别。戊戌己亥，气归于藏伏状态，阴阳闭塞不通，木的气归回根部，伏藏在土中，所以叫平地木。

- **完整对等诠释（secondary_lang_full）**：
  Gengshen-Xinyou: Five Elements belong to Metal, yet Nayin belongs to Wood, taking their mutual restraint relationship. Because Wood's nature being pungent belongs only to Pomegranate Wood. Shen-You qi returns to quiet solemnity, plants gradually ripening into fruit, seeds dwelling in Metal ground, their flavor becoming pungent, thus called Pomegranate Wood. Observing other Woods die at Wu, only this Wood flourishes at Wu, taking their nature's peculiarity. Wuxu-Jihai: qi returns to concealment, yin-yang sealed and blocked, Wood qi returning to roots, submerged in earth, thus called Level-Ground Wood.

- **核心要点**：
  - 庚申辛酉：石榴木（金地木生，味辛性偏）
  - 戊戌己亥：平地木（气归藏伏，木气归根）
  - 石榴木独特：午而旺，不午而死
  - 平地木为木的归藏完结

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_181]` `[trigger: 石榴木与平地木]` `[factor_trigger: pomegranate_wood AND level_ground_wood AND nayin_wood_peculiar]` `[role: 主干]` 庚申辛酉，五行属金，而纳音属木，以相克取之。木性辛者，唯石榴木。观他木至午而死，惟此木至午而旺，取其性之偏也。戊戌己亥，气归藏伏，木气归根，伏乎土中，故曰平地木也。 → 《三命通会》卷一#石榴木与平地木

- **详细解说**：
  此条完成木纳音的解释。庚申辛酉为"石榴木"：申酉属金，但纳音却是木，这是以相克取象的特例。石榴树的特点是味辛（果实酸甜带辛），在金旺之地（秋季）反而结实累累。其他木到午（火旺）就死，但石榴木到午反而旺盛，取其性质的特殊和顽强。戊戌己亥为"平地木"：戌亥属秋冬之交，木气藏伏归根，潜伏在土中，如平地上伏生的草木，这是木生命周期的完结。六种木纳音：桑柘木（初生）→松柏木（坚韧）→大林木（极盛）→杨柳木（柔弱）→石榴木（特异）→平地木（归藏），完整呈现木的一生。石榴木命格特殊坚韧，平地木命格平和归隐。

- **校勘与字词辨析（双语）**：
  - **中文**："石榴木"以相克取象，申酉属金而纳音属木。石榴果实味辛。"取其性之偏"指其性质特殊。"平地木"指贴地生长的草木，气已归根。
  - **English**: "Pomegranate Wood" takes mutual restraint imagery—Shen-You belong to Metal yet Nayin is Wood. Pomegranate fruit tastes pungent. "Taking nature's peculiarity" means its special characteristics. "Level-Ground Wood" refers to ground-level vegetation, qi already returned to roots."""
    normalized_text_zh: str = """"""
    subject: str = "石榴木与平地木"
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
        l1_anchor="smth_v1.0.0_石榴木与平地木_001_L1",
    )
    version: str = "1.0.0"
