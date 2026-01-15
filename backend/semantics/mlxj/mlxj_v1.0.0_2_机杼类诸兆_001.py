"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.821467
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
    semantic_id="mlxj_v1.0.0_2_机杼类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2机杼类诸兆(SemanticEntry):
    """
    #### 分类汇总

**蚕桑器具**：
- 蚕箔中蚕长：益财
- 空箔无蚕：无愁虑，得清吉
- 箔中蚕僵：失财
- 缫盆缫架缫车吉：有操持操守操纵方吉

**织机器具**：
- 梭：一生劳碌，朝投剑...
    """
    
    original_text: str = """#### 分类汇总

**蚕桑器具**：
- 蚕箔中蚕长：益财
- 空箔无蚕：无愁虑，得清吉
- 箔中蚕僵：失财
- 缫盆缫架缫车吉：有操持操守操纵方吉

**织机器具**：
- 梭：一生劳碌，朝投剑阁夕抵燕关
- 纬筒：兄弟有不宁之事
- 机剪吉：谋事忽然中断，前后分为两局
- 牵花吉：作事有呼有应

**典故**：
- 张休仲梦苇帘稿荐：后连荐官至平章（帘荐=连荐之征）"""
    normalized_text_zh: str = """"""
    subject: str = "2 机杼类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_机杼类诸兆_001_L1",
    )
    version: str = "1.0.0"
