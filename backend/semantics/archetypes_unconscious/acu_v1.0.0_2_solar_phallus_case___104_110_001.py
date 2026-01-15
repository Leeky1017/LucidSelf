"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.515617
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
    semantic_id="acu_v1.0.0_2_solar_phallus_case___104_110_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 2SolarPhallusCase104110(SemanticEntry):
    """
    **Source Text** (¶104-110, Lines 1747-1830):

> [105] 1906: Paranoid patient at window said: "Surely...
    """
    
    original_text: str = """**Source Text** (¶104-110, Lines 1747-1830):

> [105] 1906: Paranoid patient at window said: "Surely you see the sun's penis—when I move my head, it moves too, and that is where the wind comes from."
>
> [106] 1910: Mithraic liturgy (Dieterich): "the so-called tube, the origin of the ministering wind...hanging down from the disc of the sun."
>
> [109] Patient could not have known a Greek papyrus published four years later. Never travelled. No such picture in Zurich.
>
> [110] This case shows my method—not proof, but demonstration of procedure.

**English Paraphrase**:
- **Patient's vision (1906)**: Sun's penis = wind origin
- **Mithraic parallel (1910)**: Tube from sun = ministering wind
- **No possible knowledge**: Papyrus published 4 years after vision
- **Purpose**: Method demonstration, not final proof

**中文释义**：
- **患者幻象（1906）**：太阳阳具 = 风的起源
- **密特拉平行（1910）**：太阳之管 = 服务之风
- **不可能的知识**：纸莎草在幻象4年后出版
- **目的**：方法示范，非最终证明

**Narrative Snippets**:
- `[ns_cw9i_066]` `[trigger: solar_phallus]` `[factor_trigger: jung_vision AND jung_archetype]` `[role: 主干]` Patient: "Surely you see the sun's penis—that is where the wind comes from." → ¶105
- `[ns_cw9i_067]` `[trigger: mithraic_parallel]` `[factor_trigger: jung_myth AND jung_archetype]` `[role: 主干依赖]` Mithraic liturgy: "the tube, origin of ministering wind, hanging from the sun." → ¶106"""
    normalized_text_zh: str = """"""
    subject: str = "2 Solar Phallus Case (¶104-110)"
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
        l1_anchor="acu_v1.0.0_2_solar_phallus_case___104_110_001_L1",
    )
    version: str = "1.0.0"
