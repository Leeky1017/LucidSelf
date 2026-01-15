"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460779
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
    semantic_id="iod_v1.0.0_2_the_pre_scientific_view__div_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 2ThePreScientificViewDiv(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Divine Inspiration | Dreams from gods | Pre-Aristotelian view |
| True/False Dreams | Help vs mislead | Dual classification |
| Antagonistic Streams | Opposing views | Historical pattern |
| Supernatural Sources | External attribution | Contrast to Freud |

**Source Text**:

As every one knows, the ancients before Aristotle did not consider the dream a product of the dreaming mind, but a divine inspiration, and in ancient times the two antagonistic streams, which one finds throughout in the estimates of dream life, were already noticeable. They distinguished between true and valuable dreams, sent to the dreamer to warn him or to foretell the future, and vain, fraudulent, and empty dreams, the object of which was to misguide or lead him to destruction.

**English Paraphrase**:

The ancient pre-Aristotelian view saw dreams not as products of the human mind but as messages from the divine. Even in antiquity, two opposing perspectives on dreams coexisted: some dreams were considered true and valuable—warnings or prophecies sent to help the dreamer. Others were seen as false and dangerous—deceptive messages meant to mislead or destroy. This fundamental ambivalence toward dreams has persisted throughout history.

**Complete Chinese Interpretation (Secondary Language)**:

在回顾既有文献时，弗洛伊德首先指出了一个重要的历史事实：在亚里士多德之前的古代世界，人们通常并不把梦看作“做梦者心灵的产物”，而是当作神灵传递的信息。因此，梦的权威来自外在超自然力量，而非来自个体自身的心理活动。

更有意思的是，古代对于梦的态度本身就带有强烈的**二元性**：一方面，有所谓“真梦”“吉梦”，被视为神明的告诫或预言，可以帮助决策、避免灾祸；另一方面，也有“虚梦”“妖梦”，被认为是欺骗性的，引人误入歧途甚至走向毁灭。为了调和这种矛盾经验，古人往往诉诸不同的超自然来源——善神赐下的是真梦，恶灵或敌人的咒诅制造的是虚梦。

弗洛伊德在这里的用意，并不是简单否定这种“神启说”，而是强调：这种对梦既敬畏又怀疑的矛盾心态本身，折射出对梦的一个重要洞见——梦既可能带来真相，也可能制造迷惑；它一方面承载我们最深的愿望与恐惧，另一方面又通过伪装和扭曲掩盖这些内容。精神分析将把梦的来源从“神灵”转移到“心理装置”，但会保留这一点：梦内在地包含冲突与双重面貌，只是其真正的“神”和“魔”，是心灵内部的不同机构，而非外在的超自然存在。

**Core Points**:
- Ancients viewed dreams as divine inspiration, not mental products
- Two opposing streams: true/valuable vs false/dangerous dreams
- True dreams: warnings or prophecies meant to help
- False dreams: deceptions meant to mislead or destroy
- This ambivalence persists across cultures and eras

**Detailed Explanation**:

Freud identifies a crucial historical pattern: the pre-scientific understanding of dreams as supernatural communications. This view was not monolithic but contained an internal tension that Freud finds significant.

The distinction between "true" and "false" dreams served important psychological and social functions in ancient societies. True dreams validated religious authority (priests who could interpret divine messages), provided guidance for important decisions (military campaigns, marriages, business ventures), and offered comfort (communications from deceased loved ones). False dreams explained away predictions that didn't come true and warnings that led to disaster.

This binary classification reveals an implicit recognition of dreams' ambiguous nature—they seem meaningful yet often prove meaningless, appear prophetic yet frequently mislead. The ancients resolved this paradox by attributing different dreams to different sources: benevolent gods sent true dreams, while malevolent forces (demons, false gods, or one's enemies' curses) sent false ones.

Freud mentions this historical view not merely for completeness but to establish a contrast. Where the ancients attributed dreams to external supernatural forces, Freud will attribute them to internal psychic forces. Yet he preserves something of their insight: dreams do have different sources and different relationships to truth—but these sources are psychic agencies (ego, superego, unconscious wishes) rather than gods and demons.

The phrase "antagonistic streams" is significant. Freud sees ambivalence not as confusion but as insight: the ancients recognized that dreams have dual nature because dreams truly do express both desire (wishes we want fulfilled) and prohibition (fears and guilt that censor those wishes). The supernatural explanation was wrong, but the recognition of conflict was right.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Pre-Scientific View: Divine inspiration, not mental products. True/false dreams=benevolent/malevolent sources. Ambivalence reflects dreams' dual nature. Internal conflict precognized.
- **中文**: 前科学观点:神启,非心理产物。真/假梦=善/恶源头。矛盾态度反映梦的双重性。内心冲突已被预识。

**Narrative Snippets**:
- `[ns_freud_ch1_004]` `[trigger: divine_inspiration]` `[factor_trigger: pre_scientific_view]` `[role: 主干]` Pre-Aristotelian: dream = divine inspiration, not mental product; external supernatural attribution. → Historical
- `[ns_freud_ch1_005]` `[trigger: true_false_dreams]` `[factor_trigger: pre_scientific_view AND dream_classification]` `[role: 条件分支]` True/valuable dreams (warnings) vs false/dangerous dreams (deceptions); dual nature recognized. → Classification
- `[ns_freud_ch1_006]` `[trigger: antagonistic_streams]` `[factor_trigger: pre_scientific_view AND ambivalence]` `[role: 条件分支]` Antagonistic streams reflect dreams' inner conflict—desire vs prohibition, wish vs censor. → Precognition"""
    normalized_text_zh: str = """"""
    subject: str = "2 The Pre-Scientific View: Divine Inspiration"
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
        l1_anchor="iod_v1.0.0_2_the_pre_scientific_view__div_001_L1",
    )
    version: str = "1.0.0"
