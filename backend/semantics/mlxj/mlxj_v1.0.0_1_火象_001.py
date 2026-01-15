"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.831812
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
    semantic_id="mlxj_v1.0.0_1_火象_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1火象(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 火从地发大吉：天火下降，地火上升，水火既济
- 见脐中火光起：腹有光明，正则生贵子

**凶类**：
- 火灭凶：家亡财散，病入膏肓，讼困缧绁

**贞吉否...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 火从地发大吉：天火下降，地火上升，水火既济
- 见脐中火光起：腹有光明，正则生贵子

**凶类**：
- 火灭凶：家亡财散，病入膏肓，讼困缧绁

**贞吉否凶类**：
- 取水浇火：水火既济，豫防之象，事事谨慎戒惧"""
    normalized_text_zh: str = """"""
    subject: str = "1 火象"
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
        l1_anchor="mlxj_v1.0.0_1_火象_001_L1",
    )
    version: str = "1.0.0"
