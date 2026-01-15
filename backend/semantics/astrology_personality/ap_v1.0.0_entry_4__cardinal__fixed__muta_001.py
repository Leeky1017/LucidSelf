"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238149
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
    semantic_id="ap_v1.0.0_entry_4__cardinal__fixed__muta_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry4CardinalFixedMuta(SemanticEntry):
    """
    **Source Text** (Lines 8440-8491):
> Form differentiation: Energy operates on a polar rhythm of acti...
    """
    
    original_text: str = """**Source Text** (Lines 8440-8491):
> Form differentiation: Energy operates on a polar rhythm of action and reaction... the principle of "energy-differentiation" is similar to that of "substance-differentiation"...
>
> Three operations always: generation, concentration and distribution... Zodiacal signs of generation of power are called: Cardinal signs. Zodiacal signs of concentration of power are called: Fixed signs. Zodiacal signs of distribution of power are called: Mutable signs.
>
> Spirit—or Life—generates. Soul concentrates. Mind distributes. Personality manifests.

**Key Term Analysis**:
- **Cardinal signs**: `generation of power` / `spirit` / `beginnings`
- **Fixed signs**: `concentration of power` / `soul` / `mid-points`
- **Mutable signs**: `distribution of power` / `mind` / `transitions`
- **Four Avataric Gates**: `Taurus 15°, Leo 15°, Scorpio 15°, Aquarius 15°` / `maximum energy release`

**English Paraphrase (Primary Language)**:
Three-fold classification based on power operation:
- **Cardinal**: generation of power (spirit)
- **Fixed**: concentration of power (soul)
- **Mutable**: distribution of power (mind)

"Spirit—or Life—generates. Soul concentrates. Mind distributes. Personality manifests."

The Fixed signs' 15th degrees (Taurus, Leo, Scorpio, Aquarius) = Four Avataric Gates = maximum energy release points.

**Complete Chinese Interpretation (Secondary Language)**:
基于能量运作的三重分类：
- **本位**：能量生成（精神）
- **固定**：能量集中（灵魂）
- **变动**：能量分布（心智）

"精神——或生命——生成。灵魂集中。心智分布。人格显现。"

固定星座的第15度（金牛、狮子、天蝎、水瓶）= 四个阿凡达之门 = 最大能量释放点。

**Narrative Snippets**:
- `[ns_aop_171]` `[trigger: cardinal_fixed_mutable]` `[factor_trigger: astro_sign_modalities AND astro_avataric AND astro_modalities]` `[role: 主干]` Cardinal (generate) / Fixed (concentrate) / Mutable (distribute) = Spirit/Soul/Mind. → L8477-8491
- `[ns_aop_172]` `[trigger: avataric_gates]` `[factor_trigger: astro_four_gates]` `[role: 总结]` Four Avataric Gates at 15° Fixed signs: maximum energy release points. → L8408-8418"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 4: Cardinal, Fixed, Mutable Classification"
    factor_refs: list = ['modality_cardinal', 'modality_fixed', 'modality_mutable', 'avataric_gates']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_4__cardinal__fixed__muta_001_L1",
    )
    version: str = "1.0.0"
