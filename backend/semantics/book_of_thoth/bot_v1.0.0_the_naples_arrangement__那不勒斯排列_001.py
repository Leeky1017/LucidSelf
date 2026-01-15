"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.049491
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
    semantic_id="bot_v1.0.0_the_naples_arrangement__那不勒斯排列_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class TheNaplesArrangement那不勒斯排列(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Ain | Nothing | Absolute Zero |
| Ain Soph | Without Limit | Infinite Space |
| Ain Soph Aur | Limitless Light | Luminiferous medium |
| Kether | Crown, Point | First manifestation |
| Chokmah | Wisdom, Line | Second differentiation |
| Binah | Understanding, Triangle | Third: plane/form |

**Source Text**:
> "The Qabalists expanded this idea of Nothing, and got a second kind of Nothing which they called 'Ain Soph'—'Without Limit'. They then decided that in order to interpret this mere absence of any means of definition, it was necessary to postulate the Ain Soph Aur—'Limitless Light'. ... Thus appears The Point, which has 'neither parts nor magnitude, but only position'. But position does not mean anything at all unless there is something else... One has to describe it. The only way to do this is to have another Point, and that means that one must invent the number Two, making possible The Line. ... In order to discriminate between them at all, there must be a third thing. We must have another point. One must invent The Surface; one must invent The Triangle."

**English Paraphrase**:

The **Naples Arrangement** explains how **Something emerges from Nothing** through logical necessity:

**From Nothing to Something**:
1. **0 (Ain)**: Absolute Nothing—but "Nothing" is already a concept, so it contains potential
2. **00 (Ain Soph)**: "Without Limit"—Space without boundaries
3. **000 (Ain Soph Aur)**: "Limitless Light"—the medium in which manifestation occurs

**Geometric Emergence**:
- **1 (Kether)**: The **Point**—position without dimension (first Sephirah)
- **2 (Chokmah)**: The **Line**—a second point creates relationship/direction (Wisdom)
- **3 (Binah)**: The **Triangle/Plane**—three points create surface, form, Understanding
- **4**: The **Solid**—fourth point creates 3D space, Matter
- **5**: **Motion**—Time, change, events become possible
- **6 (Tiphareth)**: **Self-consciousness**—the Point that knows itself
- **7-8-9**: **Sat-Chit-Ananda** (Being-Thought-Bliss)—qualities of experience
- **10 (Malkuth)**: **Reality**—the manifest world, Earth

**完整中文诠释**：

**那不勒斯排列**解释了**有如何从无中产生**的逻辑必然性：

**从无到有**：
1. **0（Ain）**：绝对的无——但"无"本身已是概念，故包含潜能
2. **00（Ain Soph）**："无限"——无边界的空间
3. **000（Ain Soph Aur）**："无限光"——显化发生的媒介

**几何涌现**：
- **1（Kether）**：**点**——无维度的位置（第一Sephirah）
- **2（Chokmah）**：**线**——第二个点创造关系/方向（智慧）
- **3（Binah）**：**三角形/平面**——三点创造表面、形式、理解
- **4**：**立体**——第四点创造三维空间、物质
- **5**：**运动**——时间、变化、事件成为可能
- **6（Tiphareth）**：**自我意识**——认识自己的点
- **7-8-9**：**Sat-Chit-Ananda**（存在-思想-极乐）——经验的品质
- **10（Malkuth）**：**现实**——显化的世界、大地

#### Core Points

- The **Naples Arrangement** is a **creation narrative** explaining how the universe emerges from Zero through geometric/logical necessity.
- **Three Veils of Negative**: Ain → Ain Soph → Ain Soph Aur = Nothing → Infinite → Light.
- **Point → Line → Plane → Solid** = 1 → 2 → 3 → 4 = Kether → Chokmah → Binah → Matter.
- The **10 Sephiroth** are the minimal set of concepts needed to describe **any experience of reality**.
- The **40 Small Cards** of the Tarot represent these 10 Sephiroth in 4 elemental expressions.

**Narrative Snippets**:
- `[ns_thoth_theory_008]` `[trigger: naples_arrangement]` `[factor_trigger: tarot_naples AND tarot_creation]` `[role: 主干]` The Naples Arrangement explains how Something emerges from Nothing through geometric and logical necessity. → English Paraphrase
- `[ns_thoth_theory_009]` `[trigger: zero_to_ten]` `[factor_trigger: tarot_sephiroth AND tarot_manifestation]` `[role: 主干依赖]` From the Point (1) through Line (2), Triangle (3), Solid (4), Motion (5), to Self-consciousness (6) and Reality (10). → English Paraphrase
- `[ns_thoth_theory_010]` `[trigger: tree_structure]` `[factor_trigger: tree_of_life AND tarot_78]` `[role: 条件分支]` The Tree of Life with 10 Sephiroth and 22 paths forms the complete structural framework. → English Paraphrase
- `[ns_thoth_theory_011]` `[trigger: major_hebrew]` `[factor_trigger: major_arcana AND hebrew_letters]` `[role: 条件分支]` The 22 Major Arcana correspond to the 22 Hebrew letters on the Tree of Life paths. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "The Naples Arrangement (那不勒斯排列)"
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
        l1_anchor="bot_v1.0.0_the_naples_arrangement__那不勒斯排列_001_L1",
    )
    version: str = "1.0.0"
