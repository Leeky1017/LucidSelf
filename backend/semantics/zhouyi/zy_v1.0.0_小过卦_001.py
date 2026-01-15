"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919564
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
    semantic_id="zy_v1.0.0_小过卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 小过卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  小过：亨，利贞。可小事，不可大事。飞鸟遗之音，不宜上，宜下。大吉。

  【彖传】
  《彖》曰：“小过，小者过而亨也。过以利贞，与时...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  小过：亨，利贞。可小事，不可大事。飞鸟遗之音，不宜上，宜下。大吉。

  【彖传】
  《彖》曰：“小过，小者过而亨也。过以利贞，与时行也。柔得中，是以小事吉也；刚失位而不中，是以不可大事也。有飞鸟之象焉。飞鸟遗之音，不宜上，宜下，大吉；上逆而下顺也。”

  【象传】
  《象》曰：山上有雷，小过；君子以行过乎恭，丧过乎哀，用过乎俭。

  【爻辞】
  初六，飞鸟以凶。
  六二，过其祖，遇其妣；不及其君，遇其臣，无咎。
  九三，弗过防之，从或戕之，凶。
  九四，无咎，弗过遇之，往厉必戒，勿用永贞。
  六五，密云不雨，自我西郊，公弋取彼在穴。
  上六，弗遇，过之，飞鸟离之，凶，是谓灾眚。

- 分字分词释义：

  - **小过**：小处有“过”、有超出常度之处，引申为“在细节上适度超出”，而非谋大过举。
  - **可小事，不可大事**：适用于小范围调整、小规模超越，不宜承担重大决断与结构性改变。
  - **飞鸟遗之音，不宜上，宜下**：飞鸟飞过留下声音；声音上升为“上”，下降或落于下者为“下”。“不宜上，宜下”比喻行事宜低姿态、趋下，而不宜高张冒进。
  - **山上有雷**：上艮为山，下震为雷，雷在山下，声在下而势受阻，形成“小过”的局面：动而不大、声多势小。
  - **行过乎恭 / 丧过乎哀 / 用过乎俭**：在礼节、哀戚、用度上略微偏多一分，体现“宁过于不足”的态度，但都在“小过”范围内。
  - **过其祖，遇其妣；不及其君，遇其臣**：在亲属与上下结构中“略有超越”却不过分，最终仍能遇到合宜的对接对象。
  - **弗过防之**：不肯“稍过”地设防，过于放松警惕，招致凶险。
  - **密云不雨**：阴云密布却未降雨，比喻条件虽具、时机却未成，提醒切勿以大作为名行妄动之实。
  - **灾眚**：灾祸与过失的合称，指由小过发展到大祸的终局状态。

- **规范化释义（primary_lang_explained）**：

  小过卦讨论的是“在小处如何过之为宜”。卦辞说：“小过：亨，利贞。可小事，不可大事。飞鸟遗之音，不宜上，宜下。大吉。”——说明在小处有一点“过”，在细节上多出一分谨慎、一分敬意，反而有利于亨通与守正；但若把这种“过”推向大事与根本结构，就会适得其反。

  彖传强调“小者过而亨也。过以利贞，与时行也。”——在小处适度越常，配合时势而行，可以帮助维持整体平衡；柔爻得中，小事吉；刚爻失位而不中，则不宜大事。飞鸟象进一步说明：飞鸟之音若上升过高，就是“上逆”；若回落于下，就是“下顺”。小过之道在于趋下、不亢，避免高调冒进。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Xiao Guo (Small Excess) addresses 小事过之. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 小过卦核心是**“在细节上略偏，整体上守中”**：小处宁可多一分，不可少一分；大处不宜妄自超越。
  - 卦辞将“小过”的适用范围限定为“小事”，并以“飞鸟遗音”形象化地呈现“宜下不宜上”的姿态原则。
  - 各爻通过“飞鸟以凶”“过其祖，遇其妣”“密云不雨”“飞鸟离之”等象，展示从合宜小过到不加防备、走向灾眚的一整条路径。

- 详细解说：

  卦象为上艮下震：雷在山下，声在下而势受阻，形成“小过”的局面：动而不大、声多势小。君子“以行过乎恭，丧过乎哀，用过乎俭”：行为比平常更恭敬一点，丧礼比平常更哀戚一点，用度比平常更节俭一点，这些“过”都在可控范围内，用来弥补人心的迟钝与制度的粗疏。

  初六“飞鸟以凶。”象征一开始就逆势而飞：若在小事上也不顾时势、硬要高飞，则立遭凶险。六二“过其祖，遇其妣；不及其君，遇其臣，无咎。”则给出“小过得其宜”的样例：在亲属关系与上下层级中略有超越却不僭越到君位，最终仍能遇到合宜的支持者，因此无咎。

  九三“弗过防之，从或戕之，凶。”提醒：有些地方本应“小过”地加强防备，如果连这点“过”都不肯，就容易在关键时刻被人加害。九四“无咎，弗过遇之，往厉必戒，勿用永贞。”说明在中高位者即使因环境“遇之”而获利，也必须意识到自己“不当位”，前行当戒备，而不可把这种侥幸延长为“永贞”的长期策略。

  六五“密云不雨，自我西郊，公弋取彼在穴。”展现的是“小过中的等待”：条件似备而未成雨，若急于大动，反招其害；通过“公弋取彼在穴”的有限行动，获取适量成果即可。上六“弗遇，过之，飞鸟离之，凶，是谓灾眚。”则是全卦的极端：在未遇其时的情形下仍继续“过之”，结果如飞鸟被射中而坠落，由小小过度积成灾眚。


#### L2 语义提取

- **主题**：小事过之，如何在此情境中顺应天道、把握时机、实现人生目标。

- **自然属性**：
  - **象征**：山上有雷、过以利贞、可小事不可大事、飞鸟遗之音。
  - **特性**：本卦特有的运作方式与吉凶条件。
  - **元素**：上下卦组合的五行与象征意义。

- **功能象义**：

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_560]` `[trigger: 卦=小过 AND 卦辞=亨利贞]` `[factor_trigger: zhouyi_gua_xiaoguo AND zhouyi_guaci]` `[role: 主干]` 小过，亨，利贞：小事可过，大事不可。 → 《周易·小过卦·卦辞》
  - `[ns_zhouyi_561]` `[trigger: 卦=小过 AND 彖传]` `[factor_trigger: zhouyi_gua_xiaoguo AND zhouyi_tuan AND zhouyi_xiaoguo_chengdu]` `[role: 主干依赖]` 小者过而亨也。 → 《周易·小过卦·彖传》
  - `[ns_zhouyi_562]` `[trigger: 卦=小过 AND 象传=山上有雷]` `[factor_trigger: zhouyi_gua_xiaoguo AND zhouyi_xiang]` `[role: 主干依赖]` 山上有雷，小过；君子以行过乎恭，丧过乎哀：小过之时，行礼宜过。 → 《周易·小过卦·象传》
  - `[ns_zhouyi_563]` `[trigger: 卦=小过 AND 初六=飞鸟以凶]` `[factor_trigger: zhouyi_gua_xiaoguo]` `[role: 例外处理]` 飞鸟以凶：飞鸟冒进而凶。 → 《周易·小过卦·爻辞》
  - `[ns_zhouyi_564]` `[trigger: 卦=小过 AND 六二=过其祖遇其妣]` `[factor_trigger: zhouyi_gua_xiaoguo]` `[role: 条件分支]` 过其祖，遇其妣：越过祖而遇其妣。 → 《周易·小过卦·爻辞》
  - `[ns_zhouyi_565]` `[trigger: 卦=小过 AND 九三=弗过防之]` `[factor_trigger: zhouyi_gua_xiaoguo]` `[role: 例外处理]` 弗过防之，从或戕之：不过度防范，反遭戕害。 → 《周易·小过卦·爻辞》
  - `[ns_zhouyi_566]` `[trigger: 卦=小过 AND 九四=无咎弗过遇之]` `[factor_trigger: zhouyi_gua_xiaoguo]` `[role: 条件分支]` 无咎，弗过遇之：无咎而遇，非过度也。 → 《周易·小过卦·爻辞》
  - `[ns_zhouyi_567]` `[trigger: 卦=小过 AND 六五=密云不雨]` `[factor_trigger: zhouyi_gua_xiaoguo]` `[role: 主干依赖]` 密云不雨，自我西郊：云密而不雨，德泽未施。 → 《周易·小过卦·爻辞》
  - `[ns_zhouyi_568]` `[trigger: 卦=小过 AND 上六=弗遇过之]` `[factor_trigger: zhouyi_gua_xiaoguo]` `[role: 总结]` 弗遇过之，飞鸟离之：不遇而过，如飞鸟远离。 → 《周易·小过卦·爻辞》
  - **中文**：
  - 卦辞"小过：亨，利贞。可小事，不可大事。飞鸟遗之音，不宜上，宜下，大吉"依通行王弼本；"小过"谓小事可稍过常度。
  - "山上有雷"谓震雷在艮山之上，雷在高处声势虽大却受山阻，象征动而不远。
  - "行过乎恭，丧过乎哀，用过乎俭"三者皆示在礼节上"宁过于不及"之态度。
  - "飞鸟遗之音"以飞鸟为喻，鸟飞则音逝，不宜上扬冒进，宜下顺低调。
  - "过其祖，遇其妣"谓在尊卑序列中略有越过，但仍遇到合适对象；"不及其君，遇其臣"亦同。
  - "从或戕之"之"戕"释为伤害，不设防则反遭戕害。
  - **English**: Based on Wang Bi commentary edition. "小过" means small exceeding is permissible. "山上有雷" shows thunder blocked by mountain. "行过乎恭" etc. advocate slight excess in propriety. "飞鸟遗音" metaphor advises staying low. "戕" means injury."""
    normalized_text_zh: str = """"""
    subject: str = "小过卦（䷽）"
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
        l1_anchor="zy_v1.0.0_小过卦_001_L1",
    )
    version: str = "1.0.0"
