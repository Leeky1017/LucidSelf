"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919352
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
    semantic_id="zy_v1.0.0_损卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 损卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  损：有孚，元吉，无咎，可贞，利有攸往。曷之用？二簋可用享。

  【彖传】
  《彖》曰：“损，损下益上，其道上行。损而有孚，元吉，无...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  损：有孚，元吉，无咎，可贞，利有攸往。曷之用？二簋可用享。

  【彖传】
  《彖》曰：“损，损下益上，其道上行。损而有孚，元吉，无咎，可贞，利有攸往。曷之用？二簋可用享。二簋应有时，损刚益柔有时；损益盈虚，与时偕行。”

  【象传】
  《象》曰：山下有泽，损；君子以惩忿窒欲。

  【爻辞】
  初九，已事遄往，无咎。酌损之。
  九二，利贞，征凶，弗损益之。
  六三，三人行，则损一人；一人行，则得其友。
  六四，损其疾，使遄有喜，无咎。
  六五，或益之十朋之龟，弗克违，元吉。
  上九，弗损益之，无咎，贞吉，利有攸往，得臣无家。

- 分字分词释义：

  - **损**：减少、减损，可指资源、权力、欲望等的自我削减，也可指结构上“此减彼增”。
  - **损下益上，其道上行**：从下减而加于上，道路向上运行，指资源自下而上集中；既有积极扶上之义，也隐含下层被减损的张力。
  - **有孚，元吉，无咎，可贞**：在实行损之时若内怀诚信，整体可大吉而无咎，亦可据此占问与守正。
  - **利有攸往**：在适当的损益布局下，前往行事有利。
  - **曷之用？二簋可用享。**：祭祀时“二簋”已足，不必铺张；象征在“损”的时刻，简约与诚意重于外在丰饰。
  - **山下有泽**：下为兑泽，上为艮山，泽在山下，象征下部被收敛、上部止静，为“损下益上”之象。
  - **惩忿窒欲**：惩罚、压抑愤怒，堵塞、节制欲望，是君子在“损”的结构下自我修持的重点。
  - **已事遄往**：事情准备停当，迅速前往，不拖延。
  - **酌损之**：斟酌损减的程度，而非一概削减。
  - **三人行，则损一人；一人行，则得其友**：多人同行则意见纷杂，不免减损其一；一人独行则更易与真正同道者相遇。
  - **损其疾，使遄有喜**：减轻疾病或弊端，使之迅速转为可喜的局面。
  - **十朋之龟**：价值极高的大龟，象征厚重而难违的增益或馈赠。
  - **得臣无家**：得到忠臣后不再局限于“小家”，而是以天下为家，格局由私转公。

- **规范化释义（primary_lang_explained）**：

  损卦讨论的是“通过适度减损来成就整体之吉”，其焦点不在于“损”本身的痛感，而在于损益之间的节度与时宜。卦辞说：“损：有孚，元吉，无咎，可贞，利有攸往。曷之用？二簋可用享。”——实行“损”的前提是内心有孚，即在信念与承诺上真实不虚，如此才能大吉而无咎；在这样的前提下，既可以占问事务、守持正道，也有利于实际行动。至于祭祀的供物，“二簋”已足，说明在损之时，重在诚意而不在堆叠形式。

  彖传指出，损卦的基本结构是“损下益上，其道上行”：从下减而上增，象征资源、权力、注意力向上集中。但“二簋应有时，损刚益柔有时；损益盈虚，与时偕行”又提醒：不论是削减刚强、增益柔弱，还是在盈虚之间调整，都必须合乎时宜，不能将某一格局凝固为永恒。损的价值在于与时俱进的调节，而非固定的偏向。

  象传“山下有泽，损；君子以惩忿窒欲”把这种结构落实到人格修养：泽在山下，水气被收敛，不再泛滥，是对“过度外散”的约束。君子据此“惩忿窒欲”，不让情绪与欲望泛滥成灾，从而在内在层面完成“损下益上”的自我工程——削减多余欲求，增益德性与定力。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Sun (Decrease) addresses 减损与舍弃. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 损卦的核心是**“为长远的整体增益而进行有节制的减损”**。
  - “损下益上”既可理解为对上位者的支持，也提示在不同层级间如何重新分配资源，需要结合时势谨慎把握。
  - 爻辞呈现了从“斟酌损减、谨慎前往”，到“独行以得友、减疾以得喜、受大益而不可违、得臣而不局于家”的一条完整路径，强调损的目的在于释放更高层次的效用。

- 详细解说：

  卦象为上艮下兑：兑为泽、为悦，艮为山、为止。泽在山下，水受地形所限，不得恣意泛滥，是一种“被克制的愉悦与欲望”的图景。与解卦“雷雨作”的宣泄相比，损卦强调的是“抑制与节流”：在尚未爆发之前，用主动的减损避免未来更大的代价。

  初九“已事遄往，无咎。酌损之”描绘的是在局势初启时的主动：事情既已准备妥当，就应迅速行动，但又须“酌损之”，即仔细权衡减损的幅度，不可一味削减，以免误伤根本。九二“利贞，征凶，弗损益之”提醒：身居中位者若轻率出征（主动扩张），即使守正亦有凶险；此时的宜策是“不损不益”——暂不调整，以静制动。

  六三“三人行，则损一人；一人行，则得其友”是非常形象的结构隐喻：在决策与行动中，人多未必好，意见多则相互牵扯，必有其一被损；反而一人独行时，由于立场清晰，更易遇到真正的同道之友。六四“损其疾，使遄有喜，无咎”则将“损”应用于“疾病与弊端”：减轻病根和结构缺陷，便能较快获得可喜之变，这是一种“治未病”的观念。

  六五“或益之十朋之龟，弗克违，元吉”转入“被动受益”的情形：当来自上位或外界的增益巨大而正当（如价值十朋之龟），便“不克违”——不能拒绝，这种增益反而是对前期合理减损的补偿与肯定。上九“弗损益之，无咎，贞吉，利有攸往，得臣无家”则总结全卦之旨：在最高位上不轻率再行削减或增益，而是保持既定格局的平衡，以“贞吉”的姿态出行行事，因得到忠臣辅佐，而将视野由小家扩展至天下公共。


#### L2 语义提取


- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_371]` `[trigger: 卦=损 AND 卦辞=有孚元吉]` `[factor_trigger: zhouyi_gua_sun AND zhouyi_guaci]` `[role: 主干]` 损，有孚，元吉：以诚信而损，终得大吉。 → 《周易·损卦·卦辞》
  - `[ns_zhouyi_372]` `[trigger: 卦=损 AND 彖传]` `[factor_trigger: zhouyi_gua_sun AND zhouyi_tuan AND zhouyi_sunyi_chengdu]` `[role: 主干依赖]` 损下益上，其道上行。 → 《周易·损卦·彖传》
  - `[ns_zhouyi_373]` `[trigger: 卦=损 AND 象传=山下有泽]` `[factor_trigger: zhouyi_gua_sun AND zhouyi_xiang]` `[role: 主干依赖]` 山下有泽，损；君子以惩忿窒欲：以损抑怒欲。 → 《周易·损卦·象传》
  - `[ns_zhouyi_374]` `[trigger: 卦=损 AND 初九=已事遄往]` `[factor_trigger: zhouyi_gua_sun]` `[role: 条件分支]` 已事遄往，无咎：事毕速往，以助他人。 → 《周易·损卦·爻辞》
  - `[ns_zhouyi_375]` `[trigger: 卦=损 AND 九二=利贞征凶]` `[factor_trigger: zhouyi_gua_sun]` `[role: 例外处理]` 利贞，征凶：守正则利，轻举则凶。 → 《周易·损卦·爻辞》
  - `[ns_zhouyi_376]` `[trigger: 卦=损 AND 六三=三人行则损一人]` `[factor_trigger: zhouyi_gua_sun]` `[role: 条件分支]` 三人行则损一人，一人行则得其友：损以求专一。 → 《周易·损卦·爻辞》
  - `[ns_zhouyi_377]` `[trigger: 卦=损 AND 六四=损其疾]` `[factor_trigger: zhouyi_gua_sun]` `[role: 条件分支]` 损其疾，使遄有喜：损去疾病，速有喜庆。 → 《周易·损卦·爻辞》
  - `[ns_zhouyi_378]` `[trigger: 卦=损 AND 六五=或益之十朋之龟]` `[factor_trigger: zhouyi_gua_sun]` `[role: 主干依赖]` 或益之十朋之龟，弗克违：天佑以益，不可违逆。 → 《周易·损卦·爻辞》
  - `[ns_zhouyi_379]` `[trigger: 卦=损 AND 上九=弗损益之]` `[factor_trigger: zhouyi_gua_sun]` `[role: 总结]` 弗损益之，无咎：不损反益，无所咎责。 → 《周易·损卦·爻辞》
  - **中文**：
  - 卦辞"损：有孚，元吉，无咎，可贞，利有攸往。曷之用？二簋可用享"依通行王弼本；"损"为减损，艮山在上、兑泽在下。
  - "山下有泽"谓山居高而泽润下，损下以益上之象。
  - "惩忿窒欲"谓君子当损去忿怒、塞窒私欲，以修身养德。
  - "二簋可用享"之"簋"为盛食之器，二簋虽简，诚意足以祭享，示俭约不废诚敬。
  - "三人行则损一人，一人行则得其友"以数言损益之理：多则散，专则合。
  - "十朋之龟"为极贵重之龟，天之大益，不可违逆。
  - **English**: Based on Wang Bi commentary edition. "损" means decrease/sacrifice. "惩忿窒欲" advises controlling anger and desire. "二簋" (two baskets) symbolizes sincerity over lavishness. "三人/一人" shows concentration brings gain. "十朋之龟" represents heaven's great gift."""
    normalized_text_zh: str = """"""
    subject: str = "损卦（䷨）"
    factor_refs: list = ['zhouyi_gua_041', 'principle_decrease_below_benefit_above_proposal', 'principle_restrain_anger_desire_proposal', 'symbol_two_bowls_proposal', 'principle_decrease_with_sincerity_proposal']
    
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
        l1_anchor="zy_v1.0.0_损卦_001_L1",
    )
    version: str = "1.0.0"
