"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482420
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
    semantic_id="iod_v1.0.0_source_text_007",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "I instruct the patient to put himself into a state of quiet, unreflecting self-observation, and to ...
    """
    
    original_text: str = """"I instruct the patient to put himself into a state of quiet, unreflecting self-observation, and to report to me whatever internal observations he is able to make—feelings, thoughts, memories—in the order in which they occur to him. At the same time I warn him against giving way to any criticism which would lead him to exclude any of the ideas that occur to him, whether on the ground that they are too disagreeable, or too indiscreet, or too unimportant, or irrelevant to what is being looked for. I urge him simply to report what passes through his mind, and to make no selection. Only in this way can we find what we are looking for."

#### English Paraphrase (Primary Language)

Free association is Freud's revolutionary interpretive method for recovering latent dream-thoughts from manifest content. The dreamer is instructed to adopt a passive, uncritical mental state and report everything that comes to mind regarding each dream element—feelings, thoughts, memories—in the order they spontaneously occur. Crucially, the dreamer must suspend all judgment and censorship, reporting even thoughts that seem disagreeable, indiscreet, trivial, or irrelevant. The temptation to select "important" associations or suppress "embarrassing" ones must be resisted. By following these associative chains without conscious direction, the dreamer's unconscious gradually reveals the latent thoughts concealed beneath manifest content. The method works because associations are not random but follow paths determined by unconscious connections—the same paths the dream-work used in reverse.

#### Complete Chinese Interpretation

**自由联想**是弗洛伊德用来取代传统“解梦书”的核心技术：与其由分析者替梦者查字典、硬套固定象征，不如让梦者自己围绕梦中的每一个元素，毫无选择地说出心中浮现的一切念头。关键指令有三点：其一，进入一种尽量放松、不做评判的内在观察状态；其二，对每个梦片段（哪怕是最琐碎、最荒谬的细节）顺着出现顺序说出所有想到的感觉、记忆和念头；其三，刻意对抗那种“这不重要”“说了很丢脸”“与主题无关”的自我审查冲动。

自由联想之所以有效，是因为梦的工作本来就是沿着联想路径把潜梦思想变形成显梦内容：重要的观念通过相似、邻近或情感联系，被移置到别的形象上；多个记忆通过共同特征凝缩成一个符号。只要梦者愿意不加选择地顺着显梦去联想，就有机会**沿着同一条路反向走回去**——从看似无关的符号，回到被伪装的愿望和冲突。

在实践中，自由联想很快会暴露出**阻抗**：当联想突然中断、梦者声称“一片空白”、或坚称某些念头“太琐碎”“不体面”而不愿说出时，往往恰恰靠近无意识真正要隐藏的核心。这时分析者的重要任务，不是强行解释，而是维护一个足够安全、非评判的场域，鼓励梦者继续把“看似无关”的内容说出来，让意义自己从联想网络中浮现。

通过这种方式，梦的解析不再依赖权威解释者的主观直觉，而成为一套可重复、可训练的方法——解释来自梦者自身心灵的连续流动，而非外部强加。

#### Core Points

- **Passive observation**: Quiet, unreflecting self-observation without conscious direction
- **Complete reporting**: Report all thoughts/feelings/memories without selection or censorship
- **Suspend judgment**: Don't exclude disagreeable, trivial, irrelevant, or embarrassing associations
- **Sequential order**: Follow associations in order they spontaneously occur
- **Reverses dream-work**: Associative paths lead back to latent thoughts dream-work concealed

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Free Association | Uncensored reporting | Core interpretive method |
| Passive Observation | Non-directive state | Suspends conscious control |
| Censorship Suspension | No judgment | Allows unconscious emerge |
| Associative Pathways | Follow connections | Reverses dream-work |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Free association: passive observation, uncensored reporting, suspend judgment. Sequential associations retrace dream-work pathways in reverse.
- **中文**: 自由联想:被动观察,无审查报告,暂停评判。顺序联想逆向追溯梦的工作路径。

**Narrative Snippets**:
- `[ns_freud_025]` `[trigger: free_association_method]` `[factor_trigger: dream_free_association AND dream_method]` `[role: 主干]` I instruct the patient to report whatever internal observations he is able to make—feelings, thoughts, memories—in the order in which they occur to him. → Source Text
- `[ns_freud_026]` `[trigger: suspend_criticism]` `[factor_trigger: dream_association AND dream_uncritical]` `[role: 主干依赖]` I warn him against excluding any ideas, whether too disagreeable, indiscreet, unimportant, or irrelevant—simply report what passes through his mind. → Source Text
- `[ns_freud_027]` `[trigger: associative_pathway]` `[factor_trigger: dream_pathway AND dream_unconscious]` `[role: 条件分支]` Associations follow paths determined by unconscious connections—the same paths the dream-work used in reverse. → English Paraphrase
- `[ns_freud_028]` `[trigger: resistance_reveals]` `[factor_trigger: dream_resistance AND dream_significance]` `[role: 总结]` When associations cease or the dreamer censors, the analyst notes these moments as especially meaningful—resistance indicates proximity to important material. → English Paraphrase

#### Detailed Explanation

Free association revolutionized dream interpretation by providing a systematic, replicable method replacing mystical intuition or arbitrary symbol dictionaries. The technique appears simple but rests on profound assumptions about unconscious mental organization.

**The method's instructions are deceptively straightforward**: relax conscious control, report everything that comes to mind about each dream element, suspend all critical judgment. But this suspension of censorship is remarkably difficult. Conscious thought habitually selects, organizes, and censors—deeming some ideas important, others trivial; some acceptable, others shameful. Free association requires abandoning this selectivity.

**Why it works**: The dream-work transformed latent thoughts into manifest content through specific pathways of condensation, displacement, and symbolization. These transformations followed associative connections—similarities, contiguities, emotional linkages. By freely associating to manifest elements, the dreamer retraces these pathways in reverse. If latent thought A was displaced onto manifest element B through their associative connection, then associating freely to B will lead back to A.

**The dreamer's resistance reveals significance**: When associations flow easily, the material is less defended. When the dreamer encounters difficulty, claims "nothing comes to mind," or dismisses associations as "irrelevant," resistance indicates proximity to important unconscious material. The analyst notes these moments of blockage as especially meaningful.

**Overdetermination becomes apparent**: Each manifest element typically generates multiple associative chains leading to different latent thoughts. This demonstrates overdetermination—the manifest element was selected precisely because it condensed multiple latent meanings accessible through different associative paths.

**The analyst's role**: The analyst must maintain neutrality, not directing associations toward preconceived interpretations. When associations cease or the dreamer censors, the analyst gently encourages continuation without forcing specific directions. The interpretation emerges from the patterns in the dreamer's own associations, not imposed from outside.

**Limitations and resistances**: Free association works only when the therapeutic relationship enables honest reporting. Transference, defense mechanisms, and conscious resistance all interfere. The dreamer may genuinely believe an association is irrelevant or may consciously suppress embarrassing thoughts. Breaking through these resistances requires therapeutic skill and patience.

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
        l1_anchor="iod_v1.0.0_source_text_007_L1",
    )
    version: str = "1.0.0"
