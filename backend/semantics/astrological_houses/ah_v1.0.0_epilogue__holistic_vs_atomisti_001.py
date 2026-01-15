"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333923
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
    semantic_id="ah_v1.0.0_epilogue__holistic_vs_atomisti_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class EpilogueHolisticVsAtomisti(SemanticEntry):
    """
    #### Source Text

"I have stressed the difference between an 'atomistic' and a 'holistic' approach t...
    """
    
    original_text: str = """#### Source Text

"I have stressed the difference between an 'atomistic' and a 'holistic' approach to astrology. The issue that cannot be dismissed is whether man's consciousness interprets his experiences most significantly in relation to a whole, on the parts of which these experiences throw some significant light, or as separate facts about which only close analysis can give us valid knowledge. Astrologically speaking, can we really understand a birth chart and the total person it represents if we assign definite meanings to each planet, each sign, each house, each aspect—considered as a separate factor? Should we first analyze, then try to piece together the data, or should we approach the chart first as a whole having a definite 'form' and consider it a complex 'word' that can reveal 'meaning' to us?"

#### English Paraphrase (Primary Language)

Rudhyar's epilogue addresses the fundamental methodological question in astrology—and indeed in all interpretation: should we begin with parts and synthesize, or begin with the whole and differentiate? The atomistic approach treats each factor (planet, sign, house, aspect) as a separate entity with fixed meaning, then attempts synthesis. The holistic approach perceives the chart first as a unified "form"—a complex word revealing meaning—then analyzes parts in context of the whole.

This connects to a deeper philosophical issue: viewing existence as permanent entities vs phases of cyclic processes. The Buddha's teaching that a person is "the integration of many constantly changing factors" within a "wheel of existence" parallels modern atomic physics where the electron is particle or wave depending on conditions. Houses exist in space as archetypal potentialities, but require time for actualization. Space represents potential; time actualizes potential through experience. This existential understanding—that it takes time to become conscious of all implications of existence in surrounding space—is the foundation of Rudhyar's person-centered astrology.

#### Complete Chinese Interpretation (Secondary Language)

鲁迪亚的结语探讨占星学——以及所有解释——中的根本方法论问题：应该从部分开始综合，还是从整体开始分化？

**两种方法的对比**：

| 方面 | 原子论方法 | 整体论方法 |
|------|----------|----------|
| 起点 | 分离的部分 | 统一的整体 |
| 过程 | 分析→综合 | 感知→分化 |
| 对象 | 固定意义的实体 | 过程的阶段 |
| 隐喻 | 机器零件 | 有机"词语" |

**更深层的哲学问题**：
- 将存在视为永久实体 vs 循环过程的阶段
- 佛陀的教导：人是"存在之轮"内"许多不断变化因素的整合"
- 现代原子物理学：电子依条件是粒子或波

**宫位的存在论**：
- 宫位作为原型潜能存在于空间中
- 需要时间来实现这些潜能
- 空间 = 潜能；时间 = 通过经验实现潜能

这种存在主义理解——在周围空间中意识到存在的所有含义需要时间——是鲁迪亚以人为中心占星学的基础。

#### Core Points

- **Atomistic vs holistic**: Parts→synthesis vs whole→differentiation
- **Entity vs process**: Permanent things vs phases of cycles
- **Buddhist parallel**: Person as integration of changing factors in wheel of existence
- **Space-time relationship**: Space = potential, time = actualization
- **Chart as word**: Complex symbol revealing meaning, not collection of parts
- **Person-centered**: Individual's relationship to universe at birth moment

#### Narrative Snippets

- `[ns_houses_036]` `[trigger: methodology]` `[factor_trigger: astro_interpretation_approach]` `[role: 主干]` Should we approach the chart first as a whole having a definite 'form'—a complex 'word' revealing meaning—or assign definite meanings to each factor considered separately? → Epilogue
- `[ns_houses_037]` `[trigger: space_time]` `[factor_trigger: astro_existence_potential]` `[role: 总结]` Houses exist in space as archetypal potentialities, but require time for actualization—space represents potential; time actualizes through experience. → Epilogue"""
    normalized_text_zh: str = """"""
    subject: str = "Epilogue: Holistic vs Atomistic Approach"
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
        l1_anchor="ah_v1.0.0_epilogue__holistic_vs_atomisti_001_L1",
    )
    version: str = "1.0.0"
