"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460819
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
    semantic_id="iod_v1.0.0_5_dream_sources_and_stimuli_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 5DreamSourcesAndStimuli(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Dream Sources | Seen/said/desired/done | Maury's categories |
| Individual Factors | Age/sex/education/habits | Personal determinants |
| Xerxes Example | Preoccupation dreams | Ancient insight |
| Waking Thoughts | Continue in sleep | Continuity principle |

**Source Text**:

"We dream of what we have seen, said, desired or fait" (Maury). "The content of dreams is more or less determined by the individual personality, by age, sex, station in life, education, habits, and by events and experiences of the whole past life" (Jessen). The ancients had the same idea about the dependence of the dream content upon life. When Xerxes, before his march against Greece, was dissuaded from this resolution by good counsel, but was again and again incited by dreams to undertake it, one of the old rational dream-interpreters of the Persians, Artabanus, told him very appropriately that dream pictures mostly contain that of which one has been thinking while awake.

**English Paraphrase**:

Multiple sources contribute to dream content. Maury's formula captures this comprehensively: "We dream of what we have seen, said, desired, or done." Jessen adds that dreams reflect the entire person—their personality, age, gender, social position, education, habits, and accumulated life experiences. Even ancient wisdom recognized this dependency: when Xerxes kept dreaming of invading Greece despite wise counsel against it, the Persian dream-interpreter Artabanus explained that "dream pictures mostly contain that of which one has been thinking while awake."

**Complete Chinese Interpretation (Secondary Language)**:

在完成对“超忆症”的讨论后，弗洛伊德进一步整理了梦的**多重来源**。Maury 用一句话概括：我们梦见的，是“所见、所言、所欲、所为”——既包括视觉经验，也包括谈话内容、内心欲望与外在行为。而 Jessen 则从人格整体出发，认为梦的素材受年龄、性别、社会阶层、教育程度、生活习惯与整个人生经历的综合塑形。

这意味着，梦并不是从某一个单一通道取材，而是从个体整体生命史中抽取片段，再与当下的关切交织在一起。同时，古代波斯解梦者 Artabanus 的名言——“梦图像大多包含清醒时所思之事”——也被弗洛伊德视为一种早期直觉：梦紧密围绕着我们白日里反复思量、挂怀不去的主题展开，只是经过了变形与重组。

不过，弗洛伊德在这里也开始铺垫一个关键转折：如果梦的来源既包括“所见、所闻”，也包括“所欲”，那么要真正理解梦，就不能只停留在对外在经历的回顾，更要追问这些素材背后被激活的**欲望与冲突**。换言之，多重来源说明梦是“过度决定”的——一次梦往往同时回应了多条经验与驱力的线索，其中“欲望”的那一条，将在后文被确立为具有决定性地位的主轴。

**Core Points**:
- Four sources per Maury: what we've seen, said, desired, or done
- Personal factors shape dreams: age, gender, social position, education, habits
- Entire past life contributes to dream material
- Ancient wisdom: dreams reflect waking preoccupations
- Dreams particularly draw on current concerns and unresolved wishes

**Detailed Explanation**:

This section establishes that dreams have **multiple determinants** operating simultaneously. Freud is building toward his theory that dreams are **overdetermined**—having multiple causes and meanings layered together.

**Maury's Four Categories**:
1. **Seen**: Visual experiences, both recent and remote
2. **Said**: Conversations, language, verbal thoughts
3. **Desired**: Wishes, wants, longings (this will become central)
4. **Done**: Actions, behaviors, habits

**Jessen's Personal Factors**: Dreams are individualized, reflecting:
- **Personality structure**: Introverts dream differently than extroverts
- **Life stage**: Children's dreams differ from adults' differ from elderly
- **Gender**: Cultural gender roles influence dream content (though Freud will question biological determinism)
- **Social position**: Class, occupation, status shape available imagery
- **Education**: Intellectual development affects dream sophistication
- **Habits**: Repetitive behaviors and concerns appear in dreams
- **Life history**: Accumulated experiences form dream's raw material

**The Xerxes Example**: Ancient recognition that dreams reflect ongoing concerns. Xerxes kept dreaming of invading Greece because this preoccupied him while awake—his ambition, his fears, his hopes. The dreams didn't introduce the idea; they reflected and intensified what he was already thinking.

**Freud's Emerging Insight**: If dreams draw on "what we have desired," then understanding dreams requires understanding wishes—including wishes we may not consciously acknowledge. This points toward Freud's central thesis: **dreams are wish-fulfillments**.

The ancient Persian interpreter's wisdom—that dreams contain "that of which one has been thinking while awake"—is true but incomplete. Freud will add: dreams also contain thoughts we've been **avoiding** while awake, wishes we've **repressed**, and concerns we don't consciously recognize.

The reference to "desired" (désiré in Maury's French) is crucial. Dreams don't just replay experiences—they **transform** them according to desires. This transformation is the dream-work's essential function.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Dream Sources: Maury's four categories (seen/said/desired/done). Overdetermination. Xerxes example=preoccupations continue. "Desired" becomes central to Freud's theory.
- **中文**: 梦的来源:莫里四类(所见/所言/所欲/所为)。过度决定。薛西斯例子=关切延续。"所欲"成为弗洛伊德理论核心。

**Narrative Snippets**:
- `[ns_freud_ch1_013]` `[trigger: dream_sources]` `[factor_trigger: dream_material]` `[role: 主干]` Maury's four sources: seen/said/desired/done; dreams overdetermined by multiple factors. → Core
- `[ns_freud_ch1_014]` `[trigger: individual_factors]` `[factor_trigger: dream_material AND personality]` `[role: 条件分支]` Jessen: age, sex, education, habits, entire past life shape dream content. → Personal
- `[ns_freud_ch1_015]` `[trigger: desired_central]` `[factor_trigger: dream_material AND wish_fulfillment]` `[role: 条件分支]` "Desired" (désiré) becomes central: dreams transform material according to wishes. → Theory"""
    normalized_text_zh: str = """"""
    subject: str = "5 Dream Sources and Stimuli"
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_5_dream_sources_and_stimuli_001_L1",
    )
    version: str = "1.0.0"
