"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147310
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
    semantic_id="ca_v1.0.0_aspects_and_perfection___tempo_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class AspectsAndPerfectionTempo(SemanticEntry):
    """
    #### Source Text

"Aspects are certaine Distances of Degrees, wherein the Planets mutually behold ea...
    """
    
    original_text: str = """#### Source Text

"Aspects are certaine Distances of Degrees, wherein the Planets mutually behold each other, and worke more powerfully: and are either Major or Minor. The Major are five: Conjunction, Sextile, Square, Trine, Opposition. When a significator applies to another by Aspect, and both be in Degrees wherein they shall come to a perfect Aspect before either of them be impedited or turned Retrograde, we say the Aspect perfects, and the thing shall come to passe. But if ere the Aspect be compleat, one of them turn Retrograde, or be combust, or enter another Signe wherein he hath no Aspect with the former Planet, then is the Aspect frustrated, and the thing comes not to effect."

#### Key Term Analysis

- **Mutually behold**: Planets in aspect "see" each other; no aspect = no connection/awareness
- **Perfects**: An applying aspect reaching exact completion; indicates the matter will succeed
- **Impedited**: Hindered or blocked; includes combust, retrograde, besieged by malefics
- **Frustrated**: Aspect cannot complete due to impediment; matter fails or dissolves

#### English Paraphrase (Primary Language)

**Aspects** are the **angular relationships** between planets that determine whether and how matters complete. In horary, aspects are the **primary mechanism** showing outcome—they're not static descriptions but **temporal processes** revealing if/when things manifest.

**The five major aspects**:

**1. Conjunction (0°)** - 合相:
- **Meaning**: Union, merging, beginning, intensity
- **Horary use**: Querent and quesited coming together, matter completes through direct meeting
- **Example**: Querent's ruler conjuncts 7th ruler → marriage/partnership forms

**2. Sextile (60°)** - 六分相:
- **Meaning**: Opportunity, cooperation, mild harmony
- **Horary use**: Favorable outcome with some effort required
- **Example**: Querent's ruler sextiles 2nd ruler → money comes through opportunity you must take

**3. Square (90°)** - 四分相:
- **Meaning**: Tension, obstacle, friction, crisis
- **Horary use**: Matter succeeds but with difficulty, conflict, stress
- **Example**: Querent's ruler squares 10th ruler → get job but with workplace tension

**4. Trine (120°)** - 三分相:
- **Meaning**: Harmony, ease, flow, grace
- **Horary use**: Favorable outcome, easy success, natural completion
- **Example**: Querent's ruler trines 7th ruler → relationship flows naturally

**5. Opposition (180°)** - 对分相:
- **Meaning**: Confrontation, awareness, separation yet connection
- **Horary use**: Matter completes but with opposition, conflict, or open acknowledgment
- **Example**: Querent's ruler opposes enemy significator → lawsuit resolves through confrontation

**Applying vs Separating** (入相vs出相):
- **Applying**: Faster planet moving toward slower, aspect not yet exact → **Future event, YES**
- **Separating**: Faster planet past exact aspect, moving away → **Past event, NO, already happened**
- **Exact/Partile**: Within 1° of perfection → **Imminent, powerful, certain**

**Perfection** (完成): When applying aspect reaches exactitude without impediment:
- **Conditions for perfection**:
  - Both planets continue forward motion (not turning retrograde)
  - Neither planet changes sign before aspect completes (breaks connection)
  - Neither planet combusted by Sun (within ~8°, overwhelmed)
  - Neither planet enters malefic aspect (Mars/Saturn) blocking completion

**Frustration** (阻挫): When aspect cannot perfect:
- **Retrograde**: Planet turns backward before aspect exact → delays, reversal, won't complete as expected
- **Sign change**: Planet enters new sign breaking aspect → connection lost, matter dissolves
- **Combustion**: Planet too close to Sun, weakened → matter overwhelmed by authority/ego
- **Prohibition**: Mars/Saturn aspect intervenes → obstacle blocks completion

**Timing from aspects**: Degrees between planets = time units:
- **Cardinal signs** (Aries, Cancer, Libra, Capricorn): Days or weeks
- **Fixed signs** (Taurus, Leo, Scorpio, Aquarius): Months or years
- **Mutable signs** (Gemini, Virgo, Sagittarius, Pisces): Weeks or months

**Example**: "Will I get the money owed?"
- Querent's ruler (you) at 10° Gemini
- 2nd ruler (money) at 25° Gemini
- **15° apart** in mutable sign → ~15 weeks or months
- **Applying** (you moving toward money) → YES, you'll recover it
- If 2nd ruler were at 5° Gemini (behind you) → **Separating**, already lost opportunity

#### Complete Chinese Interpretation (Secondary Language)

**相位**(Aspects)是行星角度关系决定事项是否/如何完成。**入相**(Applying，向精确相位移动)=未来事件/是，征象星正在接近完成。**出相**(Separating，离开精确相位)=过去事件/否，机会已过。**完成**(Perfection)需要无阻碍：无行星介入(prohibition)、无逆行、无出界。**度数差=时间单位**：两征象星相距度数=事件发生时间(语境决定是日/周/月/年)。**五个古典相位**：合相(0°)最强、六合(60°)温和吉、刑(90°)困难凶、拱(120°)和谐吉、冲(180°)对抗凶。**阻碍**：禁止(更快行星在之前截取)、挫败(第三行星介入)、逆行(征象星退回)、燃烧(太近太阳失效)。判断完成只看入相相位，出相相位显示已经发生的事。东西对照：入相/出相 ↔ 六爻的动爻/变爻机制。

#### Core Points

- **Five major aspects**: Conjunction/sextile/square/trine/opposition with different meanings
- **Applying = YES**: Faster planet moving toward slower, future event
- **Separating = NO**: Past exact aspect, opportunity already gone
- **Perfection**: Aspect completes without impediment = matter succeeds
- **Frustration**: Retrograde, sign change, combustion, prohibition = fails
- **Timing**: Degrees between planets = time units (context determines scale)
- **Temporal mechanism**: Aspects show process not static state

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Lilly's aspect doctrine combines Ptolemaic geometry with Arabic timing techniques. The "perfection" concept (applying aspect reaching exactitude) is central to horary judgment. "Frustration" and "prohibition" derive from Masha'allah and Sahl. Modern astrologers sometimes add minor aspects (semi-sextile, quincunx) which Lilly rarely used.
- **中文**: Lilly的相位学说结合了托勒密几何学和阿拉伯时间技术。"完成"概念（入相相位达到精确）是占星判断的核心。"挫败"和"禁止"源自Masha'allah和Sahl。现代占星师有时添加次要相位（半六合、梅花相），Lilly很少使用。

**Narrative Snippets**:
- `[ns_lilly_asp_001]` `[trigger: aspects_behold]` `[factor_trigger: astro_aspect AND astro_distance AND astro_planetary_relationship]` `[role: 主干]` Aspects are certaine Distances of Degrees, wherein the Planets mutually behold each other, and worke more powerfully. → Source Text
- `[ns_lilly_asp_002]` `[trigger: aspect_perfects]` `[factor_trigger: astro_aspect AND astro_perfection]` `[role: 主干依赖]` When a significator applies to another by Aspect, and both continue to perfect the Aspect before impediment, the thing shall come to passe. → Source Text
- `[ns_lilly_asp_003]` `[trigger: frustration]` `[factor_trigger: astro_frustration AND astro_impediment]` `[role: 条件分支]` If ere the Aspect be compleat, one turn Retrograde or be combust, then is the Aspect frustrated, and the thing comes not to effect. → Source Text
- `[ns_lilly_asp_004]` `[trigger: applying_separating]` `[factor_trigger: astro_applying AND astro_separating AND astro_yes_no_judgment]` `[role: 总结]` Applying = future event, YES indicator; Separating = past event, already happened. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Aspects and Perfection - Temporal-Causal Mechanism"
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_aspects_and_perfection___tempo_001_L1",
    )
    version: str = "1.0.0"
