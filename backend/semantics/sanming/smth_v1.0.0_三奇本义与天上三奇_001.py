"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101423
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
    semantic_id="smth_v1.0.0_三奇本义与天上三奇_001",
    book_id="sanming",
    engine_id="bazi"
)
class 三奇本义与天上三奇(SemanticEntry):
    """
    - **原文（source_text）**：
  论三奇。《珞琭子》曰：「奇为贵也；奇者，异也。」谓物以贵为奇也。乙丙丁出于贵人干德配支之妙：阴贵甲德起子，则乙德在丑，丙德在寅，丁德在卯，三干相连而无...
    """
    
    original_text: str = """- **原文（source_text）**：
  论三奇。《珞琭子》曰：「奇为贵也；奇者，异也。」谓物以贵为奇也。乙丙丁出于贵人干德配支之妙：阴贵甲德起子，则乙德在丑，丙德在寅，丁德在卯，三干相连而无间；阴贵甲德起申，乙在未，丙在午，丁在巳，三间相连而无间。以其随贵人在天，故曰「天上三奇」。十干惟此为异，余则或间罗网，或间天空，或不重临，又不相联，不可以为奇。《玉霄宝鉴》谓：古人以正月为岁之始，日出于乙，故以乙为日奇；老人星见为瑞，见于丁位，故以丁为星奇；月照夜到丙位而天下明，故以丙为月奇。

- **分字分词释义**：
  - **奇为贵 / 奇者异也**：奇的本义是「特别」「珍贵」，不是随便稀奇古怪皆称三奇。
  - **乙丙丁 / 甲戊庚**：传统所称天上三奇，最初指乙丙丁三干，与贵人干德配支相连不断。
  - **三干相连而无间**：在天干运行序列中连续出现，不被其他干隔断，象征气机纯粹、不断。

- **规范化释义（primary_lang_explained）**：
  三奇之「奇」，重在贵重而非常态。原文先以乙丙丁为例：在特定贵人起点下，乙、丙、丁三干依次落在丑、寅、卯或未、午、巳之上，形成「三干相连而无间」的结构，这就是所谓「天上三奇」。《玉霄宝鉴》又从日月星三光的角度，将乙称为日奇、丙为月奇、丁为星奇，进一步强化了乙丙丁三干的「光明之奇」。后世亦有以甲戊庚为天上三奇的说法，理由是其临丑未贵地，与贵人家在斗牛之次的布置相合。

- **完整对等诠释（secondary_lang_full）**：
  Sanqi, the Three Wonders, originally refers to very special continuous triplets of stems such as Yi, Bing and Ding linked with noble positions, not to any random collection of three favourable stems.
  In the classic description they form unbroken sequences and are associated with the luminous qualities of sun, moon and stars, so their core image is pure, concentrated and elevated qi.
  When they truly appear in a chart they mark highly focused talent or authority, but only if the surrounding structure is coherent and not riddled with gaps or mixed influences.
- **核心要点**：
  - 三奇强调的是「连续而纯粹的特定三干组合」，本质是气机不杂、力量集中，不是简单把任何三个好字堆在一起。
  - 在建模时，可把乙丙丁与甲戊庚两组视作两套三奇体系，分别标记其出现位置与连续性，用于刻画命局中「光明秀气」与「刚健权柄」两类潜质。

- **详细解说**：
  1) 在命盘结构中抽取年、月、日、时四柱天干序列，形成 `gan_sequence = [year, month, day, hour]`；
  2) 分别在该序列中搜索乙丙丁与甲戊庚的连续子序列（可容许部分缺失但须保持顺序），并记录其出现位置、是否跨越关键柱位（日、时）等信息；
  3) 对于完整顺布（如年乙、月丙、日丁）与「主轴顺布」（如日乙、时丙，或日戊、时庚）分别赋予不同权重，映射为「光明型三奇」「权柄型三奇」等标签；
  4) 在特征层将三奇标记作为「高集中度气机」信号，主要用于刻画才智集中度、目标感与行动一贯性，而不是直接推断具体官职或财富等级。

- 反例与边界：
  - 不宜将任何出现乙、丙、丁或甲、戊、庚的命局都视为三奇，必须满足「同组三干」「顺序关联」等结构条件；
  - 不能把乙丙丁一概等同文贵、甲戊庚一概等同武贵，在现代社会应联系行业、教育与现实角色重新标定其意义；
  - 工程上若只用「是否有三奇」的布尔特征，而不记录其落在年/月/日/时何处，会丢失大量关于「奇气落点」的差异信息；
  - 反向误区是完全忽略三奇，将其视为古人臆造标签，而放弃对「少数高集中度格局」的识别能力。

- 小例（示意）：
  - 某命局年乙、月丙、日丁顺布，且三干多与印、食相关，系统可将其归类为「光明型三奇」，在解释中偏重其学习能力、表达力与审美创造力，但不必直接承诺高官厚禄；
  - 另一命局日甲、时戊、年庚构成局部甲戊庚链条，多与权柄、决断相关，系统可提示其在组织与资源调度方面的潜质，同时提醒若整体五行失衡，则这股集中力量也可能放大风险。"""
    normalized_text_zh: str = """"""
    subject: str = "三奇本义与天上三奇"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'new_candidate', 'bazi_semantic', 'bazi_state_factor_121', 'bazi_semantic', 'bazi_function_factor_1', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_三奇本义与天上三奇_001_L1",
    )
    version: str = "1.0.0"
