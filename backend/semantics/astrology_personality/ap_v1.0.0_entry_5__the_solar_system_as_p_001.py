"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238209
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
    semantic_id="ap_v1.0.0_entry_5__the_solar_system_as_p_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry5TheSolarSystemAsP(SemanticEntry):
    """
    **Source Text** (Lines 9514-9858):
> The Solar System As Personality: Our approach so far has dealt ...
    """
    
    original_text: str = """**Source Text** (Lines 9514-9858):
> The Solar System As Personality: Our approach so far has dealt with purely psychological factors... What has significance, however, is the idea that there is a cycle of linkage... the "higher Moons"...
>
> The first (our physical Moon) links the orbs of Mars and Venus... period of approximately 28 days... The second "Moon" links the orbs of Jupiter and Mercury... period is probably 40 months... The third "Moon" links the orb of Saturn and the photosphere of the Sun... "sun-spot cycle" of 11.2 years.
>
> The fourth "Moon" = 28-year cycle of individual selfhood... repeated three times = 84 years (Uranus cycle).

**Key Term Analysis**:
- **Physical Moon**: `links Mars-Venus` / `28 days` / `feelings, physiology`
- **Second "Moon" (Lucifer?)**: `links Jupiter-Mercury` / `40 months` / `soul growth, financial cycles`
- **Third "Moon" (Isis?)**: `links Saturn-Sun photosphere` / `11.2 years` / `Kundalini, spiritual integration`
- **Fourth "Moon"**: `links Uranus-Sun heart` / `28 years` / `individual selfhood, Temple building`

**English Paraphrase (Primary Language)**:
The Moon = "seventh" factor linking planetary pairs through cycles:

1. **Physical Moon**: Links Mars-Venus (~28 days). Physiology, feelings, sex.
2. **Second "Moon"**: Links Jupiter-Mercury (~40 months). Soul growth, financial cycles.
3. **Third "Moon"**: Links Saturn-Photosphere (~11.2 years). Kundalini, spinal integration.
4. **Fourth "Moon"**: Links Uranus-Sun heart (~28 years). Individual selfhood; 3×28 = 84 years = Uranus cycle = "Temple of Sol-o-Mon."

**Complete Chinese Interpretation (Secondary Language)**:
月亮 = 通过周期连接行星配对的"第七"因素：

1. **物质月亮**：连接火星-金星（约28天）。生理、感受、性。
2. **第二"月亮"**：连接木星-水星（约40个月）。灵魂成长、金融周期。
3. **第三"月亮"**：连接土星-光球层（约11.2年）。昆达里尼、脊柱整合。
4. **第四"月亮"**：连接天王星-太阳心（约28年）。个体自性；3×28 = 84年 = 天王星周期 = "所罗门圣殿"。

**Narrative Snippets**:
- `[ns_aop_185]` `[trigger: higher_moons]` `[factor_trigger: astro_moons_higher AND astro_higher_moons]` `[role: 主干]` Higher Moons: Physical (28d, Mars-Venus); Second (40mo, Jupiter-Mercury); Third (11.2y, Saturn-Sun). → L9725-9768
- `[ns_aop_186]` `[trigger: fourth_moon]` `[factor_trigger: astro_moon_fourth AND astro_84_temple AND astro_three_births]` `[role: 总结]` Fourth Moon: 28-year cycle × 3 = 84 years (Uranus) = Temple of Sol-o-Mon building. → L9803-9811"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 5: The Solar System as Personality - Higher Moons"
    factor_refs: list = ['moons_higher', 'temple_solomon']
    
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
        l1_anchor="ap_v1.0.0_entry_5__the_solar_system_as_p_001_L1",
    )
    version: str = "1.0.0"
