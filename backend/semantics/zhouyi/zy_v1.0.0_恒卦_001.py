"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919210
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
    semantic_id="zy_v1.0.0_恒卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 恒卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  恒：亨，无咎，利贞，利有攸往。

  【彖传】
  《彖》曰："恒，久也。刚上而柔下，雷风相与，巽而动，刚柔皆应，恒。'恒，亨，无咎，...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  恒：亨，无咎，利贞，利有攸往。

  【彖传】
  《彖》曰："恒，久也。刚上而柔下，雷风相与，巽而动，刚柔皆应，恒。'恒，亨，无咎，利贞'，久于其道也。天地之道，恒久而不已也。'利有攸往'，终则有始也。日月得天而能久照，四时变化而能久成。圣人久于其道而天下化成。观其所恒，而天地万物之情可见矣。"

  【象传】
  《象》曰：雷风，恒；君子以立不易方。

  【爻辞】
  初六，浚恒，贞凶，无攸利。
  九二，悔亡。
  九三，不恒其德，或承之羞，贞吝。
  九四，田无禽。
  六五，恒其德，贞；妇人吉，夫子凶。
  上六，振恒，凶。

- 分字分词释义：

  - **恒**：恒久、持久不变之意；在卦中强调"长久守其道"。
  - **亨，无咎，利贞，利有攸往**：以恒久之道行事则通达、无大过失，利于守正，并有利于持续前行。
  - **刚上而柔下，雷风相与**：上卦震为雷、为动；下卦巽为风、为入，刚在上、柔在下，动而不乱，风雷相与成恒象。
  - **久于其道**：长期坚持某一道路，不随便更易根本原则。
  - **立不易方**：确立根本立场而不随意改变方向。
  - **浚恒**：挖得太深、求恒太过，象征过度用力以求长久，反成凶险。
  - **不恒其德**：不能长久保持自身的德行与原则。
  - **田无禽**：在不当之处打猎，捕不到猎物，象征方向错误的坚持徒劳无功。
  - **恒其德**：能恒常守德；在不同角色（妇人与夫子）上呈现不同吉凶指向。
  - **振恒**：动摇其恒，或在上位者扰乱原有的恒常秩序。

- **规范化释义（primary_lang_explained）**：

  恒卦讨论的是"怎样把正确的道路坚持下去"。卦辞说："恒：亨，无咎，利贞，利有攸往。"——只要守住恒常之道，就能通达、免于大错，利于守正，也利于持续前行。然而"恒"并非顽固不化，而是在合乎天道人情的前提下，持之以恒。

  彖传指出："恒，久也"，并通过雷风之象说明结构：雷在上、风在下，风雷相交、不断往复，却有其规律与节奏，这就是"恒"。天地运行不息、日月久照、四时轮替，都是"恒久而不已"的体现。圣人也是通过"久于其道"而化成天下，因此观察一个人或系统"长久坚持的是什么"，就能洞察其真实本性。

  象传"君子以立不易方"把恒转化为修身之道：君子确立根本之方位（价值与原则），之后虽然随时应变，但不轻易改变底层方向。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Heng (Duration/Constancy) represents the principle of enduring persistence on the right path. The image of thunder above wind shows continuous movement with underlying order—wind follows thunder, thunder follows wind, creating an endless cycle. The Judgment "Duration: Success, no blame, favorable to persist, favorable to have a direction to go" indicates that lasting commitment to correct principles brings success. The hexagram teaches that true constancy is not rigid stubbornness but flexible adherence to fundamental values, like the ever-changing yet rhythmic dance of thunder and wind.

- 核心要点：

  - 恒卦核心是**"在合道前提下的长期坚持"**，既反对短期急躁，也警惕僵化顽固。
  - 爻辞揭示了从"求恒过深"到"不能恒德"，再到"恒其德"的角色差异，以及在上位"振恒"的危险。
  - 判断一个人或组织，可以从"其所恒者为何"入手，而不是看一时表现。

- 详细解说：

  卦象上震下巽：下卦巽为风、为入；上卦震为雷、为动。雷风相与，形成"动而入、入而动"的循环，象征天地间永不停息但又有规律的运行。君子"以立不易方"：确立根本方向后，虽然因时制宜地调整方法，却不轻易改变底层价值。

  初六"浚恒，贞凶，无攸利。"处卦之初，若急于求深、挖掘过度，反而导致凶险——这是"求恒太过"的警示。九二"悔亡。"则是恰当守恒的状态：安于中位，不急不躁，先前可能有的悔恨得以消除。

  九三"不恒其德，或承之羞，贞吝。"指出不能持续守德的困境：一会儿这样、一会儿那样，容易招致羞辱，即便想守正也难免吝惜。九四"田无禽。"则是形象的比喻：恒久在错误的位置打猎，当然捕不到猎物——方向错误的坚持毫无意义。

  - `[ns_zhouyi_296b]` `[trigger: 卦=恒 AND 彖传]` `[factor_trigger: zhouyi_gua_heng AND zhouyi_tuan AND zhouyi_hengjiu_chengdu AND zhouyi_jiuyu_qidao]` `[role: 主干依赖]` 恒，久也。刚上而柔下，雷风相与，巽而动，刚柔皆应，恒。恒亨，无咎，利贞，久于其道也。 → 《周易·恒卦·彖传》
  - `[ns_zhouyi_297]` `[trigger: 卦=恒 AND 六五=恒其德贞]` `[factor_trigger: zhouyi_gua_heng]` `[role: 主干依赖]` 恒其德，贞；妇人吉，夫子凶：柔顺之恒宜妇人，刚健者不可拘。 → 《周易·恒卦·爻辞》
  - `[ns_zhouyi_298]` `[trigger: 卦=恒 AND 上六=振恒凶]` `[factor_trigger: zhouyi_gua_heng]` `[role: 总结]` 振恒，凶：恒而躁动，终致凶咎。 → 《周易·恒卦·爻辞》
  - **中文**：

  - 卦辞"恒：亨，无咎，利贞，利有攸往"，本稿保持与通行王弼本一致，不增减字句。
  - "刚上而柔下"一语，本稿释为"震刚在上、巽柔在下"，强调上下卦的性质而非爻位的刚柔。
  - "浚恒"之"浚"释为深掘、深求，本稿不另解为疏浚水道之义。
  - "田无禽"一辞，本稿直译为"在田中打猎却捕不到猎物"，暗示因失位而有损失，但可无悔。

  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "恒卦（䷟）"
    factor_refs: list = ['zhouyi_gua_032', 'symbol_thunder_wind_cycle_proposal', 'principle_stand_firm_direction_proposal', 'principle_long_term_way_proposal', 'warning_over_striving_constancy_proposal']
    
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
        l1_anchor="zy_v1.0.0_恒卦_001_L1",
    )
    version: str = "1.0.0"
