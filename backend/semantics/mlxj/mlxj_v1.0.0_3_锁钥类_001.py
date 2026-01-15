"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.795264
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
    semantic_id="mlxj_v1.0.0_3_锁钥类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 3锁钥类(SemanticEntry):
    """
    #### 锁钥诸兆

**吉类**：
- 金锁钥：家道日隆，身荣嗣昌
- 玉锁金匙：得道学之传
- 金锁银匙：问学敏捷
- 银锁钥：得财成家

**锁钥用途对应**：
| 用途 | 主应 |
|---...
    """
    
    original_text: str = """#### 锁钥诸兆

**吉类**：
- 金锁钥：家道日隆，身荣嗣昌
- 玉锁金匙：得道学之传
- 金锁银匙：问学敏捷
- 银锁钥：得财成家

**锁钥用途对应**：
| 用途 | 主应 |
|------|------|
| 印箧 | 得官爵 |
| 仓库 | 得利禄 |
| 箱笼 | 得财帛 |
| 城门 | 凶中遇吉 |
| 房舍门户 | 小事吉 |"""
    normalized_text_zh: str = """"""
    subject: str = "3 锁钥类"
    factor_refs: list = []
    
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
        l1_anchor="mlxj_v1.0.0_3_锁钥类_001_L1",
    )
    version: str = "1.0.0"
