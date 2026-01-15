"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101397
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
    semantic_id="smth_v1.0.0_贵人昼夜与阴阳取用_001",
    book_id="sanming",
    engine_id="bazi"
)
class 贵人昼夜与阴阳取用(SemanticEntry):
    """
    - **原文（source_text）**：
  《壶中子》云：贵人分治昼夜，各自专权。以昼生遇昼贵，夜生遇夜贵，为得力。或以子后为昼，午后为夜；或以日出为昼，日入为夜，皆是臆说。不若只以寅申分阴阳：...
    """
    
    original_text: str = """- **原文（source_text）**：
  《壶中子》云：贵人分治昼夜，各自专权。以昼生遇昼贵，夜生遇夜贵，为得力。或以子后为昼，午后为夜；或以日出为昼，日入为夜，皆是臆说。不若只以寅申分阴阳：冬至后用阳贵，夏至后阴贵。人命一阳生后遇阳贵为得力，一阴生后遇阴贵为得力。《三车一览》则以甲阳木乘少阳之气生乎东方，至巳而用事毕矣，故退藏于未而为贵。庚阳金乘少阴之气而生乎西，至亥而用事毕矣，故退藏于丑而为贵。戊阳土冲和中央，播于四时：甲因之，万物生；庚因之，万物成，则生成之理毕矣。乙乃阴木，己乃阴土，二位无气失类而无所居，必待申子生旺水土滋养，充实补助不足，此二者喜见申子而为贵。丙丁之火，当盛夏至酷而害万物，性熄于酉，藏于亥，以西北成齐之气而和，此二者以酉亥阴气和而为贵。壬癸之水，至穷冬则其性严而杀万物，惟啬于卯，潜于巳，以东南温燠之气而和，此二者以巳卯阳气和而为贵。辛乃阴金，执方不能自化，须假寅午生旺之火锉刚革而成形为贵。

- **分字分词释义**：
  - **以寅申分阴阳**：弃日夜分贵之说，而以冬至后「阳生」、夏至后「阴生」来分用阳贵、阴贵。
  - **阳干退藏之贵**：甲、戊、庚等阳干在各自用事终了后退藏于未、丑等位，成天乙之贵位。
  - **阴干补气之贵**：乙、己、辛等阴干须借申子、寅午之气补足所缺，方能成贵。

- **规范化释义（primary_lang_explained）**：
  这一段辨析了各种关于「昼夜贵人」的说法，认为用子后/午后或日出/日入区分昼夜贵，多属臆测，不如以寅申为阴阳分界更为合理：冬至后一阳始生，用阳贵；夏至后一阴始生，用阴贵。随后《三车一览》从甲、庚、戊等阳干的生旺与退藏处，推导出各自对应的贵位：甲木用事毕于巳而退藏未，庚金用事毕于亥而退藏丑，戊土调和四时之后，生成之理告成。乙木、己土等阴干则需申子之水土滋养，丙丁火需酉亥阴气和之，壬癸水需卯巳阳气暖之，辛金需寅午火以锉刚成器。每一干的贵位，实质上都是「用事既毕而得其和、得其补」之处。

- **完整对等诠释（secondary_lang_full）**：
  This section rejects crude day noble and night noble formulas and instead divides usage by the Yin Shen axis and the solstices, using yang nobles after Winter Solstice and yin nobles after Summer Solstice.
  For each stem it traces where its action ends and where it retires or is replenished, and these retreat or replenishment places are defined as noble positions.
  In modern modelling such positions are best treated as balance points where an element energy is moderated and supplemented, rather than as rigid labels tied only to clock time.
- **核心要点**：
  - 天乙贵人的取用，本质是寻找「五行气机得和、得补」之位，而非拘泥于昼夜、子午等表面划分。
  - 在工程建模中，可将贵位视作「和中点」：即对某干而言，气机由偏激转为平衡的位置，在此处安置贵人标签，更合原文精神。
 
- **详细解说**：
  1) 利用精确节气（冬至、夏至）与出生时间，判断命主属于「一阳既生之后」还是「一阴既生之后」，从而选择阳贵或阴贵的取用表；
   2) 结合日干，查表得到对应的贵位地支，并与前一节的基础天乙表统一存入同一结构，以免出现多套定义并行的混乱；
   3) 在特征工程中，为每一贵位标注其「和中度」：既考虑干支自身的退藏/补气含义，也考虑实际命局中该宫的旺衰与所临十神（印、财、官、食等）；
   4) 在解释层，对于落在和中点且又符合用神方向的贵位，可说明为「气机由偏激转和、利于缓冲极端」的结构，而不是单纯说「昼生遇昼贵为得力」这类口诀化语句。
 
- 反例与边界：
  - 不宜在工程实现中简单采用「子后/午后」「日出/日入」来划分昼夜贵，而忽略当地时区与真太阳时差异，否则会在边界时刻产生大量误判；
   - 不宜将任何带三公煞或旌钺煞的命局都解读为「大贵」或「必遭重刑」，应回到实际职业、行为模式与外部环境综合判断；
   - 若缺乏精确的出生时间与历法换算，强行细分日时神煞可能引入噪音，应有降级策略（仅使用月度层级或只启用德星而暂不启用细小煞）；
   - 工程上若把所有时日神煞一股脑加入模型而不做特征选择，会导致维度爆炸与解释困难，需要通过重要性分析筛选关键因子；
   - 反向误区是完全忽略时间特征，只看静盘，使系统对「特定时间窗口的宽宥或高压」缺乏表达能力。

- 小例（示意）：
  - 某命局逢天德月德并临之月，又值天赦日，现实中在那一阶段虽有违规风险却最终得到从轻处理，系统可用「德星 + 天赦提供宽宥窗口」来解释事件走向；
  - 另一命局在三公煞叠加的年份发生产业政策强监管与团队清洗，命主身居关键岗位，系统在事前就应提高该时间段的风险提示等级，并在解释中说明这是「制度高压与个人位置叠加」的结果。"""
    normalized_text_zh: str = """"""
    subject: str = "贵人昼夜与阴阳取用"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_49', 'bazi_semantic', 'bazi_state_marker_13', 'bazi_semantic', 'bazi_yanggan', 'bazi_semantic', 'bazi_yingan', 'bazi_semantic']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_贵人昼夜与阴阳取用_001_L1",
    )
    version: str = "1.0.0"
