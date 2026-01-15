"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182511
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
    semantic_id="tb_v1.0.0_influence_of_position_with_reg_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class InfluenceOfPositionWithReg(SemanticEntry):
    """
    **Source Text** (Lines 1733-1767):
> The respective powers of the Moon and of the three superior pla...
    """
    
    original_text: str = """**Source Text** (Lines 1733-1767):
> The respective powers of the Moon and of the three superior planets are either augmented or diminished by their several positions with regard to the Sun. The Moon, during her increase, from her first emerging to her first quarter, produces chiefly moisture; on continuing her increase from her first quarter to her full state of illumination, she causes heat; from her full state to her third quarter she causes dryness; and from her third quarter to her occultation she causes cold. The planets, when matutine, and from their first emerging until they arrive at their first station, are chiefly productive of moisture; from their first station until they rise at night, of heat; from their rising at night until their second station, of dryness; and from their second station until their occultation, they produce cold.

**English Paraphrase (Primary Language)**:
Ptolemy describes how **planetary phase relative to Sun** modifies elemental qualities through a four-fold cycle.

**Moon's cycle** (synodic phases):
- New → 1st Quarter: Moisture (waxing crescent)
- 1st Quarter → Full: Heat (waxing gibbous)
- Full → 3rd Quarter: Dryness (waning gibbous)
- 3rd Quarter → New: Cold (waning crescent)

**Superior planets' cycle** (relative to Sun):
- Emergence → 1st Station: Moisture
- 1st Station → Opposition (night rising): Heat
- Opposition → 2nd Station: Dryness
- 2nd Station → Occultation: Cold

This creates a dynamic where the same planet expresses different qualities depending on its phase—a waxing Moon is moist/hot, a waning Moon is dry/cold. Configurations between planets further compound these variations.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密描述了**行星相对于太阳的位相**如何通过四重周期修改元素属性。

**月亮周期**（朔望周期）：
- 新月→上弦月：湿润（盈眉月）
- 上弦月→满月：炎热（盈凸月）
- 满月→下弦月：干燥（亏凸月）
- 下弦月→新月：寒冷（亏眉月）

**外行星周期**（相对于太阳）：
- 出现→第一次停滞：湿润
- 第一次停滞→冲（夜间升起）：炎热
- 冲→第二次停滞：干燥
- 第二次停滞→隐伏：寒冷

这创造了一种动态，同一颗行星根据其位相表达不同的属性——盈月是湿润/炎热的，亏月是干燥/寒冷的。行星之间的配置进一步复合这些变化。

**Core Points**:
- Moon's synodic cycle produces four elemental phases
- Superior planets follow parallel cycle based on Sun-position
- Waxing = moisture then heat; Waning = dryness then cold
- Phase modifies inherent planetary quality
- Configurations between planets create compound variations

**Narrative Snippets**:
- `[ns_tetra_i032]` `[trigger: moon_phase_quality]` `[factor_trigger: astro_planet_moon AND astro_lunar_phase]` `[role: 主干]` Moon from new to first quarter produces moisture; first quarter to full, heat; full to third quarter, dryness; third quarter to new, cold. → Source Text I.8
- `[ns_tetra_i033]` `[trigger: planet_phase_quality]` `[factor_trigger: astro_planet_superior AND astro_sun_position]` `[role: 主干]` Superior planets: emergence to first station = moisture; to opposition = heat; to second station = dryness; to occultation = cold. → Source Text I.8

**Textual Criticism**: Footnote notes this applies strictly to superior planets (Mars, Jupiter, Saturn); Venus and Mercury have different cycles due to limited elongation."""
    normalized_text_zh: str = """"""
    subject: str = "Influence of Position with Regard to the Sun (Chapter VIII)"
    factor_refs: list = ['lunar_phase', 'engine_id', 'lunar_phase', 'astrology_classical', 'source_ref', 'rel_i_012', 'lunar_phase', 'cycling', 'evi_i_008', 'lunar_phase', 'rule_lunar_phase', 'concept_phase', 'lunar_phase', 'mood_cycle']
    
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
        l1_anchor="tb_v1.0.0_influence_of_position_with_reg_001_L1",
    )
    version: str = "1.0.0"
