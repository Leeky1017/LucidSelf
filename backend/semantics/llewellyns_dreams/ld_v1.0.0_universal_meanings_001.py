"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386826
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
    semantic_id="ld_v1.0.0_universal_meanings_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class UniversalMeanings(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Universal Meanings | Inh...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Universal Meanings | Inherent function first | Objective grounding |
| Inherent Function | Physical/biological role | Meaning source |
| Two-Step Process | Universal then personal | Method order |
| Symbol Function | Three sources | Physical/cultural/biological |

**Source Text** (Paraphrased):
> "Lennox's interpretive approach prioritizes the symbol's universal meaning held in its use, essence, purpose, and inherent qualities—not personal associations first. This grounds interpretation in objective symbolism before personalizing. For example, abdomen universally represents emotions and gut feelings because that is its inherent function (we 'feel' emotions in the belly, 'gut instincts'). This is true regardless of any individual's specific abdomen experiences. Start with universal meaning, then layer personal associations. This makes dream dictionaries valuable: they provide universal baseline from which personal meanings elaborate."

**English Paraphrase**:
**Universal meanings approach**: Lennox method—interpret symbol's **universal meaning** based on **inherent function/essence/purpose** first, then personalize. Why this works: Symbols accumulate universal meanings through **inherent function** (abdomen = digestion/emotions), **cross-cultural use** (fire = transformation/passion), **biological/evolutionary significance** (snake = danger/transformation). **Two-step process**: (1) Identify universal baseline (2) Add personal associations. Example: Water universally = emotions/unconscious. Personal layer: "Ocean in my childhood = freedom" adds nuance but doesn't replace universal foundation.

**Complete Chinese Interpretation**:
**普遍含义法**：Lennox方法——先诠释象征的**普遍含义**基于**固有功能/本质/目的**，再个性化。为何有效：象征通过**固有功能**（腹部=消化/情绪）、**跨文化使用**（火=转化/激情）、**生物/进化意义**（蛇=危险/转化）积累普遍含义。**两步过程**：(1)识别普遍基线(2)添加个人联想。例：水普遍=情绪/无意识。个人层：“童年海洋=自由”添加细微差别但不替代普遍基础。

#### Core Points

- **Universal Meaning First**: Interpret symbol's universal meaning based on inherent function/essence/purpose first.
- **Inherent Function Source**: Symbols derive meaning from physical/biological role (abdomen = digestion → emotions).
- **Two-Step Process**: (1) Identify universal baseline (2) Add personal associations—universal = foundation.
- **Dream Dictionary Value**: Provides universal baselines from which personal meanings elaborate.
- **Objective Grounding**: Universal layer prevents purely subjective interpretation.

#### Detailed Explanation

Lennox's interpretive approach prioritizes the symbol's universal meaning held in its use, essence, purpose, and inherent qualities—not personal associations first. This grounds interpretation in objective symbolism before personalizing. For example, abdomen universally represents emotions and gut feelings because that is its inherent function. Symbols accumulate universal meanings through inherent function (abdomen = digestion/emotions), cross-cultural use (fire = transformation/passion), biological/evolutionary significance (snake = danger/transformation). Two-step process: (1) Identify universal baseline (2) Add personal associations. This makes dream dictionaries valuable as they provide universal baselines from which personal meanings elaborate."""
    normalized_text_zh: str = """"""
    subject: str = "Universal Meanings"
    factor_refs: list = ['dream_universal_meaning', 'dream_inherent_function', 'dream_twostep_process', 'dream_objective_grounding']
    
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
        l1_anchor="ld_v1.0.0_universal_meanings_001_L1",
    )
    version: str = "1.0.0"
