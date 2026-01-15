"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482400
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
    semantic_id="iod_v1.0.0_source_text_005",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "By displacement a latent element is replaced not by a component part of itself but by something mor...
    """
    
    original_text: str = """"By displacement a latent element is replaced not by a component part of itself but by something more remote, i.e., by an allusion; and secondly, the psychic accent is so displaced that elements which are important in the dream-thoughts appear in the dream only as subsidiary, while on the other hand, elements which play only a minor part in the dream-thoughts are pushed into the foreground and treated as highly important in the dream."

#### English Paraphrase (Primary Language)

Displacement is the second major dream-work mechanism, operating through two complementary processes. First, displacement of elements: important latent thoughts are represented not directly but through remote associations—allusions, indirect references, or peripheral connections. Second, displacement of emphasis: the psychic intensity or emotional charge attached to important thoughts is transferred to apparently trivial elements. What matters greatly in latent thoughts appears peripheral in the manifest dream, while genuinely trivial details are given disproportionate prominence. This creates effective disguise by making the dream appear concerned with irrelevant minutiae while concealing its true emotional core.

#### Complete Chinese Interpretation

**移置**则是梦的工作中最具“误导性”的机制，它通过转移内容与情感重量，制造一种系统性的错位。弗洛伊德强调，移置至少发生在两个层面：一是**内容的替换**，二是**重要性的转移**。

在内容层面，真正关键的潜在思想并不直接出现，而是借由遥远的联想对象来代表。例如，对父亲的强烈愤怒，可能在梦里变成与车站售票员的小争执；羞耻而不可承认的性欲，可能被伪装成对一件旧家具的莫名在意。被替代者与替代物之间往往只共享某个细节或情境，却足以在无意识里建立联系。

在重要性层面，**情绪强度被从真正重要的内容上移走，投射到表面看似琐碎的细节之上**。梦者也许会为丢伞而焦虑万分，却对房屋起火保持奇异的平静；真正承载焦虑的是那把伞，而不是火灾本身。这样，梦在表层上似乎围绕无关紧要的小事打转，实则把无法直面的冲突藏在那件小事背后。

移置的防御功能十分明显：通过让注意力被“错位”的对象吸引，自我既得以远离真正痛苦的核心，又能在形式上让欲望“有所表达”。对分析工作而言，线索恰恰隐藏在这些不成比例的情绪上——凡是被赋予过高或过低情感重量的细节，往往指向被移置的潜在主题。顺着这些异常的情绪节点追溯，才能把梦重新导回其真正的心理核心。

#### Core Points

- **Displacement of elements**: Important thoughts replaced by remote allusions/associations
- **Displacement of emphasis**: Psychic intensity transferred from important to trivial
- **Reversal of significance**: Central becomes peripheral, peripheral becomes central
- **Disguise through misdirection**: Conceals true emotional focus
- **Defensive function**: Protects against anxiety by shifting attention

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Displacement (Verschiebung) | Transfer of meaning/intensity | Second major mechanism |
| Displacement of Elements | Important→remote allusion | Content substitution |
| Displacement of Emphasis | Intensity transfer | Misdirection |
| Reversal of Significance | Central↔peripheral | Disguise effect |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Displacement operates on elements (allusions) and emphasis (intensity transfer). Important becomes peripheral, trivial becomes central. Effective disguise through misdirection.
- **中文**: 移置作用于元素(暗示)和强调(强度转移)。重要变成边缘，琐碎变成中心。通过误导有效伪装。

**Narrative Snippets**:
- `[ns_freud_017]` `[trigger: displacement_allusion]` `[factor_trigger: dream_displacement AND dream_allusion]` `[role: 主干]` By displacement a latent element is replaced not by a component part of itself but by something more remote—by an allusion. → Source Text
- `[ns_freud_018]` `[trigger: psychic_accent]` `[factor_trigger: dream_displacement AND dream_emphasis]` `[role: 主干依赖]` The psychic accent is so displaced that elements which are important appear as subsidiary, while minor elements are pushed into the foreground. → Source Text
- `[ns_freud_019]` `[trigger: reversal_significance]` `[factor_trigger: dream_reversal AND dream_concealment]` `[role: 条件分支]` Central becomes peripheral, peripheral becomes central—the dream appears concerned with irrelevant minutiae while concealing its true emotional core. → English Paraphrase
- `[ns_freud_020]` `[trigger: follow_intensity]` `[factor_trigger: dream_intensity AND dream_hidden]` `[role: 总结]` Following displaced intensity reveals concealed significance—disproportionate emotional emphasis points toward hidden latent thoughts. → English Paraphrase

#### Detailed Explanation

Displacement is the dream-work's most effective disguise mechanism, creating a systematic misdirection that conceals the dream's true concerns. It operates on two levels simultaneously: content and emphasis.

**Displacement of elements** means that important latent thoughts are not represented directly but through distant associations. If the dreamer is angry at father, the dream may show conflict with a minor authority figure like a bus driver—the father is displaced onto someone more remote and less emotionally charged. The connection may be quite indirect: similar profession, shared physical feature, or merely occurring in similar context. This indirectness makes the latent thought difficult to recognize.

**Displacement of emphasis** (or displacement of psychic intensity) transfers the emotional charge from important to trivial elements. The dreamer may feel intense anxiety in the dream about forgetting an umbrella (trivial) while remaining curiously calm about a house fire (significant). The umbrella carries displaced anxiety originally attached to something deeply important that the umbrella obliquely represents. The emotional intensity reveals what matters unconsciously even when the manifest content appears absurd.

These two types of displacement often work together. A deeply significant latent thought is both (1) represented by a remote association rather than directly, and (2) stripped of its emotional charge which is transferred to something trivial. The result is a dream that appears concerned with nonsense while the true emotional core remains hidden.

Displacement serves crucial defensive functions. It allows expression of unacceptable wishes while protecting against the anxiety direct acknowledgment would cause. The displaced substitute can be consciously tolerated where the original cannot. This is similar to symptom formation in neurosis where original conflicts are displaced onto substitute objects or concerns.

The analyst must reverse displacement by following associations from the trivial manifest elements (which carry intensity) back to the significant latent thoughts (from which intensity was displaced). The disproportionate emotional emphasis in the manifest dream is the crucial clue pointing toward the concealed latent significance.

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
        l1_anchor="iod_v1.0.0_source_text_005_L1",
    )
    version: str = "1.0.0"
