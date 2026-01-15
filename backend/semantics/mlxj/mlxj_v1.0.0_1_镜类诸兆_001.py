"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.821487
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
    semantic_id="mlxj_v1.0.0_1_镜类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1镜类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 轩辕镜吉：上下荣耀，八方洞达
- 手内持镜吉：青眼藻鉴
- 囊镜吉：弢而未燿，大吉

**吉类**：
- 得他人镜吉：得美配
- 镜内照自己：自省自察

*...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 轩辕镜吉：上下荣耀，八方洞达
- 手内持镜吉：青眼藻鉴
- 囊镜吉：弢而未燿，大吉

**吉类**：
- 得他人镜吉：得美配
- 镜内照自己：自省自察

**凶类**：
- 对镜不见影凶：凡事无形，谋望空
- 镜照他人：妻室无心于我
- 镜内两人并立：人我俱无益

#### 典故

- 郡守梦泥镜：韦应物授泥镜，寻得杀人僧疑镜
- 唐孙珏梦镜坠：合卺夕梦镜自跃坠地，后流离"""
    normalized_text_zh: str = """"""
    subject: str = "1 镜类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_镜类诸兆_001_L1",
    )
    version: str = "1.0.0"
