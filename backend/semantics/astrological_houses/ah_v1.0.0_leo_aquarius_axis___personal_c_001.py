"""
Auto-generated semantic module for astrological_houses
Generated at: 2025-12-05T13:30:20.333891
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
    semantic_id="ah_v1.0.0_leo_aquarius_axis___personal_c_001",
    book_id="astrological_houses",
    engine_id="astro"
)
class LeoAquariusAxisPersonalC(SemanticEntry):
    """
    #### Source Text

"The Leo rising individual has to impose his desire for self-projection upon whate...
    """
    
    original_text: str = """#### Source Text

"The Leo rising individual has to impose his desire for self-projection upon whatever materials are necessary. When these materials are other human beings, the Leo person becomes the man who has to lead. But this intense desire for self-projection is rooted in the fact that the individual is not sure of what he essentially is—he has to prove himself to himself. When Aquarius is rising, the individual identifies spontaneously with his culture and great dreams of reform, challenging old structures, pioneering for a New Age. Then he will seek partners who will cooperate either in cultural play or in reform and revolutionary activities."

#### English Paraphrase (Primary Language)

The Leo/Aquarius axis represents the polarity between personal creative expression and collective cultural/reforming vision. Leo rising creates intense need for self-projection—seeking mirrors (creations, children, performances) to discover identity. But this grand gesture compensates for inner uncertainty about essential nature. The Leo person must handle Aquarian symbols, words, and concepts to express their unclear self. When Aquarius rises, the individual identifies with culture, dreams of reform, New Age pioneering. These partnerships may have very emotional character because they demand wholehearted cooperation. The axis represents the fifth house (personal creation) / eleventh house (collective vision) polarity: creation OF the individual vs creation THROUGH the individual.

#### Complete Chinese Interpretation (Secondary Language)

狮子/水瓶轴代表个人创造性表达与集体文化/改革愿景之间的极性。

**狮子上升**：
- 强烈需要自我投射——寻找镜子（创作、孩子、表演）来发现身份
- 这种宏大姿态补偿了对本质自然的内在不确定性
- 必须处理水瓶式的符号、词语和概念来表达其不清晰的自我
- 需要领导，需要看到他人对自己的反应

**水瓶上升**：
- 自发地与文化、改革梦想、新时代先驱认同
- 挑战旧结构，为集体愿景工作
- 寻求在文化游戏或改革/革命活动中合作的伙伴
- 这些伙伴关系可能具有非常情感化的特征，因为要求全心全意的合作

**轴线的核心张力**：
- 个人创造vs通过个人的创造
- 第五宫（个人创作）vs第十一宫（集体愿景）
- 自我表达vs社会改革
- 内在不确定vs外在投射

#### Core Points

- **Fixed signs**: Concentration of creative or social energy
- **Leo rising**: Self-projection need, seeking mirrors for identity
- **Compensatory gesture**: Grand display masks inner uncertainty
- **Aquarius rising**: Cultural identification, reform dreams, New Age pioneering
- **Leo partner needed**: Emotional, wholehearted cooperation
- **Core polarity**: Personal creation vs collective channel"""
    normalized_text_zh: str = """"""
    subject: str = "Leo/Aquarius Axis - Personal Creation vs Collective Vision"
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
        l1_anchor="ah_v1.0.0_leo_aquarius_axis___personal_c_001_L1",
    )
    version: str = "1.0.0"
