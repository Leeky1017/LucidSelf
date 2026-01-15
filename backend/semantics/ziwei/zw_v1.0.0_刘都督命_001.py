"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699882
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
    semantic_id="zw_v1.0.0_刘都督命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 刘都督命(SemanticEntry):
    """
    - 分字分词释义：

  - **杀破贪廉**：七杀、破军、贪狼、廉贞四星同局的强杀结构。
  - **俱作恶庙而不陷**：四杀星皆在恶庙位但不落陷，杀气得控。
  - **掌三军**：掌握全军指挥权...
    """
    
    original_text: str = """- 分字分词释义：

  - **杀破贪廉**：七杀、破军、贪狼、廉贞四星同局的强杀结构。
  - **俱作恶庙而不陷**：四杀星皆在恶庙位但不落陷，杀气得控。
  - **掌三军**：掌握全军指挥权的高权力位置。
  - **左右魁钺守照**：左右辅彼与天魁天钺守照命局，主贵人辅佐。
  - **文昌同垣**：文昌星与主星同垣，主文采谋略。
  - **寅辰羊陀**：寅、辰宫见擎羊与陀罗，主硬碰、阻滞与伤厄。
  - **阴男水二局**：刘都督命盘的五行局数，水二局主智慧武贵。

- **原文（source_text）**：  
  刘都督命。阴男水二局。杀破贪廉，俱作恶庙，而不陷掌三军，此命得之，况左右魁钺，守照文昌同垣，宜武职峥嵘。但寅、辰二宫见羊陀，宜威武中所有者美也。

- **规范化释义（primary_lang_explained）**：  
  刘都督命为阴男水二局，「杀破贪廉」四星同局且多在恶庙，本属极重杀气与波动的组合；但原文特言其「而不陷掌三军」，说明这些凶曜并未落陷，反而在得地之处转为统兵之勇与果断。再加上左右魁钺守照、文昌同垣，是典型「杀星配魁钺与文星」的武职高格，主掌军权、以武功著称。  
  然而命局亦提示风险：「寅、辰二宫见羊陀」，说明在部分方位仍有擎羊、陀罗之类的硬碰与阻滞，因此虽宜威武峥嵘，却也可能在强势中夹带伤厄与锋险。整体而言，是在强杀格中借魁钺与文星调和而成就高阶武职的命。

- **完整对等诠释（secondary_lang_full）**：  
  Liu, the Commander’s chart is that of a Yin Water native in the Second Configuration. The cluster of Sha Po Tan Lian—Qi Sha, Po Jun, Tan Lang and Lian Zhen—occupies powerful yet not fallen positions. In isolation this "quartet" would be volatile and dangerous, but here it "does not fall" and so channels into military command: he "holds the three armies." With Zuo‑You and Kui‑Yue assisting and Wen Chang in the same palace, the killing energy is framed by nobility and strategy, producing a formidable general rather than a mere brawler.  
  At the same time, the presence of Yang Blade and Tuo Luo in the Yin and Chen palaces marks zones of hardness and obstruction. The text notes that "within his martial might there is still something fine," suggesting that the harshness of these stars is partly sublimated into disciplined authority and awe. This case illustrates how a heavy‑kill configuration, when dignified and properly supported, yields a distinguished military career with both glory and inherent risk.

- **核心要点**：  
  1. 杀破贪廉同局而不陷，是掌三军、专精武职的高杀格。  
  2. 左右魁钺与文昌同垣，令杀气被纳入制度与谋略之内，而非纯粹暴烈。  
  3. 寅辰见羊陀，提示在赫赫军功背后仍伴随硬碰伤厄与锋险环境。"""
    normalized_text_zh: str = """"""
    subject: str = "刘都督命"
    factor_refs: list = ['pattern_sha_po_tan_lian', 'quality_emiao_buxian', 'result_zhang_sanjun', 'pattern_zuoyou_kuiyue_shouzhao', 'star_wenchang_tongyuan', 'malefic_yinchen_yangtuo']
    
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
        l1_anchor="zw_v1.0.0_刘都督命_001_L1",
    )
    version: str = "1.0.0"
