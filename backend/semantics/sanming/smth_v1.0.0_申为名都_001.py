"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042683
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
    semantic_id="smth_v1.0.0_申为名都_001",
    book_id="sanming",
    engine_id="bazi"
)
class 申为名都(SemanticEntry):
    """
    - **原文（source_text）**：
  申为名都。坤为地，其体无疆，非名都不足以喻之。申，坤也，都者，帝王所居。申宫壬水生，又与艮山对，是水绕山环也。凡命爱申年亥时，乃地天交泰。

- **...
    """
    
    original_text: str = """- **原文（source_text）**：
  申为名都。坤为地，其体无疆，非名都不足以喻之。申，坤也，都者，帝王所居。申宫壬水生，又与艮山对，是水绕山环也。凡命爱申年亥时，乃地天交泰。

- **分字分词释义**：
  - **名都**：大都会、京畿之地，象征人群与权力高度集中。
  - **申为坤地**：申与坤地相关，有广阔承载之象。
  - **水绕山环**：壬水生于申，与艮山相对，构成山水环抱。

- **规范化释义（primary_lang_explained）**：
  申被喻为「名都」，如帝王所居的都城：地广人众、权势交汇。申宫壬水长生，又与艮山相对，如山水环抱的名城格局。命局若逢申年亥时，有「地天交泰」之象：地气与天气相合，利于人在大都会中承接天时与地利。

- **完整对等诠释（secondary_lang_full）**：
  Shen is likened to a “famed capital”, the seat of rulers: wide land, dense population, converging lines of power. It carries Kun‑Earth qualities of breadth and capacity while also hosting the birth of Ren Water; opposite it stands the Gen mountain, so that city and hills form a ring of water and earth. Charts that combine a Shen year with a Hai hour are said to show “earth and heaven in exchange”, an image of the capital as a place where terrestrial resources and heavenly timing meet and can be channelled. In practical terms, Shen‑as‑capital points toward life paths closely tied to big cities, core markets or major platforms, with all their mixed blessings: abundant resources, rich networks and visibility, but also competition, crowding and high pressure. The text invites us to see Shen not as automatic nobility but as an environment whose advantages must be consciously used and whose costs must be managed."""
    normalized_text_zh: str = """"""
    subject: str = "申为名都"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_申为名都_001_L1",
    )
    version: str = "1.0.0"
