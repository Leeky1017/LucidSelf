"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994742
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
    semantic_id="pt_v1.0.0_queen_of_wands__warm_passionat_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class QueenOfWandsWarmPassionat(SemanticEntry):
    """
    **Visual Elements**:
- Queen seated firmly on throne, legs apart (unique among Queens)
- Black cat a...
    """
    
    original_text: str = """**Visual Elements**:
- Queen seated firmly on throne, legs apart (unique among Queens)
- Black cat at feet
- Sunflower (sun symbol)
- Flowering crown
- Desert landscape
- Confident, grounded posture

**English Paraphrase**:

The **Queen of Wands** represents **fire appreciation** rather than fire command - warm, passionate engagement with life, confident in her sexuality and power without needing to dominate. She is **planted in her throne**, fully embodied, radiating solar warmth.

**Core Symbolism**:
- **Legs apart**: Sexual confidence, groundedness, power
- **Black cat**: Traditional witch's familiar - nature protects those who love it joyously
- **Sunflower**: Follows sun, embodies solar warmth and growth
- **Flowering crown**: Natural authority through vitality
- **Desert + abundance**: Creates oasis through her presence

**Upright Meaning**:
- **Warm confidence**: Self-assured without arrogance
- **Sexual vitality**: Comfortable in body, attractive through naturalness
- **Generous spirit**: Gives freely from abundance
- **Honest & sincere**: Like King, values truth over manipulation
- **Attracts joy**: Life seems to respond to her positive energy
- **Practical magic**: Manifestation through loving engagement

**Reversed/Challenged**:
- **Demands fairness**: When life doesn't reciprocate, can turn bitter
- **Jealousy/deceit**: Good nature sours under too much opposition
- **Unfaithfulness**: Seeks warmth elsewhere when current situation cold
- **Energy depleted**: Burnout from giving without receiving

**完整中文诠释**:
**权杖皇后**=**火之欣赏非火之命令**——温暖、热情投入生活，性自信与力量无需统治。**图像元素**：**稳固就座**=完全体现自我，散发阳光温暖；**腿分开**=性自信、扎根、力量；**黑猫**=传统女巫熟魔（自然保护欢乐爱它者）；**向日葵**=跟随太阳，体现阳光温暖成长。不同于国王命令式领导，皇后**邀请他人进入温暖**，人们因她的光辉而自然被吸引。**正位含义**：**温暖自信**（自在于自身力量），**性活力**（肉身欢乐无羞耻），**慷慨精神**（大方给予时间/能量/欢乐），**诚实真诚**（如国王，重视真理胜过操纵），**吸引喜悦**（生活似乎回应她的正能量），**实用魔法**（通过爱的投入而显化）。**逆位/挑战**：**要求公平**（生活不回报时可变苦涩），**嫉妒/欺骗**（善良本性在过多对抗下变酸），**不忠**（当前情境冷漠时在别处寻求温暖），**能量耗竭**（给予无接受而倦怠）。**性别注释**：如所有宫廷牌，可代表任何性别。品质关于**火元素的接近方式**（接纳/整合）而非生理性别。

**Gender Note**: Like all court cards, can represent any gender. Qualities are about **approach to fire element** (receptive/integrative) rather than biological sex.

**In Readings**:
- Person: Warm, confident presence in life
- Quality: Embody passionate engagement with life
- Advice: Trust your natural warmth and generosity
- Situation: Fertile, creative period

**Narrative Snippets**:
- `[ns_78deg_187]` `[trigger: queen_wands_warmth]` `[factor_trigger: tarot_queen_wands AND state_warmth]` `[role: 主干]` Queen of Wands represents fire appreciation rather than fire command—warm, passionate engagement with life, confident in sexuality without needing to dominate. → English Paraphrase
- `[ns_78deg_188]` `[trigger: black_cat_familiar]` `[factor_trigger: tarot_queen_wands AND symbol_black_cat]` `[role: 条件分支]` Black cat at her feet—traditional witch's familiar; nature protects those who love it joyously; magical connection to life force. → Core Symbolism
- `[ns_78deg_189]` `[trigger: queen_wands_sexuality]` `[factor_trigger: tarot_queen_wands AND state_sexual_confidence]` `[role: 主干]` Legs apart, unique among Queens—sexual confidence, groundedness, power; fully embodied, radiating solar warmth without shame. → Visual Elements
- `[ns_78deg_190]` `[trigger: queen_wands_reversed]` `[factor_trigger: tarot_queen_wands AND polarity_reversed]` `[role: 条件分支]` Reversed: demands fairness when life doesn't reciprocate; good nature sours, jealousy emerges; burnout from giving without receiving. → Reversed Meaning
- `[ns_78deg_191]` `[trigger: fire_appreciation]` `[factor_trigger: tarot_queen_wands AND principle_fire_appreciation]` `[role: 总结]` Unlike King who commands fire, Queen invites others into her warmth—people naturally drawn to her radiance; creates oasis in desert. → Personality Type
- `[ns_78deg_402]` `[trigger: sunflower_symbol]` `[factor_trigger: tarot_queen_wands AND symbol_sunflower]` `[role: 条件分支]` Sunflower follows sun, embodies solar warmth and growth—flowering crown as natural authority through vitality, not through position. → Visual Elements
- `[ns_78deg_403]` `[trigger: practical_magic]` `[factor_trigger: tarot_queen_wands AND principle_manifestation]` `[role: 条件分支]` Practical magic through loving engagement—manifestation by warmth and presence; attracts joy because life responds to positive energy. → Upright Meaning
- `[ns_78deg_480]` `[trigger: desert_oasis]` `[factor_trigger: tarot_queen_wands AND symbol_oasis]` `[role: 条件分支]` Creates oasis in desert through her presence—where she is, life flourishes; generous spirit gives freely from inner abundance; transforms barren into fertile. → Personality Type
- `[ns_78deg_524]` `[trigger: legs_apart_power]` `[factor_trigger: tarot_queen_wands AND symbol_seated_posture]` `[role: 条件分支]` Seated firmly with legs apart, unique among Queens—sexual confidence without shame; planted in throne, fully embodied; power through presence. → Visual Elements
- `[ns_78deg_525]` `[trigger: flowering_crown]` `[factor_trigger: tarot_queen_wands AND symbol_flowering_crown]` `[role: 条件分支]` Flowering crown and sunflower—natural authority through vitality, not position; she blooms because that is her nature; solar warmth radiating. → Core Symbolism"""
    normalized_text_zh: str = """"""
    subject: str = "Queen of Wands: Warm Passionate Mastery"
    factor_refs: list = ['state', 'existing', 'quality', 'existing', 'approach', 'existing', 'capacity', 'existing', 'presence', 'existing']
    
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
        l1_anchor="pt_v1.0.0_queen_of_wands__warm_passionat_001_L1",
    )
    version: str = "1.0.0"
