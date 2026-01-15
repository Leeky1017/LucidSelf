"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192672
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
    semantic_id="tb_v1.0.0_brothers_and_sisters__chapter__001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class BrothersAndSistersChapter(SemanticEntry):
    """
    **Source Text** (Lines 5178-5242):
> The place, whence inferences are drawn respecting brothers and ...
    """
    
    original_text: str = """**Source Text** (Lines 5178-5242):
> The place, whence inferences are drawn respecting brothers and sisters, is to be considered as being applicable only to children of the same mother, and it is consequently, agreeably to nature, presumed to be the same as the maternal place; viz. the sign occupying the mid-heaven; or, by day, that which contains Venus, and, by night, the Moon... Should the benefics be configurated with this place, there will be several brothers and sisters; should the malefics be in elevation over this place, the brothers and sisters will be few.

**English Paraphrase (Primary Language)**:
**Siblings** are judged from the **maternal place**:
- **By day**: Mid-heaven or Venus's sign
- **By night**: Mid-heaven or Moon's sign

**Number of siblings**:
- Benefics configurated = many siblings
- Malefics elevated = few siblings
- Bicorporeal signs = multiple births
- Masculine stars = brothers; Feminine stars = sisters
- Oriental stars = elder; Occidental stars = younger

**Sibling relationships**: Harmonious configurations between sibling-significators = brotherly love; inconjunct/opposition = enmity and fraud.

**Complete Chinese Interpretation (Secondary Language)**:
**兄弟姐妹**从**母系宫位**判断：
- **白天**：中天或金星所在星座
- **夜晚**：中天或月亮所在星座

**兄弟姐妹数量**：
- 吉星配置 = 多兄弟姐妹
- 凶星高居 = 少兄弟姐妹
- 双体星座 = 多胎
- 阳性星 = 兄弟；阴性星 = 姐妹
- 东方星 = 年长；西方星 = 年幼

**Core Points**:
- Siblings from maternal place (MC or Venus/Moon by sect)
- Benefics = many; Malefics = few
- Bicorporeal signs = multiple births
- Masculine = brothers; Feminine = sisters

**Narrative Snippets**:
- `[ns_tetra_iii013]` `[trigger: siblings_place]` `[factor_trigger: astro_house_maternal]` `[role: 主干]` Brothers and sisters are judged from the maternal place—mid-heaven or Venus/Moon by sect. → Source Text III.6
- `[ns_ptolemy_iii_031]` `[trigger: sibling_number]` `[factor_trigger: astro_benefic AND astro_malefic]` `[role: 条件分支]` Benefics configurated with maternal place = many siblings; malefics elevated = few siblings. → Number
- `[ns_ptolemy_iii_032]` `[trigger: sibling_gender]` `[factor_trigger: astro_masculine AND astro_feminine]` `[role: 条件分支]` Masculine stars indicate brothers, feminine stars indicate sisters; oriental = elder, occidental = younger. → Gender
- `[ns_tetra_iii_sn]` `[trigger: sibling_number]` `[factor_trigger: sibling_number]` `[role: 效果]` Sibling number determined by benefics/malefics at maternal place: benefics = many, malefics = few, bicorporeal signs = twins. → Source Text III.6"""
    normalized_text_zh: str = """"""
    subject: str = "Brothers and Sisters (Chapter VI)"
    factor_refs: list = ['house_maternal']
    
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
        l1_anchor="tb_v1.0.0_brothers_and_sisters__chapter__001_L1",
    )
    version: str = "1.0.0"
