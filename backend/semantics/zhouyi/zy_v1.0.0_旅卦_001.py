"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919508
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
    semantic_id="zy_v1.0.0_旅卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 旅卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  旅，小亨。旅贞吉。

  【彖传】
  《彖》曰：“旅，小亨，柔得中乎外而顺乎刚，止而丽乎明，是以小亨，旅贞吉也。旅之时义大矣哉！”
...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  旅，小亨。旅贞吉。

  【彖传】
  《彖》曰：“旅，小亨，柔得中乎外而顺乎刚，止而丽乎明，是以小亨，旅贞吉也。旅之时义大矣哉！”

  【象传】
  《象》曰：山上有火，旅；君子以明慎用刑，而不留狱。

  【爻辞】
  初六，旅琐琐，斯其所取灾。
  六二，旅即次，怀其资，得童仆贞。
  九三，旅焚其次，丧其童仆，贞厉。
  九四，旅于处，得其资斧，我心不快。
  六五，射雉，一矢亡；终以誉命。
  上九，鸟焚其巢，旅人先笑后号咷；丧牛于易，凶。

- 分字分词释义：

  - **旅**：行旅、在外寄居之意，引申为身在他乡、根基不定的状态。
  - **小亨**：在旅途或漂泊状态中，只宜求“小亨”——小有通达，不可贪大功。
  - **旅贞吉**：在旅中仍能守贞守正，则可得吉，强调“身在客位而不失其节”。
  - **山上有火**：下艮为山，上离为火，火在山上，易熄不固，比喻处境暴露、基础不深。
  - **慎用刑，而不留狱**：明察而谨慎用刑，不拖延狱讼，暗示在权力与判断上，应如旅者般知所轻重、不过度滞留。
  - **旅琐琐**：旅途之人举止琐碎、拘谨小气，处处计较，易自取灾患。
  - **次**：旅舍、驻地，“旅即次”即安顿在临时住所。
  - **怀其资，得童仆贞**：怀抱旅资，得可信的童仆，共同守贞，比喻妥善管理资源与伙伴。
  - **焚其次**：旅舍被焚，比喻临时立足点被毁。
  - **资斧**：行旅所需的资财与工具，“得其资斧”指基本物资具备。
  - **号咷**：大声号哭，情绪极度崩溃之状。
  - **丧牛于易**：在平易之地丢失牛，比喻在看似不难处境中因大意而失去根本依托。

- **规范化释义（primary_lang_explained）**：

  旅卦论的是“人在异乡、客位之中如何行事”。卦辞曰：“旅，小亨。旅贞吉。”——在旅途与寄居状态下，只宜求小有通达，不宜贪大成功；若能在他乡仍守正，则可得吉。

  彖传抓住旅卦的结构：柔爻得中而居外位，顺从刚爻之主；艮为止、离为明，“止而丽乎明”，是在不稳之地借明德为依托。旅者没有长久根基，因此更要依靠节制、自持与清明的判断，顺势而行，方能“小亨而不败”。“旅之时义大矣哉！”指出：几乎人人都会处于“旅”的时段，这不仅是地理上的远行，也是人生阶段中“无可久留之处”的共同经验。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Lv (Traveling) addresses 羁旅飘零. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - **旅卦核心是“在客位中守分而行”**：不以暂时之势妄自尊大，也不因环境卑微而自轻。
  - **只宜“小亨”而不宜“大亨”**：在旅中求大功、立大业，多招风险；安分守正、妥善安顿，才是真吉。
  - **各爻通过“旅琐琐”“焚其次”“丧牛于易”等象，展示从小心计较到根基尽毁的多种旅途风险**。

- 详细解说：

  卦象为上离下艮：山上有火，火光一时明亮，却因身处高处而难以久续，恰如旅者在异乡的短暂停留。与丰卦的“雷电皆至”相比，旅卦更多是个体层面的移动与不安定，而非整体局势的极盛。

  初六“旅琐琐，斯其所取灾。”是对旅途心态的首要警告：若在他乡处处计较、斤斤自保，反而容易激起他人反感，自招灾祸。六二“旅即次，怀其资，得童仆贞。”则呈现旅中的相对理想状态：找到合适的住处，妥善保管旅资，又得可信赖的同伴，虽仍在客位，却已相对安稳。

  九三“旅焚其次，丧其童仆，贞厉。”转而描绘旅中严重变故：旅舍被焚、童仆失散，即便内心仍守贞，处境已极其危厉。此爻提醒，在不稳根基上积累太多依赖，一旦环境有变，损失远超预期。九四“旅于处，得其资斧，我心不快。”则象征旅者在中位仍感不安：虽得所需资斧，却对所处环境与关系隐有芥蒂，提示“资源充足不等于心安”，仍需调适心态与位置。

  六五“射雉，一矢亡；终以誉命。”描绘旅途中的机会与风险：一箭射雉，却丢失其矢，虽有所得亦有所失；但最终因处理得宜，反以“誉命”收场，说明在他乡表现中庸而有节，可以赢得好名声。上九“鸟焚其巢，旅人先笑后号咷；丧牛于易，凶。”则是旅卦的极端图景：鸟巢被烧，旅人本以为与己无关而先笑，旋即因局势蔓延到自己身上而号哭；在平易之地丢失牛，更暴露出大意与轻心之祸。旅者若到此地步，已难言不凶。


#### L2 语义提取

- **主题**：羁旅飘零，如何在此情境中顺应天道、把握时机、实现人生目标。

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_506]` `[trigger: 卦=旅 AND 卦辞=小亨旅贞吉]` `[factor_trigger: zhouyi_gua_lv2 AND zhouyi_guaci]` `[role: 主干]` 旅，小亨；旅贞吉：羁旅之时，小事亨通。 → 《周易·旅卦·卦辞》
  - `[ns_zhouyi_507]` `[trigger: 卦=旅 AND 彖传]` `[factor_trigger: zhouyi_gua_lv AND zhouyi_tuan]` `[role: 主干依赖]` 小亨。柔得中乎外而顺乎刚。 → 《周易·旅卦·彖传》
  - `[ns_zhouyi_508]` `[trigger: 卦=旅 AND 象传=山上有火]` `[factor_trigger: zhouyi_gua_lv2 AND zhouyi_xiang]` `[role: 主干依赖]` 山上有火，旅；君子以明慎用刑而不留狱：旅途明慎，不滞狱事。 → 《周易·旅卦·象传》
  - `[ns_zhouyi_509]` `[trigger: 卦=旅 AND 初六=旅琐琐]` `[factor_trigger: zhouyi_gua_lv2]` `[role: 例外处理]` 旅琐琐，斯其所取灾：旅途琐碎，自招其灾。 → 《周易·旅卦·爻辞》
  - `[ns_zhouyi_510]` `[trigger: 卦=旅 AND 六二=旅即次]` `[factor_trigger: zhouyi_gua_lv2]` `[role: 条件分支]` 旅即次，怀其资，得童仆贞：旅至客舍，财资在身。 → 《周易·旅卦·爻辞》
  - `[ns_zhouyi_511]` `[trigger: 卦=旅 AND 九三=旅焚其次]` `[factor_trigger: zhouyi_gua_lv2]` `[role: 例外处理]` 旅焚其次，丧其童仆：客舍被焚，失其仆从。 → 《周易·旅卦·爻辞》
  - `[ns_zhouyi_512]` `[trigger: 卦=旅 AND 九四=旅于处]` `[factor_trigger: zhouyi_gua_lv2]` `[role: 条件分支]` 旅于处，得其资斧：旅居一处，得财得器。 → 《周易·旅卦·爻辞》
  - `[ns_zhouyi_513]` `[trigger: 卦=旅 AND 六五=射雉一矢亡]` `[factor_trigger: zhouyi_gua_lv2]` `[role: 主干依赖]` 射雉，一矢亡：射雉失矢，有所损失。 → 《周易·旅卦·爻辞》
  - `[ns_zhouyi_514]` `[trigger: 卦=旅 AND 上九=鸟焚其巢]` `[factor_trigger: zhouyi_gua_lv2]` `[role: 总结]` 鸟焚其巢，旅人先笑后号啕：鸟巢被焚，先笑后哭。 → 《周易·旅卦·爻辞》
  - **中文**：
  - 卦辞"旅：小亨。旅贞吉"依通行王弼本；"旅"指羁旅、客居，非大事可成，故仅"小亨"。
  - "山上有火"谓离火在艮山之上，火过则尽，不能久留，象征旅途无常。
  - "旅琐琐"之"琐琐"释为琐碎、卑小，旅途中斤斤计较、心态卑琐，自招其灾。
  - "旅即次"之"次"为客舍、旅馆；"怀其资"谓怀藏财物；"得童仆贞"谓得忠诚仆从。
  - "旅焚其次"谓客舍失火被焚，"丧其童仆"谓失去仆从，皆为旅途之险。
  - "鸟焚其巢，旅人先笑后号啕"谓旅途如鸟栖无定，一旦失所，由笑转哭。
  - **English**: Based on Wang Bi commentary edition. "旅" means travel/sojourning—only small success possible. "次" means inn/lodging. "琐琐" indicates petty/trivial attitude. "焚其次/巢" describe losing lodging. "先笑后号啕" shows fortune reversal."""
    normalized_text_zh: str = """"""
    subject: str = "旅卦（䷷）"
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
        l1_anchor="zy_v1.0.0_旅卦_001_L1",
    )
    version: str = "1.0.0"
