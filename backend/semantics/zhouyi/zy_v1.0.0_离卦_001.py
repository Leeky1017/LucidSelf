"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899969
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
    semantic_id="zy_v1.0.0_离卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 离卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  离。利贞，亨；畜牝牛吉。

  【彖传】
  《彖》曰：离，丽也。日月丽乎天，百榖草木丽乎土，重明以丽乎正，乃化成天下；柔丽乎中正，故...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  离。利贞，亨；畜牝牛吉。

  【彖传】
  《彖》曰：离，丽也。日月丽乎天，百榖草木丽乎土，重明以丽乎正，乃化成天下；柔丽乎中正，故亨，是以畜牝牛吉也。

  【象传】
  《象》曰：明两作，离；大人以继明照于四方。

  【爻辞】
  初九，履错然，敬之，无咎。
  六二，黄离，元吉。
  九三，日昃之离，不鼓缶而歌，则大耋之嗟，凶。
  九四，突如其来如，焚如，死如，弃如。
  六五，出涕沱若，戚嗟若，吉。
  上九，王用出征，有嘉折首，获匪其丑，无咎。

- 分字分词释义：

  - **离**：附着、依附之义，也指光明、火象。离卦上下皆离，象征"重明"。
  - **利贞，亨**：利于守持正道，可以亨通。
  - **畜牝牛吉**：蓄养柔顺的母牛，象征以柔顺之道承接光明。
  - **丽**：附着、依附，引申为附丽于正道。
  - **重明以丽乎正**：双重光明附丽于正道，可以化成天下。
  - **明两作**：两重光明并起，象征光明相继不息。
  - **继明照于四方**：相继不断地以光明照耀四方。
  - **履错然**：行步谨慎有序，交错分明。
  - **黄离**：黄色附着于天，黄为中色，象征中道之明。
  - **日昃之离**：太阳西斜时的附着，象征光明将衰。
  - **突如其来如**：忽然来临，突兀急促。
  - **出涕沱若，戚嗟若**：涕泪滂沱，忧伤叹息。
  - **王用出征，有嘉折首**：君王出兵征伐，斩获首级。

- **规范化释义（primary_lang_explained）**：

  离卦描写的是"光明附丽、以柔承刚"的智慧。卦辞"离。利贞，亨；畜牝牛吉"——附丽于正道，利于守正，可以亨通；蓄养柔顺如母牛一般的德性，方能承接光明而获吉。

  彖传指出：离即"丽"，日月附丽于天，百谷草木附丽于土，双重光明附丽于正道，方可化成天下。关键在于"柔丽乎中正"：以柔顺附着于中正之道。

  象传"明两作，离；大人以继明照于四方"强调光明相继：两重光明并起，大人以此相继不断地照耀四方。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Li, "The Clinging (Fire)" or "Radiance", portrays situations of attachment, illumination, and clarity. The Judgment, "Li: Beneficial to be correct, success; nurturing a cow brings good fortune", teaches that by adhering to the correct path with yielding gentleness, one can achieve illumination.

- 核心要点：

  - 离卦的核心是**"附丽于正道，以柔顺承光明"**。
  - "重明以丽乎正"提示：光明需要附着于正确的事物，才能持久照耀。
  - 爻辞从"履错然"的谨慎开端，经"黄离"的中道大吉，到"日昃"的衰落警示、"突如其来"的危机、"出涕沱若"的忧患，最后"王用出征"以明威行事。

- 详细解说：

  卦象为上离下离，离重而又重，是"重明"的结构根源。离为火、为日，象征光明、照耀、文明、显赫。但光明需要依附于正道，否则就是野火燎原、焚毁一切。

  初九"履错然，敬之，无咎"是光明初生时的谨慎：行步有序，敬慎而行，可以无咎；六二"黄离，元吉"是离卦的最佳状态：黄为中色，附于中位，故为大吉；九三"日昃之离，不鼓缶而歌"则是光明将衰的警示：太阳西斜，若不知调整心态、坦然面对，年老时只能哀叹。

  九四"突如其来如，焚如，死如，弃如"是光明失控的危机：突然爆发、猛烈焚烧、迅速死寂、最终被弃，象征不当的光明反而焚毁自身；六五"出涕沱若，戚嗟若，吉"则转向内在：涕泪横流、忧伤叹息，反而能获吉，因为懂得忧患的人能居安思危；上九"王用出征，有嘉折首，获匪其丑，无咎"是光明的最终功用：以明威行征伐，斩敌首级，获取异邦之人，匡正邦国。"""
    normalized_text_zh: str = """"""
    subject: str = "离卦（䷝）"
    factor_refs: list = ['zhouyi_gua_li', 'zhouyi_li_attachment', 'zhouyi_huangli']
    
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
        l1_anchor="zy_v1.0.0_离卦_001_L1",
    )
    version: str = "1.0.0"
