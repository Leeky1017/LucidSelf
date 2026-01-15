"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.823564
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
    semantic_id="mlxj_v1.0.0_2_羊类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2羊类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 万羊大吉：牧民之象
- 牵羊大吉：一阳来复

**吉类**：
- 一羊在花下吉：美欢之兆（宋吴近典故，生女为高宗后）
- 人馈羊吉：生男之兆
- 盗羊吉：阴...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 万羊大吉：牧民之象
- 牵羊大吉：一阳来复

**吉类**：
- 一羊在花下吉：美欢之兆（宋吴近典故，生女为高宗后）
- 人馈羊吉：生男之兆
- 盗羊吉：阴中生阳

**贞吉否凶类**：
- 羝羊触藩：作事羁迟
- 骑羊：自在从容，但有假无真
- 刲羊：有庆贺，无血则凶

**凶类**：
- 羊负鱼凶：鲜（羊+鱼），避难之兆（赵主石季龙典故）
- 身变羊凶：弄真成假"""
    normalized_text_zh: str = """"""
    subject: str = "2 羊类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_羊类诸兆_001_L1",
    )
    version: str = "1.0.0"
