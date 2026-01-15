"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.995143
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
    semantic_id="pt_v1.0.0_queen_of_pentacles__nurturing__001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class QueenOfPentaclesNurturing(SemanticEntry):
    """
    **Visual Elements**:
- Queen in lush garden/nature
- Holding pentacle lovingly on lap
- Rabbit at fe...
    """
    
    original_text: str = """**Visual Elements**:
- Queen in lush garden/nature
- Holding pentacle lovingly on lap
- Rabbit at feet (fertility)
- Roses and abundant vegetation
- Comfortable throne in nature
- Gazing at pentacle with appreciation

**English Paraphrase**:

The **Queen of Pentacles** represents **nurturing through material means** - the provider, nurturer who creates security and abundance for others. She embodies **practical love** - expressing care through tangible acts like providing food, comfort, home.

**Core Symbolism**:
- **Lush garden**: Abundance created through care
- **Pentacle on lap**: Wealth held gently, not grasped
- **Rabbit**: Fertility, natural abundance, gentle strength
- **Roses**: Beauty and love in material form
- **Throne in nature**: Comfort grounded in natural world

**Upright Meaning**:
- **Practical nurturing**: Caring through material provision
- **Financial security**: Creates abundance for self and others
- **Domestic skill**: Excellent homemaker, provider
- **Generosity**: Shares resources freely
- **Business sense**: Combines warmth with practicality
- **Grounded**: Solid, reliable, present

**Reversed/Challenged**:
- **Smothering**: Nurturing becomes controlling
- **Materialism**: Values物质 over relationships
- **Dependency**: Creates or enables unhealthy dependence
- **Financial insecurity**: Cannot provide or manage resources
- **Neglect**: Too focused on material, neglects emotional needs

**完整中文诠释**:
**星币皇后**=通过物质手段**滋养**——提供者、滋养者为他人创造安全与丰盛。她体现**实际之爱**——通过有形行为如提供食物、舒适、家园表达关怀。**图像元素**：**郁郁葱葱花园**=通过关怀创造丰盛；**膝上星币**=财富温柔持有，非抓握；**兔子**=生育力、自然丰盛、温和力量；**玫瑰**=物质形式的美与爱；**自然中王座**=扎根自然世界的舒适。**正位含义**：**实际滋养**（通过物质供给关怀），**财务安全**（为自己和他人创造丰盛），**家务技能**（优秀的持家者、供给者），**慷慨**（自由分享资源），**商业头脑**（结合温暖与实际），**扎根**（坚实、可靠、临在）。**逆位/挑战**：**窒息**（滋养变成控制），**唯物主义**（重视物质胜过关系），**依赖**（创造或助长不健康依赖），**财务不安全**（无法提供或管理资源），**忽视**（过于专注物质，忽视情感需求）。**原型**：**大地母亲**、**供给者**、**持家者**。不仅是家务，而是结合商业头脑与滋养——能以同等技能管理家庭或企业。

**Archetype**: The **Earth Mother**, **provider**, **homemaker**. Not just domestic but combines business sense with nurturing - can run household or business with equal skill.

**Narrative Snippets**:
- `[ns_78deg_311]` `[trigger: queen_pentacles_nurture]` `[factor_trigger: tarot_queen_pentacles AND state_nurturing_abundance]` `[role: 主干]` Queen of Pentacles represents nurturing through material means—the provider creating security and abundance; practical love expressed through tangible acts like food, comfort, home. → English Paraphrase
- `[ns_78deg_312]` `[trigger: lush_garden_queen]` `[factor_trigger: tarot_queen_pentacles AND symbol_lush_garden]` `[role: 主干依赖]` Queen in lush garden holding pentacle lovingly on lap—abundance through care; rabbit at feet for fertility; roses for beauty and love in material form; throne comfortable in nature. → Core Symbolism
- `[ns_78deg_313]` `[trigger: queen_pentacles_provider]` `[factor_trigger: tarot_queen_pentacles AND state_provision]` `[role: 条件分支]` Practical nurturing—caring through material provision; financial security for self and others; domestic skill; generosity sharing resources freely; business sense combined with warmth. → Upright Meaning
- `[ns_78deg_314]` `[trigger: queen_pentacles_reversed]` `[factor_trigger: tarot_queen_pentacles AND polarity_reversed]` `[role: 例外处理]` Reversed: smothering where nurturing becomes controlling; materialism over relationships; creating unhealthy dependence; financial insecurity; neglecting emotional needs for material focus. → Reversed Meaning
- `[ns_78deg_315]` `[trigger: earth_mother_archetype]` `[factor_trigger: tarot_queen_pentacles AND archetype_earth_mother]` `[role: 总结]` Earth Mother archetype—provider, homemaker; not just domestic but combines business sense with nurturing; can run household or business with equal skill and care. → Archetype
- `[ns_78deg_410]` `[trigger: rabbit_fertility]` `[factor_trigger: tarot_queen_pentacles AND symbol_rabbit]` `[role: 条件分支]` Rabbit at feet—fertility, natural abundance, gentle strength; nature rewards her care; wealth increases through nurturing rather than grasping. → Core Symbolism
- `[ns_78deg_411]` `[trigger: pentacle_gentle_hold]` `[factor_trigger: tarot_queen_pentacles AND symbol_pentacle_lap]` `[role: 条件分支]` Pentacle held lovingly on lap not grasped—wealth appreciates when treated with care; money serves love, not love serving money. → Core Symbolism
- `[ns_78deg_482]` `[trigger: throne_in_nature]` `[factor_trigger: tarot_queen_pentacles AND symbol_natural_throne]` `[role: 条件分支]` Throne comfortable in nature—not separate from earth but embedded in it; the garden grows around her because she participates in nature's cycles, not commanding from above. → Visual Elements
- `[ns_78deg_536]` `[trigger: roses_material_love]` `[factor_trigger: tarot_queen_pentacles AND symbol_roses]` `[role: 条件分支]` Roses and abundant vegetation—beauty and love expressed in material form; aesthetic care for environment; love made visible through what surrounds her. → Visual Elements
- `[ns_78deg_537]` `[trigger: grounded_presence]` `[factor_trigger: tarot_queen_pentacles AND state_grounded_presence]` `[role: 条件分支]` Solid, reliable, present—grounded in her body and environment; the one you can count on; stability that others draw strength from. → Upright Meaning"""
    normalized_text_zh: str = """"""
    subject: str = "Queen of Pentacles: Nurturing Abundance"
    factor_refs: list = ['quality', 'existing', 'expression', 'existing', 'archetype', 'existing', 'integration', 'existing', 'role', 'existing']
    
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
        l1_anchor="pt_v1.0.0_queen_of_pentacles__nurturing__001_L1",
    )
    version: str = "1.0.0"
