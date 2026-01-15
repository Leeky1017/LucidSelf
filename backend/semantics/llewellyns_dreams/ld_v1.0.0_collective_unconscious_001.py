"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386742
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
    semantic_id="ld_v1.0.0_collective_unconscious_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class CollectiveUnconscious(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Collective Unconscious |...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Collective Unconscious | Universal psychic substrate | Shared by all humans |
| Same Dreams Worldwide | Cross-cultural themes | Validates universal symbols |
| Archetypal Patterns | Inherited not learned | Foundation of symbols |
| Personal vs Collective | Individual vs universal | Key differentiation |

**Source Text** (Paraphrased):
> "The collective unconscious, Jung's foundational concept, is the universal symbolic realm connecting all humans. Unlike personal unconscious (individual memories), collective unconscious contains archetypal information shared by humanity. Dreams tap this reservoir of universal symbols. Lennox observes 'same dreams' worldwide—Swiss businessmen and African natives dream similar themes, though cultural symbols differ. This shared symbolic language enables dream dictionaries providing universal meanings."

**English Paraphrase**:
**Collective unconscious**: universal psychic substrate shared by all humans, containing archetypal patterns transcending personal experience and culture. Lennox's key insight: **same dreams worldwide**—fundamental experiences (fear, love, death) generate similar themes across cultures. Swiss businessman dreaming of briefcase threat = African native dreaming of spear threat = **same archetype** (livelihood anxiety), different cultural dress.

**Universal symbols exist** because humanity shares biological heritage, developmental stages, emotional patterns, social structures.

**Complete Chinese Interpretation**:
**集体无意识**：全人类共享的普遍心理基质，包含超越个人经验和文化的原型模式。Lennox关键洞见：**全球相同梦境**——基本经验（恐惧、爱、死亡）跨文化产生相似主题。瑞士商人梦公文包威胁=非洲原住民梦长矛威胁=**同一原型**（生计焦虑），不同文化外衣。**普遍象征存在**因人类共享生物遗产、发展阶段、情感模式、社会结构。

#### Core Points

- **Universal Psychic Substrate**: The collective unconscious is shared by all humans, transcending personal experience and culture.
- **Same Dreams Worldwide**: Swiss businessmen and African natives dream similar themes—same archetype, different cultural dress.
- **Archetypal Information Inherited**: Universal patterns are inherited not learned, forming the basis of human symbolic thought.
- **Personal vs Collective Distinction**: Individual memories (personal) vs archetypal patterns (collective)—key differentiation for interpretation.
- **Foundation for Dream Dictionaries**: Shared symbolic language enables universal meanings applicable across cultures.

#### Detailed Explanation

Jung's collective unconscious is the universal symbolic realm connecting all humans. Unlike personal unconscious (individual memories), collective unconscious contains archetypal information shared by humanity. Dreams tap this reservoir of universal symbols. Lennox observes 'same dreams' worldwide—Swiss businessmen and African natives dream similar themes, though cultural symbols differ. A briefcase threat and a spear threat represent the same archetype (livelihood anxiety) in different cultural dress. This shared symbolic language enables dream dictionaries providing universal meanings. Universal symbols exist because humanity shares biological heritage, developmental stages, emotional patterns, and social structures."""
    normalized_text_zh: str = """"""
    subject: str = "Collective Unconscious"
    factor_refs: list = ['psych_collective_unconscious', 'psych_archetype_info', 'dream_symbol_universal', 'dream_same_worldwide']
    
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
        l1_anchor="ld_v1.0.0_collective_unconscious_001_L1",
    )
    version: str = "1.0.0"
