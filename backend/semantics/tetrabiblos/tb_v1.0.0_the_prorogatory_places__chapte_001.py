"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192744
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
    semantic_id="tb_v1.0.0_the_prorogatory_places__chapte_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class TheProrogatoryPlacesChapte(SemanticEntry):
    """
    **Source Text** (Lines 5563-5598):
> Firstly, those places, only, are to be deemed prorogatory, to w...
    """
    
    original_text: str = """**Source Text** (Lines 5563-5598):
> Firstly, those places, only, are to be deemed prorogatory, to which the future assumption of the dominion of prorogation exclusively belongs. These several places are: the sign on the angle of the ascendant, from the fifth degree above the horizon to the twenty-fifth degree below it; the thirty degrees in dexter sextile thereto, constituting the eleventh house, called the Good Dæmon; the thirty degrees in dexter quartile, forming the mid-heaven above the earth; those in dexter trine making the ninth house, called God; and lastly, those in opposition, belonging to the angle of the west.

**English Paraphrase (Primary Language)**:
**Prorogatory places** are the five positions eligible to contain the life-giver (prorogator):

1. **Ascendant** (1st house): 5° above horizon to 25° below
2. **11th house** (Good Dæmon): Dexter sextile to ASC
3. **Mid-heaven** (10th): Dexter quartile to ASC—most powerful
4. **9th house** (God): Dexter trine to MC
5. **Descendant** (7th): Opposition to ASC

**Priority ranking**: MC > ASC > 11th > 7th > 9th

**Excluded places**: Everything under the earth except degrees ascending; the 12th house (Evil Dæmon) is excluded due to being cadent and having impaired beams.

**Complete Chinese Interpretation (Secondary Language)**:
**主限宫位**是五个可能包含生命主（主限星）的位置：

1. **上升点**（第1宫）：地平线上5°到下25°
2. **第11宫**（善精灵）：与上升的右六分
3. **中天**（第10宫）：与上升的右四分——最强大
4. **第9宫**（神）：与中天的右三分
5. **下降点**（第7宫）：与上升的对分

**优先级排序**：中天 > 上升 > 11宫 > 7宫 > 9宫

**排除位置**：地下一切，除了正在上升的度数；第12宫（恶精灵）因陷落和光线受损而被排除。

**Core Points**:
- Five prorogatory places only
- MC is most powerful, ASC second
- Degrees under earth generally excluded
- 12th house excluded due to cadency

**Narrative Snippets**:
- `[ns_tetra_iii023]` `[trigger: prorogatory_places]` `[factor_trigger: astro_house_prorogatory]` `[role: 主干]` Five prorogatory places: ASC, 11th, MC, 9th, 7th—MC is most powerful. → Source Text III.12
- `[ns_tetra_iii_pr]` `[trigger: priority]` `[factor_trigger: priority]` `[role: 条件分支]` Priority hierarchy of prorogatory places: MC is most potent, followed by ASC, 11th (Good Dæmon), 7th, and 9th. → Source Text III.12"""
    normalized_text_zh: str = """"""
    subject: str = "The Prorogatory Places (Chapter XII)"
    factor_refs: list = ['engine_id', 'house_prorogatory', 'astrology_classical', 'source_ref', 'rel_iii_023', 'astro_house_prorogatory', 'ranking', 'evi_iii_023', 'house_prorogatory', 'rule_prorogatory_places', 'concept_prorogatory', 'house_prorogatory', 'vital_center']
    
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
        l1_anchor="tb_v1.0.0_the_prorogatory_places__chapte_001_L1",
    )
    version: str = "1.0.0"
