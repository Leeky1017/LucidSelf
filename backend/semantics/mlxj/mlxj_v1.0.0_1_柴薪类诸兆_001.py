"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.802959
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
    semantic_id="mlxj_v1.0.0_1_柴薪类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1柴薪类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 柴满门内大吉：名利两实
- 薪积如山吉：富饶之象

**吉类**：
- 担柴归家吉：柴=财，财星照临
- 分柴夺柴吉：经营合伴
- 薪积火上：发扬蹈励

*...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 柴满门内大吉：名利两实
- 薪积如山吉：富饶之象

**吉类**：
- 担柴归家吉：柴=财，财星照临
- 分柴夺柴吉：经营合伴
- 薪积火上：发扬蹈励

**凶类**：
- 柴被火烧或水漂凶：散而无统
- 薪积水上：星散

#### 柴薪象征

柴者，财也。担财归家为财星照临，分柴夺柴为经营合伴。"""
    normalized_text_zh: str = """"""
    subject: str = "1 柴薪类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_柴薪类诸兆_001_L1",
    )
    version: str = "1.0.0"
