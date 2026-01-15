"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147507
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
    semantic_id="ca_v1.0.0_war_and_battle_outcomes_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class WarAndBattleOutcomes(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 1st House | Querent/Our side | Our army or party | Our forces |
| 7th House | Enemy/Adversary | Opposing army | Enemy forces |
| 10th House | Victory/King | Authority and outcome | Who prevails |
| Part of Fortune | General fortune | Success indicator | Overall outcome |

**Source Text** (Synthesized from Lilly Book II, pp. 361-401):
> Of Battle, War, or other contentions: The Ascendant signifies the Querent or the Party we favour; the 7th house the Enemy. Consider which Lord is stronger in Essential and Accidental dignity—that party shall overcome. If Lord of 1st be stronger, we prevail; if Lord of 7th be stronger, the Enemy wins. The Moon translating light between them may show treaty or intermediary.

**English Paraphrase (Primary Language)**:

**War/Battle Questions** use adversarial house structure:

| Element | Significator |
|---------|--------------|
| Our side | 1st house + L1 |
| Enemy | 7th house + L7 |
| Victory | 10th house, Part of Fortune |
| Commanders | L10 (our), L4 (enemy's 10th) |

**Victory Determination**:
- L1 > L7 in dignity = our side wins
- L7 > L1 in dignity = enemy wins
- Moon translating light = treaty possible
- Mars strong = decisive battle; Saturn = prolonged siege

**完整中文诠释**：战争/战斗问题使用对抗宫位结构。我方=第1宫+L1；敌方=第7宫+L7；胜利=第10宫+福点；指挥官=L10（我方），L4（敌方的第10）。胜利判断：L1尊贵>L7=我方胜；L7>L1=敌方胜；月亮传光=可能和谈；火星强=决战；土星=持久围攻。

#### Core Points

- **Adversarial structure**: 1st vs 7th determines victor
- **Dignity comparison**: Stronger significator wins
- **Commanders**: L10 for our side, L4 for enemy's commander
- **Moon mediation**: Translation of light = negotiation

**Narrative Snippets**:
- `[ns_lilly_war_001]` `[trigger: war_structure]` `[factor_trigger: L1_L7_comparison AND astro_war_parties]` `[role: 主干]` 1st house = our party; 7th = enemy. Whichever Lord is stronger in dignity, that party shall overcome. → Christian Astrology War
- `[ns_lilly_war_002]` `[trigger: victory_determination]` `[factor_trigger: dignity_comparison AND astro_victory_determination]` `[role: 主干依赖]` If L1 stronger, we prevail; if L7 stronger, enemy wins. Mars strong = decisive battle. → Christian Astrology War
- `[ns_lilly_war_003]` `[trigger: treaty_possibility]` `[factor_trigger: Moon_translating AND astro_treaty_possibility]` `[role: 条件分支]` Moon translating light between L1 and L7 may show treaty or intermediary bringing peace. → Christian Astrology War

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Lilly famously predicted outcomes of English Civil War battles. His Reading siege prediction (1643) brought him fame. War horary uses same principles as lawsuit (7th house opposition) but with military terminology.
- **中文**: Lilly著名地预测了英国内战战役结果。他的雷丁围城预测（1643年）使他成名。战争卜卦使用与诉讼相同原则（第7宫对抗），但用军事术语。"""
    normalized_text_zh: str = """"""
    subject: str = "War and Battle Outcomes"
    factor_refs: list = ['war_structure', 'victory_determination', 'treaty_indicator']
    
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
        l1_anchor="ca_v1.0.0_war_and_battle_outcomes_001_L1",
    )
    version: str = "1.0.0"
