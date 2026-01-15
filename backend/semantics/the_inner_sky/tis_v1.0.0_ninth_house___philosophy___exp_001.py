"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.122587
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
    semantic_id="tis_v1.0.0_ninth_house___philosophy___exp_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class NinthHousePhilosophyExp(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Mental Model | Arbitrary...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Mental Model | Arbitrary worldview | What we carry |
| Stereo Consciousness | Multiple perspectives | Goal |
| Room for Miraculous | Openness | Success |
| Dogmatism Risk | Model=Truth error | Danger |

#### Source Text

"All our views of reality are conditioned by an unspoken model of the world—and that model is always arbitrary and limiting. Ninth-house experience stretches the fabric of one's being. We must make room in our lives for the inexplicable. Room for the miraculous."

#### English Paraphrase

The **Ninth House** is the arena of **meaning, worldview, and expansion**. It governs the search for truth and the breaking of routine.

**Models of Reality**:
We all carry a mental model of the world (values, assumptions). The Ninth House challenges us to realize this is **just a model**, not absolute truth.

**Breaking Patterns**:
- **Travel**: Exposing ourselves to alien cultures to shatter our cultural conditioning.
- **Higher Education**: Expanding the mind with new concepts.
- **Philosophy/Religion**: Seeking the "Why" behind existence.

**The Goal**:
To replace a rigid, mechanical worldview with a fluid, evolving understanding. To maintain **"stereo consciousness"**—the ability to see truth from multiple perspectives.

**The Risk**:
- **Dogmatism**: Mistaking our model for The Truth.
- **Boredom**: Living in a world that is too small for our spirit.

**Success**:
Making room for the **miraculous** and the **unexpected**. Keeping the spirit of adventure alive.

#### Complete Chinese Interpretation

**第九宫**是**意义、世界观和扩展**的领域。它掌管对真理的寻求和打破常规。

**现实模型**：
我们都携带一个世界的心理模型（价值观、假设）。第九宫挑战我们去认识到这**只是一个模型**，而非绝对真理。

**打破模式**：
- **旅行**：将自己暴露于异域文化，以粉碎我们的文化制约。
- **高等教育**：用新概念扩展头脑。
- **哲学/宗教**：寻求存在背后的"为什么"。

**目标**：
用流动的、进化的理解取代僵化的、机械的世界观。保持**"立体意识"**——从多个角度看真理的能力。

**风险**：
- **教条主义**：将我们的模型误认为真理。
- **无聊**：生活在一个对我们的精神来说太小的世界里。

**成功**：
为**奇迹**和**意想不到**腾出空间。保持冒险精神的活力。

#### Core Points

- Arena of meaning, philosophy, and worldview.
- Expansion through travel, study, and challenging assumptions.
- Breaking free from cultural conditioning.
- Making room for the miraculous.
- East parallel: 迁移宫/驿马/天德 (Travel Palace, Movement, Virtue).

#### Detailed Explanation

The Ninth House governs **worldview, philosophy, and meaning-making**. Forrest's key insight is that we all operate from an unspoken **model of reality**—and that model is always arbitrary and limiting. The Ninth House challenges us to recognize our models as models, not as reality itself.

**Expansion** is the developmental method. Travel exposes us to other cultures' models. Higher education challenges assumptions. Adventure breaks up mental routines. The goal is **stereo consciousness**: the ability to see reality from multiple frameworks, knowing that all are partial.

**Successful navigation** keeps the worldview flexible and growing, making room for the miraculous and unexpected. **Unsuccessful navigation** mistakes the model for reality itself—living in a mental world we've outgrown, becoming rigid, dogmatic, and bored. The person who stopped growing at eighteen but is now thirty inhabits a worldview too simple for their actual life.

#### Narrative Snippets

- `[ns_innersky_h9_001]` `[trigger: house_9_general]` `[factor_trigger: astro_house_9]` `[role: 主干]` All our views of reality are conditioned by an unspoken model of the world—and that model is always arbitrary and limiting. → The Inner Sky Ch.7 #9H
- `[ns_innersky_h9_002]` `[trigger: house_9_stereo]` `[factor_trigger: astro_house_9 AND astro_state_success]` `[role: 主干依赖]` Suddenly you have two ways of looking at the world. Stereo consciousness. You can think like an American. And you can think like an Amazonian. Both work. One reality. Two models. → The Inner Sky Ch.7 #9H
- `[ns_innersky_h9_003]` `[trigger: house_9_failure]` `[factor_trigger: astro_house_9 AND astro_state_dysfunction]` `[role: 条件分支]` An unsuccessful navigation invariably involves mistaking a model of reality for reality itself. We live in a world we have outgrown—and it no longer engages or challenges our intelligence. → The Inner Sky Ch.7 #9H
- `[ns_innersky_h9_004]` `[trigger: house_9_mastery]` `[factor_trigger: astro_house_9 AND astro_state_success]` `[role: 条件分支]` We must learn to take chances. We must make leaps of faith—intellectually, emotionally, physically. We must intentionally move to break up our routines of behavior and thought. → The Inner Sky Ch.7 #9H
- `[ns_innersky_h9_005]` `[trigger: house_9_miraculous]` `[factor_trigger: astro_house_9]` `[role: 总结]` We must make room in our lives for the inexplicable. Room for the miraculous. Navigate its terrain gracefully and your daily life lies right on the cutting edge of your growth. → The Inner Sky Ch.7 #9H"""
    normalized_text_zh: str = """"""
    subject: str = "Ninth House - Philosophy & Expansion"
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
        l1_anchor="tis_v1.0.0_ninth_house___philosophy___exp_001_L1",
    )
    version: str = "1.0.0"
