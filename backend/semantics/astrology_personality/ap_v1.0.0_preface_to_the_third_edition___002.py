"""
Auto-generated semantic module for astrology_personality
Generated at: 2025-12-05T13:31:46.237518
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
    semantic_id="ap_v1.0.0_preface_to_the_third_edition___002",
    book_id="astrology_personality",
    engine_id="astro"
)
class PrefaceToTheThirdEdition(SemanticEntry):
    """
    **Source Text** (Lines 117-134):
> The popularization of astrology had important implications. It me...
    """
    
    original_text: str = """**Source Text** (Lines 117-134):
> The popularization of astrology had important implications. It meant that the magazines, the newspaper columns and even most textbooks had to emphasize the "Sun-sign" approach; that is, a type of astrology based on the birthday of individuals. As a result people began to say "I am a Leo. What is your sign?" This meant that general yet definite psychological characteristics had to be given to the twelve signs of the zodiac and the Sun in a chart had to be considered as the most dominant or basic factor.
>
> There is not, however, only one kind of psychology; and so the psychological interpretation of the signs and the characterization of twelve zodiacal Types of human beings could develop at several levels. Many astrologers were simply following the type of psychology outlined in old textbooks, some stressed a more "social" type of psychology. Quite a few have followed my approach in which I have tried to combine depth-psychology and holistic philosophy (both of which emphasize the integration of the personality) together with some of the most revealing and fecund vistas of occultism and Oriental metaphysics.

**Key Term Analysis**:
- **Sun-sign approach**: `birthday-based astrology` / `"I am a Leo"` / `popularized simplification`
- **Zodiacal Types**: `twelve personality categories` / `general characteristics` / `psychological stereotypes`
- **Integration of personality**: `depth-psychology goal` / `holistic wholeness` / `beyond fragmentation`
- **Oriental metaphysics**: `Eastern philosophy` / `complementary wisdom` / `transcendent dimension`

**English Paraphrase (Primary Language)**:
Rudhyar critiques the consequences of astrology's popularization: the "Sun-sign" approach reduces the complex birth chart to a single factor—the Sun's zodiacal position at birth. This simplification, while making astrology accessible ("What's your sign?"), fundamentally distorts its purpose by creating twelve rigid personality types. However, Rudhyar notes that even within psychological astrology, multiple levels exist. His own approach integrates depth-psychology's emphasis on personality integration, holistic philosophy's insistence on wholeness, and insights from occultism and Eastern metaphysics. This synthesis transcends both the superficiality of Sun-sign astrology and the limitations of purely Western psychological frameworks.

**Complete Chinese Interpretation (Secondary Language)**:
Rudhyar批评了占星学普及的后果："太阳星座"方法将复杂的出生星盘简化为单一因素——出生时太阳的黄道位置。这种简化虽然使占星学变得可及（"你是什么星座？"），但从根本上扭曲了其目的，创造了十二种僵化的人格类型。然而，Rudhyar指出，即使在心理占星学内部也存在多个层次。他自己的方法整合了深度心理学对人格整合的强调、整体论哲学对完整性的坚持，以及神秘主义和东方形而上学的洞见。这一综合超越了太阳星座占星术的肤浅性和纯西方心理学框架的局限性。

**Core Points**:
- Popularization led to Sun-sign oversimplification
- "I am a Leo" mentality reduces chart to one factor
- Multiple psychological approaches exist within astrology
- Rudhyar's synthesis: depth-psychology + holism + occultism + Oriental metaphysics
- Goal: integration of personality, not stereotyped types
- Sun-sign approach distorts astrology's deeper purpose

**Detailed Explanation**:
The "Sun-sign" phenomenon represents both astrology's greatest popular success and its intellectual degradation. By reducing the complex symbolic language of the birth chart to a single factor, newspaper horoscopes made astrology accessible but meaningless. Rudhyar's critique is not against popularization per se but against the epistemological reduction it entails. His alternative preserves complexity while remaining psychologically meaningful—the birth chart as a mandala of the whole person, not a simplistic label.

**Narrative Snippets**:
- `[ns_aop_005]` `[trigger: sun_sign_critique]` `[factor_trigger: astro_sun_sign AND zodiac AND astro_sun_sign_limit]` `[role: 主干]` The "Sun-sign" approach reduces complex birth charts to a single factor—"I am a Leo. What is your sign?" → Source Text L117-124
- `[ns_aop_006]` `[trigger: multi_level_psychology]` `[factor_trigger: astro_old_textbook AND astro_depth_approach AND astro_psych_levels AND astro_psych]` `[role: 主干依赖]` Psychological interpretation can develop at several levels—old textbooks, social psychology, or depth-psychology with holism. → Source Text L126-134
- `[ns_aop_007]` `[trigger: rudhyar_synthesis]` `[factor_trigger: astro_western AND phil_oriental AND astro_east_west]` `[role: 总结]` Rudhyar combines depth-psychology, holistic philosophy, occultism, and Oriental metaphysics into integrated approach. → Source Text L131-134

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: N/A: Single authoritative source. Rudhyar's critique of Sun-sign astrology remains consistent throughout his writings.
- **中文**: 无版本差异：单一权威来源。Rudhyar对太阳星座占星术的批评在其著作中保持一致。。"""
    normalized_text_zh: str = """"""
    subject: str = "Preface to the Third Edition: Sun-Sign Astrology and Its Limitations"
    factor_refs: list = ['astro_sun_sign', 'astro_zodiacal_types', 'psych_personality_integration', 'phil_oriental_metaphysics']
    
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
        l1_anchor="ap_v1.0.0_preface_to_the_third_edition___002_L1",
    )
    version: str = "1.0.0"
