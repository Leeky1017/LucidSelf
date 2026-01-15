"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386780
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
    semantic_id="ld_v1.0.0_character_aspects_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class CharacterAspects(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Character Aspects | Drea...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Character Aspects | Dream figures = self-parts | Externalized personality |
| 3-Adjective Method | Assign 3 adjectives | Practical technique |
| Fractured Personality | Unified self as multiple | For examination |
| Inner Dialogue | Aspect communication | Empowering insight |

**Source Text** (Paraphrased):
> "Every person in dreams represents an aspect of your personality—a character aspect. Lennox's core technique uses 3-adjective method: spontaneously assign three adjectives to dream person, these describe an aspect of yourself. Example: harsh, demanding teacher = your inner critic. All dream characters are fractured parts of total Self, projected outward for examination."

**English Paraphrase**:
**Character aspects**: all dream people = facets of dreamer's personality, not literal others but **self-parts externalized**. **3-adjective technique**: (1) Recall dream person (2) Assign 3 spontaneous adjectives (harsh, demanding, critical) (3) Apply to self: "I have a harsh, demanding, critical aspect." Dreams present **fragmented personality** as multiple characters—inner critic, rebel, nurturer, shadow. **Empowering insight**: No one "doing something to you"—all parts of yourself in dialogue.

**Complete Chinese Interpretation**:
**人格面相**：所有梦中人=梦者人格面向，非他人字面表征而是**自我部分外化**。**三形容词技术**：(1)回忆梦中人(2)分配3自发形容词(苛刻、要求、批判)(3)应用于自我："我有苛刻、要求、批判的面向。"梦呈现**碎片化人格**为多个角色——内在批评者、反叛者、养育者、阴影。**赋权洞见**：无人"对你做什么"——全是你自身部分在对话。

#### Core Points

- **Dream Figures as Self-Parts**: Every person in dreams represents an aspect of your personality, not literal others.
- **3-Adjective Method**: Spontaneously assign three adjectives to dream person—these describe an aspect of yourself.
- **Fractured Personality**: Unified self presented as multiple characters—inner critic, rebel, nurturer, shadow.
- **Inner Dialogue**: Dream interactions are communication between different self-aspects.
- **Empowering Insight**: No one is "doing something to you"—all parts of yourself in dialogue.

#### Detailed Explanation

Every person in dreams represents an aspect of your personality—a character aspect. Lennox's core technique uses the 3-adjective method: spontaneously assign three adjectives to a dream person, and these describe an aspect of yourself. Example: harsh, demanding teacher = your inner critic. All dream characters are fractured parts of the total Self, projected outward for examination. This transforms interpretation from victim stance ("they did this to me") to author stance ("this part of me is in dialogue"). The empowering insight is that no one is "doing something to you"—all are parts of yourself in dialogue."""
    normalized_text_zh: str = """"""
    subject: str = "Character Aspects"
    factor_refs: list = ['dream_character_aspects', 'dream_3adj_method', 'psych_fractured_personality', 'psych_inner_dialogue']
    
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
        l1_anchor="ld_v1.0.0_character_aspects_001_L1",
    )
    version: str = "1.0.0"
