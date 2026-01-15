"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699579
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
    semantic_id="zw_v1.0.0_燕哲之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 燕哲之命(SemanticEntry):
    """
    - 分字分词释义：

  - **禄权加会**：禄星与权星同宫或互拱，主福厚与实权并存。
  - **左右拱朝**：左辅右彼环拱命宫，主贵人扶持与富贵终身。
  - **但主人性暴**：性情急躁刚烈，...
    """
    
    original_text: str = """- 分字分词释义：

  - **禄权加会**：禄星与权星同宫或互拱，主福厚与实权并存。
  - **左右拱朝**：左辅右彼环拱命宫，主贵人扶持与富贵终身。
  - **但主人性暴**：性情急躁刚烈，易在冲突中走极端。
  - **陀罗之星**：主突发事故、阻隔与硬碰的凶星，戌生人尤忌。
  - **地劫火星同并**：地劫与火星同宫或同度，主激烈损伤与破耗。
  - **小限逢忌相冲**：小限逢忌星且与命形成冲照，主凶险倍增。
  - **阳男金四局**：燕哲命盘的五行局数，金四局主刚断烈性。

- **原文（source_text）**：  
  燕哲之命。阳男金四局。禄权加会，左右拱朝，终身福厚之论，但主人性暴。大限到于陀罗之星，戌生人有忌。且地劫、火星同并，小限逢忌相冲，故死于五十二岁。

- **规范化释义（primary_lang_explained）**：  
  燕哲命为阳男金四局，禄星与权星同会命宫或其三方，再加左右辅弼拱朝，为「禄权加会、左右拱朝」之格，一生福厚、物质不匮。但原文特别指出「但主人性暴」，说明在吉格之下仍藏性情急躁、刚烈的一面。  
  行运至大限陀罗之星所在之宫，戌生人逢此尤其为忌；再加地劫与火星同会，小限又逢忌星相冲，形成「陀罗 + 地劫 + 火星 + 忌星冲命」的多重凶局。此时自身性情之暴与外在杀伐之气共振，极易在纠纷、事故或急病中致命。命例整体呈现「福厚而性烈，在杀曜与忌星叠加之年于中年夭折」的结构。

- **完整对等诠释（secondary_lang_full）**：  
  Yan Zhe’s chart belongs to a Yang Metal native in the Fourth Configuration. With Lu and Quan converging and Left and Right Assistants supporting, the pattern "Lu‑Quan together, Zuo‑You attending" promises material abundance and sustained blessings. Yet the text notes that "his nature is violent," signalling a temperament prone to impatience, intensity and sudden outbursts beneath the auspicious surface.  
  When the major period reaches the star Tuo Luo—a sharp, cutting malefic—this is especially inauspicious for those born in Xu. At the same time Di Jie and Huo Xing combine, and the minor period encounters Ji stars that冲 the configuration. This stack of Tuo Luo, robbery/star of fire and Ji‑type malefics suggests sudden, forceful events where the native’s own volatility aggravates external danger, leading to death around fifty‑two. The case portrays a person blessed with resources yet carrying a fiery disposition, whose life is cut short when harsh transits align with inner sharpness.

- **核心要点**：  
  1. 禄权加会、左右拱朝，为终身福厚之格，但内含性情暴烈的隐忧。  
  2. 大限行至陀罗之星且为戌生人所忌，外加地劫、火星与忌星冲命，构成强烈的杀伐格局。  
  3. 中年（五十二岁）在内外凶性共振下夭折，是「福厚而性烈」命局的警示样本。

- **叙事素材（narrative_snippets）**：
  - **福厚之命**："禄权加会，左右拱朝，终身福厚之论"，燕哲命主原局衣食丰足、得权得利。
  - **性情暴烈**："但主人性暴"，提示其性格急躁刚烈，易在冲突中走极端。
  - **陀罗火劫**："大限到于陀罗之星，戌生人有忌。且地劫、火星同并，小限逢忌相冲，故死于五十二岁"，陀罗配地劫火星与忌星冲命，为中年暴亡之年。
  - **现代应用**：对「条件优渥却脾气刚烈」的人来说，在陀罗、火星等杀曜主导的年份，情绪管理与冲突降级尤其关键，否则极易在一场本可避免的事故、争执或冲动行为中付出生命代价。"""
    normalized_text_zh: str = """"""
    subject: str = "燕哲之命"
    factor_refs: list = ['pattern_luquan_jiahui', 'pattern_zuoyou_gongchao', 'quality_xingbao', 'malefic_tuoluo', 'malefic_dijie_huoxing', 'timing_xiaoxian_jiechong']
    
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
        l1_anchor="zw_v1.0.0_燕哲之命_001_L1",
    )
    version: str = "1.0.0"
