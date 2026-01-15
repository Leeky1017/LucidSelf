"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.162884
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
    semantic_id="tb_v1.0.0_particular_constitutions_of_th_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class ParticularConstitutionsOfTh(SemanticEntry):
    """
    **Source Text**:
> The particular constitutions of the atmosphere are to be considered monthly at ea...
    """
    
    original_text: str = """**Source Text**:
> The particular constitutions of the atmosphere are to be considered monthly at each new and full moon... examining the angles and the planets configurated with them.

**English Paraphrase (Primary Language)**:
**Monthly weather** is predicted from each new and full moon by examining:
- Angular planets at the lunation
- Aspects to the lunation
- Sign quality (hot/cold, moist/dry)
- Fixed stars rising/setting

The Moon's configurations with planets determine specific weather events within each lunar month.

**Complete Chinese Interpretation (Secondary Language)**:
**每月天气**通过每次新月和满月预测，检查：朔望时的角宫行星、与朔望的相位、星座性质（热/冷、湿/干）、升起/落下的恒星。月亮与行星的配置决定每个农历月内的具体天气事件。

**Core Points**:
- Monthly weather from each new/full moon
- Angular planets at lunation = key indicators
- Sign quality modifies predictions
- Fixed stars add detail

**Narrative Snippets**:
- `[ns_tetra_ii009]` `[trigger: monthly_weather]` `[factor_trigger: astro_lunation_monthly]` `[role: 条件分支]` Monthly atmospheric constitutions predicted from each new and full moon—angular planets and aspects examined. → Source Text II.13
- `[ns_tetra_ii_mw]` `[trigger: monthly_weather]` `[factor_trigger: monthly_weather]` `[role: 效果]` Monthly weather pattern determined by lunation: angular planets, aspects to Moon, sign quality, and fixed stars at new/full moon. → Source Text II.13"""
    normalized_text_zh: str = """"""
    subject: str = "Particular Constitutions of the Atmosphere (Chapter XIII)"
    factor_refs: list = ['lunation_monthly']
    
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
        l1_anchor="tb_v1.0.0_particular_constitutions_of_th_001_L1",
    )
    version: str = "1.0.0"
