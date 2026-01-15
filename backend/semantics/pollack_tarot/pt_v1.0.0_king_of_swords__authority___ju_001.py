"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.995065
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
    semantic_id="pt_v1.0.0_king_of_swords__authority___ju_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class KingOfSwordsAuthorityJu(SemanticEntry):
    """
    **Visual Elements**:
- King on throne in clouds
- Sword tilted slightly right (action side)
- Two bi...
    """
    
    original_text: str = """**Visual Elements**:
- King on throne in clouds
- Sword tilted slightly right (action side)
- Two birds behind throne
- Resembles Emperor
- Remote, elevated position

**English Paraphrase**:

The **King of Swords** represents **intellectual authority and justice** - the judge, lawmaker, ruler who maintains social order through **force of mind and will**. He is Emperor's representative in real world, embodying **principles of law and structure** in practice.

**Core Symbolism**:
- **Sword tilted right**: Not pure wisdom but wisdom applied to action
- **Throne in clouds**: Remote from daily reality, elevated perspective
- **Two birds**: Mind's ability to soar above, but also remoteness
- **Crown + authority**: Social power, responsibility to maintain order

**Upright Meaning**:
- **Judicial authority**: Judge, lawyer, administrator
- **Intellectual power**: Strong mind, clear reasoning
- **Social justice**: When connected to Justice trump, wise laws
- **Harsh but fair**: Can be cold, but committed to truth
- **Leadership**: Rules through intellect, not emotion
- **Commitment to truth**: Values facts over feelings

**Reversed/Challenged**:
- **Arrogance**: Intellect creates sense of superiority
- **Remote judgment**: Decisions divorced from real needs
- **Cold cruelty**: Harshness without mercy
- **Domineering**: Controlling through logic
- **Abuse of power**: Using authority to harm
- **Tyranny**: Law without compassion

**完整中文诠释**:
**宝剑国王**=**智力权威与正义**——法官、立法者、统治者通过**心智与意志力**维持社会秩序。他是现实世界的皇帝代表，在实践中体现**法律与结构原则**。**图像元素**：**剑右倾**=非纯智慧而是智慧应用于行动；**云中王座**=远离日常现实，升高视角；**两只鸟**=心智的超越能力，但也是遥远；**王冠+权威**=社会权力，维持秩序之责。**正位含义**：**司法权威**（法官、律师、管理者），**智力力量**（强大心智，清晰推理），**社会正义**（当与正义牌连接时，明智法律），**严厉但公平**（可能冷漠，但承诺真理），**领导力**（通过智力而非情感统治），**对真理的承诺**（重视事实胜过感受）。**逆位/挑战**：**傲慢**（智力创造优越感），**遥远判断**（决定脱离真实需求），**冷酷**（严苛无慈悲），**专横**（通过逻辑控制），**滥用权力**（用权威伤害），**暴政**（法律无慈悲）。**双重本质**：最好=正义化身，明智法律，智力正直。最坏=脱离人性的冷漠法官，专横统治者。遥远王座暗示**与被统治者分离**的危险。

**Dual Nature**: Best = Justice incarnate, wise laws, intellectual integrity. Worst = cold judge divorced from humanity, domineering ruler. Remote throne suggests danger of **separation from those he rules**.

**Narrative Snippets**:
- `[ns_78deg_334]` `[trigger: king_swords_authority]` `[factor_trigger: tarot_king_swords AND state_intellectual_authority]` `[role: 主干]` King of Swords represents intellectual authority and justice—the judge, lawmaker, ruler maintaining social order through force of mind and will; Emperor's representative in real world. → English Paraphrase
- `[ns_78deg_335]` `[trigger: sword_tilted_right]` `[factor_trigger: tarot_king_swords AND symbol_tilted_sword]` `[role: 主干依赖]` Sword tilted slightly right—not pure wisdom but wisdom applied to action; throne in clouds showing remote elevated perspective; two birds representing mind's ability to soar above. → Core Symbolism
- `[ns_78deg_336]` `[trigger: king_swords_judge]` `[factor_trigger: tarot_king_swords AND role_judicial]` `[role: 条件分支]` Judicial authority—judge, lawyer, administrator; intellectual power with clear reasoning; harsh but fair, committed to truth; values facts over feelings. → Upright Meaning
- `[ns_78deg_337]` `[trigger: king_swords_reversed]` `[factor_trigger: tarot_king_swords AND polarity_reversed]` `[role: 例外处理]` Reversed: arrogance from intellectual superiority; remote judgment divorced from real needs; cold cruelty and harshness without mercy; tyranny—law without compassion. → Reversed Meaning
- `[ns_78deg_338]` `[trigger: justice_incarnate]` `[factor_trigger: tarot_king_swords AND archetype_justice]` `[role: 总结]` Dual nature: best = Justice incarnate, wise laws, intellectual integrity; worst = cold judge divorced from humanity; remote throne suggests danger of separation from those he rules. → Dual Nature
- `[ns_78deg_418]` `[trigger: throne_clouds_king]` `[factor_trigger: tarot_king_swords AND symbol_throne_clouds]` `[role: 条件分支]` Throne in clouds—remote from daily reality, elevated perspective; danger of disconnection from those he rules; authority that has forgotten humanity. → Core Symbolism
- `[ns_78deg_419]` `[trigger: facts_over_feelings]` `[factor_trigger: tarot_king_swords AND principle_truth_commitment]` `[role: 条件分支]` Values facts over feelings—commitment to truth can become cold; rules through intellect not emotion; leadership with clarity but potentially without compassion. → Upright Meaning
- `[ns_78deg_522]` `[trigger: two_birds_soaring]` `[factor_trigger: tarot_king_swords AND symbol_two_birds]` `[role: 条件分支]` Two birds behind throne—mind's ability to soar above, seeing patterns others miss; yet also remoteness from daily reality. → Visual Elements
- `[ns_78deg_523]` `[trigger: emperor_representative]` `[factor_trigger: tarot_king_swords AND tarot_major_emperor]` `[role: 条件分支]` Emperor's representative in real world—embodying law and structure in daily practice; abstract justice made concrete. → Core Symbolism"""
    normalized_text_zh: str = """"""
    subject: str = "King of Swords: Authority & Justice"
    factor_refs: list = ['power', 'existing', 'role', 'existing', 'quality', 'existing', 'paradox', 'existing', 'pitfall', 'existing']
    
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
        l1_anchor="pt_v1.0.0_king_of_swords__authority___ju_001_L1",
    )
    version: str = "1.0.0"
