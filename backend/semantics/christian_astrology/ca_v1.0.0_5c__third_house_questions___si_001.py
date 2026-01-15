"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147369
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
    semantic_id="ca_v1.0.0_5c__third_house_questions___si_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class 5cThirdHouseQuestionsSi(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 3rd House | Fratres | House of siblings and short journeys | Communication and travel |
| Lord of 3rd | Dominus 3 | Ruler of 3rd house cusp | Sibling/journey significator |
| Short journey | Iter breve | Travel not crossing water | Local travel |

**Source Text** (Synthesized from Lilly Book II, Ch. 3):
> Of Brethren, Sisters, Kindred, Neighbours: If L3 be in good aspect with L1, and both well dignified, the querent and brethren shall agree well. If L3 be in the 3rd, strong, and in good aspect with L1, brethren prosper. Of Short Journeys: If the Moon and L3 be free from affliction and in good aspect, the journey shall be safe and successful.

**English Paraphrase (Primary Language)**:

**Third House Questions** address siblings, neighbors, short journeys, and communications:

| Question Type | Judgment Method |
|---------------|-----------------|
| Will siblings agree? | L3-L1 good aspect + dignity = harmony; affliction = discord |
| Is brother absent safe? | L3 dignified + free from malefics = safe |
| Will short journey succeed? | L3 + Moon unafflicted = safe journey |
| Are rumors true? | Mercury/Moon condition shows truth or falsity |

**完整中文诠释**：第三宫问题涉及兄弟姐妹、邻居、短途旅行和通讯。兄弟和睦：L3与L1成好相位且有尊贵=和谐；受克=不和。在外兄弟安全：L3有尊贵且无凶星=安全。短途旅行成功：L3+月亮无受克=旅程安全。

#### Core Points

- **Sibling questions**: L3-L1 relationship shows family harmony
- **Absent person**: L3 dignity indicates safety
- **Short journeys**: L3 + Moon condition determines success
- **Communications**: Mercury/Moon shows message reliability

**Narrative Snippets**:
- `[ns_lilly_3rd_001]` `[trigger: sibling_harmony]` `[factor_trigger: L3_L1_aspect AND astro_sibling_harmony]` `[role: 主干]` L3 in good aspect with L1, both well dignified = querent and siblings agree well. → Christian Astrology 3rd House
- `[ns_lilly_3rd_002]` `[trigger: short_journey]` `[factor_trigger: L3_Moon AND astro_journey_safety]` `[role: 主干依赖]` Moon and L3 free from affliction = journey safe and successful. → Christian Astrology 3rd House"""
    normalized_text_zh: str = """"""
    subject: str = "5C. Third House Questions – Siblings, Short Journeys, Communications"
    factor_refs: list = ['sibling_question', 'short_journey']
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_5c__third_house_questions___si_001_L1",
    )
    version: str = "1.0.0"
