"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460909
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
    semantic_id="iod_v1.0.0_example_1__the_botanical_monog_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class Example1TheBotanicalMonog(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Condensation | Multiple thoughts→one image | Core dream-work |
| Nodal Point | Where thought-chains intersect | Key symbol |
| Day Residue | Recent trivial stimulus | Entry point |
| Economic Principle | Max expression, min material | Dream efficiency |

**Source Text** (Freud's own dream):
"I have written a monograph on a certain plant. The book lies before me; I am just turning over a folded plate. A dried specimen of the plant, as though from a herbarium, is bound up with every copy."

**Analysis Summary**:
This seemingly trivial dream condenses multiple thought-chains:
1. **Recent stimulus**: Saw botanical monograph in bookshop window (day residue)
2. **Childhood memory**: Tearing apart books with colored plates as child
3. **Professional concern**: Colleague's monograph published, Freud feels competitive
4. **Botanical association**: Conversation about favorite flowers with wife
5. **Cocaine research**: Freud's early monograph on cocaine (pride + regret)

**Key Mechanism**: **Condensation** (凝缩)
- Single image (botanical book) represents **multiple unconscious thoughts**
- "Nodal point" where several thought-chains intersect
- Economic principle: Dream condenses to save psychic energy

**Complete Chinese Interpretation (Secondary Language)**:

“植物专著梦”表面只是一个极其简单的场景：弗洛伊德梦见自己写了一本关于植物的专著，每一册书中都夹着一份标本。若只看显梦，很容易以为这只是日间见到书店橱窗里植物学著作的余波。然而经自由联想后可以看到，这个单一意象背后实际上汇聚了**多条彼此迥异的思想链条**：童年时对彩色插图书籍的破坏性记忆、成年后对学术同行专著的嫉妒与竞争感、关于自己早期可卡因研究的骄傲与负疚，以及与妻子谈论喜爱花卉时的亲密经验。

这意味着，梦中的“植物书”并非单纯指向植物学，而是成为一个**“节点”（nodal point）**：多条记忆与情感在此压缩交汇。通过凝缩，梦工作用极少的显梦材料，承载了大量潜梦思想——既节省了“篇幅”（经济原则），又提高了隐蔽性，使得真正敏感的情感（如职业比较、学术野心、对以往科研判断的复杂情绪）被藏在一幅看似中性的图像之下。

因此，这个梦不仅是凝缩机制的经典示范，也展示了为何梦往往显得**既单薄又沉重**：文本上只有寥寥几句，背后却压着整片个人历史与情感网络。对分析者而言，真正的任务不是为“植物书”找到一个单一含义，而是沿着联想把这整束被压缩进去的生活经验重新展开。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Botanical Monograph Dream: Classic condensation example. Single image (botanical book) = nodal point for multiple thought-chains (childhood, competition, cocaine research, wife). Economic principle: minimal material, maximal expression.
- **中文**: 植物专著梦:经典凝缩示例。单一图像(植物书)=多条思想链的节点(童年、竞争、可卡因研究、妻子)。经济原则:最少材料,最大表达。

**Narrative Snippets**:
- `[ns_freud_ex_001]` `[trigger: condensation_example]` `[factor_trigger: dream_work_condensation]` `[role: 主干]` Botanical Monograph: single image = nodal point for multiple thought-chains. → Example
- `[ns_freud_ex_002]` `[trigger: economic_principle]` `[factor_trigger: dream_work_condensation AND efficiency]` `[role: 条件分支]` Economic principle: minimal manifest material, maximal latent expression. → Mechanism
- `[ns_freud_ex_003]` `[trigger: day_residue]` `[factor_trigger: dream_work_condensation AND trigger]` `[role: 条件分支]` Day residue (bookshop window) = entry point; connects to childhood, competition, cocaine research. → Structure"""
    normalized_text_zh: str = """"""
    subject: str = "Example 1: The Botanical Monograph Dream (Condensation)"
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
        l1_anchor="iod_v1.0.0_example_1__the_botanical_monog_001_L1",
    )
    version: str = "1.0.0"
