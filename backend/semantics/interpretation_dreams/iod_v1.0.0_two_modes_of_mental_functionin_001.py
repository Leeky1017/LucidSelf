"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.465553
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
    semantic_id="iod_v1.0.0_two_modes_of_mental_functionin_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class TwoModesOfMentalFunctionin(SemanticEntry):
    """
    **Source Text** (from section context):
"The processes that are described as 'psychically unconsciou...
    """
    
    original_text: str = """**Source Text** (from section context):
"The processes that are described as 'psychically unconscious' are those which we have called the 'primary psychic process.' They show the same peculiarities which we have discovered in the dream-work... condensation, displacement, and the free transferability of cathexes."

"The secondary process brings about what we call 'bound' energy and directed thinking. It operates according to logic, contradiction, and the demands of reality."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Primary Process | Unconscious mode: free energy, condensation, displacement | Dream-work mode |
| Secondary Process | Conscious mode: bound energy, logic, reality-testing | Waking thought mode |
| Free Energy | Cathexis that can shift freely | Primary process characteristic |
| Bound Energy | Cathexis held in stable structures | Secondary process characteristic |
| Pleasure Principle | Seeks immediate discharge | Primary process goal |
| Reality Principle | Delays discharge for adaptation | Secondary process goal |

**English Paraphrase (Primary Language)**:

Freud distinguishes two fundamental modes of mental functioning:

**Primary Process** (Primärvorgang):
- Characteristic of the **unconscious**
- Uses **free energy** that shifts readily between representations
- Operates through **condensation** and **displacement**
- Follows the **pleasure principle**: seeks immediate discharge
- Ignores logic, time, contradiction
- This is the mode of **dream-work**

**Secondary Process** (Sekundärvorgang):
- Characteristic of **conscious/preconscious**
- Uses **bound energy** held in stable structures
- Operates through **logic** and **reality-testing**
- Follows the **reality principle**: delays discharge for adaptive ends
- Respects contradiction, sequence, causation
- This is the mode of **waking thought**

Dreams reveal primary process because the secondary process relaxes during sleep. The bizarreness of dreams reflects primary process logic: contradictions coexist, time is fluid, one thing represents many.

**Complete Chinese Interpretation (Secondary Language)**:

弗洛伊德区分两种心理功能的基本模式：

**初级过程**（Primärvorgang）：
- **潜意识**的特征
- 使用在表象之间自由转移的**自由能量**
- 通过**凝缩**和**移置**运作
- 遵循**快乐原则**：寻求即时释放
- 忽视逻辑、时间、矛盾
- 这是**梦工作**的模式

**次级过程**（Sekundärvorgang）：
- **意识/前意识**的特征
- 使用保持在稳定结构中的**束缚能量**
- 通过**逻辑**和**现实检验**运作
- 遵循**现实原则**：为适应目的延迟释放
- 尊重矛盾、序列、因果
- 这是**清醒思维**的模式

梦揭示初级过程，因为次级过程在睡眠期间放松。梦的怪异性反映初级过程逻辑：矛盾共存，时间流动，一物代多物。

**Core Points**:

- Two fundamental modes: primary and secondary process
- Primary: free energy, condensation, displacement, pleasure principle
- Secondary: bound energy, logic, reality principle
- Dreams = primary process domination
- Waking = secondary process domination
- Sleep relaxes secondary process control

**Detailed Explanation**:

This distinction is **foundational** for psychoanalytic metapsychology. It explains not only dreams but symptoms, slips, and creative processes.

**Primary process** is older phylogenetically and ontogenetically—the infant's mind works primarily this way. **Secondary process** develops through encounter with reality's demands. Healthy waking functioning requires secondary process dominance, but primary process never disappears—it persists in the unconscious.

**Dreams** occur when secondary process vigilance relaxes during sleep. The wish, normally kept in check by reality-testing, finds expression through primary process mechanisms (condensation, displacement). The result appears "irrational" to waking consciousness because it follows different rules.

**Free vs. bound energy** explains condensation and displacement. Free energy can shift from one representation to another (displacement) or attach to multiple representations at once (condensation). Bound energy is "stuck" to its representation and follows logical pathways only.

This model underlies the concept of **defense mechanisms**: repression, for example, prevents secondary process from accessing certain primary process contents.

**Textual Criticism & Variant Analysis (Bilingual)**:

- **English**: "Primary/secondary process" (German: Primär-/Sekundärvorgang) remain Freud's preferred terms. Later he would distinguish "bound" and "free" energy more precisely.
- **中文**: "初级/次级过程"保留了弗洛伊德的术语。中文"初级"有"原始"含义，与英文primary的developmental sense一致。

**Narrative Snippets**:

- `[ns_freud_psy_008]` `[trigger: primary_process]` `[factor_trigger: primary_process AND pleasure_principle]` `[role: 主干]` The primary psychic process shows the same peculiarities as dream-work: condensation, displacement, and free transferability of cathexes—following the pleasure principle. → Freud Ch.VII #Processes
- `[ns_freud_psy_009]` `[trigger: secondary_process]` `[factor_trigger: secondary_process AND reality_principle]` `[role: 主干依赖]` The secondary process brings about bound energy and directed thinking—it operates according to logic, contradiction, and reality demands. → Freud Ch.VII #Processes
- `[ns_freud_psy_010]` `[trigger: process_dominance]` `[factor_trigger: anxiety_dream AND anxiety_signal]` `[role: 条件分支]` Dreams reveal primary process because secondary process relaxes during sleep—the bizarreness of dreams reflects primary process logic. → Freud Ch.VII #Processes
- `[ns_freud_psy_011]` `[trigger: threatening_wish]` `[factor_trigger: threatening_wish AND wish_fulfillment]` `[role: 总结]` Even anxiety dreams fulfill wishes—the threatening wish breaks through censorship, signaling danger while still seeking satisfaction. → Freud Ch.VII #Processes"""
    normalized_text_zh: str = """"""
    subject: str = "Two Modes of Mental Functioning"
    factor_refs: list = ['primary_process', 'secondary_process', 'free_energy', 'bound_energy', 'pleasure_principle', 'reality_principle']
    
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
        l1_anchor="iod_v1.0.0_two_modes_of_mental_functionin_001_L1",
    )
    version: str = "1.0.0"
