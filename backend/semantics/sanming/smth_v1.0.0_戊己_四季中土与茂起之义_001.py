"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227562
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
    semantic_id="smth_v1.0.0_戊己_四季中土与茂起之义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊己四季中土与茂起之义(SemanticEntry):
    """
    - **原文（source_text）**：
  戊巳其位土，行周四季。戊，阳土也，万物生而出之，万物伐而入之。己，阴土也，无所为而得己者也。又云：戊，茂也；已，起也。土行四季之未，万物含秀者抑屈而起...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊巳其位土，行周四季。戊，阳土也，万物生而出之，万物伐而入之。己，阴土也，无所为而得己者也。又云：戊，茂也；已，起也。土行四季之未，万物含秀者抑屈而起也。

- 分字分词释义：
  - **戊，阳土也/茂也**：主外向、扩张之土，有生长、覆盖与护持之功。
  - **己，阴土也/起也**：主内向、收敛之土，在抑屈中托起万物。
  - **行周四季**：中土随四时轮转，在季季交接处发挥承上启下作用。

- **规范化释义（primary_lang_explained）**：
  戊己为中土，随四季轮转。戊土偏阳，如外向扩展的大地，既承载万物出生，也容纳万物归根；己土偏阴，如田畴细土，在抑屈之中托起新芽。二者合而为「四季之土」，在每个季节的末尾接住前一轮、开启下一轮。

- **完整对等诠释（secondary_lang_full）**：

  Wu and Ji are the central Earth that rotates through all four seasons. Wu Earth is the Yang, outward‑spreading aspect of soil, like a broad expanse of ground that both bears the emergence of ten thousand beings and receives them back when they are cut down. Ji Earth is the Yin, fine field‑soil that, even while pressed down and low, lifts new shoots from beneath the surface. Together they form the “Earth of the four seasons”, taking over at the end of each season to gather what has matured and to support the start of the next phase. In charts, Wu Earth represents frameworks and platforms that can host many things, while Ji Earth represents the digestive, repairing layer that processes details and keeps the overall system in balance."""
    normalized_text_zh: str = """"""
    subject: str = "戊己：四季中土与茂起之义"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_戊己_四季中土与茂起之义_001_L1",
    )
    version: str = "1.0.0"
