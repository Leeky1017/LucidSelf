"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460987
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
    semantic_id="iod_v1.0.0_2_day_residues_as_dream_instig_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 2DayResiduesAsDreamInstig(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Day Residues | Tagesreste | Starting material |
| Trivial Details | Less defended | Easier to use |
| Vehicle | Carries wish | Disguise function |
| Attachment | Wish hooks to residue | Formation mechanism |

**English Paraphrase (Primary Language)**:

**Day residues** (Tagesreste) = recent, often trivial impressions that serve as starting material for dreams.

**Function**:
- Not the true instigator (that is the unconscious wish).
- Provide **representational material** for disguising the wish.
- Why trivial details? **Less defended** by censorship → easier to use.

**Mechanism**:
1. Unconscious wish seeks expression.
2. Wish attaches to recent, indifferent impression.
3. Day residue becomes vehicle for disguised wish-fulfillment.

**Complete Chinese Interpretation (Secondary Language)**:

**日残余**（Tagesreste）= 近期的、常常琐碎的印象，作为梦的起始材料。

**功能**：
- 不是真正的发动者（那是无意识愿望）。
- 为伪装愿望提供**表征材料**。
- 为何是琐碎细节？**较少被审查防御** → 更易使用。

**机制**：
1. 无意识愿望寻求表达。
2. 愿望附着于近期的、无关紧要的印象。
3. 日残余成为伪装愿望满足的载体。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Day Residues: Recent trivial impressions providing representational material. Not true instigator (that's unconscious wish). Less defended by censorship. Unconscious wish attaches to day residue as vehicle.
- **中文**: 日残余:提供表征材料的近期琐碎印象。不是真正发动者(那是无意识愿望)。较少被审查防御。无意识愿望附着于日残余作为载体。

**Narrative Snippets**:
- `[ns_freud_ch5_004]` `[trigger: day_residues]` `[factor_trigger: dream_formation]` `[role: 主干]` Day residues (Tagesreste): recent trivial impressions as starting material, not true instigator. → Core
- `[ns_freud_ch5_005]` `[trigger: less_defended]` `[factor_trigger: dream_formation AND censorship]` `[role: 条件分支]` Trivial details preferred: less defended by censorship, easier to use. → Selection
- `[ns_freud_ch5_006]` `[trigger: vehicle_function]` `[factor_trigger: dream_formation AND wish_attachment]` `[role: 条件分支]` Unconscious wish attaches to day residue as vehicle for disguised fulfillment. → Mechanism"""
    normalized_text_zh: str = """"""
    subject: str = "2 Day Residues as Dream Instigators"
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
        l1_anchor="iod_v1.0.0_2_day_residues_as_dream_instig_001_L1",
    )
    version: str = "1.0.0"
