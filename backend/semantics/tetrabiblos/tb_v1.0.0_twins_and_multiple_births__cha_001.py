"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192695
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
    semantic_id="tb_v1.0.0_twins_and_multiple_births__cha_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TwinsAndMultipleBirthsCha(SemanticEntry):
    """
    **Source Text** (Lines 5291-5366):
> When two, or all three, of the said places may be situated in b...
    """
    
    original_text: str = """**Source Text** (Lines 5291-5366):
> When two, or all three, of the said places may be situated in bicorporeal signs, births of this kind will occur... more than twins will be born, in a case wherein all the ruling places may be in bicorporeal signs... The number of children to be produced is to be inferred from the planet which exercises the right of determining the number.

**English Paraphrase (Primary Language)**:
**Multiple births** occur when:
- Two or three key places (Sun, Moon, ASC) are in **bicorporeal signs** (Gemini, Virgo, Sagittarius, Pisces)
- Ruling planets also in bicorporeal signs
- Mid-heaven connected with luminaries (not just ASC)

**Number** determined by the planet with most configurative rights.
**Sex** of multiples determined by masculine/feminine constitution of planets in configuration.

**Classical examples**:
- Saturn, Jupiter, Mars in bicorporeal signs = three males (Anactores)
- Venus, Moon, Mercury feminine = three females (Graces)
- Mixed configurations = mixed sexes (Dioscuri)

**Complete Chinese Interpretation (Secondary Language)**:
**多胎**发生于：
- 两个或三个关键位置（太阳、月亮、上升）在**双体星座**（双子、室女、射手、双鱼）
- 主星也在双体星座
- 中天与发光体连接（不仅是上升）

**数量**由配置权最多的行星决定。
**性别**由配置行星的阳/阴性决定。

**Core Points**:
- Bicorporeal signs = potential for multiples
- More bicorporeal = more children at once
- Planet with most rights determines number
- Masculine/feminine constitution determines sex of multiples

**Narrative Snippets**:
- `[ns_tetra_iii015]` `[trigger: twins_multiples]` `[factor_trigger: astro_sign_bicorporeal]` `[role: 主干]` Twins and multiples occur when luminaries and ascendant are in bicorporeal signs. → Source Text III.8
- `[ns_tetra_iii_bn]` `[trigger: birth_number]` `[factor_trigger: birth_number]` `[role: 效果]` Birth number (singleton, twins, triplets) determined by bicorporeal sign presence at Sun, Moon, Ascendant. → Source Text III.8"""
    normalized_text_zh: str = """"""
    subject: str = "Twins and Multiple Births (Chapter VIII)"
    factor_refs: list = ['sign_bicorporeal']
    
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
        l1_anchor="tb_v1.0.0_twins_and_multiple_births__cha_001_L1",
    )
    version: str = "1.0.0"
