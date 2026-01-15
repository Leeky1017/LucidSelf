"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919432
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
    semantic_id="zy_v1.0.0_井卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 井卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  井：改邑不改井，无丧无得。往来井井。汔至，亦未繘井，羸其瓶，凶。

  【彖传】
  《彖》曰：“巽乎水而上水，井。井养而不穷也。‘改...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  井：改邑不改井，无丧无得。往来井井。汔至，亦未繘井，羸其瓶，凶。

  【彖传】
  《彖》曰：“巽乎水而上水，井。井养而不穷也。‘改邑不改井’，乃以刚中也。‘汔至，亦未繘井’，未有功也。‘羸其瓶’，是以凶也。”

  【象传】
  《象》曰：木上有水，井；君子以劳民劝相。

  【爻辞】
  初六，井泥不食。旧井无禽。
  九二，井谷射鲋，瓮敝漏。
  九三，井渫不食，为我心恻。可用汲，王明，并受其福。
  六四，井甃，无咎。
  九五，井洌，寒泉食。
  上六，井收，勿幕；有孚，元吉。

- 分字分词释义：

  - **井**：水井，本为公共取水之处；在卦中多比喻公共资源、养人之道，以及“居其所而恒给于人”的君子之德。
  - **改邑不改井**：城邑可以迁徙，水井却常在原处，象征环境与制度可以变动，而“供养众人之道”应当稳定不变。
  - **无丧无得**：对井本身而言，既无损失也无所得，提示“施与不以得失计”的德行。
  - **往来井井**：“井井”本为整齐有序之状，这里指来往汲水之人络绎不绝而秩序井然。
  - **汔至**：汔，几乎、将近之意；指汲水将至井口而未出井。
  - **繘井**：用绳索汲水，绳在井中盘绕、牵引；“亦未繘井”指尚未来得及把水汲出。
  - **羸其瓶**：“羸”有缠绕、牵扯之义，“瓶”指汲水的瓦罐；言瓶罐在井中被绳索或井壁牵挂而破碎。
  - **井泥不食**：井中只有污泥而无清水，不可饮用，比喻有名无实、久废不用之才与道。
  - **井谷射鲋**：在井底洼处射捉小鱼（鲋），且用破瓮承之，比喻错用场所与器具，徒劳无功。
  - **井渫不食**：“渫”指清除污泥、疏通；井水虽已清澈，却无人前来饮用，使人心中悲恻。
  - **井甃**：甃为砖石砌成的井壁，象征基础加固、结构完备。
  - **井洌，寒泉食**：“洌”指水清而寒凉；井水如同寒泉，可供人畅饮。
  - **井收，勿幕；有孚，元吉**：“井收”指井修成、功能完备；“勿幕”是不以盖遮，任人取用；“有孚”是内怀诚信与可靠之德，故能元吉。
  - **劳民劝相**：劝勉民众互相资助、互相成就，如同共用同一口井。

- **规范化释义（primary_lang_explained）**：

  井卦以“水井”比喻公共资源与君子之德。卦辞说：“井：改邑不改井，无丧无得。往来井井。汔至，亦未繘井，羸其瓶，凶。”——城市可以迁移，井却常在原处；对井而言，人来人往汲水，不过是履行它“养人”的本分，本无所谓损失或收益。问题多出在汲水的人：水几乎提到井口，却因为绳索未理、瓦罐不慎而在井中破碎，最终一无所获，是为“羸其瓶，凶”。

  彖传从卦象切入：“巽乎水而上水，井。井养而不穷也。”——下巽为木，上坎为水，木入水中，承载井水而出，是“井养而不穷”的象。又曰：“改邑不改井，乃以刚中也。”卦体之“刚中”象征井道本身稳固可靠，因此城邑虽迁、人事虽变，井却不随意废弃；“汔至，亦未繘井，未有功也。羸其瓶，是以凶也。”则指出：若在最后关头因疏忽而前功尽弃，便只能自受其凶。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Jing (The Well) addresses 井养不穷. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 井卦核心是**“恒久供养之道”**：真正的德行与公共资源，不随政局与环境轻易更改。
  - 卦辞强调“善终”的重要性：事情做到“汔至”而不谨慎收束，往往一败涂地。
  - 爻辞从“泥井”“破井”“清井无人”“井甃具备”“寒泉可食”“井收勿幕”层层展开，刻画从废井到善井的演变路径。

- 详细解说：

  井卦卦象为上坎下巽：木在水下，木中汲水而上，是“井”之形。与前卦困的“泽无水”不同，井卦强调的不是资源枯竭，而是“资源恒在、用之或废”的问题——井水在那儿，人是否愿汲、是否会汲、是否能善终，是不同的层次。

  初六“井泥不食。旧井无禽。”描述的是最下层、最久废的井：只剩淤泥，不堪饮用，连鸟兽也不来停留。九二“井谷射鲋，瓮敝漏。”则是错误用井：把井底当作捉鱼之处，又用破漏的瓦瓮承之，不论资源还是工具都选错，难以有成。九三“井渫不食，为我心恻。可用汲，王明，并受其福。”转入“井已清而人未至”的状态：井水已清，却仍无人取用，使懂得其价值者心中悲恻；倘若明君出现，善用此井，则君民并受其福。

  六四“井甃，无咎。”象征井壁已砌好、结构完备，至少“不再出错”；九五“井洌，寒泉食。”则是善井之象：水清而甘，足以广施；上六“井收，勿幕；有孚，元吉。”更进一步：井已修成、功能稳定，不宜用盖遮蔽，而应开放供众人取用。只要井主与用井之人之间保持“有孚”——相互信任，这样的井才能真正“元吉”。这一系列图景，从废到成、从隐没到公开，构成了“井道”的完整故事。


#### L2 语义提取


- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_434]` `[trigger: 卦=井 AND 卦辞=改邑不改井]` `[factor_trigger: zhouyi_gua_jing AND zhouyi_guaci AND zhouyi_busuke]` `[role: 主干]` 井，改邑不改井，无丧无得：井道恒常，不因迁邑而变。 → 《周易·井卦·卦辞》
  - `[ns_zhouyi_435]` `[trigger: 卦=井 AND 彖传]` `[factor_trigger: zhouyi_gua_jing AND zhouyi_tuan AND zhouyi_jingyang_chengdu]` `[role: 主干依赖]` 巽乎水而上水。 → 《周易·井卦·彖传》
  - `[ns_zhouyi_436]` `[trigger: 卦=井 AND 象传=木上有水]` `[factor_trigger: zhouyi_gua_jing AND zhouyi_xiang]` `[role: 主干依赖]` 木上有水，井；君子以劳民劝相：如井养万民。 → 《周易·井卦·象传》
  - `[ns_zhouyi_437]` `[trigger: 卦=井 AND 初六=井泥不食]` `[factor_trigger: zhouyi_gua_jing]` `[role: 例外处理]` 井泥不食，旧井无禽：井底泥浊，无人取用。 → 《周易·井卦·爻辞》
  - `[ns_zhouyi_438]` `[trigger: 卦=井 AND 九二=井谷射鲋]` `[factor_trigger: zhouyi_gua_jing]` `[role: 例外处理]` 井谷射鲋，瓮敝漏：井中只有小鱼，瓦瓮亦漏。 → 《周易·井卦·爻辞》
  - `[ns_zhouyi_439]` `[trigger: 卦=井 AND 九三=井渫不食]` `[factor_trigger: zhouyi_gua_jing]` `[role: 条件分支]` 井渫不食，为我心恻：井已清洁，却无人饮用。 → 《周易·井卦·爻辞》
  - `[ns_zhouyi_440]` `[trigger: 卦=井 AND 六四=井甃无咎]` `[factor_trigger: zhouyi_gua_jing]` `[role: 条件分支]` 井甃，无咎：以砖砌井，无所咎责。 → 《周易·井卦·爻辞》
  - `[ns_zhouyi_441]` `[trigger: 卦=井 AND 九五=井洌寒泉食]` `[factor_trigger: zhouyi_gua_jing]` `[role: 主干依赖]` 井洌，寒泉食：井水清冽，可以饮用。 → 《周易·井卦·爻辞》
  - `[ns_zhouyi_442]` `[trigger: 卦=井 AND 上六=井收勿幕]` `[factor_trigger: zhouyi_gua_jing]` `[role: 总结]` 井收勿幕，有孚元吉：井口不蔽，诚信大吉。 → 《周易·井卦·爻辞》
  - **中文**：
  - 卦辞"井：改邑不改井，无丧无得。往来井井。汔至，亦未繘井，羸其瓶，凶"依通行王弼本；"井"以井喻恒常供养之德。
  - "木上有水"谓巽木在下、坎水在上，以木汲水，象征井水上涌。
  - "改邑不改井"谓城邑可迁，井道不变，恒常之德不随环境改变。
  - "汔至，亦未繘井"之"汔"释为几乎、将至；"繘"为井绳；将至井口而绳断，功亏一篑。
  - "井泥/井谷/井渫/井甃/井洌"由浊至清、由废至用，展示井道修养之次第。
  - "井收勿幕"谓井水汲满而不加盖，公开与人共享，有孚则元吉。
  - **English**: Based on Wang Bi commentary edition. "井" uses well as metaphor for constant nourishment. "改邑不改井" shows virtue unchanged by circumstances. "汔至" means almost reaching. "繘" is well rope. Progression from 泥 to 洌 shows purification stages. "勿幕" means keeping well open to share."""
    normalized_text_zh: str = """"""
    subject: str = "井卦（䷯）"
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
        l1_anchor="zy_v1.0.0_井卦_001_L1",
    )
    version: str = "1.0.0"
