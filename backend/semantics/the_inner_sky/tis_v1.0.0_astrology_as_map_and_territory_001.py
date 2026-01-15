"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134620
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
    semantic_id="tis_v1.0.0_astrology_as_map_and_territory_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class AstrologyAsMapAndTerritory(SemanticEntry):
    """
    **Source Text**:
"I love maps. Even when I was a little boy I would spend hours staring at them... T...
    """
    
    original_text: str = """**Source Text**:
"I love maps. Even when I was a little boy I would spend hours staring at them... The Map Is Not the Territory. And my bubble burst. I could bravely study every square inch of that map in an hour, but to run its waterways and walk its paths I would have to face calluses and cowardice enough to last a lifetime.
  
Astrology is like that. It is a map. It describes the terrain of the human mind. But the map is not the territory. To really experience what the astrological mind map represents, we need to lace up our boots and start exploring. We must put the birthchart away and confront the mind itself... Staring at the chart gets us nowhere. We must swallow our fear, put the map in our pocket, and walk into the woods, ready to face rainbows and rattlesnakes for which no mapmaker can prepare us.
  
Like any expedition, the astrological journey requires forethought. Long before we enter the territory, we must learn all we can about maps in general. The symbols must be familiar to us. Only then are we ready to enter the wilderness on our own. That is what this book is all about. It is a primer in the art of astrological map reading... The next step is yours... You can read until the sun cools down and still not learn how to do astrology. To really fathom it, you must open your heart to the birth-chart—and then open your mouth and talk about what you see. Commitment. Risk. The leap of faith. That is the only way.
  
...Take your time. Keep one hand on the faucet. Follow the procedures we have outlined. They will not fail you. How long did it take you to get to know that friend? A week? A year? And how long have you been sitting with his birthchart? Only a few moments... Understanding a chart, just like understanding a friend, takes a while. You need an unhurried, organized approach. Give the birthchart a chance to speak to you."
  
**Key Term Analysis**:
- `map is not the territory`: classic distinction between symbolic description and lived experience.
- `astrological mind map`: birthchart as representation of psychological terrain.
- `leap of faith`: commitment to move from endless study into real interpretations.
- `keep one hand on the faucet`: re-use of the information‑control metaphor to pace a live reading.
- `unhurried, organized approach`: guideline for how to sit with a chart like one sits with a person.
  
**English Paraphrase (Primary Language)**:
In the closing chapter Forrest returns to a central metaphor: **astrology as map**. A map can be beautiful and detailed, but it is not the journey itself. We can study birthcharts and techniques forever and still never "do" astrology. To cross that threshold we must treat the chart as a **mind map** and then actually enter the territory of the psyche—by talking, listening, and taking interpretive risks with real people.
  
That transition from reading to practice requires both **preparation and courage**. Preparation means learning the symbols and the interpretive "routes" that this book has laid out. Courage means opening our heart to the birthchart and then opening our mouth: voicing what we see, even when our inner critic panics. Forrest calls this the **leap of faith**.
  
He also repeats the advice to **"keep one hand on the faucet"**. In a first live reading we should not try to say everything at once. Instead we follow a patient, organized sequence—triad, hemispheres, focalizers, and so on—giving the chart time to "speak" at its own pace, just as a friendship deepens over months and years rather than minutes.
  
**Complete Chinese Interpretation (Secondary Language)**:
第十二章把整本书拉回到一个朴素却锋利的比喻：**占星只是「地图」，不是「领土」本身**.
  
一张地图可以画得再精细，也无法替我们走完山路。命盘亦然——它只是人类心灵地形的图像化呈现。你可以花很多年学习符号、背诵断语、推演技法，但如果从不真正开口、从不在真实的人与关系中「试着说出你所见」，你就永远停留在「看地图」的阶段，而没有走进那片森林。
  
Forrest 的要求其实很简单也很难：
- 一方面，要有**充分的准备**——先把星座、宫位、行星、相位的语言学到足够熟悉，就像出发前先学会看地图；
- 另一方面，必须在某个时刻做出**信念一跃（leap of faith）**——把书合上，把命盘摆在你和对面那位朋友之间，允许自己在不完美的状态下开始说话。
  
在这个过程中，「水龙头」的比喻再次出现：真正的占星咨询，不是一次性把所有可能的信息都倒在对方头上，而是**一边遵守既定步骤（原初三元 → 半球 → 焦点行星 → 节点），一边根据当下对话缓慢调节水流**。就像结识一个朋友一样，对一张命盘的理解需要时间，需要有条理、不过度焦虑的陪伴，而不是追求五分钟内给出「惊天洞见」。
  
**Core Points**:
- Astrology is a map of the mind, not the lived territory; study alone never becomes practice.
- Moving from reading to doing requires a leap of faith: speaking chart insights to real people.
- The "faucet" metaphor still applies in live work: control information flow via a structured sequence.
- Understanding a chart, like knowing a friend, is inherently gradual and relational.
  
**Detailed Explanation**:
This section reframes all previous technical content as **preparation for relationship**, not an end in itself. The chart is a map of potential meaning, but meaning only comes alive when we risk entering dialogue with a living person. That is why Forrest emphasizes both **method** (learn the map, follow the procedures) and **courage** (accept that you will never feel fully "ready").
  
Methodologically, the passage also stabilizes the role of the earlier guidelines: they are not rigid rules but a **safe starting script** for early readings. By keeping one hand on the faucet—limiting ourselves to a few coherent statements at a time—we reduce the chances of overwhelming either ourselves or the client. Over many sessions, the map and the territory slowly begin to coincide in our understanding.
  
**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The phrase "The Map Is Not the Territory" and the explicit "leap of faith" language are preserved verbatim. Some narrative detail about the hiking map is compressed in favor of highlighting reusable methodological principles.
- **中文**：刻意把「地图/领土」与「水龙头」这两个比喻译成可在其他典籍中复用的术语，强调它们不仅是文学修辞，也是具体的占星工作流提示；对 "Babylonian hieroglyphics" 等修辞则做意象性意译而非逐字翻译。"""
    normalized_text_zh: str = """"""
    subject: str = "Astrology as Map and Territory: From Study to Practice"
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
        l1_anchor="tis_v1.0.0_astrology_as_map_and_territory_001_L1",
    )
    version: str = "1.0.0"
