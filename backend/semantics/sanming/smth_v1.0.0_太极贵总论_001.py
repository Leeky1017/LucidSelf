"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101471
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
    semantic_id="smth_v1.0.0_太极贵总论_001",
    book_id="sanming",
    engine_id="bazi"
)
class 太极贵总论(SemanticEntry):
    """
    - **原文（source_text）**：
  论太极贵。太极者，太初也，始也，物造于初为太极；成也，收也，物有所归曰极。造化始终相保，乃曰太极贵也。甲乙木先造乎子，坎水助而生，后终乎午，离火焚而死...
    """
    
    original_text: str = """- **原文（source_text）**：
  论太极贵。太极者，太初也，始也，物造于初为太极；成也，收也，物有所归曰极。造化始终相保，乃曰太极贵也。甲乙木先造乎子，坎水助而生，后终乎午，离火焚而死。丙丁火先喜出乎震，卯也，后喜藏乎兑，酉也。庚辛金得寅，乃金生乎艮，见亥乃金庙乎乾。壬癸水先得子而生，后得巳而纳。经曰：「地陷东南，四渎俱流巽位，皆有始有终之意。」戊己，土也，喜生乎申，得辰戌丑未为正库。《理愚歌》云：「四库全时为至贵，位班上列据权衡。」人命入格，更有福气贵神扶，岂不为美。

- **分字分词释义**：
  - **太极贵**：取「有始有终」之意，五行各得生处与归处，始终相保，是为贵格。
  - **先造乎子 / 出乎震 / 得寅 / 先得子**：分别指木、火、金、水各自的生发处。
  - **终乎午 / 藏乎兑 / 见亥 / 得巳而纳**：对应其收束与归藏之地。
  - **四库全时为至贵**：辰戌丑未四库齐备、各得其位时，为太极贵中之上品。

- **规范化释义（primary_lang_explained）**：
  太极贵从造化始终的角度来立格：太极为万物之始，极为万物之归。甲乙木自子位得水助而生，终于午火焚而尽；丙丁火自震卯而出，藏于兑酉而收；庚辛金得寅艮之生，至亥乾之庙而极；壬癸水得子而生，至巳而纳；戊己土则喜生于申，归于四库辰戌丑未。若人命中五行各得其「始」与「终」，又兼四库齐全，则其一生多有始有终、能善始善终，是为太极贵。再有福星贵神相扶，则更加美备。

- **完整对等诠释（secondary_lang_full）**：
  Taiji Noble is founded on the idea that each element should have both a clear place of emergence and a clear place of return, so that creation and completion protect one another.
  A chart approaches this noble pattern when many elements simultaneously show both their starting and ending branches and when the four storage branches are present yet not chaotic or over damaged.
  In contemporary terms it points to integrity of life cycles and the ability to bring long processes to completion, which is closer to capacity for closure and stewardship than to simple wealth or rank.
- **核心要点**：
  - 太极贵重在「始终相保」，不以一时之旺衰论吉凶，而看五行是否各得其生处与归处。
  - 四库全而不杂，是格局稳定与收束有度的重要信号，在系统建模中，可视为「完备度与收官能力」的高评分结构。
 
- **详细解说**：
  1) 在排盘时，为每一五行标注其「生处」与「归处」支位，并在命局中检查是否真实落点或通过合化间接实现，形成 `start_end_pairs` 结构；
   2) 计算每一五行的「始终完整度」，例如同时具备生处与归处记为 1，仅具其一记为 0.5，全无则为 0，并综合成 `taiji_integrity_score`；
   3) 检查辰戌丑未四库是否齐备、是否为用神或中性之神，并结合是否被冲破、空亡，形成 `si_ku_completeness_score`；
   4) 在高层特征中，将太极贵视为「人生路径完备度与收官能力」的加权因子，用于解释「能否善始善终」「是否擅长长周期项目」等维度，而非直接作为富贵等级的决定性标签。

 - 反例与边界：
   - 不宜只因命局见一两个「始」或「终」位置，就草率认定入太极贵格，应有最低完整度门槛（如多行始终俱备且四库不破）才视为格成；
   - 若四库虽全却全部为忌神，或因刑冲合害而极度混杂，在工程上应将其解读为「业力收束」而非纯吉结构，避免把沉重收官压力美化为贵格；
   - 不能忽略现实时间维度，只凭静盘太极贵就断定晚年一定无忧，应结合大运流年与实际资源状态综合判断；
   - 反向误区是将太极贵仅当作古书夸饰，而完全不建模「始终相保」这一维度，使系统难以表达长期规划能力与收尾能力的差异。

 - 小例（示意）：
   - 某命局五行多能各得其生处与归处，四库亦清纯不杂，现实中表现为「做事有始有终、能扛长期项目」，系统可在职业建议中偏向长周期工程、科研或管理岗位，并提示其收官能力是优势；
  - 另一命局仅在少数五行上具备始终，且四库混杂受冲，现实呈现为「开局积极但常难以收尾」，系统则在解释中把太极相关特征视作局部补强，而非整体贵格，并提醒在项目管理与收尾阶段需额外注意。"""
    normalized_text_zh: str = """"""
    subject: str = "太极贵总论"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_2', 'bazi_semantic', 'bazi_state_factor_131', 'bazi_semantic', 'bazi_function_factor_4', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_太极贵总论_001_L1",
    )
    version: str = "1.0.0"
