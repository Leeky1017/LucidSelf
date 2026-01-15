"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460806
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
    semantic_id="iod_v1.0.0_4_memory_in_dreams__the_hyperm_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 4MemoryInDreamsTheHyperm(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Hypermnesia | Super-memory | Dreams access forgotten |
| Delbœuf's Dream | Lizard/fern | Source revealed 16yrs later |
| Memory vs Consciousness | Larger store | Unconscious evidence |
| Nothing Forgotten | Stored, inaccessible | Key Freudian claim |

**Source Text**:

It often happens that matter appears in the dream content which one cannot recognise later in the waking state as belonging to one's knowledge and experience. One remembers well enough having dreamed about the subject in question, but cannot recall the fact or time of the experience. The dreamer is therefore in the dark as to the source from which the dream has been drawing, and is even tempted to believe an independently productive activity on the part of the dream, until, often long afterwards, a new episode brings back to recollection a former experience given up as lost, and thus reveals the source of the dream.

**English Paraphrase**:

Dreams frequently contain material that the dreamer cannot consciously recognize as coming from their own experience. The dreamer knows they dreamed about something specific but cannot trace when or where they learned it. This suggests the dream has creative powers of its own. However, often years later, some chance encounter reveals the forgotten source—proving the dream accessed genuine memories that were simply inaccessible to waking consciousness. This phenomenon is called hypermnesia: dreams can remember what waking life has forgotten.

**Complete Chinese Interpretation (Secondary Language)**:

这一节提出的“**超忆症（hypermnesia）**”现象，对无意识记忆观念至关重要。许多人都有类似经验：梦里出现极其具体的场景、名字或细节，醒来后却完全想不起自己何时见过或学过这些东西，于是误以为梦“创造”出了全新的内容。弗洛伊德通过 Delbœuf 和 Maury 等人的著名案例说明：多年之后，当事人在偶然情境中重新遇到旧物或旧文献时，才发现梦中的那些“新东西”，其实都在过去的某个时刻被真实地感知和记住过，只是从清醒记忆中彻底消失了。

这说明两点：第一，人类的记忆储存远超出意识所能调用的部分，我们的大脑保留了大量被遗忘的细节，只是在清醒状态下无法自如访问；第二，梦在某些条件下能**比清醒意识更深入地动员记忆痕迹**，把那些被放弃或压抑的材料重新带回主观体验之中。梦看似在“创造”，实则是在调用深层记忆库。

“超忆症”由此成为无意识存在的重要证据：既然有些记忆在清醒时完全不可得，却能在梦中精准地复现并经日后验证为真，那么它们显然在某个非意识层面被持续保存着。梦不只是反映近期生活，更是在广阔记忆海底进行复杂检索与重组的活动。

**Core Points**:
- Dreams contain material unrecognizable to waking consciousness
- Appears like creative invention but is actually forgotten memory
- Hypermnesia: dreams access memories inaccessible when awake
- May take years to discover the dream's true source
- Challenges assumption that waking consciousness has full access to memory

**Detailed Explanation**:

Freud introduces the concept of **hypermnesia**—super-memory—which demonstrates that dreams have access to a vaster memory store than waking consciousness. This is crucial evidence for the unconscious.

**Delbœuf's Lizard Dream (1862)**: 

The botanist Delbœuf dreamed of finding lizards in snow, naming a fern "Asplenium ruta muralis," and witnessing a procession of lizards. Upon waking, he knew almost no Latin plant names and couldn't explain how he knew "Asplenium." The name proved accurate (slightly modified as "Asplenium ruta muraria"). 

**The Source Revealed (16 years later, 1878)**: Visiting a friend, Delbœuf found an old herbarium from 1860—two years before his dream. He had written the Latin names himself, at a botanist's dictation, when his friend's sister visited on her wedding trip. He had completely forgotten this event in waking life, yet his dream accessed it perfectly.

**Second Revelation (1877)**: Delbœuf found an illustrated journal from 1861 showing the exact procession of lizards from his dream. He had subscribed to the journal but forgotten reading it.

**Theoretical Significance**:

1. **Memory is Larger than Consciousness**: We "know" far more than we can consciously recall. Dreams prove this by retrieving forgotten experiences.

2. **Nothing is Truly Forgotten**: Experiences may become inaccessible to waking recall but remain stored and can be activated in dreams.

3. **Dreams Have Superior Access**: The sleeping mind can reach memory traces that waking consciousness cannot access—suggesting different systems or levels of mental functioning.

4. **Challenge to Simple Continuity**: If dreams simply reflected recent waking concerns, hypermnesia wouldn't occur. The dream must be actively searching through memory in sophisticated ways.

Maury's "Mussidan" dream similarly demonstrated hypermnesia: he dreamed detailed geography of a French town he "didn't know," which proved perfectly accurate—revealing knowledge he'd forgotten acquiring.

This phenomenon supports Freud's emerging theory: the unconscious contains vast amounts of forgotten material that can surface in dreams. The dream is not random but systematically searches memory for material relevant to unconscious concerns.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Hypermnesia: Dreams access memories inaccessible when awake. Delbœuf's 16-year gap. Nothing truly forgotten. Unconscious storage. Dreams search deep memory.
- **中文**: 超忆症:梦访问清醒时不可及的记忆。德尔布夫16年差距。无事真正遗忘。无意识储存。梦搜索深层记忆。

**Narrative Snippets**:
- `[ns_freud_ch1_010]` `[trigger: hypermnesia]` `[factor_trigger: dream_memory]` `[role: 主干]` Hypermnesia: dreams access memories inaccessible to waking consciousness; "super-memory". → Core
- `[ns_freud_ch1_011]` `[trigger: delboeuf_dream]` `[factor_trigger: dream_memory AND historical_case]` `[role: 条件分支]` Delbœuf's lizard dream: source revealed 16 years later; proves nothing truly forgotten. → Evidence
- `[ns_freud_ch1_012]` `[trigger: unconscious_storage]` `[factor_trigger: dream_memory AND unconscious_evidence]` `[role: 条件分支]` Memory larger than consciousness; dreams search deep memory; evidence for unconscious. → Theory"""
    normalized_text_zh: str = """"""
    subject: str = "4 Memory in Dreams: The Hypermnesia Phenomenon"
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
        l1_anchor="iod_v1.0.0_4_memory_in_dreams__the_hyperm_001_L1",
    )
    version: str = "1.0.0"
