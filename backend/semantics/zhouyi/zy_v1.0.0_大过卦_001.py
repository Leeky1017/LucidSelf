"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899951
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
    semantic_id="zy_v1.0.0_大过卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 大过卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  大过：栋桡；利有攸往，亨。

  【彖传】
  《彖》曰：“大过”，大者过也；“栋桡”，本末弱也。刚过而中，巽而说行，利有攸往，乃亨。...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  大过：栋桡；利有攸往，亨。

  【彖传】
  《彖》曰：“大过”，大者过也；“栋桡”，本末弱也。刚过而中，巽而说行，利有攸往，乃亨。“大过”之时大矣哉！

  【象传】
  《象》曰：泽灭木，大过；君子以独立不惧，遁世无闷。

  【爻辞】
  初六，藉用白茅，无咎。
  九二，枯杨生稊，老夫得其女妻；无不利。
  九三，栋桡，凶。
  九四，栋隆，吉；有它，吝。
  九五，枯杨生华，老妇得其士夫；无咎无誉。
  上六，过涉，灭顶，凶，无咎。

- 分字分词释义：

  - **大过**：一方面指“过度”“过盛”，另一方面也有“通过大险”“大中之过”的含义，是在极端条件下的行事之道。
  - **栋桡**：栋，屋梁；桡，弯曲。屋梁弯曲，象征结构承载过重、中心失衡。
  - **本末弱也**：根本与末端都软弱无力，无法支撑大过之重，提示底层结构与外围支持都不足。
  - **刚过而中，巽而说行**：刚强有余而能守中，通过谦巽与和悦的方式行事，方能在“过”的局面中行而不覆。
  - **泽灭木**：水泽淹没树木，象征外在环境之险已超过内部结构所能承受的程度。
  - **藉用白茅**：用洁净柔软的白茅草垫在下面，比喻在极端局势中加一层谨慎与敬畏，以减轻冲击。
  - **枯杨生稊 / 生华**：枯萎的杨木重新生芽、生花，象征在衰老结构中出现新生关系或新机缘，但其可持续性存疑。
  - **老夫得其女妻 / 老妇得其士夫**：年老者与年轻伴侣结合，隐含“配偶失衡”“年龄结构悬殊”之象，利弊并存。
  - **过涉，灭顶**：涉水过度而没过头顶，比喻越界太甚，虽未必有可责之罪，却身处极险之中。

- **规范化释义（primary_lang_explained）**：

  大过卦所描绘的是一种“结构性失衡但又必须硬撑通过”的处境。卦辞说：“大过：栋桡；利有攸往，亨。”——屋梁已弯，结构摇摇欲坠，却又偏偏是在这种时刻，“有利于有所往而亨通”，前提是必须清醒意识到“栋桡”的危险，而不是盲目加码。

  彖传解释“大过”为“大者过也”，本末皆弱，刚强之气虽然过盛，但若能守中、以巽顺喜悦之态行事，仍有在险中通达的可能。这种大过之时，既是危险之极，也是转折之机，关键在于如何分辨哪些“过”是必经之度，哪些“过”已是一脚踏空。

  象传“泽灭木，大过；君子以独立不惧，遁世无闷”把场景放大为：水泽淹没树木，周围一切支撑似乎都不可靠，君子只得独立其身，不以环境惊惧，必要时甚至隐退避世而不心怀怨怼。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Da Guo, "Great Excess" or "Preponderance of the Great", describes situations where the load or pressure has become excessive and the structure risks collapse. The Judgment, "Da Guo: the ridgepole sags; it is favorable to have somewhere to go; success", warns that immediate action is needed to address the imbalance before catastrophe occurs.

- 核心要点：

  - 大过卦讲的是**“大不平衡之中如何通过”**，既要看到结构的极限，又要在不得不行时把握分寸。
  - “栋桡”警示：在高负载局面下，任何再加重的决策都可能成为压垮结构的最后一根稻草。
  - 爻辞展示了一条从谨慎铺垫（白茅）、到勉强重组关系（枯杨）、再到极限涉险（灭顶）的轨迹。

- 详细解说：

  从卦象看，大过为上兑下巽，象“泽灭木”：柔弱在上下两端（初六、上六），中间四爻皆为阳，形成“中实而两弱”的结构，好比骨架中段刚强但两头支撑不足，因此一旦负荷过重，中心屋梁就会弯曲。

  初六“藉用白茅，无咎”提供了在大过开端的处理方式：在一切之下加一层柔软洁净的垫层，象征在制度和行动之上加一层敬畏与谨慎，使得即便承载过重也不至立刻崩坏。九二“枯杨生稊，老夫得其女妻；无不利”则象征在旧有结构上出现新芽、新配对，看似皆利，但内在仍有“过”的隐忧。

  九三“栋桡，凶”为全卦关键：当中梁弯曲之象出现时，意味着系统已处极限，继续加码势必凶险。九四“栋隆，吉；有它，吝”表示通过调整支撑，使屋梁隆起而不再下垂，可以转危为安，但若在此基础上再谋“其他欲求”，则会有可惜之失。九五“枯杨生华，老妇得其士夫；无咎无誉”显示一种勉力维持的状态：关系虽成，但难以久长，既无大祸，也难言光荣。

  上六“过涉，灭顶，凶，无咎”总结全卦：在大过终局，由于环境所逼不得不涉险，水深已至顶上，局部必凶；但在更高一层看，行此之人或许只是结构性大过中的一环，并非其咎所在，故曰“无咎”。"""
    normalized_text_zh: str = """"""
    subject: str = "大过卦（䷛）"
    factor_refs: list = ['zhouyi_gua_daguo']
    
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
        l1_anchor="zy_v1.0.0_大过卦_001_L1",
    )
    version: str = "1.0.0"
