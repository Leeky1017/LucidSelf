"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386941
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
    semantic_id="ld_v1.0.0_nakedness_exposure_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class NakednessExposure(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Nakedness | Vulnerabilit...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Nakedness | Vulnerability/authenticity | Dual meaning |
| Fear of Judgment | Being seen truly | Shame |
| Others' Reactions | Projection mirror | Notice/accept/shame |
| Authentic Emergence | Dropping masks | Growth |

**Source Text** (Paraphrased):
> "Nakedness represents vulnerability, authenticity vs fear of judgment. Feeling exposed or revealed. Can indicate authentic self emerging or fear of being 'seen' truly. Others' reactions matter: If they don't notice nakedness = self-judgment not shared by others. If they shame = internalized judgment active."

**English Paraphrase**:
**Nakedness/Exposure**: **vulnerability, authenticity vs fear of judgment**. Feeling exposed, revealed, unprotected. **Dual meaning**: (1) Authentic self emerging (positive vulnerability) or (2) Fear of being "seen" truly (shame, judgment fear). **Others' reactions** key: They don't notice = self-judgment not shared; They shame = internalized judgment; They accept = safe to be authentic.

**Complete Chinese Interpretation**:
**裸体/暴露**：**脆弱、真实vs评判恐惧**。感觉暴露、揭示、无保护。**双重含义**：(1)真实自我浮现（正面脆弱）或(2)害怕被真正"看见"（羞耻、评判恐惧）。**他人反应**关键：他们未注意=自我评判非他人共享；他们羞辱=内化评判；他们接纳=可安全真实。

#### Core Points

- **Vulnerability/Authenticity**: Nakedness represents vulnerability, authenticity vs fear of judgment.
- **Dual Meaning**: Positive (authentic self emerging) OR dream_negative (fear of being truly "seen").
- **Others' Reactions Key**: Don't notice = self-judgment only; Shame = internalized judgment; Accept = safe.
- **Feeling Exposed**: Sense of being revealed, unprotected, without social masks.
- **Self-Acceptance Indicator**: How dreamer relates to nakedness shows self-acceptance level.

#### Detailed Explanation

Nakedness represents vulnerability, authenticity vs fear of judgment. It indicates feeling exposed, revealed, unprotected. Dual meaning: (1) Authentic self emerging (positive vulnerability) or (2) Fear of being "seen" truly (shame, judgment fear). Others' reactions are key: They don't notice = self-judgment not shared by others; They shame = internalized judgment active; They accept = safe to be authentic."""
    normalized_text_zh: str = """"""
    subject: str = "Nakedness/Exposure"
    factor_refs: list = ['dream_symbol_nakedness', 'psych_authentic_emergence', 'psych_fear_being_seen', 'dream_others_reactions']
    
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
        l1_anchor="ld_v1.0.0_nakedness_exposure_001_L1",
    )
    version: str = "1.0.0"
