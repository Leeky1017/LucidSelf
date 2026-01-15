"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997581
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
    semantic_id="dts_v1.0.0_真假参差难辨论_不明不暗受邅迍_提纲不与真神照_暗处寻真也有_001",
    book_id="dts",
    engine_id="bazi"
)
class 真假参差难辨论不明不暗受邅迍提纲不与真神照暗处寻真也有(SemanticEntry):
    """
    - **原文（source_text）**：
  真假参差难辨论，不明不暗受邅迍。提纲不与真神照，暗处寻真也有真。

- 原注（原文注解）：
  　　命之真者得令，假神得局而党多，或假神得令，真神得局...
    """
    
    original_text: str = """- **原文（source_text）**：
  真假参差难辨论，不明不暗受邅迍。提纲不与真神照，暗处寻真也有真。

- 原注（原文注解）：
  　　命之真者得令，假神得局而党多，或假神得令，真神得局而党多，不见真假之迹，或真假皆得令得助，不能辨其胜负……寅月生人，不透木火而透金水为用神，是为提纲不照也，得巳丑暗邀，戊巳转生，酉冲卯，乙庚暗化，气转西方，亦为有真，亦或发福。以上特举一端耳。

- **规范化释义（primary_lang_explained）**：
  提纲不照时，可从“暗邀/暗化/冲会”中寻真；真假并陈，须察“谁得令、谁得势”。

- 分字分词释义：
  - 参差：错杂不齐。
  - 邅迍：艰难、迟滞之状。
  - 提纲不照：月令之神未透干以为纲领。
  - 暗处寻真：从暗合、暗会、暗化、冲邀中寻其真。



- **次语种完整诠释（secondary_lang_full）**:  
  Ambiguous Zhen-Jia: When True and False are mixed and hard to distinguish (Can-Ci Nan-Bian), life is difficult (Zhan-Zhun). If the Month Command does not reveal the True God (Ti-Gang Bu-Zhao), look for "Hidden Truth" (An-Chu Xun-Zhen) in hidden combinations or transformations."""
    normalized_text_zh: str = """"""
    subject: str = "真假参差难辨论，不明不暗受邅迍，提纲不与真神照，暗处寻真也有真。"
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_真假参差难辨论_不明不暗受邅迍_提纲不与真神照_暗处寻真也有_001_L1",
    )
    version: str = "1.0.0"
