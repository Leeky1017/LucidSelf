"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850637
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
    semantic_id="mlxj_v1.0.0_条目十二_怪异无占_寻常有验_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目十二怪异无占寻常有验(SemanticEntry):
    """
    ### 原文（source_text）

怪异无占，寻常有验。如所梦之兆，虽奇诞可惊，而原其情事，真属荒唐迂谬者，经固无占，强占不验。又如梦甚平常，似无足异，而究其根由，度其时势，非无关系者，经纵无文...
    """
    
    original_text: str = """### 原文（source_text）

怪异无占，寻常有验。如所梦之兆，虽奇诞可惊，而原其情事，真属荒唐迂谬者，经固无占，强占不验。又如梦甚平常，似无足异，而究其根由，度其时势，非无关系者，经纵无文，比类而推，则亦有验，不可忽也。

### 规范化释义（primary_lang_explained）

占梦的第十二条核心原则是「怪异无占，寻常有验」——并非越怪异的梦越有意义，反而平常的梦可能更有验证。

如果梦境虽然奇诞惊人，但追究其情事，确实荒唐迂谬、毫无道理，那么经典本无相应占法，强行占断也不会应验。

相反，如果梦境看似平常、似乎不值一提，但深究其根由、度量其时势，发现并非毫无关联，那么即使经典没有明文，也可以比类推断，往往会有应验，不可忽视。

### 核心要点

- 怪异无占、寻常有验是占梦第十二核心原则
- 奇诞荒唐之梦，强占不验
- 平常有关之梦，比类可验
- 不以怪异取梦，不以平常弃梦

### 叙事素材（narrative_snippets）

- `[ns_mlxj_028]` `[trigger: 梦象筛选]` `[factor_trigger: dream_significance]` `[role: 筛选原则]` 怪异无占，寻常有验。 → 《梦林玄解·卷之首》#怪异无占
- `[ns_mlxj_029]` `[trigger: 平常梦验]` `[factor_trigger: dream_significance]` `[role: 验证方法]` 梦甚平常，究其根由，比类而推，则亦有验。 → 《梦林玄解·卷之首》#寻常有验"""
    normalized_text_zh: str = """"""
    subject: str = "条目十二：怪异无占，寻常有验"
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
        l1_anchor="mlxj_v1.0.0_条目十二_怪异无占_寻常有验_001_L1",
    )
    version: str = "1.0.0"
