"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008194
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
    semantic_id="lt_v1.0.0_two_of_wands__权杖二_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class TwoOfWands权杖二(SemanticEntry):
    """
    **Source Text** (Lines 5044-5100): Keywords: Personal Power • Boldness • Originality

**English Para...
    """
    
    original_text: str = """**Source Text** (Lines 5044-5100): Keywords: Personal Power • Boldness • Originality

**English Paraphrase**: **Two of Wands** represents "personal power"—having a strong effect on people and events. "You command attention and cannot be ignored."

**Complete Chinese Interpretation**: **权杖二**代表"个人力量"——对人和事件有强大影响。"你吸引注意力，不容忽视。"

**Core Points**: Two of Wands = personal power, boldness, originality; Command attention; Pioneer spirit

**Narrative Snippets**:
- `[ns_ltt_073]` `[trigger: two_wands]` `[factor_trigger: tarot_two_wands]` `[role: 主干]` Two of Wands represents personal power—commanding attention. → L5044-5050"""
    normalized_text_zh: str = """"""
    subject: str = "Two of Wands (权杖二)"
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
        book_id="learning_tarot",
        chapter="",
        l1_anchor="lt_v1.0.0_two_of_wands__权杖二_001_L1",
    )
    version: str = "1.0.0"
