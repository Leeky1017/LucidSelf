"""
Auto-generated semantic module for learning_tarot
Generated at: 2025-12-05T13:30:20.008163
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
    semantic_id="lt_v1.0.0_judgement__审判_001",
    book_id="learning_tarot",
    engine_id="tarot"
)
class Judgement审判(SemanticEntry):
    """
    **Source Text** (Lines 4782-4845): Keywords: Judgment • Inner Calling • Rebirth • Absolution

**Engl...
    """
    
    original_text: str = """**Source Text** (Lines 4782-4845): Keywords: Judgment • Inner Calling • Rebirth • Absolution

**English Paraphrase**: **Judgement (Card 20)** represents "the feelings that come with salvation"—rebirth, cleansed of guilts and burdens. "You may feel a calling—a personal conviction of what you are meant to do."

**Complete Chinese Interpretation**: **审判（第20号牌）**代表"救赎带来的感觉"——重生、清除罪恶和负担。"你可能感到一种召唤——对你应该做什么的个人信念。"

**Core Points**: Card 20 = judgment, calling, rebirth, absolution; Salvation feelings; Personal conviction

**Narrative Snippets**:
- `[ns_ltt_067]` `[trigger: judgement_card]` `[factor_trigger: tarot_judgement AND tarot_rebirth]` `[role: 主干]` Judgement represents the psychological resurrection that follows deep self-confrontation: guilts are acknowledged and released, the dead past is integrated rather than repressed, a new self emerges purified by honest reckoning. → L4841-4842
- `[ns_ltt_068]` `[trigger: judgement_calling]` `[factor_trigger: tarot_judgement AND tarot_calling]` `[role: 主干依赖]` Judgement signals an inner summons to purpose: not external obligation but the soul's own demand for meaningful direction—the call cannot be ignored without consequences to psychic wholeness. → L4843-4844"""
    normalized_text_zh: str = """"""
    subject: str = "Judgement (审判)"
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
        l1_anchor="lt_v1.0.0_judgement__审判_001_L1",
    )
    version: str = "1.0.0"
