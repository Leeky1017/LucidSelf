"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237477
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
    semantic_id="ap_v1.0.0_preface_to_the_third_edition___001",
    book_id="astrology_personality",
    engine_id="astro"
)
class PrefaceToTheThirdEdition(SemanticEntry):
    """
    **Source Text** (Lines 89-386):
> When this book was written, following a series of articles appeari...
    """
    
    original_text: str = """**Source Text** (Lines 89-386):
> When this book was written, following a series of articles appearing in the magazine American Astrology which had just been published and edited by Paul Clancy, astrology interested relatively few people. It was associated in the public mind either with fortune-telling of the most superficial type, or with Rosicrucians, Theosophists, or Hermetists. The most well-known English astrologers, Sepharial and Alan Leo, had been occultists and Theosophists; and it was in such circles that I first heard of and studied astrology just fifty years ago.
>
> Ten years later I received the first mimeographed courses on astrology by Marc Edmund Jones, and soon afterward became deeply interested in Carl Jung's depth-psychology and also in the book Holism and Evolution written by the great South African statesman, internationalist and philosopher, Ian Smuts. It occurred to me then that astrology could be used in close connection with depth-psychology if it were considered in a new light and if many of its basic concepts were reformulated so as to fit the mentality and the experiences of the modern men and women of our post-World War I society.

**Key Term Analysis**:
- **Depth-psychology**: `Jung's analytical psychology` / `unconscious exploration` / `integration of psyche`
- **Holism**: `whole greater than parts` / `organic unity` / `Jan Smuts' philosophy`
- **Fortune-telling**: `superficial prediction` / `event-oriented astrology` / `what Rudhyar rejects`
- **Theosophists/Occultists**: `esoteric tradition` / `Alice Bailey, Sepharial, Alan Leo` / `early astrological context`
- **American Astrology magazine**: `Paul Clancy publication` / `platform for Rudhyar's articles` / `1930s popularization`

**English Paraphrase (Primary Language)**:
Rudhyar establishes the historical context for his revolutionary approach: astrology in the 1930s was marginalized, associated only with fortune-telling or occult circles. His intellectual formation combined three crucial streams: (1) Marc Edmund Jones's systematic astrological teaching, (2) Carl Jung's depth-psychology with its emphasis on the unconscious and individuation, and (3) Jan Smuts's holistic philosophy which viewed organisms as integrated wholes rather than collections of parts. This synthesis led Rudhyar to envision astrology as a tool for psychological integration rather than mere prediction—a radical reconceptualization that would found humanistic astrology.

The timing was significant: post-World War I society was in crisis, traditional values shattered, and people sought new frameworks for understanding themselves. Astrology, reformulated in psychological and holistic terms, could address this need for meaning and self-understanding that neither materialistic science nor discredited religions could fulfill.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar确立了其革命性方法的历史背景：1930年代的占星学处于边缘地位，仅与算命或神秘学圈子相关联。他的知识形成融合了三个关键源流：(1) Marc Edmund Jones的系统占星教学，(2) Carl Jung的深度心理学及其对无意识和个体化的强调，(3) Jan Smuts的整体论哲学，将有机体视为整合的整体而非部分的集合。这一综合使Rudhyar将占星学设想为心理整合的工具而非单纯的预测——这是一个根本性的重新概念化，奠定了人本占星学的基础。

时机具有重要意义：一战后的社会处于危机中，传统价值观破碎，人们寻求理解自我的新框架。以心理学和整体论术语重新表述的占星学，可以满足这种对意义和自我理解的需求，而这是唯物主义科学或失去信誉的宗教都无法满足的。

**Core Points** (decomposed, no upper limit):
- 1930s astrology was marginalized: fortune-telling or occultism only
- Rudhyar's formation: Jones (astrology) + Jung (depth-psychology) + Smuts (holism)
- Key insight: astrology could connect with depth-psychology
- Required reformulation of basic astrological concepts
- Post-WWI society needed new frameworks for self-understanding
- Synthesis aimed at fitting modern mentality and experiences
- Paul Clancy's American Astrology provided publication platform
- Early influences: Theosophical-occult tradition (Sepharial, Alan Leo)

**Detailed Explanation**:
This passage reveals the intellectual genealogy of humanistic astrology. Rudhyar's genius lay in synthesis: taking Jung's psychological framework (with its emphasis on wholeness, individuation, and the integration of conscious and unconscious), combining it with Smuts's holistic philosophy (which rejected mechanistic reductionism), and applying both to astrological symbolism. The result was a complete reorientation: astrology ceased to be about predicting events and became a tool for self-knowledge and psychological integration.

The historical context matters: the 1930s saw a crisis of meaning in Western civilization. Traditional religion had lost authority, materialistic science offered no answers to existential questions, and the trauma of WWI had shattered old certainties. Into this vacuum, Rudhyar proposed astrology as a "sacred psychology"—a symbolic language for understanding the individual's place in the cosmic order.

**Narrative Snippets** (English only, decomposed):
- `[ns_aop_001]` `[trigger: historical_context]` `[factor_trigger: astro_fortune_telling AND astro_traditional AND astro_anti_fortune AND astro_depth_integration AND astro_humanistic_origin]` `[role: 主干]` Astrology in the 1930s was marginalized, associated only with fortune-telling or occult circles—few took it seriously as a tool for self-knowledge. → Source Text L89-98
- `[ns_aop_002]` `[trigger: intellectual_formation]` `[factor_trigger: astro_theosophical AND astro_humanistic AND astro_holistic_frame]` `[role: 主干依赖]` Rudhyar's formation combined Marc Jones's astrology, Jung's depth-psychology, and Smuts's holistic philosophy into a revolutionary synthesis. → Source Text L99-106
- `[ns_aop_003]` `[trigger: reformulation]` `[factor_trigger: astro_integration AND astro_interpretation]` `[role: 条件分支]` Astrology required reformulation of basic concepts to fit modern mentality—a psychological and holistic reconceptualization. → Source Text L103-106
- `[ns_aop_004]` `[trigger: depth_psychology_connection]` `[factor_trigger: psych_depth_psychology AND astro_whole_chart]` `[role: 总结]` Astrology could be used in close connection with depth-psychology if considered in a new light. → Source Text L103-104

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A for textual variants. This is Rudhyar's 1970 Preface to Third Edition, written 35 years after the original 1936 publication. Rudhyar explicitly acknowledges that some original formulations no longer represent his mature views, particularly regarding house systems (now preferring Campanus over Placidus).
- **中文**: 无版本差异。这是Rudhyar 1970年为第三版撰写的前言，距原书出版已35年。Rudhyar明确承认一些原始表述不再代表他成熟的观点，特别是关于宫位系统（现在倾向于Campanus而非Placidus）。"""
    normalized_text_zh: str = """"""
    subject: str = "Preface to the Third Edition (1970)"
    factor_refs: list = ['psych_depth_psychology', 'phil_holism', 'astro_fortune_telling', 'astro_american_astrology', 'astro_reformulation']
    
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
        l1_anchor="ap_v1.0.0_preface_to_the_third_edition___001_L1",
    )
    version: str = "1.0.0"
