"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.169601
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
    semantic_id="tb_v1.0.0_the_kind_of_death__chapter_ix_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheKindOfDeathChapterIx(SemanticEntry):
    """
    **Source Text** (Lines 7946-8098):
> It now remains to treat of the kind and species of death... Hen...
    """
    
    original_text: str = """**Source Text** (Lines 7946-8098):
> It now remains to treat of the kind and species of death... Hence, if it happen that Saturn be in fixed signs, and in quartile or opposition to the Sun, he will produce death by suffocation, occasioned either by multitudes of people, or by hanging or strangulation... Mars will produce death by slaughter, either in civil or foreign war, or by suicide.

**English Paraphrase (Primary Language)**:
**Manner of death** is determined by:
- The **anæretic place** (from duration of life analysis)
- **Planets in dominion** over that place
- **Sign characteristics** of the anæretic degree

**Planetary death types**:

| Planet | Natural Death | Violent Death |
|--------|---------------|---------------|
| Saturn | Lingering diseases, cold, consumption, dropsy | Suffocation, hanging, strangulation, drowning |
| Jupiter | Quinsy, lung inflammation, apoplexy | Wrath of kings, judicial condemnation |
| Mars | Fevers, hemorrhage, inflammation | Slaughter, war, suicide, fire, decapitation |
| Venus | Stomach/liver disorders, consumption | Poison, female treachery |
| Mercury | Fury, madness, epilepsy, dry diseases | Combined with malefics |

**Saturn violent indicators**:
- In fixed signs + quartile/opposition Sun = suffocation, hanging
- In bestial signs = wild beasts
- In watery signs + Moon = drowning
- In tropical signs + Sun = building collapse

**Mars violent indicators**:
- In human signs = slaughter, war, suicide
- Near Gorgon (Algol) = decapitation
- In Scorpio/Taurus = surgery, burning
- In mid-heaven = crucifixion

**Complete Chinese Interpretation (Secondary Language)**:
**死亡方式**由以下决定：
- **截寿位置**（来自寿命分析）
- **主宰该位置的行星**
- **截寿度数的星座特征**

**行星死亡类型**：

| 行星 | 自然死亡 | 暴力死亡 |
|------|----------|----------|
| 土星 | 慢性病、寒冷、消耗、水肿 | 窒息、绞刑、勒死、溺水 |
| 木星 | 喉痹、肺炎、中风 | 王怒、司法定罪 |
| 火星 | 发烧、出血、炎症 | 屠杀、战争、自杀、火、斩首 |
| 金星 | 胃/肝疾病、消耗 | 毒药、女性背叛 |
| 水星 | 狂怒、疯狂、癫痫、干燥疾病 | 与凶星结合 |

**Core Points**:
- Anæretic place and its ruler determine death manner
- Saturn = cold/lingering or suffocation/drowning
- Mars = hot/inflammatory or violent/war
- Sign type modifies death manner
- Both malefics in anæretic = body unburied

**Narrative Snippets**:
- `[ns_tetra_iv013]` `[trigger: death_manner]` `[factor_trigger: astro_planet_anaeretic]` `[role: 主干]` The manner of death is determined by the planet ruling the anæretic place—each planet produces distinctive death types. → Source Text IV.9
- `[ns_tetra_iv014]` `[trigger: saturn_death]` `[factor_trigger: astro_planet_saturn AND astro_place_anaeretic]` `[role: 条件分支]` Saturn in anæretic position: natural death by cold diseases; violent by suffocation, hanging, drowning. → Source Text IV.9
- `[ns_tetra_iv015]` `[trigger: mars_death]` `[factor_trigger: astro_planet_mars AND astro_place_anaeretic]` `[role: 条件分支]` Mars in anæretic position: natural death by fevers; violent by slaughter, war, fire, decapitation. → Source Text IV.9
- `[ns_tetra_iv025]` `[trigger: algol_decapitation]` `[factor_trigger: astro_mars AND astro_algol]` `[role: 条件分支]` Mars near Gorgon (Algol) indicates death by decapitation; both malefics in anæretic = body unburied. → Source Text IV.9
- `[ns_tetra_iv_dt]` `[trigger: death_type]` `[factor_trigger: death_type]` `[role: 效果]` Death type determined by anæretic ruler: Saturn=cold/suffocation, Mars=hot/violence, Jupiter=lung/judicial, Venus=poison, Mercury=madness. → Source Text IV.9
- `[ns_tetra_iv_dm]` `[trigger: dual_malefic]` `[factor_trigger: dual_malefic]` `[role: 条件分支]` Both malefics (Saturn and Mars) in anæretic position intensify to violent death with body unburied. → Source Text IV.9

**Textual Criticism**: This chapter is the most detailed in classical literature on manner of death; foundation for all subsequent medieval death-determination techniques."""
    normalized_text_zh: str = """"""
    subject: str = "The Kind of Death (Chapter IX)"
    factor_refs: list = ['anaeretic', 'violent_death', 'natural_death']
    
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
        l1_anchor="tb_v1.0.0_the_kind_of_death__chapter_ix_001_L1",
    )
    version: str = "1.0.0"
