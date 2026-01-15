"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439771
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
    semantic_id="dvd_v1.0.0_audience_观众_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Audience观众(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: Your performance in life and how others perceive you.

**Dre...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: Your performance in life and how others perceive you.

**Dreams - Positive**: If you dream of standing in front of an audience and you are bold and confident, this could indicate a healing dream—you have risen up. Perhaps you were never confident before; such a dream indicates you have overcome this fear.

**Dreams - Negative**: If you are "playing" to an audience, you are putting on a performance. Example: Lady dreaming of audience waiting for show, but kept changing outfits—none suitable. Interpretation: concentrating on externals to get acceptance, putting on "show" to avoid rejection.

**Visions - Positive**: Vision of standing in front of audience preaching = Lord calling you to stand up and minister His word.

**Visions - Negative**: Person striving in front of audience putting on "show" = more interested in pleasing crowds than promoting Lord and truth.

### English Paraphrase

Audience = performance in life, how others perceive you. **Positive**: Bold/confident before audience = healing dream, overcoming fear, risen up. In vision, preaching to audience = call to minister. **Negative**: "Playing" to audience = putting on performance, people-pleasing. Striving for acceptance through externals rather than being authentic. More interested in crowd approval than truth.

### Chinese Interpretation（完整对等诠释）

观众 = 生活中的表现，他人如何看待你。**正面**：在观众面前勇敢/自信 = 医治的梦，克服恐惧，兴起。在异象中，向观众讲道 = 传道的呼召。**负面**：向观众「表演」= 做戏，讨好人。通过外在追求认可而非真实。对群众认可的兴趣大于真理。

### Narrative Snippets

- `[ns_dav_a060]` `[trigger: 梦观众]` `[factor_trigger: dream_symbol_audience]` `[role: 主干]` Audience = performance and perception—confident = healing, performing = people-pleasing. → Dreams Dictionary #Audience
- `[ns_dav_a061]` `[trigger: 观众正面]` `[factor_trigger: dream_symbol_audience AND performance_state]` `[role: 条件分支]` Bold/confident before audience = healing dream, fear overcome, call to minister. → Dreams Dictionary #Audience
- `[ns_dav_a062]` `[trigger: 观众负面]` `[factor_trigger: dream_symbol_audience AND performance_state]` `[role: 条件分支]` "Playing" to audience = putting on show, seeking approval through externals. → Dreams Dictionary #Audience"""
    normalized_text_zh: str = """"""
    subject: str = "Audience 观众"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_audience_观众_001_L1",
    )
    version: str = "1.0.0"
