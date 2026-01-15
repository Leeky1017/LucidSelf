"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.796547
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
    semantic_id="mlxj_v1.0.0_1_四季风雷_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1四季风雷(SemanticEntry):
    """
    #### 春季

| 梦象 | 主应 |
|------|------|
| 清和大吉 | 震声大贵大财 |
| 淋身 | 被恩宠 |
| 飘舞不积 | 东吹有喜 |
| 声隐隐 | 主晴信 |
| ...
    """
    
    original_text: str = """#### 春季

| 梦象 | 主应 |
|------|------|
| 清和大吉 | 震声大贵大财 |
| 淋身 | 被恩宠 |
| 飘舞不积 | 东吹有喜 |
| 声隐隐 | 主晴信 |
| 打身 | 名显 |

#### 夏季

| 梦象 | 主应 |
|------|------|
| 南来吉 | 被霹雳富贵 |
| 沾身 | 父母凶丧 |
| 畏声 | 官位至 |
| 见堆积 | 孝服 |
| 扫去 | 凶事散 |

#### 秋季

| 梦象 | 主应 |
|------|------|
| 起尘兵荒 | 电闪病消 |
| 淋身 | 损伤小恙 |
| 躱避 | 病愈 |
| 积如山 | 丧事 |

#### 冬季

| 梦象 | 主应 |
|------|------|
| 北来狂难至 | 大震有忧 |
| 如注 | 大财 |
| 飘舞吉 | 如被吹身前去 |
| 盈宅吉 | 贵人见责 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 四季风雷"
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
        l1_anchor="mlxj_v1.0.0_1_四季风雷_001_L1",
    )
    version: str = "1.0.0"
