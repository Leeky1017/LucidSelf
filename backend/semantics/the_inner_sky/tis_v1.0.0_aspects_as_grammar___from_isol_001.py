"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134438
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
    semantic_id="tis_v1.0.0_aspects_as_grammar___from_isol_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class AspectsAsGrammarFromIsol(SemanticEntry):
    """
    **Source Text**:
"Events in a marriage: since we are dealing with where, immediately the astrologica...
    """
    
    original_text: str = """**Source Text**:
"Events in a marriage: since we are dealing with where, immediately the astrological focus is on the seventh house. Events on the job: now we are looking at the sixth house or perhaps at the tenth. No way to understand the differences between those women without considering at least two houses in each case. So, clearly the interaction between career and marriage cannot be accounted for through an analysis of any single astrological 'bit,' since those phrases can never involve more than one house at a time. Each 'phrase' can have only one where.
... In the mind, nothing happens in a vacuum. All the parts are related. All are interactive. To put it astrologically, the birthchart is greater than the sum of its phrases.
Interpreting a chart is more than grasping each of the ten sign-planet-house combinations. We must understand how they impact on each other. We must realize how each phrase limits or enhances the expression of the rest. In reading a birthchart, we must think in terms of unity. Piecemeal 'phrase-by-phrase' interpretations get us nowhere.
How do we do it? How do we go beyond 'bits'? ...
Aspects
If signs, planets, and houses are the basic words in the astrological language, then aspects are the laws of grammar and syntax that govern how those words must be hooked together. Aspects represent our first solid step toward the formation of full-blown, coherent astrological sentences."

**Key Term Analysis**:
- `beyond bits`: moving from isolated planet–sign–house units to their interactions.
- `aspects as grammar and syntax`: aspects as structural rules linking symbols.
- `birthchart greater than sum of phrases`: whole‑chart unity over piecemeal reading.
- `phrase-by-phrase interpretations get us nowhere`: critique of cookbook astrology.

**English Paraphrase (Primary Language)**:
After teaching how to read individual bits, Forrest warns that real people are more than ten separate planet–sign–house statements. Life domains interact: work affects marriage; self‑esteem colors philosophy; playfulness influences sexuality. No single bit can contain those cross‑domain links, because each has only one house. To understand a chart, we must see how bits influence each other so that the whole birthchart becomes greater than the sum of its parts.

This is where **aspects** enter. If signs, planets, and houses are the basic words of the astrological language, aspects are its grammar and syntax—the rules that say which words are tied together and how. An aspect is simply a geometric angle between two (or more) planets, but symbolically it signals a permanent relationship between their functions. When we interpret aspects, we are no longer only asking what–how–where for each bit; we are asking how these bits cooperate, clash, or reinforce each other to form full sentences in the psyche.

**Complete Chinese Interpretation (Secondary Language)**:
在教完如何解读单个 bit 之后，Forrest 提醒读者：真实的人绝不只是十条彼此孤立的「行星×星座×宫位」说明。生活领域之间会互相牵动：工作影响婚姻，自尊影响世界观，玩心影响性表达。任何一个 bit 只能带着一个宫位，因此没办法单独解释这些跨领域连动。要真正读懂一张命盘，我们必须看到各个 bit 如何互相制约、互相加成，让整张命盘成为「大于诸多片段总和」的整体。

这正是**相位**登场的地方。如果说星座、行星与宫位是占星语言的基础「单词」，那么相位就是让这些单词组合成句子的**语法与句法规则**。在天文学上，相位不过是行星之间的几何角度；在象征层面，它表示两种心理功能之间存在一种长期而紧密的关系。从此解读就不再只是在每个 bit 上问「是什么/如何/在哪里」，而是要追问：这些 bit 之间是在合作、在冲突、还是在互相助力？它们究竟组成了怎样的心灵长句？

**Core Points**:
- Single bits are not enough; charts must be read as interacting systems.
- Aspects are the grammar and syntax that link basic words (planets, signs, houses).
- Aspects describe how different functions support, challenge, or modify each other.
- Whole‑chart unity is the goal; cookbook phrase‑by‑phrase reading is inadequate.

**Detailed Explanation**:
This framing upgrades interpretation from local to systemic. Without aspects, we know only what each function wants and where it plays out. With aspects, we learn which functions are fused, polarized, in friction, or in easy alliance. That explains, for example, why two people with similar bits can live very different lives: their internal "wiring"—the aspects—routes energy differently.

By calling aspects grammar and syntax, Forrest reinforces the language model: an aspect is not "good" or "bad" but a rule about how words must be combined. A chart rich in tense aspects may feel challenging but can support profound development; a chart full of easy aspects may invite stagnation if the person never chooses to grow. For calibration and engine design, this implies that any serious interpretive layer must include aspect relationships as constraints and modifiers on base factors, not just as separate checklists of "traits."

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The metaphor "birthchart is greater than the sum of its phrases" and "aspects = grammar and syntax" is preserved verbatim, as they anchor the conceptual shift. The critique of phrase‑by‑phrase interpretations is kept but reframed as a methodological warning rather than polemic.
- **中文**："grammar and syntax" 统一译为「语法与句法」，以强调是结构规则而非「吉凶标签」。对「greater than the sum of its phrases」直译为「大于诸多片段总和」，并补充「整体/系统」语汇，方便后续与引擎中的系统级建模对接。"""
    normalized_text_zh: str = """"""
    subject: str = "Aspects as Grammar – From Isolated Bits to Interacting Psyche"
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
        l1_anchor="tis_v1.0.0_aspects_as_grammar___from_isol_001_L1",
    )
    version: str = "1.0.0"
