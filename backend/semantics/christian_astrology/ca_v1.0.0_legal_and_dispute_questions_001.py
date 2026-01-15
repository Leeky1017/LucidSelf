"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147454
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
    semantic_id="ca_v1.0.0_legal_and_dispute_questions_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class LegalAndDisputeQuestions(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 7th house | Domus VII | Open enemies, opponents | Adversary in lawsuit |
| 10th house | Domus X | Judge, authority | Ruling power |
| 4th house | Domus IV | End of matter | Final outcome |
| L1 vs L7 strength | Self vs Other | Relative dignity comparison | Determines victor |

**English Paraphrase (Primary Language)**:

**Legal/Dispute questions** (lawsuits, conflicts):

| House | Significator | Meaning |
|-------|--------------|---------|
| 1st | L1 | Querent (plaintiff or defendant) |
| 7th | L7 | Opponent/adversary |
| 10th | L10 | Judge/authority |
| 4th | L4 | Final outcome (end of matter) |

**Judgment patterns**:

| Configuration | Outcome |
|--------------|---------|
| L1 stronger and dignified | Querent wins |
| L7 stronger and dignified | Opponent wins |
| L10 applying to L1 | Judge favors querent |
| L10 applying to L7 | Judge favors opponent |
| L1 in 7th (enemy's house) | Querent at disadvantage |
| Moon transferring light L7→L1 | Settlement/compromise possible |

**Timing**: Degrees to perfection of L1-L10 aspect = time to judgment.

**Complete Chinese Interpretation (Secondary Language)**:

**法律/争端问题**（诉讼、冲突）：

| 宫位 | 象征星 | 含义 |
|------|--------|------|
| 第1宫 | L1 | 问卜者（原告或被告） |
| 第7宫 | L7 | 对手/敌人 |
| 第10宫 | L10 | 法官/权威 |
| 第4宫 | L4 | 最终结果（事情结局） |

**判断模式**：

| 配置 | 结果 |
|------|------|
| L1 更强且有尊贵 | 问卜者胜 |
| L7 更强且有尊贵 | 对手胜 |
| L10 趋近 L1 | 法官偏向问卜者 |
| L10 趋近 L7 | 法官偏向对手 |
| L1 在第7宫（敌人宫） | 问卜者处于劣势 |
| 月亮传光 L7→L1 | 可能和解/妥协 |

**时间**：L1-L10 相位成相度数 = 到判决的时间。

**Core Points**:
- 1st-7th axis for adversarial matters
- L10 (judge) inclination shows likely ruling
- 4th house = final outcome
- Relative strength determines victor

#### Narrative Snippets

- `[ns_lilly_036]` `[trigger: horary_legal]` `[factor_trigger: horary_7th_adversary AND astro_opponent]` `[role: 主干]` In lawsuits and disputes: 1st house = querent, 7th house = adversary/opponent. The 10th house lord represents the judge who decides between them. → Christian Astrology Legal
- `[ns_lilly_037]` `[trigger: legal_outcome]` `[factor_trigger: L10_inclination AND astro_judge_favor]` `[role: 主干依赖]` L10 applying to L1 = judge favors querent; L10 applying to L7 = judge favors opponent. 4th house shows the final outcome of the matter. → Christian Astrology Legal
- `[ns_lilly_038]` `[trigger: lawsuit_victor]` `[factor_trigger: L1_L7_strength AND astro_lawsuit_victor]` `[role: 总结]` Relative dignity and strength between L1 and L7 determines who prevails in the dispute. → Christian Astrology Legal

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Legal horary was in high demand in 17th-century England's litigious society. The 10th house (authority/judge) deciding between 1st and 7th is fundamental adversarial structure. Lilly successfully predicted outcomes of famous legal cases, building his reputation. The 4th house as "end of matter" is universal in horary.
- **中文**: 法律占星在17世纪英国好讼社会需求很高。第10宫（权威/法官）在第1宫和第7宫之间裁决是基本对抗结构。Lilly成功预测了著名法律案件的结果，建立了他的声誉。第4宫作为"事情结局"在占星中是普遍的。"""
    normalized_text_zh: str = """"""
    subject: str = "Legal and Dispute Questions"
    factor_refs: list = ['house_7_adversary', 'house_10_judge', 'house_4_outcome', 'new_candidate', 'judge_inclination']
    
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
        l1_anchor="ca_v1.0.0_legal_and_dispute_questions_001_L1",
    )
    version: str = "1.0.0"
