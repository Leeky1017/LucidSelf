"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147395
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
    semantic_id="ca_v1.0.0_5e__fifth_house_questions___ch_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class 5eFifthHouseQuestionsCh(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 5th House | Filii | House of children and pleasure | Fertility and creativity |
| Lord of 5th | Dominus 5 | Ruler of 5th house cusp | Children significator |
| Fertile signs | Signa fertilia | Cancer, Scorpio, Pisces (Water) | Pregnancy indicators |

**Source Text** (Synthesized from Lilly Book II, Ch. 5):
> If one shall have children: Consider the Lord of the 5th, the Lord of the 1st, and the Moon. If these be in Fruitful Signs (Cancer, Scorpio, Pisces) or aspecting planets in such signs, children are likely. If L5 and L1 be in Barren Signs (Gemini, Leo, Virgo) and the Moon likewise, children are denied. Whether she is with child: If the Moon be in aspect with L5, and both in Fruitful Signs, she is with child.

**English Paraphrase (Primary Language)**:

**Fifth House Questions** address children, pregnancy, pleasure, and creativity:

| Question Type | Judgment Method |
|---------------|-----------------|
| Will I have children? | L5/L1/Moon in fertile signs = yes; barren signs = no |
| Is she pregnant? | Moon aspecting L5, both in fertile signs = yes |
| Is child male or female? | Masculine signs/planets = male; feminine = female |
| When is birth? | Degrees between Moon and L5 = time to delivery |

**完整中文诠释**：第五宫问题涉及子女、怀孕、娱乐和创造力。会有孩子吗：L5/L1/月亮在多产星座=是；贫瘠星座=否。是否怀孕：月亮与L5成相，均在多产星座=是。男孩女孩：阳性星座/行星=男；阴性=女。何时生产：月亮与L5间度数=到分娩时间。

#### Core Points

- **Fertility questions**: L5/L1/Moon in fertile signs indicates children
- **Pregnancy**: Moon aspecting L5 in fertile signs confirms pregnancy
- **Gender**: Masculine vs feminine signs/planets indicates sex
- **Timing**: Degrees between significators = time to birth

**Narrative Snippets**:
- `[ns_lilly_5th_001]` `[trigger: fertility_judgment]` `[factor_trigger: L5_fertile_sign]` `[role: 主干]` L5, L1, and Moon in fruitful signs (Cancer, Scorpio, Pisces) = children likely. → Christian Astrology 5th House
- `[ns_lilly_5th_002]` `[trigger: pregnancy_confirmation]` `[factor_trigger: Moon_L5_aspect AND astro_pregnancy]` `[role: 主干依赖]` Moon aspecting L5, both in fertile signs = she is with child. → Christian Astrology 5th House"""
    normalized_text_zh: str = """"""
    subject: str = "5E. Fifth House Questions – Children, Pregnancy, Pleasure"
    factor_refs: list = ['fertile_signs', 'barren_signs', 'pregnancy_question']
    
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
        l1_anchor="ca_v1.0.0_5e__fifth_house_questions___ch_001_L1",
    )
    version: str = "1.0.0"
