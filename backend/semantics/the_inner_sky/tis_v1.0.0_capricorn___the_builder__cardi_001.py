"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.113477
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
    semantic_id="tis_v1.0.0_capricorn___the_builder__cardi_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class CapricornTheBuilderCardi(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Cardinal Earth | Initiat...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Cardinal Earth | Initiating structure | Element |
| Systematic Building | Step-by-step | Method |
| Integrity | Actions=values | Goal |
| Long Game | Patience | Approach |

**Source Text**: "The Mountain Goat. Capricorn has come to achieve mastery—build something enduring, earn recognition through accomplishment, reach top through merit. The endpoint is integrity: satisfaction of work well done, goals honestly achieved."

**English Paraphrase**: **Capricorn** = **Cardinal Earth** embodying **achievement, discipline, and systematic building**. Archetype: elder/CEO climbing mountain one steady step at a time.

**Core**: Systematic building (plan/work/progress steadily), discipline (delay gratification, endure hardship), patience (play long game), realism (see as is), authority (command respect). **Shadow**: Emotional coldness (forget feelings), workaholism (all duty no joy), status anxiety (desperate recognition-seeking). **Challenge**: Summit not the point—the climb is; find meaning in work itself.

**Chinese**: 摩羯座=基本土象体现成就、纪律和系统建造。核心：系统建造、纪律、耐心、现实、权威。阴影：情感冷漠、工作狂、地位焦虑。挑战：顶峰非重点——攀爬是；在工作本身找意义。

**East**: 摩羯↔戊土阳刚/正官纪律 (yang earth discipline)

#### Narrative Snippets

- `[ns_innersky_capricorn_001]` `[trigger: sign_capricorn]` `[factor_trigger: sign_capricorn AND element_earth]` `[role: 主干]` The Mountain Goat. Capricorn has come to achieve mastery—build something enduring, earn recognition through accomplishment, reach top through merit. → The Inner Sky Ch.4 #Capricorn
- `[ns_innersky_capricorn_002]` `[trigger: sign_capricorn AND astro_strength]` `[factor_trigger: astro_sign_capricorn]` `[role: 主干依赖]` The endpoint is integrity: satisfaction of work well done, goals honestly achieved. Systematic building, discipline, patience, realism, natural authority. → The Inner Sky Ch.4 #Capricorn
- `[ns_innersky_capricorn_003]` `[trigger: sign_capricorn AND astro_shadow]` `[factor_trigger: astro_sign_capricorn AND astro_state_dysfunction]` `[role: 条件分支]` Shadow: emotional coldness (forget feelings amid duty), workaholism (all duty no joy), status anxiety (desperate recognition-seeking). → The Inner Sky Ch.4 #Capricorn
- `[ns_innersky_capricorn_004]` `[trigger: sign_capricorn AND astro_challenge]` `[factor_trigger: astro_sign_capricorn]` `[role: 总结]` Summit not the point—the climb is. Find meaning in work itself, not just in arrival at the goal. → The Inner Sky Ch.4 #Capricorn"""
    normalized_text_zh: str = """"""
    subject: str = "Capricorn - The Builder (Cardinal Earth)"
    factor_refs: list = ['sign_capricorn', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="tis_v1.0.0_capricorn___the_builder__cardi_001_L1",
    )
    version: str = "1.0.0"
