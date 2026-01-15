"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899762
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
    semantic_id="zy_v1.0.0_比卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 比卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  比：吉。原筮，元永贞，无咎。不宁方来，后夫凶。

  【爻辞】
  初六，有孚比之，无咎；有孚盈缶，终来有他，吉。
  六二，比之自内...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  比：吉。原筮，元永贞，无咎。不宁方来，后夫凶。

  【爻辞】
  初六，有孚比之，无咎；有孚盈缶，终来有他，吉。
  六二，比之自内，贞吉。
  六三，比之匪人。
  六四，外比之，贞吉。
  九五，显比，王用三驱，失前禽；邑人不诫，吉。
  上六，比之无首，凶。

  【彖传】
  《彖》曰：比，吉也；比，辅也，下顺从也。
  "原筮，元永贞，无咎"，以刚中也。
  "不宁方来"，上下应也。
  "后夫凶"，其道穷也。

  【象传】
  《象》曰：地上有水，比；先王以建万国，亲诸侯。

- 分字分词释义：

  - 比：卦名，有亲近、依附、辅佐之意，象征人与人、邦与邦之间的亲比关系。
  - 原筮：初次占筮，原始之占。
  - 元永贞：元为开始，永为长久，贞为守正，合之为“由始至终守正不移”。
  - 不宁方来：不安宁的诸方前来亲附。
  - 后夫凶：后来者凶，指迟迟不来亲附者终将陷于险境。
  - 有孚比之：以诚信相亲比，彼此信任。
  - 有孚盈缶：诚信之多如同瓦缶装满，比喻诚信充盈。
  - 他：意外之利或额外收获。
  - 比之自内：自内部自然形成的亲比关系。
  - 比之匪人：想要亲比却遇到并非其类之人。
  - 外比之：来自外部的亲附。
  - 显比：显明之比，公开而正当的结盟与亲近。
  - 三驱：古代打猎之法，三面围捕、一面敞开，比喻有所放弃，不尽取，留有余地。
  - 失前禽：放走前面的禽兽，比喻故意舍弃眼前可得之利。
  - 邑人不诫：邑中之人无需再三告诫，自然顺从。
  - 比之无首：亲比却无中心与主导，众人无所依。
  - 地上有水：上坎为水，下坤为地，象征水在地上流行，润泽四方。
  - 建万国，亲诸侯：建立诸侯邦国，并与之保持亲密关系。

- **规范化释义（primary_lang_explained）**：

  比卦讲的是“亲比与结盟之道”。卦辞“比：吉。原筮，元永贞，无咎。不宁方来，后夫凶”指出，亲比之道若建立在一开始就立定的长期守正上，则可以吉而无咎；先前不安宁的各方会前来依附，而迟迟不来的“后夫”则终将处于不利之地。此处的“比”并非盲目依附，而是以诚信为基础、以中正为原则的相互辅佐。

  六爻具体呈现不同形态的亲比关系：初六“有孚比之，无咎；有孚盈缶，终来有他，吉”强调以真诚相待，不仅可免于灾祸，且会在未来获得意外收获；六二“比之自内，贞吉”是指从内部自然形成的亲附，因地位与德行得当而吸引人来亲近；六三“比之匪人”则警示与非其类的人结盟，终将伤感与危险；六四“外比之，贞吉”说明来自外部的亲附，只要自身守正，仍可吉利。九五“显比，王用三驱，失前禽；邑人不诫，吉”则描绘理想的中央之治：君主显明而正当地对待亲比关系，通过“有舍有取”的政策（如三驱之猎，失前禽）来体现仁政，故邑中之人无需多加警戒，自然拥护。

  彖传将比卦的吉凶归结于“辅与顺”：比者辅也、下顺从也。下位之人以真诚辅佐上位，上位之人以德行与原则吸引下位，彼此相应，故吉。若迟迟不来亲比（后夫），说明其道已经穷尽，故凶。


- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Bi, "Holding Together" or "Alliance", is about the way of intimate relationships and alliance, building long-term mutual trust based on sincerity and correctness, while maintaining restraint in the distribution of benefits. The Judgment "Bi: good fortune; inquiring through divination about being primal, perpetual, and steadfast—no blame; the unsettled come; the latecomer meets misfortune" emphasizes that from the initial divination (yuanshi), one should establish principles of "being primal, perpetual, and steadfast" for relationships, reminding that at the earliest stage, a long-term, stable, and correct relationship framework must be established. The Image "water above earth, Bi; the ancient kings thereby established myriad states and maintained intimate relations with the feudal lords" shows that like water flowing over earth, nourishing all things, relationships should be built on broad-based mutual benefit and long-term companionship.

- 核心要点：

  - 比卦强调“以诚信与中正为基础的亲比关系”，既适用于人际，也适用于邦与邦之间的结盟。
  - 卦辞提出从“原筮”开始即立下“元永贞”的原则，提醒在最初阶段就要确立长期、稳定、守正的关系框架。
  - 各爻展示内部亲比、外部亲比、错误结盟、无首之比等多种状态，提示在建立关系时关注“对象是否其类”“是否有清晰中心”。
  - 比卦中的“显比”“三驱失前禽”强调在利益分配与政策制定上要有“有所不取”的节制，以此换取长远的信任与顺从。

- 详细解说：

  比卦的卦象为坤下坎上：地上有水，水润泽大地而不自居其功，象征柔顺承载之中有流动之水，形成温和而有滋养力的关系结构。先王借此而“建万国，亲诸侯”，说明国家体系与国际秩序的建立，本质上是一种有序的亲比与互信体系。

  卦辞中“原筮，元永贞，无咎”可以理解为：在做出结盟与亲附的根本占问时，就要以“长期守正”为前提，而不是以短期利益与权宜算计为主导。若一段关系在起点上就建立在互利且守正的约定之上，则其间虽有波折，也不至于根本失序。

  在爻位层面，初六与六二显示出“由下而上”的自然亲比：初六以诚信主动亲附，六二以内在的中正吸引他人来比。六三“比之匪人”则是对“错误对象”的尖锐提醒：当周围并无真正值得亲比之人时，宁可暂缓，也不可勉强与不合之人结盟。六四“外比之，贞吉”则显示外部联盟在符合自身原则时同样可吉。

  九五“显比，王用三驱，失前禽；邑人不诫，吉”是比卦中最重要的一爻：君主在处理天下亲比关系时，需要兼顾公正与节制。“三驱失前禽”意味着在打猎时有意放走部分猎物，不将所有利益都据为己有；这与“显比”结合，表现为公开透明且有节制的政策，使得邑中之人无需过多戒心，自然拥护。

  上六“比之无首，凶”则提供了一种反例：如果一群人之间存在各种亲附与互助，却没有一个被普遍认可的中心与原则，最终只会因无所统率而走向混乱。对于现代组织与人际网络而言，这是对“去中心化”乱象的一种古老提醒。

  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "比卦（䷇）"
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_比卦_001_L1",
    )
    version: str = "1.0.0"
