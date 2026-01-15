"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.568681
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
    semantic_id="acu_v1.0.0_3_projection_mechanism___121_1_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 3ProjectionMechanism1211(SemanticEntry):
    """
    **Source Text** (¶121-122, Lines 1993-2023):

> [121] Now, as we know from psychotherapeutic experie...
    """
    
    original_text: str = """**Source Text** (¶121-122, Lines 1993-2023):

> [121] Now, as we know from psychotherapeutic experience, projection is an unconscious, automatic process whereby a content that is unconscious to the subject transfers itself to an object, so that it seems to belong to that object. The projection ceases the moment it becomes conscious, that is to say when it is seen as belonging to the subject...
>
> [122] In reality, however, it is just the parental imagos that seem to be projected most frequently... Experience shows that projection is never conscious: projections are always there first and are recognized afterwards. We must therefore assume that, over and above the incest-fantasy, highly emotional contents are still bound up with the parental imagos and need to be made conscious.

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Projection | Casting outward | Inner content seen as outer | Core mechanism |
| Parental imagos | Parent-images | Archetypal parent | Primary projection |
| Transference | Therapeutic relationship | Projection onto analyst | Clinical example |
| Withdrawal | Taking back | Conscious recognition | Ending projection |

**English Paraphrase (Primary Language)**:

Jung defines **projection mechanism**:

**Definition**:
- "Unconscious, automatic process"
- Unconscious content "transfers itself to an object"
- Content "seems to belong to that object"
- Projection ceases when recognized as subject's own

**Parental projections**:
- Parental imagos most frequently projected
- Even when consciously understood, projection may continue
- "Projection is never conscious"—always there first, recognized after
- Beyond incest-fantasy: highly emotional religious contents

**Complete Chinese Interpretation (Secondary Language)**:

荣格定义**投射机制**：

**定义**：
- "无意识、自动的过程"
- 无意识内容"转移到对象上"
- 内容"似乎属于那个对象"
- 当识别为主体自身时投射停止

**父母投射**：
- 父母意象最常被投射
- 即使有意识理解，投射可能持续
- "投射从不是有意识的"——总是先存在，后识别
- 超越乱伦幻想：高度情感的宗教内容

**Core Points**:
- Projection = unconscious automatic transfer of content to object
- Projection ceases when made conscious (recognized as one's own)
- Parental imagos are most frequently projected
- Projection is never conscious—always exists before recognition
- Transference demonstrates parental projection onto analyst
- Beyond incest: religious/archetypal contents also projected

**Narrative Snippets**:
- `[ns_cw9i_II_007]` `[trigger: projection_definition]` `[factor_trigger: jung_projection]` `[role: 主干]` Projection is an unconscious, automatic process whereby a content transfers itself to an object, so that it seems to belong to that object—it ceases when made conscious. → ¶121
- `[ns_cw9i_II_008]` `[trigger: projection_unconscious]` `[factor_trigger: jung_projection]` `[role: 主干依赖]` Projection is never conscious: projections are always there first and are recognized afterwards. → ¶122"""
    normalized_text_zh: str = """"""
    subject: str = "3 Projection Mechanism (¶121-122)"
    factor_refs: list = ['engine_id', 'projection', 'psych_semantic', 'projection_withdrawal', 'psych_semantic', 'source_ref', 'opposites', 'projection_withdrawal', 'transforming', 'concept_projection', 'projection_dream']
    
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
        l1_anchor="acu_v1.0.0_3_projection_mechanism___121_1_001_L1",
    )
    version: str = "1.0.0"
