"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.122614
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
    semantic_id="tis_v1.0.0_eleventh_house___the_future__g_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class EleventhHouseTheFutureG(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Future Relationship | No...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Future Relationship | Now shaped by heading | Core concept |
| First Goal Then Friends | Aligned community | Selection logic |
| Direction vs Drifting | Intentional trajectory | Success/failure |
| Peer Network | Allies and peers | Support |

#### Source Text

"Direction—that is the essence of eleventh-house terrain. Where are you going? The arena is unique: we cannot enter it. It always lies just beyond our grasp. It is the future. To navigate successfully, that future must be chosen consciously and intentionally. First comes the goal. Then come the friends."

#### English Paraphrase

The **Eleventh House** is the arena of **the future, goals, and community**. It governs our life direction and the tribes we join.

**Relationship to Time**:
We live in the Now, but we are shaped by where we are heading. The 11th House is our **relationship with the Future** in the present moment.

**Goals**:
- Without goals, we drift.
- Goals give structure to the present.
- They must be **conscious** and **intentional**, not whimsical fantasies.

**Friends and Groups**:
- "House of Friends": Not intimate partners (7th), but **allies** and **peers**.
- **Why we choose them**: Friends symbolize the future we want. If we want to be writers, we befriend writers.
- **Function**: The group stabilizes our identity and trajectory.

**Success**:
Defining a clear vision for the future and surrounding oneself with a community that supports that vision.

**Failure**:
Drifting, lacking direction, getting stuck in "someday," or surrounding oneself with people who reinforce stagnation.

#### Complete Chinese Interpretation

**第十一宫**是**未来、目标和社群**的领域。它掌管我们的人生方向和我们加入的部落。

**与时间的关系**：
我们生活在当下，但我们被我们要去的地方所塑造。第十一宫是我们在当下时刻与**未来**的关系。

**目标**：
- 没有目标，我们就漂流。
- 目标给当下以结构。
- 它们必须是**有意识**和**有意图**的，不是异想天开的幻想。

**朋友和团体**：
- "朋友宫"：不是亲密伴侣（第七宫），而是**盟友**和**同伴**。
- **为何选择他们**：朋友象征着我们想要的未来。如果我们想成为作家，我们与作家交朋友。
- **功能**：团体稳定我们的身份和轨迹。

**成功**：
为未来定义清晰的愿景，并让自己被支持该愿景的社群包围。

**失败**：
漂流，缺乏方向，卡在"总有一天"，或让自己被强化停滞的人包围。

#### Core Points

- Arena of future goals, hopes, and wishes.
- Community, friends, and peer groups as support systems.
- Conscious choice of direction vs. drifting.
- Friends symbolize our desired future.
- East parallel: 交友宫/比劫/人脉 (Friends Palace, Peers, Network).

#### Detailed Explanation

The Eleventh House governs **direction, goals, and the future**. Though the future is only a fantasy, our **awareness of it** shapes present choices. The Eleventh House asks: Where are you going? What are you becoming? What hopes and dreams give meaning to daily life?

**Friends and community** belong here because they symbolize our chosen direction. We gravitate toward people who embody qualities we're developing in ourselves. Our peer group is a mirror of our aspirations. Choosing friends consciously is choosing who we want to become.

**Successful navigation** means making a conscious commitment to a life direction—adopting a strategy, moving intentionally toward chosen goals. **Unsuccessful navigation** produces drifting: living in "someday" without taking steps, letting circumstances choose direction, surrounding oneself with people who reinforce stasis. The person without Eleventh House development never commits to becoming anyone in particular.

#### Narrative Snippets

- `[ns_innersky_h11_001]` `[trigger: house_11_general]` `[factor_trigger: astro_house_11]` `[role: 主干]` Direction. That is the essence of eleventh-house terrain. Where are you going? What are you becoming? What are the hopes and dreams and aspirations that give meaning to your daily life? → The Inner Sky Ch.7 #11H
- `[ns_innersky_h11_002]` `[trigger: house_11_future]` `[factor_trigger: astro_house_11]` `[role: 主干依赖]` The future is only a fantasy. Of itself, it can have no relevance to us. But an awareness of the future exists for all of us in the present tense. And coping with that awareness is essential to the development of our individuality. → The Inner Sky Ch.7 #11H
- `[ns_innersky_h11_003]` `[trigger: house_11_commitment]` `[factor_trigger: astro_house_11 AND astro_state_success]` `[role: 条件分支]` We must make a commitment to become a certain kind of person, to have certain experiences, to attain particular goals. We must adopt a life strategy. → The Inner Sky Ch.7 #11H
- `[ns_innersky_h11_004]` `[trigger: house_11_friends]` `[factor_trigger: astro_house_11]` `[role: 条件分支]` How do we choose those people? We choose them because they reflect our goals. By embodying the future we want for ourselves, those people help stabilize our own intentions. For us, they symbolize the future. → The Inner Sky Ch.7 #11H
- `[ns_innersky_h11_005]` `[trigger: house_11_failure]` `[factor_trigger: astro_house_11 AND astro_state_dysfunction]` `[role: 总结]` If we fail, we drift. And if we drift, we become desperate. Without goals, there can be no meaningful action. So we act, and our actions are tentative, sporadic, uncertain. Full of false starts and empty gestures. → The Inner Sky Ch.7 #11H"""
    normalized_text_zh: str = """"""
    subject: str = "Eleventh House - The Future (Goals & Community)"
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
        l1_anchor="tis_v1.0.0_eleventh_house___the_future__g_001_L1",
    )
    version: str = "1.0.0"
