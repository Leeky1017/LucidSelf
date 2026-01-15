"""
Auto-generated semantic module for planets_in_transit
Generated at: 2025-12-05T13:30:20.224250
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
    semantic_id="pit_v1.0.0_sun_opposition_mercury__流年太阳冲本_001",
    book_id="planets_in_transit",
    engine_id="astro"
)
class SunOppositionMercury流年太阳冲本(SemanticEntry):
    """
    **Source Text** (Lines 2386-2417):
> Powerful stimulus to mind and communication. Almost continuous ...
    """
    
    original_text: str = """**Source Text** (Lines 2386-2417):
> Powerful stimulus to mind and communication. Almost continuous dialogue with others; tells you exactly how you stand. This is NOT the time to just tell everyone about yourself—listen carefully. If dominated by self-concern, a day of argument and unconstructive dispute. If receptive, you can learn much and promote your own ideas by showing they're not a threat.
> 
> Normally not a time to go in new direction—you're learning results of previous directions. Sometimes consult another person for a clear picture. Look at life as it is, not as you'd like it to be.

**English Paraphrase**: Powerful mind stimulus; continuous dialogue shows where you stand. NOT time to just talk—listen. Self-concern = argument. Receptivity = learning and idea promotion. Not time for new directions—learn previous results. Consult others for clear picture. See life as it is.

**Complete Chinese Interpretation**: 强大的心智刺激；持续对话显示你的立场。不是只说话的时候——要倾听。自我关注=争论。接受=学习和想法推广。不是新方向的时候——学习以前的结果。咨询他人获得清晰画面。看到生活本来的样子。

**Narrative Snippets**:
- `[ns_pit_071]` `[trigger: transit_sun_opposition_natal_mercury]` `[factor_trigger: astro_transit_sun OPPOSITION natal_mercury]` `[role: 主干]` Powerful stimulus to mind—continuous dialogue shows where you stand. Listen, don't just talk. → PIT Ch4 Sun☍Mercury
- `[ns_pit_072]` `[trigger: transit_sun_opposition_natal_mercury]` `[factor_trigger: astro_transit_sun OPPOSITION natal_mercury]` `[role: 条件分支]` If self-concerned: argument. If receptive: learn much. Look at life as it is, not as you'd like. → PIT Ch4 Sun☍Mercury"""
    normalized_text_zh: str = """"""
    subject: str = "Sun Opposition Mercury (流年太阳冲本命水星)"
    factor_refs: list = []
    
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
        l1_anchor="pit_v1.0.0_sun_opposition_mercury__流年太阳冲本_001_L1",
    )
    version: str = "1.0.0"
