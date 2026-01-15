"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162838
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
    semantic_id="tb_v1.0.0_colours_in_eclipses_and_comets_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ColoursInEclipsesAndComets(SemanticEntry):
    """
    **Source Text** (Lines 4159-4213):
> In investigating general events, it is necessary further to obs...
    """
    
    original_text: str = """**Source Text** (Lines 4159-4213):
> In investigating general events, it is necessary further to observe the colours or hues displayed during an eclipse. If these colours be black or greenish, they portend effects similar to Saturn's nature; if white, to Jupiter; if reddish, to Mars; if yellow, to Venus; and if of various colours, to Mercury. Comets are displayed in the shape of beams, trumpets, pipes, and operate effects like those of Mars and Mercury; exciting wars, heated dispositions, and turbulent weather.

**English Paraphrase (Primary Language)**:
**Eclipse colours** and **comets** provide additional mundane indicators:

**Eclipse Colours**:
| Colour | Planetary Nature |
|--------|------------------|
| Black/Greenish | Saturn effects |
| White | Jupiter effects |
| Reddish | Mars effects |
| Yellow | Venus effects |
| Various | Mercury effects |

**Comets**: Have Mars-Mercury nature—indicate wars, heated temperaments, atmospheric disturbance. Their position and train direction show affected regions; duration shows effect length.

**Complete Chinese Interpretation (Secondary Language)**:
**日食颜色**和**彗星**提供额外的世俗指标：

**日食颜色**：
| 颜色 | 行星性质 |
|-----|---------|
| 黑色/绿色 | 土星效应 |
| 白色 | 木星效应 |
| 红色 | 火星效应 |
| 黄色 | 金星效应 |
| 多色 | 水星效应 |

**彗星**：具有火星-水星性质——指示战争、暴躁气质、大气扰动。其位置和彗尾方向显示受影响地区；持续时间显示效应长度。

**Core Points**:
- Eclipse colour indicates planetary nature of effects
- Black/green = Saturn; White = Jupiter; Red = Mars
- Comets have Mars-Mercury nature
- Comet appearance indicates wars and disturbance

**Narrative Snippets**:
- `[ns_tetra_ii_013]` `[trigger: eclipse_colour]` `[factor_trigger: astro_eclipse_colour]` `[role: 主干]` Eclipse colours indicate planetary nature: black=Saturn, white=Jupiter, red=Mars. → Source Text II.10"""
    normalized_text_zh: str = """"""
    subject: str = "Colours in Eclipses and Comets (Chapter X)"
    factor_refs: list = ['engine_id', 'eclipse_colour', 'astrology_classical', 'comet', 'astrology_classical', 'source_ref', 'rel_ii_013', 'astro_eclipse_colour', 'modifying', 'evi_ii_013', 'eclipse_colour', 'rule_eclipse_colour', 'concept_eclipse_colour', 'eclipse_colour', 'synesthesia']
    
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
        l1_anchor="tb_v1.0.0_colours_in_eclipses_and_comets_001_L1",
    )
    version: str = "1.0.0"
