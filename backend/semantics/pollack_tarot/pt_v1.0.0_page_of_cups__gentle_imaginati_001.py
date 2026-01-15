"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994833
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
    semantic_id="pt_v1.0.0_page_of_cups__gentle_imaginati_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class PageOfCupsGentleImaginati(SemanticEntry):
    """
    **Visual Elements**:
- Youth gazing at fish emerging from cup
- Amused, gentle expression
- Calm wat...
    """
    
    original_text: str = """**Visual Elements**:
- Youth gazing at fish emerging from cup
- Amused, gentle expression
- Calm waters
- Contemplative, peaceful scene

**English Paraphrase**:

The **Page of Cups** represents **gentle imagination** and **developing intuition**. The fish of imagination emerges from the cup to greet the Page, who observes it with amused wonder. This is **contemplation for its own sake**, undisturbed by demands or desires.

**Core Symbolism**:
- **Fish in cup**: Imagination/psychic talent becoming visible
- **Mutual gaze**: Dialogue with unconscious, playful relationship
- **Youth**: Child-like openness, beginner's mind
- **Calm demeanor**: No conflict with responsibility or desire

**Upright Meaning**:
- **Psychic sensitivity**: Developing intuitive abilities
- **Gentle creativity**: Imagination bubbling up naturally
- **Emotional message**: News of feelings, tender communication
- **Student of emotion**: Learning about inner world
- **Playful contemplation**: Fantasy as its own justification
- **Innocence**: Unspoiled by cynicism or harsh experience

**Reversed/Challenged**:
- **Fear of imagination**: Fish seems threatening not amusing
- **Psychic overwhelm**: Talents emerge too rapidly, frightening
- **Immaturity**: Cannot handle emotional responsibilities
- **Emotional deception**: Message false or manipulative
- **Blocked intuition**: Unable to access inner knowing

**完整中文诠释**:
**圣杯侍从**=**温柔想象力**与**发展中的直觉**。想象之鱼从杯中浮现迎接侍从，侍从以愉快惊奇观察。这是**为自身而沉思**，不受要求或欲望干扰。**图像元素**：**杯中鱼**=想象力/灵媒天赋变得可见；**相互凝视**=与无意识对话，玩耍关系；**青年**=孩童般开放，初学者心；**平静举止**=与责任或欲望无冲突。**正位含义**：**灵媒敏感**（发展直觉能力），**温柔创造力**（想象力自然涌现），**情感信息**（感受的消息，温柔沟通），**情感学生**（学习内在世界），**嬉戏沉思**（幻想本身即为理由），**天真无邪**（未被愤世嫉俗或严酷经验破坏）。**逆位/挑战**：**恐惧想象力**（鱼显得威胁而非有趣），**灵媒淹没**（才能出现太快，令人恐惧），**不成熟**（无法处理情感责任），**情感欺骗**（消息虚假或操纵），**直觉受阻**（无法接近内在知晓）。**在解读中**：具有灵媒天赋的年轻人，关于情感/直觉事务的消息，温柔自我探索的时间，开始发展内在觉知。

**In Readings**:
- Young person with psychic gifts
- Message about emotional/intuitive matters
- Time for gentle self-exploration
- Beginning to develop inner awareness

**Narrative Snippets**:
- `[ns_78deg_221]` `[trigger: page_cups_fish]` `[factor_trigger: tarot_page_cups AND symbol_fish_cup]` `[role: 主干]` Page of Cups with fish emerging from cup—imagination/psychic talent becoming visible; the youth gazes with pleased surprise at what surfaces from unconscious. → Visual Elements
- `[ns_78deg_222]` `[trigger: page_cups_dialogue]` `[factor_trigger: tarot_page_cups AND state_unconscious_dialogue]` `[role: 主干依赖]` Mutual gaze between page and fish—dialogue with unconscious, playful relationship; contemplation for its own sake, not driven by demands or desire. → Core Symbolism
- `[ns_78deg_223]` `[trigger: page_cups_sensitivity]` `[factor_trigger: tarot_page_cups AND state_psychic_sensitivity]` `[role: 条件分支]` Psychic sensitivity developing—intuitive abilities emerging naturally; emotional messenger bringing news of inner world, tender communication. → Upright Meaning
- `[ns_78deg_224]` `[trigger: page_cups_innocence]` `[factor_trigger: tarot_page_cups AND state_emotional_innocence]` `[role: 条件分支]` Innocence unspoiled by cynicism—childlike openness to imagination; fantasy as its own justification, play without demanding purpose. → Upright Meaning
- `[ns_78deg_225]` `[trigger: page_cups_reversed]` `[factor_trigger: tarot_page_cups AND polarity_reversed]` `[role: 例外处理]` Reversed: fish seems threatening not amusing; psychic overwhelm—talents emerge too rapidly; blocked intuition unable to access inner knowing. → Reversed Meaning
- `[ns_78deg_226]` `[trigger: page_cups_student]` `[factor_trigger: tarot_page_cups AND function_student]` `[role: 总结]` Student of emotion learning about inner world—beginner's mind open to what surfaces; developing awareness through gentle self-exploration. → In Readings
- `[ns_78deg_444]` `[trigger: calm_waters]` `[factor_trigger: tarot_page_cups AND symbol_calm_water]` `[role: 条件分支]` Calm waters surrounding the Page—peaceful emotional state; no conflict with responsibility or desire; contemplation undisturbed by outer demands. → Visual Elements
- `[ns_78deg_445]` `[trigger: playful_fantasy]` `[factor_trigger: tarot_page_cups AND state_playful_contemplation]` `[role: 条件分支]` Playful contemplation—fantasy as its own justification; imagination bubbling up naturally without purpose beyond delight; the joy of inner discovery. → Upright Meaning
- `[ns_78deg_526]` `[trigger: amused_wonder]` `[factor_trigger: tarot_page_cups AND state_amused_wonder]` `[role: 条件分支]` Amused, gentle expression gazing at fish—surprised but not frightened by what surfaces from depths; smile of recognition. → Visual Elements
- `[ns_78deg_527]` `[trigger: beginners_mind]` `[factor_trigger: tarot_page_cups AND principle_beginners_mind]` `[role: 条件分支]` Beginner's mind open to what surfaces—child-like openness, not yet knowing what to expect; receiving inner messages fresh. → Core Symbolism"""
    normalized_text_zh: str = """"""
    subject: str = "Page of Cups: Gentle Imagination"
    factor_refs: list = ['faculty', 'existing', 'process', 'existing', 'relationship', 'existing', 'quality', 'existing', 'function', 'existing']
    
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
        l1_anchor="pt_v1.0.0_page_of_cups__gentle_imaginati_001_L1",
    )
    version: str = "1.0.0"
