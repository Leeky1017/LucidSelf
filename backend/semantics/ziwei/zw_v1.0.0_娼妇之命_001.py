"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.700032
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
    semantic_id="zw_v1.0.0_娼妇之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 娼妇之命(SemanticEntry):
    """
    - 分字分词释义：

  - **七杀临身终不美**：七杀星临于身宫或命宫，形成刚烈不和的基调。
  - **天空地劫更无良**：天空与地劫同时出现，进一步抽空根基与福泽。
  - **虽有紫府守命垣...
    """
    
    original_text: str = """- 分字分词释义：

  - **七杀临身终不美**：七杀星临于身宫或命宫，形成刚烈不和的基调。
  - **天空地劫更无良**：天空与地劫同时出现，进一步抽空根基与福泽。
  - **虽有紫府守命垣**：虽然有紫微天府等贵星守命。
  - **夫君子婳二宫甚混杂**：夫妻宫与子女宫星曜混杂不清，婚姻与子嗣都不稳定。
  - **姚忌居干福德**：天姚与化忌同居于福德宫，主淫欲与不良。
  - **其贱无疑**：沉为娼妇几乎无可避免。
  - **阴女水二局**：娼妇命盘的五行局数，水二局主智慧沉沦。

- **原文（source_text）**：  
  娼妇之命。阴女水二局。七杀临身终不美，天空地劫更无良。虽有紫府守命垣，而夫君、子婳二宫甚混杂，且姚、忌居干福德，其贱无疑矣。

- **规范化释义（primary_lang_explained）**：  
  娼妇之命为阴女水二局，「七杀临身终不美」说明七杀星临于身宫或命宫，形成刚烈而不和的基调。「天空地劫更无良」，天空与地劫同时出现，进一步抽空根基与福泽。「虽有紫府守命垣」，虽然有紫微天府等贵星守命，「而夫君、子婳二宫甚混杂」，夫妻宫与子女宫星曜混杂不清，婚姻与子嗣都不稳定。「且姚、忌居干福德，其贱无疑矣」，姚星（天姚主桃花淫欲）与化忌同居于福德宫，命主沦为娼妇几乎无可避免。

- **完整对等诠释（secondary_lang_full）**：  
  This "Prostitute's Destiny" chart is that of a Yin Water female. Qi Sha on Body or Life creates harshness; Kong and Jie drain any foundation. Although Zi Wei and Tian Fu guard Life, the Spouse and Children palaces are muddled. Worse, Yao (Heavenly Enticement, signifying licentiousness) and Hua Ji sit in the Fortune sector. The path to degradation is certain.

- **核心要点**：  
  1. 七杀临身配天空地劫，根基不稳且刚烈。  
  2. 紫府守命但夫妻子媳二宫混杂，婚姻子嗣不利。  
  3. 姚忌居福德宫，沦为娼妇无疑。"""
    normalized_text_zh: str = """"""
    subject: str = "娼妇之命"
    factor_refs: list = ['malefic_qisha_linshen', 'malefic_tiankong_dijie', 'pattern_zifu_shouming', 'malefic_fuzi_hunza', 'malefic_yaoji_fude', 'result_qi_jian_wuyi']
    
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
        l1_anchor="zw_v1.0.0_娼妇之命_001_L1",
    )
    version: str = "1.0.0"
