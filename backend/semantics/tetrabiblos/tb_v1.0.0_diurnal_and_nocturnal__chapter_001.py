"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182498
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
    semantic_id="tb_v1.0.0_diurnal_and_nocturnal__chapter_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class DiurnalAndNocturnalChapter(SemanticEntry):
    """
    **Source Text** (Lines 1699-1725):
> The day and the night are the visible divisions of time. The da...
    """
    
    original_text: str = """**Source Text** (Lines 1699-1725):
> The day and the night are the visible divisions of time. The day, in its heat and its aptitude for action, is masculine:—the night, in its moisture and its appropriation to rest, feminine. Hence, again, the Moon and Venus are esteemed to be nocturnal; the Sun and Jupiter, diurnal; and Mercury, common; since in his matutine position he is diurnal, but nocturnal when vespertine. Of the other two planets, Saturn and Mars, which are noxious, one is considered to be diurnal, and the other nocturnal. Neither of them, however, is allotted to that division of time with which its nature accords (as heat accords with heat), but each is disposed of on a contrary principle: and for this reason, that, although the benefit is increased when a favourable temperament receives an addition of its own nature, yet, the evil arising from a pernicious influence is much mitigated when dissimilar qualities are mingled with that influence. Hence the coldness of Saturn is allotted to the day, to counterbalance its heat; and the dryness of Mars to the night, to counterbalance its moisture.

**English Paraphrase (Primary Language)**:
Ptolemy establishes the **sect** (αἵρεσις) doctrine—planets belong to either the day or night sect based on their qualities and the principle of **mitigation through opposition**.

**Sect assignments**:
- **Diurnal (Day sect)**: Sun, Jupiter, Saturn
- **Nocturnal (Night sect)**: Moon, Venus, Mars
- **Common**: Mercury (diurnal when matutine, nocturnal when vespertine)

The logic for benefics is straightforward: Sun and Jupiter (warm) belong to the warm day; Moon and Venus (moist) belong to the moist night. But malefics are assigned **contrarily** to mitigate their harm: Saturn (cold) is placed in the hot day to temper his coldness; Mars (dry/hot) is placed in the moist night to temper his dryness. This is a key principle: **similars strengthen, contraries temper**.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密建立了**派系**（αἵρεσις）教义——行星根据其属性和**通过对立缓和**的原则属于日派或夜派。

**派系分配**：
- **日间派（日派）**：太阳、木星、土星
- **夜间派（夜派）**：月亮、金星、火星
- **共同**：水星（晨星时为日间，昏星时为夜间）

吉星的逻辑很简单：太阳和木星（温暖）属于温暖的白天；月亮和金星（湿润）属于湿润的夜晚。但凶星被**相反地**分配以缓和其伤害：土星（寒冷）被置于炎热的白天以调和其寒冷；火星（干燥/炎热）被置于湿润的夜晚以调和其干燥。这是一个关键原则：**同类强化，对立调和**。

**Core Points**:
- Day = masculine, hot, active; Night = feminine, moist, restful
- Diurnal sect: Sun, Jupiter, Saturn
- Nocturnal sect: Moon, Venus, Mars
- Mercury is common (varies by position)
- Benefics assigned by affinity (similar strengthens)
- Malefics assigned contrarily (dissimilar tempers)
- Saturn (cold) → Day (hot) to mitigate
- Mars (dry) → Night (moist) to mitigate

**Narrative Snippets**:
- `[ns_tetra_i030]` `[trigger: sect_doctrine]` `[factor_trigger: astro_planet_sect]` `[role: 主干]` Day is masculine and hot; night is feminine and moist—planets are assigned accordingly. → Source Text I.7
- `[ns_tetra_i031]` `[trigger: malefic_mitigation]` `[factor_trigger: astro_planet_saturn OR astro_planet_mars]` `[role: 主干]` Malefics are assigned contrarily: Saturn's cold to day's heat, Mars's dryness to night's moisture—to mitigate harm. → Source Text I.7

**Textual Criticism**: N/A: Sect doctrine is foundational and consistent."""
    normalized_text_zh: str = """"""
    subject: str = "Diurnal and Nocturnal (Chapter VII)"
    factor_refs: list = []
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_diurnal_and_nocturnal__chapter_001_L1",
    )
    version: str = "1.0.0"
