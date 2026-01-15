"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.793480
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
    semantic_id="mlxj_v1.0.0_1_星象综论_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1星象综论(SemanticEntry):
    """
    #### 原文（source_text）

星主文章，有三垣，有七政，有二十八宿，有众星。则星之见于梦者，宜以辰次为候，分野为推，因地因时，文明所耀，非寻等之占。盖星者，元气之英华也。

#### 规...
    """
    
    original_text: str = """#### 原文（source_text）

星主文章，有三垣，有七政，有二十八宿，有众星。则星之见于梦者，宜以辰次为候，分野为推，因地因时，文明所耀，非寻等之占。盖星者，元气之英华也。

#### 规范化释义（primary_lang_explained）

星象主文章功名。天上有三垣（紫微、太微、天市）、七政（日月五星）、二十八宿、众星。星象入梦，应以所在辰次为候、分野为推，因地因时，文明所耀，非寻常之占。星是元气的英华精粹。

#### 核心要点

- 星主文章
- 三垣七政二十八宿为天象框架
- 以辰次分野推占
- 星为元气之英华"""
    normalized_text_zh: str = """"""
    subject: str = "1 星象综论"
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
        l1_anchor="mlxj_v1.0.0_1_星象综论_001_L1",
    )
    version: str = "1.0.0"
