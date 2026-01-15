"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192563
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
    semantic_id="tb_v1.0.0_conception_and_birth__chapter__001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ConceptionAndBirthChapter(SemanticEntry):
    """
    **Source Text** (Lines 4685-4776):
> The actual moment, in which human generation commences, is, in ...
    """
    
    original_text: str = """**Source Text** (Lines 4685-4776):
> The actual moment, in which human generation commences, is, in fact, by nature, the moment of the conception itself; but, in efficacy with regard to subsequent events, it is the parturition or birth. In every case where the actual time of conception may be ascertained, it is useful to remark the effective influence of the configuration of the stars as it existed at that time. For the seed will, at the very first, receive its due quality, as then dispensed by the Ambient. But, if the time of conception cannot be precisely made out, that of the birth must be received as the original date of generation; for it is virtually the most important.

**English Paraphrase (Primary Language)**:
Ptolemy distinguishes between **conception** and **birth** as two starting points for natal astrology:

1. **Conception**: The true natural beginning—the seed receives its initial quality from the Ambient at conception
2. **Birth**: The practical beginning—when conception time is unknown, birth serves as the effective origin

**Key insight**: The birth chart is not inferior to conception chart because:
- Nature times birth to correspond with conception positions
- Birth adds qualities (senses, movement) not present in the womb
- Both moments are cosmically connected through sympathetic correspondence

**Complete Chinese Interpretation (Secondary Language)**:
托勒密区分了**受孕**和**出生**作为本命占星学的两个起点：

1. **受孕**：真正的自然开始——种子在受孕时从环境接收其初始品质
2. **出生**：实际的开始——当受孕时间未知时，出生作为有效起点

**关键洞见**：出生图并不逊于受孕图，因为：
- 自然使出生时间与受孕位置相对应
- 出生增加了子宫内不存在的品质（感官、运动）
- 两个时刻通过交感对应在宇宙上相连

**Core Points**:
- Conception = natural beginning; Birth = practical beginning
- Both charts valid and cosmically connected
- Seed receives quality at conception
- Birth adds human-specific qualities

**Narrative Snippets**:
- `[ns_tetra_iii_010]` `[trigger: conception_birth]` `[factor_trigger: astro_chart_origin]` `[role: 主干]` Conception is the natural origin, birth is the practical origin—both are cosmically valid. → Source Text III.2
- `[ns_ptolemy_iii_028]` `[trigger: seed_quality]` `[factor_trigger: astro_conception AND astro_ambient]` `[role: 条件分支]` The seed receives its due quality from the Ambient at conception—the initial stellar imprint. → Seed
- `[ns_ptolemy_iii_029]` `[trigger: sympathetic_timing]` `[factor_trigger: astro_conception AND astro_birth]` `[role: 条件分支]` Nature times birth to correspond with conception positions through sympathetic correspondence. → Connection
- `[ns_tetra_iii_cb]` `[trigger: chart_birth]` `[factor_trigger: chart_birth]` `[role: 主干]` Birth chart serves as practical origin when conception time is unknown—the moment of manifestation with senses and movement. → Source Text III.2
- `[ns_tetra_iii_cc]` `[trigger: chart_conception]` `[factor_trigger: chart_conception]` `[role: 条件分支]` Conception chart is the natural origin—the seed receives its initial quality from the cosmic ambient at this moment. → Source Text III.2"""
    normalized_text_zh: str = """"""
    subject: str = "Conception and Birth (Chapter II)"
    factor_refs: list = ['engine_id', 'chart_conception', 'astrology_classical', 'chart_birth', 'astrology_classical', 'source_ref', 'rel_iii_010', 'chart_conception', 'equivalent', 'rel_iii_010b', 'astro_conception_chart', 'grounding', 'evi_iii_010', 'chart_conception', 'rule_conception', 'concept_origin', 'chart_origin', 'birth_trauma']
    
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
        l1_anchor="tb_v1.0.0_conception_and_birth__chapter__001_L1",
    )
    version: str = "1.0.0"
