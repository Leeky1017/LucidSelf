"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.169590
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
    semantic_id="tb_v1.0.0_travelling__chapter_viii_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TravellingChapterViii(SemanticEntry):
    """
    **Source Text** (Lines 7872-7937):
> The circumstances indicative of travel are to be considered by ...
    """
    
    original_text: str = """**Source Text** (Lines 7872-7937):
> The circumstances indicative of travel are to be considered by means of the situation held by both the luminaries, in respect to the angles... should she be descending, or cadent from the angles, she will cause journeys and changes of residence.

**English Paraphrase (Primary Language)**:
**Travel** is indicated by:
- **Moon cadent** from angles = journeys and relocations
- **Mars cadent** from zenith, in quartile/opposition to luminaries = same
- **Part of Fortune** in travel-producing signs

**Quality of travel**:
- Benefics supervising = honorable, profitable, safe return
- Malefics supervising = perilous, fruitless, difficult return

**Direction of travel**:
- Luminaries in oriental/cadent houses = east or south
- Luminaries in occidental = north or west

**Frequency**:
- Single-form signs = occasional travel
- Bicorporeal signs = constant travel

**Dangers**:
- Saturn/Mars in watery signs = shipwreck
- In fixed signs = precipices, winds
- In tropical = lack of necessities
- In human signs = robbery
- In terrestrial = wild beasts

**Complete Chinese Interpretation (Secondary Language)**:
**旅行**由以下指示：
- **月亮果宫**于角宫 = 旅行和搬迁
- **火星果宫**于天顶，与发光体四分/对分 = 同样
- **福点**在产生旅行的星座

**旅行质量**：
- 吉星监督 = 尊贵、有利、安全返回
- 凶星监督 = 危险、无果、艰难返回

**旅行方向**：
- 发光体在东方/果宫 = 东或南
- 发光体在西方 = 北或西

**Core Points**:
- Moon/Mars cadent = travel indicated
- Benefics = safe, profitable; Malefics = dangerous
- Sign type determines travel frequency and dangers
- Direction from luminary position

**Narrative Snippets**:
- `[ns_tetra_iv012]` `[trigger: travel_indicated]` `[factor_trigger: astro_moon_cadent]` `[role: 主干]` Travel is indicated when Moon is cadent from angles or Part of Fortune is in travel-producing signs. → Source Text IV.8
- `[ns_tetra_iv023]` `[trigger: travel_safety]` `[factor_trigger: astro_benefic AND astro_malefic]` `[role: 条件分支]` Benefics supervising = honorable, profitable, safe return; malefics = perilous, fruitless, difficult return. → Safety
- `[ns_tetra_iv024]` `[trigger: travel_danger]` `[factor_trigger: astro_saturn AND astro_mars AND astro_sign]` `[role: 条件分支]` Saturn/Mars in watery signs = shipwreck; in fixed = precipices; in human = robbery; in terrestrial = wild beasts. → Dangers
- `[ns_tetra_iv_to]` `[trigger: travel_outcome]` `[factor_trigger: travel_outcome]` `[role: 效果]` Travel outcome: safe and profitable if benefics supervise; dangerous and fruitless if malefics supervise. → Source Text IV.8
- `[ns_tetra_iv_bs]` `[trigger: benefic_supervise]` `[factor_trigger: benefic_supervise]` `[role: 条件分支]` Benefic supervision (Jupiter/Venus aspecting travel indicators) produces honorable, profitable journeys with safe return. → Source Text IV.8"""
    normalized_text_zh: str = """"""
    subject: str = "Travelling (Chapter VIII)"
    factor_refs: list = ['travel_indicator', 'new_candidate']
    
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
        l1_anchor="tb_v1.0.0_travelling__chapter_viii_001_L1",
    )
    version: str = "1.0.0"
