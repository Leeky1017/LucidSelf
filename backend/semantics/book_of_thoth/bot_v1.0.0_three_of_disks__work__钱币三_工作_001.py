"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.063389
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
    semantic_id="bot_v1.0.0_three_of_disks__work__钱币三_工作_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class ThreeOfDisksWork钱币三工作(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Binah in Earth | Form in Earth | Material establishment |
| Mars in Capricorn | Exalted Mars | Constructive energy |
| Pyramid from Above | Top-down view | Foundation structure |
| Three Wheels | Alchemical triad | Mercury/Sulphur/Salt |

**Title**: Lord of Material Works (物质建造之主)
**Qabalistic**: Binah in Earth (土中之理解)
**Astrological**: Mars in Capricorn (火星入摩羯座)

**Source Text**:
> "The influence of Binah in the sphere of Earth shows the material establishment of the idea of the Universe, the determination of its basic form. It is ruled by Mars in Capricornus; he is exalted in that Sign, and therefore at his best. His energy is constructive, like that of the builder or engineer. The card represents a pyramid viewed from above the apex. The base is formed by three wheels—Mercury, Sulphur, and Salt; Sattvas, Rajas, and Tamas in the Hindu system; Aleph, Shin, and Mem—Air, Fire, and Water—the three Mother letters of the Hebrew alphabet. This pyramid is situated in the great Sea of Binah in the Night of Time, but the sea is solidified..."

**English Paraphrase**:
**Building the Foundation** – Corresponds to Binah (Understanding/Form) in Earth: the **material establishment** of the Universe's basic structure. Ruled by **Mars in Capricorn**, where Mars is exalted and at his best: disciplined, constructive energy like that of a builder or engineer. The image shows a **pyramid viewed from above**, its base formed by three wheels representing **Mercury/Sulphur/Salt** (alchemical principles), **Sattva/Rajas/Tamas** (Hindu gunas), and **Aleph/Shin/Mem** (Hebrew Mother letters: Air/Fire/Water). The pyramid rests in the solidified Sea of Binah, showing form emerging from the primordial matrix. This is **Work**: skilled labor, planning, construction, and the disciplined application of knowledge to matter.

**Core**: **Skilled Construction** – Craftsmanship, engineering, building, disciplined effort, bringing plans into reality.

**Chinese Explanation**:
**钱币三（工作）**对应土元素中的**Binah（理解/大母）**，代表宇宙之观念的**物质确立**与基本形式的决定。统治星为**火星入摩羯座**，这是火星**入旺**（exalted）的位置，能量处于最佳状态：不是破坏性的，而是**建设性的**，像工程师或建筑师那样有计划、有纪律地塑造物质。牌面呈现一座**从顶端俯视的金字塔**，塔基由三个轮子组成，分别代表**水银/硫磺/盐**（炼金三元素）、**悦性/变性/惰性**（印度三德）、以及**Aleph/Shin/Mem**（希伯来三母字母：气/火/水）。金字塔坐落在已凝固的 Binah 之海中，象征**从无形到有形的落实**。这张牌强调通过技能、规划与努力来建造实体成果。

**In Readings**: Work, construction, skilled labor, craftsmanship, building foundations, teamwork, engineering, bringing designs into reality.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Three of Disks shows Binah establishing material form. Mars in Capricorn exalted - constructive like builder. Pyramid from above with three wheels base (Mercury/Sulphur/Salt). Sea of Binah solidified.
- **中文**: Crowley的钱币三展示Binah确立物质形式。火星入摩羯入旺—建设性如建筑师。俭视金字塔底座三轮（水银/硫磺/盐）。Binah之海凝固。

**Narrative Snippets**:
- `[ns_thoth_disks_007]` `[trigger: three_disks_work]` `[factor_trigger: thoth_disks_three]` `[role: 主干]` Three of Disks = Lord of Material Works—Binah in Earth; Mars in Capricorn exalted; constructive. → Core
- `[ns_thoth_disks_008]` `[trigger: mars_capricorn_exalted]` `[factor_trigger: thoth_disks_three AND planet_mars_capricorn]` `[role: 条件分支]` Mars exalted in Capricorn—energy constructive like builder or engineer; disciplined. → Astrological
- `[ns_thoth_disks_009]` `[trigger: pyramid_three_wheels]` `[factor_trigger: thoth_disks_three AND symbol_pyramid]` `[role: 条件分支]` Pyramid from above; three wheels base (Mercury/Sulphur/Salt); Sea of Binah solidified. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Three of Disks: Work (钱币三：工作)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_disks_three_001', 'tarot_material_construction', 'rel_disks_three_002', 'tarot_stable_foundation', 'l1_anchor', 'confidence', 'evi_disks_three_001', 'evi_disks_three_002', 'tarot_three_wheels', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_disks_three_001', 'tarot_disks_three', 'astro_mars_capricorn']
    
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_three_of_disks__work__钱币三_工作_001_L1",
    )
    version: str = "1.0.0"
