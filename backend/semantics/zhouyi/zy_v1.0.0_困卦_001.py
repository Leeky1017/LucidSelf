"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919423
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
    semantic_id="zy_v1.0.0_困卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 困卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  困：亨；贞，大人吉，无咎；有言不信。

  【彖传】
  《彖》曰：“困，刚掩也。险以说，困而不失其所亨，其唯君子乎？贞，大人吉，以刚...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  困：亨；贞，大人吉，无咎；有言不信。

  【彖传】
  《彖》曰：“困，刚掩也。险以说，困而不失其所亨，其唯君子乎？贞，大人吉，以刚中也。有言不信，尚口乃穷也。”

  【象传】
  《象》曰：泽无水，困；君子以致命遂志。

  【爻辞】
  初六，臀困于株木，入于幽谷，三岁不觌。
  九二，困于酒食，朱绂方来；利用享祀，征凶，无咎。
  六三，困于石，据于蒺藜；入于其宫，不见其妻，凶。
  九四，来徐徐，困于金车，吝，有终。
  九五，劓刖，困于赤绂；乃徐有说，利用祭祀。
  上六，困于葛藟，于臲卼；曰动悔，有悔，征吉。

- 分字分词释义：

  - **困**：困窘、受困之意，可指物质匮乏、处境受阻、心志受压，也可指局势被包围难以展开。
  - **亨；贞，大人吉，无咎**：在困境之中仍有“亨”的可能，但前提是守正（贞）并有“大人”之德行与格局，方能吉而无咎。
  - **有言不信**：即便有合乎道理的言语、忠告，也一时不被采纳，提示“困”中常有沟通受阻、信息失灵的成分。
  - **刚掩也**：阳刚之气被阻掩，不能畅行，比喻有能力者受压制、不得其用。
  - **险以说**：下坎为险，上兑为悦，在险中而仍须保持“兑说”的和悦与信心，是困中不失其亨的关键。
  - **泽无水**：兑本为泽、水，此卦之象却是“泽中无水”，外表仍是泽，内部已经枯竭，象征资源、情绪、信任被消耗殆尽的困局。
  - **致命遂志**：在困境中仍以生命所系之志向为重，“致命”并非轻生，而是把“该做之事”贯彻到底。
  - **臀困于株木**：臀部卡在树桩上，动弹不得，形容在低位受困、进退不得。
  - **幽谷，三岁不觌**：退入幽深山谷，经年累月不与外界相见，象征被动隐退或长期边缘化。
  - **困于酒食，朱绂方来**：困在酒食匮乏的境地，朱绂（红色官服）却将至，预示困中有机。
  - **石、蒺藜**：石坚难移，蒺藜多刺，比喻处处磕绊、难以下脚之位。
  - **金车**：贵重的车，象征身份与资源本来不低，却仍陷于缓慢与窒碍。
  - **劓刖，困于赤绂**：刑罚（割鼻、断足）与赤色礼服并见，象征功名与创伤并存的矛盾状态。
  - **葛藟、臲卼**：葛藟蔓缠绕，臲卼为不稳之状，形容被纠缠于不稳之局，动静两难。

- **规范化释义（primary_lang_explained）**：

  困卦专门讨论“如何在困境中保住可通之道”。卦辞说：“困：亨；贞，大人吉，无咎；有言不信。”——困并不等于绝路，只是“亨”被包裹起来，不容易被看见。若能在困中守正，并具“大人”之德与视野，仍可趋吉无咎；但一大现实是：在困境中，言语往往不足以打动众人，“有言不信”，也构成困的一部分。

  彖传以“刚掩也，险以说”点明结构：内坎为险，外兑为说，阳刚之才被险与形势所掩，君子若能在险中保持和悦，不失其应得之亨，便是“困而不失其所亨”。“有言不信，尚口乃穷也”则提醒：若只依赖口舌，不辅以实际德行与担当，终会穷尽，困境难解。

  象传“泽无水，困；君子以致命遂志”给出一幅图像：原该充满水的泽已枯竭，只剩外形而无内容。君子对此的应对不是逃避，而是“致命遂志”——在承认现实困窘的同时，把“该完成的志业”坚持到底。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Kun (Oppression) addresses 困顿穷厄. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 困卦的核心是**“在资源枯竭、沟通受阻时，如何不丢失可通之道”**。
  - 卦辞并未否定“亨”，只是把条件收紧到“贞、大人”——仅有口舌说辞远远不够。
  - 爻辞展开了多种困境形态：低位之困、享乐之困、家庭关系之困、身份资源之困、荣辱交织之困、纠缠不稳之困。

- 详细解说：

  卦象为上兑下坎：坎为水、为险，兑为泽、为悦；“泽无水”即下之水被困，泽象空存。与萃卦的“泽上于地”相比，这里强调的是“形在而实无”：结构尚在，内容已枯。

  初六“臀困于株木，入于幽谷，三岁不觌”象征低位之人被卡在局部结构里，活动空间极小，只能退入幽处，长久与主流隔绝。此困的风险在于：退得太深，迟迟不出，则三年不见天地。

  九二“困于酒食，朱绂方来；利用享祀，征凶，无咎”则呈现另一种困：物质困乏之时，反而有官服（朱绂）将至——外在荣誉接近之际，仍须保持“利用享祀”的敬畏与节制，不可轻易出征行事，否则虽终无大咎，过程却有凶险。六三“困于石，据于蒺藜；入于其宫，不见其妻，凶”则将困转向关系与归属：在内外皆刺的格局中，即便回到“自己的宫室”，也见不到“应有的亲密关系”，是一种在家亦无归依的凶困。

  九四“来徐徐，困于金车，吝，有终”显示中层之困：有金车之贵，却行进缓慢，被重物与身份拖累。若能在迟缓中保持节制，仍可“有终”；但其间难免“吝”，即难免有可惜之处。九五“劓刖，困于赤绂；乃徐有说，利用祭祀”则点明高位之困：身受劓刖之辱，却又裹于赤绂之尊，功与过、名与刑交缠。唯有缓缓化解、重新通过“祭祀”这种对上对内的自省仪式，才能逐渐恢复“说”（悦）。

  上六“困于葛藟，于臲卼；曰动悔，有悔，征吉”收束全卦：被葛藟所缠，又立于臲卼不稳之地，此时“动”与“不动”都有悔恨的可能，但若能清醒地识别并承认这份悔意，选择在困中仍迈出应有之步，则“征吉”——在困中启程，可能是唯一的出路。


#### L2 语义提取

- **主题**：困顿穷厄，如何在此情境中顺应天道、把握时机、实现人生目标。

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_425]` `[trigger: 卦=困 AND 卦辞=亨贞大人吉]` `[factor_trigger: zhouyi_gua_kun2 AND zhouyi_guaci]` `[role: 主干]` 困，亨；贞大人吉：困境之中，大人守正可吉。 → 《周易·困卦·卦辞》
  - `[ns_zhouyi_426]` `[trigger: 卦=困 AND 彖传]` `[factor_trigger: zhouyi_gua_kun2 AND zhouyi_tuan AND zhouyi_kunnan_chengdu]` `[role: 主干依赖]` 刚掩也。险以说。 → 《周易·困卦·彖传》
  - `[ns_zhouyi_427]` `[trigger: 卦=困 AND 象传=泽无水困]` `[factor_trigger: zhouyi_gua_kun2 AND zhouyi_xiang]` `[role: 主干依赖]` 泽无水，困；君子以致命遂志：泽竭而困，君子以志遂命。 → 《周易·困卦·象传》
  - `[ns_zhouyi_428]` `[trigger: 卦=困 AND 初六=臀困于株木]` `[factor_trigger: zhouyi_gua_kun2]` `[role: 条件分支]` 臀困于株木，入于幽谷：困于枯木，陷入幽谷。 → 《周易·困卦·爻辞》
  - `[ns_zhouyi_429]` `[trigger: 卦=困 AND 九二=困于酒食]` `[factor_trigger: zhouyi_gua_kun2]` `[role: 条件分支]` 困于酒食，朱绂方来：虽困于酒食，赤绂将至。 → 《周易·困卦·爻辞》
  - `[ns_zhouyi_430]` `[trigger: 卦=困 AND 六三=困于石据于蒺藜]` `[factor_trigger: zhouyi_gua_kun2]` `[role: 例外处理]` 困于石，据于蒺藜：前困于石，后倚蒺藜。 → 《周易·困卦·爻辞》
  - `[ns_zhouyi_431]` `[trigger: 卦=困 AND 九四=来徐徐]` `[factor_trigger: zhouyi_gua_kun2]` `[role: 条件分支]` 来徐徐，困于金车：缓缓而来，困于金车。 → 《周易·困卦·爻辞》
  - `[ns_zhouyi_432]` `[trigger: 卦=困 AND 九五=劓刖困于赤绂]` `[factor_trigger: zhouyi_gua_kun2]` `[role: 主干依赖]` 劓刖，困于赤绂：刑罚施身，困于爵禄。 → 《周易·困卦·爻辞》
  - `[ns_zhouyi_433]` `[trigger: 卦=困 AND 上六=困于葛藟]` `[factor_trigger: zhouyi_gua_kun2]` `[role: 总结]` 困于葛藟，于臲卼：困于藤蔓，摇摇欲坠。 → 《周易·困卦·爻辞》
  - **中文**：
  - 卦辞"困：亨；贞，大人吉，无咎；有言不信"依通行王弼本；"困"为困穷，兑泽在上、坎水在下。
  - "泽无水"谓兑泽在坎水之上，泽中无水，象征资源枯竭、处境困穷。
  - "致命遂志"谓君子在困境中舍命以遂其志，不改其道。
  - "有言不信"谓困中言语不被人信任，故宜少言多行。
  - "困于株木/幽谷/石/蒺藜/金车/赤绂/葛藟"六爻以不同困境为喻，由浅入深。
  - "劓刖"为割鼻砍足之刑；"赤绂"为赤色官服，刑罚与爵禄皆可为困。
  - "葛藟"为野葡萄藤，"臲卼"为动摇不安貌，困极而摇摇欲坠。
  - **English**: Based on Wang Bi commentary edition. "困" means exhaustion/entrapment. "泽无水" shows dry marsh—resources depleted. "致命遂志" means sacrificing life for aspiration. "有言不信" warns words won't be trusted. Various困 imagery shows deepening entrapment."""
    normalized_text_zh: str = """"""
    subject: str = "困卦（䷮）"
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
        l1_anchor="zy_v1.0.0_困卦_001_L1",
    )
    version: str = "1.0.0"
