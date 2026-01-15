"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134260
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
    semantic_id="tis_v1.0.0_major_aspect_families___conjun_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class MajorAspectFamiliesConjun(SemanticEntry):
    """
    **Source Text**:
"Aspects
If signs, planets, and houses are the basic words in the astrological lang...
    """
    
    original_text: str = """**Source Text**:
"Aspects
If signs, planets, and houses are the basic words in the astrological language, then aspects are the laws of grammar and syntax that govern how those words must be hooked together. Aspects represent our first solid step toward the formation of full-blown, coherent astrological sentences."

"Zero Degrees: The Conjunction
The simplest of all the aspects is the conjunction. This occurs when two planets are right on top of each other. Their functions are grafted together. Each one flavors the other, and in their union a kind of 'macro-bit' is formed, far more complex than a single sign-planet-house combination. Fusion—that is the essence of the conjunction. Two 'bits' become one."

"180 Degrees: The Opposition
The opposition is one of the 'bad' aspects in old-time astrology. It is true that this aspect produces enormous tension. But that tension can add profound depth and resiliency to the birthchart. Much depends on how the individual chooses to respond to the issues the opposition presents. ... The tension between the Taurean planet and the Scorpionic one can be invaluable. Each can correct for the excesses and deficiencies of the other. Neither one likes it. But both are better off. ... That is the point with oppositions—expanding our awareness sufficiently to see both sides of an issue."

"90 Degrees: The Square
Like the opposition, the square is considered to be a malevolent aspect. ... Squares produce friction, just as oppositions produce tension. ... In a square, the two phrases have no basis for mutual understanding. There is no common ground, no common language. Only a mile-high wall of incomprehension. ... Squares serve the same purpose: the friction produced in a square exerts relentless developmental pressure on each of the planets. To survive, they must evolve. ... Don’t look for ways to 'resolve' a square. You won’t find them. ... Ideally, that restlessness is a healing force, leading not to peace, but to growth and accomplishment."

"120 Degrees: The Trine
To the fortune-tellers, it is the Rolls-Royce of aspects. ... Don’t believe it. Thinking that trines are automatically 'good' is like believing that any marriage in which the partners never fight must automatically be a great one. ... Trines mean harmony. ... But because of that internal accord, the phrases support each other in a web of common needs, but the trine gives planets no perspective on themselves. ... The trick with trines is to see them as representing areas of life with almost unlimited potential for growth. ... We must awaken them. ... If we succeed in sparking a trine into action and development, it can carry us further than any square or opposition, and do so with far less effort."

"60 Degrees: The Sextile
Another 'good' aspect, the sextile is usually understood to work like a watered-down trine. In actual fact, its action is quite distinct. ... Sextiles produce excitation. They are intense, colorful, dynamic. Both planets are stimulated and enlivened. ... Like trines, sextiles can suffer from short-sightedness. ... Like friendly marriages, their Achilles’ heel is their slowness to recognize fundamental interactive weaknesses. And without that recognition there can be no strategy for defense and no possibility of growth."

**Key Term Analysis**:
- `conjunction as fusion`: two bits forming a macro‑bit with fused functions.
- `opposition as tension`: polarized planets creating depth through holding both sides.
- `square as friction and pressure`: developmental conflict with no common language.
- `trine as dormant potential`: easy harmony that needs conscious activation.
- `sextile as excitation`: lively, stimulating alliance that can be short‑sighted.

**English Paraphrase (Primary Language)**:
Forrest groups the major aspects into functional families with distinct growth roles. A **conjunction** (0°) fuses two functions. Their circuits are grafted together so thoroughly that when one fires, so does the other. The result is a macro‑bit—more complex than a simple planet–sign–house statement—demanding that we understand how the two fused functions now operate as one.

An **opposition** (180°) polarizes two planets. Old astrology called it "bad" because it creates enormous tension. Forrest reframes it: the strain can be invaluable if we let each side correct the other’s excesses. The task is to widen awareness enough to hold both ends of the polarity and negotiate a living compromise, rather than flipping between them.

A **square** (90°) brings friction and misunderstanding. The two phrases have no common ground; their agendas and languages clash. Yet that very friction exerts relentless evolutionary pressure. Squares are not meant to be "solved" into comfort; they remain sources of restlessness that, when faced honestly, drive growth and accomplishment.

A **trine** (120°) links planets in easy harmony. Functions become natural allies, joining forces without effort. But trines can lull us to sleep: ease without awareness becomes complacency. Forrest treats trines as zones of almost unlimited potential that must be consciously awakened and directed. When activated, they can carry us farther than tense aspects, with less wear and tear.

Finally, a **sextile** (60°) resembles a lively friendship or first romance. It excites and energizes both planets, clarifying their essence through mutual stimulation. Like trines, sextiles are friendly, but their risk is giddiness and lack of perspective: enthusiasm that flares up and dies before anything solid is built.

**Complete Chinese Interpretation (Secondary Language)**:
Forrest 将主要相位划分为几个具有不同成长功能的家族。

**合相（0°）**：两颗行星几乎「叠在一起」，各自的心理功能被紧密嫁接在一起，形成一个更复杂的「巨型 bit」。一旦其中一条电路被点燃，另一条也随之启动。因此在解读时，必须把这两种功能当作一个合成整体来理解，而不是分开看两条说明。

**对分（180°）**：两颗行星处于极端对立的位置。旧式占星把它视为「凶相」，因为它带来巨大的张力。Forrest 重新诠释它：这种拉扯若被好好运用，可以赋予命盘深度与韧性。任务是扩展觉察，一边让两端的需求彼此校正，一边学会在两极之间保持有意识的平衡，而不是在「非此即彼」的摆荡中自我破坏。

**刑相（90°）**：带来摩擦与「听不懂对方在说什么」。两个象征之间既无共同语言、也无共同目标，却被迫共存。正因为这种不和谐，刑相对双方施加持续的演化压力：要活下来就必须进化。它们不提供最终和平，提供的是推动力——一种迫使人格不断调整、精炼和成长的内在紧张。

**拱相（120°）**：行星之间的自然同盟，运行顺畅、感觉「好」。但这种顺畅的危险在于：没有摩擦就缺乏自省，很容易躺平。Forrest 把拱相视为「潜力几乎无限的区域」，前提是当事人要主动点燃它——有意识地培养与运用那些已经很顺手的天赋。一旦被唤醒，拱相可以在较小代价下，带来比刑/对分更长远的成长。

**六合（60°）**：常被误解为「缩水版拱相」，实际上更像一场高能、略带青春期色彩的互动：彼此激发、充满活力，但不一定稳定。六合有助于两颗行星走向成熟，却也容易流于三分钟热度。若欠缺觉察，这种激动可能在真正结果出现之前就消散。

**Core Points**:
- Conjunctions fuse functions into macro‑bits that must be read as one.
- Oppositions create tension that can deepen character if both sides are honored.
- Squares provide relentless developmental friction rather than peace.
- Trines mark latent zones of ease that need conscious activation to avoid stagnation.
- Sextiles excite and energize, but require perspective to turn enthusiasm into maturity.

**Detailed Explanation**:
These aspect families provide a functional vocabulary for describing how planetary circuits interact. Conjunctions answer "what is fused with what"; oppositions and squares define where tension and friction push for evolution; trines and sextiles highlight where energy flows easily but may be under‑used.

For growth‑oriented astrology, the key is to drop "good/bad" judgments and instead ask what each aspect family is trying to accomplish. Oppositions and squares often feel hard but keep us from one‑sidedness. Trines and sextiles feel good but may hide unexamined habits. Conjunctions can be brilliant synergies or blind spots where two functions are so merged we can’t tell them apart. This functional framing lets interpreters offer nuanced guidance: where to lean into difficulty, where to wake up latent gifts, and where fused energies need differentiation.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The traditional labels "good/bad" are explicitly rejected following Forrest. Terms like "malevolent" are kept only in historical quotations, then reframed in functional language (tension, friction, potential, excitation).
- **中文**：对「凶吉」语汇不作正面使用，而是统一转译为「张力、摩擦、潜力、激发」等中性功能性表述；对 "macro-bit" 继续借用「巨型 bit」以保持与前文结构建模的一致性。

**Narrative Snippets**:
- `[ns_innersky_013]` `[trigger: explaining_aspects]` `[factor_trigger: tension]` `[role: 主干]` Aspects are the laws of grammar that govern how planets must be hooked together into coherent sentences. → Source Text
- `[ns_innersky_014]` `[trigger: conjunction_reading]` `[factor_trigger: aspect_conjunction]` `[role: 主干依赖]` In a conjunction, two functions are grafted together—fusion is the essence; two bits become one. → Source Text
- `[ns_innersky_015]` `[trigger: opposition_reading]` `[factor_trigger: aspect_opposition]` `[role: 条件分支]` Opposition produces enormous tension, but that tension can add profound depth and resiliency to the chart. → Source Text
- `[ns_innersky_016]` `[trigger: square_reading]` `[factor_trigger: aspect_square]` `[role: 总结]` Squares produce relentless developmental pressure—don't look for ways to resolve them; you won't find them. → Source Text
- `[ns_innersky_017]` `[trigger: trine_reading]` `[factor_trigger: aspect_trine]` `[role: 主干]` Trines represent areas with almost unlimited potential for growth—but we must awaken them. → Source Text
- `[ns_innersky_018]` `[trigger: sextile_reading]` `[factor_trigger: aspect_sextile]` `[role: 主干依赖]` Sextiles produce excitation and liveliness, but their Achilles' heel is slowness to recognize fundamental weaknesses. → Source Text"""
    normalized_text_zh: str = """"""
    subject: str = "Major Aspect Families – Conjunction, Opposition, Square, Trine, Sextile"
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
        l1_anchor="tis_v1.0.0_major_aspect_families___conjun_001_L1",
    )
    version: str = "1.0.0"
