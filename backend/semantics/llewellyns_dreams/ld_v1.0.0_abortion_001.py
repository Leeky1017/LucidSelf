"""
Auto-generated semantic module for llewellyns_dreams
Generated at: 2025-12-05T13:30:20.386864
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
    semantic_id="ld_v1.0.0_abortion_001",
    book_id="llewellyns_dreams",
    engine_id="dream"
)
class Abortion(SemanticEntry):
    """
    | Term | Definition | Significance |
|------|-----------|---------------|
| Abortion | Aborted creat...
    """
    
    original_text: str = """| Term | Definition | Significance |
|------|-----------|---------------|
| Abortion | Aborted creativity | Not literal |
| Symbolic Pregnancy | Idea/project gestation | Nascent potential |
| Termination Choice | Conscious decision | Responsibility |
| Rarely Literal | Unless processing | Actual decision |

**Source Text** (Paraphrased):
> "Fetus as symbol for idea or project in gestation. Abortion represents choice to eliminate that possibility for something new. From symbolic perspective, choosing to eliminate an action course you're not prepared to take responsibility for. Rarely about literal abortion unless dreamer actively processing that decision."

**English Paraphrase**:
**Abortion**: Fetus = **idea/project in gestation**. Abortion = **choice to eliminate** that possibility. Symbolic perspective: choosing to end action course not prepared to take responsibility for. Can represent: Abandoned creative project, Canceled plan, Rejected new direction, Terminated beginning. Rarely literal unless actively processing actual abortion decision.

**Complete Chinese Interpretation**:
**堕胎**：胎儿=**孕育中想法/项目**。堕胎=**选择消除**该可能性。象征视角：选择结束不准备负责任的行动路线。可代表：放弃创造项目、取消计划、拒绝新方向、终止开端。罕为字面除非正积极处理实际堕胎决定。

#### Core Points

- **Symbolic Pregnancy**: Fetus = idea/project in gestation, not literal baby.
- **Choice to Eliminate**: Abortion = conscious decision to end nascent potential.
- **Responsibility Theme**: Choosing to eliminate action course not prepared to take responsibility for.
- **Rarely Literal**: About actual abortion only if actively processing that decision.
- **Creative Termination**: Can represent abandoned projects, canceled plans, rejected new directions.

#### Detailed Explanation

Fetus as symbol represents an idea or project in gestation. Abortion in dreams represents the choice to eliminate that possibility for something new. From a symbolic perspective, it means choosing to eliminate an action course you're not prepared to take responsibility for. It can represent: abandoned creative project, canceled plan, rejected new direction, terminated beginning. The dream is rarely about literal abortion unless the dreamer is actively processing that actual decision."""
    normalized_text_zh: str = """"""
    subject: str = "Abortion"
    factor_refs: list = ['dream_symbol_abortion', 'dream_symbolic_pregnancy', 'psych_responsibility_avoid']
    
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
        book_id="llewellyns_dreams",
        chapter="",
        l1_anchor="ld_v1.0.0_abortion_001_L1",
    )
    version: str = "1.0.0"
