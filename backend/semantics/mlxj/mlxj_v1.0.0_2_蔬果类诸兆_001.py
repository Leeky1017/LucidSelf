"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.798224
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
    semantic_id="mlxj_v1.0.0_2_蔬果类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2蔬果类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 花椒大吉：辟邪除恶，眼目光明
- 桂皮大吉：折桂之兆
- 萱花大吉：忘忧，宜男

**吉类**：
- 青云菜吉：登云路
- 石花菜吉：无中生有
- 金花菜吉...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 花椒大吉：辟邪除恶，眼目光明
- 桂皮大吉：折桂之兆
- 萱花大吉：忘忧，宜男

**吉类**：
- 青云菜吉：登云路
- 石花菜吉：无中生有
- 金花菜吉：名利通达
- 芥菜吉：功名唾手取
- 竹笋吉：生男之兆
- 桑椹：生贵子

**贞吉否凶类**：
- 苋菜：利女人不利男子
- 莱菔（萝卜）：辛苦匍匐之劳

#### 典故

- 蔡齐典故：宋真宗梦殿下菜苗与殿基齐，拆卷得蔡齐，后为状元定制"""
    normalized_text_zh: str = """"""
    subject: str = "2 蔬果类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_蔬果类诸兆_001_L1",
    )
    version: str = "1.0.0"
