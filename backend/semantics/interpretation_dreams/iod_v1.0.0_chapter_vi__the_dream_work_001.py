"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460997
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
    semantic_id="iod_v1.0.0_chapter_vi__the_dream_work_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class ChapterViTheDreamWork(SemanticEntry):
    """
    ### 6.1 Dream-Work as System of Mechanisms

#### Key Term Analysis

| Term | Definition | Significan...
    """
    
    original_text: str = """### 6.1 Dream-Work as System of Mechanisms

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Dream-Work | Traumarbeit | Transformation process |
| Four Mechanisms | Condensation/displacement/symbol/revision | Sequential stages |
| Transforms Not Thinks | Key principle | Not rational thought |
| Factory Model | Raw material processing | Mechanical metaphor |

**Source Text** (Synthesized):
> The dream-work is not simply careless, arbitrary thinking; it is a completely different psychical function, which can be sharply distinguished from the thinking we do when awake. The dream-work does not think, calculate, or judge; it simply transforms.

**English Paraphrase (Primary Language)**:

**Dream-work** (Traumarbeit) = the **transformation process** converting latent content into manifest dream.

| Mechanism | Function | Direction |
|-----------|----------|-----------|
| **Condensation** | Combines multiple elements into one | Many → One |
| **Displacement** | Shifts emphasis from important to trivial | Center → Periphery |
| **Symbolization** | Represents abstract ideas with concrete images | Abstract → Concrete |
| **Secondary revision** | Rationalizes incoherent material | Chaos → Narrative |

**Key principle**: Dream-work does NOT think; it **transforms**. The latent thoughts are processed like raw material through a factory.

**Mechanism interrelations**:
```
Latent content (wishes + day residues)
    ↓ Condensation (compress)
    ↓ Displacement (shift emphasis)
    ↓ Symbolization (encode)
    ↓ Secondary revision (narrativize)
Manifest content (remembered dream)
```

**Complete Chinese Interpretation (Secondary Language)**:

**梦的工作**（Traumarbeit）= 将隐梦内容转化为显梦的**转化过程**。

| 机制 | 功能 | 方向 |
|------|------|------|
| **凝缩** | 将多个元素合并为一 | 多 → 一 |
| **移置** | 将重点从重要转移到琐碎 | 中心 → 边缘 |
| **象征化** | 用具体意象表征抽象观念 | 抽象 → 具体 |
| **次级修饰** | 使不连贯材料合理化 | 混乱 → 叙事 |

**关键原则**：梦的工作不思考；它**转化**。隐梦思想像原料一样通过工厂加工。

**Core Points**:
- Dream-work = transformation, not thought.
- Four mechanisms work in sequence.
- Censorship drives the distortion.
- Secondary revision adds surface coherence.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Dream-Work: Transformation process (not thought). Four mechanisms: condensation, displacement, symbolization, secondary revision. Censorship drives distortion. Latent→manifest through sequential processing.
- **中文**: 梦的工作:转化过程(非思想)。四种机制:凝缩、移置、象征化、次级修饰。审查驱动扭曲。潜梦→显梦通过顺序加工。

**Narrative Snippets**:
- `[ns_freud_ch6_001]` `[trigger: dream_work_system]` `[factor_trigger: traumarbeit]` `[role: 主干]` Dream-work (Traumarbeit): transformation process, not thought; does not think, only transforms. → Core
- `[ns_freud_ch6_002]` `[trigger: four_mechanisms]` `[factor_trigger: traumarbeit AND process]` `[role: 条件分支]` Four mechanisms: condensation (many→one), displacement (center→periphery), symbolization, secondary revision. → Structure
- `[ns_freud_ch6_003]` `[trigger: factory_model]` `[factor_trigger: traumarbeit AND metaphor]` `[role: 条件分支]` Latent content processed like raw material through factory; sequential transformation stages. → Model"""
    normalized_text_zh: str = """"""
    subject: str = "Chapter VI: The Dream-Work"
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
        l1_anchor="iod_v1.0.0_chapter_vi__the_dream_work_001_L1",
    )
    version: str = "1.0.0"
