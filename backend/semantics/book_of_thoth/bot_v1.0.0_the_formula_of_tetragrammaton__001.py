"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.049508
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
    semantic_id="bot_v1.0.0_the_formula_of_tetragrammaton__001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TheFormulaOfTetragrammaton(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| YHVH | Yod-Heh-Vav-Heh | Four-letter Divine Name |
| Yod (י) | Hand/Seed/Father | Active creative principle |
| Heh (ה) | Window/Mother | Receptive formative principle |
| Vav (ו) | Nail/Son | Result of union |
| Heh final | Daughter | Material manifestation |

**Source Text**:
> "What was the first mental process? Obliged to describe Nothing, the only way to do so without destroying its integrity was to represent it as the union of a Plus Something with an equivalent Minus Something. One may call these two ideas, the Active and Passive, the Father and Mother. But although the Father and Mother can make a perfect union, thereby returning to Zero, which is a retrogression, they can also go forward into Matter, so that their union produces a Son and a Daughter."

**English Paraphrase**:

The **Tetragrammaton (YHVH)** is the **creative formula** underlying all manifestation:

**The Four Letters**:
- **Yod (י) = Father/Knight/Fire**: The **active principle**, the initial spark, will, seed. Corresponds to **Wands** and the **element Fire**.
- **Heh (ה) = Mother/Queen/Water**: The **receptive principle**, the womb that gives form. Corresponds to **Cups** and the **element Water**.
- **Vav (ו) = Son/Prince/Air**: The **product of union**, thought, mediation between active and receptive. Corresponds to **Swords** and the **element Air**.
- **Heh final (ה) = Daughter/Princess/Earth**: The **material result**, the crystallization, the manifest world. Corresponds to **Disks** and the **element Earth**.

**The Creative Cycle**:
Father + Mother → Son + Daughter
The Daughter contains the seed of the new cycle—she rises to the throne of the Mother, and the cycle repeats. This is the **Wheel of Fortune**, the eternal rotation.

**Why Four Court Cards?**
Unlike playing cards with three court cards (King, Queen, Jack), the Tarot has **four** because the creative formula requires Father, Mother, Son, **and** Daughter. The Daughter is essential—she is the manifest result and the seed of renewal.

**完整中文诠释**：

**四字神名（YHVH）**是所有显化背后的**创造公式**：

**四个字母**：
- **Yod（י）= 父亲/骑士/火**：**主动原则**，最初的火花、意志、种子。对应**权杖**和**火元素**。
- **Heh（ה）= 母亲/皇后/水**：**接受原则**，赋予形式的子宫。对应**圣杯**和**水元素**。
- **Vav（ו）= 儿子/王子/气**：**结合的产物**，思想，主动与接受之间的中介。对应**宝剑**和**气元素**。
- **Heh final（ה）= 女儿/公主/土**：**物质结果**，结晶，显化的世界。对应**钱币**和**土元素**。

**创造循环**：
父亲 + 母亲 → 儿子 + 女儿
女儿包含新循环的种子——她升至母亲的宝座，循环重复。这就是**命运之轮**，永恒的旋转。

**为何有四张宫廷牌？**
与只有三张宫廷牌（国王、皇后、骑士）的扑克牌不同，塔罗有**四张**，因为创造公式需要父亲、母亲、儿子、**以及**女儿。女儿至关重要——她是显化的结果，也是更新的种子。

#### Core Points

- **YHVH (Tetragrammaton)** is the fundamental **creative formula** of the Western esoteric tradition.
- **Four letters = Four elements = Four suits = Four Court Cards**: Yod/Fire/Wands, Heh/Water/Cups, Vav/Air/Swords, Heh-final/Earth/Disks.
- The **Father-Mother-Son-Daughter** formula explains why Tarot has **four** court cards per suit, not three.
- The **Daughter rises to the throne of the Mother** = the cycle repeats endlessly (Wheel).
- This formula is **both linear and circular**: Hebrew (linear creation) + Pagan (eternal wheel).

**Narrative Snippets**:
- `[ns_thoth_theory_005]` `[trigger: tetragrammaton]` `[factor_trigger: tarot_qabalah AND tarot_tetragrammaton]` `[role: 主干]` YHVH is the creative formula: Father (Yod/Fire), Mother (Heh/Water), Son (Vav/Air), Daughter (Heh-final/Earth). → English Paraphrase
- `[ns_thoth_theory_006]` `[trigger: four_court]` `[factor_trigger: tarot_court AND tarot_tetragrammaton]` `[role: 主干依赖]` The Tarot has four court cards because the Tetragrammaton requires Father, Mother, Son, AND Daughter. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "The Formula of Tetragrammaton (四字神名公式)"
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
        l1_anchor="bot_v1.0.0_the_formula_of_tetragrammaton__001_L1",
    )
    version: str = "1.0.0"
