"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482333
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
    semantic_id="iod_v1.0.0_source_text_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "In attempting a discussion of the Interpretation of Dreams, I do not believe that I have oversteppe...
    """
    
    original_text: str = """"In attempting a discussion of the Interpretation of Dreams, I do not believe that I have overstepped the bounds of neuropathological interest. For, on psychological investigation, the dream proves to be the first link in a chain of abnormal psychic structures whose other links, the hysterical phobia, the obsession, and the delusion must, for practical reasons, claim the interest of the physician. The dream (as will appear) can lay no claim to a corresponding practical significance; its theoretical value as a paradigm is, however, all the greater, and one who cannot explain the origin of the dream pictures will strive in vain to understand the phobias, obsessive and delusional ideas, and likewise their therapeutic importance."

#### English Paraphrase (Primary Language)

Freud establishes that dream study is not peripheral but central to understanding psychopathology. The dream represents the first and most accessible link in a chain of abnormal psychic structures that includes hysterical phobias, obsessions, and delusions. While dreams may lack the immediate clinical urgency of these severe conditions, their value as a theoretical paradigm is immense. Dreams are universal, occurring nightly in all humans, making them the ideal model for studying unconscious mechanisms. Without understanding how dreams form, one cannot hope to comprehend the more complex psychopathological phenomena or their treatment.

#### Complete Chinese Interpretation

弗洛伊德在开篇就为梦的研究重新定位：梦并不是神经病学边缘的小题，而是通向一切心理病理现象的**“第一环”**。在他看来，梦、歇斯底里恐惧、强迫观念、妄想等，并非互不相干的现象，而是同一连续谱上的不同级别——机制相同，只是扰乱生活的程度与外显形式不同。

梦之所以具有独特理论价值，在于它既**普遍**又**易于接近**：每个人每晚都会做梦，无需病人、医院或极端案例，就能反复观察无意识如何运作；而恐惧症、强迫症、妄想等严重症状只有在患者就医时才会暴露。借由梦，分析者可以在相对“低风险”的场景中，看到同一套无意识机制如何塑造症状：欲望怎样伪装自己，防御如何压抑或扭曲冲动，象征如何取代直接表达。

因此，“不能解释梦的人，也无法真正理解恐惧症、强迫症和妄想”并非夸张口号，而是一条方法论宣言：梦的解析提供了一把通用钥匙，可以外推到更严重的精神症状之上。梦也许在临床操作上“无足轻重”，却在理论上成为理解无意识世界的范式入口，是精神分析整套体系的基础。

#### Core Points

- Dreams are first link in chain of abnormal psychic structures (phobias, obsessions, delusions)
- Limited practical clinical significance but immense theoretical value as paradigm
- Universal accessibility makes dreams ideal model for studying unconscious
- Cannot understand neuroses without first understanding dreams
- Dreams reveal fundamental mechanisms of unconscious mind

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Psychological Paradigm | Model revealing universal mechanisms | Dreams as ideal example |
| Chain of Psychic Structures | Dream→Phobia→Obsession→Delusion | Shared mechanisms |
| Theoretical Value | Paradigmatic significance | Beyond practical use |
| Universal Accessibility | Everyone dreams nightly | Ideal study subject |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Dreams as psychological paradigm. First link in pathological chain. Universal accessibility makes ideal study model. Theoretical value over practical significance.
- **中文**: 梦作为心理范式。病理链的第一环。普遍可及性使其成为理想研究模型。理论价值超越实践意义。

**Narrative Snippets**:
- `[ns_freud_001]` `[trigger: first_link]` `[factor_trigger: dream_phobia AND dream_dream_obsession]` `[role: 主干]` The dream proves to be the first link in a chain of abnormal psychic structures—phobias, obsessions, delusions. → Source Text
- `[ns_freud_002]` `[trigger: paradigm_value]` `[factor_trigger: dream_dream_delusion AND dream_dream_psychopathology]` `[role: 主干依赖]` The dream's theoretical value as a paradigm is all the greater; one who cannot explain dreams will strive in vain to understand phobias. → Source Text
- `[ns_freud_003]` `[trigger: universal_access]` `[factor_trigger: dream_dream_accessible AND unconscious_mech]` `[role: 条件分支]` Dreams are universal, occurring nightly in all humans, making them the ideal model for studying unconscious mechanisms. → English Paraphrase
- `[ns_freud_004]` `[trigger: foundation]` `[factor_trigger: theoretical_value AND paradigm]` `[role: 总结]` Cannot understand neuroses without first understanding dreams—dreams are the foundational paradigm. → English Paraphrase

#### Detailed Explanation

This opening passage establishes Freud's revolutionary positioning of dreams within psychological science. By calling dreams the "first link" in a chain of psychopathological structures, Freud argues that dreams are both the most accessible and the most revealing window into unconscious processes that underlie all neurotic phenomena.

The progression Freud outlines—from dreams to phobias to obsessions to delusions—reflects increasing degrees of dysfunction and interference with daily life, yet all share common mechanisms of wish-fulfillment, symbolization, and defense. Dreams occur nightly in all humans, requiring no special clinical access to observe. Unlike phobias or delusions which may be rare or require therapeutic relationship to study, everyone experiences dreams and can report them. This universality makes the dream the ideal "paradigm"—a representative example that reveals general principles.

Freud's insistence on dreams' "theoretical value" over "practical significance" positions psychoanalysis as a science concerned with fundamental principles of mind rather than merely symptom relief. This theoretical orientation became characteristic of psychoanalytic thought, prioritizing understanding over cure.

The claim that one "cannot explain" neuroses without understanding dreams establishes dream interpretation as foundational—not an optional specialty but the essential prerequisite for all psychoanalytic work. This bold assertion would prove controversial but became core to psychoanalytic training.

---"""
    normalized_text_zh: str = """"""
    subject: str = "Source Text"
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
        l1_anchor="iod_v1.0.0_source_text_001_L1",
    )
    version: str = "1.0.0"
