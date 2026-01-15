"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.113490
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
    semantic_id="tis_v1.0.0_aquarius___the_visionary__fixe_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class AquariusTheVisionaryFixe(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Fixed Air | Sustained th...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Fixed Air | Sustained thought | Element |
| Individuation | Fully oneself | Goal |
| Genius | Fresh thinking | Gift |
| Freedom | From tribal conditioning | Core drive |

**Source Text**: "The Water-Bearer (knowledge carrier). Aquarius has come to achieve freedom—psychological liberation from tribal conditioning, autonomy to be completely oneself. The endpoint is individuation: so fully oneself cannot be reduced to any category."

**English Paraphrase**: **Aquarius** = **Fixed Air** embodying **independence, innovation, and revolutionary truth**. Archetype: genius/exile defending individual truth against collective pressure.

**Core**: Resist conformity (question assumptions), genius (think freshly, see new patterns), rebellion (stand alone for truth), objectivity (see larger pattern), stubbornness (unshakable certainty), originality (create new paradigms). **Shadow**: Perverse eccentricity (artificial quirks), alienation (cold, unreachable), arrogance (contempt for "unenlightened"). **Challenge**: True freedom includes freedom to connect; warmth without losing independence.

**Chinese**: 水瓶座=固定风象体现独立、创新和革命真理。核心：抵抗从众、天才、反叛、客观、固执、原创。阴影：刻意怪癖、疏离、傲慢。挑战：真自由包含连接自由；不失独立的温暖。

**East**: 水瓶↔庚金阳刚/伤官革新 (yang metal innovation)

#### Narrative Snippets

- `[ns_innersky_aquarius_001]` `[trigger: sign_aquarius]` `[factor_trigger: sign_aquarius AND element_air]` `[role: 主干]` The Water-Bearer (knowledge carrier). Aquarius has come to achieve freedom—psychological liberation from tribal conditioning, autonomy to be completely oneself. → The Inner Sky Ch.4 #Aquarius
- `[ns_innersky_aquarius_002]` `[trigger: sign_aquarius AND astro_strength]` `[factor_trigger: astro_sign_aquarius]` `[role: 主干依赖]` The endpoint is individuation: so fully oneself cannot be reduced to any category. Genius, rebellion, objectivity, originality creating new paradigms. → The Inner Sky Ch.4 #Aquarius
- `[ns_innersky_aquarius_003]` `[trigger: sign_aquarius AND astro_shadow]` `[factor_trigger: astro_sign_aquarius AND astro_state_dysfunction]` `[role: 条件分支]` Shadow: perverse eccentricity (artificial quirks for quirks' sake), alienation (cold, unreachable), arrogance (contempt for "unenlightened" masses). → The Inner Sky Ch.4 #Aquarius
- `[ns_innersky_aquarius_004]` `[trigger: sign_aquarius AND astro_challenge]` `[factor_trigger: astro_sign_aquarius]` `[role: 总结]` True freedom includes freedom to connect; warmth without losing independence. The challenge is to be different while still belonging. → The Inner Sky Ch.4 #Aquarius"""
    normalized_text_zh: str = """"""
    subject: str = "Aquarius - The Visionary (Fixed Air)"
    factor_refs: list = ['sign_aquarius', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="tis_v1.0.0_aquarius___the_visionary__fixe_001_L1",
    )
    version: str = "1.0.0"
