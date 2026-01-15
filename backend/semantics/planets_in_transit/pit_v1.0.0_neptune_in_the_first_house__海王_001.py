"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.272519
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
    semantic_id="pit_v1.0.0_neptune_in_the_first_house__海王_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class NeptuneInTheFirstHouse海王(SemanticEntry):
    """
    **Source Text** (Lines 16650-16680):
> For several years you will be changing ways of interacting wi...
    """
    
    original_text: str = """**Source Text** (Lines 16650-16680):
> For several years you will be changing ways of interacting with others. Self-knowledge difficult but essential. Chameleon phase—unintentionally present wide variety of faces. Learn who you are in your own terms. Changes may confuse you and others. Relationships difficult because people attract only to currently projected image. Just as you may confuse and delude others, they may do the same to you. Wary of weird schemes—sense of reality not at best. May operate idealistically—acting on what you want to be true. May stimulate compassion—take care of someone or work to help others. Tendency to want to save others—avoid improper dependency. May seek someone who seems stronger—danger of becoming permanently dependent.

**English Paraphrase**: Self-knowledge essential but difficult. Chameleon phase—many faces. Relationships confused by projections. Be wary of weird schemes—reality sense poor. May act idealistically. Compassion stimulated but avoid creating dependency.

**Complete Chinese Interpretation**: 自我认知必要但困难。变色龙阶段——多面。关系被投射混淆。警惕奇怪计划——现实感差。可能理想主义行事。同情心被激发但避免制造依赖。

**Narrative Snippets**:
- `[ns_pit_ne001]` `[trigger: neptune_transit_house_1]` `[factor_trigger: astro_transit_neptune AND astro_house_1]` `[role: 主干]` Self-knowledge essential. Chameleon phase. Reality sense poor. Compassion but avoid dependency. → PIT Ch12 Neptune-1H"""
    normalized_text_zh: str = """"""
    subject: str = "Neptune in the First House (海王星过境第一宫)"
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
        l1_anchor="pit_v1.0.0_neptune_in_the_first_house__海王_001_L1",
    )
    version: str = "1.0.0"
