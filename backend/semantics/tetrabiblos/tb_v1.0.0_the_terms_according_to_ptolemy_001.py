"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182709
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
    semantic_id="tb_v1.0.0_the_terms_according_to_ptolemy_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheTermsAccordingToPtolemy(SemanticEntry):
    """
    **Source Text** (Lines 2714-2802):
> The foregoing terms are disposed agreeably to the Ægyptian meth...
    """
    
    original_text: str = """**Source Text** (Lines 2714-2802):
> The foregoing terms are disposed agreeably to the Ægyptian method; which, however, is neither consonant with order, nor with any assignment of a substantial reason. But the terms according to the Chaldaic mode, which observes a connected order and arrangement by decans, are more worthy of regard... Nevertheless, there is still another method, founded on a plausible system, and entitled to credit on account of its connection with the natures of the stars, and their qualities of domination.

**English Paraphrase (Primary Language)**:
**Ptolemaic Terms** represent Ptolemy's reformed system based on rational dignity principles:

**Ptolemy's method**:
1. Count dignities each planet holds in a sign (domicile, exaltation, triplicity)
2. Planets with most dignities receive first/largest portions
3. Default allocations: Benefics 7°, Malefics 5°, Mercury 6°
4. Order within sign follows dignity count, then natural order

**Rationale**: Unlike Egyptian system, Ptolemaic terms have consistent mathematical basis—allocations derive from measurable dignities.

**Historical note**: Despite Ptolemy's preference for his own system, medieval and Renaissance astrologers often retained Egyptian terms, viewing them as having ancient authority.

**Complete Chinese Interpretation (Secondary Language)**:
**托勒密界**代表托勒密基于理性尊贵原则的改革系统：

**托勒密的方法**：
1. 计算每颗行星在星座中持有的尊贵（庙旺、曜升、三分）
2. 拥有最多尊贵的行星获得第一/最大份额
3. 默认分配：吉星7°，凶星5°，水星6°
4. 星座内顺序遵循尊贵计数，然后是自然顺序

**理据**：与埃及系统不同，托勒密界有一致的数学基础——分配源于可测量的尊贵。

**历史注释**：尽管托勒密偏好自己的系统，中世纪和文艺复兴时期的占星家常保留埃及界，视其具有古老权威。

**Core Points**:
- Ptolemaic system based on dignity count
- Benefics (Jupiter, Venus) receive 7° default
- Malefics (Saturn, Mars) receive 5° default
- Mercury receives 6° default
- Order determined by dignity hierarchy
- More rational than Egyptian system

**Narrative Snippets**:
- `[ns_tetra_i055]` `[trigger: ptolemaic_terms]` `[factor_trigger: astro_terms_ptolemaic]` `[role: 主干]` Ptolemaic terms allocate degrees based on dignity count—benefics 7°, malefics 5°, Mercury 6°. → Source Text I.24"""
    normalized_text_zh: str = """"""
    subject: str = "The Terms According to Ptolemy (Chapter XXIV)"
    factor_refs: list = ['engine_id', 'terms_ptolemaic', 'astrology_classical', 'source_ref', 'rel_i_021b', 'terms_ptolemaic', 'supporting', 'evi_i_017b', 'terms_ptolemaic', 'rule_ptolemaic_terms', 'concept_ptolemaic_terms', 'terms_ptolemaic', 'rationality']
    
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
        l1_anchor="tb_v1.0.0_the_terms_according_to_ptolemy_001_L1",
    )
    version: str = "1.0.0"
