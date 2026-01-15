"""
Auto-generated semantic module for collected_works
Generated at: 2025-12-05T13:30:20.574975
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
    semantic_id="cw_v1.0.0_source_text_011",
    book_id="collected_works",
    engine_id="psych"
)
class SourceText(SemanticEntry):
    """
    "The alchemical opus proceeds through distinct stages: nigredo (blackening), albedo (whitening), and...
    """
    
    original_text: str = """"The alchemical opus proceeds through distinct stages: nigredo (blackening), albedo (whitening), and rubedo (reddening). These correspond psychologically to the stages of individuation—dissolution of the old self, purification, and final integration."

#### English Paraphrase (Primary Language)

**Opus** (The Work) = Alchemical transformation through **three/four stages**:

| Stage | Color | Process | Psychological Meaning |
|-------|-------|---------|----------------------|
| **Nigredo** | Black | Death, putrefaction, dissolution | Depression, ego-death, confronting shadow |
| **Albedo** | White | Purification, washing, lunar light | Purification, differentiation, anima/animus work |
| **Citrinitas** | Yellow | Dawn, transition (sometimes omitted) | Awakening, preparation |
| **Rubedo** | Red | Union, sunrise, completion | Integration, Self-realization, coniunctio |

**Psychological parallels**:
- **Nigredo**: Dark night of soul, breakdown of old identity, necessary depression
- **Albedo**: Moonlit consciousness, reflective clarity, feminine principle activated
- **Rubedo**: Solar achievement, full consciousness, masculine-feminine united

**Key insight**: Transformation **requires** nigredo—no rebirth without death of old form.

#### Complete Chinese Interpretation (Secondary Language)

**作业**（炼金工作）= 通过**三/四阶段**的炼金转化：

| 阶段 | 颜色 | 过程 | 心理含义 |
|------|------|------|----------|
| **黑化** | 黑 | 死亡、腐化、分解 | 抑郁、自我死亡、面对阴影 |
| **白化** | 白 | 净化、洗涤、月光 | 净化、分化、阿尼玛/阿尼姆斯工作 |
| **黄化** | 黄 | 黎明、过渡（有时省略） | 觉醒、准备 |
| **赤化** | 红 | 结合、日出、完成 | 整合、本我实现、神圣婚姻 |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_jung_11 | concept | jung_11 | system | Theoretical | When theoretical framework connects concept to system | connecting | Source #jung |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_jung_11 | "Source text" | jung_11 | Concept -> application | Theory | High | Yes | rule_jung_11 |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_jung_11 | Core concept | | relevant | | relevant | System |
<!-- L2.5_END -->

**心理对应**：
- **黑化**：灵魂暗夜、旧身份崩解、必要的抑郁
- **白化**：月光下的意识、反思的清明、阴性原则激活
- **赤化**：太阳成就、完全意识、男女性合一

**关键洞见**：转化**必须**经历黑化——没有旧形式的死亡就没有重生。

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Nigredo | Blackening/death | Initial dissolution |
| Albedo | Whitening/purification | Lunar consciousness |
| Rubedo | Reddening/union | Solar completion |
| Opus | The Work | Transformation process |

#### Core Points

- Three main stages: Nigredo → Albedo → Rubedo
- Nigredo (death) is necessary—no shortcut to transformation
- Psychological parallels to individuation stages
- Colors symbolize psychic states in transformation

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Opus: Alchemical transformation stages. Nigredo (death/dissolution) → Albedo (purification/lunar) → Rubedo (union/solar). Nigredo cannot be skipped. Colors map to psychic states.
- **中文**: 作业:炼金转化阶段。黑化(死亡/分解)→白化(净化/月光)→赤化(合一/太阳)。黑化不可跳过。颜色映射心理状态。

**Narrative Snippets**:
- `[ns_jung_041]` `[trigger: opus_stages]` `[factor_trigger: jung_opus AND jung_transformation AND jung_opus_stages]` `[role: 主干]` The alchemical opus proceeds through distinct stages: nigredo (blackening), albedo (whitening), and rubedo (reddening). → Core
- `[ns_jung_042]` `[trigger: nigredo_necessity]` `[factor_trigger: jung_nigredo AND jung_death]` `[role: 条件分支]` Transformation requires nigredo—no rebirth without death of old form; dissolution of old self precedes integration. → Necessity
- `[ns_jung_043]` `[trigger: rubedo_completion]` `[factor_trigger: jung_rubedo AND jung_individuation AND jung_albedo]` `[role: 条件分支]` These stages correspond psychologically to individuation—nigredo (shadow work), albedo (purification), rubedo (final integration). → Psychology"""
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
        book_id="collected_works",
        chapter="",
        l1_anchor="cw_v1.0.0_source_text_011_L1",
    )
    version: str = "1.0.0"
