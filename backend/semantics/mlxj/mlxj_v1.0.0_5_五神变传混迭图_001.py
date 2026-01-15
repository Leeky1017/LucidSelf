"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.789189
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
    semantic_id="mlxj_v1.0.0_5_五神变传混迭图_001",
    book_id="mlxj",
    engine_id="dream"
)
class 5五神变传混迭图(SemanticEntry):
    """
    #### 原文（source_text）

凡人寝卧，魂藏于肝，肝为诸神之主，故梦中所形，千变万化，错综混迭，不可思议，而一以肝神平寔为吉，故或生中克，或克中生，或生生而复克，或克克而复生，要以始终肝...
    """
    
    original_text: str = """#### 原文（source_text）

凡人寝卧，魂藏于肝，肝为诸神之主，故梦中所形，千变万化，错综混迭，不可思议，而一以肝神平寔为吉，故或生中克，或克中生，或生生而复克，或克克而复生，要以始终肝属者，则定夫生克焉。

甚有一梦所见，事事物物，皆形于本脏之神所属者，此又非得以生克之道推之也。甚有两神相生而反凶，两神相克而反吉者，宜以所梦事物机兆何如，以为详察，切勿拘一。

甚有颠倒紊乱，幻恍莫倪者，此必精神散杂，气血虚实所致，又不可以五神传见之常论尔。

#### 规范化释义（primary_lang_explained）

人睡眠时，魂藏于肝，肝为诸神之主，故梦中所现千变万化、错综混迭、不可思议。判断吉凶的关键是「肝神平实为吉」。可能出现生中有克、克中有生、生生复克、克克复生等复杂情况，关键看梦境始终是否归于肝属。

有些梦中事事物物都属于同一脏神，不能用生克之道推断。有些两神相生反凶、两神相克反吉，需详察梦中事物的具体机兆，不可拘泥。

有些梦颠倒紊乱、幻恍莫测，这是精神散杂、气血虚实失调所致，不能用五神传变的常规理论来解释。

#### 核心要点

- 肝为诸神之主，魂藏于肝
- 肝神平实为吉的核心原则
- 生克可互相转化
- 同脏梦不用生克推断
- 相生反凶、相克反吉的例外情况
- 精神散杂者的梦不适用常规理论"""
    normalized_text_zh: str = """"""
    subject: str = "5 五神变传混迭图"
    factor_refs: list = ['source_ref']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_5_五神变传混迭图_001_L1",
    )
    version: str = "1.0.0"
