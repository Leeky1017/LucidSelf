"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.477364
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
    semantic_id="iod_v1.0.0_1_symbolic_interpretation_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 1SymbolicInterpretation(SemanticEntry):
    """
    **Source Text**:
"The first of these procedures regards the dream content as a whole and seeks to re...
    """
    
    original_text: str = """**Source Text**:
"The first of these procedures regards the dream content as a whole and seeks to replace it by another content which is intelligible and in certain respects analogous. This is symbolic dream interpretation."

"The construction which the biblical Joseph places upon the dream of Pharaoh furnishes an example: The seven fat kine, after which came seven lean ones which devour the former, furnish a symbolic substitute for a prediction of seven years of famine in the land of Egypt."

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Symbolic Interpretation | 象征解释 | Treating dream as unified symbol | Pre-scientific; relies on intuition |
| Dream Content as Whole | 梦内容整体 | Entire dream = single meaning | Loses individual elements |
| Intelligible Substitute | 可理解的替代 | Clear meaning replacing obscure | Joseph's Pharaoh interpretation |
| Analogous Content | 类比内容 | Similar structure, different domain | 7 kine → 7 years |

**English Paraphrase (Primary Language)**:

The **symbolic method** treats the dream as a unified whole and seeks a single, coherent meaning to replace it. This is the method of oracles, seers, and prophets. Joseph interpreting Pharaoh's dream of seven fat and seven lean cattle as predicting seven years of plenty followed by seven years of famine exemplifies this approach.

The method has two critical limitations:
1. It **fails entirely** with confused, incoherent dreams that resist unified interpretation
2. It depends on **intuition and genius** rather than teachable method—"success remains a matter of ingenious conjecture"

This method survives in popular dream books and folk interpretations, but cannot form the basis for scientific investigation.

**Complete Chinese Interpretation (Secondary Language)**:

**象征解释法**将梦作为统一整体处理，寻求单一、连贯的意义来替代它。这是神谕、预言者和先知的方法。约瑟解释法老的梦——七头肥牛和七头瘦牛预示七个丰年后接着七个荒年——就是这种方法的典范。

该方法有两个关键局限：
1. 对于混乱、不连贯的梦**完全失效**，因为它们抵抗统一解释
2. 依赖于**直觉和天赋**而非可教授的方法——"成功仍是巧妙猜测的结果"

这种方法在流行梦书和民间解释中存续，但无法形成科学研究的基础。

**Narrative Snippets**:

- `[ns_freud_method_001]` `[trigger: symbolic_method]` `[factor_trigger: dream_interpretation AND dream_symbol]` `[role: 主干]` Symbolic dream interpretation treats the dream content as a whole, seeking to replace it with another content which is intelligible and analogous—as Joseph interpreted Pharaoh's seven kine as seven years. → Freud Ch.II #Method
- `[ns_freud_method_002]` `[trigger: symbolic_limitation]` `[factor_trigger: dream_interpretation]` `[role: 条件分支]` Symbolic interpretation fails with confused dreams and depends on ingenious conjecture rather than teachable method—success remains a matter of intuition. → Freud Ch.II #Method"""
    normalized_text_zh: str = """"""
    subject: str = "1 Symbolic Interpretation"
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_1_symbolic_interpretation_001_L1",
    )
    version: str = "1.0.0"
