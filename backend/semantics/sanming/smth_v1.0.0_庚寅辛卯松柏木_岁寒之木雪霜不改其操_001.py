"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228527
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
    semantic_id="smth_v1.0.0_庚寅辛卯松柏木_岁寒之木雪霜不改其操_001",
    book_id="sanming",
    engine_id="bazi"
)
class 庚寅辛卯松柏木岁寒之木雪霜不改其操(SemanticEntry):
    """
    - **原文（source_text）**：
  烛神经云：庚寅、辛卯岁寒之木，雪霜无以改其操，况金能克之乎？上有庚辛，不假制治，自然成材。阎东叟云：辛卯木自旺，春夏则气节挺拔，建功立事；生于秋，则狂...
    """
    
    original_text: str = """- **原文（source_text）**：
  烛神经云：庚寅、辛卯岁寒之木，雪霜无以改其操，况金能克之乎？上有庚辛，不假制治，自然成材。阎东叟云：辛卯木自旺，春夏则气节挺拔，建功立事；生于秋，则狂狷折挫，劲气不伸。

- **分字分词释义**：
  - **岁寒之木**：寒冬的木，喻松柏。
  - **雪霜无以改其操**：雪霜不能改变其节操。
  - **不假制治**：不需要人工制作。
  - **自然成材**：自然成为栋梁之材。
  - **气节挺拔**：气节高尚挺拔。
  - **狂狷折挫**：狂放拘谨受挫折。
  - **劲气不伸**：刚劲之气不能伸展。

- **规范化释义（primary_lang_explained）**：
  烛神经说：庚寅、辛卯是岁寒的木（松柏木），雪霜不能改变其节操，何况金能克制它呢？天干上有庚辛金，不需要人工制作，自然成材。阎东叟说：辛卯木自身旺盛，如果生在春夏，气节挺拔，能建功立业；如果生在秋季，则狂放拘谨受挫折，刚劲之气不能伸展。

- **完整对等诠释（secondary_lang_full）**：
  Candle-Spirit Classic says: Gengyin and Xinmao are year-cold wood (Pine-Cypress Wood), snow-frost cannot change their integrity, how could Metal overcome them? Above having Geng-Xin, not needing artificial treatment, naturally become timber. Yan Dongsou says: Xinmao Wood self-prosperous, if born spring-summer, character-integrity upright, establishes achievements; if born autumn, then wild-restrained frustrated, vigorous energy cannot extend.

- **核心要点**：
  - 庚寅辛卯为松柏木，岁寒之木
  - 雪霜不改其操，金不能克
  - 上有庚辛不假制治，自然成材
  - 辛卯春夏气节挺拔，秋生则受挫

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_226]` `[trigger: 庚寅辛卯木性质]` `[factor_trigger: gengyin_xinmao_year_cold_wood AND snow_frost_unchanged_integrity AND spring_summer_upright]` `[role: 主干]` 烛神经云：庚寅、辛卯岁寒之木，雪霜无以改其操，况金能克之乎？上有庚辛，不假制治，自然成材。阎东叟云：辛卯木自旺，春夏则气节挺拔，建功立事；生于秋，则狂狷折挫，劲气不伸。 → 《三命通会》卷一#庚寅辛卯木性质

- **详细解说**：
  此条论述庚寅、辛卯（松柏木）的性质。松柏木是岁寒之木，象征坚贞不屈，雪霜不能改变其节操，金也难以克制（因为木性刚强）。天干有庚辛金反而不需要人工制作，自然成材（金木相济）。特别指出辛卯木自旺，春夏生则气节挺拔能成事，秋生则受金克而气不能伸。这是论述木的季节与格局关系。

- **校勘与字词辨析（双语）**：
  - **中文**："岁寒"指严冬，典出《论语》"岁寒然后知松柏之后凋也"。"不假"指不需要。"狂狷"指狂放与拘谨两种极端。
  - **English**: "Year-cold" refers to severe winter, from Analects "only in year-cold know pine-cypress wither last". "Not needing" means no need for. "Wild-restrained" refers to two extremes of unrestrained and inhibited."""
    normalized_text_zh: str = """"""
    subject: str = "庚寅辛卯松柏木：岁寒之木雪霜不改其操"
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
        l1_anchor="smth_v1.0.0_庚寅辛卯松柏木_岁寒之木雪霜不改其操_001_L1",
    )
    version: str = "1.0.0"
