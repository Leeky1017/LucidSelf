"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162654
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
    semantic_id="tb_v1.0.0_general_division_of_the_subjec_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class GeneralDivisionOfTheSubjec(SemanticEntry):
    """
    **Source Text** (Lines 2991-3048):
> The foreknowledge to be acquired by means of Astrology is to be...
    """
    
    original_text: str = """**Source Text** (Lines 2991-3048):
> The foreknowledge to be acquired by means of Astrology is to be regarded in two great and principal divisions. The first, which may be properly called General, or Universal, concerns entire nations, countries, or cities; and the second, denominated Particular, or Genethliacal, relates to men individually... general events are produced by causes greater and more compulsatory than the causes of particular events.

**English Paraphrase (Primary Language)**:
Ptolemy divides astrology into two principal branches: (1) **Universal/Mundane**—concerning nations, countries, cities; (2) **Genethliacal/Natal**—concerning individuals. Mundane takes precedence because general causes are greater and more compulsory, extended potencies control limited ones, and particular events are comprehended within general events.

Mundane events subdivide into: events affecting **entire countries** (wars, pestilence, famine, earthquakes) and events affecting **cities/districts** (seasonal weather, provisions). Methodology requires knowing zodiacal familiarities of regions and observing eclipses/transits affecting those regions.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密将占星学分为两个主要分支：（1）**世俗/总体**——关于国家、地区、城市；（2）**本命/个人**——关于个人。世俗占星优先，因为普遍原因更大且更强制，宏观力量控制微观力量，个别事件被包含在普遍事件中。

**Core Points**:
- Two divisions: Universal (mundane) vs Particular (natal)
- Mundane takes precedence over natal
- General causes greater and more compulsory than particular
- Macro controls micro; particular comprehended in general

**Narrative Snippets**:
- `[ns_tetra_ii001]` `[trigger: mundane_natal_division]` `[factor_trigger: astro_mundane_astrology AND mundane_astrology AND natal_astrology]` `[role: 主干]` Astrology divides into Universal (nations/cities) and Particular (individuals); general takes precedence over particular. → Source Text II.1
- `[ns_tetra_ii015]` `[trigger: general_precedence]` `[factor_trigger: astro_mundane AND astro_hierarchy AND general_precedence]` `[role: 条件分支]` General causes are greater and more compulsory than particular—extended potencies control limited ones. → Precedence
- `[ns_tetra_ii016]` `[trigger: mundane_scope]` `[factor_trigger: astro_mundane AND astro_collective]` `[role: 条件分支]` Mundane concerns wars, pestilence, famine, earthquakes affecting entire countries or seasonal weather affecting cities. → Scope"""
    normalized_text_zh: str = """"""
    subject: str = "General Division of the Subject (Chapter I)"
    factor_refs: list = ['mundane_astrology', 'natal_astrology']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_general_division_of_the_subjec_001_L1",
    )
    version: str = "1.0.0"
