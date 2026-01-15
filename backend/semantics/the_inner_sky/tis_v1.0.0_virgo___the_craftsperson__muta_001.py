"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.104894
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
    semantic_id="tis_v1.0.0_virgo___the_craftsperson__muta_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class VirgoTheCraftspersonMuta(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Mutable Earth | Adaptabl...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Mutable Earth | Adaptable precision | Element |
| Noble Service | Chosen support | Core drive |
| Useful Excellence | Practical mastery | Goal |
| Inner Critic | Guide or punish | Shadow |

#### Source Text

"The Virgin—complete unto oneself, whole, self-contained. Virgo has come to perfect the craft of living: develop skill, serve meaningfully, make things work better. The endpoint is useful excellence—mastery applied to practical needs."

#### English Paraphrase

**Virgo** = **Mutable Earth** sign embodying **refinement, service, and practical mastery**. The Virgin archetype: self-complete, choosing to serve through dedicated craftsmanship.

**Core Drives**:
- **Refine Through Practice**: Learn by doing, improve through repetition
- **Analyze**: Take apart to understand, identify problems, devise solutions
- **Serve**: Not servitude but noble service—"How can I help?"
- **Health**: Maintain wellness through small daily practices

**Virgoan Strengths**:
- **Precision**: Notice details, get things right, catch errors
- **Practicality**: See what actually works (not just theory)
- **Dedication**: Commit to work however long it takes
- **Humility**: Work itself is reward, doing well is satisfaction

**Shadow Manifestations**:
- **Perfectionism**: Nothing ever good enough, paralysis from standards
- **Criticism**: Analytical eye becomes weapon (toward self and others)
- **Fussiness**: Lost in trivial details, micromanaging
- **Anxiety**: Worrying about health, mistakes, things falling apart

**Evolutionary Challenge**:
Learn that "good enough IS good enough"—perfection guides, doesn't punish. Know when to refine and when to release. Highest expression serves with skill and grace, improving life through quiet dedicated craftsmanship.

#### Complete Chinese Interpretation

**处女座**=**变动土象**星座体现**精炼、服务和实用掌握**。处女原型：自我完整、选择通过专注工艺服务。

**核心驱力**：通过实践精炼(边做边学、重复改进)；分析(拆解理解、识别问题、设计方案)；服务(非奴役而是高贵服务——"我能如何帮忙？")；健康(通过小日常实践维护幸福)

**处女优势**：精确(注意细节、做对、捕捉错误)；实用(看到实际工作的-非仅理论)；奉献(无论多久承诺工作)；谦卑(工作本身是奖励、做好是满足)

**阴影显化**：完美主义(无物足够好、标准导致瘫痪)；批评(分析眼成武器-对自己和他人)；挑剔(迷失琐碎细节、微观管理)；焦虑(担心健康、错误、事物崩溃)

**进化挑战**：学习"足够好就是足够好"——完美引导、不惩罚。知道何时精炼何时释放。最高表达以技能和优雅服务、通过安静专注工艺改善生活。

#### Core Points

- Mutable Earth: practical refinement through service
- Archetype: self-complete Virgin choosing to serve
- Resources: precision, practicality, dedication, humility
- Shadow: perfectionism, criticism, fussiness, anxiety
- Challenge: "good enough is good enough"
- East parallel: 处女↔己土阴柔/正印细致 (yin earth precision)

#### Detailed Explanation

Virgo is **Mutable Earth**—adapting practical energy through refinement and service. The Virgin archetype is not asexual but **self-complete**—choosing to serve from fullness rather than lack. Virgo brings precision, humble craftsmanship, and continuous improvement to whatever it touches.

Virgo's resources include **precision, practicality, dedication, and humility**—the eye for improvement, the impulse to fix what's broken, the satisfaction in a job well done.

**Dysfunction** appears as perfectionism (nothing is ever good enough), criticism (seeing only flaws), fussiness (obsessing over details), or anxiety (paralysis before imperfection). The evolutionary challenge is learning that **"good enough is good enough"**—perfection guides but doesn't punish, knowing when to refine and when to release.

#### Narrative Snippets

- `[ns_innersky_virgo_001]` `[trigger: sign_virgo]` `[factor_trigger: astro_sign_virgo AND element_earth]` `[role: 主干]` The Virgin. Not asexual, but self-complete—choosing to serve from fullness, not lack. Virgo brings practical precision, humble craftsmanship, and refinement to whatever it touches. → The Inner Sky Ch.4 #Virgo
- `[ns_innersky_virgo_002]` `[trigger: sign_virgo AND astro_strength]` `[factor_trigger: element_earth]` `[role: 主干依赖]` Virgo's gift is precision and dedication—eye for improvement, impulse to fix what's broken, satisfaction in a job well done. Highest expression: service with skill and grace. → The Inner Sky Ch.4 #Virgo
- `[ns_innersky_virgo_003]` `[trigger: sign_virgo AND astro_shadow]` `[factor_trigger: planet_mercury]` `[role: 条件分支]` Shadow: harsh inner critic attacks self and others (perfectionism), analysis paralysis from impossible standards, anxiety, endless nitpicking that poisons relationships. → The Inner Sky Ch.4 #Virgo
- `[ns_innersky_virgo_004]` `[trigger: sign_virgo AND astro_challenge]` `[factor_trigger: sign_virgo]` `[role: 总结]` Evolutionary challenge: learn 'good enough is good enough'—let perfection guide, not punish. Know when to refine and when to release. → The Inner Sky Ch.4 #Virgo"""
    normalized_text_zh: str = """"""
    subject: str = "Virgo - The Craftsperson (Mutable Earth)"
    factor_refs: list = ['new_candidate', 'sign_virgo', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_virgo___the_craftsperson__muta_001_L1",
    )
    version: str = "1.0.0"
