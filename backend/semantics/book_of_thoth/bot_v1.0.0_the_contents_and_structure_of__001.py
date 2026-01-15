"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.049438
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
    semantic_id="bot_v1.0.0_the_contents_and_structure_of__001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TheContentsAndStructureOf(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Tarot | 78-card deck | Complete symbolic system |
| Major Arcana | 22 Trumps/Atu | Paths on Tree of Life |
| Minor Arcana | 56 cards (4×14) | Sephiroth + Court Cards |
| Court Cards | Knight/Queen/Prince/Princess | Father/Mother/Son/Daughter |

**Source Text**:
> "THE TAROT is a pack of seventy-eight cards. There are four suits, as in modern playing cards, which are derived from it. But the Court cards number four instead of three. In addition, there are twenty-two cards called 'Trumps', each of which is a symbolic picture with a title itself. At first sight one would suppose this arrangement to be arbitrary, but it is not. It is necessitated, as will appear later, by the structure of the universe, and in particular of the Solar System, as symbolized by the Holy Qabalah."

**English Paraphrase**:

The **Tarot** is a **78-card system** with precise structural logic rooted in **Qabalistic cosmology**:

**Structure**:
- **22 Major Arcana (Atu/Trumps)**: Correspond to the **22 paths** connecting the Sephiroth on the Tree of Life, and to the **22 Hebrew letters**
- **40 Small Cards (Pip Cards)**: 4 suits × 10 numbers, representing the **10 Sephiroth** in **4 elements** (Fire/Water/Air/Earth)
- **16 Court Cards**: 4 suits × 4 figures (Knight/Queen/Prince/Princess), representing **Father/Mother/Son/Daughter** or the **Tetragrammaton** (YHVH)

**Why This Structure?**
The arrangement mirrors the **architecture of the universe** as mapped by Qabalah. The Tree of Life has 10 Sephiroth (spheres) and 22 paths connecting them. The four suits correspond to the four elements and the four letters of the Divine Name (Yod-Heh-Vav-Heh).

**完整中文诠释**：

**塔罗牌**是一套**78张牌的系统**，其结构逻辑根植于**卡巴拉宇宙论**：

**结构**：
- **22张大阿尔卡纳（Atu/王牌）**：对应生命之树上连接Sephiroth的**22条路径**，以及**22个希伯来字母**
- **40张小牌（数字牌）**：4个花色×10个数字，代表**4元素**中的**10个Sephiroth**（火/水/气/土）
- **16张宫廷牌**：4个花色×4个人物（骑士/皇后/王子/公主），代表**父/母/子/女**或**四字神名**（YHVH）

**为何是这种结构？**
排列反映了卡巴拉所映射的**宇宙架构**。生命之树有10个Sephiroth（球体）和22条连接它们的路径。四个花色对应四元素和神圣之名的四个字母（Yod-Heh-Vav-Heh）。

#### Core Points

- The Tarot's **78-card structure** (22 + 40 + 16) is not arbitrary but reflects the **Qabalistic model of the universe**.
- **22 Major Arcana** = 22 Hebrew letters = 22 paths on the Tree of Life.
- **40 Small Cards** = 10 Sephiroth expressed through 4 elemental suits.
- **16 Court Cards** = Tetragrammaton (YHVH) expressed in 4 suits: Father (Knight), Mother (Queen), Son (Prince), Daughter (Princess).
- The entire deck is a **portable map of creation**, encoding the structure of reality itself.

**Narrative Snippets**:
- `[ns_thoth_theory_001]` `[trigger: tarot_structure]` `[factor_trigger: tarot_cosmic_structure AND tarot_path_system]` `[role: 主干]` The Tarot is a pack of seventy-eight cards whose structure mirrors the Qabalistic Tree of Life and the Holy Name. → English Paraphrase
- `[ns_thoth_theory_002]` `[trigger: 22_paths]` `[factor_trigger: paths_22 AND hebrew_linear]` `[role: 主干依赖]` The 22 Major Arcana correspond to the 22 paths connecting the 10 Sephiroth and to the 22 Hebrew letters. → English Paraphrase
- `[ns_thoth_theory_003]` `[trigger: court_structure]` `[factor_trigger: court_cards AND daughter_rise]` `[role: 条件分支]` The 16 Court Cards represent Father/Mother/Son/Daughter or the Tetragrammaton (YHVH). → English Paraphrase
- `[ns_thoth_theory_004]` `[trigger: elements]` `[factor_trigger: four_elements AND four_suits]` `[role: 条件分支]` The four suits correspond to the four elements (Fire/Water/Air/Earth). → English Paraphrase
- `[ns_thoth_theory_005]` `[trigger: yhvh_formula]` `[factor_trigger: yhvh AND mother]` `[role: 条件分支]` The Tetragrammaton YHVH represents Father-Mother-Son-Daughter cycle. → English Paraphrase
- `[ns_thoth_theory_006]` `[trigger: hebrew_mother]` `[factor_trigger: mother_letters AND element_earth]` `[role: 条件分支]` The three Mother letters represent primordial elements in creation. → English Paraphrase
- `[ns_thoth_theory_007]` `[trigger: pagan_view]` `[factor_trigger: pagan_circular AND tarot_reality]` `[role: 条件分支]` The pagan circular view of time contrasts with linear Hebrew cosmology. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "The Contents and Structure of the Tarot"
    factor_refs: list = []
    
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
        l1_anchor="bot_v1.0.0_the_contents_and_structure_of__001_L1",
    )
    version: str = "1.0.0"
