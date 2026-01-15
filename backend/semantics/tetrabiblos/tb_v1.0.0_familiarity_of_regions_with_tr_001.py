"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162743
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
    semantic_id="tb_v1.0.0_familiarity_of_regions_with_tr_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class FamiliarityOfRegionsWithTr(SemanticEntry):
    """
    **Source Text** (Lines 3142-3481):
> It has been already stated that there are four triplicities dis...
    """
    
    original_text: str = """**Source Text** (Lines 3142-3481):
> It has been already stated that there are four triplicities distinguishable in the zodiac. The first, composed of Aries, Leo, and Sagittarius, is the north-west triplicity; Jupiter has chief dominion, Mars also rules... The whole inhabited earth is accordingly divided into four quadrants, agreeing with the number of the triplicities... [Extensive catalog of nations assigned to triplicities with their planetary rulers and resulting characteristics]

**English Paraphrase (Primary Language)**:
Ptolemy assigns **world regions to triplicities**:

| Quadrant | Triplicity | Signs | Rulers | Regions |
|----------|-----------|-------|--------|---------|
| NW (Europe) | Fire | Aries/Leo/Sag | Jupiter, Mars | Britain, Germany, Italy, Gaul, Spain |
| SE (Asia) | Earth | Taurus/Virgo/Cap | Venus, Saturn | India, Persia, Babylon, Mesopotamia |
| NE (N. Asia) | Air | Gemini/Libra/Aqu | Saturn, Jupiter | Hyrcania, Armenia, Bactriana, Scythia |
| SW (Libya) | Water | Cancer/Scorp/Pisces | Mars, Venus | Numidia, Carthage, Africa, Mauritania |

Each triplicity's planetary rulers determine regional characteristics:
- Fire triplicity (Europe): Imperious, lovers of freedom, warlike, industrious
- Earth triplicity (Asia): Worship Venus, hot constitution, amorous, fond of ornaments
- Air triplicity (N. Asia): Rich, luxurious, learned in theology, just, chaste
- Water triplicity (Libya): Hot, desirous of women, courageous, addicted to magic

**Complete Chinese Interpretation (Secondary Language)**:
托勒密将**世界地区分配给三分性**：

| 象限 | 三分性 | 星座 | 主星 | 地区 |
|------|--------|------|------|------|
| 西北（欧洲）| 火 | 白羊/狮子/射手 | 木星、火星 | 英国、德国、意大利、高卢、西班牙 |
| 东南（亚洲）| 土 | 金牛/室女/摩羯 | 金星、土星 | 印度、波斯、巴比伦、美索不达米亚 |
| 东北（北亚）| 风 | 双子/天秤/水瓶 | 土星、木星 | 希尔卡尼亚、亚美尼亚、巴克特里亚 |
| 西南（利比亚）| 水 | 巨蟹/天蝎/双鱼 | 火星、金星 | 努米底亚、迦太基、非洲、毛里塔尼亚 |

**Core Points**:
- Earth divided into 4 quadrants matching 4 triplicities
- Each quadrant ruled by triplicity planets
- Regional characteristics derive from ruling planets
- Europe (Fire) = warlike, free; Asia (Earth) = religious, amorous
- N. Asia (Air) = learned, just; Libya (Water) = hot, magical

**Narrative Snippets**:
- `[ns_tetra_ii003]` `[trigger: regional_triplicities]` `[factor_trigger: astro_triplicity_region]` `[role: 主干]` World regions are assigned to triplicities—their characteristics derive from ruling planets. → Source Text II.3
- `[ns_tetra_ii004]` `[trigger: europe_fire]` `[factor_trigger: astro_triplicity_fire AND astro_region_europe]` `[role: 条件分支]` Europe belongs to Fire triplicity (Jupiter/Mars): inhabitants are warlike, lovers of freedom, imperious. → Source Text II.3"""
    normalized_text_zh: str = """"""
    subject: str = "Familiarity of Regions with Triplicities (Chapter III)"
    factor_refs: list = ['triplicity_region']
    
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
        l1_anchor="tb_v1.0.0_familiarity_of_regions_with_tr_001_L1",
    )
    version: str = "1.0.0"
