"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.169522
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
    semantic_id="tb_v1.0.0_rank_and_dignity__chapter_ii_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class RankAndDignityChapterIi(SemanticEntry):
    """
    **Source Text** (Lines 7250-7350):
> The inquiry into the degree of dignity, in any nativity, is to ...
    """
    
    original_text: str = """**Source Text** (Lines 7250-7350):
> The inquiry into the degree of dignity, in any nativity, is to be accomplished by means of the situation of the luminaries, and the familiarity subsisting between them and their attendant stars... If both luminaries be in masculine signs, and either both or one of them angular, especially if also attended by the five planets in glory, the persons then born will be kings.

**English Paraphrase (Primary Language)**:
**Rank and dignity** are determined by:

1. **Luminaries** (Sun and Moon) in masculine/feminine signs
2. **Angular positions** of luminaries
3. **Doryphory** (attendant planets) of luminaries

**Royal nativity** indicators:
- Both luminaries in masculine signs
- Both or one angular
- Attended by all five planets in dignity
- Fixed stars of first magnitude rising

**Noble but not royal**:
- Luminaries angular but not all planets attending
- Some planets in dignity, others not

**Common nativity**:
- Luminaries cadent or afflicted
- Malefics elevated over luminaries
- No planetary attendance

**Complete Chinese Interpretation (Secondary Language)**:
**地位与尊贵**由以下决定：

1. **发光体**（太阳和月亮）在阳/阴性星座
2. **发光体的角宫位置**
3. **发光体的护卫星**

**王室本命**指标：
- 两发光体都在阳性星座
- 两者或其一在角宫
- 五颗行星都以尊贵伴随
- 一等恒星升起

**贵族但非王室**：
- 发光体在角宫但非所有行星伴随
- 一些行星有尊贵，其他没有

**平民本命**：
- 发光体果宫或受刑
- 凶星高居于发光体之上
- 无行星伴随

**Core Points**:
- Luminaries in masculine signs + angular = high rank
- Full doryphory (all planets attending) = kingship
- Partial doryphory = nobility
- No doryphory, cadent luminaries = common status
- Fixed stars of first magnitude add eminence

**Narrative Snippets**:
- `[ns_tetra_iv003]` `[trigger: rank_dignity]` `[factor_trigger: astro_luminary_angular AND house_angular]` `[role: 主干]` Rank is determined by the luminaries' angular position and their planetary attendants. → Source Text IV.2
- `[ns_tetra_iv004]` `[trigger: royal_nativity]` `[factor_trigger: astro_doryphory_complete]` `[role: 条件分支]` Royal nativity: both luminaries in masculine signs, angular, attended by all five planets in dignity. → Source Text IV.2
- `[ns_tetra_iv_sm]` `[trigger: sun_moon]` `[factor_trigger: sun_moon]` `[role: 主干]` Sun and Moon together (luminaries) are primary rank indicators—their angular position and planetary attendants determine eminence. → Source Text IV.2
- `[ns_tetra_iv_ro]` `[trigger: rank_outcome]` `[factor_trigger: rank_outcome]` `[role: 效果]` Rank outcome ranges from kingship (full doryphory) through nobility (partial) to common status (none). → Source Text IV.2"""
    normalized_text_zh: str = """"""
    subject: str = "Rank and Dignity (Chapter II)"
    factor_refs: list = ['doryphory', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="tb_v1.0.0_rank_and_dignity__chapter_ii_001_L1",
    )
    version: str = "1.0.0"
