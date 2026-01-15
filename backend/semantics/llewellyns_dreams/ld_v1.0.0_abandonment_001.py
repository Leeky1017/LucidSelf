"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386848
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
    semantic_id="ld_v1.0.0_abandonment_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class Abandonment(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Abandonment | Self-worth...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Abandonment | Self-worth fears | Primitive anxiety |
| Primitive Fear | Infant alone=death | Root of adult fear |
| Support Withdrawal | Which aspect gone | Character method |
| Who Abandons | Key interpretation | Self-aspect ID |

**Source Text** (Paraphrased):
> "Abandonment dreams reflect fears around self-worth. This is a primitive fear rooted in infancy—being left alone equals death for an infant. Dream processes abandonment feelings, prepares psyche for waking life scenarios. Pay attention to WHO abandons in dream—this is key to interpretation using character aspects method. The abandoner represents which self-aspect is withdrawing support?"

**English Paraphrase**:
**Abandonment**: reflects **fears around self-worth**. Primitive fear rooted in infancy (alone = death for infant). Dream processes abandonment feelings, prepares for waking life. **Key interpretation**: WHO abandons? That person/figure = self-aspect withdrawing support. Example: Parent abandons = internalized nurturing aspect unavailable. Partner abandons = love/acceptance aspect feels withdrawn.

**Complete Chinese Interpretation**:
**被遗弃**：反映**自我价值恐惧**。原始恐惧根植于婴儿期（独自=婴儿死亡）。梦处理遗弃感，准备清醒生活。**关键诠释**：谁遗弃？该人/人物=撤回支持的自我面相。例：父母遗弃=内化的养育面相不可得。伴侣遗弃=爱/接纳面相感觉撤回。

#### Core Points

- **Self-Worth Fears**: Abandonment dreams reflect fears around self-worth and value.
- **Primitive Root**: Rooted in infant survival anxiety—being alone equals death for an infant.
- **Who Abandons**: Pay attention to WHO abandons—this reveals which self-aspect withdraws support.
- **Character Aspect Method**: Parent=nurturance aspect; Partner=love/acceptance aspect.
- **Processing Function**: Dream processes abandonment feelings, prepares psyche for waking life.

#### Detailed Explanation

Abandonment dreams reflect fears around self-worth. This is a primitive fear rooted in infancy—being left alone equals death for an infant. The dream processes abandonment feelings and prepares the psyche for waking life scenarios. The key interpretation question: WHO abandons in the dream? Using the character aspects method, the abandoner represents which self-aspect is withdrawing support. Parent abandons = internalized nurturing aspect unavailable. Partner abandons = love/acceptance aspect feels withdrawn."""
    normalized_text_zh: str = """"""
    subject: str = "Abandonment"
    factor_refs: list = ['dream_symbol_abandonment', 'psych_primitive_fear', 'psych_support_withdrawal']
    
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
        l1_anchor="ld_v1.0.0_abandonment_001_L1",
    )
    version: str = "1.0.0"
