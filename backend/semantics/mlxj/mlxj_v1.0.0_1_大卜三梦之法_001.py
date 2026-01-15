"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.808900
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
    semantic_id="mlxj_v1.0.0_1_大卜三梦之法_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1大卜三梦之法(SemanticEntry):
    """
    #### 原文（source_text）

周礼大卜掌三兆之法，一玉兆，二瓦兆，三原兆。掌三易之法，一连山，二归藏，三周易。掌三梦之法，一曰致梦，二曰觭梦，三曰咸陟。其经运十，其别九十。占梦以岁时、日...
    """
    
    original_text: str = """#### 原文（source_text）

周礼大卜掌三兆之法，一玉兆，二瓦兆，三原兆。掌三易之法，一连山，二归藏，三周易。掌三梦之法，一曰致梦，二曰觭梦，三曰咸陟。其经运十，其别九十。占梦以岁时、日月星辰为运，梦之吉凶，每运九变，故其别九十，其术今亡矣。以邦事作八命：一曰征，二曰象，三曰与，四曰谋，五曰果，六曰至，七曰雨，八曰瘳。

#### 规范化释义（primary_lang_explained）

《周礼》大卜掌三兆之法（玉兆、瓦兆、原兆）、三易之法（连山、归藏、周易）、三梦之法（致梦、觭梦、咸陟）。

三梦之法：
- **致梦**：郑氏以为夏后氏所作
- **觭梦**：商人所作
- **咸陟**：言梦之得，周人取焉

其经运十（以岁时日月星辰为运），其别九十（每运九变），占梦吉凶，其术今亡矣。

以邦事作八命：征、象、与、谋、果、至、雨、瘳。"""
    normalized_text_zh: str = """"""
    subject: str = "1 大卜三梦之法"
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
        l1_anchor="mlxj_v1.0.0_1_大卜三梦之法_001_L1",
    )
    version: str = "1.0.0"
