"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101579
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
    semantic_id="smth_v1.0.0_神煞取舍与重点体系_001",
    book_id="sanming",
    engine_id="bazi"
)
class 神煞取舍与重点体系(SemanticEntry):
    """
    - **原文（source_text）**：
  总论诸神煞。神煞，古有百二十名，其说穿凿支离，造化恐不如是。除羊刃、空亡、劫煞、灾煞、大煞、元辰、勾绞、咸池、破碎、罗网、冲击、天空、悬针、平头、倒戈...
    """
    
    original_text: str = """- **原文（source_text）**：
  总论诸神煞。神煞，古有百二十名，其说穿凿支离，造化恐不如是。除羊刃、空亡、劫煞、灾煞、大煞、元辰、勾绞、咸池、破碎、罗网、冲击、天空、悬针、平头、倒戈等煞命中切要者，已备论于前矣，兹以诸星家考验有理者，复备叙于左。

- **分字分词释义**：
  - **百二十名神煞**：点出传统神煞体系繁多且多有牵强之处。
  - **穿凿支离**：批评部分神煞之说缺乏依据、逻辑支离。
  - **命中切要者**：强调只有少数与命局结构关系密切、在实践中多次验证的要煞值得重点把握。

- **规范化释义（primary_lang_explained）**：
  本节首先对神煞体系作总评：历代星命家所立神煞名目繁多，其中多有牵强附会之说。作者因此只保留少数与命局结构关系密切、在实践中多次验证的要煞，如羊刃、空亡、劫煞、灾煞、元辰、勾绞、罗网等，并对其进行系统论述。余下的诸煞，只在确有经验依据时略作附录，不主张以一星定终身。

- **次语种完整诠释（secondary_lang_full）**：
  This general summary critiques the proliferation of over 120 Shen Sha (Spirits and Killings) in historical texts, labeling many as forced or fragmented logic. The author advocates for a "Less but Precise" approach, retaining only the verified and structural Sha (such as Yang Ren, Kong Wang, Jie Sha, Zai Sha, Yuan Chen, Gou Jiao, Luo Wang) as core indicators. Other minor Sha are treated as appendices and should only be used when strictly verified by experience, avoiding the pitfall of judging a destiny by a single star.

- **核心要点**：
  - 批判神煞名目泛滥与穿凿
  - 确立“少而精”的核心神煞体系
  - 强调实践验证与结构优先

- **详细解说**：
  在应用层面，本节提出了神煞使用的分级原则。"""
    normalized_text_zh: str = """"""
    subject: str = "神煞取舍与重点体系"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_神煞取舍与重点体系_001_L1",
    )
    version: str = "1.0.0"
