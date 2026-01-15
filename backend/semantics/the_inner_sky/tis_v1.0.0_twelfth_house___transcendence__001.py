"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.122626
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
    semantic_id="tis_v1.0.0_twelfth_house___transcendence__001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class TwelfthHouseTranscendence(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| House of Troubles/Wisdom...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| House of Troubles/Wisdom | Dual nature | Medieval vs modern |
| Ego Dissolution | Surrender | Core process |
| Escapism vs Transcendence | Numb vs awaken | Failure/success |
| Inner Peace | Quiet center | Goal |

#### Source Text

"To the medievals, it was the House of Troubles. But we need not respond to trouble with self-pity. We can use it. We can turn inward. We can let go. Our identity in the world is a transitory phenomenon. Only consciousness itself is eternal. Grasp that, and the House of Troubles is troubled no longer. It is the House of Wisdom."

#### English Paraphrase

The **Twelfth House** is the arena of **transcendence, unconsciousness, and spiritual surrender**. It is where the ego dissolves back into the universal.

**The House of Troubles?**:
Traditionally associated with prisons, hospitals, and self-undoing. Why? Because if we cling to the ego here, we suffer. Life forces us to **let go**.

**The Function**:
- **Surrender**: Releasing attachment to outcomes, identities, and plans.
- **Ego Death**: Realizing we are not the "doer," but part of a larger flow.
- **Inner Peace**: Finding the quiet center amidst chaos.

**Techniques**:
- **Meditation**: Consciously entering the state of non-doing.
- **Solitude**: Withdrawing from the world to recharge.
- **Compassion**: Selfless service (dissolving boundaries between self and other).

**Failure (Escapism)**:
Instead of transcending, we **numb out**. Alcohol, drugs, TV, sleep—anything to turn off consciousness without doing the spiritual work.

**Success**:
Realizing that our worldly identity is temporary, but our consciousness is eternal. This brings ultimate **freedom** and **wisdom**.

#### Complete Chinese Interpretation

**第十二宫**是**超越、无意识和精神臣服**的领域。这是小我消解回普遍性的地方。

**麻烦之宫？**：
传统上与监狱、医院和自我毁灭相关联。为什么？因为如果我们在这里执着于小我，我们就会受苦。生活强迫我们**放手**。

**功能**：
- **臣服**：释放对结果、身份和计划的依恋。
- **小我死亡**：认识到我们不是"做事者"，而是更大流动的一部分。
- **内在平静**：在混乱中找到安静的中心。

**技术**：
- **冥想**：有意识地进入无为状态。
- **独处**：从世界撤退以充电。
- **慈悲**：无私服务（消解自我与他者之间的边界）。

**失败（逃避主义）**：
我们不超越，而是**麻木**。酒精、毒品、电视、睡眠——任何能关闭意识而不做灵性工作的东西。

**成功**：
认识到我们的世俗身份是暂时的，但我们的意识是永恒的。这带来终极的**自由**和**智慧**。

#### Core Points

- Arena of transcendence, spirituality, and the unconscious.
- Letting go of ego and worldly identity.
- Meditation, solitude, and selfless service.
- Danger of escapism vs. promise of enlightenment.
- East parallel: 福德宫/空亡/修行 (Fortune/Virtue Palace, Emptiness, Cultivation).

#### Detailed Explanation

The Twelfth House governs **transcendence, spirituality, and the dissolution of ego**. Forrest describes it as a built-in "escape route"—the capacity to move attention away from personality's dramas into a peaceful center within. This is the realm of meditation, prayer, and contemplation.

The Twelfth House represents **letting go**: releasing attachment to worldly identity, accepting that ego is temporary while consciousness is eternal. This brings ultimate freedom and wisdom. Selfless service—giving without thought of return—is a Twelfth House practice because it dissolves the ego's constant self-reference.

**Successful navigation** means finding genuine spiritual peace and perspective on life's struggles. **Unsuccessful navigation** confuses transcendence with **escapism**: seeking numbness instead of peace, obliteration instead of enlightenment. Alcoholism and drug abuse are failed Twelfth House strategies—attempts to transcend that destroy rather than liberate.

#### Narrative Snippets

- `[ns_innersky_h12_001]` `[trigger: house_12_general]` `[factor_trigger: astro_house_12]` `[role: 主干]` Whenever trouble strikes, each of us has a built-in escape route. We can move our attention away from the dramas of personality. We can focus it on a peaceful place deep within us, a place that is always there, waiting. → The Inner Sky Ch.7 #12H
- `[ns_innersky_h12_002]` `[trigger: house_12_meditation]` `[factor_trigger: astro_house_12 AND astro_state_success]` `[role: 主干依赖]` We can call that escape route meditation. We can call it prayer or contemplation. And the peace we find we can call God or 'our center' or just relaxation. There is no house in which words are less significant. → The Inner Sky Ch.7 #12H
- `[ns_innersky_h12_003]` `[trigger: house_12_escapism]` `[factor_trigger: astro_house_12 AND astro_state_dysfunction]` `[role: 条件分支]` Instead of seeking peace, we seek numbness. Instead of retreating temporarily into our depths, we seek to obliterate consciousness altogether. The alcoholic and the drug abuser are both failed twelfth-house navigators. → The Inner Sky Ch.7 #12H
- `[ns_innersky_h12_004]` `[trigger: house_12_letting_go]` `[factor_trigger: astro_house_12]` `[role: 条件分支]` We can gracefully let go of a set of dying circumstances, knowing that when the dust settles, we can begin again. Such letting go is never easy. Those dying circumstances are dear to us. They are the foundation of our identity in the world. → The Inner Sky Ch.7 #12H
- `[ns_innersky_h12_005]` `[trigger: house_12_wisdom]` `[factor_trigger: astro_house_12 AND astro_state_success]` `[role: 总结]` Our identity in the world is a transitory phenomenon. Only consciousness itself is eternal. Nothing else matters. Grasp that, and the House of Troubles is troubled no longer. It is the House of Wisdom. → The Inner Sky Ch.7 #12H"""
    normalized_text_zh: str = """"""
    subject: str = "Twelfth House - Transcendence (Letting Go)"
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
        l1_anchor="tis_v1.0.0_twelfth_house___transcendence__001_L1",
    )
    version: str = "1.0.0"
