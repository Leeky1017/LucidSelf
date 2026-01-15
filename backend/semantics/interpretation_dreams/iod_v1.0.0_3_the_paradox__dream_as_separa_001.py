"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460793
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
    semantic_id="iod_v1.0.0_3_the_paradox__dream_as_separa_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 3TheParadoxDreamAsSepara(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Separate | Dream as alien state | One view |
| Continuous | Dream linked to waking | Opposing view |
| Paradox | Both true somehow | Freud's resolution |
| Psychic Life | Unified perspective | Key insight |

The contradiction expressed in these two views as to the relation between dream life and waking life seems indeed insoluble. It will therefore not be out of place to mention the description of F. W. Hildebrandt (1875), who believes that the peculiarities of the dream can generally be described only by calling them a "series of contrasts which apparently shade off into contradictions." "The first of these contrasts is formed on the one hand by the strict isolation or seclusion of the dream from true and actual life, and on the other hand by the continuous encroachment of the one upon the other, and the constant dependency of one upon the other."

**English Paraphrase**:

Two contradictory views dominate the literature on dreams' relationship to waking life. Some authors (Burdach, Strümpell) argue that dreams are completely separate from waking consciousness—we "turn our backs" on reality when dreaming. Others (Haffner, Weygandt, Maury) insist dreams directly continue waking life, drawing material from recent experiences and ongoing concerns. 

Hildebrandt recognized this apparent contradiction cannot be easily resolved. He proposed that dreams are characterized by fundamental paradoxes—they are simultaneously isolated from reality yet continuously connected to it. Dreams seem hermetically sealed from waking life, yet they constantly draw upon and reflect waking experiences.

**Complete Chinese Interpretation (Secondary Language)**:

在这一节中，弗洛伊德总结了梦与清醒生活关系上的一组经典对立：一派（如 Burdach、Strümpell）强调**隔离性**，认为做梦时我们几乎把现实世界抛在身后，进入一个完全不同的领域；另一派（如 Haffner、Weygandt、Maury）则强调**连续性**，认为梦紧密承接白日经验与当前关切，“我们梦见所见、所言、所欲、所为”。

Hildebrandt 的重要贡献在于，他没有简单站队，而是提出：梦的本质恰恰是一种**张力性的悖论状态**——一方面，梦在主观体验上的确像是从现实中抽离出来，许多重大现实事件在梦中反而缺席；另一方面，细致追踪梦的素材，却又几乎总能找到与前一天经验或长期关切的联系。梦既像是封闭的小宇宙，又持续从清醒生活中汲取原料。

弗洛伊德借用这一悖论，为后文的区分埋下伏笔：表面上看去与现实脱节的，是**显梦内容**；真正与现实关切紧密相连的，是隐藏在底层的**潜梦思想**。梦的工作通过凝缩、移置、象征等机制，把这条联系伪装起来，于是我们的主观体验就变成：“这个梦好像跟我现实中的事毫不相干”。隔离与连续并存，其实正是显层与深层之间被扭曲后的关系。

**Core Points**:
- Two contradictory schools: dream as separate vs dream as continuous
- Isolation view: dreams turn away from waking reality entirely
- Continuity view: dreams directly extend waking thoughts and experiences
- Hildebrandt's synthesis: dreams embody fundamental paradox—both isolated and connected
- This contradiction points to dream's complex relationship with consciousness

**Detailed Explanation**:

This section reveals a fundamental tension in dream theory that Freud will eventually resolve through his concept of the unconscious. The debate between "isolation" and "continuity" theorists isn't merely academic—it reflects a genuine phenomenological puzzle.

**The Isolation Position** (Burdach, Strümpell): When we dream, we enter a completely different world. Even when waking life is dominated by intense concerns—grief, important tasks, passionate interests—dreams either ignore these entirely or transform them beyond recognition. Dreams don't replay our day; they transport us elsewhere. The example Hildebrandt provides is vivid: a person who never sold wine, never sailed, harbors no sympathy for Napoleon, and wasn't even alive during Napoleon's exile nonetheless dreams of sailing to St. Helena to bring Napoleon Moselle wine. Nothing in this dream connects to the dreamer's actual life.

**The Continuity Position** (Haffner, Weygandt, Maury): Dreams are filled with residues of recent experiences, ongoing preoccupations, and familiar concerns. "We dream of what we have seen, said, desired, or done" (Maury). Careful examination nearly always reveals "a thread by which the dream has connected itself with the experience of the previous day" (Haffner). Dreams don't transport us away from everyday life; they immerse us more deeply in it.

**Hildebrandt's Paradox**: Both views are correct. Dreams are simultaneously:
1. **Isolated**: Hermetically sealed, freed from reality, operating by completely different rules
2. **Connected**: Drawing all material from reality, reflecting waking concerns, continuous with conscious life

Freud will resolve this paradox by distinguishing between **manifest content** (which appears disconnected) and **latent content** (which is intimately connected to waking concerns). The dream disguises its connection to reality through the dream-work, creating an appearance of isolation while maintaining deep continuity.

The ancient example from Artabanus is significant: "Dream pictures mostly contain that of which one has been thinking while awake." This wisdom predates psychoanalysis but captures a key insight—dreams reflect waking preoccupations, even when the connection is obscured.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Dream Paradox: Separate yet continuous. Manifest content appears isolated, latent content intimately connected. Dream-work disguises the connection. Hildebrandt's synthesis.
- **中文**: 梦的悖论:分离又连续。显梦看似孤立,潜梦紧密相连。梦的工作伪装连接。希尔德布朗特综合。

**Narrative Snippets**:
- `[ns_freud_ch1_007]` `[trigger: dream_paradox]` `[factor_trigger: dream_phenomenology]` `[role: 主干]` Dream paradox: simultaneously isolated from and connected to waking life; "series of contrasts". → Core
- `[ns_freud_ch1_008]` `[trigger: isolation_vs_continuity]` `[factor_trigger: dream_phenomenology AND theoretical_debate]` `[role: 条件分支]` Two schools: isolation (Burdach/Strümpell) vs continuity (Haffner/Maury); Hildebrandt synthesizes. → Position
- `[ns_freud_ch1_009]` `[trigger: manifest_latent_solution]` `[factor_trigger: dream_phenomenology AND dream_work]` `[role: 条件分支]` Resolution: manifest content appears isolated, latent content intimately connected; dream-work disguises. → Resolution"""
    normalized_text_zh: str = """"""
    subject: str = "3 The Paradox: Dream as Separate vs Dream as Continuous"
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_3_the_paradox__dream_as_separa_001_L1",
    )
    version: str = "1.0.0"
