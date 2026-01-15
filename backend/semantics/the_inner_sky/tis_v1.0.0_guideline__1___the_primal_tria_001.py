"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134468
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
    semantic_id="tis_v1.0.0_guideline__1___the_primal_tria_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class Guideline1ThePrimalTria(SemanticEntry):
    """
    **Source Text**:
"Ten planets, each molded into a 'bit' by a sign and a house. Five aspects weaving ...
    """
    
    original_text: str = """**Source Text**:
"Ten planets, each molded into a 'bit' by a sign and a house. Five aspects weaving those 'bits' together in five different ways. Throw in rulerships, retrogradation, the moon’s nodes. Add a concentration of planets above the horizon, or in the east. Getting dizzy? That’s not surprising. Astrology is complicated. Sometimes, looking at a birthchart, you might begin to feel like a juggler with one too many balls in the air. But rest assured: there are procedures to follow, maps designed to help us navigate through the often bewildering territory of the birthchart. If we stick to them, we will not get lost. ...
GUIDELINE NUMBER ONE: Ignore everything until you have thoroughly grasped the sun, moon, and ascendant.
This simple rule is the most valuable piece of practical advice available to anyone learning to interpret birthcharts. I strongly suggest you never deviate from it. Sun, moon, and ascendant stand head and shoulders above the other influences. They are the Primal Triad. Regardless of what signs and houses they occupy and what aspects they make, they are the kingpins of the birthchart. Nothing that is not well supported by them is likely to figure prominently in the personality. Think of the primal triad as forming the skeleton of the character. ...
Sun, moon, and ascendant: identity, the soul behind that identity, and the mask it wears in the world. Simple. Clear. Effective."

"Five Steps—Analysis of the Primal Triad
STEP ONE Look at the Sun. Its what is the formation of identity. Consider the sign it occupies. Why is that person alive? What is his evolutionary goal? How can he most effectively realize it? What risks does he face? Now add the sun’s house. Where is he confronted with the clearest expression of those solar ego-forming issues? Where is the major battlefield of his life?
STEP TWO Look at the moon. Its what is the formation of the individual’s subjective, emotional nature. What sign shapes it? What kinds of experience are most essential to his happiness? How can he attain them? ... Now add the moon’s house. Where does he face the most turbulent emotional issues in his life? ...
STEP THREE Consider the ascendant. ... How does this person appear to the world? What is his mask? ... How is that mask different from what we see in the sun and moon? How is it similar? ...
STEP FOUR Consider the aspects among the elements of the primal triad. ...
STEP FIVE ... Get a 'feel' for the individual’s primal triad. If you could make only one statement about it, what would it be? Who is this person? ... Grasp that, and you have established a context for the rest of the astrological analysis. Fail, and your interpretation is fragmentary and disconnected."

**Key Term Analysis**:
- `Primal Triad`: the sun, moon, and ascendant as the three "kingpins" of the chart.
- `chart skeleton`: core structure defined by identity, soul, and mask, before adding other details.
- `Guideline #1`: rule to ignore everything else until the Primal Triad is understood.
- `five-step analysis`: ordered procedure for working through the triad before the rest of the chart.

**English Paraphrase (Primary Language)**:
Forrest opens his whole-chart method by acknowledging that astrology easily overwhelms us. Ten planetary bits, five aspect families, rulerships, retrogrades, the nodes, hemispheres—too many moving parts. To regain control, he proposes clear guidelines, starting with **Guideline #1**: ignore everything until you have thoroughly grasped the **Primal Triad**—sun, moon, and ascendant.

These three stand above all other influences. Together they form the skeleton of character: the sun as identity and ego, the moon as soul and emotional core, and the ascendant as the mask or vehicle through which that inner life meets the world. Nothing that is not supported by them is likely to matter deeply in the personality. Forrest then offers a five‑step procedure: analyze the sun by sign and house (what, why, where of identity); analyze the moon by sign and house (what experiences the soul needs and where feeling issues concentrate); analyze the ascendant (what kind of social personality and mask fits the chart); consider aspects linking the three; and finally, synthesize a single, evocative sentence that captures their blend.

Only once this skeleton is clear should we move on to other planets and techniques. Without that structural context, interpretations become fragmented lists rather than a coherent story.

**Complete Chinese Interpretation (Secondary Language)**:
Forrest 在进入「整体解读」之前，先承认一件事：一张命盘的信息量很容易把人淹没。十颗行星各自形成的 bit，五大相位家族、守护与失势、逆行、月亮交点、半球分布……符号越来越多，思路反而越来越乱。为此，他给出一套「控制信息水龙头」的工作规程，其中最重要的就是**指引一：在彻底理解太阳、月亮与上升之前，先把其他一切都暂时放下**。

这三者合称 **Primal Triad（原初三元）**，是整张命盘的「支点」。无论它们落在哪些星座与宫位、形成哪些相位，太阳、月亮与上升永远站在其他因素之上，是人格结构的**骨架**：太阳定义「我是怎样的一个人」；月亮刻画「我内在的感受与灵魂基调」；上升则是「我用来在世界里行动与呈现自己的面具/载具」。凡是不被这三者支撑的象征，很少会在人格中占据真正核心的位置。

为避免只停留在抽象概念，Forrest 进一步给出一个**五步分析流程**：
1. 先看太阳：以星座与宫位回答「我为何而活？演化目标是什么？在哪个生活领域最明显地被推去练习这个目标？」
2. 再看月亮：以星座与宫位回答「什么经验对我的幸福最关键？情绪风暴通常在哪个生活领域爆发？」
3. 接着看上升：观察「我在人前的样子」与「最适合作为日常人格载具的风格」，以及它与日月之间的相似与反差。
4. 然后考察三者之间的相位：它们之间究竟是相互支援，还是充满张力？
5. 最后，把这一切压缩成一句话：如果只能用一条描述来概括这个人的原初三元，那会是什么？这一句话就构成之后所有细节解读的背景与坐标系。

只有在这条骨架先被看清之后，其它行星与技术才值得逐一展开；否则，命盘就只会变成一串割裂的「配置清单」，而难以形成真正连贯的生命叙事。

**Core Points**:
- The Primal Triad (sun, moon, ascendant) is the skeleton of the chart.
- Guideline #1: ignore other factors until the triad is well understood.
- A five‑step process turns the triad into a single, evocative characterization.
- All other bits must be interpreted in the context of this structural core.

**Detailed Explanation**:
This guideline operationalizes information control. Instead of trying to hold all ten planets and every technique in mind at once, we anchor interpretation in three central symbols. Their signs and houses define identity, soul tone, and social mask; their aspects define whether those layers harmonize or clash. The final "one‑sentence" synthesis forces the astrologer (or engine) to prioritize: what is most essential about this person’s core configuration?

Once that skeleton is in place, additional details become refinements rather than competing centers of gravity. Mars, for example, can no longer be misread in a way that contradicts the triad. For system design, this suggests a staged pipeline: first derive a triad‑level profile, then let all subsequent modules inherit that context.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The phrase "Ignore everything until you have thoroughly grasped the sun, moon, and ascendant" is preserved as the central rule. The metaphor of the triad as skeleton is kept and expanded into procedural language.
- **中文**：把 Guideline #1 译为「在理解日月上升前先放下其他一切」，并将 Primal Triad 统一译作「原初三元」，以与之前章节保持术语一致；对「one statement about it」则译为「一句话压缩描述」，鼓励在实际解读与引擎实现中都进行强制信息压缩。"""
    normalized_text_zh: str = """"""
    subject: str = "Guideline #1 – The Primal Triad as Chart Skeleton"
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
        l1_anchor="tis_v1.0.0_guideline__1___the_primal_tria_001_L1",
    )
    version: str = "1.0.0"
