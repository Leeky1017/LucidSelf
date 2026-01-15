"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994919
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
    semantic_id="pt_v1.0.0_king_of_cups__emotional_master_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class KingOfCupsEmotionalMaster(SemanticEntry):
    """
    **Visual Elements**:
- King on throne floating on turbulent sea
- Fish ornament around neck (artific...
    """
    
    original_text: str = """**Visual Elements**:
- King on throne floating on turbulent sea
- Fish ornament around neck (artificial)
- Live fish jumping behind throne
- Holds cup like scepter (tool of power, not contemplation)
- Feet don't touch water (unlike Queen)

**English Paraphrase**:

The **King of Cups** represents **emotional mastery through discipline** - creativity channeled into social responsibility and achievement. He has **suppressed playful imagination** to fulfill his role as maintainer of society, yet **creativity remains alive** beneath surface (jumping fish).

**Core Symbolism**:
- **Artificial fish ornament**: Creativity become decorative, not flowing
- **Live fish jumping**: Imagination still alive, pushed to background
- **Throne floating**: Achievement based on creativity, but separated from it
- **Cup held like scepter**: Emotion as tool of power, not self-expression
- **Turbulent sea**: Strong emotions controlled, not eliminated

**Upright Meaning**:
- **Artistic achievement**: Mastery in creative fields
- **Emotional control**: Feelings disciplined, responsibility before expression
- **Business/law/divinity**: Success in socially responsible professions
- **Maturity**: Imagination channeled into useful achievements
- **Hidden emotions**: Troubled feelings beneath calm exterior (Air of Water interpretation)
- **Creative leader**: Uses imagination for others' benefit

**Reversed/Challenged**:
- **Dishonesty/corruption**: Creativity turned to vice, swindling
- **Suppressed emotions emerge**: Calm exterior breaks, violence surfaces
- **Dishonest lover**: Domineering yet untrustworthy
- **Artistic failure**: Work proves insignificant, lacks maturity
- **Dam breaks**: Controlled emotions overwhelm

**完整中文诠释**:
**圣杯国王**=通过纪律的**情感掌握**——创造力引导至社会责任与成就。已**压制嬉戏想象力**以履行维护社会之角色，然**创造力仍在表面下存活**（跳跃的鱼）。**图像元素**：**人工鱼饰品**=创造力变装饰非流动；**活鱼跳跃**=想象力仍活，被推至背景；**漂浮王座**=基于创造力之成就但与之分离；**杯如权杖持**=情感作权力工具非自我表达；**汹涌海洋**=强情感受控非消除。**正位含义**：**艺术成就**（创意成功管理），**情感控制**（掌握感受非压抑），**商业/法律/神职**（领导角色需情感智慧），**成熟**（知何时约束何时表达），**隐藏情感**（深层感受不可见），**创意领袖**（引导他人想象力）。**逆位/挑战**：**不诚实/腐败**（压抑导致欺骗），**压抑情感浮现**（失控爆发），**不诚恋人**（虚假情感承诺），**艺术失败**（创造力无法约束），**水坝决堤**（情感控制崩溃）。**双重本质**：最好=艺术家与领袖，情感智慧服务社会。最坏=情感阉割者，压抑真实自我为成功。跳跃的鱼=希望：即使受控，创造力仍活着。

**Paradox**: Most mature Cups figure is also most separated from Cups essence. **Success requires discipline**, but at cost of spontaneous flow. Compare Queen (integrated) vs King (divided).

**Narrative Snippets**:
- `[ns_78deg_251]` `[trigger: king_cups_mastery]` `[factor_trigger: tarot_king_cups AND state_emotional_mastery]` `[role: 主干]` King of Cups represents emotional mastery through discipline—creativity channeled into social responsibility; he has suppressed playful imagination to fulfill his role. → English Paraphrase
- `[ns_78deg_252]` `[trigger: artificial_fish]` `[factor_trigger: tarot_king_cups AND symbol_artificial_fish]` `[role: 主干依赖]` Artificial fish ornament vs live fish jumping behind—creativity become decorative while imagination remains alive beneath surface, pushed to background. → Core Symbolism
- `[ns_78deg_253]` `[trigger: king_cups_achievement]` `[factor_trigger: tarot_king_cups AND state_artistic_achievement]` `[role: 条件分支]` Artistic achievement, emotional control—feelings disciplined, responsibility before expression; mastery in creative or socially responsible professions. → Upright Meaning
- `[ns_78deg_254]` `[trigger: throne_on_sea]` `[factor_trigger: tarot_king_cups AND symbol_floating_throne]` `[role: 条件分支]` Throne floating on turbulent sea, cup held like scepter—achievement based on creativity but separated from it; emotion as tool of power, not self-expression. → Core Symbolism
- `[ns_78deg_255]` `[trigger: king_cups_reversed]` `[factor_trigger: tarot_king_cups AND polarity_reversed]` `[role: 例外处理]` Reversed: suppressed emotions emerge violently; dishonesty and corruption; calm exterior breaks—the dam bursts; artistic failure. → Reversed Meaning
- `[ns_78deg_256]` `[trigger: mastery_paradox]` `[factor_trigger: tarot_king_cups AND principle_discipline_cost]` `[role: 总结]` Paradox: most mature Cups figure is also most separated from Cups essence—success requires discipline at cost of spontaneous flow; Queen integrated, King divided. → Paradox
- `[ns_78deg_514]` `[trigger: turbulent_sea_control]` `[factor_trigger: tarot_king_cups AND symbol_turbulent_sea]` `[role: 条件分支]` Throne floating on turbulent sea—strong emotions controlled not eliminated; the waters rage but throne remains stable; mastery not through denial but through containment. → Core Symbolism
- `[ns_78deg_515]` `[trigger: jumping_fish_hope]` `[factor_trigger: tarot_king_cups AND symbol_jumping_fish]` `[role: 条件分支]` Live fish jumping behind throne—imagination remains alive even when suppressed; hope that spontaneity can return; creative essence persists beneath surface. → Core Symbolism
- `[ns_78deg_516]` `[trigger: feet_not_touching]` `[factor_trigger: tarot_king_cups AND symbol_separated_feet]` `[role: 条件分支]` Feet don't touch water unlike Queen—separated from emotional source; success achieved at cost of direct feeling connection; authority requires distance. → Visual Elements
- `[ns_78deg_517]` `[trigger: cup_as_scepter]` `[factor_trigger: tarot_king_cups AND symbol_cup_scepter]` `[role: 条件分支]` Cup held like scepter—emotion as tool of power rather than self-expression; feelings channeled into leadership function; the personal made institutional. → Core Symbolism"""
    normalized_text_zh: str = """"""
    subject: str = "King of Cups: Emotional Mastery & Discipline"
    factor_refs: list = ['attainment', 'existing', 'role', 'existing', 'shadow', 'existing', 'paradox', 'existing', 'potential', 'existing']
    
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
        l1_anchor="pt_v1.0.0_king_of_cups__emotional_master_001_L1",
    )
    version: str = "1.0.0"
