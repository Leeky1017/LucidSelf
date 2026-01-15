"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.199936
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
    semantic_id="pit_v1.0.0_retrograde_motion___triple_pas_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class RetrogradeMotionTriplePas(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Retrograde | Apparent ba...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Retrograde | Apparent backward motion | Triple pass |
| Triple Pass | Direct-Retro-Direct | Integration cycle |
| Station Point | Direction change | Maximum intensity |
| 反复/伏吟 Parallel | Repetition principle | East-West bridge |

#### Source Text

"When an outer planet turns retrograde, it appears to move backward through the zodiac, creating a triple-pass pattern: the planet crosses a sensitive degree going forward (direct), then backward (retrograde), then forward again (direct). This means any transit from an outer planet to a natal point typically occurs three times over several months to years, allowing progressive integration of the transit's lessons rather than a single overwhelming experience."

#### English Paraphrase (Primary Language)

**Retrograde motion** is an optical illusion caused by Earth's orbit: as we pass a slower outer planet, that planet appears to move backward against the zodiac background. This creates the famous **triple-pass pattern** essential to transit interpretation.

**Three passes**:
1. **First Direct Pass**: Initial encounter with transit energy. Issues emerge, patterns become conscious, first opportunities/challenges appear. Often exciting or surprising—something new is happening.
  
2. **Retrograde Pass**: Review, rework, deepen. The planet moves backward over the same degree, returning to the transit point. This is interior work—processing, integrating, dealing with what emerged during first pass. Often more difficult as internal resistance surfaces.

3. **Final Direct Pass**: Resolution, completion, manifestation. The planet moves forward across the transit point for the last time. By now, the work has been done internally; this pass brings external completion and manifestation of whatever was being developed.

**Why triple passes matter**: Major life changes require time for integration. A single pass would be overwhelming—too much too fast. Three passes over months/years allow gradual adjustment:
- First pass: Awareness awakens
- Second pass (retrograde): Interior work processes  
- Third pass: External manifestation completes

**Station points** (when planet appears motionless before direction change) are maximum intensity—energy concentrated, pressure peaks, breakthroughs or breakdowns most likely.

**Example**: Transit Pluto conjunct natal Sun might span 1-2 years with three exact contacts. First pass introduces ego-death themes. Retrograde pass deepens psychological transformation. Final pass completes the death-rebirth cycle with new identity manifesting.

**East-West parallel**: This resembles Chinese concepts of **反复** (repetition), **伏吟** (hidden recurrence), and **重复应验** (repeated manifestation)—the idea that important destiny patterns must repeat multiple times for full integration.

#### Complete Chinese Interpretation (Secondary Language)

外行星的逆行，让它们在黄道上对同一个度数形成经典的**三次经过模式**：先是顺行第一次精确相位，然后逆行回头再撞一次，最后再度顺行完成第三次接触。汉德认为，正是这三次往返，使得那些涉及深层人格重塑的行运（尤其是土星、天王星、海王、冥王）有机会被**分段消化**，而不是一次性把人压垮。

第一次顺行经过，好比剧情的“开场通知”：相关主题突然浮上海面——某段关系开始摇晃、某个健康信号出现、某种职业不满足开始变得明显，但往往还带着新鲜感或偶然感。逆行回头的第二次经过，则把人推进**内在的审视与再加工**：你被迫反思第一次经过中暴露的问题，旧模式的抗拒、否认和防御会在这段时间集中爆发，也是最容易觉得“反复折腾”的阶段。第三次顺行经过，才是真正的**结果显化与定型**：前两轮累积的心理工作与外在调整，在这一轮变成可见的现实结构——关系是修复了、重组了还是结束了，路径是坚定下来还是被彻底放弃。

这种“顺—逆—顺”的三段式，与中国命理中强调的**反复 / 伏吟 / 重复应验**高度契合：真正重要的命运课题不会只敲一次门，而是以不同角度多次出现，直到被看见、被理解、被整合。理解三次经过模式，有助于当事人在第二次逆行阶段不过度恐慌，而是明白自己正处于“回炉内炼”的必经过程。

#### Core Points

- **Triple-pass pattern**: Direct → Retrograde → Direct (three exact aspects)
- **Gradual integration**: Prevents overwhelming single impact
- **Three stages**: Awareness (1st) → Interior work (2nd) → Manifestation (3rd)
- **Station intensity**: Maximum pressure at direction-change points
- **Time span**: Months to years for outer planet transits
- **Progressive development**: Each pass deepens understanding and integration
- **East-West parallel**: Matches 反复/伏吟 (repetition and hidden recurrence)"""
    normalized_text_zh: str = """"""
    subject: str = "Retrograde Motion - Triple Pass Integration"
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
        l1_anchor="pit_v1.0.0_retrograde_motion___triple_pas_001_L1",
    )
    version: str = "1.0.0"
