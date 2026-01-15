"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.049540
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
    semantic_id="bot_v1.0.0_the_twenty_two_paths_and_the_a_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TheTwentyTwoPathsAndTheA(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| 22 Paths | Lines connecting Sephiroth | Relations between emanations |
| 22 Hebrew Letters | א to ת | Each letter = one path |
| Atu | Egyptian term for Trumps | Major Arcana |
| Three Classes | Mothers, Doubles, Singles | Letter classification |

**Source Text**:
> "It will be noticed that twenty-two lines are employed to complete the structure of the Tree of Life. It will be explained in due course how it is that these correspond to the letters of the Hebrew alphabet."

**English Paraphrase**:

The **22 Major Arcana (Atu)** correspond to the **22 paths** on the Tree of Life and to the **22 Hebrew letters**:

**Three Classes of Letters/Paths**:
1. **Three Mother Letters (א מ ש)**: Aleph, Mem, Shin → Air, Water, Fire → Fool, Hanged Man, Aeon
2. **Seven Double Letters (ב ג ד כ פ ר ת)**: Letters with two sounds → Seven Planets → Magus, Priestess, Empress, Wheel, Tower, Sun, Universe
3. **Twelve Simple Letters**: Remaining letters → Twelve Zodiac Signs → Remaining Atu

**Path Function**:
Each path connects two Sephiroth and represents a **specific type of experience** or **mode of consciousness**. The Atu are **pictorial representations** of these paths—meditation on the image is meditation on the cosmic relationship.

**Initiatory Significance**:
Walking the paths = the **journey of initiation**. Each Atu represents a **grade of understanding** or a **test to be passed**. The entire Major Arcana is a **curriculum of spiritual development**.

**完整中文诠释**：

**22张大阿尔卡纳（Atu）**对应生命之树上的**22条路径**和**22个希伯来字母**：

**三类字母/路径**：
1. **三母字母（א מ ש）**：Aleph、Mem、Shin → 气、水、火 → 愚者、倒吊人、永劫
2. **七重字母（ב ג ד כ פ ר ת）**：有两种发音的字母 → 七大行星 → 魔术师、女祭司、皇后、命运之轮、塔、太阳、宇宙
3. **十二单字母**：剩余字母 → 十二星座 → 剩余Atu

**路径功能**：
每条路径连接两个Sephiroth，代表**特定类型的经验**或**意识模式**。Atu是这些路径的**图像表示**——冥想图像就是冥想宇宙关系。

**启蒙意义**：
行走路径 = **启蒙之旅**。每张Atu代表一个**理解等级**或**需要通过的考验**。整个大阿尔卡纳是**灵性发展的课程**。

#### Core Points

- **22 Atu = 22 Hebrew Letters = 22 Paths** on the Tree of Life.
- Letters divided into **Three Mothers** (elements), **Seven Doubles** (planets), **Twelve Singles** (zodiac).
- Each Atu is a **pictorial meditation** on a specific cosmic relationship (path between Sephiroth).
- The Major Arcana sequence represents an **initiatory curriculum**—grades of understanding.
- The **Fool (0)** is outside the sequence, representing the **soul** that walks all paths.

**Narrative Snippets**:
- `[ns_thoth_theory_009]` `[trigger: 22_atu]` `[factor_trigger: tarot_major AND tarot_qabalah]` `[role: 主干]` The 22 Major Arcana correspond to the 22 Hebrew letters and 22 paths on the Tree of Life. → English Paraphrase
- `[ns_thoth_theory_010]` `[trigger: path_initiation]` `[factor_trigger: tarot_major AND tarot_initiation]` `[role: 主干依赖]` Each Atu represents a grade of understanding or test in the initiatory journey across the Tree. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "The Twenty-Two Paths and the Atu (22条路径与Atu)"
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
        l1_anchor="bot_v1.0.0_the_twenty_two_paths_and_the_a_001_L1",
    )
    version: str = "1.0.0"
