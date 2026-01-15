"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.789165
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
    semantic_id="mlxj_v1.0.0_2_五神传梦吉图_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2五神传梦吉图(SemanticEntry):
    """
    #### 原文（source_text）

凡先梦脾属事物，而后及肺之所属梦，肺属事物而后及肾之所属梦，肾属事物而后及肝之所属梦，肝属事物而后及心之所属，此为正传占吉也。

#### 规范化释义（pr...
    """
    
    original_text: str = """#### 原文（source_text）

凡先梦脾属事物，而后及肺之所属梦，肺属事物而后及肾之所属梦，肾属事物而后及肝之所属梦，肝属事物而后及心之所属，此为正传占吉也。

#### 规范化释义（primary_lang_explained）

五神传梦吉图的规律是：先梦脾属事物，然后传至肺属事物；由肺属传至肾属；由肾属传至肝属；由肝属传至心属。此为正传，占断为吉。

传梦顺序：脾→肺→肾→肝→心（土生金、金生水、水生木、木生火）

这是五行相生的顺序，故主吉。

#### 核心要点

- **传梦顺序**：脾→肺→肾→肝→心
- **五行对应**：土→金→水→木→火
- **规律**：顺五行相生
- **吉凶**：吉"""
    normalized_text_zh: str = """"""
    subject: str = "2 五神传梦吉图"
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
        l1_anchor="mlxj_v1.0.0_2_五神传梦吉图_001_L1",
    )
    version: str = "1.0.0"
