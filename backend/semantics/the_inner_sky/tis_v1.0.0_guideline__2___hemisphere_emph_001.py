"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134482
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
    semantic_id="tis_v1.0.0_guideline__2___hemisphere_emph_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class Guideline2HemisphereEmph(SemanticEntry):
    """
    **Source Text**:
"GUIDELINE NUMBER TWO: Temporarily forget the individual meanings of the planets. S...
    """
    
    original_text: str = """**Source Text**:
"GUIDELINE NUMBER TWO: Temporarily forget the individual meanings of the planets. Simply observe whether a majority of them lie in any one of the four 'hemispheres' of the birthchart.
If you are fuzzy about the meanings of the hemispheres, you might want to go back to chapter 7 for a detailed review. Let’s briefly recapitulate here, to refresh ourselves.
The horizon divides the chart into an upper hemisphere, representing objectivity, and a lower one, representing subjectivity. When a majority of planets lies above the horizon, the focus of the person’s life is in the objective realm: he or she grows through the crafting of a series of events through which the evolving individuality is publicly and visibly expressed. ... A majority of planets below the horizon has the opposite connotation: such a person’s life is focused far more in the subjective realm. ... Just as the upper-hemisphere person must craft events, his lower-hemisphere counterpart must seek realizations. That is where his happiness lies.
The two hemispheres created by the vertical axis of the birthchart—the meridian—establish a different polarity altogether. The east symbolizes freedom and individual choice, while the west represents fate or destiny. ... Hemisphere emphasis describes the shape of the life, not the tones and textures that make up the fabric of the person’s nature. It reveals the rules of the game, not the personality of the player."

**Key Term Analysis**:
- `hemisphere emphasis`: majority of planets in one of the chart halves/quadrants.
- `upper vs lower hemisphere`: objectivity (events) vs subjectivity (inner realizations).
- `east vs west hemisphere`: freedom/choice vs fate/destiny framing of life.
- `shape of life, not personality`: hemisphere patterns describe life-structure, not traits.

**English Paraphrase (Primary Language)**:
Forrest’s second whole-chart guideline tells us to temporarily ignore the meanings of individual planets and simply note where most of them fall in the chart. This **hemisphere emphasis** offers a fast way to see the overall shape of a person’s life.

The horizon divides the chart into an **upper hemisphere** (above the horizon) linked with objectivity and outer events, and a **lower hemisphere** (below the horizon) linked with subjectivity and inner life. When most planets are above the horizon, growth tends to come through public experience and visible engagement with the world—crafting events, careers, and actions. When most planets are below, growth is centered in inner realizations, feeling, and reflection; life may still be busy externally, but the essential work happens inside.

The vertical meridian divides the chart into an **eastern hemisphere** associated with freedom and individual choice, and a **western hemisphere** associated with fate or destiny—the sense that life is shaped largely through encounters and circumstances. Importantly, Forrest insists that hemisphere emphasis describes the **shape of life**, not personality qualities like shyness or charisma. It reveals the "rules of the game"—where growth is likely to be found and how much initiative versus response is structurally emphasized—not the detailed texture of the player.

**Complete Chinese Interpretation (Secondary Language)**:
在第二条整体解读指引中，Forrest 要我们**先暂时忘掉行星各自的含义**，只看一件事：大部分行星集中在哪个半球/象限。这样可以非常快速地勾勒出一个人的**生命轨迹轮廓**。

首先，地平线把命盘分成上下两个半球：上半球对应「客观世界」，下半球对应「主观世界」。若多数行星位于上半球，生命成长往往主要通过外在事件与公共舞台来完成——是透过「打造一连串事件」来表达和塑造自己；若多数行星位于下半球，则人生重点更偏向内在世界——外在可以很热闹，但真正关键的成长都发生在心里、在意识与情绪的层面。

其次，子午线把命盘分成左右两个半球：东方象征「自由与主动选择」，西方象征「命运或遭遇」。东半球偏重「我先动手」的叙事结构，西半球则更像是在回应别人、环境与关系带来的抛球。Forrest 一再强调：**半球重心所描述的是「人生的玩法和棋盘结构」，而不是「这个人外向还是内向、好不好相处」**。它告诉我们的是「游戏规则」——一个人更需要通过什么样的路径来获得成长，而不是描述玩家的细节性格。

**Core Points**:
- Guideline #2: before reading planetary meanings, notice hemisphere emphasis.
- Upper vs lower hemispheres: outer events vs inner realizations as primary growth arenas.
- East vs west hemispheres: initiative/freedom vs encounter/destiny framing.
- Hemisphere patterns define life-shape and game-rules, not detailed personality traits.

**Detailed Explanation**:
Hemisphere emphasis gives a macro-geometry for the chart. It complements the Primal Triad: while the triad tells us who the person is, the hemispheres say **where and how life tends to happen**. With an upper-hemisphere focus, the person may be repeatedly pushed toward public roles, visible projects, and impact in the outer world; retreating too far from events often starves growth. With a lower-hemisphere focus, the crucial movements are internal; even intense outer careers will feel empty if they do not trigger depth experiences.

Similarly, an eastern emphasis suggests that life presents many openings for self-directed action; problems arise when the person refuses to choose. A western emphasis suggests a curriculum built around relationships and circumstances; the work is not to "take control of everything" but to respond consciously to what arrives. For practice or engine design, hemisphere counts can be implemented early in the pipeline as a coarse-grained descriptor of life structure, which later modules then refine.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The distinction "shape of the life, not the personality of the player" is preserved verbatim as it corrects common misuse of hemisphere emphasis. The summary of upper/lower and east/west meanings is slightly compressed but follows Forrest’s logic.
- **中文**：刻意用「棋盘/游戏规则」的比喻来对应原文的 life-shape，比直接译成「人生结构」更便于读者直觉把握「不是性格，而是生命布局」的差异。"""
    normalized_text_zh: str = """"""
    subject: str = "Guideline #2 – Hemisphere Emphasis: Shape of Life, Not Personality"
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_guideline__2___hemisphere_emph_001_L1",
    )
    version: str = "1.0.0"
