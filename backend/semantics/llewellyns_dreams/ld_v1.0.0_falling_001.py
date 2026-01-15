"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386893
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
    semantic_id="ld_v1.0.0_falling_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class Falling(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Falling | Loss of contro...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Falling | Loss of control | Anxiety dream |
| Insecurity | Unsupported feeling | Fear of failure |
| Landing Outcome | Safe/crash | Survival expectation |
| Waking Before Impact | Unresolved anxiety | Common pattern |

**Source Text** (Paraphrased):
> "Falling represents loss of control, insecurity, fear of failure. Common anxiety dream. Indicates feeling unsupported or overwhelmed in waking life. Landing safely vs crashing shows outcome expectation—will you survive this loss of control?"

**English Paraphrase**:
**Falling**: **loss of control, insecurity, fear of failure**. Common anxiety dream indicating: Feeling unsupported, Overwhelmed by circumstances, Fear of failing, Loss of stability. **Landing matters**: Soft landing = resilience, will survive; Crashing = catastrophic outcome feared; Never landing (waking before impact) = unresolved anxiety.

**Complete Chinese Interpretation**:
**坠落**：**失控、不安全、失败恐惧**。常见焦虑梦指示：感觉无支持、被环境压倒、害怕失败、失去稳定。**着陆重要**：软着陆=韧性，将生存；坠毁=恐惧灾难性结果；从不着陆（撞击前醒来）=未解决焦虑。

#### Core Points

- **Loss of Control**: Falling represents loss of control, insecurity, fear of failure.
- **Common Anxiety Dream**: One of the most common stress-response dreams.
- **Feeling Unsupported**: Indicates feeling unsupported or overwhelmed in waking life.
- **Landing Outcome**: Soft landing = resilience; crashing = catastrophe feared; no landing = unresolved.
- **Waking Before Impact**: Common pattern indicating unresolved anxiety.

#### Detailed Explanation

Falling represents loss of control, insecurity, and fear of failure. It is a common anxiety dream indicating: feeling unsupported, overwhelmed by circumstances, fear of failing, loss of stability. The landing matters significantly: soft landing = resilience, will survive this loss of control; crashing = catastrophic outcome feared; never landing (waking before impact) = unresolved anxiety about the situation."""
    normalized_text_zh: str = """"""
    subject: str = "Falling"
    factor_refs: list = ['dream_symbol_falling', 'dream_landing_outcome', 'psych_loss_support']
    
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
        l1_anchor="ld_v1.0.0_falling_001_L1",
    )
    version: str = "1.0.0"
