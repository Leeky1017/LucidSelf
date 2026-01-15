"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.541788
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
    semantic_id="acu_v1.0.0_section_3__anima__animus__and__001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class Section3AnimaAnimusAnd(SemanticEntry):
    """
    **Source Text** (¶511-518, Lines 7900-7990):

> [511] In the unconscious of every man there is hidde...
    """
    
    original_text: str = """**Source Text** (¶511-518, Lines 7900-7990):

> [511] In the unconscious of every man there is hidden a feminine personality, and in that of every woman a masculine personality.
>
> [512] A man therefore has in him a feminine side, an unconscious feminine figure—a fact of which he is generally quite unaware. I may take it as known that I have called this figure the "anima," and its counterpart in a woman the "animus."
>
> [513] Another, no less important and clearly defined figure is the "shadow." Like the anima, it appears either in projection on suitable persons, or personified as such in dreams. The shadow coincides with the "personal" unconscious... The shadow personifies everything that the subject refuses to acknowledge about himself and yet is always thrusting itself upon him directly or indirectly—for instance, inferior traits of character and other incompatible tendencies.
>
> [514] The fact that the unconscious spontaneously personifies certain affectively toned contents in dreams is the reason why I have taken over these personifications in my terminology and formulated them as names.
>
> [515-516] Besides these figures there are still a few others, less frequent and less striking, which have likewise undergone poetic as well as mythological formulation—the figure of the hero and the wise old man. All these figures irrupt autonomously into consciousness as soon as it gets into a pathological state. They show the most striking connections with mythological ideas completely unknown to the layman. The case of Benoît's L'Atlantide paralleling Rider Haggard's She—the lawsuit proved unsuccessful; Benoît had never heard of She.
>
> [517] When one studies the archetypal personalities with the help of dreams, fantasies, and delusions of patients, one is profoundly impressed by their manifold connections with mythological ideas. They form a species of singular beings whom one would like to endow with ego-consciousness. Yet they show all the marks of fragmentary personalities—masklike, wraithlike, without problems, lacking self-reflection, with no conflicts, no doubts, no sufferings; like gods who have no philosophy. They always remain strangers in consciousness, unwelcome intruders saturating the atmosphere with uncanny forebodings.
>
> [518] They evidently live and function in the deeper layers of the unconscious, especially in that phylogenetic substratum which I have called the collective unconscious. It is the mind of our unknown ancestors, their way of thinking and feeling, their way of experiencing life and the world, gods and men.
>
> [519] The anima and animus live in a world quite different from the world outside—in a world where the pulse of time beats infinitely slowly, where the birth and death of individuals count for little. No wonder their nature is strange, so strange that their irruption into consciousness often amounts to a psychosis.

**English Paraphrase**: Every man has hidden feminine personality (anima); every woman has masculine (animus). Shadow = personal unconscious, personifies what subject refuses to acknowledge (inferior traits). Anima/animus/shadow live in deeper layers—collective unconscious (phylogenetic substratum). It is the mind of unknown ancestors. Anima/animus live where time beats infinitely slowly—their irruption into consciousness often amounts to psychosis.

**中文诠释**: 每个男人有隐藏的女性人格（阿尼玛）；每个女人有男性（阿尼姆斯）。阴影=个人无意识，人格化主体拒绝承认的（低劣特质）。阿尼玛/阿尼姆斯/阴影生活在更深层——集体无意识（种系发生基层）。它们将未知的祖先心理生活带入意识。

**Narrative Snippets**:
- `[ns_cw9i_VIII_004]` `[trigger: anima_animus]` `[factor_trigger: jung_anima AND jung_animus]` `[role: 主干]` Anima (in man) and animus (in woman) = contrasexual unconscious personality. → ¶511-512
- `[ns_cw9i_VIII_005]` `[trigger: shadow_define]` `[factor_trigger: jung_shadow AND jung_personal]` `[role: 主干依赖]` Shadow = personal unconscious, personifies refused inferior traits. → ¶513"""
    normalized_text_zh: str = """"""
    subject: str = "Section 3: Anima, Animus, and Shadow (¶511-518)"
    factor_refs: list = ['anima_definition', 'animus_definition', 'shadow_definition', 'collective_location']
    
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_section_3__anima__animus__and__001_L1",
    )
    version: str = "1.0.0"
