"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.497953
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
    semantic_id="acu_v1.0.0_385_388__精神_概念的语义分析_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 385388精神概念的语义分析(SemanticEntry):
    """
    **原文** (§385-388, 行5870-5924):

> [385] The word "spirit" possesses such a wide range of application...
    """
    
    original_text: str = """**原文** (§385-388, 行5870-5924):

> [385] The word "spirit" possesses such a wide range of application that it requires considerable effort to make clear to oneself all the things it can mean. Spirit, we say, is the principle that stands in opposition to matter...
>
> [388] This score or so of meanings and shades of meaning attributable to the word "spirit" make it difficult for the psychologist to delimit his subject conceptually, but on the other hand they lighten the task of describing it, since the many different aspects go to form a vivid and concrete picture of the phenomenon in question.

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Spirit (精神) | 灵/气 | 物质对立面 | 多义词 |
| Pneuma (πνεῦμα) | 气息/风 | 灵性原理 | 希腊语 |
| Anima/Animus | 灵魂 | 风/气 | 拉丁语 |
| Geist | 精神 | 发酵/泡沫 | 德语 |

**英文释义（主语言）**:

**"精神"的广泛应用**：
"精神"一词拥有如此广泛的应用范围，需要相当的努力才能弄清它可能意味的一切。

**精神的主要意义层次**：
1. **与物质对立的原理** - 非物质实体
2. **生命原理** - 活力、生气
3. **态度或倾向** - 如"战斗精神"
4. **时代精神** - 集体观点和行动的原则
5. **客观精神** - 文化财产的总和
6. **鬼魂/幽灵** - 死者的灵魂

**语言学渊源**：
- **Psyche (ψυχή)** 与 **psychos/psycros (ψυχός/ψῡχος)** 相关 = "冷"
- **Pneuma (πνεῦμα)** 原义 = "运动中的空气"
- **Anima/Animus** 与 **anemos (ἄνεμος)** 相关 = "风"
- **Geist** 与泡沫(Gischt)、酵母(Gäscht)、ghost相关

**完整中文诠释（次语言）**:

**"精神"的语义复杂性**：
"精神"一词拥有如此广泛的应用范围，需要相当的努力才能弄清它可能意味的一切。这二十多种意义和意义阴影使心理学家难以在概念上界定其主题，但另一方面也减轻了描述它的任务，因为这些不同方面形成了所讨论现象的生动具体画面。

**精神的原始含义**：
精神最初被感受为看不见的、类似呼吸的"存在"。威廉·詹姆斯在《宗教经验的种类》中生动描述了这种原初现象。五旬节奇迹的风也是例子。原始心智很自然地将这种看不见的存在人格化为鬼魂或精灵。

**核心要点**:
- 精神 = 多义词，约20种意义和阴影
- 主要意义：物质对立面、生命原理、态度、时代精神、客观精神、鬼魂
- 语言学：与冷、风、气息、发酵相关
- 原始感受：看不见的、呼吸般的存在
- 情感被视为附身（被精灵占据）

**叙事片段**:
- `[ns_cw9i_VI_385_001]` `[trigger: spirit_meanings]` `[factor_trigger: jung_spirit AND jung_semantics]` `[role: 主干]` "精神"=多义词，约20种意义——物质对立面、生命原理、态度、时代精神、客观精神、鬼魂。→ §385-388"""
    normalized_text_zh: str = """"""
    subject: str = "§385-388 "精神"概念的语义分析"
    factor_refs: list = ['engine_id', 'spirit', 'psych_semantic', 'spirit_vs_matter', 'psych_semantic', 'life_principle', 'psych_semantic', 'wind_breath', 'psych_semantic']
    
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_385_388__精神_概念的语义分析_001_L1",
    )
    version: str = "1.0.0"
