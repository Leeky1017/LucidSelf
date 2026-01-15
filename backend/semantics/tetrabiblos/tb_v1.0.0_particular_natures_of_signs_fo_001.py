"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162867
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
    semantic_id="tb_v1.0.0_particular_natures_of_signs_fo_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ParticularNaturesOfSignsFo(SemanticEntry):
    """
    **Source Text** (Lines 4296-4378):
> The sign of Aries has a general tendency to promote thunder and...
    """
    
    original_text: str = """**Source Text** (Lines 4296-4378):
> The sign of Aries has a general tendency to promote thunder and hail. Its front parts excite rain and wind; the middle are temperate; those behind are heating and pestilential. The northern parts are heating and pernicious, but the southern cooling and frosty. Taurus: the front parts heating, the middle temperate, the hinder parts exciting wind. Gemini: temperate throughout. Cancer: spring-like. Leo: hot and stifling. Virgo: moist and stormy. Libra: changeable. Scorpio: fiery and pestilential. Sagittarius: windy. Capricorn: moist. Aquarius: cold and watery. Pisces: cold and windy.

**English Paraphrase (Primary Language)**:
Each **zodiacal sign** has weather-producing qualities in its parts:

| Sign | General Quality | Front | Middle | Back |
|------|-----------------|-------|--------|------|
| Aries | Thunder/hail | Rain/wind | Temperate | Hot/pestilent |
| Taurus | Variable | Heating | Temperate | Windy |
| Gemini | Temperate | — | — | — |
| Cancer | Spring-like | — | — | — |
| Leo | Hot/stifling | — | — | — |
| Virgo | Moist/stormy | — | — | — |
| Libra | Changeable | — | — | — |
| Scorpio | Fiery/pestilent | — | — | — |
| Sagittarius | Windy | — | — | — |
| Capricorn | Moist | — | — | — |
| Aquarius | Cold/watery | — | — | — |
| Pisces | Cold/windy | — | — | — |

**Complete Chinese Interpretation (Secondary Language)**:
每个**黄道星座**在其各部分都有产生天气的特质：

| 星座 | 一般特质 | 前部 | 中部 | 后部 |
|-----|---------|-----|------|-----|
| 白羊座 | 雷雹 | 雨风 | 温和 | 热/疫病 |
| 金牛座 | 多变 | 加热 | 温和 | 多风 |
| 双子座 | 温和 | — | — | — |
| 巨蟹座 | 春季般 | — | — | — |
| 狮子座 | 热/闷 | — | — | — |
| 室女座 | 湿/暴风 | — | — | — |

**Core Points**:
- Each sign produces specific weather
- Sign parts (front/middle/back) have different effects
- Northern/southern parts also differ
- Foundation for weather prediction by Moon position

**Narrative Snippets**:
- `[ns_tetra_ii_014]` `[trigger: sign_weather]` `[factor_trigger: astro_sign_weather_quality]` `[role: 主干]` Each sign has weather-producing qualities—Aries brings thunder and hail, Leo is hot and stifling. → Source Text II.12
- `[ns_tetra_ii_we]` `[trigger: weather_effect]` `[factor_trigger: weather_effect]` `[role: 效果]` Weather effect produced by Moon's sign position: thunder, hail, rain, heat, storms, or temperate conditions according to sign's nature. → Source Text II.12"""
    normalized_text_zh: str = """"""
    subject: str = "Particular Natures of Signs for Weather (Chapter XII)"
    factor_refs: list = ['engine_id', 'sign_weather_quality', 'astrology_classical', 'source_ref', 'rel_ii_014', 'astro_sign_weather_quality', 'producing', 'evi_ii_014', 'sign_weather_quality', 'rule_sign_weather', 'concept_sign_weather', 'sign_weather_quality', 'mood_weather']
    
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
        l1_anchor="tb_v1.0.0_particular_natures_of_signs_fo_001_L1",
    )
    version: str = "1.0.0"
