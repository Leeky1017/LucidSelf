"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237943
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
    semantic_id="ap_v1.0.0_entry_3__the_new_world_formula_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry3TheNewWorldFormula(SemanticEntry):
    """
    **Source Text** (Lines 4614-4674):
> The "New World" Formula: We claim that a third type of universa...
    """
    
    original_text: str = """**Source Text** (Lines 4614-4674):
> The "New World" Formula: We claim that a third type of universal integration is possible, which would emphasize neither the One-in-the-beginning, nor the "process" which we call "life"—but the ultimate sum total, the con-summation, the ingathering of all elements within the "circle of wholeness."...
>
> Perhaps the term "Holism" is as good as any to characterize this new attitude to life, if the meaning of the term is broadened beyond General Smuts' definition. We have used the phrase "philosophy of operative wholeness."...
>
> What is needed, however, is a simple symbolic presentation of life-principles such as we find in the old Yi King: a general formula which relates, centers and crystallizes all the new ideas and ideals... Astrological symbolism, as symbolism, may yet play a most important part in making concrete and intelligible some of the deepest ideas involved in the philosophy of the new civilization.

**Key Term Analysis**:
- **New World formula**: `emphasizes End/Consummation` / `ingathering within wholeness circle` / `integrates Hindu & Chinese`
- **Holism**: `operative wholeness philosophy` / `beyond Smuts` / `new civilization basis`
- **Astrology's role**: `symbolic presentation of life-principles` / `concretize deepest ideas` / `like Yi King`

**English Paraphrase (Primary Language)**:
Rudhyar proposes a "New World" formula emphasizing neither Beginning (Hindu) nor Process (Chinese), but "the ultimate sum total, the con-summation"—the End. This integrates features of both traditions plus Christianity's stress on personality.

"Holism" characterizes this new attitude—"philosophy of operative wholeness." Astrology can serve as the Yi King of this new civilization—"a general formula which relates, centers and crystallizes all the new ideas."

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar提出"新世界"公式，既不强调开始（印度）也不强调过程（中国），而是"最终的总和，圆满"——终点。这整合了两种传统的特点以及基督教对人格的强调。

"整体论"表征这种新态度——"运作整体性的哲学"。占星学可以作为这个新文明的易经——"一个关联、集中和结晶所有新观念的通用公式。"

**Narrative Snippets**:
- `[ns_aop_127]` `[trigger: new_formula]` `[factor_trigger: astro_new_formula AND astro_new_form_struct]` `[role: 主干]` New World formula: emphasizes End/Consummation, integrates Hindu+Chinese+Christian. → L4614-4627
- `[ns_aop_128]` `[trigger: holism_astrology]` `[factor_trigger: astro_holism_role AND astro_yi_king_role]` `[role: 总结]` Holism = operative wholeness; astrology as new Yi King for new civilization. → L4635-4674"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 3: The New World Formula—Holism"
    factor_refs: list = ['astro_new_formula', 'astro_oper_wholeness']
    
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
        book_id="astrology_personality",
        chapter="",
        l1_anchor="ap_v1.0.0_entry_3__the_new_world_formula_001_L1",
    )
    version: str = "1.0.0"
