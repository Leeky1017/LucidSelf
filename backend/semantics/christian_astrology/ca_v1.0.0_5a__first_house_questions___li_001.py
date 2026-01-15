"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147340
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
    semantic_id="ca_v1.0.0_5a__first_house_questions___li_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class 5aFirstHouseQuestionsLi(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| Ascendant | Horoscopus | Rising sign at question moment | Querent's primary significator |
| Lord of 1st | Dominus Ascendentis | Ruler of Ascendant sign | Querent's representative |
| Part of Fortune | Pars Fortunae | Arabian lot of Moon, Sun, ASC | General fortune indicator |
| Hyleg | Apheta | Life-giver | Longevity determination |

**Source Text** (Synthesized from Lilly Book II, Ch. 1):
> If the Querent is likely to live long yea or not: Consider the Lord of the Ascendant, whether he be in an Angle, especially in the 1st or 10th, and in Essential Dignity, free from Combustion and the malefic rays of Saturn or Mars; if so, the Native may live long. If the Lord of the Ascendant be Cadent, Peregrine, Combust, or afflicted by Malefics, life is short or health poor.

**English Paraphrase (Primary Language)**:

**First House Questions** address the querent's life, health, physical body, and general fortune:

| Question Type | Judgment Method |
|---------------|-----------------|
| Will I live long? | L1 dignified + angular = long life; L1 cadent + afflicted = short |
| What direction is best? | Strongest planet by dignity indicates beneficial direction |
| Which life period is best? | House where L1 falls = most favorable period |
| Am I in danger? | Malefics afflicting L1 or ASC = danger present |

**完整中文诠释**：第一宫问题涉及问卜者的生命、健康、身体和总体运势。判断寿命：L1有尊贵且在角宫=长寿；L1在果宫且受克=寿短或健康差。判断最佳方向：最强行星指示有利方向。判断最佳人生阶段：L1所在宫位=最有利时期。

#### Core Points

- **Life questions**: L1 dignity + house position determines longevity/health
- **Direction questions**: Strongest planet indicates beneficial direction  
- **Life period**: L1 house position shows favorable life stage
- **Danger assessment**: Malefics afflicting L1 show threats

**Narrative Snippets**:
- `[ns_lilly_1A_001]` `[trigger: longevity_judgment]` `[factor_trigger: L1_dignity AND astro_life_length]` `[role: 主干]` L1 dignified and angular = long life; L1 cadent and afflicted = short life or poor health. → Christian Astrology 1st House
- `[ns_lilly_1A_002]` `[trigger: best_direction]` `[factor_trigger: planet_strength AND astro_best_direction]` `[role: 主干依赖]` The strongest planet by dignity indicates the most beneficial direction for the querent's affairs. → Christian Astrology 1st House"""
    normalized_text_zh: str = """"""
    subject: str = "5A. First House Questions – Life, Health, and Direction"
    factor_refs: list = ['life_question', 'direction_question']
    
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
        l1_anchor="ca_v1.0.0_5a__first_house_questions___li_001_L1",
    )
    version: str = "1.0.0"
