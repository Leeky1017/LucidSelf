"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699215
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
    semantic_id="zw_v1.0.0_韩信之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 韩信之命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫府拱照**：紫微天府拱照命宫，主极贵。
  - **禄合科权**：禄存与化科化权会合，主出将入相。
  - **出将入相**：可为将军亦可为宰相的极贵命格。
  -...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫府拱照**：紫微天府拱照命宫，主极贵。
  - **禄合科权**：禄存与化科化权会合，主出将入相。
  - **出将入相**：可为将军亦可为宰相的极贵命格。
  - **羊陀冲照**：擎羊陀罗冲照命宫，主被害。
  - **空劫伤忌**：天空地劫天伤化忌齐聚，主功高震主。
  - **被毒死**：韩信被吕后毒杀的历史事件，为命亡应期。
  - **阳男土五局**：韩信命盘的五行局数，土五局主厚重稳健。

- **原文（source_text）**：  
  韩信之命。阳男土五局。紫府拱照，左右加舍，禄合科权，出将入相之命。三十二岁，小限在亥，值伤忌，太岁空劫，任巳冲之，又大限羊陀冲照，故𮞸毒死。

- **规范化释义（primary_lang_explained）**：  
  韩信命属阳男土五局，紫府拱照、左右加会、禄合科权，主出将入相。三十二岁小限在亥值伤忌，太岁空劫，巳冲之，大限羊陀冲照，遂被毒死。

- **完整对等诠释（secondary_lang_full）**：  
  Han Xin's Yang male Earth Fifth chart has Ziwei‑Tianfu flanking, Left‑Right join, Salary combines with Academic‑Authority—a general‑minister destiny. At 32 minor at Hai meets Wound‑taboo; Tai Sui with Void‑Robbery, Si clashes. Major with Blade‑Tuo clash. Poisoned to death.

- **核心要点**：  
  1. 紫府拱照、左右禄合科权，主出将入相。  
  2. 小限伤忌、太岁空劫冲照。  
  3. 大限羊陀冲照，为被毒死应期。

- **叙事素材（narrative_snippets）**：
  - **出将入相**："紫府拱照，左右加舍，禄合科权，出将入相之命"，韩信命主能文能武、战功赫赫。
  - **空劫伤忌**："三十二岁，小限在亥，值伤忌，太岁空劫，任巳冲之"，伤忌加空劫，暗示功高震主之危局。
  - **羊陀冲照**："又大限羊陀冲照，故𮞸毒死"，羊陀冲命为遭人暗害、毒死之星象组合。
  - **现代应用**：在组织内部权力斗争激烈的环境中，此类格局到达羊陀冲照之年，应谨慎处理功劳与权力分配，避免成为众矢之的。"""
    normalized_text_zh: str = """"""
    subject: str = "韩信之命"
    factor_refs: list = ['result_chujiangruxiang', 'pattern_yangtuochongzhao', 'pattern_kongjieshangi', 'source_ref', 'rel_hanxin_001', 'pattern_zifukequan', 'rel_hanxin_002', 'pattern_kongjieshangi', 'rel_hanxin_003', 'pattern_yangtuochongzhao', 'evi_hanxin_001', 'pattern_yangtuochongzhao', 'rule_yangtuo_chongzhao', 'concept_general_minister', 'concept_blade_tuo']
    
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
        l1_anchor="zw_v1.0.0_韩信之命_001_L1",
    )
    version: str = "1.0.0"
