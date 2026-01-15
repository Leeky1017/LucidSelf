"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.789219
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
    semantic_id="mlxj_v1.0.0_1_阳气盛极发梦_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1阳气盛极发梦(SemanticEntry):
    """
    #### 原文（source_text）

凡人阳盛者，乃气旺也。气旺则损其血，血损则亏其阴。阴不能济阳，水不能制火，孤阳绝阴，燔天灼地。南方丙丁之威于斯独盛，故梦中烧烁之象见焉。在人养阴以退阳，葆真...
    """
    
    original_text: str = """#### 原文（source_text）

凡人阳盛者，乃气旺也。气旺则损其血，血损则亏其阴。阴不能济阳，水不能制火，孤阳绝阴，燔天灼地。南方丙丁之威于斯独盛，故梦中烧烁之象见焉。在人养阴以退阳，葆真以制欲，其兆不求辟而自解矣。

#### 规范化释义（primary_lang_explained）

阳气盛极者，是气旺之人。气旺则损血，血损则阴亏。阴不能济阳、水不能制火，形成孤阳绝阴、燔天灼地之势。南方丙丁火之威独盛，故梦中出现烧烁之象。

调养之法：养阴以退阳，葆真以制欲，则凶兆不求辟禳而自解。"""
    normalized_text_zh: str = """"""
    subject: str = "1 阳气盛极发梦"
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
        l1_anchor="mlxj_v1.0.0_1_阳气盛极发梦_001_L1",
    )
    version: str = "1.0.0"
