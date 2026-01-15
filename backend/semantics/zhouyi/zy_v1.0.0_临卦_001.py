"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899868
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
    semantic_id="zy_v1.0.0_临卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 临卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  临：元亨，利贞，至于八月有凶。

  【彖传】
  《彖》曰：“临，刚浸而长，说而顺，刚中而应，大亨以正，天之道也。至于八月有凶，消不...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  临：元亨，利贞，至于八月有凶。

  【彖传】
  《彖》曰：“临，刚浸而长，说而顺，刚中而应，大亨以正，天之道也。至于八月有凶，消不久也。”

  【象传】
  《象》曰：泽上有地，临；君子以教思无穷，容保民无疆。

  【爻辞】
  初九，咸临，贞吉。
  九二，咸临，吉，无不利。
  六三，甘临，无攸利；既忧之，无咎。
  六四，至临，无咎。
  六五，知临，大君之宜，吉。
  上六，敦临，吉，无咎。

- 分字分词释义：

  - **临**：临视、面临、亲临之意，上而临下，亦有走近、关怀之象。
  - **元亨，利贞**：大通大顺，又利于坚守正道，为“临”得其正的基础条件。
  - **至于八月有凶**：八月象征阴长阳消，“盛极而衰”的时间拐点，提示在盛势之中预防凶险。
  - **刚浸而长，说而顺**：阳刚之气逐渐浸润、增长，风气和悦而顺，既有上升之势，又需循理而行。
  - **教思无穷，容保民无疆**：教化之思无穷尽，以宽容之德庇护百姓，不设疆界。
  - **咸临 / 甘临 / 至临 / 知临 / 敦临**：分别指感通而临、以甜言而临、深入而临、以智慧而临、以敦厚而临，代表不同的临民姿态。

- **规范化释义（primary_lang_explained）**：

  临卦讲“在位者如何临下”“如何在高位中保持自省与节制”。卦辞一方面肯定“临：元亨，利贞”，说明只要临之以正，则可以大吉大利；另一方面又加上一句“至于八月有凶”，提醒盛势之中自有将衰之机，临得越高，越需预备收敛与转折。

  彖传从卦象说明：阳刚之气渐渐浸润而长，氛围和悦而顺，阳刚居中并与柔顺相应，因此可以“大亨以正”，符合“天之道”；但阳盛不久，终归消退，故“消不久也”。象传“泽上有地，临”：上为地、下为泽，如在上的人俯临众生；君子体此之象，应在教化上“不厌其烦”，在庇护上“不设疆界”。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Lin, "Approach", describes a time when strength and influence are growing, and one is approaching a position of power or responsibility. The Judgment, "Lin: great success through correctness; in the eighth month there will be misfortune", indicates that while the approach is auspicious, one must remain vigilant because after reaching a peak, decline can follow.

- 核心要点：

  - 临卦强调**权柄在手时的姿态与节制**：临下既要感通、教化，又要知其时限，不可沉迷于一时顺势。
  - “至于八月有凶”提供一个清晰的**时间告诫**：当局面极盛时，风险已经逼近，需要提前调整节奏。
  - 各爻从咸临、甘临到知临、敦临，刻画了不同层次的“临”，可视为领导风格与带人方式的标本。

- 详细解说：

  卦象为地临泽：泽处于下，地处于上，上者厚重而在高位，下者卑而受润，构成“在上而临下”的局面。与前一卦蛊相比，蛊偏重“整弊治乱”，临则偏重“在整顿之后，如何长期持守与教化”。

  时间意象是本卦的关键特色。“八月有凶”并不局限于农历八月，而是提示任何形势发展都会经历一个“阳长阴消”到“阳消阴长”的转折点。对个人与组织而言，当资源、声望、影响力正盛时，若仍只看“元亨利贞”，而忽略“消不久也”，就很容易在后续骤然遭遇逆风。

  爻辞中的多种“临”，也提醒人们分辨不同的临人方式：
  - “咸临”重在真诚感通；
  - “甘临”则偏向糖衣与安抚，如果能“既忧之”，还可回头；
  - “知临”是大君理想的临视之道——知人、知时、知止；
  - “敦临”则是收尾阶段的姿态：在高位之时仍能敦厚不苛求外功，方可避凶。


  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "临卦（䷒）"
    factor_refs: list = ['zhouyi_gua_lin']
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_临卦_001_L1",
    )
    version: str = "1.0.0"
