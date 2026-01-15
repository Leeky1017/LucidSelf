"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008236
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
    semantic_id="lt_v1.0.0_six_of_wands__权杖六_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class SixOfWands权杖六(SemanticEntry):
    """
    **Source Text** (Lines 5272-5328): Keywords: Triumph • Acclaim • Pride

**English Paraphrase**: **Si...
    """
    
    original_text: str = """**Source Text** (Lines 5272-5328): Keywords: Triumph • Acclaim • Pride

**English Paraphrase**: **Six of Wands** represents "triumph"—receiving acclaim, achieving success, being proud of accomplishments.

**Complete Chinese Interpretation**: **权杖六**代表"胜利"——获得赞誉、取得成功、为成就感到自豪。

**Core Points**: Six of Wands = triumph, acclaim, pride; Victory parade; Public recognition

**Narrative Snippets**:
- `[ns_ltt_077]` `[trigger: six_wands]` `[factor_trigger: tarot_six_wands AND tarot_victory]` `[role: 主干]` Six of Wands depicts the victory parade: public recognition of achievement, riding high with wreath of success; the moment when effort receives external validation—enjoy it, but remember that acclaim is temporary and not the goal itself."""
    normalized_text_zh: str = """"""
    subject: str = "Six of Wands (权杖六)"
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
        l1_anchor="lt_v1.0.0_six_of_wands__权杖六_001_L1",
    )
    version: str = "1.0.0"
