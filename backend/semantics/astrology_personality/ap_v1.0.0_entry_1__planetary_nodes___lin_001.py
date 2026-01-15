"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238219
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
    semantic_id="ap_v1.0.0_entry_1__planetary_nodes___lin_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry1PlanetaryNodesLin(SemanticEntry):
    """
    **Source Text** (Lines 9877-9967):
> Planetary Nodes: The nodes of a planet are two opposite points ...
    """
    
    original_text: str = """**Source Text** (Lines 9877-9967):
> Planetary Nodes: The nodes of a planet are two opposite points where the plane of the orbit of the planet intersects the ecliptic...
>
> The North Node is the positive pole of integration; the South Node the negative pole where disintegration of some sort takes place. The former is a point of ingestion and assimilation; the latter, a point of release and evacuation...
>
> If, therefore, we refer again to the present position of Uranus' nodes... its North Node, being in the fourteenth degree of Gemini, signifies that positive regeneration comes to mankind at present by the use of the concrete intellect.

**Key Term Analysis**:
- **Planetary nodes**: `orbit plane intersects ecliptic` / `orbital relationship to Earth`
- **North Node**: `positive integration` / `ingestion, assimilation` / `future direction`
- **South Node**: `negative/disintegration` / `release, evacuation` / `past heritage`
- **Uranus nodes example**: `Gemini 13.40 (N)` / `Sagittarius 13.40 (S)` / `regeneration through intellect`

**English Paraphrase (Primary Language)**:
Planetary nodes = points where planet's orbital plane intersects ecliptic, showing the planet's activity in Earth's developmental scheme.

**North Node**: positive pole of integration, point of ingestion and assimilation.
**South Node**: negative pole (disintegration), point of release and evacuation.

Example: Uranus' North Node in Gemini 13.40 = "positive regeneration through concrete intellect"; South Node in Sagittarius = "line of least resistance" through religious idealism.

**Complete Chinese Interpretation (Secondary Language)**:
行星交点 = 行星轨道平面与黄道交叉的点，显示行星活动在地球发展方案中的位置。

**北交点**：整合的正极，摄入和同化的点。
**南交点**：负极（分解），释放和排出的点。

例：天王星北交点在双子座13.40 = "通过具体智力的积极再生"；南交点在射手座 = 通过宗教理想主义的"最小阻力路线"。

**Narrative Snippets**:
- `[ns_aop_187]` `[trigger: planetary_nodes]` `[factor_trigger: astro_nodes_planetary AND astro_planetary_nodes]` `[role: 主干]` Planetary nodes: orbit-ecliptic intersection; North = integration, South = disintegration. → L9879-9947
- `[ns_aop_188]` `[trigger: uranus_nodes]` `[factor_trigger: astro_uranus_nodal AND astro_planetary_nodes]` `[role: 主干依赖]` Uranus nodes: N in Gemini (intellect regeneration), S in Sagittarius (religious escape). → L9949-9980"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 1: Planetary Nodes - Line of Integration"
    factor_refs: list = ['nodes_planetary', 'node_north', 'node_south']
    
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
        l1_anchor="ap_v1.0.0_entry_1__planetary_nodes___lin_001_L1",
    )
    version: str = "1.0.0"
