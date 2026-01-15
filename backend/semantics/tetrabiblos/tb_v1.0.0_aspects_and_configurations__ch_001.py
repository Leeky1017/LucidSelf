"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182616
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
    semantic_id="tb_v1.0.0_aspects_and_configurations__ch_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class AspectsAndConfigurationsCh(SemanticEntry):
    """
    **Source Text** (Lines 2188-2252):
> There are certain familiarities or connections between differen...
    """
    
    original_text: str = """**Source Text** (Lines 2188-2252):
> There are certain familiarities or connections between different parts of the zodiac... This mutual configuration attaches to all parts diametrically distant from each other, containing between them two right angles, or six signs, or a hundred and eighty degrees [opposition]: it also exists in all parts at the triangular distance [trine, 120°]... at the quadrate distance [square, 90°]... and at the hexagonal distance [sextile, 60°]... Of these configurations, the trine and the sextile are each called harmonious, because they are constituted between signs of the same kind; being formed between either all feminine or all masculine signs. The opposition and quartile are considered to be discordant, because they are configurations made between signs not of the same kind, but of different natures and sexes.

**English Paraphrase (Primary Language)**:
Ptolemy defines the **four major aspects** by geometric division of the circle:
- **Opposition** (180°, 6 signs): Diameter—maximum separation
- **Trine** (120°, 4 signs): Equilateral triangle—harmonious
- **Square** (90°, 3 signs): Right angle—discordant
- **Sextile** (60°, 2 signs): Hexagon—harmonious

The distinction between **harmonious** (trine, sextile) and **discordant** (square, opposition) aspects is based on **sign gender**: trines and sextiles connect signs of the same gender (all masculine or all feminine); squares and oppositions connect signs of different genders.

The conjunction is notably absent from this chapter because it involves parts in the same place, not configurated "with each other" at a distance.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密通过圆的几何划分定义**四大相位**：
- **对冲**（180°，6个星座）：直径——最大分离
- **三分**（120°，4个星座）：等边三角形——和谐
- **四分**（90°，3个星座）：直角——不和谐
- **六分**（60°，2个星座）：六边形——和谐

**和谐**（三分、六分）与**不和谐**（四分、对冲）相位的区分基于**星座性别**：三分和六分连接相同性别的星座（都是阳性或都是阴性）；四分和对冲连接不同性别的星座。

合相在本章中明显缺席，因为它涉及同一位置的部分，而不是在远处"彼此"配置。

**Core Points**:
- Opposition (180°): Maximum tension, discordant
- Trine (120°): Flowing harmony, same-gender signs
- Square (90°): Dynamic tension, different-gender signs
- Sextile (60°): Gentle harmony, same-gender signs
- Aspect quality derived from sign gender compatibility
- Conjunction not listed (same place, not configurated)

**Narrative Snippets**:
- `[ns_tetra_i044]` `[trigger: aspect_definition]` `[factor_trigger: astro_aspect_type]` `[role: 主干]` Aspects are determined by geometric division: opposition (180°), trine (120°), square (90°), sextile (60°). → Source Text I.16
- `[ns_tetra_i045]` `[trigger: harmonious_aspects]` `[factor_trigger: astro_aspect_trine OR astro_aspect_sextile]` `[role: 条件分支]` Trine and sextile are harmonious because they connect signs of the same gender. → Source Text I.16
- `[ns_tetra_i046]` `[trigger: discordant_aspects]` `[factor_trigger: astro_aspect_square OR astro_aspect_opposition]` `[role: 条件分支]` Opposition and square are discordant because they connect signs of different genders. → Source Text I.16

**Textual Criticism**: Footnote notes Kepler's later addition of minor aspects (quintile, semisquare, etc.) not found in Ptolemy."""
    normalized_text_zh: str = """"""
    subject: str = "Aspects and Configurations (Chapter XVI)"
    factor_refs: list = ['engine_id', 'aspect_type', 'astrology_classical', 'source_ref', 'rel_i_017', 'aspect_type', 'characterizing', 'evi_i_013', 'aspect_type', 'rule_aspect_nature', 'concept_aspect', 'aspect_type', 'interpersonal']
    
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
        l1_anchor="tb_v1.0.0_aspects_and_configurations__ch_001_L1",
    )
    version: str = "1.0.0"
