"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.789227
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
    semantic_id="mlxj_v1.0.0_2_阴气盛极发梦_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2阴气盛极发梦(SemanticEntry):
    """
    #### 原文（source_text）

凡人阴盛者，乃邪气有余也，阳火衰微，真元失守之兆。火既微弱，则脾土无依，脾土无依，则狂澜莫遏，飘摇荡漾，浩渺汪洋。北方壬癸之势，于斯独盛，故梦中汨没之象见焉...
    """
    
    original_text: str = """#### 原文（source_text）

凡人阴盛者，乃邪气有余也，阳火衰微，真元失守之兆。火既微弱，则脾土无依，脾土无依，则狂澜莫遏，飘摇荡漾，浩渺汪洋。北方壬癸之势，于斯独盛，故梦中汨没之象见焉。在人保固元阳，摄精守气，其兆不祛而自退矣。

#### 规范化释义（primary_lang_explained）

阴气盛极者，是邪气有余之人，阳火衰微、真元失守。火既微弱则脾土无依，脾土无依则狂澜莫遏，飘摇荡漾、浩渺汪洋。北方壬癸水之势独盛，故梦中出现汨没（沉溺）之象。

调养之法：保固元阳，摄精守气，则凶兆不祀而自退。"""
    normalized_text_zh: str = """"""
    subject: str = "2 阴气盛极发梦"
    factor_refs: list = ['source_ref']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_2_阴气盛极发梦_001_L1",
    )
    version: str = "1.0.0"
