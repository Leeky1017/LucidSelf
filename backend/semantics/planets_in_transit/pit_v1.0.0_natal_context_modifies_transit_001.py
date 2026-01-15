"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.199972
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
    semantic_id="pit_v1.0.0_natal_context_modifies_transit_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NatalContextModifiesTransit(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Natal Context | Foundati...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Natal Context | Foundation pattern | King principle |
| Transit Activation | Triggers natal | Temporary |
| Aspect Modification | Natal colors transit | Filtering |
| 命局底色 Parallel | Chart foundation | East-West bridge |

#### Source Text

"A natal aspect between two planets colors how transits between those same planets are experienced. For example, if you have natal Sun square Saturn (lifelong authority/discipline issues), then when transiting Saturn trines your Sun (theoretically harmonious), the natal square modifies the transit. The transit trine may bring opportunities related to authority and structure, but the underlying natal square tension remains—you might experience constructive discipline rather than easy fortune."

#### English Paraphrase (Primary Language)

**Natal context is king**: This is one of Hand's most important principles. A transit doesn't operate in vacuum—it activates and is filtered through the natal pattern. The natal chart is the **permanent foundation**; transits are **temporary activations** of that foundation.

**How modification works**:
- **Natal harmony + transit challenge**: Natal Sun trine Saturn (natural discipline) + transit Saturn square Sun = challenge handled with natural competence
- **Natal challenge + transit harmony**: Natal Sun square Saturn (authority conflict) + transit Saturn trine Sun = opportunity appears but with underlying tension
- **Natal challenge + transit challenge**: Natal Sun square Saturn + transit Saturn square Sun = double difficulty, crisis likely
- **Natal harmony + transit harmony**: Natal Sun trine Saturn + transit Saturn trine Sun = flowing opportunity, easy progress

**Why this matters**: Beginning astrologers often read transits in isolation—"Saturn trine Sun is good, square is bad." But the natal pattern is far more powerful than the transit aspect. Someone with natal Sun conjunct Saturn might experience a Saturn square transit as constructive (familiar energy) while someone with natal Sun opposite Saturn might experience a Saturn trine transit as threatening (unfamiliar ease creating suspicion).

**The natal pattern doesn't change**: This is crucial. If you have natal Sun square Saturn, you always have authority/discipline challenges—that's who you are. Transits don't fix or remove natal patterns; they **activate** them at different intensity levels and through different experiential doors.

**Practical application**: When interpreting transits, always check:
1. What's the natal pattern between these two planets?
2. How does the person typically experience this pattern?
3. The transit aspect provides the door/opportunity, but the natal aspect provides the experience quality

**East-West parallel**: This perfectly parallels the Chinese concept of **命局底色决定流运表现** (natal chart foundation determines transit manifestation)—the permanent birth chart is destiny's foundation; annual/monthly transits are temporary activations filtered through that foundation.

#### Complete Chinese Interpretation (Secondary Language)

汉德在这里提出一个贯穿全书的原则：**本命模式永远比行运相位更“重”**。行运只是“什么时候按下这一键”的机制，但被按下的键、会发出怎样的音色，完全由本命盘预先决定。举例来说：如果一个人的本命太阳与土星是和谐三分相，他对“结构、权威、纪律”的能量整体是熟悉且正向的，那么即便遇到土星对太阳的挑战性四分行运，也更可能以“辛苦但有建设性的承担”来体验；反之，若本命就是困难的太阳刑土星，即便后来来的是看似吉利的土星三分太阳行运，底层的不安全感和与权威的紧张也不会凭空消失。

因此，所有行运解读都必须放在**本命上下文**中理解：行运只是在不同时间为同一模式提供不同的“入口角度”（吉相位的门、凶相位的门），但进入之后你所遇见的房间，仍然是你命局里那间熟悉的房间。命局没有写下的东西，行运不会凭空制造；命局反复强调的课题，则会被不同时序的行运一再点亮。这与中国命理“**命局底色决定流运表现**”的判断方式完全平行：先看命局是何种格局、何种用神，再看大运流年如何“引动”这些潜势。

#### Core Points

- **Natal context is king**: Natal pattern more powerful than transit aspect
- **Transits activate natal**: Don't create new patterns, activate existing
- **Aspect modification**: Transit harmony/challenge filtered through natal harmony/challenge
- **Pattern permanence**: Natal doesn't change, only activates at different levels
- **Quality determination**: Natal provides experience quality, transit provides timing
- **Practical method**: Always check natal pattern first before transit interpretation
- **East-West parallel**: Matches 命局底色决定流运表现 (chart foundation determines transit)"""
    normalized_text_zh: str = """"""
    subject: str = "Natal Context Modifies Transit - Pattern Layering"
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_natal_context_modifies_transit_001_L1",
    )
    version: str = "1.0.0"
