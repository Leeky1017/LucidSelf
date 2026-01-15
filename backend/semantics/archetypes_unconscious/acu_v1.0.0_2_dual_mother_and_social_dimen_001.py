"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515596
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
    semantic_id="acu_v1.0.0_2_dual_mother_and_social_dimen_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 2DualMotherAndSocialDimen(SemanticEntry):
    """
    **Source Text** (¶93-99, Lines 1575-1687):

> [93] Leonardo's St. Anne: interwoven with personal psy...
    """
    
    original_text: str = """**Source Text** (¶93-99, Lines 1575-1687):

> [93] Leonardo's St. Anne: interwoven with personal psychology is the impersonal dual-mother archetype—found in rebirth rituals, baptism, godparents.
>
> [96] Patient's neurosis caused by reactivation of dual-mother archetype—regardless of whether he had one or two mothers.
>
> [98] Can we not see how a whole nation is reviving an archaic symbol? If anyone predicted medieval Jew-persecutions would return, swastika replacing the Cross, that man would have been mocked. And today? All this absurdity is a horrible reality.
>
> [99] As many archetypes as typical life situations. When activated, compulsiveness appears—gains its way against all reason and will.

**English Paraphrase**:
- **Dual mother**: Universal archetype, not just personal (Leonardo, rebirth rituals)
- **Archetype cause**: Reactivation causes neurosis, not personal history
- **Social dimension**: Nazi Germany = whole nation reviving archaic symbol
- **Activation**: Compulsiveness against reason and will

**中文释义**：
- **双重母亲**：普遍原型，不仅是个人的（达芬奇、重生仪式）
- **原型原因**：再激活导致神经症，非个人历史
- **社会维度**：纳粹德国 = 整个民族复兴古老象征
- **激活**：违背理性和意志的强迫性"""
    normalized_text_zh: str = """"""
    subject: str = "2 Dual Mother and Social Dimension (¶93-99)"
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_2_dual_mother_and_social_dimen_001_L1",
    )
    version: str = "1.0.0"
