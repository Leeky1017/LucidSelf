"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.853822
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
    semantic_id="mlxj_v1.0.0_1_火盗类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1火盗类诸兆(SemanticEntry):
    """
    #### 火类汇总

**大吉类**：
- 家内火起火焰炎炎：大财兴旺
- 宅中火发：家业兴隆
- 宅中火光明亮：吉利昌荣
- 身被火烧死：大发之征

**吉类**：
- 门上火炎：凡事闪乐
- 厅边...
    """
    
    original_text: str = """#### 火类汇总

**大吉类**：
- 家内火起火焰炎炎：大财兴旺
- 宅中火发：家业兴隆
- 宅中火光明亮：吉利昌荣
- 身被火烧死：大发之征

**吉类**：
- 门上火炎：凡事闪乐
- 厅边燃火：官居明府
- 把火烧门：家兴旺
- 梦火烧天：天下太平
- 梦火烧日月：贵人助力
- 梦火烧河水：既济之兆，命寿长永

**凶类**：
- 身被火烧（不死）：大凶（隋炀帝典故）
- 烧而火不透发：非祥
- 烟黑色：病至
- 火烧地：疾病缠身

#### 盗类汇总

**吉类**：
- 梦统人杀贼：事兴昌

**凶类**：
- 梦被盗：财物损失
- 梦为盗：行为失当"""
    normalized_text_zh: str = """"""
    subject: str = "1 火盗类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_火盗类诸兆_001_L1",
    )
    version: str = "1.0.0"
