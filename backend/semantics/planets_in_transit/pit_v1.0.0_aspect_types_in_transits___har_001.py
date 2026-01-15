"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.199988
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
    semantic_id="pit_v1.0.0_aspect_types_in_transits___har_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class AspectTypesInTransitsHar(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Aspect Type | Geometric ...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Aspect Type | Geometric angle | Experiential doorway |
| Conjunction | 0° fusion | Intensity/beginning |
| Square | 90° tension | Crisis/growth |
| 吉凶相位 Parallel | Harmony/conflict | East-West bridge |

#### Source Text

"The aspect formed between transiting and natal planets determines the experiential quality of the transit. Conjunctions (0°) merge energies intensely. Oppositions (180°) create confrontation and awareness. Trines (120°) and sextiles (60°) offer flowing opportunities. Squares (90°) create dynamic tension demanding action. Each aspect type provides a different doorway through which the transit's themes manifest."

#### English Paraphrase (Primary Language)

**Aspect type** determines **how** transit energy manifests—the experiential doorway or channel. The same planetary combination (e.g., Saturn-Sun) produces radically different experiences depending on the aspect formed.

**Major transit aspects**:

**Conjunction (0°)**: Fusion, intensity, beginning. Transiting and natal planets merge, creating maximum intensity and new beginnings. Like two people standing face-to-face, energies blend completely. Often overwhelming but initiatory—something fundamentally new starts. Duration typically longer due to tight orb and retrograde pattern. Example: Transit Saturn conjunct natal Venus = serious relationship commitments, practical love lessons.

**Opposition (180°)**: Confrontation, awareness, projection. Transiting and natal planets stand opposite, forcing conscious awareness. What was internal becomes external—often projects onto others or circumstances. Maximum objectivity but also maximum tension. Like seeing yourself in a mirror held by another. Example: Transit Uranus opposite natal Sun = mid-life crisis, authenticity vs conformity battle externalized.

**Trine (120°)**: Flow, ease, opportunity. Harmonious aspect allowing easy energy exchange. Opportunities come naturally, talents express effortlessly. Can be too easy—lacking motivation for growth if unmet by conscious use. Grace without effort. Example: Transit Jupiter trine natal Mercury = easy communication success, teaching/learning flows.

**Square (90°)**: Tension, crisis, action. Dynamic friction creating pressure to act. Most growth-producing aspect—discomfort forces change. Crisis as opportunity. The "grow or suffer" aspect. Example: Transit Pluto square natal Moon = emotional transformation through crisis, family/security upheaval.

**Sextile (60°)**: Opportunity, cooperation, mild ease. Gentler than trine, requiring some conscious effort. Opportunity knocks but you must answer. Productive harmony with awareness. Example: Transit Neptune sextile natal Venus = creative/spiritual relationship opportunities with conscious cultivation.

**Minor aspects** (semi-square 45°, sesquiquadrate 135°, quincunx 150°) used by some astrologers but Hand focuses on majors for clarity.

**East-West parallel**: Chinese astrology similarly distinguishes **吉凶相位** (auspicious/inauspicious aspects): 三合/六合 (trine/sextile, harmonious), 刑冲 (square/opposition, challenging), with 合 (conjunction) as fusion requiring careful navigation.

#### Complete Chinese Interpretation (Secondary Language)

在行运分析中，同一组行星组合（例如“土星—太阳”），因形成的相位类型不同，其体验质感可以截然相反。**合相**是能量的高度融合与集中，好比两股力量叠加在同一点：既可能带来极大的专注与新开端，也可能因为过度密集而让人感到压迫甚至窒息；**对冲**把两股能量拉到 180° 的对立面上，使之通过外部人物或情境互相映照，典型体验是“被对方逼到墙角被迫看见自己”；**三分**提供的是近乎无阻力的顺流，好事自然而然地发生，却也可能因为太顺而缺乏成长动力；**四分**制造的是尖锐张力，逼迫行动与抉择，是最“痛并成长”的格局；**六合**则像带一点门槛的机会之门——需要你主动伸手接住。

汉德强调，不能简单把相位分成“好/坏”：三分若被完全浪费，就只剩下“轻松却空过”；四分若被有意识地面对，往往成为人生重大突破的关键契机。从东西对比看，这一套体验逻辑与中国占星中对**吉凶相位 / 三合六合 / 刑冲 / 合**的分类高度一致：和谐角度提供顺流与合作的通道，不和谐角度制造冲突与转折，而合相则是最需小心拿捏的高度集中点。真正成熟的运用，是把每一种相位都视为不同类型的“修行门径”。

#### Core Points

- **Conjunction (0°)**: Fusion, intensity, beginning, overwhelming initiation
- **Opposition (180°)**: Confrontation, awareness, projection, externalization
- **Trine (120°)**: Flow, ease, grace, can be too easy lacking motivation
- **Square (90°)**: Tension, crisis, action, maximum growth through friction
- **Sextile (60°)**: Opportunity, mild ease, requires conscious effort
- **Aspect determines how**: Same planets different aspects = different experiences
- **East-West parallel**: Matches 吉凶相位 (auspicious/inauspicious aspects)"""
    normalized_text_zh: str = """"""
    subject: str = "Aspect Types in Transits - Harmonic Qualities"
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
        l1_anchor="pit_v1.0.0_aspect_types_in_transits___har_001_L1",
    )
    version: str = "1.0.0"
