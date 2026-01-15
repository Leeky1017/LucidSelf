"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.816092
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
    semantic_id="mlxj_v1.0.0_1_各类符咒_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1各类符咒(SemanticEntry):
    """
    #### 护身符类

| 符名 | 功用 | 佩戴位置 |
|------|------|---------|
| 太乙护身符 | 总护全身 | 胸前 |
| 辟邪符 | 驱除邪祟 | 门首 |
| ...
    """
    
    original_text: str = """#### 护身符类

| 符名 | 功用 | 佩戴位置 |
|------|------|---------|
| 太乙护身符 | 总护全身 | 胸前 |
| 辟邪符 | 驱除邪祟 | 门首 |
| 安魂符 | 安定魂魄 | 枕下 |
| 镇宅符 | 镇压邪气 | 宅中 |

#### 咒语类

| 咒名 | 功用 | 念诵时机 |
|------|------|---------|
| 卧咒 | 安眠禳梦 | 临睡前 |
| 醒咒 | 驱散恶气 | 恶梦醒后 |
| 净心咒 | 清净心神 | 日间 |
| 辟邪咒 | 辟除邪祟 | 随时 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 各类符咒"
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
        l1_anchor="mlxj_v1.0.0_1_各类符咒_001_L1",
    )
    version: str = "1.0.0"
