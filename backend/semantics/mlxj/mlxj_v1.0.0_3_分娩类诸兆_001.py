"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.801368
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
    semantic_id="mlxj_v1.0.0_3_分娩类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 3分娩类诸兆(SemanticEntry):
    """
    #### 分类汇总

**吉类**：
- 生二三子：仕宦梦之，官爵高升一品
- 见人产儿：尊长产儿主小口兴旺，卑幼产儿主添神
- 见男子产：主得子
- 见女人产：主得财
- 妻女产儿：子孙茂盛

**...
    """
    
    original_text: str = """#### 分类汇总

**吉类**：
- 生二三子：仕宦梦之，官爵高升一品
- 见人产儿：尊长产儿主小口兴旺，卑幼产儿主添神
- 见男子产：主得子
- 见女人产：主得财
- 妻女产儿：子孙茂盛

**凶类**：
- 产下鬼形：文墨之士梦此主大魁天下（反转）
- 父母产儿：祖业空虚
- 平民梦生二三子：是非口舌连累

**贞吉否凶类**：
- 身是小儿为人产下：出入腹我之兆"""
    normalized_text_zh: str = """"""
    subject: str = "3 分娩类诸兆"
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
        l1_anchor="mlxj_v1.0.0_3_分娩类诸兆_001_L1",
    )
    version: str = "1.0.0"
