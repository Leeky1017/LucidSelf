"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386856
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
    semantic_id="ld_v1.0.0_abdomen_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class Abdomen(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Abdomen | Emotions/gut f...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Abdomen | Emotions/gut feelings | Body location |
| Gut Feelings | Visceral knowing | Instinctive |
| Self-Nourishment | Life feeding quality | Self-care |
| Compromised | Pain/injury | Repression signal |

**Source Text** (Paraphrased):
> "Abdomen as body part associated with emotions and gut feelings. Dream featuring abdomen indicates issue with trusting instincts. Compromised abdomen (pain, injury) represents repressing gut feelings. Also relates to digestion and self-care—how well is life feeding you? Are you nourishing yourself properly?"

**English Paraphrase**:
**Abdomen**: body part associated with **emotions and gut feelings**. Dream featuring abdomen = issue with **trusting instincts**. Compromised abdomen (pain, injury, disease) = repressing gut feelings, not trusting intuition. Also **digestion/self-care** = how well life feeds you. Healthy abdomen = good self-nourishment; damaged abdomen = poor self-care.

**Complete Chinese Interpretation**:
**腹部**：与**情绪和直觉**相关身体部位。梦中腹部=**信任本能**问题。受损腹部（疼痛、伤害、疾病）=压抑直觉，不信任直觉。也**消化/自我照顾**=生活滋养你程度。健康腹部=良好自我滋养；受损腹部=不良自我照顾。

#### Core Points

- **Emotions/Gut Feelings**: Abdomen as body part associated with emotions and gut feelings.
- **Trusting Instincts**: Dream featuring abdomen indicates issue with trusting instincts.
- **Compromised = Repression**: Compromised abdomen (pain, injury) = repressing gut feelings.
- **Self-Nourishment**: Also relates to digestion and self-care—how well is life feeding you?
- **Physical→Emotional Layering**: Physical digestion connects to emotional processing.

#### Detailed Explanation

Abdomen as a body part is associated with emotions and gut feelings. A dream featuring the abdomen indicates an issue with trusting instincts. A compromised abdomen (pain, injury, disease) represents repressing gut feelings, not trusting intuition. It also relates to digestion and self-care: How well is life feeding you? Are you nourishing yourself properly? Healthy abdomen = good self-nourishment; damaged abdomen = poor self-care."""
    normalized_text_zh: str = """"""
    subject: str = "Abdomen"
    factor_refs: list = ['dream_symbol_abdomen', 'psych_gut_feelings', 'psych_self_nourishment']
    
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
        l1_anchor="ld_v1.0.0_abdomen_001_L1",
    )
    version: str = "1.0.0"
