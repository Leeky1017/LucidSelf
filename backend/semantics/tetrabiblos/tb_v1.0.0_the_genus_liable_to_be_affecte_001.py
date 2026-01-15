"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162815
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
    semantic_id="tb_v1.0.0_the_genus_liable_to_be_affecte_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheGenusLiableToBeAffecte(SemanticEntry):
    """
    **Source Text** (Lines 3809-3952):
> The third division relates to the genus or species to sustain t...
    """
    
    original_text: str = """**Source Text** (Lines 3809-3952):
> The third division relates to the genus or species to sustain the expected effect. This distinction is made by means of the signs in which the eclipse takes place and the ruling fixed stars and planets. If the zodiacal constellations be of human shape, the effect will fall upon the human race. If terrestrial or quadrupedal, on similar animals. Signs shaped like reptiles signify serpents; ferocious beast signs denote savage animals; tame beast signs show domestic animals.

**English Paraphrase (Primary Language)**:
The **genus or class affected** is determined by sign shape:

| Sign Type | Affected Class |
|-----------|----------------|
| Human-shaped (Gemini, Virgo, Aquarius) | Humans |
| Quadrupedal (Aries, Taurus, Leo, Sagittarius, Capricorn) | Four-footed animals |
| Reptile (Scorpio) | Snakes, reptiles |
| Marine (Cancer, Pisces) | Sea creatures, shipping |
| Winged (associated stars) | Birds |

Additional modifiers:
- Tropical/Equinoctial signs: Atmospheric changes
- Northern signs: Earthquakes
- Southern signs: Floods

**Complete Chinese Interpretation (Secondary Language)**:
**受影响的类别**由星座形状决定：

| 星座类型 | 受影响类别 |
|---------|-----------|
| 人形（双子座、室女座、水瓶座） | 人类 |
| 四足（白羊座、金牛座、狮子座、射手座、摩羯座） | 四足动物 |
| 爬行类（天蝎座） | 蛇、爬行动物 |
| 海洋类（巨蟹座、双鱼座） | 海洋生物、航运 |
| 有翅类（相关恒星） | 鸟类 |

附加修饰语：
- 回归/分点星座：大气变化
- 北方星座：地震
- 南方星座：洪水

**Core Points**:
- Sign shape determines affected class
- Human signs = human affairs
- Animal signs = corresponding animals
- Cardinal signs = seasonal changes
- Northern = earthquakes; Southern = floods

**Narrative Snippets**:
- `[ns_tetra_ii_012]` `[trigger: genus_affected]` `[factor_trigger: astro_sign_shape]` `[role: 主干]` Sign shape (human, quadrupedal, marine) determines the genus affected by eclipse. → Source Text II.8
- `[ns_tetra_ii_026]` `[trigger: human_signs]` `[factor_trigger: astro_sign_human AND astro_eclipse]` `[role: 条件分支]` Human-shaped signs (Gemini, Virgo, Aquarius) indicate effects will fall upon the human race. → Humans
- `[ns_tetra_ii_027]` `[trigger: terrestrial_signs]` `[factor_trigger: astro_sign_terrestrial AND astro_eclipse]` `[role: 条件分支]` Tropical signs = atmospheric changes; Northern signs = earthquakes; Southern signs = floods. → Elements
- `[ns_tetra_ii_ga]` `[trigger: genus_affected]` `[factor_trigger: genus_affected]` `[role: 效果]` Genus affected by eclipse: human-shaped signs affect humans, quadrupedal signs affect cattle, marine signs affect sea creatures. → Source Text II.8"""
    normalized_text_zh: str = """"""
    subject: str = "The Genus Liable to be Affected (Chapter VIII)"
    factor_refs: list = ['engine_id', 'sign_shape', 'astrology_classical', 'source_ref', 'rel_ii_012', 'astro_sign_shape', 'determining', 'evi_ii_012', 'sign_shape', 'rule_sign_genus', 'concept_genus', 'sign_shape', 'classification']
    
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
        l1_anchor="tb_v1.0.0_the_genus_liable_to_be_affecte_001_L1",
    )
    version: str = "1.0.0"
