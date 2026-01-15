"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.169546
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
    semantic_id="tb_v1.0.0_quality_of_employment__chapter_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class QualityOfEmploymentChapter(SemanticEntry):
    """
    **Source Text** (Lines 7201-7398):
> The dominion of the employment, or profession, is claimed in tw...
    """
    
    original_text: str = """**Source Text** (Lines 7201-7398):
> The dominion of the employment, or profession, is claimed in two quarters; viz. by the Sun, and by the sign on the mid-heaven. It is necessary to observe whether any planet may be making its oriental appearance nearest to the Sun, and whether any be posited in the mid-heaven; especially, when also receiving the application of the Moon. Mercury produces writers, accountants, teachers in the sciences, merchants and bankers, astrologers. Venus produces those engaged in perfumes, flowers, wines, colours, dyes. Mars produces soldiers, founders, carpenters, physicians, surgeons.

**English Paraphrase (Primary Language)**:
**Quality of employment** is determined by planets:
1. Making oriental appearance nearest to Sun
2. Posited in MC receiving Moon's application

**Planetary professions** (detailed):
- **Mercury**: Writers, accountants, teachers, merchants, astrologers, interpreters
  - +Saturn = dream interpreters, temple diviners
  - +Jupiter = orators, painters, lawyers
- **Venus**: Perfumers, florists, wine merchants, dyers, painters
  - +Saturn = entertainers, jugglers, sorcerers
  - +Jupiter = athletes, honorees through women
- **Mars**: Those working with fire—cooks, metalworkers
  - Separated from Sun = shipwrights, smiths, carpenters
  - +Saturn = miners, butchers, bath attendants
  - +Jupiter = soldiers, tax collectors

**Complete Chinese Interpretation (Secondary Language)**:
**职业质量**由行星决定：
1. 在太阳附近东方升起
2. 位于中天接收月亮的入相

**行星职业**（详细）：
- **水星**：作家、会计师、教师、商人、占星家、翻译
  - +土星 = 解梦者、神庙占卜师
  - +木星 = 演说家、画家、律师
- **金星**：香水商、花商、酒商、染工、画家
  - +土星 = 艺人、杂耍者、巫师
  - +木星 = 运动员、因女性而获荣誉者
- **火星**：使用火工作的人——厨师、金属工人
  - 与太阳分离 = 造船工、铁匠、木匠
  - +土星 = 矿工、屠夫、浴室服务员
  - +木星 = 士兵、税务员

**Core Points**:
- Employment determined by oriental planet or MC ruler
- Three key planets: Mercury, Venus, Mars
- Saturn/Jupiter modify the base profession
- No planet in position = occasional employment only

**Narrative Snippets**:
- `[ns_tetra_iv_010]` `[trigger: employment_quality]` `[factor_trigger: astro_planet_profession]` `[role: 主干]` Employment quality determined by oriental planet or MC ruler—Mercury for writing, Venus for arts, Mars for manual work. → Source Text IV.4
- `[ns_tetra_iv_eq]` `[trigger: employment_quality]` `[factor_trigger: employment_quality]` `[role: 效果]` Employment quality: the specific nature of profession determined by oriental planet or MC position—honorable if benefic, dishonorable if malefic. → Source Text IV.4"""
    normalized_text_zh: str = """"""
    subject: str = "Quality of Employment (Chapter IV)"
    factor_refs: list = ['engine_id', 'employment_quality', 'astrology_classical', 'source_ref', 'rel_iv_010', 'employment_quality', 'determining', 'evi_iv_010', 'employment_quality', 'rule_employment', 'concept_trade', 'employment_quality', 'vocational_aptitude']
    
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
        l1_anchor="tb_v1.0.0_quality_of_employment__chapter_001_L1",
    )
    version: str = "1.0.0"
