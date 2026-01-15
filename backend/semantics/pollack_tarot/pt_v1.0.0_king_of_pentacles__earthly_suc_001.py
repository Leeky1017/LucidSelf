"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.995106
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
    semantic_id="pt_v1.0.0_king_of_pentacles__earthly_suc_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class KingOfPentaclesEarthlySuc(SemanticEntry):
    """
    **Visual Elements**:
- King seated casually on throne
- Bulls on throne (Taurus, Earth sign)
- Looks...
    """
    
    original_text: str = """**Visual Elements**:
- King seated casually on throne
- Bulls on throne (Taurus, Earth sign)
- Looks fondly at pentacle
- Castle and vines (prosperity)
- Comfortable, satisfied demeanor

**English Paraphrase**:

The **King of Pentacles** represents **successful manifestation in material world** - the business leader, capable professional, person who has achieved tangible success and **enjoys it**. Unlike Kings of Wands/Cups (frustrated by responsibility), he is **comfortable in his role**.

**Core Symbolism**:
- **Casual sitting**: Satisfied, not striving
- **Fond regard for pentacle**: Appreciates achievements without greed
- **Bulls**: Earth sign Taurus, stubborn persistence, material strength
- **Vines/castle**: Accumulated prosperity, established success
- **Resembles Fool**: Successful Fool - journey completed in material realm

**Upright Meaning**:
- **Material success**: Wealth, career achievement, financial security
- **Business acumen**: Practical wisdom, capable management
- **Generosity**: Shares prosperity, not hoarding
- **Reliability**: Dependable, solid, trustworthy
- **Enjoys life**: Appreciates physical pleasures - food, comfort, nature
- **Patience**: Builds slowly, persistently over time

**Reversed/Challenged**:
- **Corruption**: Uses success for vice
- **Materialism**: Money becomes sole value
- **Stubbornness**: Earth固 becomes obstinate
- **Dullness**: Loses joy, becomes routine
- **Financial failure**: Success crumbles, poor management

**完整中文诠释**:
**星币国王**=**物质世界中的成功显化**——商业领袖、有能力的专业人士、已达成有形成功并**享受它**的人。不同于权杖/圣杯国王（因责任沮丧），他在角色中**舒适**。**图像元素**：**随意坐**=满足，非奋斗；**深情看星币**=欣赏成就无贪婪；**公牛**=土相金牛，固执坚持，物质力量；**藤蔓/城堡**=积累繁荣，既定成功；**类似愚者**=成功的愚者——物质领域完成旅程。**正位含义**：**物质成功**（财富、事业成就、财务安全），**商业头脑**（实际智慧，有能力管理），**慷慨**（分享繁荣，不囤积），**可靠**（可依赖、坚实、值得信赖），**享受生活**（欣赏身体愉悦——食物、舒适、自然），**耐心**（缓慢、持续地随时间建造）。**逆位/挑战**：**腐败**（利用成功于罪恶），**唯物主义**（金钱成为唯一价值），**固执**（土之坚固变成固执），**乏味**（失去喜悦，变成例行），**财务失败**（成功崩溃，管理不善）。**人格类型**：**成功企业家**、**成熟专业人士**、**土地拥有者**。已经成就且可以放松享受。代表土之礼物（繁荣、稳定）而无其危险（停滞、贪婪）。

**Personality Type**: The **successful entrepreneur**, **established professional**, **land owner**. Has achieved and can relax into enjoyment. Represents Earth's gift (prosperity, stability) without its danger (stagnation, greed).

**Narrative Snippets**:
- `[ns_78deg_296]` `[trigger: king_pentacles_success]` `[factor_trigger: tarot_king_pentacles AND state_material_success]` `[role: 主干]` King of Pentacles represents successful manifestation in material world—business leader who has achieved tangible success and enjoys it; comfortable in his role, unlike frustrated Kings of Wands/Cups. → English Paraphrase
- `[ns_78deg_297]` `[trigger: bulls_throne]` `[factor_trigger: tarot_king_pentacles AND symbol_bulls]` `[role: 主干依赖]` Casual sitting with bulls on throne—Taurus Earth sign, stubborn persistence; fond regard for pentacle appreciating achievements without greed; vines and castle showing accumulated prosperity. → Core Symbolism
- `[ns_78deg_298]` `[trigger: king_pentacles_prosperity]` `[factor_trigger: tarot_king_pentacles AND state_prosperity]` `[role: 条件分支]` Material success—wealth, career achievement, financial security; business acumen with practical wisdom; generosity sharing prosperity rather than hoarding; reliability and patience. → Upright Meaning
- `[ns_78deg_299]` `[trigger: king_pentacles_reversed]` `[factor_trigger: tarot_king_pentacles AND polarity_reversed]` `[role: 例外处理]` Reversed: corruption using success for vice; materialism making money sole value; stubbornness becoming obstinate; dullness losing joy; financial failure and poor management. → Reversed Meaning
- `[ns_78deg_300]` `[trigger: successful_fool]` `[factor_trigger: tarot_king_pentacles AND archetype_successful_fool]` `[role: 总结]` Resembles Fool—successful Fool with journey completed in material realm; represents Earth's gift (prosperity, stability) without its danger (stagnation, greed). → Personality Type
- `[ns_78deg_412]` `[trigger: vines_castle]` `[factor_trigger: tarot_king_pentacles AND symbol_vines_castle]` `[role: 条件分支]` Vines and castle—accumulated prosperity, established success; patient building over time produces lasting structures; wealth that grows naturally. → Core Symbolism
- `[ns_78deg_413]` `[trigger: comfortable_role]` `[factor_trigger: tarot_king_pentacles AND state_comfortable_achievement]` `[role: 条件分支]` Comfortable in his role unlike other frustrated Kings—enjoys success without guilt; casual sitting showing satisfaction not continued striving; has achieved and can relax. → Personality Type
- `[ns_78deg_478]` `[trigger: fond_regard_pentacle]` `[factor_trigger: tarot_king_pentacles AND attitude_appreciation]` `[role: 条件分支]` Looks fondly at pentacle—appreciates achievements without greed or anxiety; healthy relationship with wealth where money serves life rather than dominates it. → Core Symbolism
- `[ns_78deg_509]` `[trigger: patient_builder]` `[factor_trigger: tarot_king_pentacles AND principle_patience]` `[role: 条件分支]` Builds slowly, persistently over time—Taurus determination; not flash success but lasting prosperity; foundation laid stone by stone until castle stands. → Upright Meaning"""
    normalized_text_zh: str = """"""
    subject: str = "King of Pentacles: Earthly Success"
    factor_refs: list = ['attainment', 'existing', 'faculty', 'existing', 'quality', 'existing', 'state', 'existing', 'condition', 'existing']
    
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
        l1_anchor="pt_v1.0.0_king_of_pentacles__earthly_suc_001_L1",
    )
    version: str = "1.0.0"
