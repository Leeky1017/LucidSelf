"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238199
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
    semantic_id="ap_v1.0.0_entry_4__collective_unconsciou_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry4CollectiveUnconsciou(SemanticEntry):
    """
    **Source Text** (Lines 9290-9497):
> B. THE COLLECTIVE UNCONSCIOUS... This voice of the collective, ...
    """
    
    original_text: str = """**Source Text** (Lines 9290-9497):
> B. THE COLLECTIVE UNCONSCIOUS... This voice of the collective, insofar as it acts upon individuals, is symbolized by the trinity of remote planets: Uranus, Neptune and Pluto...
>
> Uranus is the projective power of the unconscious... Uranus is characterized by its image-forming power. It regenerates the conscious by bringing to it vistas of the whole...
>
> Neptune acts in more subtle and mysterious ways. It eats up like a strong acid the crystallizations of the ego...
>
> Pluto is the planet of the second birth, ruler of the Mysteries... Pluto represents the Law of the whole-Self in opposition to the law of the particular ego.

**Key Term Analysis**:
- **Uranus**: `projective power` / `image-forming` / `transformation/creation` / `genius or insanity`
- **Neptune**: `dissolving power` / `ego crystallizations` / `universalization` / `redemption`
- **Pluto**: `regenerating power` / `second birth` / `ruler of Mysteries` / `Law of whole-Self`
- **Discovery timing**: `Uranus (1781) = revolutions` / `Neptune (1846) = humanitarianism` / `Pluto (1930) = new social structures`

**English Paraphrase (Primary Language)**:
Three outer planets = "voice of collective unconscious" acting on individuals:

**Uranus**: "projective power... image-forming power" that transforms consciousness. "Genius or insanity; inspiration or perversion."

**Neptune**: "dissolving power... eats up ego crystallizations like strong acid." Universalization, compassion, redemption—or escape into artificial paradise.

**Pluto**: "planet of second birth, ruler of Mysteries." Represents "Law of whole-Self" vs ego law. "God-in-the-depths, God made concrete at center of personality."

**Complete Chinese Interpretation (Secondary Language)**:
三颗外行星 = "集体无意识的声音"作用于个体：

**天王星**："投射力量……形象形成力量"转化意识。"天才或疯狂；灵感或堕落。"

**海王星**："溶解力量……像强酸一样吞噬自我结晶。"普遍化、慈悲、救赎——或逃入人造天堂。

**冥王星**："第二次诞生的行星，神秘的统治者。"代表"整体自性的法则"vs自我法则。"深处的神，在人格中心具体化的神。"

**Narrative Snippets**:
- `[ns_aop_182]` `[trigger: uranus_function]` `[factor_trigger: astro_uranus_projective AND astro_uranus]` `[role: 主干]` Uranus: projective, image-forming power; transforms conscious. Genius or insanity. → L9343-9357
- `[ns_aop_183]` `[trigger: neptune_function]` `[factor_trigger: astro_neptune_dissolving AND astro_neptune]` `[role: 主干]` Neptune: dissolving power; eats ego crystallizations. Universalization or escape. → L9359-9389
- `[ns_aop_184]` `[trigger: pluto_function]` `[factor_trigger: astro_pluto_regenerating AND astro_pluto]` `[role: 主干]` Pluto: second birth, Mysteries; Law of whole-Self. God-in-depths. → L9391-9425"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 4: Collective Unconscious - Uranus, Neptune, Pluto"
    factor_refs: list = ['uranus_proj', 'neptune_diss', 'pluto_regen', 'collective_uncon']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_4__collective_unconsciou_001_L1",
    )
    version: str = "1.0.0"
