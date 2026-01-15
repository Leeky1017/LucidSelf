"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238050
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
    semantic_id="ap_v1.0.0_entry_4__occult_astrology_crea_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry4OccultAstrologyCrea(SemanticEntry):
    """
    **Source Text** (Lines 6798-6956):
> 3. OCCULT ASTROLOGY: Occult astrology should not be considered ...
    """
    
    original_text: str = """**Source Text** (Lines 6798-6956):
> 3. OCCULT ASTROLOGY: Occult astrology should not be considered entirely apart from the two preceding types... We have seen that the gyration of the Poles is determined by a combination of factors: mainly, the rotation of the planet around its axis and the gravitational pull of the Sun...
>
> The involutionary process refers to the equatorial realm and the zodiac; the evolutionary process, to the polar axis and its motions...
>
> The zodiacal Hierarchies are hierarchies of Builders—Cosmocrea-tores... In and through the zodiac, earth-substance becomes Man. But along the path of the polar axis, the "tree" of the "I am," Man polarizes himself in turn to the seven great Rays of the Logos or God.

**Key Term Analysis**:
- **Occult astrology**: `creative-spiritual factor` / `polar axis emphasis` / `Divine Hierarchies`
- **Involution-Evolution**: `involution = zodiacal Builders construct astral prototype` / `evolution = polar axis, consciousness expansion`
- **Seven Rays**: `cosmic creative energies` / `Logos manifestation` / `permutation principle`
- **Stars as Teachers**: `not just symbols but cosmic Beings` / `influence planet and mankind`

**English Paraphrase (Primary Language)**:
**Occult Astrology** integrates individual and collective, emphasizing the creative/spiritual factor. The zodiacal Hierarchies ("Builders") represent involution—building the human prototype. The polar axis represents evolution—consciousness expansion through attunement to the Seven Rays.

"In and through the zodiac, earth-substance becomes Man. But along the path of the polar axis... Man polarizes himself to the seven great Rays of the Logos."

**Complete Chinese Interpretation (Secondary Language)**:
**神秘占星学**整合个体与集体，强调创造性/精神因素。黄道等级（"建造者"）代表退化——建造人类原型。极轴代表进化——通过与七道光的调谐实现意识扩展。

"在黄道中并通过黄道，地球物质成为人类。但沿着极轴的道路……人类将自己极化到圣言的七道大光。"

**Narrative Snippets**:
- `[ns_aop_151]` `[trigger: occult_astrology]` `[factor_trigger: astro_occult_type AND astro_occult_struct]` `[role: 主干]` Occult astrology: creative-spiritual factor, polar axis emphasis, Divine Hierarchies. → L6798-6810
- `[ns_aop_152]` `[trigger: involution_evolution]` `[factor_trigger: astro_invol_evol AND astro_rays]` `[role: 主干依赖]` Involution (zodiac, Builders) vs Evolution (polar axis, Seven Rays). → L6843-6874"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 4: Occult Astrology—Creative and Spiritual"
    factor_refs: list = ['astro_occult', 'astro_seven_rays']
    
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
        l1_anchor="ap_v1.0.0_entry_4__occult_astrology_crea_001_L1",
    )
    version: str = "1.0.0"
