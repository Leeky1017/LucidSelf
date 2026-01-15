"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227605
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
    semantic_id="smth_v1.0.0_辰巳午未_阳极与成熟之名义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 辰巳午未阳极与成熟之名义(SemanticEntry):
    """
    - **原文（source_text）**：
  辰者，阳已过半，三月之时，物尽震而长。巳者，四月，正阳而无阴，自子至巳，阳之位，阳于是尽。午者，阳尚未屈，阴始生而为主，又云：午，长也，大也，物至五月...
    """
    
    original_text: str = """- **原文（source_text）**：
  辰者，阳已过半，三月之时，物尽震而长。巳者，四月，正阳而无阴，自子至巳，阳之位，阳于是尽。午者，阳尚未屈，阴始生而为主，又云：午，长也，大也，物至五月皆丰满长大也。未，六月，又云：未，味也，物成而有味。

- 分字分词释义：
  - **辰：震而长**：阳气过半，事物震动而迅速生长；
  - **巳：阳极之位**：正阳无阴，为阳气将尽之前极盛；
  - **午：长、大**：万物丰满长大，显其成形之势；
  - **未：味**：物成而有味，进入成熟与品评阶段。

- **规范化释义（primary_lang_explained）**：
  辰为春末，阳气已过半，万物迅速拔高；巳为阳极之处，阳气全展，将转入收敛。午则是表面最盛的时刻，形体丰满、气势极大；未则是「有味」之时，成果渐次显露，人事也进入审视与评估阶段。

- **完整对等诠释（secondary_lang_full）**：

  Chen belongs to late spring, when Yang Qi has passed the halfway mark and things shoot up rapidly, as if shaken into sudden growth. Si is the point of pure Yang, with no Yin yet returning—it is the last, most intense flare of energy before contraction begins. Wu is the moment of visible fullness: forms are plump, momentum is at its height, reputation and influence are most conspicuous. Wei, associated with "taste", marks the stage when results ripen and can be judged and enjoyed; achievements acquire flavour and are weighed and evaluated. Taken together, these four branches sketch the middle stretch of any development curve, from accelerated rise through peak display to the first phase of maturity, and invite us to distinguish between growth speed, summit experience and the quieter work of consolidating what has been gained."""
    normalized_text_zh: str = """"""
    subject: str = "辰巳午未：阳极与成熟之名义"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_辰巳午未_阳极与成熟之名义_001_L1",
    )
    version: str = "1.0.0"
