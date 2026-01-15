"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386901
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
    semantic_id="ld_v1.0.0_death_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class Death(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Death | Transformation/e...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Death | Transformation/endings | Rarely literal |
| Ego Death | Identity shift | Self death |
| Symbolic Death | Old dies for new | Positive reframe |
| Character Death | Aspect transforms | Adjective method |

**Source Text** (Paraphrased):
> "Death represents transformation, endings, new beginnings—rarely literal death prediction. Symbolic death of old self or situation to make room for new. Death of known person = that character aspect transforming. Death of self = ego death, major identity shift."

**English Paraphrase**:
**Death**: **transformation, endings, new beginnings**—rarely literal death prediction. **Symbolic death**: Old self/situation dying to make room for new. **Death variations**: Death of known person = that character aspect (adjective method) transforming/ending; Death of self = ego death, major identity transformation; Death of stranger = unknown aspect releasing. Always ask: "What is ending to make room for what new?"

**Complete Chinese Interpretation**:
**死亡**：**转化、结束、新开端**——罕为字面死亡预测。**象征性死亡**：旧我/情况死亡为新腾空间。**死亡变体**：熟人死=该人格面相（形容词法）转化/结束；自我死=小我死亡、重大身份转化；陌生人死=未知面相释放。总问："什么结束为什么新事物腾空间？"

#### Core Points

- **Transformation, Not Literal**: Death represents transformation, endings, new beginnings—rarely literal prediction.
- **Symbolic Death**: Old self/situation dying to make room for new growth.
- **Character Death**: Death of known person = that character aspect transforming (use adjective method).
- **Ego Death**: Death of self = major identity transformation, not physical death.
- **Key Question**: Always ask "What is ending to make room for what new?"

#### Detailed Explanation

Death represents transformation, endings, and new beginnings—rarely literal death prediction. Symbolic death means the old self or situation is dying to make room for the new. Death variations: death of a known person = that character aspect (use the adjective method) is transforming or ending; death of self = ego death, major identity shift; death of stranger = unknown aspect releasing. Always ask the key question: "What is ending to make room for what new?""""
    normalized_text_zh: str = """"""
    subject: str = "Death"
    factor_refs: list = ['dream_symbol_death', 'dream_symbolic_death', 'psych_ego_death', 'dream_transform_metaphor']
    
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
        book_id="llewellyns_dreams",
        chapter="",
        l1_anchor="ld_v1.0.0_death_001_L1",
    )
    version: str = "1.0.0"
