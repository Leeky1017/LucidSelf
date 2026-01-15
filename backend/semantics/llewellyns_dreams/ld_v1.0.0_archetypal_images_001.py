"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386815
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
    semantic_id="ld_v1.0.0_archetypal_images_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class ArchetypalImages(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Archetypal Images | Univ...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Archetypal Images | Universal energy patterns | Pre-existing templates |
| Warrior/Nurturer | Power/Care archetypes | Key universal roles |
| Trickster | Chaos/transformation | Change agent |
| Activation Function | Dream calls principle | Current needs |

**Source Text** (Paraphrased):
> "Archetypes are universal energy patterns forming fundamental human ideas, represented by similar images across cultures. Warrior (power, defense), Nurturer (love, care), Trickster (chaos, transformation), Wise One (knowledge, guidance), Hero (quest, triumph). These are pre-existing patterns individuals embody rather than create. Dreaming of archetypal figure activates that principle in psyche."

**English Paraphrase**:
**Archetypal images**: universal energy patterns forming fundamental ideas, appearing across all cultures. **Key archetypes**: Warrior (power/defense), Nurturer (love/care), Trickster (chaos/transformation), Wise One (knowledge/guidance), Hero (quest/triumph), Shadow (dark opposite). **Pre-existing templates** humans embody not create—psychological instincts for meaning-making. **Dream function**: Archetypal figure activates that principle in psyche for current life needs.

**Complete Chinese Interpretation**:
**原型意象**：普遍能量模式形成基本观念，出现于所有文化。**关键原型**：战士（力量/防御）、养育者（爱/照顾）、骗子（混乱/转化）、智慧者（知识/引导）、英雄（探寻/胜利）、阴影（黑暗对立面）。**预存模板**人类体现非创造——意义生成的心理本能。**梦境功能**：原型人物激活该原则在心灵为当前生活需求。

#### Core Points

- **Universal Energy Patterns**: Archetypes are universal energy patterns forming fundamental human ideas across cultures.
- **Key Archetypes**: Warrior (power/defense), Nurturer (love/care), Trickster (chaos/transformation), Wise One, Hero, Shadow.
- **Pre-existing Templates**: Inherited patterns humans embody rather than create—psychological instincts.
- **Activation Function**: Dreaming of archetypal figure activates that principle in psyche for current needs.
- **Cross-cultural Consistency**: Similar images appear worldwide, validating universal nature.

#### Detailed Explanation

Archetypes are universal energy patterns forming fundamental human ideas, represented by similar images across cultures. Key archetypes include: Warrior (power, defense), Nurturer (love, care), Trickster (chaos, transformation), Wise One (knowledge, guidance), Hero (quest, triumph), Shadow (dark opposite). These are pre-existing patterns individuals embody rather than create—psychological instincts for meaning-making. The dream function: archetypal figure activates that principle in the psyche when that energy is needed for current life situations."""
    normalized_text_zh: str = """"""
    subject: str = "Archetypal Images"
    factor_refs: list = ['psych_archetype_images', 'psych_preexisting_templates', 'psych_archetype_trio', 'dream_archetype_activation']
    
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
        l1_anchor="ld_v1.0.0_archetypal_images_001_L1",
    )
    version: str = "1.0.0"
