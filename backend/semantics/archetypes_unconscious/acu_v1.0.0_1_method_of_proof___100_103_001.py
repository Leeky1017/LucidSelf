"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515606
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
    semantic_id="acu_v1.0.0_1_method_of_proof___100_103_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 1MethodOfProof100103(SemanticEntry):
    """
    **Source Text** (¶100-103, Lines 1691-1743):

> [100] Main source = dreams—involuntary, pure product...
    """
    
    original_text: str = """**Source Text** (¶100-103, Lines 1691-1743):

> [100] Main source = dreams—involuntary, pure products of nature.
> [101] Second source = active imagination—deliberate concentration on fantasy.
> [103] Other sources: paranoid delusions, trance fantasies, childhood dreams (3-5). Valueless without mythological parallels with same functional meaning.

**English Paraphrase**:
- **Dreams**: Main proof source—involuntary, spontaneous
- **Active imagination**: Deliberate fantasy concentration
- **Validation**: Requires mythological parallels with same functional meaning

**中文释义**：
- **梦**：主要证明来源——非自愿、自发
- **主动想象**：刻意的幻想专注
- **验证**：需要具有相同功能意义的神话平行"""
    normalized_text_zh: str = """"""
    subject: str = "1 Method of Proof (¶100-103)"
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
        l1_anchor="acu_v1.0.0_1_method_of_proof___100_103_001_L1",
    )
    version: str = "1.0.0"
