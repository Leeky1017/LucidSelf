"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134494
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
    semantic_id="tis_v1.0.0_guideline__3___planetary_focal_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class Guideline3PlanetaryFocal(SemanticEntry):
    """
    **Source Text**:
"GUIDELINE NUMBER THREE: After absorbing the meaning of the primal triad and unders...
    """
    
    original_text: str = """**Source Text**:
"GUIDELINE NUMBER THREE: After absorbing the meaning of the primal triad and understanding the birthchart’s hemispheric emphasis, establish the identities of the planetary focalizers. Once identified, understand what role they play in the chart.
Many different factors can spotlight a particular planet, making it stand out above the others. Many other factors can weaken a planet, rendering its influence obscure. Medieval astrologers referred to these two situations as dignities and debilities. The words are still useful, provided we do not equate them with 'good' and 'bad.' ...
Every birthchart has at least one focalizer, and picking it out is easy. It is the ruler of the ascendant, and no matter how debilitated it might be by other factors, it is still a powerhouse. ... Simply knowing that a planet is a focalizer tells us very little. We must go further. We must understand how that dignity affects its function in the birthchart. ...
Planets in their rulerships ... become focalizers. ... Planets in their falls are debilitated. ... Placement in its own natural house strengthens a planet, increasing its dignity. Such planets may also serve as focalizers.
Any planet forming a conjunction with the sun is a focalizer. ... A stellium occurs when three or more planets all occupy the same sign or house. ... The stellium itself becomes the focalizer. ... The four angles of the birthchart ... are power points. Any planet that forms a conjunction with one of them is immediately catapulted into a position of tremendous prominence. It becomes a focalizer of inordinate power ... A singleton is a planet that lies alone in any one of the four hemispheres of the birthchart. ... Such a position places a heavy load on the planet. ... Singletons are not common. But when they do exist, they certainly serve as critical focalizers. Planets are stationary when they are standing still in the sky, about to turn retrograde or direct. ... Such a planet has increased authority in the birthchart. It too can serve as a focalizer. ... Any planet that makes a great number of aspects is a focalizer. Why? Simply because it has a finger in everyone’s pie. ... If there is any rule of thumb here, it is this: compare each planet to all the others in the same birthchart. Which one is wired into the chart most inextricably? That one is certainly your focalizer.
... What focalizers help us do is to organize our approach to the planets. They tell us which phrases are most vividly present in an individual’s character, and which ones play secondary roles. ... The question focalizers answer best is a purely practical one: Which planets should we talk about first? Priorities, that’s all."

**Key Term Analysis**:
- `planetary focalizer`: a planet (or pattern) singled out as structurally central in a chart.
- `dignity and debility`: relative strengthening or weakening conditions, not moral good/bad.
- `ruler of the ascendant`: guaranteed focalizer as ambassador of the rising sign.
- `stellium / angular planet / singleton / stationary planet / heavily aspected planet`: distinct mechanisms that confer focalizer status.

**English Paraphrase (Primary Language)**:
Guideline #3 adds the next layer of whole‑chart order: once we understand the Primal Triad and hemisphere emphasis, we must locate the **planetary focalizers**—the planets or patterns that stand out above the rest. Forrest defines focalizers through a language of **dignities and debilities**, but warns that these are not moral labels; they only indicate relative strength or clarity of expression.

Every chart has at least one focalizer: the **ruler of the ascendant**, which always plays a pivotal role in centering the personality. Other focalizers arise when planets are strongly **dignified**—for example, in their own signs or natural houses, conjunct the sun, forming **stellia**, or placed on the four angles or in angular houses. More subtle cases include **singletons** (the only planet in a hemisphere), **stationary planets** about to turn retrograde or direct, and **heavily aspected planets** that keep appearing in the aspect grid. In practice, several of these factors may converge in one planet, or be distributed among a small group.

Identifying a focalizer is only the first step. We must still interpret the underlying bit: its sign, house, and aspects, especially to the Primal Triad. The point of guideline #3 is not to crown a single "Lord of the Chart" but to establish **priorities**. Focalizers tell us which phrases we must discuss first and in greatest depth, and which can be treated as secondary nuances.

**Complete Chinese Interpretation (Secondary Language)**:
第三条整体指引是在原初三元与半球重心之上，再往前推进一步：找出这张命盘中**哪几颗行星（或行星组合）在结构上格外「抢眼」**。Forrest 把这种被凸显出来的行星称为 **focalizers（焦点行星）**，并借用「得势/失势（dignity/debility）」的传统术语来讨论它们的强弱，但他特别提醒：这里谈的只是**表达强度与清晰度**，绝不是「好坏吉凶」。

每一张命盘至少有一个焦点行星：**上升的守护星**。无论它在其他维度上多么失势，它都在帮助个体维持「我是谁」的中心感，是上升星座的「大使」。除此之外，一颗行星如果满足下列任一条件，也很可能成为焦点：
- 落在自己守护的星座或自然宫位（得势）；
- 与太阳合相，被「嫁接」进人格核心；
- 参与一个 **stellium（多颗行星聚集同一星座/宫位）**，整个 stellium 本身就成为焦点；
- 与四大角度（上升、下降、中天、天底）合相，或至少落在四个角宫（1/4/7/10 宫）之一；
- 成为 **singleton（半球孤星）**，独自承担一个半球的能量主题；
- 处于即将逆行或顺行的 **stationary（驻留）** 状态；
- 在相位网格中「到处都出现」，也就是一颗 **heavy-aspected planet（重相位行星）**。

真正的工作不只是在清单上勾选谁是焦点，而是：一旦确认某颗行星为焦点，就要回到它自身的 bit——星座、宫位与相位——去细致解读，并且特别观察它与原初三元之间的互动。Guideline #3 的目的不是选出一个「至尊行星」把其他全部盖掉，而是为了在解读顺序上建立**轻重缓急**：哪些象征必须优先、深入地谈清楚，哪些则可以作为次要修饰线索。

**Core Points**:
- Guideline #3: after triad and hemispheres, identify planetary focalizers.
- Focalizers are defined by structural conditions of dignity, not by moral value.
- The ruler of the ascendant is always a focalizer; many other patterns can add or create focalizers.
- Focalizers are about interpretive priorities—what must be discussed first and in depth.

**Detailed Explanation**:
This guideline prevents "flat" readings where all placements seem equally important. In reality, some circuits are more central: they sit on angles, rule the mask, cluster in stellia, or connect to everything via aspects. By naming them as focalizers, Forrest gives the interpreter a triage tool: start with these, connect them back to the Primal Triad, then expand outward.

For an engine or structured practice, focalizers suggest a scoring layer that **weights** planets by structural prominence: rulership of the ascendant, angularity, rulership dignity, stellium membership, singleton status, station, aspect centrality. But Forrest resists turning this into a rigid point game. The goal is not to crown a winner; it is to know which planetary stories are carrying the heaviest developmental pressure and self‑identification for this person.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The catalogue of focalizer conditions is condensed but preserves all major categories Forrest lists. The critique of old "point system" dignity scoring is echoed by emphasizing priorities over domination.
- **中文**：对 dignity/debility 统一译为「得势/失势」，并反复强调其功能性含义（强弱、清晰度），避免被重新理解成吉凶高低。"focalizer" 直接音译为「焦点行星」，并在上下文中说明其是「解读顺序与权重」的技术性概念。"""
    normalized_text_zh: str = """"""
    subject: str = "Guideline #3 – Planetary Focalizers and Dignity"
    factor_refs: list = ['dignity', 'debility', 'singleton']
    
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
        l1_anchor="tis_v1.0.0_guideline__3___planetary_focal_001_L1",
    )
    version: str = "1.0.0"
