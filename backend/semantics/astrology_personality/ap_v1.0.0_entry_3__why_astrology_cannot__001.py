"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237722
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
    semantic_id="ap_v1.0.0_entry_3__why_astrology_cannot__001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry3WhyAstrologyCannot(SemanticEntry):
    """
    **Source Text** (Lines 1765-1837):
> Scientific induction is the basic postulate of exact sciences.....
    """
    
    original_text: str = """**Source Text** (Lines 1765-1837):
> Scientific induction is the basic postulate of exact sciences... "it must yield the result that a correlation which has been found true in a number of cases, and has never been found false, has at least a certain assignable degree of probability of being always true." This definition is of great importance to us, for who, among astrologers, will claim that any astrological correlation "has never been found false"?
>
> Even if planetary "rays" were discovered... Why should the first house represent matters affecting self; the second house, finances; the seventh house, marriage? Why should zodiacal signs be related to certain parts of the body? Why should certain planets "rule" certain signs? How could "progressions" be "scientifically" explained?
>
> Whatever science may discover concerning cosmic radiations, we do not believe that the philosophy of astrology can or should ever be the same as that of an empirical science.

**Key Term Analysis**:
- **Scientific induction**: `correlations never found false` / `Russell's criterion` / `astrology fails`
- **Ray insufficiency**: `wouldn't explain house meanings` / `wouldn't explain rulerships` / `wouldn't explain progressions`
- **Horary-natal unity**: `natal = special case of horary` / `Marc Jones` / `"How is my life problem solved?"`

**English Paraphrase (Primary Language)**:
Rudhyar demonstrates why astrology cannot be empirical science: (1) scientific induction requires correlations "never found false"—no astrological correlation meets this; (2) even if planetary rays existed, they couldn't explain house meanings, sign-body correlations, rulerships, or progressions; (3) horary astrology shows the framework is about meaning, not physical causation.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar论证占星学为何不能成为经验科学：(1)科学归纳要求关联"从未被证伪"——没有占星关联符合这一标准；(2)即使存在行星射线，也无法解释宫位含义、星座-身体对应、守护关系或推运；(3)时辰占星学表明这一框架关乎意义而非物理因果。

**Core Points**:
- Scientific induction requires "never found false"—astrology fails this
- Planetary rays wouldn't explain astrological structure
- House meanings, rulerships, progressions remain "mysteries"
- Natal astrology = special case of horary (Marc Jones)
- Astrology's philosophy ≠ empirical science philosophy

**Narrative Snippets**:
- `[ns_aop_065]` `[trigger: induction_fail]` `[factor_trigger: induction AND astro_induct_struct]` `[role: 主干]` Scientific induction requires "never found false"—no astrological correlation meets this. → L1776-1783
- `[ns_aop_066]` `[trigger: ray_insufficiency]` `[factor_trigger: rays AND structure AND astro_ray_func]` `[role: 主干依赖]` Even rays can't explain house meanings, rulerships, progressions. → L1809-1817
- `[ns_aop_067]` `[trigger: horary_natal]` `[factor_trigger: astro_horary]` `[role: 条件分支]` Natal = special case of horary—meaning-based, not causal. → L1821-1828
- `[ns_aop_068]` `[trigger: diff_philosophy]` `[factor_trigger: astro_philosophy AND astro_non_emp]` `[role: 总结]` Astrology's philosophy cannot be empirical science's. → L1835-1837"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3: Why Astrology Cannot Be Empirical Science"
    factor_refs: list = ['astro_induct_fail', 'astro_ray_insuff', 'astro_horary_natal']
    
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
        l1_anchor="ap_v1.0.0_entry_3__why_astrology_cannot__001_L1",
    )
    version: str = "1.0.0"
