"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192683
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
    semantic_id="tb_v1.0.0_male_or_female__chapter_vii_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class MaleOrFemaleChapterVii(SemanticEntry):
    """
    **Source Text** (Lines 5256-5283):
> The consideration of this question rests not on a single basis....
    """
    
    original_text: str = """**Source Text** (Lines 5256-5283):
> The consideration of this question rests not on a single basis... it depends on the several situations of the two luminaries and the ascendant, and upon such planets as possess any prerogatives in the places of those situations... by the nature of the signs in which they are situated, by their relative position to each other, and also by their position towards the earth; as when in the east, they are masculinely disposed, and, when in the west, femininely.

**English Paraphrase (Primary Language)**:
Sex of the native is determined by examining **three places**: Sun, Moon, and Ascendant, with their rulers:

**Masculine indicators**:
- Planets in masculine signs (Fire/Air)
- Eastern position (oriental)
- Matutine position (before Sun)

**Feminine indicators**:
- Planets in feminine signs (Earth/Water)
- Western position (occidental)
- Vespertine position (after Sun)

The majority determines the sex.

**Complete Chinese Interpretation (Secondary Language)**:
原命性别通过检查**三个位置**确定：太阳、月亮和上升点，及其主星：

**阳性指标**：
- 行星在阳性星座（火/风）
- 东方位置（东方的）
- 晨星位置（太阳之前）

**阴性指标**：
- 行星在阴性星座（土/水）
- 西方位置（西方的）
- 昏星位置（太阳之后）

多数决定性别。

**Core Points**:
- Three places examined: Sun, Moon, Ascendant
- Masculine = Fire/Air signs, oriental, matutine
- Feminine = Earth/Water signs, occidental, vespertine
- Majority determines sex

**Narrative Snippets**:
- `[ns_tetra_iii014]` `[trigger: sex_determination]` `[factor_trigger: astro_planet_masculine OR astro_planet_feminine]` `[role: 主干]` Sex is determined by the masculine or feminine constitution of Sun, Moon, Ascendant and their rulers. → Source Text III.7
- `[ns_ptolemy_iii_033]` `[trigger: oriental_masculine]` `[factor_trigger: astro_oriental AND astro_masculine]` `[role: 条件分支]` When planets are in the east (oriental) they are masculinely disposed; when in the west, femininely. → Position
- `[ns_ptolemy_iii_034]` `[trigger: majority_rule]` `[factor_trigger: astro_majority AND astro_sex]` `[role: 条件分支]` The majority of masculine or feminine indicators among Sun, Moon, Ascendant determines the native's sex. → Method
- `[ns_tetra_iii_ns]` `[trigger: native_sex]` `[factor_trigger: native_sex]` `[role: 效果]` Native's sex determined by majority of masculine/feminine indicators at Sun, Moon, Ascendant and their rulers. → Source Text III.7"""
    normalized_text_zh: str = """"""
    subject: str = "Male or Female (Chapter VII)"
    factor_refs: list = ['masculine_indicator']
    
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
        l1_anchor="tb_v1.0.0_male_or_female__chapter_vii_001_L1",
    )
    version: str = "1.0.0"
