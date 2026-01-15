"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699321
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
    semantic_id="zw_v1.0.0_宋璟之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 宋璟之命(SemanticEntry):
    """
    - 分字分词释义：

  - **府相左右**：天府天相与左辅右彼同宫，主辅佐之力。
  - **科禄朝垣禄合**：科禄与禄存拱照并会合，主富贵终身。
  - **贵人守命**：贵人星守命宫，主一生多...
    """
    
    original_text: str = """- 分字分词释义：

  - **府相左右**：天府天相与左辅右彼同宫，主辅佐之力。
  - **科禄朝垣禄合**：科禄与禄存拱照并会合，主富贵终身。
  - **贵人守命**：贵人星守命宫，主一生多贵人。
  - **劫空在命**：地劫天空在命宫，主寿不长。
  - **小限七杀**：小限行至七杀宫位，主凶险。
  - **流年羊陀**：流年擎羊陀罗齐聚，主伤寿。
  - **阳男金四局**：宋璟命盘的五行局数，金四局主刚断清正。

- **原文（source_text）**：  
  宋璟之命。阳男金四局。府相左右，科禄朝垣禄合，格局明白，贵人守命垣，因论富贵终身，只是劫空在命，故寿不长。小限七杀，流年羊陀，太岁冲命甚凶，其年伤寿。

- **规范化释义（primary_lang_explained）**：  
  宋璟命属阳男金四局，府相左右、科禄朝垣禄合，贵人守命，主富贵终身。然劫空在命，寿不长。小限七杀、流年羊陀、太岁冲命，其年伤寿而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Song Jing's Yang male Metal Fourth chart has Fu‑Xiang Left‑Right, Academic‑Salary facing court with combination, noble guards Life—lifelong wealth. But Robbery‑Void at Life, short lifespan. Minor Seven Killings, annual Blade‑Tuo, Tai Sui clashes Life. Lifespan cut that year.

- **核心要点**：  
  1. 府相左右、科禄禄合，主富贵终身。  
  2. 劫空在命，寿不长。  
  3. 小限七杀、流年羊陀、太岁冲命，为伤寿应期。

- **叙事素材（narrative_snippets）**：
  - **富贵终身**："府相左右，科禄朝垣禄合，格局明白，贵人守命垣，因论富贵终身"，宋璟命主一生位高权重、清名在外。
  - **劫空折寿**："只是劫空在命，故寿不长"，劫空坐命使寿元受损，难以享尽富贵之期。
  - **伤寿之年**："小限七杀，流年羊陀，太岁冲命甚凶，其年伤寿"，七杀羊陀加太岁冲命，为明显的折寿年份。
  - **现代应用**：富贵但体质偏弱的命局，在七杀羊陀加太岁冲命的年份，应强化健康管理与压力调节，避免“富贵身先死”。"""
    normalized_text_zh: str = """"""
    subject: str = "宋璟之命"
    factor_refs: list = ['pattern_jiekongzaiming', 'pattern_fuxiangzuoyou', 'pattern_keluluhe', 'source_ref', 'rel_songjing_001', 'pattern_fuxiangkelu', 'rel_songjing_002', 'pattern_jiekongzaiming', 'rel_songjing_003', 'pattern_qishayangtuochong', 'evi_songjing_001', 'pattern_jiekongzaiming', 'rule_jiekong_shangshou', 'concept_robbery_life', 'concept_fu_xiang']
    
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
        l1_anchor="zw_v1.0.0_宋璟之命_001_L1",
    )
    version: str = "1.0.0"
