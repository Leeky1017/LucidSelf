"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.461023
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
    semantic_id="iod_v1.0.0_chapter_vii__the_psychology_of_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class ChapterViiThePsychologyOf(SemanticEntry):
    """
    ### 7.1 The Psychical Apparatus Model

#### Key Term Analysis

| Term | Definition | Significance |
...
    """
    
    original_text: str = """### 7.1 The Psychical Apparatus Model

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Psychical Apparatus | Compound instrument | Spatial model |
| Five Systems | Pcpt/Mnem/Pcs/Ucs/M | Layered psyche |
| Direction | Forward vs regressive | Waking vs dreaming |
| Spatial Orientation | Systems in sequence | Freud's innovation |

**Source Text** (Synthesized):
> We picture the psychical apparatus as a compound instrument, to the components of which we give the name of 'instances' or 'systems.' These systems have a definite spatial orientation: they stand in a relation of precedence to each other.

**English Paraphrase (Primary Language)**:

Freud introduces the **psychical apparatus** model to explain dream formation:

| System | Location | Function |
|--------|----------|----------|
| **Perceptual (Pcpt)** | Input end | Receives sensory stimuli |
| **Memory systems (Mnem)** | Middle | Store traces of perceptions |
| **Preconscious (Pcs)** | Near output | Accessible to consciousness; verbal |
| **Unconscious (Ucs)** | Deep | Inaccessible; wish-repository |
| **Motor (M)** | Output end | Initiates action |

**Direction of excitation**:
- Waking: Pcpt → Mnem → Pcs → M (forward, toward action)
- Dreaming: Ucs → Mnem → Pcpt (regressive, toward hallucination)

**Complete Chinese Interpretation (Secondary Language)**:

弗洛伊德引入**心理装置**模型解释梦的形成：

| 系统 | 位置 | 功能 |
|------|------|------|
| **知觉（Pcpt）** | 输入端 | 接收感官刺激 |
| **记忆系统（Mnem）** | 中间 | 存储知觉痕迹 |
| **前意识（Pcs）** | 接近输出 | 可被意识访问；言语性 |
| **无意识（Ucs）** | 深处 | 不可访问；愿望储存库 |
| **运动（M）** | 输出端 | 启动行动 |

**兴奋方向**：
- 清醒：Pcpt → Mnem → Pcs → M（前进，朝向行动）
- 做梦：Ucs → Mnem → Pcpt（回退，朝向幻觉）

**Core Points**:
- Psyche as spatial apparatus with systems.
- Waking = forward direction; dreaming = regressive.
- Dreams achieve hallucination by reversing direction.
- Unconscious wishes drive the regressive movement.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Psychical Apparatus: Mind as spatial system with five instances (Pcpt/Mnem/Pcs/Ucs/M). Waking=forward direction; dreaming=regressive. Dreams achieve hallucination by reversing excitation direction.
- **中文**: 心理装置:心灵作为五个实例的空间系统(Pcpt/Mnem/Pcs/Ucs/M)。清醒=前进方向;做梦=回退。梦通过逆转兴奔方向实现幻觉。

**Narrative Snippets**:
- `[ns_freud_ch7_001]` `[trigger: psychical_apparatus]` `[factor_trigger: mental_model]` `[role: 主干]` Psychical apparatus: mind as spatial system with five instances (Pcpt/Mnem/Pcs/Ucs/M). → Core
- `[ns_freud_ch7_002]` `[trigger: direction_excitation]` `[factor_trigger: mental_model AND flow]` `[role: 条件分支]` Waking = forward direction (toward action); dreaming = regressive (toward hallucination). → Direction
- `[ns_freud_ch7_003]` `[trigger: ucs_drives]` `[factor_trigger: mental_model AND unconscious]` `[role: 条件分支]` Unconscious wishes drive regressive movement; achieve hallucination by reversing direction. → Mechanism"""
    normalized_text_zh: str = """"""
    subject: str = "Chapter VII: The Psychology of the Dream Activities"
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
        l1_anchor="iod_v1.0.0_chapter_vii__the_psychology_of_001_L1",
    )
    version: str = "1.0.0"
