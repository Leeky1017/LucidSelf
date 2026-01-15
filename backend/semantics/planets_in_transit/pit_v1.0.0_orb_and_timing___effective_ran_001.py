"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.199954
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
    semantic_id="pit_v1.0.0_orb_and_timing___effective_ran_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class OrbAndTimingEffectiveRan(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Orb | Degree range effec...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Orb | Degree range effective | Timing parameter |
| Outer Planet Orb | 1-3° tight | Long focused |
| Inner Planet Orb | 5-8° wide | Brief light |
| 应期 Parallel | Response period | East-West bridge |

#### Source Text

"The orb is the range of degrees before and after an exact aspect where the transit's effects are felt. Outer planets typically use tighter orbs (1-3°) due to their slow motion and concentrated impact. Inner planets use wider orbs (5-8°) due to faster motion and lighter impact. The orb determines the duration of the transit's influence—how long before exact aspect you feel it approaching, and how long after exact aspect it continues to fade."

#### English Paraphrase (Primary Language)

**Orb** is the crucial timing parameter determining when a transit becomes effective and how long it lasts. An aspect isn't binary (on/off) but gradual—the transit's influence **builds** as the planets approach exactitude, peaks at exact aspect, then **fades** as they separate.

**Orb sizes by planet speed**:
- **Outer planets** (Saturn, Uranus, Neptune, Pluto): **1-3° orb**. Slow motion means tight, focused impact. A 2° orb for Pluto transit might span 6-12 months.
- **Middle planets** (Jupiter, Mars): **3-5° orb**. Moderate speed, moderate impact duration.
- **Inner planets** (Sun, Mercury, Venus): **5-8° orb** for transit analysis (wider for natal). Fast motion means lighter, briefer impact.

**Why orb matters for timing**:
- **Approaching orb**: First feelings of transit emerge. Issues begin surfacing. Often unconscious—just vague pressure or emerging themes.
- **Exact aspect** (0° orb): Peak intensity. Maximum pressure or opportunity. Events most likely to manifest. Psychological peak.
- **Separating orb**: Effects fade. Integration begins. External intensity lessens, internal processing continues.

**Duration examples**:
- Transiting Pluto square natal Sun (2° orb): 1-2 years total duration with three exact passes (retrograde pattern)
- Transiting Jupiter trine natal Venus (3° orb): 2-4 weeks total duration  
- Transiting Mars conjunct natal Mercury (4° orb): 1-2 weeks total duration

**Tighter orbs for precision**: Professional astrologers often use tighter orbs (1° for outer planets, 2° for inner) for prediction precision. Wider orbs capture the full psychological atmosphere but make timing vague.

**East-West parallel**: This resembles Chinese **应期** (response period) and **运程时间窗** (fortune timing window) concepts—the distinction between effective period (orb) and exact timing (0° aspect).

#### Complete Chinese Interpretation (Secondary Language)

“容许度”（orb）是行运时间技术的关键参数，它定义了一个相位在**精确命中之前多久开始生效、在精确命中之后多久才真正消退**。汉德反对把相位理解成简单的“开/关开关”：现实中，行星接近精确度数时，其象征能量会逐步增强；在 0° 精确相位时达到峰值；随后又在分离过程中缓慢减弱。因此，对外行星而言，通常只给 1–3° 的紧密容许度，以确保整段高压期既集中又可被识别；对内行星则容许 5–8° 的宽度，因为它们运行很快，若容许度过窄，几乎捕捉不到任何体验感。

从时间感受上看，容许度让我们能区分“**应期**”与“**时间窗**”：前者类似一个较宽的、持续数周到数年的影响带，后者则是精确相位附近那几天甚至几小时的强烈聚焦。占星师在判断时，既要用较宽的容许度把握心理与事件的整体背景，又要用较紧的容许度标记关键节点（例如签约、分手、事故、顿悟等具体事件）。

在东西方对照中，可以把外行星 1–3° 的紧密容许度视作“应期”的核心区间，而内行星较宽的容许度则像是围绕这一核心反复触发的“运程时间窗”。理解并精细运用 orb，使预测工作从粗糙的年份级别压缩到更可操作的月/周/日尺度。

#### Core Points

- **Orb**: Degree range before/after exact aspect where transit effective
- **Outer planets**: 1-3° tight orb (focused, long duration)
- **Inner planets**: 5-8° wide orb (light, brief duration)
- **Three phases**: Approaching (building) → Exact (peak) → Separating (fading)
- **Duration determination**: Orb size × planet speed = total transit time
- **Timing precision**: Tighter orbs improve prediction accuracy
- **East-West parallel**: Matches 应期/时间窗 (response period/timing window)"""
    normalized_text_zh: str = """"""
    subject: str = "Orb and Timing - Effective Range"
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
        l1_anchor="pit_v1.0.0_orb_and_timing___effective_ran_001_L1",
    )
    version: str = "1.0.0"
