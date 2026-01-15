"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042674
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
    semantic_id="smth_v1.0.0_寅为广谷_001",
    book_id="sanming",
    engine_id="bazi"
)
class 寅为广谷(SemanticEntry):
    """
    - **原文（source_text）**：
  寅为广谷。寅乃艮方，艮为山，戊土长生于是，而广谷之义著矣。然寅宫有虎，寅生人而时戊辰者，谓之虎啸而谷风生，威震万里。

- **分字分词释义**：
 ...
    """
    
    original_text: str = """- **原文（source_text）**：
  寅为广谷。寅乃艮方，艮为山，戊土长生于是，而广谷之义著矣。然寅宫有虎，寅生人而时戊辰者，谓之虎啸而谷风生，威震万里。

- **分字分词释义**：
  - **广谷**：宽广的山谷，象征山地之间的通道与气流。
  - **艮为山、戊土长生**：寅宫山势与厚土并存。
  - **虎啸谷风生**：寅中有虎象，虎啸引动谷风，喻威势与号召。

- **规范化释义（primary_lang_explained）**：
  寅居艮位，为山之象，又为戊土长生之处，故名「广谷」：山谷宽阔、气流通达。寅宫藏甲丙戊，有虎之象；寅生人而时支见戊辰，如虎啸山谷，谷风随之而起，象征威名远播、能动山川之势。地理上，寅多指山谷要道、交通隘口等处。

- **完整对等诠释（secondary_lang_full）**：
  Yin occupies the Gen sector and takes the shape of mountains, yet within it lies a broad valley where Wu Earth is born. Hence the name “wide valley”: cliffs on both sides, a spacious channel in between, and winds that can travel far. Yin hides Jia, Bing and Wu and so contains the image of the Tiger; when a Yin‑born person meets Wu‑Chen at the hour, the text speaks of “the tiger roaring and valley winds arising”, a picture of authority that can stir currents well beyond its immediate spot. Geographically, this points to passes, gorges, transport corridors and other choke points between regions. Interpreted in life reading, Yin‑as‑wide‑valley marks positions where one stands at an interface—between centres, systems or groups—through which flows of people, resources or influence must pass, and where a single roar or decision can change the direction of the wind."""
    normalized_text_zh: str = """"""
    subject: str = "寅为广谷"
    factor_refs: list = ['source_ref', 'rel_smth_ygg_001', 'yin', 'rel_smth_ygg_002', 'yin_wuchen', 'rel_smth_ygg_003', 'yinxiang', 'evi_smth_ygg_001', 'yin_guanggu', 'rule_ygg', 'concept_channel_hub']
    
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
        l1_anchor="smth_v1.0.0_寅为广谷_001_L1",
    )
    version: str = "1.0.0"
