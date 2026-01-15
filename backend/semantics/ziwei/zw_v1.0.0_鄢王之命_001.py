"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699620
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
    semantic_id="zw_v1.0.0_鄢王之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 鄢王之命(SemanticEntry):
    """
    - 分字分词释义：

  - **贪武同行**：贪狼与武曲同宫或互对，主财富与武职并重。
  - **左右对守**：左辅右彼分居命宫两侧或对守，主贵人护持。
  - **太岁到寅**：太岁行至寅位，为...
    """
    
    original_text: str = """- 分字分词释义：

  - **贪武同行**：贪狼与武曲同宫或互对，主财富与武职并重。
  - **左右对守**：左辅右彼分居命宫两侧或对守，主贵人护持。
  - **太岁到寅**：太岁行至寅位，为特定生人之忌地。
  - **火星凶矣**：火星临寅位时凶性大增，易致突发灾祸。
  - **小限天罗**：小限行至天罗之位，主缠绕困顿与难脱之局。
  - **猴人作鬼**：申年或申时之人遇特定凶运而易有死亡之虑。
  - **阳男木三局**：鄢王命盘的五行局数，木三局主生发财武。

- **原文（source_text）**：  
  鄢王之命。阳男木三局。贪武同行，左右对守，本为吉命，一生坐享富贵。六十七岁，太岁到寅，火星凶矣，小限天罗，猴人作鬼，是凶。

- **规范化释义（primary_lang_explained）**：  
  鄢王命为阳男木三局，「贪武同行，左右对守」指贪狼与武曲同宫或互对，并得左右夹辅，是富贵而带武职意味的吉命，一生坐享富贵。命主体质强健，胆识与开拓力兼具。  
  然而，在六十七岁这一节点，太岁行至寅位，火星临之而显凶，小限又逢天罗，原文言「猴人作鬼」，点出申猴之人遇此组合格外不利。这是「火星 + 太岁寅位 + 天罗」叠加的高危运：一方面象征外界突发火爆事件或意外，另一方面代表天罗网住命局，使其难以逃脱。于是命主于此年死亡。命例刻画「贪武左右富贵格在迟暮遭遇火星与天罗之灾」的格局。

- **完整对等诠释（secondary_lang_full）**：  
  Yan Wang’s chart is that of a Yang Wood native in the Third Configuration. With Tan Lang and Wu Qu "travelling together" and Left and Right Assistants facing each other, the pattern blends wealth, martial capacity and supportive networks, enabling a life of "sitting and enjoying riches." The native is marked by courage, initiative and access to resources.  
  At sixty‑seven, however, the Annual Tai Sui moves into Yin where Huo Xing shows its malefic face, and the minor period encounters Tian Luo. The text notes that "Monkey people become ghosts," underscoring the particular danger when this combination meets those of the Shen branch. The fusion of fiery malefic (Huo Xing) with the net‑like Tian Luo describes sudden, potentially fatal events from which escape is difficult. The example shows a person long accustomed to comfort and advantage whose life ends in late years under a harsh, constricting fire‑net transit.

- **核心要点**：  
  1. 贪武同行、左右对守，为富贵带武职意味的吉命，一生坐享富贵。  
  2. 六十七岁太岁到寅，火星显凶，小限天罗，尤其对申人（猴人）极为不利。  
  3. 命例展现「富贵格在迟暮遭火星与天罗之灾而亡」的形态。

- **叙事素材（narrative_snippets）**：
  - **贪武左右**："贪武同行，左右对守，本为吉命，一生坐享富贵"，鄢王命主以贪狼、武曲配左右，兼具财富、武职与享受。
  - **寅火天罗**："六十七岁，太岁到寅，火星凶矣，小限天罗"，火星在寅位显凶，加小限天罗，构成晚年火灾、事故或突发性变故的高危组合。
  - **猴人作鬼**："猴人作鬼，是凶"，特别提醒申年或申时之人遇此组合时，死亡风险显著放大。
  - **现代应用**：对晚年仍热衷出行、投资或亲自参与高风险事务的富贵命主而言，在火星 + 天罗年份应主动降低出行频次与危险行为，并改善居家防火与安全设施，避免「老来一场大意失足」。"""
    normalized_text_zh: str = """"""
    subject: str = "鄢王之命"
    factor_refs: list = ['pattern_tanwu_tongxing', 'pattern_zuoyou_duishou', 'timing_taisui_yin', 'malefic_huoxing_yin', 'timing_xiaoxian_tianluo', 'condition_houren_zuogui']
    
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
        l1_anchor="zw_v1.0.0_鄢王之命_001_L1",
    )
    version: str = "1.0.0"
