"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.834539
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
    semantic_id="mlxj_v1.0.0_1_经卷类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1经卷类诸兆(SemanticEntry):
    """
    #### 分类汇总

**吉类**：
- 金刚经吉：五阴皆空
- 弥陀经大吉：禅定西归
- 法华经大吉：功圆行满
- 心经吉：无挂无碍
- 仙经吉：却病延年
- 文昌经贞吉：士人姓名扬

**贞吉否凶...
    """
    
    original_text: str = """#### 分类汇总

**吉类**：
- 金刚经吉：五阴皆空
- 弥陀经大吉：禅定西归
- 法华经大吉：功圆行满
- 心经吉：无挂无碍
- 仙经吉：却病延年
- 文昌经贞吉：士人姓名扬

**贞吉否凶类**：
- 道经贞吉否凶：因而自省
- 玉皇经贞吉：宜清修高隐
- 朝天忏贞吉：见君之征
- 南北二斗经贞吉否凶：南斗注生北注死

**凶类**：
- 灶王经贞吉否凶：警戒世人

#### 典故

- 棋经三卷：唐僖宗梦吞棋经，凡所指画皆出人意表"""
    normalized_text_zh: str = """"""
    subject: str = "1 经卷类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_经卷类诸兆_001_L1",
    )
    version: str = "1.0.0"
