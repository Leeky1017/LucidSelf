"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251535
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
    semantic_id="pit_v1.0.0_natal_aspect_modifies_transit__001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NatalAspectModifiesTransit(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "A natal aspect between two planets colors and modifies t...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "A natal aspect between two planets colors and modifies the meaning of a transit between those same planets. For example, if your natal Sun is square Saturn, a transit of Saturn to your Sun will be experienced through the lens of that natal square—the transit trine becomes modified by the natal square's tension."

**English Paraphrase (Primary Language)**:
**Natal aspects modify transits** is a crucial principle: the natal chart provides the **interpretive lens** through which all transits are filtered. If you have natal Sun square Saturn (lifelong tension between ego and limitation), a transit Saturn trine Sun won't feel like pure ease—it will be filtered through your natal square's pattern. The transit trine brings opportunity and ease, but your natal square means you'll approach it with caution, skepticism, or self-doubt. Conversely, if you have natal Sun trine Saturn (natural ease with structure), a transit Saturn square Sun will be less harsh because you have built-in structural competence. Hand emphasizes this **natal context principle**: every transit is interpreted through the natal chart's existing patterns. The natal chart is the **permanent filter**; transits are the **temporary catalyst**. Together they create the actual experience.

**Complete Chinese Interpretation (Secondary Language)**:
**本命相位修改行运**是一个关键原则：本命盘提供了所有行运被过滤的**解读透镜**。如果你有本命太阳刑土星（小我与限制之间的终身张力），一个行运土星拱太阳不会感觉像纯粹的轻松——它会被你本命相位的模式过滤。行运拱相带来机遇和轻松，但你的本命刑相意味着你会以谨慎、怀疑或自我怀疑的态度接近它。反之，如果你有本命太阳拱土星（与结构的自然轻松），一个行运土星四分太阳会不那么严厉，因为你有内置的结构能力。汉德强调这个**本命语境原则**：每个行运都通过本命盘的既有模式来解读。本命盘是**永久过滤器**；行运是**临时催化剂**。一起它们创造实际体验。

**Key Term Analysis**:
- **Natal Aspect**: `permanent pattern` / `lifelong theme` / `interpretive lens`
- **Transit Aspect**: `temporary catalyst` / `current activation` / `filtered by natal`
- **Modification**: `natal colors transit` / `context shapes meaning` / `lens effect`

**Core Points** (decomposed, no upper limit):
- Natal aspect between two planets modifies transit between same planets
- Natal chart provides interpretive lens
- Transit is filtered through natal pattern
- Natal aspect is permanent; transit is temporary
- Example: natal Sun-Saturn square modifies transit Saturn-Sun aspects
- Natal trine Saturn makes transit Saturn-square less harsh
- Natal square Saturn makes transit Saturn-trine less easy
- Natal context principle: all transits filtered through natal chart
- Together natal + transit create actual experience

**Detailed Explanation**:
This principle explains why the same transit affects different people differently. A Saturn transit to Sun is challenging for everyone, but someone with natal Sun-Saturn square has already learned to work with that tension; someone with natal Sun-Saturn trine must learn it fresh. The natal chart is your psychological baseline; transits activate and modify that baseline.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_028]` `[trigger: natal_modifies]` `[factor_trigger: astro_natal_modifies_transit AND astro_natal_aspect]` `[role: 主干]` Natal aspect modifies transit meaning—natal chart provides the interpretive lens. → Source Text
- `[ns_hand_pit_029]` `[trigger: natal_context]` `[factor_trigger: astro_natal_context_principle]` `[role: 主干依赖]` Natal chart is permanent filter; transits are temporary catalyst. → Source Text
- `[ns_hand_pit_030]` `[trigger: actual_experience]` `[factor_trigger: astro_actual_experience]` `[role: 总结]` Natal + transit together create actual experience—not transit alone. → English Paraphrase

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A: Single authoritative source (Hand's "Planets in Transit" 1976). The natal context principle is fundamental to accurate transit interpretation.
- **中文**: 无版本差异：单一权威来源（Hand《行运中的行星》1976）。本命语境原则是准确行运解读的基础。"""
    normalized_text_zh: str = """"""
    subject: str = "Natal Aspect Modifies Transit (本命相位修改行运)"
    factor_refs: list = ['astro_natal_aspect', 'astro_natal_context_principle', 'astro_interpretive_lens', 'astro_actual_experience']
    
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
        l1_anchor="pit_v1.0.0_natal_aspect_modifies_transit__001_L1",
    )
    version: str = "1.0.0"
