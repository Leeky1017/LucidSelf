"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238180
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
    semantic_id="ap_v1.0.0_entry_2__planets_of_the_consci_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2PlanetsOfTheConsci(SemanticEntry):
    """
    **Source Text** (Lines 8884-9028):
> Saturn-Moon: Saturn, in Greek mythology, is the ruler of the Go...
    """
    
    original_text: str = """**Source Text** (Lines 8884-9028):
> Saturn-Moon: Saturn, in Greek mythology, is the ruler of the Golden Age... It refers to the first process whereby the universal life-force becomes differentiated, limited, particularized as a living cell... Psychologically speaking, Saturn symbolizes, therefore, that process which leads to the realization: "I am."...
>
> Jupiter-Mercury: Jupiter is the function of compensation in all its possible aspects... Jupiter is thus the power in us of right action, the voice of our true Destiny...
>
> Mars-Venus: Mars "shows the tendency of the life in expressing itself, moving from itself outward without particular regard for external conditions"... Venus is the end of the experience and what we have gathered as a result of it.

**Key Term Analysis**:
- **Saturn-Moon pair**: `Saturn = ego boundary "I am"` / `Moon = psychic energy within Saturn boundaries`
- **Jupiter-Mercury pair**: `Jupiter = compensation, destiny, soul` / `Mercury = intelligence, vehicle of soul`
- **Mars-Venus pair**: `Mars = centrifugal, outgoing libido` / `Venus = centripetal, returning wisdom`
- **Three operations**: `being (Saturn-Moon)` / `maintaining (Jupiter-Mercury)` / `reproducing (Mars-Venus)`

**English Paraphrase (Primary Language)**:
Three pairs of conscious planets, each active-reactive:
1. **Saturn-Moon**: Being. Saturn = ego boundary ("I am"); Moon = psychic energy within.
2. **Jupiter-Mercury**: Maintaining. Jupiter = compensation, destiny, soul; Mercury = intelligence, vehicle.
3. **Mars-Venus**: Reproducing. Mars = centrifugal outgoing; Venus = centripetal returning wisdom.

"Every living entity must first BE (Saturn); then MAINTAIN itself (Jupiter); finally REPRODUCE itself (Mars)."

**Complete Chinese Interpretation (Secondary Language)**:
三对意识行星，各有主动-反应：
1. **土星-月亮**：存在。土星 = 自我边界（"我是"）；月亮 = 内在心理能量。
2. **木星-水星**：维持。木星 = 补偿、命运、灵魂；水星 = 智力、载体。
3. **火星-金星**：繁殖。火星 = 离心外向；金星 = 向心返回的智慧。

"每个活的实体必须首先存在（土星）；然后维持自己（木星）；最后繁殖自己（火星）。"

**Narrative Snippets**:
- `[ns_aop_177]` `[trigger: saturn_moon]` `[factor_trigger: astro_pair_saturn_moon]` `[role: 主干]` Saturn-Moon: Being. Saturn = ego "I am"; Moon = psychic energy within. → L8909-8932
- `[ns_aop_178]` `[trigger: jupiter_mercury]` `[factor_trigger: astro_pair_jupiter_mercury AND astro_jupiter_mercury]` `[role: 主干]` Jupiter-Mercury: Maintaining. Jupiter = compensation/destiny; Mercury = intelligence. → L8934-8987
- `[ns_aop_179]` `[trigger: mars_venus]` `[factor_trigger: astro_pair_mars_venus AND astro_mars_venus]` `[role: 主干]` Mars-Venus: Reproducing. Mars = outgoing; Venus = returning wisdom. → L8996-9028"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: Planets of the Conscious (Saturn-Moon, Jupiter-Mercury, Mars-Venus)"
    factor_refs: list = ['pair_saturn_moon', 'pair_jupiter_mercury', 'pair_mars_venus']
    
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
        l1_anchor="ap_v1.0.0_entry_2__planets_of_the_consci_001_L1",
    )
    version: str = "1.0.0"
