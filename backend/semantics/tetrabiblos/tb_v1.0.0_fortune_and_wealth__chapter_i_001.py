"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.169487
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
    semantic_id="tb_v1.0.0_fortune_and_wealth__chapter_i_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class FortuneAndWealthChapterI(SemanticEntry):
    """
    **Source Text** (Lines 7100-7200):
> The consideration of fortune requires to be entered into with a...
    """
    
    original_text: str = """**Source Text** (Lines 7100-7200):
> The consideration of fortune requires to be entered into with a view to ascertaining, whether it will be great or small, and from what sources it will be derived... The part of Fortune, and the places of its rulers, the Moon, and the planets configurated with them, are to be observed.

**English Paraphrase (Primary Language)**:
**Material fortune** is judged from:

1. **Part of Fortune** (Lot of Fortune) and its rulers
2. **Moon** and her configurations
3. **Planets aspectng Part of Fortune**

**Wealth indicators**:
- Benefics (Jupiter, Venus) ruling/aspecting Part of Fortune = prosperity
- Malefics (Saturn, Mars) afflicting = poverty, loss
- Part of Fortune in angles = prominent fortune
- Part of Fortune cadent = humble circumstances

**Sources of wealth** depend on the planet ruling Part of Fortune:
- Saturn: Agriculture, building, navigation
- Jupiter: Trusts, stewardships, priesthoods
- Mars: Military, command, fire-related
- Venus: Gifts, women, ornaments
- Mercury: Trade, commerce, rhetoric

**Complete Chinese Interpretation (Secondary Language)**:
**物质财富**从以下判断：

1. **福点**（命运之分）及其主星
2. **月亮**及其配置
3. **与福点相位的行星**

**财富指标**：
- 吉星（木星、金星）主宰/相位福点 = 繁荣
- 凶星（土星、火星）刑克 = 贫穷、损失
- 福点在角宫 = 显著财富
- 福点在果宫 = 卑微处境

**财富来源**取决于主宰福点的行星：
- 土星：农业、建筑、航海
- 木星：信托、管理、祭司
- 火星：军事、指挥、与火相关
- 金星：礼物、女性、装饰品
- 水星：贸易、商业、修辞

**Core Points**:
- Part of Fortune = primary wealth indicator
- Benefic rulers = prosperity; Malefic rulers = poverty
- Angular Part = prominent; Cadent Part = humble
- Ruling planet determines wealth source
- Moon configurations modify fortune

**Narrative Snippets**:
- `[ns_tetra_iv001]` `[trigger: fortune_wealth]` `[factor_trigger: astro_part_of_fortune AND pars_fortunae AND benefic_ruler AND malefic_ruler AND wealth_outcome]` `[role: 主干]` Material fortune is judged from the Part of Fortune, its rulers, and the Moon's configurations. → Source Text IV.1
- `[ns_tetra_iv002]` `[trigger: wealth_source]` `[factor_trigger: astro_planet_ruler_fortune]` `[role: 条件分支]` The ruling planet of Part of Fortune determines the source of wealth—Saturn agriculture, Jupiter trusts, Mars military. → Source Text IV.1

**Textual Criticism**: Part of Fortune calculation: Day = ASC + Moon - Sun; Night = ASC + Sun - Moon (some traditions reverse)."""
    normalized_text_zh: str = """"""
    subject: str = "Fortune and Wealth (Chapter I)"
    factor_refs: list = ['pars_fortunae', 'doryphory', 'new_candidate']
    
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
        l1_anchor="tb_v1.0.0_fortune_and_wealth__chapter_i_001_L1",
    )
    version: str = "1.0.0"
