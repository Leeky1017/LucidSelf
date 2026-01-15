"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.206623
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
    semantic_id="pit_v1.0.0_uranus_in_the_fourth_house__天王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class UranusInTheFourthHouse天王(SemanticEntry):
    """
    **Source Text** (Lines 14524-14556):
> Focus on most personal and intimate aspects—home, parents, fa...
    """
    
    original_text: str = """**Source Text** (Lines 14524-14556):
> Focus on most personal and intimate aspects—home, parents, family. May be upsets showing where life needs change, but acquire new sense of freedom from influence of past. Common effect: sudden change in home environment or complete change of residence. Settled family life may be threatened by divorce, accident, death. Deepest aspects no longer reliable. Fourth house rules ultimate basis of being. Changes extremely upsetting—must be flexible. Old ties with past may be broken—lose roots but gain freedom from enslaving patterns. Problems and tensions surface and must be handled. Living conditions may change and take years to settle. At deepest level, changes in unconscious mind—whole experience of world quite different after.

**English Paraphrase**: Focus on home/family. Upsets show where change needed. May move or change residence. Family life threatened. Deep basis of being challenged. Old ties broken—lose roots, gain freedom. Problems surface. Unconscious mind changes.

**Complete Chinese Interpretation**: 聚焦家庭/家人。动荡显示哪里需要改变。可能搬家或改变住所。家庭生活受威胁。存在的深层基础受挑战。旧纽带断裂——失去根基，获得自由。问题浮出水面。无意识心灵改变。

**Narrative Snippets**:
- `[ns_pit_ur004]` `[trigger: uranus_transit_house_4]` `[factor_trigger: astro_transit_uranus AND astro_house_4]` `[role: 主干]` Home/family focus. May move. Old ties broken. Problems surface. Deep unconscious changes. → PIT Ch11 Uranus-4H"""
    normalized_text_zh: str = """"""
    subject: str = "Uranus in the Fourth House (天王星过境第四宫)"
    factor_refs: list = []
    
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_uranus_in_the_fourth_house__天王_001_L1",
    )
    version: str = "1.0.0"
