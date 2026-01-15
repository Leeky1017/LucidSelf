"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.793430
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
    semantic_id="mlxj_v1.0.0_4_天地黑陷_001",
    book_id="mlxj",
    engine_id="dream"
)
class 4天地黑陷(SemanticEntry):
    """
    #### 原文（source_text）

天地黑陷凶。此梦幽囚险坠之兆，黑者，明之背，陷者，平之反。占象应天地者，梦此非吉。婚姻不成，交易不遂，父母不宁，官讼不理。凡事宜小心警惧，或志气昏惰神思惊惶...
    """
    
    original_text: str = """#### 原文（source_text）

天地黑陷凶。此梦幽囚险坠之兆，黑者，明之背，陷者，平之反。占象应天地者，梦此非吉。婚姻不成，交易不遂，父母不宁，官讼不理。凡事宜小心警惧，或志气昏惰神思惊惶有此兆。

#### 规范化释义（primary_lang_explained）

梦见天地黑暗塌陷，凶。此为幽囚险坠之兆。黑是光明的反面，陷是平安的反面。凡应于天地的占象，梦此皆非吉利。主婚姻不成、交易不遂、父母不宁、官讼不理。凡事宜小心警惧。此梦也可能因志气昏惰、神思惊惶而生。

#### 核心要点

- **梦象**：天地黑陷
- **吉凶**：凶
- **象义**：幽囚险坠
- **主应**：婚姻不成、交易不遂、父母不宁、官讼不理
- **成因**：志气昏惰、神思惊惶"""
    normalized_text_zh: str = """"""
    subject: str = "4 天地黑陷"
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
        l1_anchor="mlxj_v1.0.0_4_天地黑陷_001_L1",
    )
    version: str = "1.0.0"
