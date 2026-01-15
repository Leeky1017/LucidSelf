"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237851
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
    semantic_id="ap_v1.0.0_entry_13__astrology_as_languag_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry13AstrologyAsLanguag(SemanticEntry):
    """
    **Source Text** (Lines 2974-3080):
> To such a perfected intuitive man no particular system of symbo...
    """
    
    original_text: str = """**Source Text** (Lines 2974-3080):
> To such a perfected intuitive man no particular system of symbolism is necessary; and astrology is of no special value. But he cannot communicate his intuitions to others. Communication necessitates a system of interpretation; a set of symbols which can serve as spatial-mental "bridges" between the wholeness of the moment and all perceivers. It thus needs a language. Astrology is such a language, just as the series of hexagrams of the Chinese Yi King is such a language.
>
> The true foundation of astrology is such a holistic logic... This holistic logic, based on the perception of the wholeness of the material used as symbolical elements and of its functional coherency, is for the truly intuitive man as logical as intellectual logic. But it is not as rigid and set... because it is creative. It is a function of evolving life.
>
> ...any correlation established between, say, Saturn and a particular psychological function must derive from a consistent interpretation of: 1) the solar system as a whole; 2) the human psyche as a whole. If a principle of correlation is established giving to one planet a symbolical significance in terms of its distance to the Sun, then all planets must be given their respective symbolical significance in the same way.

**Key Term Analysis**:
- **Astrology as language**: `communication system` / `spatial-mental bridges` / `like Yi King`
- **Functional coherency**: `holistic logic principle` / `consistent interpretation` / `no mixing planes`
- **Systematic correlation**: `Saturn-function must derive from whole interpretation` / `same principle for all`

**English Paraphrase (Primary Language)**:
The perfected intuitive needs no astrology; but communication requires a language—"a set of symbols which can serve as spatial-mental bridges." Astrology is such a language, like the Yi King.

Holistic logic's key principle: "functional coherency." Any correlation (e.g., Saturn = X function) must derive from consistent interpretation of both the solar system as whole and the human psyche as whole. If one principle establishes significance (e.g., distance to Sun), all planets must follow the same principle. No mixing of interpretation planes.

**Complete Chinese Interpretation (Secondary Language)**:
完美的直觉者不需要占星学；但沟通需要一种语言——"一套可以作为空间-心智桥梁的符号"。占星学就是这样一种语言，如同易经。

整体论逻辑的关键原则："功能一致性"。任何关联（如土星=X功能）必须源自对太阳系作为整体和人类心理作为整体的一致解释。如果一个原则建立意义（如到太阳的距离），所有行星必须遵循同一原则。不能混淆解释层面。

**Narrative Snippets**:
- `[ns_aop_105]` `[trigger: astrology_language]` `[factor_trigger: astro_language AND astro_lang_struct]` `[role: 主干]` Astrology = language for communicating intuitions, spatial-mental bridges, like Yi King. → L2974-2982
- `[ns_aop_106]` `[trigger: functional_coherency]` `[factor_trigger: astro_func_coher AND astro_func_coh AND astro_dual_sym]` `[role: 主干依赖]` Holistic logic principle: functional coherency—consistent interpretation, no mixing planes. → L3065-3080"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 13: Astrology as Language—Functional Coherency"
    factor_refs: list = ['astro_language', 'astro_func_coherency']
    
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
        l1_anchor="ap_v1.0.0_entry_13__astrology_as_languag_001_L1",
    )
    version: str = "1.0.0"
