"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.156310
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
    semantic_id="ca_v1.0.0_mars_______the_lesser_malefic_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class MarsTheLesserMalefic(SemanticEntry):
    """
    #### Source Text
(Lilly Book I, pp. 65-68): "Mars finisheth his course in two years. He is hot, dry,...
    """
    
    original_text: str = """#### Source Text
(Lilly Book I, pp. 65-68): "Mars finisheth his course in two years. He is hot, dry, choleric, fiery, the lesser infortune. Mars signifies warriors, soldiers, surgeons, butchers, smiths."

#### English Paraphrase (Primary Language)

**Mars** = **action, conflict, courage, energy**. 2-year orbit. Nocturnal planet.

| Attribute | Value |
|-----------|-------|
| Temperature | Hot (activates, inflames) |
| Moisture | Dry (separates, cuts) |
| Temperament | Choleric |
| People | Warriors, surgeons, smiths, butchers |
| Body | Muscles, gallbladder, head |

#### Complete Chinese Interpretation (Secondary Language)

**火星** = **行动、冲突、勇气、能量**。2年轨道。夜间行星。热燥胆汁质。象征战士、外科医生、铁匠、屠夫。主肌肉、胆囊、头部。

**Narrative Snippets**:
- `[ns_lilly_mars_001]` `[trigger: mars_nature]` `[factor_trigger: astro_planet_mars AND astro_action_conflict]` `[role: 主干]` Mars is hot, dry, choleric—Lesser Malefic of action and conflict. → CA I #Mars"""
    normalized_text_zh: str = """"""
    subject: str = "Mars (♂) - The Lesser Malefic"
    factor_refs: list = ['mars_malefic', 'temperament_choleric']
    
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
        l1_anchor="ca_v1.0.0_mars_______the_lesser_malefic_001_L1",
    )
    version: str = "1.0.0"
