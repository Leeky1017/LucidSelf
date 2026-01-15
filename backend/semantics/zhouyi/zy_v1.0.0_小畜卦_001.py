"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899773
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
    semantic_id="zy_v1.0.0_小畜卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 小畜卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  小畜：亨。密云不雨，自我西郊。

  【彖传】
  《彖》曰：“小畜”，柔得位而上下应之，曰小畜。
  健而巽，刚中而志行，乃亨。
 ...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  小畜：亨。密云不雨，自我西郊。

  【彖传】
  《彖》曰：“小畜”，柔得位而上下应之，曰小畜。
  健而巽，刚中而志行，乃亨。
  “密云不雨”，尚往也；“自我西郊”，施未行也。

  【象传】
  《象》曰：风行天上，小畜；君子以懿文德。

  【爻辞】
  初九，复自道，何其咎？吉。
  九二，牵复，吉。
  九三，舆说辐，夫妻反目。
  六四，有孚；血去惕出，无咎。
  九五，有孚挛如，富以其邻。
  上九，既雨既处，尚德载；妇贞厉，月几望；君子征凶。

- 分字分词释义：

  - 小畜：卦名，“畜”有蓄积、蕴养之意；与大畜相比，重在“小规模的积聚与约束”。
  - 亨：通达、顺利，但在本卦中带有“以小蓄成大亨”的意味。
  - 密云不雨：云气聚集而暂未降雨，象征条件已备而效果未显。
  - 自我西郊：从自身所在之西郊起，暗示尚处边缘、施泽未及中土。
  - 健而巽：下乾为健，上巽为顺，内刚外柔。
  - 刚中而志行：阳爻居中得正，其志可以实行。
  - 复自道：返回自身本来的正道。
  - 牵复：被牵引而一同返回，比喻相互影响而回到正轨。
  - 舆说辐：车轮辐条脱落，象征结构松散、关系反目。
  - 夫妻反目：最亲近关系出现对立与不和。
  - 有孚：内怀诚信、信任。
  - 血去惕出：血去，伤害消除；惕出，恐惧逐渐消退。
  - 挛如：相互牵系、缠绕，象征密切相连。
  - 富以其邻：以自身财富惠及邻人，不独自享受。
  - 既雨既处：雨已落下且停止，蓄积释放而趋于平稳。
  - 尚德载：尊崇德行，以德承载众务。
  - 月几望：月亮将满未满，象征接近极点的状态。

- **规范化释义（primary_lang_explained）**：

  小畜卦讲的是“小规模蓄积与约束”的过程。卦辞说“亨”，说明整体趋向是可通达的，但“密云不雨，自我西郊”指出目前仍处在能量聚集而尚未显效的阶段：条件具备、云气已成，却还未降雨；影响范围也只在“西郊”之域，尚未深入腹地。彖传以“柔得位而上下应之，小畜”说明此时是以柔顺之力居要位、驾驭众阳；下健上巽，内刚外柔，使得“刚中志行”而得以亨通，但这一亨需要时间与节制才能显现。

  六爻刻画小畜发展中的不同姿态：初九“复自道，何其咎？吉”，强调在初始阶段若能自觉回到本来正道，自然无咎而吉；九二“牵复，吉”，则描写中位之阳受到初九影响而一同复道，强调良性牵引在集体中的作用。九三“舆说辐，夫妻反目”是对“蓄而不通”的警示：结构松散、沟通不良会导致亲密关系失衡。六四“有孚；血去惕出，无咎”，表现出在阴柔位置上以诚信化解冲突，逐渐让伤害与恐惧消散；九五“有孚挛如，富以其邻”把这种信任扩展为互惠关系——以自己的富足惠及邻里，形成良性网络。上九“既雨既处”则提醒我们：能量终究会释放，雨既下、情势已变之后，若仍依旧激烈推进，就会像“月几望”那样逼近极限，导致“君子征凶”。因此，小畜之道的成熟形态是：在合适时机适度释放，而非永远积压或突然过度爆发。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Xiao Chu, "Lesser Accumulation/Restraint", describes a phase in which power and resources are being gathered in small increments while still held in check. The Judgment says, "Xiao Chu: success. Dense clouds yet no rain, arising from our western outskirts." This image shows that conditions are already coming together—clouds are full—but the rain has not yet fallen, and the influence is still confined to the outskirts rather than reaching the center. The Tuan commentary explains that a gentle Yin line in a key position restrains and guides the strong Yang lines below; inwardly we have the firmness of Qian (Heaven), outwardly the yielding of Xun (Wind). Strength is thus directed by flexibility, so it can eventually bring success, but only through patience, gradual cultivation, and appropriate limitation.

  The six lines portray different attitudes toward this accumulated but delayed potential. The first and second lines, "return by ones own path" and "being drawn back in return", show how an initial act of self-correction can pull others back to the right way, creating a chain of gentle adjustment. The third line, "the carriage loses its spokes; husband and wife turn against each other", warns that when structure falls apart and communication breaks down, stored energy turns into conflict instead of progress. The fourth line, "with trust, blood departs and fear leaves", shows a soft position dissolving hurt and fear through sincerity; the fifth line, "with trust bound together, wealthy in his neighbors", elevates this into a network of mutual benefit, where one persons abundance naturally extends to those around him. The top line, "already raining, already at rest", reminds us that accumulation must at some point be released: once the rain has fallen and the situation has shifted, one should rest on virtue rather than continue to push forward. At the moment "the moon is nearly full", any further advance courts danger. In practice, Xiao Chu points to projects, relationships, or states of mind in a gestation and fine-tuning phase, where building trust, strengthening structure, and making small, precise adjustments matter more than forcing big, immediate outcomes.

- 核心要点：

  - 小畜不是“不能大作为”，而是强调在尚未成熟阶段，通过小规模蓄积与节制来准备大通。
  - 卦辞中的“密云不雨，自我西郊”提示：条件趋近成熟但未到爆发点，此时宜内修德行、稳固关系。
  - 各爻围绕“复道、牵复、反目、有孚、挛如、既雨既处”等意象，呈现从自我纠偏到关系牵引、从冲突到信任再到释放的过程。
  - 对应用而言，小畜常对应项目、关系或心态中的“能量累积期”：要重视细微调整与信任网络的构建，而非急于见大成果。

- 详细解说：

  从卦象看，小畜为“风行天上”：乾为天在下，巽为风在上，风在天上吹拂却尚未带来降雨，好比理念、计划在精神层面已不断酝酿，实际落地与资源释放仍在等待时机。柔得位而上下应之，说明当前局面由柔顺者居中调度阳刚之力，这是一种“以柔制刚”“以阴畜阳”的局势，宜用温和而持续的方式来管理积聚的能量。

  初九与九二共同构成“复道—牵复”的双联：一个主动回归正道，另一个在牵引下随之回归，暗示在团队或关系中，一个人对原则的坚持可以对周围产生连锁修正效应。九三“舆说辐，夫妻反目”则是蓄而不通的反面教材：当载体结构松散、沟通断裂时，即使资源在手，也会因内耗而失去前进能力。六四“有孚；血去惕出，无咎”表明在中上位置的阴柔角色，若以真诚与审慎处理矛盾，可以逐步化解积怨与恐惧，避免事态扩大。

  九五“有孚挛如，富以其邻”是小畜卦的关键所在：真正的“畜”不仅是自我储蓄，更是形成互惠网络——以信任为纽带，让富足溢出到邻里，使整体系统更稳固。上九“既雨既处”则说明蓄积终将释放，雨既降而复止，此时应以德承载而非再行征伐；若在“月几望”的临界点仍执意前行，则有凶险。

  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "小畜卦（䷈）"
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
        l1_anchor="zy_v1.0.0_小畜卦_001_L1",
    )
    version: str = "1.0.0"
