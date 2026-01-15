"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251490
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
    semantic_id="pit_v1.0.0_retrograde_motion__逆行运动_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class RetrogradeMotion逆行运动(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "When a planet appears to move backward (retrograde), it ...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "When a planet appears to move backward (retrograde), it creates a triple-pass pattern: the planet aspects the natal point while moving forward, then again while retrograding, then a third time while resuming direct motion. This repetition forces deeper integration and review of unresolved issues."

**English Paraphrase (Primary Language)**:
**Retrograde motion** is the apparent backward movement of planets as seen from Earth. Due to Earth's orbital perspective, outer planets periodically appear to reverse direction in the zodiac. When a transiting planet is retrograding, it creates a **three-pass pattern**: first pass (forward approach), second pass (retrograde), third pass (forward departure). This triple aspect means the same transit theme is reworked three times over months or years. Hand emphasizes this forces **deeper integration**—you can't ignore the issue after one pass; you must review, reconsider, and integrate more thoroughly. Retrograde transits are often more psychologically intense than direct transits because the repetition prevents superficial resolution.

**Complete Chinese Interpretation (Secondary Language)**:
**逆行运动**是行星从地球视角的表观向后运动。由于地球轨道视角，外行星周期性地在黄道上显现反向运动。当行运行星逆行时，它创造**三次经过模式**：第一次经过（顺行接近）、第二次经过（逆行）、第三次经过（顺行离开）。这个三重相位意味着同一行运主题被重做三次，跨越数月或数年。汉德强调这**迫使更深整合**——你不能在一次经过后忽视问题；你必须回顾、重新考虑并更彻底地整合。逆行行运常常比顺行行运心理强度更大，因为重复防止了表面解决。

**Key Term Analysis**:
- **Retrograde Motion**: `apparent backward` / `Earth perspective` / `cyclical pattern`
- **Triple-Pass Pattern**: `forward-retrograde-forward` / `three exact aspects` / `repetition`
- **Deeper Integration**: `forced review` / `unresolved issues` / `psychological intensity`

**Core Points** (decomposed, no upper limit):
- Retrograde = apparent backward motion from Earth's perspective
- Creates triple-pass pattern (forward-retrograde-forward)
- Same transit aspect occurs three times over months/years
- Each pass reworks the same theme
- Forces deeper integration and review
- Prevents superficial resolution
- Psychologically more intense than direct transits
- Unresolved issues come back for reconsideration

**Detailed Explanation**:
The retrograde cycle is nature's way of ensuring thorough processing. A direct transit might be resolved quickly; a retrograde transit keeps returning to the issue, demanding deeper understanding. Clients often notice that retrograde transits feel cyclical—the issue surfaces, seems to resolve, then resurfaces weeks or months later. This isn't failure; it's the retrograde pattern working as designed. Each pass deepens understanding and integration.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_019]` `[trigger: retrograde_definition]` `[factor_trigger: astro_saturn_identity AND astro_saturn_maturity AND astro_retrograde_motion]` `[role: 主干]` Retrograde motion creates a triple-pass pattern: forward, retrograde, forward. → Source Text
- `[ns_hand_pit_020]` `[trigger: triple_pass]` `[factor_trigger: astro_saturn_partnership AND astro_saturn_resources AND astro_triple_pass_pattern]` `[role: 主干依赖]` The same transit aspect occurs three times, forcing deeper integration. → Source Text
- `[ns_hand_pit_021]` `[trigger: deeper_integration]` `[factor_trigger: astro_saturn_responsibility AND astro_saturn_restriction AND astro_deeper_integration AND astro_cyclical_review]` `[role: 总结]` Retrograde prevents superficial resolution; unresolved issues return for reconsideration. → English Paraphrase

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A: Single authoritative source (Hand's "Planets in Transit" 1976). Retrograde cycles are standard in modern predictive astrology.
- **中文**: 无版本差异：单一权威来源（Hand《行运中的行星》1976）。逆行周期在现代预测占星中是标准的。"""
    normalized_text_zh: str = """"""
    subject: str = "Retrograde Motion (逆行运动)"
    factor_refs: list = ['astro_retrograde_motion', 'astro_triple_pass_pattern', 'astro_deeper_integration', 'astro_cyclical_review']
    
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_retrograde_motion__逆行运动_001_L1",
    )
    version: str = "1.0.0"
