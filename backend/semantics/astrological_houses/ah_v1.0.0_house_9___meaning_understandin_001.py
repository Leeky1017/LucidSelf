"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333779
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
    semantic_id="ah_v1.0.0_house_9___meaning_understandin_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class House9MeaningUnderstandin(SemanticEntry):
    """
    #### Source Text

"The ninth house experiences are those encountered by an individual in the search ...
    """
    
    original_text: str = """#### Source Text

"The ninth house experiences are those encountered by an individual in the search for the meaning of things. It refers to matters which enable partnerships and group activity to operate successfully and expand within the framework of society and culture. This requires knowledge of over-all conditions, procedures, and laws. The ninth house is traditionally the house of philosophy and religion, dealing with legal matters, long journeys, contacts with other cultures, and 'great dreams' revealing meaning. Understanding is a holistic process implying the experience of a people and their culture. The danger is over-expansion caused by ambition and greed for power."

#### English Paraphrase (Primary Language)

The ninth house represents the search for meaning that enables relationship and society to function coherently. While the third house deals with empirical "how to" knowledge, the ninth house concerns holistic understanding—seeing parts in relation to the whole. Philosophy, religion, law, and higher education all belong here because they provide the conceptual frameworks through which society operates. This is also the house of symbol and interpretation—all words, gestures, and artistic expressions are symbols requiring interpretation. Great dreams and visionary experiences belong here as communications from the universal to the particular. The danger is ambition—using knowledge for ego-expansion and power accumulation rather than service to the whole.

#### Complete Chinese Interpretation (Secondary Language)

第九宫代表使关系和社会能够连贯运作的意义追寻。第三宫处理经验性的"如何做"知识，第九宫则关注整体性理解——看到部分与整体的关系。

**第三宫vs第九宫**：
- **第三宫**：知道（直接接触）、经验性、实用性
- **第九宫**：理解（综合）、整体性、象征性

哲学、宗教、法律和高等教育都属于这里，因为它们提供社会运作的概念框架。这也是象征和解释之宫——所有词语、手势和艺术表达都是需要解释的象征。伟大的梦境和幻象经验属于这里，作为从普遍到特殊的沟通。危险是野心——利用知识进行自我扩张和权力积累，而不是服务于整体。

#### Core Points

- **Meaning search**: Understanding that enables society to function
- **Holistic process**: Seeing parts in relation to whole (vs third house empiricism)
- **Symbolic realm**: All communication is symbol requiring interpretation
- **Legal framework**: Laws as symbolic expression of collective togetherness
- **Great dreams**: Visionary communications from universal to particular
- **Ambition danger**: Knowledge for ego-power rather than service

#### Narrative Snippets

- `[ns_houses_h9_001]` `[trigger: house_9]` `[factor_trigger: house_9 AND whole]` `[role: 主干]` Ninth house experiences are those encountered in the search for the meaning of things—understanding is a holistic process implying the experience of a people and their culture. → House 9 Source
- `[ns_houses_h9_002]` `[trigger: house_9 AND astro_symbol]` `[factor_trigger: house_9 AND dharma]` `[role: 条件分支]` The ninth house is the house of symbols—all words, gestures, and artistic expressions are symbols requiring interpretation against cultural background. → House 9 Source"""
    normalized_text_zh: str = """"""
    subject: str = "House 9 - Meaning/Understanding (Cadent)"
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
        book_id="astrological_houses",
        chapter="",
        l1_anchor="ah_v1.0.0_house_9___meaning_understandin_001_L1",
    )
    version: str = "1.0.0"
