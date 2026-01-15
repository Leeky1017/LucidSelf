"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.169612
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
    semantic_id="tb_v1.0.0_periodical_divisions_of_time___001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class PeriodicalDivisionsOfTime(SemanticEntry):
    """
    **Source Text** (Lines 8128-8280):
> Further attention is demanded with respect to the division of t...
    """
    
    original_text: str = """**Source Text** (Lines 8128-8280):
> Further attention is demanded with respect to the division of time. The mode of consideration applicable to human nature is universally one and the same; it is analogous to the arrangement of the seven planetary orbs. It commences with the first age of human life and the first sphere next above the earth, that of the Moon, and terminates with the final age of man and the last planetary sphere, that of Saturn.

**English Paraphrase (Primary Language)**:
**Periodical divisions of time** correlate life stages with planetary spheres:

| Planet | Age | Years | Characteristics |
|--------|-----|-------|-----------------|
| Moon | Infancy | 0-4 | Moist, rapid growth, variable |
| Mercury | Childhood | 4-14 | Learning, reason develops |
| Venus | Adolescence | 14-22 | Sexuality, passion |
| Sun | Adulthood | 22-41 | Authority, career, glory |
| Mars | Maturity | 41-56 | Austerity, vexation, care |
| Jupiter | Seniority | 56-68 | Gravity, prudence, honor |
| Saturn | Old age | 68+ | Coldness, mental slowness |

**Additional prorogations** for specific life domains:
- ASC prorogation = body and travel
- Part of Fortune = wealth
- Moon = mind and relationships
- Sun = dignities and glory
- MC = employment, friends, children

**Complete Chinese Interpretation (Secondary Language)**:
**时间的周期划分**将人生阶段与行星天体对应：

| 行星 | 年龄段 | 年份 | 特征 |
|-----|------|-----|-----|
| 月亮 | 婴儿期 | 0-4 | 潮湿、快速生长、多变 |
| 水星 | 童年期 | 4-14 | 学习、理性发展 |
| 金星 | 青春期 | 14-22 | 性欲、激情 |
| 太阳 | 成年期 | 22-41 | 权威、事业、荣耀 |
| 火星 | 壮年期 | 41-56 | 严肃、烦恼、忧虑 |
| 木星 | 老年前期 | 56-68 | 庄重、审慎、荣誉 |
| 土星 | 老年期 | 68+ | 寒冷、精神迟缓 |

**特定生活领域的附加推运**：
- 上升推运 = 身体和旅行
- 福点 = 财富
- 月亮 = 心智和关系
- 太阳 = 尊严和荣耀
- 中天 = 职业、朋友、子女

**Core Points**:
- Seven ages of man correspond to seven planets
- Each planet governs its appropriate life stage
- Multiple prorogations for different life areas
- Events may be mixed (good and bad simultaneously)

**Narrative Snippets**:
- `[ns_tetra_iv_020]` `[trigger: time_division]` `[factor_trigger: astro_planet_age]` `[role: 主干]` Seven ages of life correspond to seven planets—Moon for infancy, Mercury for childhood, through Saturn for old age. → Source Text IV.10
- `[ns_tetra_iv_ls]` `[trigger: life_stage]` `[factor_trigger: life_stage]` `[role: 效果]` Life stage governed by planetary period: Moon=0-4, Mercury=4-14, Venus=14-22, Sun=22-41, Mars=41-56, Jupiter=56-68, Saturn=68+. → Source Text IV.10"""
    normalized_text_zh: str = """"""
    subject: str = "Periodical Divisions of Time (Chapter X)"
    factor_refs: list = ['engine_id', 'planet_age', 'astrology_classical', 'prorogation_multiple', 'astrology_classical', 'source_ref', 'rel_iv_020', 'astro_planet_age', 'governing', 'evi_iv_020', 'planet_age', 'rule_planet_age', 'concept_life_stage', 'planet_age', 'developmental_stages']
    
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
        l1_anchor="tb_v1.0.0_periodical_divisions_of_time___001_L1",
    )
    version: str = "1.0.0"
