"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919587
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
    semantic_id="zy_v1.0.0_未济卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 未济卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  未济：亨。小狐汔济，濡其尾，无攸利。

  【彖传】
  《彖》曰：“未济，亨，柔得中也。小狐汔济，未出中也。濡其尾，无攸利，不续终也...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  未济：亨。小狐汔济，濡其尾，无攸利。

  【彖传】
  《彖》曰：“未济，亨，柔得中也。小狐汔济，未出中也。濡其尾，无攸利，不续终也。虽不当位，刚柔应也。”

  【象传】
  《象》曰：火在水上，未济；君子以慎辨物居方。

  【爻辞】
  初六，濡其尾，吝。
  九二，曳其轮，贞吉。
  六三，未济，征凶；利涉大川。
  九四，贞吉，悔亡。震用伐鬼方，三年有赏于大国。
  六五，贞吉，无悔。君子之光，有孚，吉。
  上九，有孚于饮酒，无咎；濡其首，有孚，失是。

- 分字分词释义：

  - **未济**：尚未渡过、尚未完成；卦名指“过程中的中段”，既非起点，也非终点。
  - **小狐汔济**：“汔”为几、将要之意，小狐狸将要渡河却未全渡，比喻事情临近成功却尚有关键一段未成。
  - **濡其尾，无攸利**：尾巴沾湿，象征在最后关头失足；因未能“续终”，所以无所利。
  - **火在水上**：上离为火，下坎为水，与既济“水在火上”相反，象征尚在混乱、难以稳定的状态。
  - **慎辨物居方**：谨慎分辨事物各自当处之方位，让人事与资源各得其所。
  - **曳其轮，贞吉**：拉住车轮不使前进过快，在未济阶段以守正而稍缓行动，反成吉利。
  - **征凶，利涉大川**：前行有凶险，却仍有“涉大川”的必要，提醒在危险旅程中不能完全停滞。
  - **震用伐鬼方，三年有赏于大国**：与既济卦九三遥相呼应，再次提及伐鬼方，强调长期艰难中的坚持与最终奖赏。
  - **君子之光，有孚，吉**：君子的德光与诚信相映，在未济中起稳定与照明作用。
  - **有孚于饮酒…濡其首，有孚，失是**：在酒宴中保持诚信无咎；一旦失于节度，即便有孚亦失正。

- **规范化释义（primary_lang_explained）**：

  未济卦聚焦于“尚未完成之时的行事之道”。卦辞曰：“未济：亨。小狐汔济，濡其尾，无攸利。”——虽名“未济”，仍然可以亨通；然而像小狐狸渡河将成未成，在最后一刻若失足而湿尾，就难言有利。

  彖传指出：“未济，亨，柔得中也。”——未济之所以还能亨，是因为柔爻居中，使整体不至失衡；但“小狐汔济，未出中也”说明尚未出险，若不能“续终”，则会在关键处功亏一篑。未济因此要求在人、事、位的安排上“慎辨物居方”，而不是急于求成或放任散乱。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Wei Ji (Before Completion) addresses 未竟未济. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 未济卦核心是**“在未竟之时稳住结构、守中而终”**。
  - 小狐意象强调“最后一段”的重要性：前面所有努力若不能顺利收束，整体成败依旧未定。
  - 各爻展现从“初濡其尾”的不慎，到“曳其轮”的克制、“征凶而涉川”的必要行动、“伐鬼方三年”的长期战役、“君子之光”的稳定作用，再到“饮酒濡首”的失节风险。

- 详细解说：

  卦象火在水上：水在下，火在上，既相克又相需，整体尚处于不稳定的结构中。君子“以慎辨物居方”：在资源、角色和时机尚未完全配齐之时，谨慎地把各要素安置到合适位置，是使未济转向既济的关键。

  初六“濡其尾，吝。”直接承接卦辞意象：一开始就因不慎而湿尾，虽未至大凶，已属可惜。九二“曳其轮，贞吉。”则提示在未济阶段需要有意识地放慢车轮，即便具备行动能力，也要以守正为主，避免过急。

  六三“未济，征凶；利涉大川。”表明在结构尚未成形时强行前进会有凶险，但又不得不涉大川——说明有些风险性的行动在未济阶段难以完全避免，只能在清楚其凶性的前提下谨慎行之。九四“贞吉，悔亡。震用伐鬼方，三年有赏于大国。”指出：若能持正不懈，即便历经长期艰难，最终仍可得赏，悔恨可以消除。

  六五“贞吉，无悔。君子之光，有孚，吉。”强调在尊位上以光明与诚信为核心，使未济的局面中仍有可依赖的灯塔。上九“有孚于饮酒，无咎；濡其首，有孚，失是。”则以饮酒示警：在未济阶段，适度的欢聚并不有害，关键是不能让放松演变为失节；一旦到“濡其首”的程度，即便心怀诚信，也偏离了应有之道。


#### L2 语义提取

- **主题**：未竟未济，如何在此情境中顺应天道、把握时机、实现人生目标。

- **自然属性**：

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_578]` `[trigger: 卦=未济 AND 卦辞=亨小狐汔济]` `[factor_trigger: zhouyi_gua_weiji AND zhouyi_guaci]` `[role: 主干]` 未济，亨；小狐汔济，濡其尾：小狐将渡，尾已湿矣。 → 《周易·未济卦·卦辞》
  - `[ns_zhouyi_579]` `[trigger: 卦=未济 AND 彖传]` `[factor_trigger: zhouyi_gua_weiji AND zhouyi_tuan AND zhouyi_weicheng_chengdu]` `[role: 主干依赖]` 亨。柔得中也。 → 《周易·未济卦·彖传》
  - `[ns_zhouyi_580]` `[trigger: 卦=未济 AND 象传=火在水上]` `[factor_trigger: zhouyi_gua_weiji AND zhouyi_xiang]` `[role: 主干依赖]` 火在水上，未济；君子以慎辨物居方：火水未济，慎辨物类。 → 《周易·未济卦·象传》
  - `[ns_zhouyi_581]` `[trigger: 卦=未济 AND 初六=濡其尾]` `[factor_trigger: zhouyi_gua_weiji]` `[role: 条件分支]` 濡其尾，吝：尾已湿，有所吝惜。 → 《周易·未济卦·爻辞》
  - `[ns_zhouyi_582]` `[trigger: 卦=未济 AND 九二=曳其轮]` `[factor_trigger: zhouyi_gua_weiji]` `[role: 条件分支]` 曳其轮，贞吉：拖曳车轮，守正则吉。 → 《周易·未济卦·爻辞》
  - `[ns_zhouyi_583]` `[trigger: 卦=未济 AND 六三=未济征凶]` `[factor_trigger: zhouyi_gua_weiji]` `[role: 例外处理]` 未济，征凶，利涉大川：未济而征，凶；利涉险川。 → 《周易·未济卦·爻辞》
  - `[ns_zhouyi_584]` `[trigger: 卦=未济 AND 九四=贞吉悔亡]` `[factor_trigger: zhouyi_gua_weiji]` `[role: 条件分支]` 贞吉，悔亡：守正则吉，悔恨消解。 → 《周易·未济卦·爻辞》
  - `[ns_zhouyi_585]` `[trigger: 卦=未济 AND 六五=贞吉无悔]` `[factor_trigger: zhouyi_gua_weiji]` `[role: 主干依赖]` 贞吉，无悔：君子之光，有孚吉。 → 《周易·未济卦·爻辞》
  - `[ns_zhouyi_586]` `[trigger: 卦=未济 AND 上九=有孚于饮酒]` `[factor_trigger: zhouyi_gua_weiji]` `[role: 总结]` 有孚于饮酒，无咎：诚信饮酒，无所咎责。 → 《周易·未济卦·爻辞》
  - **中文**：
  - 卦辞"未济：亨。小狐汔济，濡其尾，无攸利"依通行王弼本；"未济"谓事尚未成，与既济相对，为《周易》终卦。
  - "火在水上"谓离火在坎水之上，火水不交，各居其位而未相济，象征尚待完成之状。
  - "小狐汔济"之"汔"释为几乎、将要；小狐将渡而尾已湿，功亏一篑之象。
  - "慎辨物居方"谓审慎分辨事物、各安其位，未济之时尤需明辨。
  - "君子之光，有孚吉"谓君子光辉在于诚信，有孚则吉。
  - "有孚于饮酒，无咎；濡其首，有孚，失是"对比节制与失度：诚信于饮酒可无咎，但沉溺至濡首则虽有孚亦失其正。
  - **English**: Based on Wang Bi commentary edition. "未济" means not yet completed—final hexagram of Zhouyi. "火在水上" shows fire-water separation. "汔" means almost. "君子之光" relates virtue to sincerity. "濡首" warns of excess even with sincerity."""
    normalized_text_zh: str = """"""
    subject: str = "未济卦（䷿）"
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
        l1_anchor="zy_v1.0.0_未济卦_001_L1",
    )
    version: str = "1.0.0"
