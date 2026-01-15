"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.109884
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
    semantic_id="tis_v1.0.0_opposition__180_____tension_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class Opposition180Tension(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Opposition | 180° aspect, planets across zodiac | Polarization of energies |
| Projection | Seeing own traits in others | Relationship dynamic |
| Integration | Balancing opposing forces | Developmental goal |

#### Source Text

"The opposition is one of the 'bad' aspects in old-time astrology. It is true that this aspect produces tension. Two planets, separated by 180 degrees, are as far apart as they can get. Each one represents a distinct fragment of our personalities. And they are pulling in opposite directions. The problem—and the opportunity—with the opposition is that we tend to project one end of it onto other people."

#### English Paraphrase (Primary Language)

The **opposition** (180°) creates **polarization**: two planetary energies pulling in completely opposite directions. Traditional astrology labels this "bad," but Forrest reframes it as a **developmental challenge**.

**Key dynamic**: We often **project** one end of the opposition onto others. If Sun opposes Moon, we may identify with the Sun (ego, will) and project the Moon (emotions, needs) onto partners, seeing them as "too emotional" while denying our own feelings.

**Integration path**: The opposition demands we **own both ends**—recognizing that the "other person's" qualities are actually our own disowned aspects. When integrated, opposition becomes a source of **balance and perspective**.

#### Complete Chinese Interpretation (Secondary Language)

**对分相**（180度）创造**极化**：两种行星能量朝完全相反的方向拉扯。传统占星将此标记为"凶"，但Forrest将其重新定义为**发展性挑战**。

**关键动态**：我们经常将对分相的一端**投射**到他人身上。如果太阳对分月亮，我们可能认同太阳（自我、意志）而将月亮（情感、需求）投射到伴侣身上，认为他们"太情绪化"同时否认自己的感受。

**整合路径**：对分相要求我们**拥有两端**——认识到"他人的"品质实际上是我们自己被否认的面向。整合后，对分相成为**平衡与视角**的来源。

#### Core Points

- **180° aspect**: Maximum separation, polar opposition
- **Projection tendency**: One end externalized onto others
- **Relationship aspect**: Often manifests through partnerships
- **Integration challenge**: Own both poles for balance

#### Detailed Explanation

The opposition represents the **maximum distance** two planets can achieve—they face each other across the zodiac like antagonists in a duel. Forrest's key insight is that this opposition often manifests externally through **projection**: we identify with one planet and project the other onto partners, enemies, or significant others.

This projection mechanism makes oppositions fundamentally **relationship aspects**. Sun opposite Moon may manifest as attracting partners who embody the lunar qualities we deny in ourselves. Mars opposite Venus may create relationships where desire and conflict become intertwined. The people we attract often carry our disowned planets.

**Integration** is the developmental task. The person must recognize that both poles exist within them—the qualities they admire or despise in others are actually their own unlived potential. When both ends are consciously owned, the opposition becomes a source of **balance, perspective, and completeness**. The tension transforms into productive dialogue rather than external conflict.

Unlike the square's internal friction, the opposition's tension often feels **external** until integration occurs. This can make it harder to recognize as one's own issue—"it's always the other person's fault" is a classic opposition pattern.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Forrest's opposition interpretation emphasizes projection and integration rather than simple conflict. This aligns with Jungian shadow work concepts.
- **中文**: Forrest的对分相诠释强调投射与整合而非简单冲突。这与荣格阴影工作概念一致。

**Narrative Snippets**:
- `[ns_forrest_asp_003]` `[trigger: opposition]` `[factor_trigger: opposition AND projection]` `[role: 主干]` The opposition produces tension with two planets pulling in opposite directions, often leading to projection onto others. → Source Text
- `[ns_forrest_asp_004]` `[trigger: projection]` `[factor_trigger: aspect_opposition AND projection_mechanism]` `[role: 主干依赖]` We tend to project one end of the opposition onto other people, denying that quality in ourselves. → English Paraphrase
- `[ns_forrest_asp_013]` `[trigger: opposition_integration]` `[factor_trigger: aspect_opposition AND aspect_integration]` `[role: 条件分支]` The opposition demands we own both ends—recognizing that the "other person's" qualities are our own disowned aspects. → Integration
- `[ns_forrest_asp_014]` `[trigger: relationship_aspect]` `[factor_trigger: aspect_opposition AND relationship_dynamic]` `[role: 条件分支]` Opposition is fundamentally a relationship aspect—the people we attract often carry our disowned planets. → Relationship"""
    normalized_text_zh: str = """"""
    subject: str = "Opposition (180°) - Tension"
    factor_refs: list = ['aspect_opposition', 'new_candidate', 'new_candidate', 'engine_id', 'aspect_opposition', 'astro_semantic', 'new_candidate', 'astro_semantic', 'new_candidate', 'astro_semantic', 'source_ref', 'rel_forrest_opp_001', 'aspect_opposition', 'polarizing', 'rel_forrest_opp_002', 'opposition', 'integrating', 'evi_forrest_opp_001', 'rule_aspect_opposition', 'concept_opposition', 'chong_clash', 'conflict_dream']
    
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_opposition__180_____tension_001_L1",
    )
    version: str = "1.0.0"
