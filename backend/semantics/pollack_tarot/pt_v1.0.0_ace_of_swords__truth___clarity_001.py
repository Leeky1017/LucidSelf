"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994947
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
    semantic_id="pt_v1.0.0_ace_of_swords__truth___clarity_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class AceOfSwordsTruthClarity(SemanticEntry):
    """
    **Visual Elements**:
- Sword pointing straight up
- Piercing crown (material world)
- Hand from clou...
    """
    
    original_text: str = """**Visual Elements**:
- Sword pointing straight up
- Piercing crown (material world)
- Hand from cloud
- Mountains in background (abstract truth)
- Crown with branches (victory through truth)

**English Paraphrase**:

The **Ace of Swords** represents **gift of truth and clarity** - the mind's power to pierce illusions and reach spiritual reality. This is **intellect at its purest** - not overthinking, but clear perception that cuts through fog to reveal what is real.

**Core Symbolism**:
- **Sword pointing up**: True perception, reaching beyond material
- **Piercing crown**: Breaking through limitations of ordinary consciousness
- **Mountains**: Abstract truth independent of personal viewpoint
- **Hand from cloud**: Divine gift, spiritual origin of clear thinking
- **Tight grip**: Emotional force (love and hate) hard to control

**Upright Meaning**:
- **Mental clarity**: Cutting through confusion to see truth
- **Breakthrough**: Sudden understanding, revelation
- **Justice**: Fair judgment, impartial assessment
- **New idea**: Intellectual conception, fresh perspective
- **Truth revealed**: Reality becomes clear, illusions dispelled
- **Emotional intensity**: Extreme feelings (both love and hate) expressed directly

**Reversed/Challenged**:
- **Grip fails**: Loss of clarity, confused thinking
- **Illusion**: Mistaking false for true
- **Emotional overwhelm**: Feelings overpower reason
- **Exaggeration**: Problems appear larger than reality
- **Need balance**: Take hold of self, find realistic perspective

**完整中文诠释**:
**宝剑王牌**=**真理与清晰之礼物**——心智力量穿透幻觉达灵性实在。**最纯粹智慧**——非过度思考而是穿透迷雾显示真实的清晰感知。**图像元素**：**剑指向上**=真知觉超越物质；**穿透王冠**=突破普通意识限制；**远处山脉**=独立于个人观点的抽象真理；**云中之手**=神圣礼物，清晰思考之灵性源头；**紧握**=情感力量（爱恨）难以控制。**正位含义**：心智清晰、突破、正义、新想法、真理显现、情感强度。混乱情境突然变清晰，需要说出困难真理，法律事务/合同/决定，切断不再服务的联系，学习/工作中的智力突破。**逆位/挑战**：握力失败、幻觉、情感淹没、夸张、需要平衡。**哲学层面**：在所有小牌中，宝剑王牌最接近第五元素（灵性）。但单凭智力创造更多幻觉——需要**圣杯王牌（爱）才能找到真理**，然而只有智力能超越即时经验。**两者都需要**：情感表达真实的我们，但可能被夸大/自我中心；单凭智力不带来觉知。两者必须来自**更深的灵性价值观**（大阿尔卡纳）。

**Philosophical Layer**: **More than any Minor card, Ace of Swords reaches fifth element (Spirit)**. But intellect alone creates more illusion - needs **Ace of Cups (love) to find truth**, yet only intellect can transcend immediate experience. **Both needed**: emotion expresses real us, but can be exaggerated/egotistic; intellect alone brings no awareness. Both must come from **deeper spiritual values** (Major Arcana).

**Practical Applications**:
- Confusing situation suddenly becomes clear
- Need to speak difficult truth
- Legal matters, contracts, decisions
- Cutting ties that no longer serve
- Intellectual breakthrough in study/work

**Narrative Snippets**:
- `[ns_78deg_257]` `[trigger: ace_swords_truth]` `[factor_trigger: tarot_ace_swords AND state_mental_clarity]` `[role: 主干]` Ace of Swords represents the gift of truth and clarity—mind's power to pierce illusions; intellect at its purest, cutting through fog to reveal what is real. → English Paraphrase
- `[ns_78deg_258]` `[trigger: sword_up_crown]` `[factor_trigger: tarot_ace_swords AND symbol_sword_crown]` `[role: 主干依赖]` Sword pointing straight up, piercing crown—true perception reaching beyond material world; breaking through limitations of ordinary consciousness. → Core Symbolism
- `[ns_78deg_259]` `[trigger: ace_swords_breakthrough]` `[factor_trigger: tarot_ace_swords AND event_breakthrough]` `[role: 条件分支]` Mental clarity cutting through confusion—sudden understanding, revelation; fair judgment, impartial assessment; new idea, fresh intellectual perspective. → Upright Meaning
- `[ns_78deg_260]` `[trigger: ace_swords_reversed]` `[factor_trigger: tarot_ace_swords AND polarity_reversed]` `[role: 例外处理]` Reversed: grip fails, loss of clarity; mistaking false for true; emotional overwhelm overpowering reason; problems appearing larger than reality. → Reversed Meaning
- `[ns_78deg_261]` `[trigger: swords_cups_needed]` `[factor_trigger: tarot_ace_swords AND tarot_ace_cups]` `[role: 条件分支]` Intellect alone creates more illusion—needs Ace of Cups (love) to find truth; yet only intellect can transcend immediate experience. Both are needed. → Philosophical Layer
- `[ns_78deg_262]` `[trigger: ace_swords_spirit]` `[factor_trigger: tarot_ace_swords AND element_spirit]` `[role: 总结]` More than any Minor card, Ace of Swords reaches fifth element (Spirit)—but both emotion and intellect must come from deeper spiritual values (Major Arcana). → Philosophical Layer
- `[ns_78deg_454]` `[trigger: tight_grip]` `[factor_trigger: tarot_ace_swords AND symbol_tight_grip]` `[role: 条件分支]` Hand from cloud with tight grip—emotional force (love and hate) hard to control; intellect combined with intensity; the sword must be held firmly or it cuts the wielder. → Core Symbolism
- `[ns_78deg_455]` `[trigger: abstract_mountains]` `[factor_trigger: tarot_ace_swords AND symbol_mountains_truth]` `[role: 条件分支]` Mountains in background—abstract truth independent of personal viewpoint; objective reality that intellect can perceive when freed from ego distortions. → Core Symbolism
- `[ns_78deg_495]` `[trigger: double_edged_blade]` `[factor_trigger: tarot_ace_swords AND principle_double_edge]` `[role: 条件分支]` Sword as double-edged blade—truth cuts both ways; revelation may bring pain alongside clarity; the same intellect that liberates can wound if misused. → Core Symbolism
- `[ns_78deg_552]` `[trigger: crown_branches]` `[factor_trigger: tarot_ace_swords AND symbol_crown_branches]` `[role: 条件分支]` Crown with branches pierced by sword—victory through truth; mental clarity crowned with organic growth; the intellect's triumph not sterile but fertile. → Visual Elements"""
    normalized_text_zh: str = """"""
    subject: str = "Ace of Swords: Truth & Clarity"
    factor_refs: list = ['gift', 'existing', 'breakthrough', 'existing', 'principle', 'existing', 'force', 'existing', 'mixed', 'existing']
    
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
        book_id="pollack_tarot",
        chapter="",
        l1_anchor="pt_v1.0.0_ace_of_swords__truth___clarity_001_L1",
    )
    version: str = "1.0.0"
