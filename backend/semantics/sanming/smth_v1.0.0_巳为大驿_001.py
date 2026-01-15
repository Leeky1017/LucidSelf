"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042692
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
    semantic_id="smth_v1.0.0_巳为大驿_001",
    book_id="sanming",
    engine_id="bazi"
)
class 巳为大驿(SemanticEntry):
    """
    - **原文（source_text）**：
  巳为大驿。大驿者，人烟凑集，道路通达之地。巳中有丙火戊土，是其象也，又巳前有午马，故曰大驿。巳生喜得辰时，蛇化轻龙，于格为千里龙驹。

- **分字分...
    """
    
    original_text: str = """- **原文（source_text）**：
  巳为大驿。大驿者，人烟凑集，道路通达之地。巳中有丙火戊土，是其象也，又巳前有午马，故曰大驿。巳生喜得辰时，蛇化轻龙，于格为千里龙驹。

- **分字分词释义**：
  - **大驿**：交通枢纽、驿站之地，人流汇集、道路四通八达。
  - **丙火戊土**：巳中所藏，象征热力与土台，利于商旅往来。
  - **蛇化轻龙**：巳为蛇，得辰则如化龙，喻由平凡到显达。

- **规范化释义（primary_lang_explained）**：
  巳被称作「大驿」，类似古代驿站或现代交通节点，人烟聚集、道路通达。巳中藏丙火戊土，既有热力又有承载，利于活动频繁。巳生人得辰时，有「蛇化轻龙」之象，从普通行旅变成千里龙驹，强调在流动与迁移中获得跃升机会。

- **完整对等诠释（secondary_lang_full）**：
  Si is called the great relay station, like a major inn or modern transport hub where people converge and roads branch out in many directions. Within Si are hidden Bing Fire and Wu Earth, giving both driving force and a platform strong enough to bear the constant coming and going. A person born in Si who meets Chen at the hour is said to show “the snake turning into a light dragon”: the snake of Si gains the lift of the Dragon and becomes a swift steed able to cover a thousand li, a metaphor for upgrades achieved through movement. In reading a life, Si‑as‑relay points to careers and stages built around transit, transfer and repeated change of scene—sales, consultancy, logistics, cross‑regional projects—where the art is to turn each stopover into a step up rather than mere exhaustion."""
    normalized_text_zh: str = """"""
    subject: str = "巳为大驿"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'si_chen_combo', 'channel_capacity_index', 'cross_domain_connectivity_index', 'bazi_semantic', 'energy_burn_rate_index', 'environment_volatility_level', 'burnout_scattered_effort_risk_flag', 'source_ref', 'rel_smth_sdy_001', 'si', 'rel_smth_sdy_002', 'si_chen', 'rel_smth_sdy_003', 'sixiang', 'evi_smth_sdy_001', 'si_dayi', 'rule_sdy', 'concept_transit_hub']
    
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
        l1_anchor="smth_v1.0.0_巳为大驿_001_L1",
    )
    version: str = "1.0.0"
