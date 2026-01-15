"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699717
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
    semantic_id="zw_v1.0.0_石崇富命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 石崇富命(SemanticEntry):
    """
    - 分字分词释义：

  - **权禄守财**：权星与禄星守于财帛宫，主掌控巨额资源与收益。
  - **昌武曲拱命**：文昌与武曲同拱命垣，主文武兼备与财禄丰厚。
  - **巨富之命**：命局具备...
    """
    
    original_text: str = """- 分字分词释义：

  - **权禄守财**：权星与禄星守于财帛宫，主掌控巨额资源与收益。
  - **昌武曲拱命**：文昌与武曲同拱命垣，主文武兼备与财禄丰厚。
  - **巨富之命**：命局具备巨额财富累积的结构特征。
  - **天空天伤**：虚空与伤曜同见，主虚耗、事故与突发伤害。
  - **天使夹耗**：天使与耗损类星形成夹局，主职位压力与资源被消耗。
  - **太岁逢劫**：太岁与劫星同临，主该年突发损失与掠夺。
  - **阳男木三局**：石崇富命盘的五行局数，木三局主生发巨富。

- **原文（source_text）**：  
  石崇富命。阳男木三局。处世荣华，权禄守财，福之莅文。昌武曲俱拱命垣，为巨富之命。大限四十三岁，入于天空天伤之地。四十四岁，小限入于天使夹耗之地，又兼太岁逢劫，故死。

- **规范化释义（primary_lang_explained）**：  
  石崇富命为阳男木三局，「处世荣华，权禄守财」言其一生处在富贵环境中，权星、禄星守于财帛与命垣，福星与文星同来会照，昌曲与武曲拱命，为「权禄守财 + 昌武曲拱命」的巨富结构，典型「石崇式豪富」之象。  
  然而大限于四十三岁行入「天空天伤之地」，天空主虚耗、天伤主病损与突发伤害；四十四岁小限行至天使夹耗之地，再兼太岁逢劫，是「天空天伤 + 天使夹耗 + 太岁逢劫」的三重削弱与打击组合。财源、身命与环境支撑在短时间内被同时透支与冲击，终在此阶段死亡，呈现「巨富而不免横遭结构性崩塌」的命运。

- **完整对等诠释（secondary_lang_full）**：  
  Shi Chongfu’s chart is that of a Yang Wood native in the Third Configuration. The text notes that he "moves through life in splendour" with Power and Lu guarding wealth; auspicious and literary stars attend, and both Wen Chang/Wu Qu and other dignified planets beam on the Life. This "Power‑Lu guarding wealth with Chang and Wu Qu encircling" pattern fits the image of an extremely rich magnate.  
  But at age forty‑three the major period enters a region of Tian Kong and Tian Shang, linking emptiness with wounding; at forty‑four the minor period passes into a sector where a "Heavenly Office" is clamped by耗‑type stars, and in that same span the Annual Tai Sui meets Di Jie. The combination—void and wound, office‑and‑drain, plus earth‑robbery—describes a situation where resources, body and social position are all undermined at once. The native dies in this interval. The case portrays a chart of vast wealth that nonetheless ends in a period of structural collapse.

- **核心要点**：  
  1. 权禄守财、昌武曲拱命，是典型「豪富」格局，资源极其丰厚。  
  2. 四十三岁大限入天空天伤之地，四十四岁小限入天使夹耗，再兼太岁逢劫。  
  3. 命例显示「极富之命在虚耗、伤害与劫夺并临时，仍难免崩塌与死亡」。"""
    normalized_text_zh: str = """"""
    subject: str = "石崇富命"
    factor_refs: list = ['pattern_quanlu_shoucai', 'pattern_changwuqu_gongming', 'quality_jufu_zhi_ming', 'malefic_tiankong_tianshang', 'malefic_tianshi_jiahao', 'timing_taisui_fengjie']
    
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
        l1_anchor="zw_v1.0.0_石崇富命_001_L1",
    )
    version: str = "1.0.0"
