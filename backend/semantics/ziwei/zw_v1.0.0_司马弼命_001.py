"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699668
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
    semantic_id="zw_v1.0.0_司马弼命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 司马弼命(SemanticEntry):
    """
    - 分字分词释义：

  - **权禄会合**：权星与禄星同宫或互拱，主权位与俸禄并增。
  - **左右同宫**：左辅右彼同宫，主贵人扶持与内部助力。
  - **少年贵题**：少年即显清贵与仕途机...
    """
    
    original_text: str = """- 分字分词释义：

  - **权禄会合**：权星与禄星同宫或互拱，主权位与俸禄并增。
  - **左右同宫**：左辅右彼同宫，主贵人扶持与内部助力。
  - **少年贵题**：少年即显清贵与仕途机会的格局。
  - **命逢化忌**：命垣逢化忌转化，主损耗、纠纷与隐患。
  - **大限地网**：大限行至地支或凶曜形成的网状困局，主受困与阻塞。
  - **丧门白虎**：与丧事、血光与损伤相关的一对凶曜。
  - **阳男水二局**：司马弼命盘的五行局数，水二局主智慧早发。

- **原文（source_text）**：  
  司马弼命。阳男水二局。权禄会合，左右同宫，少年贵题，命逢化忌，大限地网，小限巳亥寅，生人有忌，丧门、白虎为残，其死必矣，故亡于二十六岁。

- **规范化释义（primary_lang_explained）**：  
  司马弼命为阳男水二局，命局中权星与禄星会合，左右辅弼同宫，是「权禄会合、左右同宫」的少年贵题格局，主早发科名与仕途机会，少年即有清贵之象。  
  然而，命逢化忌，说明在结构吉美之下隐含破损之势。大限行至地网之地，小限又轮行巳、亥、寅等对该命局不利的方位，并逢丧门、白虎等丧曜杀曜，是「地网 + 化忌 + 丧门白虎」叠加的高危结构。结果在二十六岁夭亡，形成「少年得志而早折」的命例，对同类少年贵格具有警示意义。

- **完整对等诠释（secondary_lang_full）**：  
  Sima Bi's chart is that of a Yang Water native in the Second Configuration. With Power and Lu stars combining and Left and Right Assistants in the same palace, the pattern "Quan‑Lu united, Zuo‑You together" marks early honours and official prospects. It is a classic "young noble" structure, promising examination success and early advancement.  
  Yet the chart also encounters Hua Ji, indicating underlying capacity for loss or damage. The major period moves into an Earthly Net region while the minor periods traverse Si, Hai and Yin, directions deemed inauspicious for this native, and Sang Men with Bai Hu appear as funeral and predatory stars. This combination—Earth Net plus Hua Ji plus Sang Men and Bai Hu—creates a sharply dangerous configuration, and the text records death at twenty‑six. The example portrays a youth who rises quickly only to die prematurely, serving as a cautionary instance for similar early‑noble charts.

- **核心要点**：  
  1. 权禄会合、左右同宫，是少年贵题与早发科名的吉格。  
  2. 命逢化忌，大限地网，小限巳亥寅并见丧门白虎，构成早年极高风险。  
  3. 命例刻画「少年得志而早夭」的命局路径。

- **叙事素材（narrative_snippets）**：  
  - **少年贵题**："权禄会合，左右同宫，少年贵题"，司马弼命主自少年即具贵气与仕途机会。  
  - **化忌地网**："命逢化忌，大限地网"，吉格之下暗藏化忌与地网，使早年运势本就带有折损潜势。  
  - **丧门白虎**："小限巳亥寅，生人有忌，丧门、白虎为残，其死必矣"，小限行巳亥寅并逢丧门白虎，是二十六岁早夭的直接触发结构。  
  - **现代应用**：对很早就取得光鲜头衔或资源的年轻人而言，若命局同时带化忌与丧曜组合，需要格外注意在高危年龄段不要过度冒进、飙车、熬夜或参与高风险项目，以免「少年成名却寿不永」。"""
    normalized_text_zh: str = """"""
    subject: str = "司马弼命"
    factor_refs: list = ['pattern_quanlu_huihe', 'pattern_zuoyou_tonggong', 'pattern_shaonian_guiti', 'transform_huaji', 'malefic_diwang', 'malefic_sangmen_baihu']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_司马弼命_001_L1",
    )
    version: str = "1.0.0"
