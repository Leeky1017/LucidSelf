"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482389
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
    semantic_id="iod_v1.0.0_source_text_004",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "The first thing that becomes clear to anyone who compares the dream-content with the dream-thoughts...
    """
    
    original_text: str = """"The first thing that becomes clear to anyone who compares the dream-content with the dream-thoughts is that a tremendous work of condensation has been accomplished. The dream is meagre, paltry and laconic in comparison with the range and copiousness of the dream-thoughts. The dream, when written down, fills half a page; the analysis, which contains the dream-thoughts, requires six, eight, twelve times as much space."

#### English Paraphrase (Primary Language)

Condensation is the first major mechanism of dream-work, whereby multiple latent thoughts are compressed into a single manifest element. The manifest dream appears remarkably brief and sparse compared to the rich, extensive network of latent thoughts underlying it. A dream that occupies half a page when written requires many pages of analysis to uncover all the condensed meanings. Dream condensation works through several methods: composite figures (one person with features of several), collective figures (one character representing many), verbal condensation (puns, portmanteau words), and overdetermination (single elements carrying multiple meanings simultaneously).

#### Complete Chinese Interpretation

在具体操作层面，**凝缩**是梦的工作中最典型、也最容易观察到的一种机制。弗洛伊德指出，如果把显梦内容与分析中呈现的潜梦材料进行对比，就会发现一个惊人的比例差：半页纸的梦叙述，往往需要六到十二页的联想笔记才能解释清楚。这意味着，来自不同来源的大量思想与记忆，被压进了寥寥数个画面与词语之中。

凝缩的常见形式包括：**复合人物**——梦中某个角色同时具有多个人的面貌、口气与行为特征；**集合人物**——一个“老师”或“医生”代表了整类权威对象；以及**文字层面的合成词与双关语**，一个怪异的名字或词语背后往往叠加了数个线索。这些技术使得一个梦中形象可以同时承载多重关系、记忆和情绪，既节省了“篇幅”，又提高了隐蔽性。

此外，梦中的每个元素通常是**多重决定的**：一幢房子可能同时指向童年故居、当前住处、母体意象乃至分析室本身，从而成为多个潜梦思想的交汇点。对分析者来说，真正的任务不是为一个符号寻找单一固定含义，而是通过自由联想，把那个被压缩进去的复杂网络重新展开。

从防御角度看，凝缩帮助梦在有限的可呈现空间里，既表达了欲望，又避免直白暴露其全部内容；从认识论角度看，它揭示了无意识思维的一个特色：倾向于把看似无关的材料编织成高密度的意象节点，而不是清晰分割的单线性叙事。

#### Core Points

- **Compression principle**: Multiple latent thoughts condensed into single manifest elements
- **Economy of representation**: Brief manifest dream represents extensive latent material
- **Methods**: Composite figures, collective persons, verbal condensation, overdetermination
- **Analysis expansion**: Dream text expands many-fold when latent content revealed
- **Disguise function**: Makes latent thoughts unrecognizable in manifest form

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Condensation (Verdichtung) | Multiple into single | Primary dream mechanism |
| Composite Figure | One figure with many features | Common condensation type |
| Overdetermination | One element, multiple causes | Convergence point |
| Compression Ratio | Manifest:Latent ~1:6-12 | Extent of condensation |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Condensation compresses multiple latent thoughts into single manifest elements. Composite figures, overdetermination. Brief dream expands 6-12x in analysis.
- **中文**: 凝缩将多个潜梦思想压缩为单一显梦元素。复合人物、多重决定。简短梦在分析中扩展6-12倍。

**Narrative Snippets**:
- `[ns_freud_013]` `[trigger: condensation_principle]` `[factor_trigger: condensation AND composite_figure]` `[role: 主干]` A tremendous work of condensation has been accomplished—the dream is meagre and laconic in comparison with the range of dream-thoughts. → Source Text
- `[ns_freud_014]` `[trigger: compression_ratio]` `[factor_trigger: disproportion_ratio AND dream_abortion]` `[role: 主干依赖]` The dream fills half a page; the analysis requires six, eight, twelve times as much space. → Source Text
- `[ns_freud_015]` `[trigger: composite_figures]` `[factor_trigger: day_residue AND day_residues]` `[role: 条件分支]` Condensation creates composite figures—one dream character with features of several real persons. → English Paraphrase
- `[ns_freud_016]` `[trigger: overdetermination]` `[factor_trigger: overdetermination AND nodal_point]` `[role: 总结]` Each manifest element is overdetermined—multiply caused by several latent thoughts converging on it. → English Paraphrase

#### Detailed Explanation

Condensation is perhaps the most characteristic and universal mechanism of dream-work. It explains why dreams appear so cryptic and compressed—a vast network of thoughts and associations has been condensed into a remarkably economical manifest representation.

The compression ratio is striking: what takes half a page to recount as manifest dream may require six, eight, or twelve pages of associative material to unpack the underlying latent thoughts. This is not because the analyst adds extraneous material but because the dream has genuinely compressed multiple meanings into single elements through various techniques.

**Composite figures** are a primary condensation method. A dream character may have the face of person A, the voice of person B, the clothing of person C, and behave like person D—creating a single composite representing all four. This allows the dream to express multiple relationships and thoughts simultaneously through one figure.

**Collective figures** represent a category rather than specific individuals—"a professor" represents all authority figures the dreamer has encountered, condensing many specific memories and attitudes.

**Verbal condensation** creates portmanteau words or puns that combine multiple meanings. Freud's famous example "Norekdal" combined "Nora" (person's name), "Ekdal" (Ibsen character), and other associations into one dream-word expressing multiple thoughts simultaneously.

**Overdetermination** means each manifest element is multiply determined by several latent thoughts converging on it. A dream image of a house might simultaneously represent childhood home, current residence, mother's body, and the analytical setting—all condensed into one symbol.

Condensation serves the dream-work's need for economy and disguise. It reduces the bulk of latent material to manageable manifest size while simultaneously making the latent thoughts unrecognizable through compression. The analyst must reverse this process, expanding the compressed manifest elements back into their full latent richness.

---"""
    normalized_text_zh: str = """"""
    subject: str = "Source Text"
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
        l1_anchor="iod_v1.0.0_source_text_004_L1",
    )
    version: str = "1.0.0"
