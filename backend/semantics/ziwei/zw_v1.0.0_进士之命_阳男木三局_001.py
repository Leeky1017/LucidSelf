"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699925
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
    semantic_id="zw_v1.0.0_进士之命_阳男木三局_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 进士之命阳男木三局(SemanticEntry):
    """
    - 分字分词释义：

  - **寅申最喜会同鸿**：寅申二宫喜得文星同会，主科名顺畅。
  - **禄权守照**：禄星与权星同时守照命宫，主富贵必矣。
  - **大限行辰太阳正照**：大限行至辰宫...
    """
    
    original_text: str = """- 分字分词释义：

  - **寅申最喜会同鸿**：寅申二宫喜得文星同会，主科名顺畅。
  - **禄权守照**：禄星与权星同时守照命宫，主富贵必矣。
  - **大限行辰太阳正照**：大限行至辰宫且太阳正照，主事业光明。
  - **小限寅卯**：小限在寅卯位，配合流年文星。
  - **流昌流曲文禄会身命**：流年文昌文曲与文禄同会身命，触发登科。
  - **连登官至四品上**：连续登科取得进士功名，官至四品以上。
  - **阳男木三局**：进士命盘的五行局数，木三局主生发科第。

- **原文（source_text）**：  
  进士之命。阳男木三局。寅申最喜会同鿄，且禄权守照，富贵必矣，故二十九、三十岁，大限行辰，太阳正照，小限寅卯，流昌流曲，文禄会身命，是以连登，官至四品上。

- **规范化释义（primary_lang_explained）**：  
  此条进士命为阳男木三局，「寅申最喜会同鿄」说明寅申二宫喜得文星同会，「且禄权守照」，禄星与权星同时守照命宫，「富贵必矣」。原文详述应期：「二十九、三十岁，大限行辰，太阳正照，小限寅卯，流昌流曲，文禄会身命」，在二十九至三十岁时，大限行至辰宫且太阳正照，小限在寅卯，流年文昌文曲与文禄同会身命，多重文星配合，「是以连登」，连续登科取得进士功名，「官至四品上」。此命例展示「中年早期大小限与流年文星同时配合而连登」的顺达进士命路径。

- **完整对等诠释（secondary_lang_full）**：  
  This "Jinshi" chart for a Yang Wood native in the Third Configuration especially favors Yin and Shen positions meeting literary stars. With Lu and Quan guarding Life, wealth and status are assured. At ages twenty‑nine to thirty, the major period enters Chen with Tai Yang shining directly; the minor period falls in Yin‑Mao; Flowing Chang and Qu plus Wen Lu all converge on Body and Life. Under this multi‑layer alignment, the native "registers consecutively"—achieving Jinshi and reaching Fourth Rank or above. This exemplifies a "smooth early‑mid‑life" Jinshi path where major, minor and annual periods all align favorably.

- **核心要点**：  
  1. 寅申会同文星配禄权守照，是必然富贵的进士格局。  
  2. 二十九至三十岁大限行辰、太阳正照，小限寅卯配流昌流曲文禄。  
  3. 多重文星与流年同时配合，连登进士，官至四品。"""
    normalized_text_zh: str = """"""
    subject: str = "进士之命（阳男木三局）"
    factor_refs: list = ['pattern_yinshen_wenxing', 'pattern_luquan_shouzhao', 'timing_daxian_chen_taiyang', 'timing_xiaoxian_yinmao', 'timing_liu_changqu_wenlu', 'result_liandeng_sipin']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_进士之命_阳男木三局_001_L1",
    )
    version: str = "1.0.0"
