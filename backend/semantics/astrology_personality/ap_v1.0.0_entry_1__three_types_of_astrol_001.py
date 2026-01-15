"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238022
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
    semantic_id="ap_v1.0.0_entry_1__three_types_of_astrol_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1ThreeTypesOfAstrol(SemanticEntry):
    """
    **Source Text** (Lines 6574-6622):
> Three Types of Astrology: The foregoing study of the three basi...
    """
    
    original_text: str = """**Source Text** (Lines 6574-6622):
> Three Types of Astrology: The foregoing study of the three basic types of planetary motion and of their relative significances... will enable us to bring order into a confused situation...
>
> One type of astrology will function primarily in terms of axial motion, and stress the individual factor... Another type will emphasize every element connected with orbital revolution... Still another type—very little developed as yet—will be of a more occult character and deal with vast planetary factors, with the cosmic (spiritual and creative) influence of stars and Divine Hierarchies...
>
> Each type should normally and logically evolve its own technique of interpretation.

**Key Term Analysis**:
- **Astrology of Individual**: `axial motion emphasis` / `natal astrology, horary astrology` / `psychological values`
- **Astrology of Collective**: `orbital revolution emphasis` / `mundane astrology` / `cosmic electro-dynamics`
- **Occult Astrology**: `polar gyration` / `cosmic creative influences` / `stars and Divine Hierarchies`

**English Paraphrase (Primary Language)**:
Rudhyar classifies astrology into three types based on planetary motion:
1. **Individual astrology** (axial motion): natal/horary, stresses individual, psychological values
2. **Collective astrology** (orbital revolution): mundane astrology, cosmic electro-dynamics, solar emphasis
3. **Occult astrology** (polar gyration): cosmic creative, stars, Divine Hierarchies, yet undeveloped

Each type "should normally and logically evolve its own technique of interpretation."

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar根据行星运动将占星学分为三类：
1. **个体占星学**（轴向运动）：本命/卜卦占星，强调个体，心理价值
2. **集体占星学**（轨道公转）：世俗占星，宇宙电动力学，太阳强调
3. **神秘占星学**（极点进动）：宇宙创造性，恒星，神圣等级，尚未发展

每种类型"应该正常且合乎逻辑地发展自己的解释技术。"

**Narrative Snippets**:
- `[ns_aop_145]` `[trigger: three_types]` `[factor_trigger: astro_three_types]` `[role: 主干]` Three types of astrology: Individual (axial), Collective (orbital), Occult (polar). → L6603-6612
- `[ns_aop_146]` `[trigger: own_technique]` `[factor_trigger: astro_technique]` `[role: 总结]` Each type evolves its own interpretation technique based on motion emphasis. → L6614-6622"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: Three Types of Astrology—Overview"
    factor_refs: list = ['astro_individual', 'astro_collective', 'astro_occult']
    
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
        l1_anchor="ap_v1.0.0_entry_1__three_types_of_astrol_001_L1",
    )
    version: str = "1.0.0"
