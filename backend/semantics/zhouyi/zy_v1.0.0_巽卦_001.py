"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919517
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
    semantic_id="zy_v1.0.0_巽卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 巽卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  巽：小亨。利有攸往，利见大人。

  【彖传】
  《彖》曰：“重巽以申命，刚巽乎中正而志行，柔皆顺乎刚。是以小亨，利有攸往，利见大人...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  巽：小亨。利有攸往，利见大人。

  【彖传】
  《彖》曰：“重巽以申命，刚巽乎中正而志行，柔皆顺乎刚。是以小亨，利有攸往，利见大人。”

  【象传】
  《象》曰：随风，巽；君子以申命行事。

  【爻辞】
  初六，进退，利武人之贞。
  九二，巽在床下，用史巫纷若，吉，无咎。
  九三，频巽，吝。
  六四，悔亡，田获三品。
  九五，贞吉，悔亡，无不利；无初有终。先庚三日，后庚三日，吉。
  上九，巽在床下，丧其资斧，贞凶。

- 分字分词释义：

  - **巽**：本义为入、顺从，引申为谦逊、委婉、风行之象；卦名中既有“入”的含义，也有“以柔入刚、以顺承命”的意味。
  - **小亨**：略有亨通，并非大亨，提示巽之道适用于细腻渗透、渐进通达，不宜寄望立刻大成。
  - **利有攸往，利见大人**：以巽顺之道有所往行，有利于前往应办之事，也有利于见到“大人”——德位兼备、能主持大事之人。
  - **随风，巽**：风随物形而行，入乎万物之间，比喻影响方式是渗透、弥散，而非正面冲撞。
  - **进退，利武人之贞**：处在进退之间、徘徊不定之际，适宜以“武人之贞”——果决、守纪的态度持守正道。
  - **巽在床下**：在床下而不显于上，象征影响力潜伏、作用隐微；既可为谨慎周到，也可为畏缩不前。
  - **用史巫纷若**：借助史官、巫者以多方陈说、沟通，如同多线并行的说理与仪式，表示在微妙局面中需多层次表达。
  - **频巽**：频繁示弱、过度逢迎，导致失其节度之巽，故为“吝”。
  - **田获三品**：田猎而获三等之物，象征在巽顺中仍能有实在收获，且层次分明。
  - **无初有终；先庚三日，后庚三日**：起初不顺利，但终可善终；“庚日”前后三日，比喻在关键时点前后反复斟酌与调整。
  - **资斧**：资财与工具之总称，丧其资斧即失去赖以行事的资源与手段。

- **规范化释义（primary_lang_explained）**：

  巽卦讲的是“以入、以顺而行事”的方式：如何在多方力量与命令交织之中，通过谦逊、委婉而不失原则地推动事情发展。卦辞曰：“巽：小亨。利有攸往，利见大人。”——以巽顺之道，不必求一举大成，但可以获得小规模的通达；在这样的态度下出行办事，利于有所作为，也利于接近与自己上位的大人。

  彖传说“重巽以申命”，上下皆巽，是反复宣告命令之象；九二、九五刚爻居中，以刚而能巽，志向得以实行，其余柔爻皆顺乎此刚，构成“柔顺围绕刚中”的结构。因此，巽卦的“顺”并非无原则的退让，而是在有中正之纲领的前提下，灵活渗透与调整。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Xun (Gentle/Wind) addresses 巽顺入微. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 巽卦核心是**“有原则的入与顺”**：在大方向不变的前提下，以柔入刚、以谦顺达成沟通与落实。
  - 卦辞“小亨”提示巽之通达多在细部与过程，而非立即显现的大功。
  - 各爻通过“巽在床下”“频巽”“田获三品”“丧其资斧”等象，展示从合宜谦顺到过度卑屈、以至资源尽失的连续光谱。

- 详细解说：

  卦象为上巽下巽，风行于风，重巽之象。一方面表示命令、风气、影响力可以层层渗透；另一方面，也提示在这样一个“处处皆风”的情境中，人容易过度随风摇摆，失去自己的定向。君子“以申命行事”，意在反复、清晰地传达大义，使柔顺不至于流于盲从。

  初六“进退，利武人之贞。”处卦之初，面对进退两难，若以柔弱犹豫对待，容易失机；因此特别强调“武人之贞”——在原则上刚毅果决，即便方式上仍可委婉。九二“巽在床下，用史巫纷若，吉，无咎。”则描述一种在内部潜行、借助多种角色沟通的局面：虽不显于台前，却通过史、巫等不同角色多线陈说，仍可达成吉而无咎的结果。

  九三“频巽，吝。”则提示：若一味频频示弱、反复逢迎，以至失去自持，则虽未必立刻招致大凶，已属可羞可惜的“吝”境。六四“悔亡，田获三品。”则转向“以巽行事而有实获”：通过适度的顺从与配合，田猎中得到三品之获，象征在结构中找到合宜位置与层次，悔恨得以消除。

  九五“贞吉，悔亡，无不利；无初有终。先庚三日，后庚三日，吉。”展示巽卦的高位理想：在尊位者若能坚守正道、反复斟酌时机（庚日前后三日），即便开端不顺，终可善终并“无不利”。上九“巽在床下，丧其资斧，贞凶。”则是巽之过度：长期潜伏于床下、畏首畏尾，结果反而失去资财与工具，即便内心自以为守贞，客观上已陷凶境。


#### L2 语义提取

- **主题**：巽顺入微，如何在此情境中顺应天道、把握时机、实现人生目标。

- **自然属性**：

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_515]` `[trigger: 卦=巽 AND 卦辞=小亨利有攸往]` `[factor_trigger: zhouyi_gua_xun AND zhouyi_guaci]` `[role: 主干]` 巽，小亨；利有攸往，利见大人：巽顺入微，利见大人。 → 《周易·巽卦·卦辞》
  - `[ns_zhouyi_516]` `[trigger: 卦=巽 AND 彖传]` `[factor_trigger: zhouyi_gua_xun AND zhouyi_tuan AND zhouyi_shunru_chengdu]` `[role: 主干依赖]` 重巽以申命。 → 《周易·巽卦·彖传》
  - `[ns_zhouyi_517]` `[trigger: 卦=巽 AND 象传=随风巽]` `[factor_trigger: zhouyi_gua_xun AND zhouyi_xiang]` `[role: 主干依赖]` 随风，巽；君子以申命行事：风行相随，申明号令。 → 《周易·巽卦·象传》
  - `[ns_zhouyi_518]` `[trigger: 卦=巽 AND 初六=进退利武人之贞]` `[factor_trigger: zhouyi_gua_xun]` `[role: 条件分支]` 进退，利武人之贞：进退不定，须武人守正。 → 《周易·巽卦·爻辞》
  - `[ns_zhouyi_519]` `[trigger: 卦=巽 AND 九二=巽在床下]` `[factor_trigger: zhouyi_gua_xun]` `[role: 条件分支]` 巽在床下，用史巫纷若：卑顺在下，多用史巫。 → 《周易·巽卦·爻辞》
  - `[ns_zhouyi_520]` `[trigger: 卦=巽 AND 九三=频巽吝]` `[factor_trigger: zhouyi_gua_xun]` `[role: 例外处理]` 频巽，吝：过于卑顺，反生吝惜。 → 《周易·巽卦·爻辞》
  - `[ns_zhouyi_521]` `[trigger: 卦=巽 AND 六四=悔亡田获三品]` `[factor_trigger: zhouyi_gua_xun]` `[role: 条件分支]` 悔亡，田获三品：悔恨消解，田猎有获。 → 《周易·巽卦·爻辞》
  - `[ns_zhouyi_522]` `[trigger: 卦=巽 AND 九五=贞吉悔亡无不利]` `[factor_trigger: zhouyi_gua_xun]` `[role: 主干依赖]` 贞吉，悔亡，无不利：守正则吉，无所不利。 → 《周易·巽卦·爻辞》
  - `[ns_zhouyi_523]` `[trigger: 卦=巽 AND 上九=巽在床下]` `[factor_trigger: zhouyi_gua_xun]` `[role: 总结]` 巽在床下，丧其资斧：过于卑顺，失其资器。 → 《周易·巽卦·爻辞》
  - **中文**：
  - 卦辞"巽：小亨。利有攸往，利见大人"依通行王弼本；"巽"为入、为顺，柔顺入微，故仅"小亨"。
  - "随风巽"谓上下皆巽，风行相随，象征号令层层传达、柔顺渗透。
  - "巽在床下"一语重见于初六与上九，释为过于卑顺，如伏于床下，有失尊严。
  - "用史巫纷若"中"史巫"为掌卜筮祭祀之人，"纷若"为众多貌，示多方求助。
  - "频巽"之"频"释为频繁、再三，过度卑顺反生吝惜之象。
  - "先庚三日，后庚三日"与蛊卦"先甲后甲"相类，以干支纪日示号令更新之时机。
  - **English**: Based on Wang Bi commentary edition. "巽" means entering/yielding—only small success. "随风" means winds following. "床下" indicates excessive humility. "史巫" refers to diviners/shamans. "先庚后庚" parallels 先甲后甲 in timing of decrees."""
    normalized_text_zh: str = """"""
    subject: str = "巽卦（䷸）"
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
        l1_anchor="zy_v1.0.0_巽卦_001_L1",
    )
    version: str = "1.0.0"
