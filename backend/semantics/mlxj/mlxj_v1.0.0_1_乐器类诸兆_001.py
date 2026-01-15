"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.821494
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
    semantic_id="mlxj_v1.0.0_1_乐器类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1乐器类诸兆(SemanticEntry):
    """
    #### 分类汇总

**钟类**：
- 铸钟：作事诚实
- 撞钟有声：事必应
- 撞钟无声：难幸获
- 自鸣钟：运气一通
- 钟声洪远吉：造诣非凡，事业宏久
- 钟现五色：文章昭著

**磬类**：...
    """
    
    original_text: str = """#### 分类汇总

**钟类**：
- 铸钟：作事诚实
- 撞钟有声：事必应
- 撞钟无声：难幸获
- 自鸣钟：运气一通
- 钟声洪远吉：造诣非凡，事业宏久
- 钟现五色：文章昭著

**磬类**：
- 磬大吉：喜庆重叠
- 磬在地：及第之兆
- 击磬：庆来非止一端
- 磬声嘹亮：事主通畅
- 磬破：好事不成

#### 典故

- 杨淮梦二磬相香：中式，后授重庆府同知（二磬=重庆）
- 王茂梦钟磬自坠：乐崩则身亡"""
    normalized_text_zh: str = """"""
    subject: str = "1 乐器类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_乐器类诸兆_001_L1",
    )
    version: str = "1.0.0"
