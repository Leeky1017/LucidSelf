"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228434
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
    semantic_id="smth_v1.0.0_癸未木性质_自库之木生旺则佳_001",
    book_id="sanming",
    engine_id="bazi"
)
class 癸未木性质自库之木生旺则佳(SemanticEntry):
    """
    - **原文（source_text）**：
  癸未木、自库之木，生旺则佳，虽乙丑金不能冲破，各归其根而不相犯。

- **分字分词释义**：
  - **自库之木**：自入库的木。
  - **生...
    """
    
    original_text: str = """- **原文（source_text）**：
  癸未木、自库之木，生旺则佳，虽乙丑金不能冲破，各归其根而不相犯。

- **分字分词释义**：
  - **自库之木**：自入库的木。
  - **生旺则佳**：生旺则好。
  - **不能冲破**：不能冲克破坏。
  - **各归其根而不相犯**：各自归根不互相侵犯。

- **规范化释义（primary_lang_explained）**：
  癸未木，是自入库的木，生旺则好，即使乙丑金也不能冲破，各自归根不互相侵犯。

- **完整对等诠释（secondary_lang_full）**：
  Guiwei belongs to Willow Wood and is pictured as Wood that has already entered its own storehouse. When it is in a lively, prosperous condition it is especially favourable: even Yichou Metal, which might appear strong enough to cut, is taken as unable to break its root or overturn its position. Instead, each returns to and abides in its own base, so that Metal and Wood keep to their proper spheres rather than attacking and destroying one another.

- **核心要点**：
  - 癸未为杨柳木，自库之木
  - 生旺则佳
  - 乙丑金不能冲破
  - 各归其根不相犯

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_214]` `[trigger: 癸未木性质]` `[factor_trigger: guiwei_wood_self_storage AND born_prosperous_good AND each_own_root]` `[role: 主干]` 癸未木、自库之木，生旺则佳，虽乙丑金不能冲破，各归其根而不相犯。 → 《三命通会》卷一#癸未木性质

- **详细解说**：
  此条解释癸未（杨柳木）的性质。癸未纳音也是木，是自入库的木（未为木库），生旺时很好，即使乙丑金（海中金）也不能冲破（丑未相冲但各有其根），各自归根互不侵犯。库木需要适当的生旺条件才能发挥作用。

- **校勘与字词辨析（双语）**：
  - **中文**："自库"指自己入库。"生旺"指生长旺盛。"冲破"指冲克破坏。"各归其根"指各有根基。
  - **English**: "Self-storage" means entering own storage. "Born-prosperous" means growing vigorously. "Clash-break" means clash and destroy. "Each returning to root" means each has own foundation."""
    normalized_text_zh: str = """"""
    subject: str = "癸未木性质：自库之木生旺则佳"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_癸未木性质_自库之木生旺则佳_001_L1",
    )
    version: str = "1.0.0"
