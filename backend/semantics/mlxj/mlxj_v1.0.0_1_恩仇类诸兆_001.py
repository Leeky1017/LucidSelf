"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.853830
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
    semantic_id="mlxj_v1.0.0_1_恩仇类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1恩仇类诸兆(SemanticEntry):
    """
    #### 人感恩类

凡人有阴德积善者，幽冥之中必有感激。或报以福禄，或报以年寿，或报以子嗣，或救其大难。每于梦寐之中，来相告语。

**典故**：刘弘敬救兰孙父女，梦兰孙之父紫衣象简，许延寿二十五载...
    """
    
    original_text: str = """#### 人感恩类

凡人有阴德积善者，幽冥之中必有感激。或报以福禄，或报以年寿，或报以子嗣，或救其大难。每于梦寐之中，来相告语。

**典故**：刘弘敬救兰孙父女，梦兰孙之父紫衣象简，许延寿二十五载，富及三代。

#### 人复冤类

凡人有罪孽过恶者，冥魂愤恨，至罪恶贯盈之时，必来报复。或致以祸，或促以寿，或破其家，或斩其嗣，或灭其族。

**典故**：
- 许州卢彦绪取古墓钗镜，梦妇人怒色，经年而卒
- 康季孙好杀奴婢，梦神人戒杀，后违誓呕血而卒"""
    normalized_text_zh: str = """"""
    subject: str = "1 恩仇类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_恩仇类诸兆_001_L1",
    )
    version: str = "1.0.0"
