"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.113448
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
    semantic_id="tis_v1.0.0_scorpio___the_transformer__fix_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class ScorpioTheTransformerFix(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Fixed Water | Sustained ...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Fixed Water | Sustained depth | Element |
| Death-Rebirth | Transformation | Core cycle |
| Penetration | See through | Function |
| Regeneration | Renewal | Goal |

**Source Text**: "The Scorpion/Eagle/Phoenix. Scorpio has come to master transformation—learning nothing lasts forever, all forms dissolve, in dissolution lies renewal seed. The endpoint is regeneration: capacity to die psychologically and be reborn, again and again."

**English Paraphrase**: **Scorpio** = **Fixed Water** embodying **depth, intensity, and transformative power**. Archetype: shaman diving beneath surfaces, mastering death-rebirth cycles.

**Core**: Penetration (see through masks), courage (into darkness/pain/taboo), magnetism (intense charisma). **Shadow**: Vengefulness (strike back when hurt), obsession (fixated on wound), control (manipulate from distrust). **Challenge**: Transform without destroying; use intensity for healing not harm.

**Chinese**: 天蝎座=固定水象体现深度、强度和转化力。核心：洞察、勇气、磁力。阴影：报复、执念、控制。挑战：不破坏地转化；用强度疗愈非伤害。

**East**: 天蝎↔壬水阳刚/七杀转化 (yang water transformation)

#### Narrative Snippets

- `[ns_innersky_scorpio_001]` `[trigger: sign_scorpio]` `[factor_trigger: sign_scorpio AND element_water]` `[role: 主干]` The Scorpion/Eagle/Phoenix. Scorpio has come to master transformation—learning nothing lasts forever, all forms dissolve, in dissolution lies renewal seed. → The Inner Sky Ch.4 #Scorpio
- `[ns_innersky_scorpio_002]` `[trigger: sign_scorpio AND astro_strength]` `[factor_trigger: astro_sign_scorpio]` `[role: 主干依赖]` The endpoint is regeneration: capacity to die psychologically and be reborn, again and again. Penetration, courage into darkness, magnetic intensity. → The Inner Sky Ch.4 #Scorpio
- `[ns_innersky_scorpio_003]` `[trigger: sign_scorpio AND astro_shadow]` `[factor_trigger: astro_sign_scorpio AND astro_state_dysfunction]` `[role: 条件分支]` Shadow: vengefulness (strike back when hurt), obsession (fixated on wound), control (manipulate from distrust). → The Inner Sky Ch.4 #Scorpio
- `[ns_innersky_scorpio_004]` `[trigger: sign_scorpio AND astro_challenge]` `[factor_trigger: astro_sign_scorpio]` `[role: 总结]` Transform without destroying; use intensity for healing not harm. Rise from ashes as Phoenix rather than strike as Scorpion. → The Inner Sky Ch.4 #Scorpio"""
    normalized_text_zh: str = """"""
    subject: str = "Scorpio - The Transformer (Fixed Water)"
    factor_refs: list = ['new_candidate', 'sign_scorpio', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_scorpio___the_transformer__fix_001_L1",
    )
    version: str = "1.0.0"
