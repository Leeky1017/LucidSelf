"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.461044
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
    semantic_id="iod_v1.0.0_3_the_role_of_the_unconscious__001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 3TheRoleOfTheUnconscious(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Unconscious Wish | Necessary condition | Every dream requires |
| Wish Hierarchy | Ucs/Pcs/somatic | Levels of contribution |
| Psychical Intensity | Energy to break through | Why Ucs necessary |
| Fundamental Claim | Core of Freud's theory | Chapter VII thesis |

**English Paraphrase (Primary Language)**:

**Central thesis of Chapter VII**: Every dream is instigated by an **unconscious wish**.

**Wish hierarchy**:
1. **Unconscious wish** (infantile, repressed) = necessary condition
2. **Preconscious wish** (day residue) = possible contributor
3. **Somatic stimulus** = possible contributor

**Key argument**: Without unconscious wish-energy, preconscious wishes cannot produce dreams; they lack the psychical intensity needed to force through the censorship.

**Complete Chinese Interpretation (Secondary Language)**:

**第七章核心论题**：每个梦都由一个**无意识愿望**发动。

**愿望层级**：
1. **无意识愿望**（婴儿期，被压抑的）= 必要条件
2. **前意识愿望**（日残余）= 可能贡献者
3. **躯体刺激** = 可能贡献者

**关键论证**：没有无意识愿望能量，前意识愿望无法产生梦；它们缺乏突破审查所需的心理强度。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Unconscious Wish: Necessary condition for every dream. Hierarchy: Ucs wish (necessary), Pcs wish (contributor), somatic stimulus (contributor). Without Ucs energy, Pcs wishes cannot force through censorship.
- **中文**: 无意识愿望:每个梦的必要条件。层级:无意识愿望(必要)、前意识愿望(贡献者)、躯体刺激(贡献者)。没有无意识能量,前意识愿望无法突破审查。

**Narrative Snippets**:
- `[ns_freud_ch7_007]` `[trigger: ucs_wish_necessary]` `[factor_trigger: dream_instigator]` `[role: 主干]` Every dream instigated by unconscious wish; Ucs wish = necessary condition. → Core
- `[ns_freud_ch7_008]` `[trigger: wish_hierarchy]` `[factor_trigger: dream_instigator AND levels]` `[role: 条件分支]` Hierarchy: Ucs (infantile/repressed) necessary; Pcs (day residue) contributor; somatic possible. → Structure
- `[ns_freud_ch7_009]` `[trigger: psychical_intensity]` `[factor_trigger: dream_instigator AND energy]` `[role: 条件分支]` Without Ucs energy, Pcs wishes lack intensity to force through censorship. → Mechanism"""
    normalized_text_zh: str = """"""
    subject: str = "3 The Role of the Unconscious Wish"
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
        l1_anchor="iod_v1.0.0_3_the_role_of_the_unconscious__001_L1",
    )
    version: str = "1.0.0"
