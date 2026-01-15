"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.847063
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
    semantic_id="mlxj_v1.0.0_1_四季交际_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1四季交际(SemanticEntry):
    """
    #### 春季

| 梦象 | 主应 |
|------|------|
| 妇女相争 | 口舌增吉 |
| 餽送䌷段 | 对门相拜 |
| 招饮喜事 | 官讼凶至 |
| 送饭来 | 口舌 |
| ...
    """
    
    original_text: str = """#### 春季

| 梦象 | 主应 |
|------|------|
| 妇女相争 | 口舌增吉 |
| 餽送䌷段 | 对门相拜 |
| 招饮喜事 | 官讼凶至 |
| 送饭来 | 口舌 |
| 送鲜花来 | 得财得贵子 |
| 送酒肉来 | 有口舌 |

#### 夏季

| 梦象 | 主应 |
|------|------|
| 送时果 | 得福吉寿 |
| 送米粟来 | 得财吉 |
| 送酒殽来 | 得财 |
| 群儿嬉戏 | 得大财吉 |

#### 秋季

| 梦象 | 主应 |
|------|------|
| 汲井水 | 防盗 |
| 还簪得婚 | 大吉 |
| 送貂裘 | 贵人吉 |
| 借针线 | 增寿 |

#### 冬季

| 梦象 | 主应 |
|------|------|
| 同烧香礼神佛 | 礼神凶拜佛吉 |
| 相打血出吉 | 作事大成 |
| 携手相商 | 大利 |
| 送枕来 | 重婚 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 四季交际"
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
        l1_anchor="mlxj_v1.0.0_1_四季交际_001_L1",
    )
    version: str = "1.0.0"
