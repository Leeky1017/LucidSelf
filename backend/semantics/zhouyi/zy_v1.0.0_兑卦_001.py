"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919526
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
    semantic_id="zy_v1.0.0_兑卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 兑卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  兑：亨，利贞。

  【彖传】
  《彖》曰：“兑，说也。刚中，而柔外，说以利贞，是以顺乎天，而应乎人。说以先民，民忘其劳；说以犯难，...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  兑：亨，利贞。

  【彖传】
  《彖》曰：“兑，说也。刚中，而柔外，说以利贞，是以顺乎天，而应乎人。说以先民，民忘其劳；说以犯难，民忘其死；说之大，民劝矣哉！”

  【象传】
  《象》曰：丽泽，兑；君子以朋友讲习。

  【爻辞】
  初九，和兑，吉。
  九二，孚兑，吉，悔亡。
  六三，来兑，凶。
  九四，商兑，未宁，介疾有喜。
  九五，孚于剥，有厉。
  上六，引兑。

- 分字分词释义：

  - **兑**：本义为悦、喜悦，亦指泽；卦名中代表以喜悦之道沟通人心。
  - **亨，利贞**：亨通而又利于守贞，说明真正的喜悦应与正道相合，而非放纵。
  - **说也**：说，同“悦”，本卦以“喜悦”作为整卦的核心意象。
  - **刚中，而柔外**：二、五之刚爻居中为内核，三、上之柔爻在外为外层，象征内在有刚正之中，外表以柔和相接。
  - **说以先民 / 说以犯难**：以喜悦、和悦的方式带领人民，或面对艰难时仍以喜悦之心相勉，使民众忘劳、忘死。
  - **丽泽**：两泽相丽，泽泽相连，比喻人与人之间的互相映照与滋润。
  - **和兑 / 孚兑 / 来兑 / 商兑 / 引兑**：一系列关于“兑”的态度：和而不流、以信为本的兑；一味趋向他人的“来兑”；借商谈与权衡维持的兑；以及被牵引、拉扯的兑。
  - **介疾有喜**：介，如介意、介入；疾，为病患。指虽有介意之疾，但由此反而有喜，暗示通过正视问题获取改善。
  - **孚于剥**：在剥夺之境仍存诚信，既有危险之意，也隐含“在困境中仍以诚相待”的张力。

- **规范化释义（primary_lang_explained）**：

  兑卦谈的是“以喜悦为媒介的沟通与感召”。卦辞简言：“兑：亨，利贞。”——喜悦之道若合乎正道，可带来亨通，并有利于守贞。若喜悦脱离正道，则易流于放纵和媚悦。

  彖传指出：兑为“说也”，以喜悦为本；结构上刚在其中、柔在其外，使得“说以利贞”——喜悦与中正相配合，便能顺天应人。以喜悦之心“先民”，人民可以忘却劳苦；以喜悦之心“犯难”，人民可以不惧生死，由此可见“说之大”，即喜悦在组织与激励中的巨大作用。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Dui (Joy/Lake) addresses 悦以刚中. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 兑卦核心是**“中正之中、喜悦在外”**：以刚中为骨、以柔说为用，使人际关系与集体气氛得以调和。
  - 喜悦本身既可为德行之器，也可滑向浅薄媚悦，关键在于是否“利贞”。
  - 爻辞展示从“和兑”“孚兑”的良性喜悦，到“来兑”的趋附、“引兑”的被牵引，以及困境中的“孚于剥”等多重状态。

- 详细解说：

  卦象为上兑下兑，双泽相连，如两湖相接，水面彼此映照，形成“丽泽”的画面。君子“以朋友讲习”：通过朋友间的讨论与学习，以和悦之气氛推进道义，而非以恐惧压迫。

  初九“和兑，吉。”强调的是“和而不流”的兑：在喜悦中保持和谐，不至于失去立场，因此为吉。九二“孚兑，吉，悔亡。”则进一层：在喜悦关系中以诚信为本（孚），既可得吉，又可消除先前的悔恨。

  六三“来兑，凶。”则警示：若只是一味趋向他人的喜悦、被动迎合，而不自持其度，则终致凶险。九四“商兑，未宁，介疾有喜。”描绘的是在商议、权衡中的兑：一开始尚未安宁，内心介意如病，但正因面对这些不适、通过沟通与调整，反而可迎来喜的转机。

  九五“孚于剥，有厉。”显示兑之另一面：在“剥”——资源、支持被剥夺的情境中仍保持诚信，虽然充满危险，但也保留了一线可托付的信任空间。上六“引兑。”则是兑之极端：喜悦不再出自内在中正，而是不断被外在所牵引，随波逐流，容易沦为空洞的讨好或被操纵的情绪，因而为全卦所警惕的终局图景。


#### L2 语义提取

- **主题**：悦以刚中，如何在此情境中顺应天道、把握时机、实现人生目标。

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_524]` `[trigger: 卦=兑 AND 卦辞=亨利贞]` `[factor_trigger: zhouyi_gua_dui AND zhouyi_guaci AND zhouyi_huanle_chengdu]` `[role: 主干]` 兑，亨，利贞：悦泽之道，亨通利贞。 → 《周易·兑卦·卦辞》
  - `[ns_zhouyi_525]` `[trigger: 卦=兑 AND 彖传]` `[factor_trigger: zhouyi_gua_dui AND zhouyi_tuan AND zhouyi_xiyue_chengdu]` `[role: 主干依赖]` 说也。刚中而柔外。 → 《周易·兑卦·彖传》
  - `[ns_zhouyi_526]` `[trigger: 卦=兑 AND 象传=丽泽兑]` `[factor_trigger: zhouyi_gua_dui AND zhouyi_xiang]` `[role: 主干依赖]` 丽泽，兑；君子以朋友讲习：两泽相丽，朋友讲学。 → 《周易·兑卦·象传》
  - `[ns_zhouyi_527]` `[trigger: 卦=兑 AND 初九=和兑吉]` `[factor_trigger: zhouyi_gua_dui]` `[role: 条件分支]` 和兑，吉：和悦待人，自然吉祥。 → 《周易·兑卦·爻辞》
  - `[ns_zhouyi_528]` `[trigger: 卦=兑 AND 九二=孚兑吉]` `[factor_trigger: zhouyi_gua_dui]` `[role: 条件分支]` 孚兑，吉，悔亡：诚信而悦，悔恨消解。 → 《周易·兑卦·爻辞》
  - `[ns_zhouyi_529]` `[trigger: 卦=兑 AND 六三=来兑凶]` `[factor_trigger: zhouyi_gua_dui]` `[role: 例外处理]` 来兑，凶：来求悦人，反招其凶。 → 《周易·兑卦·爻辞》
  - `[ns_zhouyi_530]` `[trigger: 卦=兑 AND 九四=商兑未宁]` `[factor_trigger: zhouyi_gua_dui]` `[role: 条件分支]` 商兑未宁，介疾有喜：商议悦乐，未能安宁。 → 《周易·兑卦·爻辞》
  - `[ns_zhouyi_531]` `[trigger: 卦=兑 AND 九五=孚于剥有厉]` `[factor_trigger: zhouyi_gua_dui]` `[role: 例外处理]` 孚于剥，有厉：信于小人，终有危厉。 → 《周易·兑卦·爻辞》
  - `[ns_zhouyi_532]` `[trigger: 卦=兑 AND 上六=引兑]` `[factor_trigger: zhouyi_gua_dui]` `[role: 总结]` 引兑：引人共悦，牵引其心。 → 《周易·兑卦·爻辞》
  - **中文**：
  - 卦辞"兑：亨，利贞"依通行王弼本；"兑"为悦、为泽，刚中柔外，和悦顺承，故亨通而利守正。
  - "丽泽兑"谓上下皆兑，两泽相连，象征朋友讲习、互相切磋之乐。
  - "和兑"谓以和悦待人；"孚兑"谓以诚信而悦，皆为正面之悦。
  - "来兑"之"来"示主动来求悦人，有谄媚失正之象，故凶。
  - "商兑"之"商"释为商量、计较，悦而商议未能安宁；"介疾有喜"谓介于疾病之间而有喜转。
  - "孚于剥"谓诚信于小人（剥为阴消），有危厉之象。
  - **English**: Based on Wang Bi commentary edition. "兑" means joy/lake—firmness inside, softness outside. "丽泽" means connected lakes. "和兑/孚兑" are proper joy; "来兑" is improper (seeking favor). "商兑" indicates debating joy. "孚于剥" warns of trusting petty people."""
    normalized_text_zh: str = """"""
    subject: str = "兑卦（䷹）"
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
        l1_anchor="zy_v1.0.0_兑卦_001_L1",
    )
    version: str = "1.0.0"
