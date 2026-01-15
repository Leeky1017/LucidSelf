"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251607
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
    semantic_id="pit_v1.0.0_jupiter_return__every_12_years_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterReturnEvery12Years(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "Jupiter return occurs when transiting Jupiter returns to...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "Jupiter return occurs when transiting Jupiter returns to its natal position, completing a 12-year cycle. This marks the beginning of a new growth phase: fresh opportunities, philosophical renewal, and expansion into new areas. Jupiter returns occur at predictable ages: 12, 24, 36, 48, 60, 72."

**English Paraphrase (Primary Language)**:
**Jupiter return** is the moment when transiting Jupiter returns to its exact natal position, completing one 12-year cycle and initiating a new one. Unlike Saturn returns which are reality testing points, Jupiter returns are **opportunity initiations**—moments when new growth cycles naturally begin. Hand emphasizes that Jupiter returns are **fortune windows**: times when the universe seems to open doors and create opportunities. The **first Jupiter return** (age 12) marks transition from childhood to adolescence—new learning opportunities, social expansion. The **second return** (age 24) marks transition to adulthood—career opportunities, relationship expansion. The **third return** (age 36) marks mature adulthood—wisdom and philosophical expansion. Each return brings **fresh opportunities** and invites **expansion into new areas**. Unlike Saturn's restrictive testing, Jupiter's returns are invitations to grow, explore, and expand horizons. The predictable timing (12, 24, 36, 48, 60, 72) means you can anticipate opportunity windows and prepare to seize them.

**Complete Chinese Interpretation (Secondary Language)**:
**木星回归**是行运木星回到其精确本命位置的时刻，完成一个 12 年周期并启动新周期。与土星回归是现实考验点不同，木星回归是**机遇启动**——新成长周期自然开始的时刻。汉德强调木星回归是**幸运窗**：宇宙似乎打开门并创造机遇的时刻。**第一次木星回归**（12 岁）标记从童年到青少年的过渡——新学习机遇、社交扩展。**第二次回归**（24 岁）标记向成年过渡——职业机遇、关系扩展。**第三次回归**（36 岁）标记成熟成年——智慧和哲学扩展。每次回归都带来**新鲜机遇**并邀请**向新领域扩张**。与土星的限制性测试不同，木星的回归是邀请成长、探索和扩展视野。可预测的时机（12、24、36、48、60、72）意味着你可以预期机遇窗并准备抓住它们。

**Key Term Analysis**:
- **Jupiter Return**: `12-year cycle completion` / `opportunity initiation` / `growth phase beginning`
- **Fortune Windows**: `natural opportunity times` / `universe cooperation` / `expansion invitations`
- **Predictable Ages**: `12, 24, 36, 48, 60, 72` / `life transition points` / `opportunity markers`

**Core Points** (decomposed, no upper limit):
- Jupiter return = transiting Jupiter returns to natal position
- Occurs every 12 years at predictable ages
- Ages 12, 24, 36, 48, 60, 72 = opportunity windows
- Marks beginning of new growth cycle
- Fresh opportunities and expansion invitations
- Philosophical renewal and wisdom expansion
- Contrasts with Saturn's reality testing
- Fortune windows: times when universe opens doors
- Can anticipate and prepare for opportunities
- Each return brings new growth phase

**Detailed Explanation**:
Jupiter returns are nature's invitations to expand. While Saturn returns test what you've built, Jupiter returns invite you to build something new. The 12-year rhythm means you get regular opportunity windows—roughly every 12 years, Jupiter returns to key natal positions, creating natural times for new ventures, learning, and expansion.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_049]` `[trigger: jupiter_return]` `[factor_trigger: astro_jupiter_return]` `[role: 主干]` Jupiter return occurs when transiting Jupiter returns to natal position, completing 12-year cycle. → Source Text
- `[ns_hand_pit_050]` `[trigger: opportunity_initiation]` `[factor_trigger: astro_opportunity_initiation]` `[role: 主干依赖]` Jupiter returns mark beginning of new growth phase with fresh opportunities. → Source Text
- `[ns_hand_pit_051]` `[trigger: predictable_ages]` `[factor_trigger: astro_predictable_ages]` `[role: 主干依赖]` Jupiter returns occur at predictable ages: 12, 24, 36, 48, 60, 72. → Source Text
- `[ns_hand_pit_052]` `[trigger: fortune_windows]` `[factor_trigger: astro_fortune_windows]` `[role: 总结]` Jupiter returns are fortune windows when universe opens doors and creates opportunities. → English Paraphrase

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A: Single authoritative source (Hand's "Planets in Transit" 1976). Jupiter returns are standard in modern predictive astrology.
- **中文**: 无版本差异：单一权威来源（Hand《行运中的行星》1976）。木星回归在现代预测占星中是标准的。"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Return (Every 12 Years) (木星回归)"
    factor_refs: list = ['astro_jupiter_return', 'astro_opportunity_initiation', 'astro_predictable_ages', 'astro_growth_phase']
    
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
        book_id="planets_in_transit",
        chapter="",
        l1_anchor="pit_v1.0.0_jupiter_return__every_12_years_001_L1",
    )
    version: str = "1.0.0"
