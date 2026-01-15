"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.076421
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
    semantic_id="bot_v1.0.0_three_of_swords__sorrow__宝剑三_悲_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class ThreeOfSwordsSorrow宝剑三悲(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Binah in Air | Dark Mother in Air | Womb of Chaos |
| Saturn in Libra | Heavy restriction | Exalted but sorrowful |
| Destroyed Rose | Pierced flower | Hope/beauty shattered |
| Storm Night | Brooding darkness | Implacable grief |

**Title**: Lord of Sorrow (悲伤之主)
**Qabalistic**: Binah in Air (气中之理解)
**Astrological**: Saturn in Libra (土星入天秤座)

**Source Text**:
> "Binah, the Great Mother, here rules the realm of Air... not the beneficent Mother completing the Trinity with Kether and Chokmah. She represents the darkness of the Great Sea. This is accentuated by the Celestial Lordship of Saturn in Libra. This card is dark and heavy; it is, so to speak, the womb of Chaos. There is an intense lurking passion to create, but its children are monsters. ... Secrecy is here, and Perversion... The impact has destroyed the rose. In the background, storm broods under implacable night."

**English Paraphrase**:
**Deep Mental Sorrow** – Corresponds to Binah (Understanding/Great Mother) in Air, but here she is the **dark Sea**, not the nurturing Mother. With **Saturn in Libra**, heaviness and restriction enter the airy realm of balance and justice. The great Sword of the Magician pierces and destroys the rose; storm clouds brood under implacable night. This is the **womb of Chaos** in the mind: painful realizations, heartbreak of intellect and conscience, and a sense that creativity has turned monstrous. It is sorrow that cuts deep, exposing the limits of thought and fairness.

**Core**: **Heart‑Mind Ache** – Grief, disappointment, mental anguish, severe truth, the pain of seeing clearly.

**Chinese Explanation**:
**宝剑三（悲伤）**对应空气元素中的**Binah（理解/大母神）**，但此处的大母并非慈爱滋养的一面，而是**黑暗深海**的一面。加上**土星入天秤座**的配置，本应追求平衡与正义的天秤，被土星的**沉重、收缩与限制**压得喘不过气。大剑击碎了玫瑰，背景中乌云翻涌、黑夜无情，象征心智世界中的**混沌子宫**：有强烈的创造冲动，却孕育出扭曲、怪异的结果。这张牌指向**深层的心理与情感创伤**——被真相刺痛、被不公或破裂关系伤害，理性与情感在痛苦中被迫面对现实的残酷。

**In Readings**: Sorrow, heartbreak, painful truth, mental breakdown, heavy karma, loss that forces deep understanding.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Three of Swords shows Binah as dark Sea, not nurturing Mother. Saturn in Libra brings heavy restriction. Great sword destroys rose. Womb of Chaos in the mind.
- **中文**: Crowley的宝剑三展示Binah作为黑暗之海，非滋养之母。土星入天秤带来沉重限制。大剑击毁玫瑰。心智中的混沌子宫。

**Narrative Snippets**:
- `[ns_thoth_swords_007]` `[trigger: three_swords_sorrow]` `[factor_trigger: thoth_swords_three]` `[role: 主干]` Three of Swords = Lord of Sorrow—Binah as dark Sea, not nurturing Mother; womb of Chaos. → Core
- `[ns_thoth_swords_008]` `[trigger: saturn_libra_heavy]` `[factor_trigger: thoth_swords_three AND planet_saturn_libra]` `[role: 条件分支]` Saturn in Libra—heavy restriction in realm of balance; intense lurking passion creating monsters. → Astrological
- `[ns_thoth_swords_009]` `[trigger: destroyed_rose]` `[factor_trigger: thoth_swords_three AND symbol_destroyed_rose]` `[role: 条件分支]` Great sword destroys rose; storm broods under implacable night—perversion and secrecy. → Visual"""
    normalized_text_zh: str = """"""
    subject: str = "Three of Swords: Sorrow (宝剑三：悲伤)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_swords_three_001', 'tarot_mental_anguish', 'rel_swords_three_002', 'tarot_heartbreak', 'l1_anchor', 'confidence', 'evi_swords_three_001', 'evi_swords_three_002', 'tarot_destroyed_rose', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_swords_three_001', 'tarot_swords_three', 'astro_saturn_libra']
    
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_three_of_swords__sorrow__宝剑三_悲_001_L1",
    )
    version: str = "1.0.0"
