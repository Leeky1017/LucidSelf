"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251503
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
    semantic_id="pit_v1.0.0_multiple_pass_pattern__多次经过模式_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class MultiplePassPattern多次经过模式(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "The three passes of a retrograding planet create a progr...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "The three passes of a retrograding planet create a progressive deepening of understanding. Each pass adds layers of meaning and integration. The first pass introduces the theme, the second pass (retrograde) deepens it, the third pass consolidates the learning."

**English Paraphrase (Primary Language)**:
The **multiple pass pattern** describes how the retrograde cycle unfolds in three distinct phases, each with its own psychological character. The **first pass** (forward approach) introduces the transit theme—the issue first surfaces, often unconsciously. The **second pass** (retrograde) deepens the theme—now conscious, the person must engage more directly with the issue. The **third pass** (forward departure) consolidates learning—integration occurs, and the person moves forward with new understanding. This three-phase structure means major outer-planet transits can span 6–12 months or longer, with each phase requiring different psychological work. Hand emphasizes that **gradual adjustment** is the gift of the multiple-pass pattern—you're not forced to transform overnight but given time to integrate change.

**Complete Chinese Interpretation (Secondary Language)**:
**多次经过模式**描述逆行周期如何分三个不同阶段展开，每个阶段有其自己的心理特征。**第一次经过**（顺行接近）引入行运主题——问题首次浮现，常常无意识地。**第二次经过**（逆行）深化主题——现在有意识，人必须更直接地与问题互动。**第三次经过**（顺行离开）巩固学习——整合发生，人以新理解向前迈进。这个三阶段结构意味着主要外行星行运可以跨越6–12个月或更长，每个阶段需要不同的心理工作。汉德强调**逐步调整**是多次经过模式的礼物——你不是被迫一夜间转变，而是被给予时间来整合改变。

**Key Term Analysis**:
- **Multiple Pass Pattern**: `three phases` / `progressive deepening` / `gradual adjustment`
- **First Pass**: `introduces theme` / `unconscious surfacing` / `initial contact`
- **Second Pass**: `deepens engagement` / `conscious confrontation` / `active work`
- **Third Pass**: `consolidates learning` / `integration` / `moving forward`

**Core Points** (decomposed, no upper limit):
- Multiple pass pattern = three distinct phases of retrograde cycle
- First pass: introduces theme, often unconsciously
- Second pass (retrograde): deepens theme, requires conscious engagement
- Third pass: consolidates learning, integration occurs
- Each phase has different psychological character
- Spans 6–12 months or longer for major outer-planet transits
- Allows gradual adjustment to major changes
- Prevents forced overnight transformation
- Gives time for integration and understanding

**Detailed Explanation**:
The multiple-pass pattern is a mercy—it prevents shock and allows integration. Instead of a single overwhelming transit, you get three opportunities to work with the energy. First pass: "Something's shifting." Second pass: "I need to face this directly." Third pass: "I've integrated this; I'm moving forward." This rhythm respects human psychology and the time needed for genuine transformation.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_022]` `[trigger: three_phases]` `[factor_trigger: astro_three_phases AND astro_multiple_pass_pattern AND astro_growth_phase AND astro_consolidation_phase]` `[role: 主干]` The three passes create progressive deepening: first introduces, second deepens, third consolidates. → Source Text
- `[ns_hand_pit_023]` `[trigger: gradual_adjustment]` `[factor_trigger: astro_gradual_adjustment]` `[role: 主干依赖]` Gradual adjustment is the gift—time to integrate rather than forced overnight transformation. → Source Text
- `[ns_hand_pit_024]` `[trigger: integration_rhythm]` `[factor_trigger: astro_integration_rhythm]` `[role: 总结]` Each phase requires different psychological work; the rhythm respects human capacity for change. → English Paraphrase

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A: Single authoritative source (Hand's "Planets in Transit" 1976). The three-phase model is standard in modern transit interpretation.
- **中文**: 无版本差异：单一权威来源（Hand《行运中的行星》1976）。三阶段模型在现代行运解读中是标准的。"""
    normalized_text_zh: str = """"""
    subject: str = "Multiple Pass Pattern (多次经过模式)"
    factor_refs: list = ['astro_multiple_pass_pattern', 'astro_gradual_adjustment', 'astro_integration_rhythm']
    
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
        l1_anchor="pit_v1.0.0_multiple_pass_pattern__多次经过模式_001_L1",
    )
    version: str = "1.0.0"
