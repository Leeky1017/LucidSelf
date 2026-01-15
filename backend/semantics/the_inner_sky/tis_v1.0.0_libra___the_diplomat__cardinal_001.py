"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.113395
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
    semantic_id="tis_v1.0.0_libra___the_diplomat__cardinal_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class LibraTheDiplomatCardinal(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Cardinal Air | Relationa...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Cardinal Air | Relational initiation | Element |
| Partnership | Mutual enhancement | Core drive |
| Mirroring | Reflect others | Function |
| Creative Collaboration | Two wholes | Goal |

**Source Text**: "The Scales. Libra has come to learn the art of partnership—not just romantic, but harmonious mutually beneficial relationships where both parties grow. The endpoint is creative collaboration: two autonomous individuals enhancing each other while remaining themselves."

**English Paraphrase**: **Libra** = **Cardinal Air** embodying **partnership, balance, and aesthetic harmony**. Archetype: diplomat seeking other to create identity through relationship.

**Core**: Mirroring (show others who they are), diplomacy (see both sides), grace (social elegance), fairness (interpersonal justice). **Shadow**: Codependency (lose self in other), indecisiveness (paralyzed by options), passive aggression (smile while undermining). **Challenge**: True partnership requires two whole people, not two halves.

**Chinese**: 天秤座=基本风象体现伙伴、平衡和审美和谐。核心：镜像、外交、优雅、公平。阴影：共依赖、优柔寡断、被动攻击。挑战：真正伙伴需两个完整人非两半。

**East**: 天秤↔辛金阴柔/正官关系 (yin metal partnership)

#### Narrative Snippets

- `[ns_innersky_libra_001]` `[trigger: sign_libra]` `[factor_trigger: sign_libra AND element_air]` `[role: 主干]` The Scales. Libra has come to learn the art of partnership—not just romantic, but harmonious mutually beneficial relationships where both parties grow. → The Inner Sky Ch.4 #Libra
- `[ns_innersky_libra_002]` `[trigger: sign_libra AND astro_strength]` `[factor_trigger: astro_sign_libra]` `[role: 主干依赖]` The endpoint is creative collaboration: two autonomous individuals enhancing each other while remaining themselves. Mirroring, diplomacy, grace, fairness. → The Inner Sky Ch.4 #Libra
- `[ns_innersky_libra_003]` `[trigger: sign_libra AND astro_shadow]` `[factor_trigger: astro_sign_libra AND astro_state_dysfunction]` `[role: 条件分支]` Shadow: codependency (lose self in other), indecisiveness (paralyzed by options), passive aggression (smile while undermining). → The Inner Sky Ch.4 #Libra
- `[ns_innersky_libra_004]` `[trigger: sign_libra AND astro_challenge]` `[factor_trigger: astro_sign_libra]` `[role: 总结]` True partnership requires two whole people, not two halves. The challenge is to be fully oneself while being fully present with another. → The Inner Sky Ch.4 #Libra"""
    normalized_text_zh: str = """"""
    subject: str = "Libra - The Diplomat (Cardinal Air)"
    factor_refs: list = ['new_candidate', 'sign_libra', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="tis_v1.0.0_libra___the_diplomat__cardinal_001_L1",
    )
    version: str = "1.0.0"
