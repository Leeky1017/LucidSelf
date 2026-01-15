"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.806618
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
    semantic_id="mlxj_v1.0.0_1_羽族类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1羽族类(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 魏 | 文帝 | 瓦坠化鸳鸯 | 宫人相杀 |
| 西晋 | 罗会 |...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 魏 | 文帝 | 瓦坠化鸳鸯 | 宫人相杀 |
| 西晋 | 罗会 | 吞五色鸟 | 文章著 |
| 西晋 | 张𬸦 | 紫翅大鸟止庭 | 文名青钱学士 |
| 唐 | 武后 | 鹦鹉拆两翼 | 二子被废 |

### 4.2 水族昆虫类"""
    normalized_text_zh: str = """"""
    subject: str = "1 羽族类"
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
        l1_anchor="mlxj_v1.0.0_1_羽族类_001_L1",
    )
    version: str = "1.0.0"
