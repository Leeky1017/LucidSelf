"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228233
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
    semantic_id="smth_v1.0.0_壁上土与城头土_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壁上土与城头土(SemanticEntry):
    """
    - **原文（source_text）**：
  庚子辛丑，何以取象壁上土？气居闭塞，物尚包藏，掩形遮体，内外不交，故曰壁上土。戊寅己卯，气能成物，功以育物，发乎根荄，壮乎萼蕊，乃曰城头土也。

- ...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚子辛丑，何以取象壁上土？气居闭塞，物尚包藏，掩形遮体，内外不交，故曰壁上土。戊寅己卯，气能成物，功以育物，发乎根荄，壮乎萼蕊，乃曰城头土也。

- **分字分词释义**：
  - **壁上土**：墙壁上的土。
  - **气居闭塞**：气处在闭塞状态。
  - **物尚包藏**：物还在包藏中。
  - **掩形遮体**：遮掩形体。
  - **内外不交**：内外不相通。
  - **气能成物**：气能够成就事物。
  - **功以育物**：功用在于养育事物。
  - **发乎根荄**：发生于根部。
  - **壮乎萼蕊**：壮大于花萼花蕊。

- **规范化释义（primary_lang_explained）**：
  庚子辛丑，为什么取象为壁上土？气处在闭塞状态，物还在包藏中，遮掩形体，内外不相通，所以叫壁上土。戊寅己卯，气能够成就事物，功用在于养育事物，发生于根部，壮大于花萼花蕊，就叫城头土。

- **完整对等诠释（secondary_lang_full）**：
  Gengzi-Xinchou, why symbolize Wall-Surface Earth? Qi dwelling in sealed state, objects still concealed, covering form shielding body, interior-exterior not communicating, thus called Wall-Surface Earth. Wuyin-Jimao: qi able to accomplish things, function nurturing things, sprouting from roots, flourishing in calyx and pistils, thus called City-Rampart Earth.

- **核心要点**：
  - 庚子辛丑：壁上土（气居闭塞，内外不交）
  - 戊寅己卯：城头土（气能成物，发乎根荄）
  - 壁上土为土的封闭包藏
  - 城头土为土的育物养生

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_188]` `[trigger: 壁上土与城头土]` `[factor_trigger: wall_surface_earth AND city_rampart_earth AND nayin_earth_initial]` `[role: 主干]` 庚子辛丑，何以取象壁上土？气居闭塞，物尚包藏，掩形遮体，内外不交，故曰壁上土。戊寅己卯，气能成物，功以育物，发乎根荄，壮乎萼蕊，乃曰城头土也。 → 《三命通会》卷一#壁上土与城头土

- **详细解说**：
  此条开始解释土纳音。庚子辛丑为"壁上土"：子丑属冬季，土气闭塞，如墙壁上的土，遮掩形体，内外不通，这是土的封闭状态，如粉刷墙壁的土。戊寅己卯为"城头土"：寅卯属春季木旺，土能成物育物（土生万物），从根部发生到花蕊壮大，如城墙之土，高大稳固，有养育防护之功。从壁上土（封闭）到城头土（育物），体现了土从静止到生发的转变。命理上，壁上土命格内敛封闭，城头土命格稳固有力。

- **校勘与字词辨析（双语）**：
  - **中文**："壁上土"指墙壁表面的土（粉刷用土）。"气居闭塞"指冬季土气闭塞。"城头土"指城墙之土，高大稳固。"根荄"，荄指草根。"萼蕊"指花萼和花蕊。
  - **English**: "Wall-Surface Earth" refers to earth on wall surfaces (plastering earth). "Qi in sealed state" means earth qi sealed in winter. "City-Rampart Earth" refers to city wall earth, tall and stable. "Gen-gai" means plant roots. "E-rui" means calyx and pistils."""
    normalized_text_zh: str = """"""
    subject: str = "壁上土与城头土"
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
        l1_anchor="smth_v1.0.0_壁上土与城头土_001_L1",
    )
    version: str = "1.0.0"
