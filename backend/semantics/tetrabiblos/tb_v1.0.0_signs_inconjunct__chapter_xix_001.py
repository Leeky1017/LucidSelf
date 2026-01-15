"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182650
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
    semantic_id="tb_v1.0.0_signs_inconjunct__chapter_xix_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class SignsInconjunctChapterXix(SemanticEntry):
    """
    **Source Text** (Lines 2295-2320):
> All signs, between which there does not exist any familiarity i...
    """
    
    original_text: str = """**Source Text** (Lines 2295-2320):
> All signs, between which there does not exist any familiarity in any of the modes above specified, are inconjunct and separated. For instance, all signs are inconjunct which are neither commanding nor obeying, and not beholding each other nor of equal power, as well as all signs which contain between them the space of one sign only, or the space of five signs, and which do not at all share in any of the four prescribed configurations.

**English Paraphrase (Primary Language)**:
Ptolemy defines **inconjunct signs** (aversion, ἀσύνδετα)—signs with NO relationship:
- Not commanding/obeying
- Not beholding each other
- Not in aspect (opposition, trine, square, sextile)
- Specifically: **semi-sextile** (30°, one sign apart) and **quincunx** (150°, five signs apart)

These are the only angular distances that share no aspect, no antiscia, no commanding/obeying relationship. They are "blind" to each other.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密定义了**不合星座**（背离，ἀσύνδετα）——没有任何关系的星座：
- 非命令/服从
- 非互视
- 无相位（对冲、三分、四分、六分）
- 具体来说：**半六分**（30°，相隔一个星座）和**梅花相**（150°，相隔五个星座）

这些是唯一不共享任何相位、反映点、命令/服从关系的角度距离。它们彼此"看不见"。

**Core Points**:
- Inconjunct = no familiarity in any mode
- Semi-sextile (30°) and Quincunx (150°) are inconjunct
- These signs are "blind" to each other
- No aspect, no antiscia, no command/obey

**Narrative Snippets**:
- `[ns_tetra_i076]` `[trigger: inconjunct]` `[factor_trigger: astro_aspect_inconjunct]` `[role: 主干]` Signs one or five signs apart are inconjunct—no familiarity exists. → Source Text I.19"""
    normalized_text_zh: str = """"""
    subject: str = "Signs Inconjunct (Chapter XIX)"
    factor_refs: list = ['engine_id', 'aspect_inconjunct', 'astrology_classical', 'source_ref', 'rel_i_031', 'aspect_inconjunct', 'disconnecting', 'rel_i_031b', 'astro_aspect_inconjunct', 'contrasting', 'evi_i_026', 'aspect_inconjunct', 'rule_inconjunct', 'concept_inconjunct', 'aspect_inconjunct', 'dissociation']
    
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
        l1_anchor="tb_v1.0.0_signs_inconjunct__chapter_xix_001_L1",
    )
    version: str = "1.0.0"
