"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.789174
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
    semantic_id="mlxj_v1.0.0_3_五神传梦凶图_001",
    book_id="mlxj",
    engine_id="dream"
)
class 3五神传梦凶图(SemanticEntry):
    """
    #### 原文（source_text）

凡先梦脾属事物而后及肾之所属梦，肾属事物而后及心之所属梦，心属事物而后及肺之所属梦，肺属事物而后及肝之所属，此为逆传占凶也。

#### 规范化释义（pri...
    """
    
    original_text: str = """#### 原文（source_text）

凡先梦脾属事物而后及肾之所属梦，肾属事物而后及心之所属梦，心属事物而后及肺之所属梦，肺属事物而后及肝之所属，此为逆传占凶也。

#### 规范化释义（primary_lang_explained）

五神传梦凶图的规律是：先梦脾属事物，然后传至肾属事物；由肾属传至心属；由心属传至肺属；由肺属传至肝属。此为逆传，占断为凶。

传梦顺序：脾→肾→心→肺→肝（土克水、水克火、火克金、金克木）

这是五行相克的顺序，故主凶。

#### 核心要点

- **传梦顺序**：脾→肾→心→肺→肝
- **五行对应**：土→水→火→金→木
- **规律**：逆五行相克
- **吉凶**：凶"""
    normalized_text_zh: str = """"""
    subject: str = "3 五神传梦凶图"
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
        l1_anchor="mlxj_v1.0.0_3_五神传梦凶图_001_L1",
    )
    version: str = "1.0.0"
