"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460977
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
    semantic_id="iod_v1.0.0_chapter_v__the_material_and_so_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class ChapterVTheMaterialAndSo(SemanticEntry):
    """
    ### 5.1 Four Sources of Dream Material

#### Key Term Analysis

| Term | Definition | Significance |...
    """
    
    original_text: str = """### 5.1 Four Sources of Dream Material

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Four Sources | Recent/infantile/somatic/typical | Dream material origins |
| Day Residues | Recent impressions | Manifest material |
| Infantile Memory | Childhood experiences | Latent wish-structure |
| Typical Symbols | Universal elements | Shared by all |

**Source Text** (Synthesized):
> Dreams are constructed from the day's residues and from infantile memories. The material of dreams may be derived from: (1) recent and indifferent material; (2) infantile material; (3) somatic sources; (4) typical dreams with universal symbols.

**English Paraphrase (Primary Language)**:

Freud identifies **four sources** from which dream material is drawn:

| Source | Description | Example |
|--------|-------------|---------|
| **Recent impressions** | Events from last 1-2 days ("day residues") | Seeing a book → book appears in dream |
| **Infantile memories** | Childhood experiences, often forgotten | Childhood home reappears in adult dream |
| **Somatic stimuli** | Body sensations during sleep | Thirst → dream of drinking |
| **Typical symbols** | Universal dream elements shared by all | Falling, flying, teeth falling out |

**Key insight**: Recent impressions provide the **manifest material**; infantile memories provide the **latent wish-structure**.

**Complete Chinese Interpretation (Secondary Language)**:

弗洛伊德识别出梦境素材的**四个来源**：

| 来源 | 描述 | 示例 |
|------|------|------|
| **近期印象** | 过去1-2天的事件（"日残余"） | 看到书 → 梦中出现书 |
| **婴儿记忆** | 童年经历，常被遗忘 | 成人梦中重现童年之家 |
| **躯体刺激** | 睡眠时的身体感觉 | 口渴 → 梦见喝水 |
| **典型符号** | 人类共享的普遍梦元素 | 坠落、飞翔、掉牙 |

**关键洞见**：近期印象提供**显梦材料**；婴儿记忆提供**隐梦愿望结构**。

**Core Points**:
- Four sources: recent, infantile, somatic, typical.
- Day residues = hooks for deeper wishes.
- Infantile material = ultimate source of wish-energy.
- Somatic stimuli can be incorporated but not originate dreams.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Four Sources of Dream Material: Recent impressions (day residues), infantile memories, somatic stimuli, typical symbols. Recent=manifest material; Infantile=latent wish-structure.
- **中文**: 梦材料四源:近期印象(日残余)、婴儿记忆、躯体刺激、典型符号。近期=显梦材料;婴儿期=潜梦愿望结构。

**Narrative Snippets**:
- `[ns_freud_ch5_001]` `[trigger: four_sources]` `[factor_trigger: dream_material]` `[role: 主干]` Four sources: recent impressions, infantile memories, somatic stimuli, typical symbols. → Core
- `[ns_freud_ch5_002]` `[trigger: day_residue_manifest]` `[factor_trigger: dream_material AND day_residue]` `[role: 条件分支]` Recent impressions provide manifest material; day residues as starting hooks. → Structure
- `[ns_freud_ch5_003]` `[trigger: infantile_latent]` `[factor_trigger: dream_material AND infantile_memory]` `[role: 条件分支]` Infantile memories provide latent wish-structure; ultimate source of wish-energy. → Depth"""
    normalized_text_zh: str = """"""
    subject: str = "Chapter V: The Material and Sources of Dreams"
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
        l1_anchor="iod_v1.0.0_chapter_v__the_material_and_so_001_L1",
    )
    version: str = "1.0.0"
