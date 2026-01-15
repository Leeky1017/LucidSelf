"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.088949
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
    semantic_id="bot_v1.0.0_princess_of_wands__权杖公主_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class PrincessOfWands权杖公主(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Earth of Fire | Fire's fuel | Combustion source |
| Chemical Attraction | Irresistible bond | Fire's material |
| Nude Figure | Freedom to combine | Pure reactivity |
| Daring Passion | Vigorous beauty | Creative force |

**Title**: The Princess of the Shining Flame (闪耀火焰的公主)
**Elemental**: The Earthy part of Fire (火中之土)
**Rule**: Quadrant around North Pole (北极周围象限)

**Source Text**:
> "The Princess of Wands represents the earthy part of Fire; one might say, she is the fuel of Fire. ... irresistible chemical attraction of the combustible substance. ... She is unclothed... chemical action can only take place when the element is perfectly free... She is brilliant and daring. She creates her own beauty by her essential vigour... In anger or love she is sudden, violent, and implacable."

**English Paraphrase**:
**Fuel of Fire** - Represents the **Earthy part of Fire** (Fuel/Combustion). She is the **irresistible chemical attraction** that allows fire to burn. Depicted nude (freedom to combine) with plumes of justice like flames. Qualities: **Brilliance, daring, vigour**. She creates beauty through sheer energy. In love or anger, she is sudden, violent, and implacable. She represents the **materialization of fire**—enthusiasm, ambition, and the power to consume.

**Core**: **Daring Passion** - Vitality, sexual/chemical attraction, enthusiasm, ambition, suddenness, materialization of will.

**Chinese Explanation**:
**权杖公主**代表**火中之土**（火的燃料）。她是可燃物质的**不可抗拒的化学吸引力**。她裸体（为了自由结合），戴着像火焰一样的正义羽毛。品质：**辉煌、大胆、活力**。她通过本质的活力创造自己的美。在爱或愤怒中，她是突然、猛烈且无法平息的。她代表火的**物质化**——热情、野心以及吞噬的力量。

**In Readings**: Enthusiasm, daring, sexual attraction, ambition, sudden news, violent reaction, fearlessness.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Princess of Wands represents Earth of Fire (fuel/combustion). Nude figure shows freedom for chemical reaction. Irresistible attraction enables fire. In love or anger: sudden, violent, implacable.
- **中文**: Crowley的权杖公主代表火中之土（燃料/燃烧）。裸体人物显示化学反应的自由。不可抗拒的吸引力使火成为可能。在爱或怒中：突然、猛烈、无法平息。

**Narrative Snippets**:
- `[ns_thoth_wands_040]` `[trigger: princess_wands_thoth]` `[factor_trigger: thoth_wands_princess]` `[role: 主干]` Princess of Wands = Earth of Fire—fuel of Fire; irresistible chemical attraction of combustible. → Core
- `[ns_thoth_wands_041]` `[trigger: nude_freedom]` `[factor_trigger: thoth_wands_princess AND symbol_nude]` `[role: 条件分支]` Nude figure—chemical action requires element perfectly free; plumes of justice like flames. → Visual
- `[ns_thoth_wands_042]` `[trigger: sudden_violent]` `[factor_trigger: thoth_wands_princess AND state_passion]` `[role: 条件分支]` In anger or love: sudden, violent, implacable—creates beauty by essential vigour. → Character"""
    normalized_text_zh: str = """"""
    subject: str = "Princess of Wands (权杖公主)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_princess_wands_earth', 'earth_of_fire', 'rel_princess_wands_passion', 'chemical_force', 'princess_wands_fuel']
    
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_princess_of_wands__权杖公主_001_L1",
    )
    version: str = "1.0.0"
