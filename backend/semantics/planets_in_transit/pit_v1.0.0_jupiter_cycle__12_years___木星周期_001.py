"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.251593
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
    semantic_id="pit_v1.0.0_jupiter_cycle__12_years___木星周期_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class JupiterCycle12Years木星周期(SemanticEntry):
    """
    **Source Text** (Paraphrased from Hand):
> "Jupiter's 12-year orbital period creates the expansion a...
    """
    
    original_text: str = """**Source Text** (Paraphrased from Hand):
> "Jupiter's 12-year orbital period creates the expansion and growth cycle. Jupiter rules opportunity, abundance, optimism, exploration, and philosophical expansion. The 12-year cycle divides into phases of expansion and consolidation, marking natural opportunity windows for growth and new ventures."

**English Paraphrase (Primary Language)**:
The **Jupiter cycle** (12 years) is astrology's primary **growth and expansion cycle**, governing opportunities, abundance, and philosophical development. Jupiter symbolizes **expansion principle**: opportunity, luck, abundance, optimism, exploration, wisdom, faith. Unlike Saturn's restrictive maturation, Jupiter opens doors and invites expansion. The 12-year cycle creates **natural opportunity windows**—periods when growth is favored and new ventures have better chances of success. Hand emphasizes that Jupiter transits are **fortune windows**: times when the universe seems to cooperate with your efforts. A Jupiter transit to your Sun or Ascendant often coincides with career advancement, relationship expansion, or spiritual growth. The cycle divides into phases: expansion (growth, new ventures, exploration) and consolidation (integrating gains, stabilizing). Understanding Jupiter's 12-year rhythm helps explain why certain ages (12, 24, 36, 48, 60, 72) feel like natural opportunity points—Jupiter is returning to key natal positions.

**Complete Chinese Interpretation (Secondary Language)**:
**木星周期**（12 年）是占星学的主要**成长和扩展周期**，管理机遇、丰盛和哲学发展。木星象征**扩展原则**：机遇、幸运、丰盛、乐观、探索、智慧、信仰。与土星的限制成熟不同，木星打开门并邀请扩展。12 年周期创造**自然机遇窗**——成长受欢迎且新企业有更好成功机会的时期。汉德强调木星行运是**幸运窗**：宇宙似乎与你的努力合作的时期。木星行运到你的太阳或上升点常常与职业晋升、关系扩展或精神成长相吻合。周期分为阶段：扩展（成长、新企业、探索）和巩固（整合收益、稳定）。理解木星的 12 年节奏有助于解释为什么某些年龄（12、24、36、48、60、72）感觉像自然机遇点——木星正在回到关键本命位置。

**Key Term Analysis**:
- **Jupiter Cycle**: `12-year orbit` / `expansion principle` / `opportunity windows`
- **Expansion Phase**: `growth` / `new ventures` / `exploration`
- **Consolidation Phase**: `integrating gains` / `stabilizing` / `wisdom`
- **Fortune Windows**: `natural opportunity times` / `universe cooperation` / `luck`

**Core Points** (decomposed, no upper limit):
- Jupiter cycle = 12-year orbital period
- Expansion and growth cycle
- Opportunity, abundance, optimism, exploration themes
- Natural opportunity windows for growth
- Expansion phase: growth, new ventures, exploration
- Consolidation phase: integrating gains, stabilizing
- Ages 12, 24, 36, 48, 60, 72 = natural opportunity points
- Jupiter transits often coincide with advancement and expansion
- Fortune windows: times when universe cooperates
- Contrasts with Saturn's restrictive maturation

**Detailed Explanation**:
Jupiter is the "yes" to Saturn's "no." While Saturn teaches through limitation, Jupiter teaches through expansion. A Jupiter transit is an invitation to grow, explore, and expand your horizons. The 12-year cycle means you get regular opportunity windows—roughly every 12 years, Jupiter returns to key natal positions, creating natural times for new ventures and growth.

**Narrative Snippets** (English only, decomposed):
- `[ns_hand_pit_045]` `[trigger: jupiter_cycle]` `[factor_trigger: astro_jupiter_cycle]` `[role: 主干]` Jupiter's 12-year cycle is the expansion and growth cycle. → Source Text
- `[ns_hand_pit_046]` `[trigger: expansion_phase]` `[factor_trigger: astro_expansion_phase]` `[role: 主干依赖]` Expansion phase: growth, new ventures, exploration. → Source Text
- `[ns_hand_pit_047]` `[trigger: opportunity_windows]` `[factor_trigger: astro_opportunity_windows]` `[role: 主干依赖]` Natural opportunity windows at ages 12, 24, 36, 48, 60, 72. → Source Text
- `[ns_hand_pit_048]` `[trigger: fortune_windows]` `[factor_trigger: astro_fortune_windows]` `[role: 总结]` Jupiter transits are fortune windows when universe cooperates with efforts. → English Paraphrase

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A: Single authoritative source (Hand's "Planets in Transit" 1976). The Jupiter cycle is standard in modern predictive astrology.
- **中文**: 无版本差异：单一权威来源（Hand《行运中的行星》1976）。木星周期在现代预测占星中是标准的。"""
    normalized_text_zh: str = """"""
    subject: str = "Jupiter Cycle (12 Years) (木星周期)"
    factor_refs: list = ['astro_jupiter_cycle', 'astro_expansion_phase', 'astro_consolidation_phase', 'astro_opportunity_windows', 'astro_fortune_windows']
    
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
        l1_anchor="pit_v1.0.0_jupiter_cycle__12_years___木星周期_001_L1",
    )
    version: str = "1.0.0"
