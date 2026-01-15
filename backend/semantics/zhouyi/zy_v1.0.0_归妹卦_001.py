"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919489
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
    semantic_id="zy_v1.0.0_归妹卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 归妹卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  归妹，征凶，无攸利。

  【彖传】
  《彖》曰：“归妹，天地之大义也。天地不交，而万物不兴；归妹，人之终始也。说以动，所归妹也。征...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  归妹，征凶，无攸利。

  【彖传】
  《彖》曰：“归妹，天地之大义也。天地不交，而万物不兴；归妹，人之终始也。说以动，所归妹也。征凶，位不当也。无攸利，柔乘刚也。”

  【象传】
  《象》曰：泽上有雷，归妹；君子以永终知敝。

  【爻辞】
  初九，归妹以娣，跛能履，征吉。
  九二，眇能视，利幽人之贞。
  六三，归妹以须，反归以娣。
  九四，归妹愆期，迟归有时。
  六五，帝乙归妹，其君之袂不如其娣之袂良，月几望，吉。
  上六，女承筐无实，士刲羊无血，无攸利。

- 分字分词释义：

  - **归妹**：“归”本义为女子出嫁，“妹”指少女，卦名指少女归嫁；在本卦多带“不当之归”之意。
  - **征凶，无攸利**：在此结构下主动出征、主动推进，多为凶，无所利，提示在“不当之归”情形下不宜再行扩张。
  - **泽上有雷**：下兑为泽，上震为雷，雷在泽上，声音浮于表，而下实未必充足。
  - **永终知敝**：从事物的终局来观其弊病，君子由归妹之象而知“有终无始”的各种问题。
  - **以娣 / 以须**：“娣”为陪嫁的妹妹，“须”有等待、迟延之意；“归妹以娣 / 以须”指婚配顺序、时机的错乱或拖延。
  - **眇能视**：一目失明而仍能看，比喻视野偏颇但尚有局部洞见。
  - **幽人之贞**：隐居之人的守正，适宜在不当结构下退居内在而守节。
  - **愆期**：错过正当的时机。
  - **帝乙归妹**：以商朝帝乙嫁女为象，强调“嫁得其时其人”之吉，但细节中仍有“君之袂不如其娣之袂良”的张力。
  - **承筐无实 / 刲羊无血**：筐中无物、宰羊无血，比喻形式有余而内容不足，徒具礼仪而无真实内涵。

- **规范化释义（primary_lang_explained）**：

  归妹卦与渐卦同属“婚姻系列”，但从“循礼渐进”转向“结构不当的归嫁”。卦辞直言：“归妹，征凶，无攸利。”——在归妹这样的局面中，主动出征、主动推进，多半带来凶险，很难获利。

  彖传一方面承认“归妹，天地之大义也”：天地阴阳不交，万物不兴；少女出嫁，是人类生息的终始之道；另一方面却指出本卦结构中的失衡：以“说以动”而动，位置又多不当，“柔乘刚”，导致征伐为凶、难有其利。归妹因此成为“看清不当之合、不当之终局”的一面镜子。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Gui Mei (Marrying Maiden) addresses 归嫁之道. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 归妹卦的核心是**“阴阳交合之道中的失衡与不当之合”**。
  - 在这种结构下，宜观终局、警惕弊病，而不宜贸然再行进取。
  - 多数爻辞通过婚嫁顺序、礼仪形式的错位，展示“形式有而实不足”的危机。

- 详细解说：

  卦象为上震下兑：震为雷、为动，兑为泽、为悦，雷在泽上，声势彰显于表，而下实未必充足。与渐卦“山上有木”的厚积薄发不同，归妹中的动多半偏于表层情绪与短期安排。

  初九“归妹以娣，跛能履，征吉。”描述的是一种次序错乱却仍可勉强成行的局面：以娣陪归而成婚，如跛者尚能行走，虽不完美，尚可“征吉”，但隐含结构偏差。九二“眇能视，利幽人之贞。”则提示：在视野偏颇、局势不正之时，不如退入“幽人之贞”，在隐处守节，比强行参与更有利。

  六三“归妹以须，反归以娣。”展现的是婚期一再拖延，最后又以娣陪归的反复变化，象征在不当结构中摇摆，终难全美。九四“归妹愆期，迟归有时。”说明错过了最佳时机之后，再归也只能视为“迟归”：虽然仍有其时，却不及理想之和合。

  六五“帝乙归妹，其君之袂不如其娣之袂良，月几望，吉。”用帝乙嫁女的典故暗示：即便整体归嫁得其时其人，细节上仍有“君之袂不如娣之袂”之失衡——主次倒置、美丑不均。然“月几望”象征接近圆满，整体仍可为吉。上六“女承筐无实，士刲羊无血，无攸利。”则收束全卦：礼仪形式虽全，却“筐无实”“羊无血”，只剩空壳，最终“无攸利”。


#### L2 语义提取


- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_488]` `[trigger: 卦=归妹 AND 卦辞=征凶无攸利]` `[factor_trigger: zhouyi_gua_guimei AND zhouyi_guaci]` `[role: 主干]` 归妹，征凶，无攸利：少女归嫁，冒进则凶。 → 《周易·归妹卦·卦辞》
  - `[ns_zhouyi_489]` `[trigger: 卦=归妹 AND 彖传]` `[factor_trigger: zhouyi_gua_guimei AND zhouyi_tuan AND zhouyi_hunyin_chengdu]` `[role: 主干依赖]` 天地之大义也。 → 《周易·归妹卦·彖传》
  - `[ns_zhouyi_490]` `[trigger: 卦=归妹 AND 象传=泽上有雷]` `[factor_trigger: zhouyi_gua_guimei AND zhouyi_xiang]` `[role: 主干依赖]` 泽上有雷，归妹；君子以永终知敝：雷动泽上，知其终敝。 → 《周易·归妹卦·象传》
  - `[ns_zhouyi_491]` `[trigger: 卦=归妹 AND 初九=归妹以娣]` `[factor_trigger: zhouyi_gua_guimei]` `[role: 条件分支]` 归妹以娣，跛能履：以妾身份出嫁。 → 《周易·归妹卦·爻辞》
  - `[ns_zhouyi_492]` `[trigger: 卦=归妹 AND 九二=眇能视]` `[factor_trigger: zhouyi_gua_guimei]` `[role: 条件分支]` 眇能视，利幽人之贞：独眼能视，利于幽人守正。 → 《周易·归妹卦·爻辞》
  - `[ns_zhouyi_493]` `[trigger: 卦=归妹 AND 六三=归妹以须]` `[factor_trigger: zhouyi_gua_guimei]` `[role: 条件分支]` 归妹以须，反归以娣：等待而后出嫁。 → 《周易·归妹卦·爻辞》
  - `[ns_zhouyi_494]` `[trigger: 卦=归妹 AND 九四=归妹愆期]` `[factor_trigger: zhouyi_gua_guimei]` `[role: 例外处理]` 归妹愆期，迟归有时：婚期延误，终有其时。 → 《周易·归妹卦·爻辞》
  - `[ns_zhouyi_495]` `[trigger: 卦=归妹 AND 六五=帝乙归妹]` `[factor_trigger: zhouyi_gua_guimei]` `[role: 主干依赖]` 帝乙归妹，其君之袂不如其娣之袂良：帝乙嫁女，妾衣胜主。 → 《周易·归妹卦·爻辞》
  - `[ns_zhouyi_496]` `[trigger: 卦=归妹 AND 上六=女承筐无实]` `[factor_trigger: zhouyi_gua_guimei]` `[role: 总结]` 女承筐无实，士刲羊无血：虚礼无实。 → 《周易·归妹卦·爻辞》
  - **中文**：
  - 卦辞"归妹：征凶，无攸利"依通行王弼本；"归妹"指少女出嫁，嶽上有震，悦而动，有轻率之象，故"征凶"。
  - "以娣"之"娣"为随嫁之妹，即媞；"跠能履"谓足跠仍能行走，比喻位卑但能尽责。
  - "眷能视"谓独眼能见，与"跠能履"同为“残而能用”之象，适合幽隱守正者。
  - "帝乙归妹"引史事，帝乙为商王名；"其君之裂不如其娣之裂良"谓正室衣饰反不如媞女华美，暗示地位与行为乍归。
  - "女承筐无实，士刲羊无血"谓婚礼之筐空无果实、杀羊无血，象征形式主义、虚礼无实。
  - **English**: Based on Wang Bi commentary edition. "归妹" refers to younger sister marrying. "娣" is a concubine who accompanies the bride. "跠/眷" (lame/one-eyed) symbolize incomplete but functional roles. "帝乙归妹" is a historical allusion. "无实/无血" indicate empty formalities."""
    normalized_text_zh: str = """"""
    subject: str = "归妹卦（䷵）"
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
        l1_anchor="zy_v1.0.0_归妹卦_001_L1",
    )
    version: str = "1.0.0"
