"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042554
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
    semantic_id="smth_v1.0.0_五行用法与中和之贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 五行用法与中和之贵(SemanticEntry):
    """
    - 原文（source_text）：
  大抵五行用法，总无真实，生死衰旺，亦假名耳。直向源头，明其出处，如五阳为刚，五阴为柔。若失令身衰，不遇资扶而频泄气，则刚者失其为刚；若得令身强，用事有助，则柔...
    """
    
    original_text: str = """- 原文（source_text）：
  大抵五行用法，总无真实，生死衰旺，亦假名耳。直向源头，明其出处，如五阳为刚，五阴为柔。若失令身衰，不遇资扶而频泄气，则刚者失其为刚；若得令身强，用事有助，则柔者不失之柔。中间又分木火为阳，金水为阴，皆喜生扶资助，要以中和为贵。

- 分字分词释义：
  - **总无真实、生死衰旺亦假名**：强调各类长生旺衰之名，只是为了指示气机状态，非实有之物。
  - **五阳为刚、五阴为柔**：回到十干阴阳本性，以刚柔之别作为判断气质的源头标准。
  - **中和为贵**：五行运用的最高原则在于阴阳不偏、刚柔得所，而非一味追求旺盛。

- 规范化释义（primary_lang_explained）：
  这一段是对前文全卷的总收束：五行所谓「生、旺、衰、死」，只是方便的名称，用来描述气机处于不同阶段的状态，并不是绝对固定的吉凶标签。关键要看此行之气是否得时得势、是否有资扶、有制约：若失令又屡遭克泄，再刚的阳气也会失其刚健；反过来，若得令而又有人事、运势相助，再柔的阴气也能保持柔而不弱。木火总归属阳，金水总归属阴，但不论阴阳，都喜生扶资助，最终目的都是让全局趋于中和，而不是单点极旺。"""
    normalized_text_zh: str = """"""
    subject: str = "五行用法与中和之贵"
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
        l1_anchor="smth_v1.0.0_五行用法与中和之贵_001_L1",
    )
    version: str = "1.0.0"
