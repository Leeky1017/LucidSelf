"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515574
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
    semantic_id="acu_v1.0.0_2_individuation_and_therapy____001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 2IndividuationAndTherapy(SemanticEntry):
    """
    **Source Text** (¶83-86, Lines 1447-1495):

> [83] What appears brutally in insanity remains hidden ...
    """
    
    original_text: str = """**Source Text** (¶83-86, Lines 1447-1495):

> [83] What appears brutally in insanity remains hidden in neurosis but still influences consciousness. Pathology = dissociation of consciousness that can't control the unconscious. In all dissociation: integrate unconscious into consciousness—the "individuation process."
>
> [84] This process follows the natural course of life—individual becomes what he always was. Primitive therapy = restitution ceremonies (Australian alcheringa, Pueblos "sons of sun", Isis mysteries).
>
> [85] Archetypes are numinous and autonomous—cannot be integrated by rational means alone. Requires dialectical procedure—the alchemical meditatio: "an inner colloquy with one's good angel."

**English Paraphrase**:
- **Individuation defined**: Integrating unconscious into consciousness
- **Natural course**: Individual becomes what he always was
- **Primitive parallels**: Restitution ceremonies (alcheringa, Helios apotheosis)
- **Method**: Dialectical, not just rational; alchemical meditatio

**中文释义**：
- **个体化定义**：将无意识整合入意识
- **自然进程**：个体成为他一直是的
- **原始平行**：恢复仪式（alcheringa、赫利俄斯神化）
- **方法**：辩证的而非仅理性；炼金术冥想

**Narrative Snippets**:
- `[ns_cw9i_064]` `[trigger: individuation_defined]` `[factor_trigger: jung_individuation AND jung_integration]` `[role: 主干]` In all dissociation: integrate unconscious into consciousness—the "individuation process." → ¶83
- `[ns_cw9i_065]` `[trigger: dialectical_method]` `[factor_trigger: jung_archetype AND jung_alchemy]` `[role: 主干依赖]` Archetypes require dialectical procedure—the alchemical meditatio: "inner colloquy with one's good angel." → ¶85"""
    normalized_text_zh: str = """"""
    subject: str = "2 Individuation and Therapy (¶83-86)"
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
        l1_anchor="acu_v1.0.0_2_individuation_and_therapy____001_L1",
    )
    version: str = "1.0.0"
