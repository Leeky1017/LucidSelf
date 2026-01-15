"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997339
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
    semantic_id="dts_v1.0.0_若然方局一齐来_须是干头无反复_001",
    book_id="dts",
    engine_id="bazi"
)
class 若然方局一齐来须是干头无反复(SemanticEntry):
    """
    - **原文（source_text）**：
  若然方局一齐来，须是干头无反复。

- 原注（原文注解）：
  　　如木局木方齐来，须要天干顺序，行运不悖。

- 分字分词释义：
  - 若然：假如...
    """
    
    original_text: str = """- **原文（source_text）**：
  若然方局一齐来，须是干头无反复。

- 原注（原文注解）：
  　　如木局木方齐来，须要天干顺序，行运不悖。

- 分字分词释义：
  - 若然：假如、如果。
  - 方局：方气（三会方）与局气（三合局）。
  - 一齐来：同时出现于命局中。
  - 须是：必须、务必。
  - 干头：天干的头部、主导天干。
  - 无反复：不来回折返、顺序一致。

- **规范化释义（primary_lang_explained）**：
  方与局同来，天干须顺序一致，行运亦当不相悖，方可成用。

- **次语种完整诠释（secondary_lang_full）**:  
  When Fang and Ju of the same element appear together, they create an impressive concentration of one kind of qi. This only becomes truly usable if the stems and the timing form a coherent chain. The main heavenly stems should follow one another along a clear line of generation or support, instead of jumping back and forth or undoing what the previous stem has built; and the major luck cycles should broadly move with this flow rather than cutting across it. If the stems reverse direction or the luck runs against the current, the combined power of Fang and Ju tangles into contradiction and cannot deliver stable results. The verse therefore stresses planning and order: when multiple strong structures are present, they must be organised into a single forward path."""
    normalized_text_zh: str = """"""
    subject: str = "若然方局一齐来，须是干头无反复。"
    factor_refs: list = ['fangju_yiqilai', 'gantou_wufanfu', 'shunxu', 'xingyun_bubei', 'chengyong', 'shuncheng_liantiao']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_若然方局一齐来_须是干头无反复_001_L1",
    )
    version: str = "1.0.0"
