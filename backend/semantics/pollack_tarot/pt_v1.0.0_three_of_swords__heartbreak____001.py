"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994961
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
    semantic_id="pt_v1.0.0_three_of_swords__heartbreak____001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class ThreeOfSwordsHeartbreak(SemanticEntry):
    """
    **Visual Elements**:
- Three swords piercing heart
- Gray rainy sky
- Symmetrical composition despit...
    """
    
    original_text: str = """**Visual Elements**:
- Three swords piercing heart
- Gray rainy sky
- Symmetrical composition despite pain
- Heart exposed, vulnerable

**English Paraphrase**:

The **Three of Swords** represents **sorrow and heartbreak** in its most direct form. Yet within this pain lies a teaching: **we cannot push sorrow away but must take it into our hearts**, accept it, and through acceptance transform it with courage and love.

**Core Symbolism**:
- **Three swords in heart**: Triple pain, inescapable suffering
- **Rain**: Tears, grief, cleansing through sorrow
- **Symmetry**: Even in pain, there is order and potential for peace
- **Exposed heart**: Vulnerability, openness to hurt but also to healing

**Upright Meaning**:
- **Heartbreak**: Love lost, betrayal, grief
- **Painful truth**: Reality that hurts to acknowledge
- **Separation**: Ending of relationship, loss of connection
- **Mourning**: Processing death or ending
- **Necessary pain**: Suffering that leads to growth
- **Acceptance required**: Cannot avoid, must face and integrate

**Reversed/Challenged**:
- **Blocked healing**: Pushing pain away prevents recovery
- **Mental alienation**: Refusing to process grief leads to disorder
- **Avoided mourning**: Trying not to think about it keeps pain forever present
- **Unresolved loss**: Past hurt constraining current potential
- **Increased hold**: Avoidance makes pain stronger, not weaker

**完整中文诠释**:
**宝剑三**=最直接形式的**悲伤与心碎**。然而痛苦中有教导：**不能推开悲伤必须纳入心中**，接受它，通过接受以勇气与爱转化它。**图像元素**：**三剑穿心**=三重痛苦，无可逃避之苦；**灰雨天空**=泪水、悲伤、通过悲伤净化；**对称构图**=即使痛苦中仍有秩序与和平潜力；**暴露的心**=脆弱，既可被伤也可愈合之开放。**正位含义**：**心碎**（失去的爱、背叛、悲伤），**痛苦真理**（承认伤人的现实），**分离**（关系结束、失去连接），**哀悼**（处理死亡或结束），**必要痛苦**（导向成长的受苦），**需要接受**（无法避免，必须面对并整合）。**逆位/挑战**：**阻塞疗愈**（推开痛苦阻止康复），**心智疏离**（拒绝处理悲伤导致混乱），**回避哀悼**（试图不去想反而让痛苦永存），**未解失落**（过去伤害限制当前潜能），**加剧控制**（回避使痛苦更强而非更弱）。**转化原则**：相同数字的牌常指示转化而非对立。**宝剑三与圣杯三交叉**（悲伤与喜悦交叉）=**接受与爱能将痛苦转化为喜悦记忆**，尽管失去仍拥抱生活。

**Transformation Principle**: Cards of same number often indicate transformation, not opposition. **Three of Swords crossed by Three of Cups** (sorrow crossed by joy) = **acceptance and love can turn pain into joyful memory**, embracing life despite loss.

**In Readings**:
- Death, divorce, betrayal, loss
- Painful truth must be faced
- Grief process beginning
- Need to accept what cannot be changed
- Background issue: unresolved past hurt blocking current growth

**Narrative Snippets**:
- `[ns_78deg_263]` `[trigger: three_swords_heartbreak]` `[factor_trigger: tarot_three_swords AND state_heartbreak]` `[role: 主干]` Three of Swords represents sorrow and heartbreak in its most direct form—yet within pain lies teaching: we cannot push sorrow away but must accept it. → English Paraphrase
- `[ns_78deg_264]` `[trigger: three_swords_heart]` `[factor_trigger: tarot_three_swords AND symbol_pierced_heart]` `[role: 主干依赖]` Three swords piercing heart beneath gray rain—triple pain, inescapable suffering; yet symmetry in composition shows order and potential for peace even in pain. → Core Symbolism
- `[ns_78deg_265]` `[trigger: three_swords_acceptance]` `[factor_trigger: tarot_three_swords AND principle_acceptance]` `[role: 条件分支]` Heartbreak, painful truth, separation, mourning—necessary pain that leads to growth; cannot avoid, must face and integrate; acceptance required for healing. → Upright Meaning
- `[ns_78deg_266]` `[trigger: three_swords_reversed]` `[factor_trigger: tarot_three_swords AND polarity_reversed]` `[role: 例外处理]` Reversed: blocked healing, pushing pain away prevents recovery; mental alienation from refusing to grieve; avoidance makes pain stronger, not weaker. → Reversed Meaning
- `[ns_78deg_267]` `[trigger: swords_cups_three]` `[factor_trigger: tarot_three_swords AND tarot_three_cups]` `[role: 条件分支]` Three of Swords crossed by Three of Cups—acceptance and love can turn pain into joyful memory; embracing life despite loss, transformation through integration. → Transformation Principle
- `[ns_78deg_268]` `[trigger: necessary_pain]` `[factor_trigger: tarot_three_swords AND principle_transformation]` `[role: 总结]` Rain as tears and cleansing—grief processes loss; take sorrow into heart with courage and love; through acceptance, pain transforms into growth. → Core Symbolism
- `[ns_78deg_458]` `[trigger: symmetry_pain]` `[factor_trigger: tarot_three_swords AND symbol_symmetry]` `[role: 条件分支]` Symmetrical composition despite pain—even in heartbreak there is order and potential for peace; suffering has its own geometry, leading toward resolution. → Core Symbolism
- `[ns_78deg_459]` `[trigger: exposed_heart]` `[factor_trigger: tarot_three_swords AND symbol_exposed_heart]` `[role: 条件分支]` Heart exposed and vulnerable—openness to hurt but also to healing; cannot protect against grief without also blocking love; vulnerability as necessary condition for growth. → Core Symbolism
- `[ns_78deg_498]` `[trigger: cleansing_rain]` `[factor_trigger: tarot_three_swords AND symbol_rain]` `[role: 条件分支]` Gray rainy sky as tears and cleansing—grief processes loss; the storm that cleanses what it damages; after the rain, clarity returns. → Visual Elements"""
    normalized_text_zh: str = """"""
    subject: str = "Three of Swords: Heartbreak & Acceptance"
    factor_refs: list = ['teaching', 'existing', 'state', 'existing', 'process', 'existing', 'shadow', 'existing', 'revelation', 'existing']
    
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
        l1_anchor="pt_v1.0.0_three_of_swords__heartbreak____001_L1",
    )
    version: str = "1.0.0"
