"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919335
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
    semantic_id="zy_v1.0.0_解卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 解卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  解：利西南。无所往，其来复吉。有攸往，夙吉。

  【彖传】
  《彖》曰：“解，险以动，动而免乎险，解。解，利西南，往得众也；其来复...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  解：利西南。无所往，其来复吉。有攸往，夙吉。

  【彖传】
  《彖》曰：“解，险以动，动而免乎险，解。解，利西南，往得众也；其来复吉，乃得中也；有攸往，夙吉，往有功也。天地解而雷雨作，雷雨作而百果草木皆甲坼。解之时义大矣哉！”

  【象传】
  《象》曰：雷雨作，解；君子以赦过宥罪。

  【爻辞】
  初六，无咎。
  九二，田获三狐，得黄矢，贞吉。
  六三，负且乘，致寇至，贞吝。
  九四，解而拇，朋至斯孚。
  六五，君子维有解，吉，有孚于小人。
  上六，公用射隼于高墉之上，获之，无不利。

- 分字分词释义：

  - **解**：解除、解开、解散之意，也有冬尽冰解、春雷发动、万物解冻之象。
  - **险以动，动而免乎险**：处在险境之中，以合宜之动而脱离险境，因此称为“解”。
  - **利西南**：与蹇卦相应，西南为坤方、为众，向“得众、得地”的方向行动，有利于化险为夷。
  - **无所往，其来复吉**：一时无路可走时，退回原位反而为吉，表示解局也需要懂得退守。
  - **有攸往，夙吉**：若已有合宜之去处，则应尽早前往，拖延反会贻误时机。
  - **雷雨作**：上震为雷，下坎为水，雷与雨并作，象征郁滞之气被打散、万物萌发。
  - **赦过宥罪**：赦免过错、宽恕罪人，是君子用“解”之道调和人心的方式。
  - **田获三狐，得黄矢**：打猎得到三只狐狸，又获黄色箭矢，象征发现多重隐患，并得到中正的矫正工具。
  - **负且乘，致寇至**：身负重物又乘车招摇，自招盗寇，指自身炫耀与不谨慎引来灾祸。
  - **解而拇**：先从脚趾之拘束处解开，比喻从细微之处开始化解问题。
  - **射隼于高墉之上**：在高墙上射下隼鸟，象征对占据高位、为患甚深的顽梗之源，施行果断而精准的处理。

- **规范化释义（primary_lang_explained）**：

  解卦承接蹇卦，讨论的是“如何从艰难危局中解脱出来”。卦辞云：“解：利西南。无所往，其来复吉。有攸往，夙吉。”——在危险之中，如果一时无路可走，则宜退回原位，收缩战线，以求安全；若已有合宜的方向和目标，则宜尽早前往，不可犹豫拖延。整体方向同样偏向“西南”之坤方，象征向众处、向基础处、向柔顺处移动。

  彖传以“险以动，动而免乎险”点明结构：解并不是没有险，而是在险中找到应动之时与应动之法，以动解险。天地之“解”表现为雷雨并作：冰雪消融、草木破土而出，“百果草木皆甲坼”，态势一变，郁结之气便自然疏解。解的关键不在“力大”，而在“时义”——顺时而行，方能大有其用。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Jie (Deliverance) addresses 解脱困境. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 解卦的核心是**“在险中择动，用动来化解”**，介于一味僵止与盲目乱动之间。
  - “无所往，其来复吉”与“有攸往，夙吉”构成一对：无路则宜退守，有路则及早前行，重在识局与择时。
  - 爻辞从“无咎”的起点，到“田获三狐、负且乘致寇至、解而拇、君子有解、公射隼”，展示了从发现问题、避免自招其乱，到循序解缚、终至果断处理的完整路径。

- 详细解说：

  卦象为上震下坎：坎为险、为水，震为雷、为动，雷自险中发出，是“险中有动、动出于险”的图景。与蹇卦“山上有水”的停滞相比，解卦强调在同样有险的状态下，由于出现了合宜的动因和行动者，局势出现转机。

  初六“无咎”象征解局伊始，只要顺势而动、不妄自作为，便可无咎。九二“田获三狐，得黄矢，贞吉”说明：在田猎（事务处理）过程中，能够捕获象征隐患与狡黠的“狐狸”，并获得象征中道之“黄矢”，就能在解决问题时坚持中正之道而获吉。

  六三“负且乘，致寇至，贞吝”是对自招其乱的告诫：在需要化解危险之时，若仍负物乘车、张扬炫显，便是将危险引到自己身上，即使占得贞，也难免有可叹之处。九四“解而拇，朋至斯孚”提示：化解应从最细微处着手——先解除脚趾之拘束，一点一点松动结构，由此也更容易获得朋友的信任与到来。

  六五“君子维有解，吉，有孚于小人”强调：真正的“解”，不仅能令君子得吉，也要让“小人”信服、退避，从而削减阻力，而非制造新的对立。上六“公用射隼于高墉之上，获之，无不利”，则将全卦推向高潮：对于仍盘踞高位、扰乱秩序的“隼”，在合适时机必须由“公”出面，以光明正大的权威手段，一举制伏，这样才能从根本上解除隐患，自然“无不利”。


#### L2 语义提取

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_362]` `[trigger: 卦=解 AND 卦辞=利西南无所往]` `[factor_trigger: zhouyi_gua_jie AND zhouyi_guaci]` `[role: 主干]` 解，利西南；无所往，其来复吉：难解之后，宜归于平。 → 《周易·解卦·卦辞》
  - `[ns_zhouyi_363]` `[trigger: 卦=解 AND 彖传]` `[factor_trigger: zhouyi_gua_jie AND zhouyi_tuan AND zhouyi_jiechu_chengdu]` `[role: 主干依赖]` 险以动，动而免乎险。 → 《周易·解卦·彖传》
  - `[ns_zhouyi_364]` `[trigger: 卦=解 AND 象传=雷雨作解]` `[factor_trigger: zhouyi_gua_jie AND zhouyi_xiang]` `[role: 主干依赖]` 雷雨作，解；君子以赦过宥罪：雷雨解散阴郁，赦免过罪。 → 《周易·解卦·象传》
  - `[ns_zhouyi_365]` `[trigger: 卦=解 AND 初六=无咎]` `[factor_trigger: zhouyi_gua_jie]` `[role: 条件分支]` 无咎：解之初，无所咎。 → 《周易·解卦·爻辞》
  - `[ns_zhouyi_366]` `[trigger: 卦=解 AND 九二=田获三狐]` `[factor_trigger: zhouyi_gua_jie]` `[role: 条件分支]` 田获三狐，得黄矢：解除群狐之患，得正直之器。 → 《周易·解卦·爻辞》
  - `[ns_zhouyi_367]` `[trigger: 卦=解 AND 六三=负且乘]` `[factor_trigger: zhouyi_gua_jie]` `[role: 例外处理]` 负且乘，致寇至：身份错位，招致祸患。 → 《周易·解卦·爻辞》
  - `[ns_zhouyi_368]` `[trigger: 卦=解 AND 九四=解而拇]` `[factor_trigger: zhouyi_gua_jie]` `[role: 条件分支]` 解而拇，朋至斯孚：先解小处，朋友来信。 → 《周易·解卦·爻辞》
  - `[ns_zhouyi_369]` `[trigger: 卦=解 AND 六五=君子维有解]` `[factor_trigger: zhouyi_gua_jie]` `[role: 主干依赖]` 君子维有解，吉：君子自有解脱之道。 → 《周易·解卦·爻辞》
  - `[ns_zhouyi_370]` `[trigger: 卦=解 AND 上六=公用射隼]` `[factor_trigger: zhouyi_gua_jie]` `[role: 总结]` 公用射隼于高墉之上：以正手段解除高处之患。 → 《周易·解卦·爻辞》
  - **中文**：
  - 卦辞"解：利西南。无所往，其来复吉。有攸往，夙吉"依通行王弼本；"解"为解散、缓解，震雷在上、坎水在下。
  - "雷雨作，解"谓雷雨交作而解散阴郁之气，天地之大解也。
  - "赦过宥罪"谓君子效法雷雨之解，赦免过失、宽宥罪责。
  - "田获三狐"之"狐"为阴险之物，"黄矢"为正直之器，解除群狐而得正器。
  - "负且乘，致寇至"谓背负货物本为负贩之人，却乘车而行，身份错乱，招致盗寇觊觎。
  - "射隼于高墉之上"以射猎高处之隼鸟喻以正当手段解除高位之患。
  - **English**: Based on Wang Bi commentary edition. "解" means release/dissolution. "雷雨作" shows thunder and rain dissolving oppression. "赦过宥罪" advises pardoning. "负且乘" warns of status confusion. "射隼" symbolizes removing high-placed threats."""
    normalized_text_zh: str = """"""
    subject: str = "解卦（䷧）"
    factor_refs: list = ['zhouyi_gua_040', 'symbol_thunder_rain_release_proposal', 'principle_pardon_forgive_proposal', 'method_release_toe_proposal', 'method_shoot_hawk_proposal']
    
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
        l1_anchor="zy_v1.0.0_解卦_001_L1",
    )
    version: str = "1.0.0"
