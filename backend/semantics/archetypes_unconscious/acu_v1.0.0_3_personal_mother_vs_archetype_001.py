"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491539
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
    semantic_id="acu_v1.0.0_3_personal_mother_vs_archetype_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 3PersonalMotherVsArchetype(SemanticEntry):
    """
    **Source Text** (¶159-160, Lines 2537-2580):

> [159] Although the figure of the mother as it appear...
    """
    
    original_text: str = """**Source Text** (¶159-160, Lines 2537-2580):

> [159] Although the figure of the mother as it appears in folklore is more or less universal, this image changes markedly when it appears in the individual psyche. The personal mother looms so large in personalistic psychologies that they never got beyond it. My view differs: I attribute to the personal mother only a limited aetiological significance. All those influences do not come from the mother herself, but from the archetype projected upon her, which gives her mythological background and invests her with authority and numinosity.
>
> [160] Archetypes are among the inalienable assets of every psyche. They form the "treasure in the realm of shadowy thoughts" of which Kant spoke. An archetype is in no sense just an annoying prejudice; it becomes so only when in the wrong place. Archetypal images are among the highest values of the human psyche—they have peopled the heavens of all races. Our task is not to deny the archetype, but to dissolve projections, restoring contents to the individual who has lost them.

**English Paraphrase**:
- Personal mother = limited aetiological significance
- True influence = archetype projected upon her
- Archetype gives mythological background + numinosity
- Archetypes = inalienable assets, highest values
- Task = dissolve projections, restore contents to individual

**中文诠释**:
- 个人母亲 = 有限的病因学意义
- 真正影响 = 投射于其上的原型
- 原型赋予神话背景 + 神圣性
- 原型 = 不可剥夺的资产，最高价值
- 任务 = 解除投射，将内容归还个体

**Narrative Snippets**:
- `[ns_cw9i_III_159]` `[trigger: mother_projection]` `[factor_trigger: jung_mother AND jung_archetype]` `[role: 主干]` Personal mother has only limited significance—true influence is the archetype projected upon her. → ¶159
- `[ns_cw9i_III_160]` `[trigger: dissolve_projection]` `[factor_trigger: jung_projection AND jung_archetype]` `[role: 主干依赖]` Archetypes are inalienable assets; task is to dissolve projections, not deny archetypes. → ¶160"""
    normalized_text_zh: str = """"""
    subject: str = "3 Personal Mother vs Archetype (¶159-160)"
    factor_refs: list = []
    
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_3_personal_mother_vs_archetype_001_L1",
    )
    version: str = "1.0.0"
