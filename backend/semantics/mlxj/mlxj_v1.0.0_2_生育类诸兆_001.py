"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.801360
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
    semantic_id="mlxj_v1.0.0_2_生育类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2生育类诸兆(SemanticEntry):
    """
    #### 原文摘要

金丹妙诀云：胎成十月生，个个会骑鹤。世所称鹤神，即此也。鹤善鸣，鹤神主耗，故梦儿童主口舌。而修炼大方家，善养生者，梦怀胎为得道，梦儿童为婴儿姹女，梦产育为不祥，气聚气散之说也。
...
    """
    
    original_text: str = """#### 原文摘要

金丹妙诀云：胎成十月生，个个会骑鹤。世所称鹤神，即此也。鹤善鸣，鹤神主耗，故梦儿童主口舌。而修炼大方家，善养生者，梦怀胎为得道，梦儿童为婴儿姹女，梦产育为不祥，气聚气散之说也。

恒人占之：
- 梦生男：为疾病
- 梦生女：为失财
- 梦抱新生子孙：为大发，生生之谓也
- 梦小口病死：为口舌消散

#### 生育梦象汇总

**吉类**：
- 梦抱新生子孙：大发
- 梦贺人生育：喜庆
- 好学之士梦孕育：得遂志

**凶类**：
- 梦生男：疾病
- 梦生女：失财
- 梦产育（修炼者）：不祥

**分化类**：
- 托生梦：主产业废兴，或天降异兆
- 弥月梦：主凡事有三十日之占
- 周岁梦：及期之象，周旋之兆
- 小产梦：口舌消散，疾病捐除"""
    normalized_text_zh: str = """"""
    subject: str = "2 生育类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_生育类诸兆_001_L1",
    )
    version: str = "1.0.0"
