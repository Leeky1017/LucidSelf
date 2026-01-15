"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042408
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
    semantic_id="smth_v1.0.0_地支之用与月令为主_001",
    book_id="sanming",
    engine_id="bazi"
)
class 地支之用与月令为主(SemanticEntry):
    """
    - **原文（source_text）**：
  地支之用，不比天干，动静不同，圆方迥异。然五行所属则一，而所处之地不一。且如在年则有在年之论，在月则有在月之论，在日时则有日时之论，其阴阳、轻重、刚柔...
    """
    
    original_text: str = """- **原文（source_text）**：
  地支之用，不比天干，动静不同，圆方迥异。然五行所属则一，而所处之地不一。且如在年则有在年之论，在月则有在月之论，在日时则有日时之论，其阴阳、轻重、刚柔岂混于一体？今当以月提为主，所藏所用，要见何神，所耗所嫌，要系何物。凡四柱之神，较量深浅而用。

- **分字分词释义**：
  - **地支之用，不比天干**：支重在方位、动静与气场，干重在气质与发用，两者不可混同。
  - **圆方迥异**：圆指运行之轨迹，方指方位之定局，喻支在运动与空间上的多重角色。
  - **以月提为主**：以月支所主之令为纲，统摄年、日、时诸支的气机判断。

- **规范化释义（primary_lang_explained）**：
  本段先总纲：地支的用法不同于天干，着重在「所在之地」「所行之势」，同一五行在不同方位、不同时间段所起的作用并不一样。论命时年支有年支之说，月支有月支之说，日时又各有不同，阴阳、轻重、刚柔不能混作一团。实务上，以月令为核心，观其所藏何神、所助何神、所耗何物，再结合年、日、时诸支深浅轻重，方能立论。

- **完整对等诠释（secondary_lang_full）**：
  This passage establishes the fundamental principle that Earthly Branches operate differently from Heavenly Stems, focusing on "positional placement" and "directional momentum" rather than inherent qualities. The same Five Element manifests differently depending on its location and temporal phase. When analyzing destiny, Year Branch has its specific discourse, Month Branch its own, and Day-Hour Branches each carry distinct significance—yin-yang qualities, relative weights, and firmness-flexibility cannot be conflated into a single mass. In practical application, the Month Branch serves as the core framework: observe which deity it harbors, which it supports, and what it consumes or dislikes, then integrate the depth and weight of Year, Day, and Hour Branches to establish a coherent judgment. This creates a multi-layered environmental coordinate system where timing and spatial positioning determine how elemental forces manifest."""
    normalized_text_zh: str = """"""
    subject: str = "地支之用与月令为主"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_set', 'bazi_calculator', 'dizhi_to_season_mapping', 'bazi_calculator', 'pillar_role_label', 'bazi_semantic', 'seasonal_phase', 'bazi_calculator', 'season_alignment_score', 'bazi_calculator', 'wuxing_balance_score', 'bazi_calculator', 'missing_pillar_info_flag', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_地支之用与月令为主_001_L1",
    )
    version: str = "1.0.0"
