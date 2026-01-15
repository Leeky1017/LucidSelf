"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.169570
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
    semantic_id="tb_v1.0.0_children__chapter_vi_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ChildrenChapterVi(SemanticEntry):
    """
    **Source Text** (Lines 7645-7728):
> The Moon, Jupiter, and Venus are esteemed as givers of offsprin...
    """
    
    original_text: str = """**Source Text** (Lines 7645-7728):
> The Moon, Jupiter, and Venus are esteemed as givers of offspring; but the Sun, Mars, and Saturn are considered as denying children altogether, or as allowing but few... if prolific signs, such as Pisces, Cancer, and Scorpio, they will grant twins, or even more.

**English Paraphrase (Primary Language)**:
**Children** are judged from:
- **Mid-heaven** and **11th house** (Good Dæmon)
- Planets configurated with these places

**Child-giving planets**: Moon, Jupiter, Venus
**Child-denying planets**: Sun, Saturn, Mars
**Mercury**: Common—gives when oriental, denies when occidental

**Number of children**:
- Single = planets in signs of single form
- Twins/more = planets in bicorporeal or prolific signs (Pisces, Cancer, Scorpio)

**Health of children**:
- Benefics ruling = healthy, long-lived
- Malefics ruling = sickly, short-lived
- Malefics elevated over child-givers = children die young

**Complete Chinese Interpretation (Secondary Language)**:
**子女**从以下判断：
- **中天**和**第11宫**（善精灵）
- 与这些位置配置的行星

**赐子行星**：月亮、木星、金星
**无子行星**：太阳、土星、火星
**水星**：共通——东方时赐，西方时拒

**子女数量**：
- 单一 = 行星在单形星座
- 双胞胎/更多 = 行星在双体或多产星座（双鱼、巨蟹、天蝎）

**子女健康**：
- 吉星主宰 = 健康、长寿
- 凶星主宰 = 多病、短命
- 凶星高居于赐子星之上 = 子女夭折

**Core Points**:
- MC and 11th house = children places
- Moon/Jupiter/Venus = child-givers; Sun/Saturn/Mars = deniers
- Prolific signs = twins or more
- Malefics afflicting = sickly or dying children

**Narrative Snippets**:
- `[ns_tetra_iv009]` `[trigger: children_givers]` `[factor_trigger: astro_planet_fertile]` `[role: 主干]` Moon, Jupiter, and Venus are child-giving planets; Sun, Saturn, Mars deny or limit offspring. → Source Text IV.6
- `[ns_tetra_iv010]` `[trigger: prolific_signs]` `[factor_trigger: astro_sign_prolific]` `[role: 条件分支]` Prolific signs (Pisces, Cancer, Scorpio) indicate twins or multiple children. → Source Text IV.6
- `[ns_tetra_iv020]` `[trigger: children_health]` `[factor_trigger: astro_benefic AND astro_malefic]` `[role: 条件分支]` Benefics ruling children places = healthy, long-lived; malefics elevated = sickly or die young. → Health
- `[ns_tetra_iv_co]` `[trigger: children_outcome]` `[factor_trigger: children_outcome]` `[role: 效果]` Children outcome: many/healthy if fertile planets (Moon/Jupiter/Venus) in 11th/MC; few/sickly if barren planets (Sun/Saturn/Mars). → Source Text IV.6
- `[ns_tetra_iv_pb]` `[trigger: planet_barren]` `[factor_trigger: planet_barren]` `[role: 条件分支]` Barren planets (Sun, Saturn, Mars) deny children or grant few—especially when in MC or 11th house. → Source Text IV.6"""
    normalized_text_zh: str = """"""
    subject: str = "Children (Chapter VI)"
    factor_refs: list = ['planet_fertile', 'sign_prolific']
    
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
        l1_anchor="tb_v1.0.0_children__chapter_vi_001_L1",
    )
    version: str = "1.0.0"
