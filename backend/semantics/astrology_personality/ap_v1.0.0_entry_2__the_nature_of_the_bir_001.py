"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.238319
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
    semantic_id="ap_v1.0.0_entry_2__the_nature_of_the_bir_001",
    book_id="astrology_personality",
    engine_id="astro"
)
class Entry2TheNatureOfTheBir(SemanticEntry):
    """
    **Source Text** (Lines 13574-13607):
> The birth-chart of an individual... is called also the radica...
    """
    
    original_text: str = """**Source Text** (Lines 13574-13607):
> The birth-chart of an individual... is called also the radical chart, being considered as the root-factor in all astrological interpretation. The term "root" is somewhat inaccurate, and "seed" would be a much better word...
>
> A birth-chart is the symbolical macrocosmic representation of the potential fullness of the perfected microcosm. It is the "blueprint" of the complete man. It is therefore nothing but a set of potentialities... Because it is a representation formed by macrocosmic factors (planets, horizon, etc.), it is purely symbolical. It indicates nothing factual; nothing concrete; nothing precisely "fated."

**Key Term Analysis**:
- **Radical chart**: `root-factor` / `seed better than root` / `archetypal form`
- **Blueprint**: `complete man` / `set of potentialities` / `symbolical, not factual`
- **Potentialities**: `nothing precisely fated` / `types of eventualities` / `varying actualizability`
- **Archetypal form**: `changeless throughout planetary cycle` / `contents unlimited`

**English Paraphrase (Primary Language)**:
Birth-chart = "blueprint of the complete man," a "set of potentialities." "Seed" better than "root."

"It indicates nothing factual; nothing concrete; nothing precisely 'fated.'" Only "types of potential eventualities, with varying degrees of actualizability."

The form (selfhood) is changeless; the contents are "relatively unlimited"—limited only by the "Ring-Pass-Not" of planetary evolution.

**Complete Chinese Interpretation (Secondary Language)**:
出生图 = "完整人的蓝图"，一套"潜能"。"种子"比"根"更好。

"它不指示任何事实；不指示任何具体的；不指示任何精确'命定的'。"只有"潜在可能性的类型，具有不同程度的可实现性。"

形式（自性）是不变的；内容是"相对无限的"——仅受行星进化的"不可逾越之环"限制。

**Narrative Snippets**:
- `[ns_aop_209]` `[trigger: birth_chart_nature]` `[factor_trigger: astro_chart_blueprint AND astro_birth_chart AND astro_selfhood AND astro_form]` `[role: 主干]` Birth-chart = blueprint of complete man; set of potentialities, not fated events. → L13583-13594
- `[ns_aop_210]` `[trigger: form_contents]` `[factor_trigger: astro_form_vs_contents]` `[role: 总结]` Form (selfhood) changeless; contents unlimited except Ring-Pass-Not. → L13687-13695"""
    normalized_text_zh: str = """"""
    subject: str = "Entry 2: The Nature of the Birth-Chart - Blueprint of Potentialities"
    factor_refs: list = ['birth_chart', 'ring_pass_not']
    
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
        l1_anchor="ap_v1.0.0_entry_2__the_nature_of_the_bir_001_L1",
    )
    version: str = "1.0.0"
