"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147355
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
    semantic_id="ca_v1.0.0_5b__second_house_questions___w_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class 5bSecondHouseQuestionsW(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 2nd House | Substantia | House of moveable wealth | Financial questions |
| Lord of 2nd | Dominus 2 | Ruler of 2nd house cusp | Money significator |
| Part of Fortune | Pars Fortunae | General fortune lot | Wealth potential |

**Source Text** (Synthesized from Lilly Book II, Ch. 2):
> Whether the Querent shall be rich or not: If the Lord of the 2nd house be in the 2nd, or in the Ascendant, or in the 10th, well dignified, and in Aspect with the Lord of the Ascendant or Part of Fortune, the Querent may attain wealth. If L2 be in Cadent houses, Peregrine, or afflicted by Malefics, wealth is difficult to obtain.

**English Paraphrase (Primary Language)**:

**Second House Questions** address money, moveable possessions, and financial gain:

| Question Type | Judgment Method |
|---------------|-----------------|
| Will I be rich? | L2 dignified + angular/1st/10th = wealth; L2 cadent + afflicted = poverty |
| By what means? | Planet aspecting L2 or in 2nd indicates source |
| Will I recover debt? | L2 applying to L1 = recovery; separating = loss |
| Is money safe? | Malefics in 2nd or afflicting L2 = danger to wealth |

**完整中文诠释**：第二宫问题涉及金钱、动产和财务收益。判断富贵：L2有尊贵且在角宫/1宫/10宫=财富；L2在果宫且受克=贫困。判断来源：与L2成相或在2宫的行星指示来源。判断收债：L2趋近L1=收回；分离=损失。

#### Core Points

- **Wealth questions**: L2 dignity + position determines financial fortune
- **Means of wealth**: Aspecting planet or 2nd house planet shows source
- **Debt recovery**: L2-L1 application indicates recovery
- **Safety of wealth**: Malefics in/afflicting 2nd show threats

**Narrative Snippets**:
- `[ns_lilly_2nd_001]` `[trigger: wealth_judgment]` `[factor_trigger: L2_dignity]` `[role: 主干]` L2 dignified and in angular house or 1st/10th = querent will attain wealth. → Christian Astrology 2nd House
- `[ns_lilly_2nd_002]` `[trigger: wealth_source]` `[factor_trigger: planet_in_2nd AND astro_wealth_source]` `[role: 主干依赖]` Planet aspecting L2 or placed in 2nd house indicates the means by which wealth is obtained. → Christian Astrology 2nd House"""
    normalized_text_zh: str = """"""
    subject: str = "5B. Second House Questions – Wealth and Possessions"
    factor_refs: list = ['wealth_question', 'debt_recovery']
    
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
        l1_anchor="ca_v1.0.0_5b__second_house_questions___w_001_L1",
    )
    version: str = "1.0.0"
