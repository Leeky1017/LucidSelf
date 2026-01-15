"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182733
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
    semantic_id="tb_v1.0.0_faces__chariots__and_planetary_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class FacesChariotsAndPlanetary(SemanticEntry):
    """
    **Source Text** (Lines 2848-2879):
> Each is said to be in its proper face, when the aspect it holds...
    """
    
    original_text: str = """**Source Text** (Lines 2848-2879):
> Each is said to be in its proper face, when the aspect it holds to the Sun, or Moon, is similar to that which its own house bears to their houses... Each planet is also said to be in its proper chariot, or throne, or otherwise triumphantly situated, when it holds familiarity with the place which it actually occupies by two, or more, of the prescribed modes of connection... Each planet is said to rejoice when any connection subsists between itself and other stars of the same condition... when a planet occupies a place adverse and dissimilar in condition to itself, much of its influence is dissipated and lost.

**English Paraphrase (Primary Language)**:
Ptolemy describes additional planetary dignities:

**Face (πρόσωπον)**: A planet is "in its face" when its aspect to the Sun/Moon mirrors the aspect of its house to the luminaries' houses. E.g., Venus rules the sextile houses from the luminaries, so Venus is "in face" when sextile the Sun (occidental) or Moon (oriental).

**Chariot/Throne (ἅρμα)**: A planet is "in its chariot" when it holds multiple dignities simultaneously in its current sign (e.g., domicile + triplicity, or exaltation + terms). This greatly strengthens its influence.

**Joy**: A planet "rejoices" when configured with planets of similar nature, even at distance.

**Detriment**: A planet in a sign adverse to its nature loses influence through "admixture" of contrary temperament.

**Complete Chinese Interpretation (Secondary Language)**:
托勒密描述了额外的行星尊贵：

**面（πρόσωπον）**：当行星与太阳/月亮的相位反映其宫位与发光体宫位的相位时，该行星处于"面"中。例如，金星主宰与发光体六分相的宫位，因此金星与太阳六分（西方）或月亮六分（东方）时处于"面"中。

**车架/宝座（ἅρμα）**：当行星在其当前星座同时拥有多重尊贵（如庙旺+三分性，或擢升+界）时，处于"车架"中。这极大增强其影响力。

**喜乐**：当行星与性质相似的行星配置时，即使距离远也"喜乐"。

**损害**：行星在与其性质相反的星座中通过相反气质的"混合"失去影响力。

**Core Points**:
- Face: Aspect to luminaries mirrors house-luminary aspect
- Chariot/Throne: Multiple dignities in same sign = great strength
- Joy: Configuration with similar-natured planets
- Detriment: Contrary sign dissipates influence
- Cumulative dignities strengthen; contrary placements weaken

**Narrative Snippets**:
- `[ns_tetra_i058]` `[trigger: planetary_face]` `[factor_trigger: astro_planet_dignity_face AND planet_dignity_face]` `[role: 条件分支]` A planet is in its face when its aspect to the luminaries mirrors its houses' aspect to their houses. → Source Text I.26
- `[ns_tetra_i059]` `[trigger: chariot_throne]` `[factor_trigger: astro_planet_dignity_multiple]` `[role: 主干]` A planet in its chariot holds two or more dignities simultaneously, greatly augmenting its influence. → Source Text I.26

**Textual Criticism**: N/A: Standard dignity terminology."""
    normalized_text_zh: str = """"""
    subject: str = "Faces, Chariots, and Planetary Conditions (Chapter XXVI)"
    factor_refs: list = ['engine_id', 'planet_dignity_face', 'astrology_classical', 'planet_dignity_multiple', 'astrology_classical', 'source_ref', 'rel_i_023', 'planet_dignity_multiple', 'amplifying', 'evi_i_019', 'planet_dignity_multiple', 'rule_chariot', 'concept_cumulative_dignity', 'planet_dignity_multiple', 'self_mastery']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_faces__chariots__and_planetary_001_L1",
    )
    version: str = "1.0.0"
