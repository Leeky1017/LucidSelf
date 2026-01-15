"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101302
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
    semantic_id="smth_v1.0.0_戊禄巳_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊禄巳(SemanticEntry):
    """
    - **原文（source_text）**：
  戊禄巳。见己巳，九天库禄，壬吉。辛巳，截路空亡。癸巳，贵神禄，戊癸化合，有官位重。乙巳，驿马同乡禄。丁巳，旺库禄，俱吉。

- **分字分词释义**：...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊禄巳。见己巳，九天库禄，壬吉。辛巳，截路空亡。癸巳，贵神禄，戊癸化合，有官位重。乙巳，驿马同乡禄。丁巳，旺库禄，俱吉。

- **分字分词释义**：
  - **戊禄巳**：与丙禄巳类似，皆在巳火之地得禄，偏重土承火势。
  - **贵神禄**：贵人与禄同宫，且与日主相合，主职位尊显。
  - **驿马同乡禄**：禄位兼具驿马动象，主外出与变动中得利。

- **规范化释义（primary_lang_explained）**：
  戊土禄在巳。见己巳为「九天库禄」，两土同宫承火，主根基深厚。辛巳为截路空亡，凶。癸巳为「贵神禄」，又有戊癸化合之象，多主有官位且权责较重。乙巳为「驿马同乡禄」，利走动迁移。丁巳为「旺库禄」，火土俱旺，禄势坚固，主稳实之福。

- **完整对等诠释（secondary_lang_full）**：
  Wu Earth has its Lu in Si. When Wu stands with Ji-Si, two Earth stems share a palace while receiving Fire, forming the "Nine-Heaven Storage Lu" that indicates a deep foundation and strong backing.
  Xin-Si gives the "Cut-Path Void" structure and is judged as harmful. Gui-Si produces the "Noble-Spirit Lu" and at the same time the Wu-Gui combination, often showing formal office together with heavy responsibilities.
  Yi-Si is the "Post-Horse Same-Territory Lu", favourable for travel, relocation and work that moves between regions. Ding-Si yields a "Prosperous-Storage Lu" in which both Fire and Earth are vigorous and the Lu force is firm, pointing toward solid, steady kinds of good fortune.
- **核心要点**：
  - 戊禄巳在用神为土或官时，多有「厚载有权」之象；若火过旺、金水克制太重，则库中之禄反变为压力与包袱。
  - 现代建模可将「贵神禄」与「驿马禄」拆解为「权力密度」与「空间流动性」两种不同的禄用模式。

- **详细解说**：
  1) 确定日主为戊土，标出巳支所在柱位，并记录其上所透天干（己、辛、癸、乙、丁）；
  2) 将己巳、辛巳、癸巳、乙巳、丁巳分别归类为九天库禄、截路空亡、贵神禄、驿马同乡禄、旺库禄，细化为「资源厚薄」「官贵强度」「迁移机会」等子特征；
  3) 在职位与权力建模中，对贵神禄结构提高「责任/权柄」权重，对驿马禄结构提高「跨地域/跨部门」特征权重；
  4) 随行运变化，当巳地或相关火土局被强化时，系统动态调整「权力密度」与「压力负荷」，并结合日主承载力给出预警或鼓励。

- 反例与边界：
  - 不宜一见贵神禄就绝对化为「高官厚禄」，现实中更多是「责任重、不可轻易下车」的结构；
  - 不能把驿马禄一味理解为频繁调动好事，长期高频迁移对家庭与身心亦有成本；
  - 工程上若不区分「库」与「压」，可能将「资源丰厚但高度捆绑」与「真正自由可调动的资源」混为一谈；
  - 反向误区则是只看到「包袱」，忽略这类禄在稳住局面、托举团队方面的积极作用。

- 小例（示意）：
  - 某戊日命，命中癸巳贵神禄，行运再逢官印旺地，系统可解读为「在稳定机构中承担要职、权责极重」的周期，并同时提示其注意健康与家庭平衡；
  - 另一戊日命，乙巳驿马禄、行运多见出差外派，系统则强调其「跨区域资源统筹」能力，但提醒适时为家人与自身预留静养时间，以免长期处于高压流动状态。"""
    normalized_text_zh: str = """"""
    subject: str = "戊禄巳"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_wu_si', 'bazi_semantic', 'bazi_state_marker_9', 'bazi_semantic', 'bazi_state_yima_marker_1', 'bazi_semantic', 'bazi_state_factor_103', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_戊禄巳_001_L1",
    )
    version: str = "1.0.0"
