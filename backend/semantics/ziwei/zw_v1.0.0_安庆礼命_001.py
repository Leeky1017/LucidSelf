"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699460
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
    semantic_id="zw_v1.0.0_安庆礼命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安庆礼命(SemanticEntry):
    """
    - 分字分词释义：

  - **科禄加会**：科星与禄星同会命宫，主科名与俸禄兼收。
  - **左右扶持**：左辅右彼同来扶持命宫，主贵人相助、所求称意。
  - **富贵全美**：科禄加左右的近...
    """
    
    original_text: str = """- 分字分词释义：

  - **科禄加会**：科星与禄星同会命宫，主科名与俸禄兼收。
  - **左右扶持**：左辅右彼同来扶持命宫，主贵人相助、所求称意。
  - **富贵全美**：科禄加左右的近乎完美格局。
  - **申人忌铃星**：申年生人逢铃星时凶象额外加重。
  - **天刑天伤天哭**：代表刑罚、伤病与悲痛的三类星曜。
  - **小限在天使之地**：小限行至天使所在宫位，主急变或生死相关事件。
  - **阳男火六局**：安庆礼命盘的五行局数，火六局主热情执行。

- **原文（source_text）**：  
  安庆礼命。阳男火六局。科禄加会，左右扶持，皆得称意，富贵全美。流年太岁大限入戌，申人忌铃星，且芜天刑、天伤、天哭，小限又在天使之地，俱为倒寿之年也。

- **规范化释义（primary_lang_explained）**：  
  安庆礼为阳男火六局，命宫得科星、禄星加会，再逢左辅、右弼扶持，是典型「科禄加会、左右朝垣」的富贵全美格局：一生多有科名、声誉与实利，做事顺势而上，所求多得。  
  然而原文也指出其寿元隐忧：当流年太岁与大限同入戌宫时，对申人而言铃星尤为凶烈，再加天刑、天伤、天哭等一系列刑伤与悲耗之星聚集，小限又行至天使之地，形成「诸凶会集 + 倒寿年份」的组合。此时既有外在环境的高压与事故风险，也有身体与情绪层面的消耗，一旦触发往往难以无事度过，导致本来「富贵全美」的人生在特定年份被截短。

- **完整对等诠释（secondary_lang_full）**：  
  An Qingli’s chart belongs to a Yang Fire native whose Life palace enjoys the joint presence of Academic and Salary stars, supported by Left and Right Assistants. This "Ke‑Lu with assistants" structure underpins a life of recognition, examinations going well and material ease—hence the description "wealth and honour in full perfection."  
  But the text also isolates a cluster of dangerous years. When the Annual Tai Sui and the major period both enter Xu, the bell star Ling becomes particularly ominous for those of the Shen branch. Together with punitive and wounding stars such as Tian Xing, Tian Shang and Tian Ku, and with the minor period moving through the "Heavenly Envoy" sector, a dense concentration of malefics arises. In such years external pressure, legal or medical crises and emotional strain combine, making it difficult for even a well‑endowed life to pass through safely. The case illustrates how a chart of nearly flawless fortune can still be cut short by a few heavily loaded "life‑reversal" years.

- **核心要点**：  
  1. 科禄加会、左右扶持，构成近乎「富贵全美」的上佳格局。  
  2. 对申人而言，铃星配合天刑、天伤、天哭等刑伤星在特定戌年格外凶猛。  
  3. 流年太岁与大限同入戌，小限又行天使之地，形成多重凶象叠加的倒寿年份。

- **叙事素材（narrative_snippets）**：
  - **富贵全美**："科禄加会，左右扶持，皆得称意，富贵全美"，安庆礼命主一生顺遂、所求多得。
  - **申人忌铃**："流年太岁大限入戌，申人忌铃星"，点明申年生人逢铃星戌限时格外危险。
  - **诸凶会集**："且芜天刑、天伤、天哭，小限又在天使之地，俱为倒寿之年也"，多重刑伤悲耗星与天使同至，为寿元承压之年。
  - **现代应用**：对格局近乎完美的人而言，更要在「看似不会出事」的年份保持警惕：尤其当个人出生支所忌之星（如铃星）与刑伤、病耗同会时，宜降低工作强度与高风险投资，留出冗余空间。"""
    normalized_text_zh: str = """"""
    subject: str = "安庆礼命"
    factor_refs: list = ['pattern_kelu_jiahui', 'pattern_zuoyou_fuchi', 'malefic_lingxing', 'taboo_shenren_lingxing', 'malefic_xingshangku', 'position_tianshi']
    
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
        l1_anchor="zw_v1.0.0_安庆礼命_001_L1",
    )
    version: str = "1.0.0"
