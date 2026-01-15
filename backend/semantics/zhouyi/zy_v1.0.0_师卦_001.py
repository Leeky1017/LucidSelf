"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899753
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
    semantic_id="zy_v1.0.0_师卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 师卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  师：贞，丈人吉，无咎。

  【爻辞】
  初六，师出以律，否臧凶。
  九二，在师中，吉，无咎；王三锡命。
  六三，师或舆尸，凶。...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  师：贞，丈人吉，无咎。

  【爻辞】
  初六，师出以律，否臧凶。
  九二，在师中，吉，无咎；王三锡命。
  六三，师或舆尸，凶。
  六四，师左次，无咎。
  六五，田有禽，利执言，无咎；长子帅师，弟子舆尸，贞凶。
  上六，大君有命，开国承家，小人勿用。

  【彖传】
  《彖》曰：师，众也；贞，正也。能以众正，可以王矣。
  刚中而应，行险而顺，以此毒天下，而民从之，吉又何咎矣！

  【象传】
  《象》曰：地中有水，师；君子以容民畜众。

- 分字分词释义：

  - 师：卦名，意为军队、众人，也可引申为领众而行之事。
  - 贞：正、正固，强调用兵之道必须合乎正义。
  - 丈人：德高望重的长者，比喻有德有经验的统帅。
  - 师出以律：军队出征依照法度与纪律行事。
  - 否臧凶：好坏混杂则凶，指军纪不明则有凶祸。
  - 在师中：处于军队之中，位置得当、角色适宜。
  - 王三锡命：君王多次赐予命令与赏赐，象征宠信与重任。
  - 师或舆尸：军队可能载着尸体而归，比喻战事失败或损失惨重。
  - 左次：向左侧安营、退居一旁，象征暂缓前进、调整部署。
  - 田有禽，利执言：打猎有所获，利于提出意见与主张。
  - 长子帅师：强健有德者统帅军队。
  - 弟子舆尸：年幼或资浅者却承担运尸之事，象征任用不当。
  - 大君有命，开国承家：君王下令分封诸侯，开国建家。
  - 小人勿用：不可任用品行不端之人，以免祸乱邦国。
  - 地中有水：下坎为水，上坤为地，象征地中蓄水、众聚而未发。
  - 容民畜众：宽容百姓、养育众人，指治理民众之道。

- **规范化释义（primary_lang_explained）**：

  师卦讲的是“用众与用兵之道”。卦辞“师：贞，丈人吉，无咎”指出，用兵必须立于正道，统帅宜由德高望重之人担当，如此方可吉而无咎。师卦并非鼓励好战，而是强调在不得不用众时，应遵循正义与节制，确保军队的行动服务于秩序与民生，而非私欲。

  六爻分别刻画了用师过程中不同角色与局面：初六“师出以律，否臧凶”强调军队一出，必须以纪律为先；若赏罚不明、好坏混杂，则必有凶祸。九二“在师中，吉，无咎；王三锡命”象征居中正之位、能力与德行皆可承命者，能在军中得吉、受重用。六三“师或舆尸，凶”提醒在中下之位若缺乏德才，易导致军旅无功而有伤亡。六四“师左次，无咎”讲在形势不利或时机未到时，主动退居一侧、暂缓进军可免于灾祸。六五“田有禽，利执言，无咎；长子帅师，弟子舆尸，贞凶”一方面指出用兵得当可以有所获，一方面警示指挥者选择将领与分配职责必须得其当位，否则虽守贞亦凶。上六“大君有命，开国承家，小人勿用”则强调用兵成功之后的封赏与分封也需谨慎，不可任用小人，以免乱邦。

  彖传以“师，众也；贞，正也。能以众正，可以王矣”指出：真正的“师道”在于以正统御众人，在险中行事而能保持顺势与合德，方能成王业。象传“地中有水，师；君子以容民畜众”提醒君子以容纳与养育的姿态对待民众，军队乃治理之器，而非统治之玩物。


- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Song, "Conflict" or "Litigation", addresses how to avoid, handle, and resolve disputes in the midst of disagreement. The Judgment "Song: having sincerity yet being constrained; being vigilant brings centrality and good fortune, but ending brings misfortune; it is favorable to see the great person, not favorable to cross the great water" establishes the basic principle for handling conflict: even if one's position is correct, litigation cannot be prolonged; one should seek resolution through a just and impartial great person rather than pursue victory at all costs. The Image "heaven and water move in contrary directions, Song; the noble person thereby plans the beginning when undertaking affairs" points to the root of litigation: upper and lower moving in opposite directions, directions not unified; if the noble person wishes to avoid litigation, the key is to "plan the beginning when undertaking affairs"—clarify direction and define responsibilities from the very start, preventing disputes at the source.

- 核心要点：

  - 师卦重在“用众须合乎正”，并以德高望重者为统帅，方能吉而无咎。
  - 六爻刻画从军纪、将帅、退守、用人、分封等多个维度的用兵之道，强调知进退、慎用人。
  - 兵器与军队始终是为护国安民而设，若为私欲而用，必致“舆尸”“小人乱邦”等凶象。

- 详细解说：

  师卦在结构上为坤上坎下：地中有水，水众而未散，象征民众聚集与力量蓄积。此时最大的课题不是如何煽动众人，而是如何安顿、引导与约束这股力量。卦辞强调“贞，丈人吉，无咎”，指出必须由有德之“丈人”主其事，即具备长远眼光与深厚德性的人。

  爻辞中对“律”的强调在初爻即出现：师出以律，说明在最初阶段就需确立清晰纪律，这与现代组织管理同样相通。九二居中而承上，是执行力与中枢的象征，“王三锡命”反映出在合德之人身上，权力与责任都会不断加码。六三处偏且柔，故有“师或舆尸，凶”的危险，提醒在关键岗位上如果是能力不足或德行不备之人，容易使集体付出沉重代价。

  六四“师左次，无咎”给出了战略退却的一种范式：在不利局势下，主动撤步或变阵并非怯懦，而是一种符合时势的智慧选择。六五则于“田有禽，利执言”中表达“得禽”与“执言”的结合：打猎、用兵都需精准判断，敢于发言者若立足于中正，则其建议可使行动无咎；但若用人失当，“长子帅师，弟子舆尸”便显示了权责倒置、用人不当导致的凶象。上六则将视角拉回到胜利之后的“分配环节”：大君有命、开国承家之后，若再用小人，则此前所有的军功都可能转为祸源。

  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "师卦（䷆）"
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
        l1_anchor="zy_v1.0.0_师卦_001_L1",
    )
    version: str = "1.0.0"
