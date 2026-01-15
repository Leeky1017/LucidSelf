"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.808937
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
    semantic_id="mlxj_v1.0.0_2_王潜夫梦列十类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2王潜夫梦列十类(SemanticEntry):
    """
    #### 原文（source_text）

梦有直有象，有精有想，有人有感，有时有反，有病有性。

直梦：所梦不察而懵愦冒名也，故亦不专信以断。
象梦：比拟相肖谓之象。
精梦：凝念注神谓之精。
想梦：...
    """
    
    original_text: str = """#### 原文（source_text）

梦有直有象，有精有想，有人有感，有时有反，有病有性。

直梦：所梦不察而懵愦冒名也，故亦不专信以断。
象梦：比拟相肖谓之象。
精梦：凝念注神谓之精。
想梦：昼有所思，夜梦其事。
人梦：贵贱贤愚、男女长少谓之人。
感梦：风雨寒暑谓之感。
时梦：五行王相谓之时。
反梦：阴极则吉，阳极则凶，谓之反。
病梦：观其所疾，察其所梦，谓之病。
性梦：心情好恶，于事有验，谓之性。

此十者，占梦之大略也。

#### 规范化释义（primary_lang_explained）

王潜夫《梦列篇》论梦十类：

| 类型 | 定义 | 特征 |
|------|------|------|
| 直梦 | 梦后直接应验 | 先有所梦，后无差忒 |
| 象梦 | 比拟相肖 | 象征性表达 |
| 精梦 | 凝念注神 | 精诚所感 |
| 想梦 | 昼有所思，夜梦其事 | 乍吉乍凶，善恶不信 |
| 人梦 | 因梦者身份而异 | 贵贱贤愚、男女长少 |
| 感梦 | 因外界感应 | 风雨寒暑 |
| 时梦 | 因时令五行 | 五行王相 |
| 反梦 | 反向应验 | 阴极则吉，阳极则凶 |
| 病梦 | 因疾病所致 | 观其所疾，察其所梦 |
| 性梦 | 因心性好恶 | 心情好恶，于事有验 |

此十者，占梦之大略也。"""
    normalized_text_zh: str = """"""
    subject: str = "2 王潜夫梦列十类"
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
        l1_anchor="mlxj_v1.0.0_2_王潜夫梦列十类_001_L1",
    )
    version: str = "1.0.0"
