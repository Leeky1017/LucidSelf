"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162704
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
    semantic_id="tb_v1.0.0_peculiarities_throughout_clima_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class PeculiaritiesThroughoutClima(SemanticEntry):
    """
    **Source Text** (Lines 3056-3133):
> The peculiarities of all nations are distinguished according to...
    """
    
    original_text: str = """**Source Text** (Lines 3056-3133):
> The peculiarities of all nations are distinguished according to entire parallels and entire angles, and by their situation with regard to the Sun and the Ecliptic... nations under more southern parallels have the Sun in their zenith, are continually scorched, consequently black in complexion with thick curled hair, ugly, contracted stature, hot disposition, fierce manners... nations under more remote northern parallels have zenith far from zodiac, constitutions abound in cold and moisture, fair complexion, straight hair, large bodies, cold disposition, wild manners... nations between summer tropic and Arctic circle enjoy well-temperated atmosphere.

**English Paraphrase (Primary Language)**:
Ptolemy establishes **climatic astrology**—national characteristics derive from latitude and solar relationship:

- **Southern regions** (equator to tropic): Hot, dry → dark complexion, curled hair, small stature, fierce temperament ("Æthiopians")
- **Northern regions** (beyond Arctic): Cold, moist → fair complexion, straight hair, large bodies, wild manners ("Scythians")
- **Temperate zones** (between): Balanced → proportionate stature, civilized habits, good disposition

Further refinements: those toward south are more **industrious and ingenious** (proximity to zodiac); those toward east are more **courageous** (Sun's nature); those toward west are **milder, more feminine** (Moon's nature).

**Complete Chinese Interpretation (Secondary Language)**:
托勒密建立**气候占星学**——民族特征源于纬度和太阳关系：

- **南方地区**（赤道到回归线）：热、干→深色皮肤、卷发、矮小身材、凶猛气质（"埃塞俄比亚人"）
- **北方地区**（北极圈以外）：冷、湿→白皙皮肤、直发、高大身材、野蛮习性（"斯基泰人"）
- **温带**（介于两者之间）：平衡→匀称身材、文明习惯、良好性情

**Core Points**:
- Latitude determines national temperament
- Southern = hot/dry → dark, fierce
- Northern = cold/moist → fair, wild
- Temperate = balanced → civilized
- East = courageous (solar); West = mild (lunar)

**Narrative Snippets**:
- `[ns_tetra_ii002]` `[trigger: climatic_astrology]` `[factor_trigger: astro_geographic_latitude]` `[role: 主干]` National peculiarities derive from latitude—southern peoples are hot-tempered, northern cold-natured, temperate zones civilized. → Source Text II.2
- `[ns_tetra_ii017]` `[trigger: solar_lunar_quarter]` `[factor_trigger: astro_quarter AND astro_sun_moon]` `[role: 条件分支]` Eastern peoples are more courageous (Sun's nature); western peoples milder, more feminine (Moon's nature). → Quarter
- `[ns_tetra_ii018]` `[trigger: temperate_zone]` `[factor_trigger: astro_climate AND astro_civilization]` `[role: 条件分支]` Nations in temperate zones enjoy well-balanced atmosphere—proportionate stature, civilized habits, good disposition. → Balance
- `[ns_tetra_ii_nt01]` `[trigger: national_temperament]` `[factor_trigger: national_temperament]` `[role: 效果]` National temperament varies by latitude: southern peoples hot-tempered and fierce, northern peoples cold and wild, temperate zones civilized and balanced. → Source Text II.2"""
    normalized_text_zh: str = """"""
    subject: str = "Peculiarities Throughout Climates (Chapter II)"
    factor_refs: list = ['climatic_astrology']
    
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
        l1_anchor="tb_v1.0.0_peculiarities_throughout_clima_001_L1",
    )
    version: str = "1.0.0"
