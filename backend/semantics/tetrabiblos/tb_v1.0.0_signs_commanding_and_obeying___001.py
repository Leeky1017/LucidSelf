"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182629
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
    semantic_id="tb_v1.0.0_signs_commanding_and_obeying___001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class SignsCommandingAndObeying(SemanticEntry):
    """
    **Source Text** (Lines 2255-2268):
> Any two signs configurated with each other at an equal distance...
    """
    
    original_text: str = """**Source Text** (Lines 2255-2268):
> Any two signs configurated with each other at an equal distance from the same, or from either equinoctial point, are termed commanding and obeying, because the ascensional and descensional times of the one are equal to those of the other, and both describe equal parallels. The signs in the summer semicircle are commanding; those in the winter semicircle, obeying: for, when the Sun is present in the former, he makes the day longer than the night; and, when in the latter, he produces the contrary effect.

**English Paraphrase (Primary Language)**:
Ptolemy defines **commanding and obeying signs**—pairs equidistant from an equinoctial point:
- **Commanding signs** (summer semicircle: Aries-Virgo): When Sun is here, days are longer
- **Obeying signs** (winter semicircle: Libra-Pisces): When Sun is here, nights are longer

This creates antiscia-like pairs (Aries-Virgo, Taurus-Leo, Gemini-Cancer / Libra-Pisces, Scorpio-Aquarius, Sagittarius-Capricorn) with equal ascensional times.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密定义了**命令与服从星座**——与分点等距的星座对：
- **命令星座**（夏季半圆：白羊座-室女座）：太阳在此时，白昼更长
- **服从星座**（冬季半圆：天秤座-双鱼座）：太阳在此时，黑夜更长

这创造了类似反映点的配对，具有相等的上升时间。

**Core Points**:
- Commanding = summer signs (longer days)
- Obeying = winter signs (longer nights)
- Pairs equidistant from equinoxes
- Related to ascensional times

**Narrative Snippets**:
- `[ns_tetra_i074]` `[trigger: commanding_obeying]` `[factor_trigger: astro_sign_commanding AND sign_command_obey]` `[role: 主干]` Summer signs command, winter signs obey—based on day/night length. → Source Text I.17"""
    normalized_text_zh: str = """"""
    subject: str = "Signs Commanding and Obeying (Chapter XVII)"
    factor_refs: list = ['engine_id', 'sign_command_obey', 'astrology_classical', 'source_ref', 'rel_i_029', 'sign_commanding', 'commanding', 'evi_i_024', 'sign_command_obey', 'rule_command_obey', 'concept_command', 'sign_command_obey', 'dominance']
    
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
        l1_anchor="tb_v1.0.0_signs_commanding_and_obeying___001_L1",
    )
    version: str = "1.0.0"
