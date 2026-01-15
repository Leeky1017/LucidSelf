"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.568648
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
    semantic_id="acu_v1.0.0_1_syzygy_motif_and_anima_defin_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 1SyzygyMotifAndAnimaDefin(SemanticEntry):
    """
    **Source Text** (¶119-120, Lines 1967-1991):

> [119] One of these archetypes, which is of paramount...
    """
    
    original_text: str = """**Source Text** (¶119-120, Lines 1967-1991):

> [119] One of these archetypes, which is of paramount practical importance for the psychotherapist, I have named the anima. This Latin expression is meant to connote something that should not be confused with any dogmatic Christian idea of the soul or with any of the previous philosophical conceptions of it. If one wishes to form anything like a concrete conception of what this term covers, one would do better to go back to a classical author like Macrobius, or to classical Chinese philosophy, where the anima (p'o or kuei) is regarded as the feminine and chthonic part of the soul...
>
> [120] Unperturbed by the philosophical pros and cons of the age, a scientific psychology must regard those transcendental intuitions that sprang from the human mind in all ages as projections, that is, as psychic contents that were extrapolated in metaphysical space and hypostatized. We encounter the anima historically above all in the divine syzygies, the male-female pairs of deities. These reach down... into the obscurities of primitive mythology, and up... into the philosophical speculations of Gnosticism and of classical Chinese philosophy, where the cosmogonic pair of concepts are designated yang (masculine) and yin (feminine).

**Key Term Analysis**:

| Term | Literal Meaning | Symbolic Significance | Contextual Usage |
|------|----------------|----------------------|------------------|
| Syzygy | Pairing/conjunction | Male-female archetype | Divine pairs |
| P'o/Kuei | Chinese soul-terms | Feminine/chthonic soul | Eastern parallel |
| Yang/Yin | Masculine/feminine | Universal polarity | Chinese cosmology |
| Projection | Casting outward | Inner seen as outer | Psychological mechanism |

**English Paraphrase (Primary Language)**:

Jung introduces the **syzygy motif** as universal archetype:

**Anima defined through cross-cultural parallels**:
- NOT dogmatic Christian soul, NOT philosophical conception
- Chinese parallel: p'o or kuei = "feminine and chthonic part of soul"
- Macrobius: classical Roman soul-concept

**Syzygy as universal**:
- Divine syzygies = male-female deity pairs
- Found in: primitive mythology → Gnosticism → Chinese philosophy
- Yang (masculine) and Yin (feminine) = cosmogonic pair
- "As universal as the existence of man and woman"

**Psychological interpretation**:
- Transcendental intuitions = projections
- "Psychic contents extrapolated in metaphysical space"
- Gods/syzygies are projected psychic contents

**Complete Chinese Interpretation (Secondary Language)**:

荣格引入**配对母题**作为普遍原型：

**通过跨文化平行定义阿尼玛**：
- 不是教条基督教灵魂，不是哲学概念
- 中国平行：魄或鬼 = "灵魂的女性和地下部分"
- Macrobius：古典罗马灵魂概念

**配对作为普遍**：
- 神圣配对 = 男女神明配对
- 发现于：原始神话 → 诺斯替主义 → 中国哲学
- 阳（男性）和阴（女性）= 宇宙生成配对
- "如男女存在一样普遍"

**心理学解释**：
- 超验直觉 = 投射
- "在形而上空间外推的心理内容"
- 神明/配对是投射的心理内容

**Core Points**:
- Anima paralleled in Chinese p'o/kuei (feminine soul)
- Syzygy = divine male-female pairs, universal archetype
- Found across all cultures: primitive to philosophical
- Yang-Yin = cosmogonic expression of syzygy
- Gods are projections of psychic contents
- Syzygy is "as universal as man and woman"

**Narrative Snippets**:
- `[ns_cw9i_II_004]` `[trigger: anima_chinese]` `[factor_trigger: jung_anima]` `[role: 条件分支]` In classical Chinese philosophy, the anima (p'o or kuei) is regarded as the feminine and chthonic part of the soul. → ¶119
- `[ns_cw9i_II_005]` `[trigger: syzygy_universal]` `[factor_trigger: jung_syzygy]` `[role: 主干]` We encounter the anima in the divine syzygies, male-female pairs of deities—yang and yin—as universal as the existence of man and woman. → ¶120
- `[ns_cw9i_II_006]` `[trigger: gods_as_projections]` `[factor_trigger: jung_projection]` `[role: 主干依赖]` Transcendental intuitions are projections—psychic contents extrapolated in metaphysical space and hypostatized. → ¶120"""
    normalized_text_zh: str = """"""
    subject: str = "1 Syzygy Motif and Anima Definition (¶119-120)"
    factor_refs: list = ['engine_id', 'syzygy', 'psych_semantic', 'yang_yin', 'psych_semantic', 'po_kuei', 'psych_semantic', 'source_ref', 'expression_of', 'jung_syzygy', 'manifesting', 'parallel', 'anima', 'corresponding', 'concept_syzygy', 'divine_couple_dream', 'concept_yin_anima', 'feminine_figure']
    
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_1_syzygy_motif_and_anima_defin_001_L1",
    )
    version: str = "1.0.0"
