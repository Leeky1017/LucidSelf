"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101211
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
    semantic_id="smth_v1.0.0_十干禄总论_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十干禄总论(SemanticEntry):
    """
    - **原文（source_text）**：
  禄，爵禄也，当得势而享，乃谓之禄。自始分十干、十二支时，便以甲乙配同寅卯，居东；丙丁配同巳午，居南；庚辛配同申酉，居西；壬癸配同亥子，居北。十干就支神...
    """
    
    original_text: str = """- **原文（source_text）**：
  禄，爵禄也，当得势而享，乃谓之禄。自始分十干、十二支时，便以甲乙配同寅卯，居东；丙丁配同巳午，居南；庚辛配同申酉，居西；壬癸配同亥子，居北。十干就支神为禄，谓禄随旺行：所以甲禄寅，乙禄卯，庚禄申，辛禄酉，壬禄亥，癸禄子，丙禄巳，丁禄午，戊寄巳，己寄午，谓巳午乃火旺之乡，子随母得禄之义。内有辰戌丑未：辰戌为魁罡，名曰边鄙恶地，禄元不寄；丑未乃天乙贵人出入之门，禄元避之，所以四宫无禄。又曰：四季有杂气，为禄不专，故不取。

- **分字分词释义**：
  - **禄**：本义为爵禄、俸禄，引申为五行在特定支位上「得势而享」之处。
  - **禄随旺行**：禄位随当令旺气而安置，十干各以一支为正禄。
  - **戊寄巳、己寄午**：戊己无固定禄支，而寄禄于巳午火旺之乡，取「子随母得禄」之义。
  - **四宫无禄**：辰戌丑未四库为杂气与贵人门户之地，禄不专，不取为本禄。

- **规范化释义（primary_lang_explained）**：
  本段先界定「禄」的含义：本为人事中的爵禄、俸禄，在命理中则指十干在某一地支上得势享用之位。十干与十二支一开始就按方位配对：甲乙同寅卯居东方，丙丁同巳午居南方，庚辛同申酉居西方，壬癸同亥子居北方。于是就有甲禄寅、乙禄卯、庚禄申、辛禄酉、壬禄亥、癸禄子、丙禄巳、丁禄午之说。戊己二土则寄禄于巳午火地,取「子随母旺」之象。至于辰戌丑未四库，因为魁罡恶地或贵人出入之门户，气杂不专，因此不立为正禄位。

- **完整对等诠释（secondary_lang_full）**：
  Lu, or "salary and rank", is the point where a Heavenly Stem truly holds power and can enjoy what it controls. When the ten Heavenly Stems and twelve Earthly Branches were first arranged, Jia and Yi were paired with Yin and Mao in the east, Bing and Ding with Si and Wu in the south, Geng and Xin with Shen and You in the west, and Ren and Gui with Hai and Zi in the north.
  Each stem takes its matching branch as its Lu, so we speak of Jia having Lu in Yin, Yi in Mao, Geng in Shen, Xin in You, Ren in Hai, Gui in Zi, Bing in Si and Ding in Wu. Wu Earth and Ji Earth do not own an independent Lu branch and are said to lodge their Lu in Si and Wu, borrowing the fiery territory where they are born and raised.
  The four storage branches Chen, Xu, Chou and Wei are treated either as harsh, mixed places or as gates through which noble stars come and go, so the root of Lu avoids them and they are not counted as true Lu positions.
- **核心要点**：
  - 十干禄位，是干在支上的「权力与资源聚集点」，可视作干的天然根据地。
  - 戊己寄禄，说明土之权柄多寓于火势所及之处，不能孤立看土，而要看其所依之火局。
  - 命盘中天干得其禄位，多主有根有势；无禄或禄被破，则需进一步看格局与用神，不能简单断凶。

- **详细解说**：
  1) 在建模与判盘时，先按「干→禄支」的固定映射（甲寅、乙卯、丙巳、丁午、戊巳、己午、庚申、辛酉、壬亥、癸子）为每个天干标注其禄位支；
  2) 对日主，重点检查：命局是否见本禄支、是否坐禄（日支即禄）、是否有他干来占据或合夺禄位，并将这些情况编码为不同的配置标签（如「坐禄」「夺禄」「寄禄」）；
  3) 结合节令与旺衰，对「有禄」的有效程度加权：当令之季、得地之支上的禄权重更高；反之在休囚死地虽有禄名，权重应打折；
  4) 在应用层，将禄结构更多用于刻画「资源与根据地」维度，如岗位稳定度、可支配资源、社会支持度，而不是直接推导财富或官位结果。

- 反例与边界：
  - 不宜一见「有禄」便断为「必有官、必富贵」，更不能据此预言具体职级与金额；
  - 不可将「四库无禄」机械理解为人生失败，库地本身在许多格局中反而是收束与蓄积之所；
  - 工程实现中若把「有禄/无禄」当作强决定特征，而忽略用神、格局、运势，将导致模型过度依赖单一标签、解释僵化；
  - 反向误区是完全忽略禄位，只看数值强弱，失去对「资源集中点」这一古典结构的利用价值。

- 小例（示意）：
  - 某命局甲日坐寅，又见他柱寅木成局，系统可标记为「日主坐禄且禄根重」，在解释中说明其在关键领域容易拥有稳定根据地与资源承载，但仍需结合官杀、财星判断实际职位高低；
  - 另一命局日主无禄而财官旺，并有清晰的学堂、贵人结构，系统则提示：此类命例虽不靠「本干禄位」取胜，但可依托平台与制度取得发展，不宜因「无禄」标签做消极判断。"""
    normalized_text_zh: str = """"""
    subject: str = "十干禄总论"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_42', 'bazi_semantic', 'bazi_state_day_master_marker', 'bazi_semantic', 'bazi_state_marker', 'bazi_semantic', 'bazi_wu_ji', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_十干禄总论_001_L1",
    )
    version: str = "1.0.0"
