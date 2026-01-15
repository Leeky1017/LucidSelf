"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.482474
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
    semantic_id="iod_v1.0.0_source_text_013",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class SourceText(SemanticEntry):
    """
    "Anxiety dreams appear to contradict my theory of wish-fulfillment. But the anxiety belongs not to t...
    """
    
    original_text: str = """"Anxiety dreams appear to contradict my theory of wish-fulfillment. But the anxiety belongs not to the dream content but to the censorship. The wish being fulfilled is a repressed, forbidden one; the anxiety signals that the censorship is alarmed by how close the wish came to consciousness."

#### English Paraphrase (Primary Language)

**Anxiety Dreams** = Dreams producing **fear, dread, or terror** that seem to contradict wish-fulfillment theory.

**Resolution of paradox**:
- Anxiety **not from dream content** itself
- Anxiety from **censorship's alarm** at forbidden wish approaching consciousness
- The wish **is still being fulfilled**—but it's a repressed, unacceptable one
- Censorship fails partially → anxiety signals its distress

**Types of anxiety dreams**:
1. **Punishment dreams**: Superego's wish to punish ego
2. **Traumatic dreams**: Exception—repetition compulsion, not wish
3. **Failed disguise**: Latent content too thinly veiled

**Key insight**: Anxiety = **signal of repression struggling**. The more forbidden the wish, the more anxiety when it approaches expression.

#### Complete Chinese Interpretation (Secondary Language)

**焦虑梦** = 产生**恐惧、畏惧或惊恐**的梦，似乎与愿望满足理论矛盾。

**悖论的解决**：
- 焦虑**不是来自梦内容**本身
- 焦虑来自**检查机制的警报**——被禁止的愿望接近意识
- 愿望**仍在被满足**——但它是被压抑的、不可接受的
- 检查部分失效 → 焦虑信号其苦恼

**焦虑梦类型**：
1. **惩罚梦**：超我惩罚自我的愿望
2. **创伤梦**：例外——重复强迫，非愿望
3. **伪装失败**：潜隐内容伪装太薄

**关键洞见**：焦虑 = **压抑挣扎的信号**。愿望越禁忌，接近表达时焦虑越大。

#### Core Points

- Anxiety dreams do not contradict wish-fulfillment
- Anxiety signals censorship's alarm, not dream content
- Forbidden wish is still being fulfilled
- Exception: traumatic dreams (repetition compulsion)

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Anxiety Dreams | Fear-producing dreams | Paradox resolved |
| Censorship Alarm | Anxiety signal | Failed disguise |
| Punishment Dreams | Superego wish | Moral masochism |
| Traumatic Dreams | Repetition compulsion | Exception to theory |

#### Textual Criticism & Variant Analysis (Bilingual)
- **English**: Anxiety dreams: do not contradict wish-fulfillment. Anxiety = censorship's alarm at forbidden wish. Punishment dreams fulfill superego wish. Traumatic dreams = exception (repetition compulsion).
- **中文**: 焦虑梦:不与愿望满足矛盾。焦虑=审查对禁忌愿望的警报。惩罚梦满足超我愿望。创伤梦=例外(重复强迫)。

#### L2 Semantic Extraction

- **Theme**: Anxiety in dreams as signal of censorship struggling against forbidden wishes.
- **Natural Attributes**:
  - Symbolism: Fear, alarm, punishment, trauma.
  - Characteristics: Paradoxical, signaling, defensive.
  - Elements: Censorship, repressed wish, superego.
- **Functional Symbolism**:
  - Anxiety = censorship's distress signal.
  - Shows wish-fulfillment even in unpleasant dreams.
  - Reveals dynamic conflict between wish and defense.
- **Conditional Structure**:
  - **Necessary Conditions**: Forbidden wish + partial censorship failure.
  - **Enhancing Conditions**: Intense repression, strong superego.
  - **Nullifying Conditions**: Traumatic dreams operate differently (repetition compulsion).
- **Multi-layered Interpretation**:
  - Literal Layer: Nightmares, fear-inducing dreams.
  - Psychological Layer: Censorship failing, wish approaching.
  - Dynamic Layer: Conflict between id wish and superego prohibition.
  - Clinical Layer: Anxiety dreams often mark therapy progress.

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition |
|--------------|--------------|-------------------|-------------------|
| Anxiety dream | 焦虑梦 | Dream producing fear due to censorship's alarm | 因检查机制警报而产生恐惧的梦 |
| Punishment dream | 惩罚梦 | Dream fulfilling superego's wish to punish ego | 满足超我惩罚自我愿望的梦 |
| Traumatic dream | 创伤梦 | Dream repeating traumatic experience (exception to wish-fulfillment) | 重复创伤经验的梦（愿望满足的例外） |
| Censorship alarm | 检查警报 | Anxiety signal when forbidden wish approaches consciousness | 禁忌愿望接近意识时的焦虑信号 |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|-------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Pattern | Anxiety dream | freud_anxiety_dream | new_candidate | Dream Category | Paradoxical wish-fulfillment | dream_semantic | Censorship signal |
| Process | Censorship alarm | freud_censorship_alarm | new_candidate | Defense Signal | Anxiety = failed disguise | dream_semantic | Dynamic indicator |
| Pattern | Punishment dream | freud_punishment_dream | new_candidate | Dream Subtype | Superego wish | dream_semantic | Moral masochism |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_freud_anxiety | dream_mechanism | anxiety_dream | censorship | Psychodynamic | When forbidden wish anxiety dream alarms censorship | alarming | Freud #Dreams |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_freud_anxiety | "Anxiety belongs not to dream content but to censorship" | anxiety_dream | Alarm -> signal | Anxiety = censorship alarm | High | Yes | rule_freud_anxiety |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_freud_anxiety | Anxiety as censorship signal | | | nightmare_analysis | defense_mechanism | Freud |
<!-- L2.5_END -->

---

## Completion Summary

**Status**: ✅ v2.1 COMPLETE - The Interpretation of Dreams Core Mechanisms Upgraded (P0 + P2)

**Achievements**:
- 13/15 core concepts fully upgraded to v2.1 format (11 P0 + 2 P2)
- Complete L1+L2+Factor Layer for all concepts
- Bilingual English-Chinese term glossary
- 100% template compliance

**Coverage**:
- Part 1: Foundational Theory (3 concepts) - Paradigm, Manifest/Latent, Wish-Fulfillment
- Part 2: Dream-Work Mechanisms (5 concepts) - Condensation, Displacement, Symbolization, Free Association, Censorship
- Part 3: Additional Concepts (3 concepts) - Day Residues, Regression, Primary/Secondary Process
- Part 4: Dream Types P2 (2 concepts) - Typical Dreams, Anxiety Dreams

**Note**: Concepts 14-15 (Dream Sources, Theoretical Synthesis) can be added in future expansion if needed. Current 13 concepts provide comprehensive foundation of Freud's core dream theory.

**Quality Standards Met**:
- ✅ Complete bilingual structure (Primary English, Secondary Chinese)"""
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
        l1_anchor="iod_v1.0.0_source_text_013_L1",
    )
    version: str = "1.0.0"
