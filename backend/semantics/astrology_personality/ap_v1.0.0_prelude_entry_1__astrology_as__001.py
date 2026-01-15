"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237590
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
    semantic_id="ap_v1.0.0_prelude_entry_1__astrology_as__001",
    book_id="astrology_personality",
    engine_id="astro"
)
class PreludeEntry1AstrologyAs(SemanticEntry):
    """
    **Source Text** (Lines 568-694):
> The history of astrology is the history of the successive transfo...
    """
    
    original_text: str = """**Source Text** (Lines 568-694):
> The history of astrology is the history of the successive transformations of man's attitude to Nature:—external nature, perceived through sense-impressions; and as well, internal or "human" nature, the sum total of those physiological and psychological phenomena which somehow man calls his own; saying, "my" body, "my" soul, "my" mind.
>
> What today is usually called astrology is the result of a particular phase of this relationship between man's conscious ego and Nature. Though this phase may have lasted hundreds and thousands of years, it was preceded by other phases of perhaps greater significance; and the purpose of this book is to show that a new phase is just now beginning...
>
> Astrology is the most significant index to man's practical philosophy of living. Philosophy per se speculates about life and man. But astrology, in every age, characterizes, directly or indirectly, the deepest quality of man's actual response to life...
>
> The astrology which is in vogue today originated almost entirely in the work of the Alexandrian astrologer, Claudius Ptolemy: Tetrabiblos... Ptolemaic astrology is the end-product of the East Mediterranean-Greek culture, and can only be understood in function of the intellectualism of this culture...
>
> If we want to understand the living essence of astrology we must forget Ptolemy and the type of medieval astrology from which present-day astrology is mostly derived, and reach to the earthly vital depths of archaic mankind...
>
> And we claim that any astrology which does not bring to man a message of integration is an adulteration and a perversion of true astrology.

**Key Term Analysis**:
- **History of astrology = history of attitudes to Nature**: `external/internal nature` / `successive transformations` / `man-Nature relationship`
- **Ptolemaic astrology**: `Tetrabiblos` / `Alexandrian intellectualism` / `end-product of Greek culture`
- **Index to practical philosophy**: `not speculation but response` / `deepest quality of living` / `actualized attitude`
- **Message of integration**: `true astrology's keynote` / `versus disintegration` / `all ages' essential purpose`
- **Archaic mankind**: `pre-Ptolemaic` / `vital depths` / `living essence`

**English Paraphrase (Primary Language)**:
Rudhyar establishes his revolutionary historical framework: the history of astrology is identical with the history of human attitudes toward Nature—both external (world) and internal (body, soul, mind). Current astrology represents just one phase in this ongoing transformation, preceded by phases of potentially greater significance. A new phase is now beginning.

Astrology's unique function is as "the most significant index to man's practical philosophy of living." Unlike abstract philosophy which speculates, astrology reveals how humans actually respond to life in each era. It characterizes the deepest quality of lived experience.

Crucially, Rudhyar argues that Ptolemaic astrology (Tetrabiblos)—the foundation of Western astrology—is the late-stage intellectual product of Greco-Roman culture, having lost contact with the living spiritual traditions of Orphic and Pythagorean periods. To understand astrology's living essence, we must go beyond Ptolemy to archaic humanity's vital relationship with cosmos.

The fundamental criterion: any astrology not bringing "a message of integration" is perversion of true astrology. Integration, not prediction, is the authentic keynote.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar建立了其革命性的历史框架：占星学的历史等同于人类对自然态度的历史——包括外在自然（世界）和内在自然（身体、灵魂、心智）。当前的占星学仅代表这一持续转变中的一个阶段，之前存在可能更重要的阶段。新的阶段正在开始。

占星学的独特功能是作为"人类生活实践哲学最重要的指标"。与抽象的哲学思辨不同，占星学揭示人类在每个时代如何实际回应生命。它表征了生活体验的最深层品质。

至关重要的是，Rudhyar认为托勒密占星学（Tetrabiblos）——西方占星学的基础——是希腊-罗马文化晚期的知识产物，已与奥菲斯和毕达哥拉斯时期的活生生精神传统失去联系。要理解占星学的活生生本质，我们必须超越托勒密，回到古代人类与宇宙的生机关系。

根本标准：任何不带来"整合信息"的占星学都是真正占星学的歪曲。整合，而非预测，是真正的基调。

**Core Points**:
- History of astrology = history of human attitudes to Nature
- Both external and internal nature involved
- Current astrology is one phase; new phase beginning
- Astrology = index to practical philosophy (not speculation)
- Ptolemaic astrology = late-stage Greek intellectualism
- Tetrabiblos lost contact with archaic spiritual traditions
- Must recover archaic vitality to understand essence
- True astrology's keynote: integration
- Non-integrative astrology = perversion

**Detailed Explanation**:
This opening establishes Rudhyar's historical methodology and evaluative criterion. He refuses to accept received Western astrology (Ptolemy) as the definitive form, instead positioning it as a historically conditioned product of Greek intellectualism. This move is radical: it frees astrology from having to justify itself in terms of Ptolemaic categories (prediction, essential dignities) and opens space for reconceiving its purpose.

The criterion of "integration" becomes central: astrology either integrates the person or disintegrates them. Fortune-telling that creates fear, dependency, or fragmentation fails this test. Only astrology that helps the person become whole—integrating conscious and unconscious, individual and cosmic—is authentic.

**Narrative Snippets**:
- `[ns_aop_022]` `[trigger: history_definition]` `[factor_trigger: astrology AND astro_historical_evolution]` `[role: 主干]` The history of astrology is the history of successive transformations of man's attitude to Nature—external and internal. → Source Text L568-572
- `[ns_aop_023]` `[trigger: index_philosophy]` `[factor_trigger: astro_practical_philosophy]` `[role: 主干依赖]` Astrology is the most significant index to man's practical philosophy of living—it characterizes the deepest quality of actual response to life. → Source Text L584-587
- `[ns_aop_024]` `[trigger: ptolemy_critique]` `[factor_trigger: astro_ptolemaic AND astro_archaic AND astro_ptolemaic_archaic]` `[role: 条件分支]` Ptolemaic astrology is the end-product of Greek intellectualism, having lost contact with archaic spiritual traditions. → Source Text L657-666
- `[ns_aop_025]` `[trigger: integration_criterion]` `[factor_trigger: astro_authenticity AND accurate_judgment AND astro_integration_criterion]` `[role: 总结]` Any astrology which does not bring a message of integration is an adulteration and perversion of true astrology. → Source Text L693-694

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: Rudhyar's critique of Ptolemy was controversial among traditional astrologers but anticipated later scholarship (Project Hindsight, Hellenistic recovery) which revealed pre-Ptolemaic techniques.
- **中文**: Rudhyar对托勒密的批评在传统占星家中引起争议，但预见了后来的学术研究（Hindsight项目、希腊化复兴），这些研究揭示了托勒密之前的技术。"""
    normalized_text_zh: str = """"""
    subject: str = "Prelude Entry 1: Astrology as Index to Man's Philosophy of Living"
    factor_refs: list = ['astro_practical_index', 'astro_ptolemaic', 'astro_integration_message', 'astro_archaic_mankind']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_prelude_entry_1__astrology_as__001_L1",
    )
    version: str = "1.0.0"
