"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.093992
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
    semantic_id="tis_v1.0.0_third_house___perception___com_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class ThirdHousePerceptionCom(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| House of Perception | In...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| House of Perception | Info processing | Better name |
| Second World | Mental map | We live here |
| Perceptual Biases | Planetary filters | Distortion |
| Reality Testing | Communication purpose | Clarity |

#### Source Text

"Better name: House of Perception. Perception flows two ways: we gather information from the world, then echo it back again. There is a physical world around us. And within the brain we create a second world modeled on the first. That second world is the one we truly inhabit."

#### English Paraphrase

The **Third House** is the arena of **perception, communication, and the immediate environment**. It governs how we process information and construct our reality.

**The Loop of Perception**:
1.  **Input**: Gathering data from the world (listening, observing, reading).
2.  **Processing**: Creating an internal model of reality based on that data.
3.  **Output**: Expressing that internal model back to the world (speaking, writing, gesturing).

**The "Second World"**:
We don't live in the raw physical world; we live in our **mental map** of it. The Third House describes the quality and clarity of that map.

**Biases**:
Planets in the Third House create **perceptual biases**—filters that distort information. We see what we expect to see.

**Clarity**:
Achieving clarity requires **comparing notes** with others. We must communicate our perceptions and listen to theirs to correct our internal map. This is the true purpose of communication: reality testing.

**Curiosity**:
The engine of the Third House is curiosity—the urge to explore, name, and understand the environment.

#### Complete Chinese Interpretation

**第三宫**是**感知、沟通和直接环境**的领域。它掌管我们如何处理信息和构建我们的现实。

**感知的循环**：
1.  **输入**：从世界收集数据（倾听、观察、阅读）。
2.  **处理**：基于该数据建立现实的内在模型。
3.  **输出**：将该内在模型表达回世界（说话、写作、手势）。

**"第二世界"**：
我们不生活在原始的物理世界中；我们生活在我们对它的**心理地图**中。第三宫描述了那张地图的质量和清晰度。

**偏见**：
第三宫的行星创造**感知偏见**——扭曲信息的过滤器。我们看到我们期望看到的。

**清晰度**：
获得清晰度需要与他人**核对笔记**。我们必须沟通我们的感知并倾听他人的，以修正我们的内在地图。这是沟通的真正目的：现实测试。

**好奇心**：
第三宫的引擎是好奇心——探索、命名和理解环境的冲动。

#### Core Points

- House of Perception (Input/Processing/Output).
- We live in our mental map ("Second World"), not raw reality.
- Communication acts as reality testing/clarifying.
- Planetary filters create perceptual biases.
- East parallel: 兄弟宫/文昌/口才 (Siblings Palace, Intellect, Eloquence).

#### Detailed Explanation

The Third House governs how we **perceive and process** reality. Forrest's "Second World" concept is key: we don't live in raw reality but in a **mental map** we construct from sensory data. This map is always partial, always filtered through the planetary energies in our Third House.

Perception flows **two ways**: we gather information from the world (input), and we echo it back through communication (output). Speaking and writing aren't just expression—they're **reality testing**. By articulating our perceptions, we clarify them, discover their flaws, and refine our mental maps.

**Successful navigation** means developing accurate, flexible perception that can update based on new information. The person sees truth more clearly because they communicate openly and allow their views to be challenged. **Unsuccessful navigation** produces rigid mental maps, confirmation bias, and an inability to learn from feedback. The person confuses their map with the territory.

#### Narrative Snippets

- `[ns_innersky_h3_001]` `[trigger: house_3_general]` `[factor_trigger: astro_house_3]` `[role: 主干]` Let's call the third house the House of Perception, remembering always that perception flows two ways: we gather information from the world and then we echo it back again. → The Inner Sky Ch.7 #3H
- `[ns_innersky_h3_002]` `[trigger: house_3_second_world]` `[factor_trigger: astro_house_3]` `[role: 主干依赖]` There is a physical world around us. And within the neurons and synapses of the brain we create a second world modeled on the first. That second world is the one we truly inhabit. → The Inner Sky Ch.7 #3H
- `[ns_innersky_h3_003]` `[trigger: house_3_mastery]` `[factor_trigger: astro_house_3 AND astro_state_success]` `[role: 条件分支]` Those who have mastered that delicate art are masters of the third-house terrain. More than most of us, they see truth—the truth that is never in us, but always among us. → The Inner Sky Ch.7 #3H
- `[ns_innersky_h3_004]` `[trigger: house_3_dysfunction]` `[factor_trigger: astro_house_3 AND astro_state_dysfunction]` `[role: 条件分支]` Those whose passage through the third house has been a failure must live in a universe in which dreams, nightmares, and reality are forever shifting into one another. → The Inner Sky Ch.7 #3H
- `[ns_innersky_h3_005]` `[trigger: house_3_clarity]` `[factor_trigger: astro_house_3]` `[role: 总结]` To perceive clearly, the two worlds must be aligned. We can straighten out the distortions only by comparing notes with other perceivers. → The Inner Sky Ch.7 #3H"""
    normalized_text_zh: str = """"""
    subject: str = "Third House - Perception & Communication"
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_third_house___perception___com_001_L1",
    )
    version: str = "1.0.0"
