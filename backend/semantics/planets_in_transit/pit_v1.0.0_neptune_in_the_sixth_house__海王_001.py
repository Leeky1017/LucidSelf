"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272607
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
    semantic_id="pit_v1.0.0_neptune_in_the_sixth_house__海王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneInTheSixthHouse海王(SemanticEntry):
    """
    **Source Text** (Lines 16802-16834):
> Affects health and work very strongly. Be careful of health—m...
    """
    
    original_text: str = """**Source Text** (Lines 16802-16834):
> Affects health and work very strongly. Be careful of health—more subject to illnesses and infections. Usually no problems unless difficult transits simultaneously. Be careful of diseases from poisons and toxins, drugs or alcohol. May get strange ideas about nutrition and hygiene—total abstention diets. These not bad in themselves, but observe effects carefully, don't follow blindly. In area of work: best handled by working in social service field—with sick in hospitals/asylums or with poor. Not good time for advancing career for egotistical reasons—harder you work for own benefit, less you get. Can make great achievements only if working in spirit of service to others. May encounter serious misunderstanding with employers/employees. Path to advancement may be blocked mysteriously. May become involved in dishonest or subversive work without being aware. Effects minimized if regard work as service without worrying about what you'll get.

**English Paraphrase**: Health and work affected. Be careful—more susceptible to illness, toxins, drugs/alcohol. Strange diet ideas. Work best in social service. Egotistical career advancement doesn't work—service to others does. May have work misunderstandings or be mysteriously blocked. Could unknowingly be involved in dishonest work.

**Complete Chinese Interpretation**: 健康和工作受影响。小心——更容易患病、毒素、药物/酒精。奇怪的饮食想法。最好在社会服务工作。自私的职业晋升不奏效——服务他人才行。可能有工作误解或被神秘阻挡。可能不知不觉参与不诚实的工作。

**Narrative Snippets**:
- `[ns_pit_ne006]` `[trigger: neptune_transit_house_6]` `[factor_trigger: astro_transit_neptune AND astro_house_6]` `[role: 主干]` Health susceptible. Strange diet ideas. Work best as service. Ego-driven career doesn't work. → PIT Ch12 Neptune-6H"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune in the Sixth House (海王星过境第六宫)"
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
        l1_anchor="pit_v1.0.0_neptune_in_the_sixth_house__海王_001_L1",
    )
    version: str = "1.0.0"
