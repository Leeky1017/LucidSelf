"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.498149
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
    semantic_id="acu_v1.0.0_393_395_精神的三个标志_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 393395精神的三个标志(SemanticEntry):
    """
    **原文** (§393-395, 行6007-6054):

> [393] The hallmarks of spirit are, firstly, the principle of spont...
    """
    
    original_text: str = """**原文** (§393-395, 行6007-6054):

> [393] The hallmarks of spirit are, firstly, the principle of spontaneous movement and activity; secondly, the spontaneous capacity to produce images independently of sense perception; and thirdly, the autonomous and sovereign manipulation of these images...
>
> [395] This brings us to a point we have not considered at all in the course of our observations so far. We have availed ourselves of cultural and everyday conceptions... But we have yet to consider that because of its original autonomy, about which there can be no doubt in the psychological sense, the spirit is quite capable of staging its own manifestations spontaneously.

**英文释义（主语言）**:

**精神的三个标志**：
1. **自发运动和活动的原理** - 主动性
2. **独立于感觉知觉自发产生图像的能力** - 想象力
3. **对这些图像的自主和主权操控** - 思维和理性

**精神的动态本质**：
按照其原始的风之本性，精神始终是主动的、有翅膀的、敏捷的存在，同时也是使万物有生气、刺激、激发、燃烧和启发的存在。用现代语言说，精神是**动态原理**，因此形成了与物质——其静止和惰性——的经典对立。

**精神的自主性**：
由于其原始的自主性（在心理学意义上毫无疑问），精神完全能够**自发地展示自己的显现**。这引出了精神在梦中的自我呈现问题。

**完整中文诠释（次语言）**:

**精神的三个本质标志**：
精神的标志首先是自发运动和活动的原理；其次是独立于感觉知觉自发产生图像的能力；第三是对这些图像的自主和主权操控。这个精神实体以外来物的方式接近原始人；但随着发展，它安居于人的意识中，成为从属功能，因此表面上丧失了其原始的自主性。

**精神与自然的对立**：
精神下降到人类意识领域表达于神圣努斯被自然拥抱的神话。这个持续数世纪的过程可能是不可避免的必然性，如果宗教相信可以阻止进化，就会发现自己处于非常孤立的境地。

**精神的危险**：
精神威胁天真者以膨胀，我们时代给出了最可怕的教训性例子。危险随着我们对外部对象的兴趣增加以及我们忘记与自然的分化关系应与对精神的相应分化关系齐头并进而增加。

**核心要点**:
- 精神三标志：自发运动、自发产像、自主操控
- 精神 = 动态原理 vs 物质 = 静止惰性
- 精神原初以外来物接近原始人
- 随发展安居于意识，表面丧失自主性
- 精神实际保持原始自主性
- 精神威胁天真者以膨胀

**叙事片段**:
- `[ns_cw9i_VI_393_001]` `[trigger: spirit_hallmarks]` `[factor_trigger: jung_spirit AND jung_characteristics]` `[role: 主干]` 精神三标志：自发运动、自发产像、自主操控——动态原理vs物质的静止惰性。→ §393"""
    normalized_text_zh: str = """"""
    subject: str = "§393-395 精神的三个标志"
    factor_refs: list = ['engine_id', 'spontaneous_movement', 'psych_semantic', 'spontaneous_images', 'psych_semantic', 'autonomous_manipulation', 'psych_semantic', 'dynamic_principle', 'psych_semantic']
    
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
        l1_anchor="acu_v1.0.0_393_395_精神的三个标志_001_L1",
    )
    version: str = "1.0.0"
