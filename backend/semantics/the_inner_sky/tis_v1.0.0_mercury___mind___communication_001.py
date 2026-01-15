"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.116140
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
    semantic_id="tis_v1.0.0_mercury___mind___communication_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class MercuryMindCommunication(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Mind Function | Thinking...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Mind Function | Thinking/knowing | Core role |
| Messenger | Translator | Mythology |
| Fastest Planet | Rapid thought | Nature |
| Retrograde | Inward innovation | Cycle |  

#### Source Text

"Mercury is the planet in charge of the library we keep in our heads. Its function is to think, to know, to deduce, to reason. No planet is closer to the sun than Mercury, and no planet moves with more alacrity. This is the planet of the mind, of the linear, logical functions."

#### English Paraphrase

**Mercury** represents the **mind function**—intelligence, communication, perception, and learning. It's the fastest-moving planet (88-day orbit), symbolizing the rapid-fire nature of thought.

**Primary Functions**:
- Intelligence: Thinking, knowing, reasoning, deducing
- Transmission: Talking, teaching, writing, expressing ideas
- Reception: Listening, learning, reading, observing
- Mental processing: Making sense of sensory input

**Mercury as Messenger**: In mythology, Mercury is messenger of gods—translating divine will into language. Psychologically, it translates unconscious/感觉 into conscious/思想.

**When Retrograde**: Mind turns inward, thinking becomes innovative but expression difficult

**Dysfunction**: Nervousness, rationalization, worry, hyperactivity, chattering, intellectualism

**Feeding**: Mercury in Fire signs needs philosophical thought; Earth signs need practical problem-solving; Air signs need abstract concepts; Water signs need emotional intelligence

#### Complete Chinese Interpretation

**水星**代表**心智功能**——智力、沟通、感知和学习。它是最快行星（88天轨道），象征思想的快速发射本质。

**主要功能**：智力（思考、知道、推理、推演）、传输（说话、教学、写作、表达想法）、接收（倾听、学习、阅读、观察）、心智处理（理解感官输入）

**水星作为信使**：神话中水星是诸神信使——将神圣意志译成语言。心理上，它将无意识/感觉译成有意识/思想。

**逆行时**：心智转向内，思维变创新但表达困难

**功能失调**：紧张、合理化、担忧、过度活跃、喋喋不休、智识主义

**喂养**：火象水星需哲学思考；土象需实际问题解决；风象需抽象概念；水象需情感智力

#### Core Points

- Mercury = mind/communication function
- Fastest planet = rapid thought speed
- Messenger = translator (unconscious → conscious)
- Retrograde = inward innovative thinking
- East parallel: Mercury ≈ 伤官/食神 (expressive intelligence)

#### Detailed Explanation

Mercury governs the **mind, thought, and communication**—the linear, logical functions that organize information. As the fastest planet and closest to the Sun, it symbolizes the **rapid-fire nature of thought**: intelligence, perception, learning, and the constant chatter of the mental faculty.

Mythologically, Mercury is the **messenger of the gods**—translator between divine and human realms. Psychologically, this means translating **unconscious feeling into conscious thought**, making the inarticulate articulable. Mercury bridges inner knowing and outer expression.

**Mercury retrograde** (appearing to move backward) creates **inward-directed thinking**—innovative, unconventional, but sometimes difficult to communicate. The person may seem to think "differently" because their mental process runs against conventional logic.

#### Narrative Snippets

- `[ns_innersky_mercury_001]` `[trigger: planet_mercury]` `[factor_trigger: planet_mercury AND mercury_mind_function]` `[role: 主干]` Mercury is the planet in charge of the library we keep in our heads. Its function is to think, to know, to deduce, to reason. This is the planet of the mind, of the linear, logical functions. → The Inner Sky Ch.6 #Mercury
- `[ns_innersky_mercury_002]` `[trigger: planet_mercury AND astro_function]` `[factor_trigger: astro_planet_mercury]` `[role: 主干依赖]` No planet is closer to the sun than Mercury, and no planet moves with more alacrity. It symbolizes the rapid-fire nature of thought—intelligence, communication, perception, and learning. → The Inner Sky Ch.6 #Mercury
- `[ns_innersky_mercury_003]` `[trigger: planet_mercury AND astro_messenger]` `[factor_trigger: astro_planet_mercury]` `[role: 条件分支]` Mercury is messenger of gods—translating divine will into language. Psychologically, it translates unconscious feeling into conscious thought. → The Inner Sky Ch.6 #Mercury
- `[ns_innersky_mercury_004]` `[trigger: planet_mercury AND astro_shadow]` `[factor_trigger: astro_planet_mercury AND astro_state_dysfunction]` `[role: 总结]` Dysfunction: nervousness, rationalization, worry, hyperactivity, chattering, intellectualism—mind running without purpose. → The Inner Sky Ch.6 #Mercury
- `[ns_innersky_mercury_005]` `[trigger: mercury_retrograde]` `[factor_trigger: retrograde_state AND mercury_mind_function]` `[role: 条件分支]` Mercury retrograde creates inward-directed thinking—innovative, unconventional, but sometimes difficult to communicate. The mental process runs against conventional logic. → The Inner Sky Ch.6 #Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Mercury - Mind & Communication"
    factor_refs: list = ['planet_mercury', 'mercury_mind_function', 'new_candidate', 'retrograde_state']
    
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
        l1_anchor="tis_v1.0.0_mercury___mind___communication_001_L1",
    )
    version: str = "1.0.0"
