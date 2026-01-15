"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.192757
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
    semantic_id="tb_v1.0.0_number_of_prorogators_and_part_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class NumberOfProrogatorsAndPart(SemanticEntry):
    """
    **Source Text** (Lines 5601-5708):
> After due attention has been given to the prorogatory places, t...
    """
    
    original_text: str = """**Source Text** (Lines 5601-5708):
> After due attention has been given to the prorogatory places, the Sun, the Moon, the Ascendant, and the Part of Fortune, are to be considered as the four principally liable to be elected to the office of prorogator... By day the Sun is to be preferred, provided he be situated in a prorogatory place; if not, the Moon; if the Moon also not, then that planet with most dominion, then the ASC. By night, the Moon is preferred first.

**English Paraphrase (Primary Language)**:
**Prorogator candidates** (four principal):
1. Sun
2. Moon
3. Ascendant
4. Part of Fortune (calculated from Sun-Moon-ASC relationship)

**Selection by sect**:
- **By day**: Sun first → Moon → Ruling planet → ASC
- **By night**: Moon first → Sun → Ruling planet → ASC or Part of Fortune

**Part of Fortune calculation**: Compute degrees from Sun to Moon, then place that distance from ASC in sign order. It becomes a "lunar horoscope."

**Ruling planet selection**: Planet with most dignities over Sun (day) or Moon (night), the prenatal lunation, and ASC—at least 3 of 5 dignities required.

**Complete Chinese Interpretation (Secondary Language)**:
**主限星候选**（四个主要）：
1. 太阳
2. 月亮
3. 上升点
4. 福点（从太阳-月亮-上升关系计算）

**按昼夜派选择**：
- **白天**：太阳优先 → 月亮 → 主星 → 上升
- **夜晚**：月亮优先 → 太阳 → 主星 → 上升或福点

**福点计算**：计算太阳到月亮的度数，然后按星座顺序从上升放置该距离。它成为"月亮地平"。

**主星选择**：对太阳（白天）或月亮（夜晚）、产前朔望和上升拥有最多尊贵的行星——至少需要5个尊贵中的3个。

**Core Points**:
- Four principal prorogator candidates
- Sect determines selection priority
- Part of Fortune = lunar horoscope
- Ruling planet needs 3+ dignities

**Narrative Snippets**:
- `[ns_tetra_iii024]` `[trigger: prorogator_selection]` `[factor_trigger: astro_prorogator]` `[role: 主干]` Four prorogator candidates: Sun, Moon, ASC, Part of Fortune—selection follows sect rules. → Source Text III.13"""
    normalized_text_zh: str = """"""
    subject: str = "Number of Prorogators and Part of Fortune (Chapter XIII)"
    factor_refs: list = ['engine_id', 'prorogator', 'astrology_classical', 'part_fortune', 'astrology_classical', 'source_ref', 'rel_iii_024', 'astro_prorogator', 'priority', 'evi_iii_024', 'prorogator', 'rule_prorogator_sect', 'concept_prorogator', 'prorogator', 'life_force']
    
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
        l1_anchor="tb_v1.0.0_number_of_prorogators_and_part_001_L1",
    )
    version: str = "1.0.0"
