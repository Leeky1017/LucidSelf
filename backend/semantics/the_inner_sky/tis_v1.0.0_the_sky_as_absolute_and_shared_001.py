"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134381
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
    semantic_id="tis_v1.0.0_the_sky_as_absolute_and_shared_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class TheSkyAsAbsoluteAndShared(SemanticEntry):
    """
    **Source Text**:
The sky. That is astrology’s prime symbol. The sky is the bedrock from which the el...
    """
    
    original_text: str = """**Source Text**:
The sky. That is astrology’s prime symbol. The sky is the bedrock from which the elaborate language of the birthchart arises.
But what does it mean? To the astronomer, the question doesn’t make sense. He or she can say what the sky is. But what it means—that is something for poets and philosophers to dwell on, not astronomers. Burn away all the name calling, and the difference between astrologers and astronomers boils down to this: astronomers seek to know the form of the heavens, while astrologers pursue their meaning. Astrology is the poetry of astronomy. It is not so much a study of structure as of significance. Not what the sky is. But what it says to us.
...
Astrology’s prime symbol, the great sphere of space that surrounds us, is a symbol of that awe and reverence. We might choose to call it a symbol of God. It represents infinity and perfection, timelessness and universality. Americans, Russians, Europeans, Africans—we all stand beneath the same sky. Like breathing, like sex, like death, it binds us together. It reminds us of our common humanity.

**Key Term Analysis**:
- `prime symbol`: the foundational image from which all other astrological symbols are derived.
- `poetry of astronomy`: astrology as interpretation of meaning rather than measurement of form.
- `infinity and universality`: the sky as a symbol of boundlessness, timelessness, and shared human condition.
- `common humanity under one sky`: the idea that the same sky unites all cultures and individuals.

**English Paraphrase (Primary Language)**:
Forrest begins his discussion of the prime symbol by pointing to something utterly ordinary and utterly overwhelming: the sky. Astrologically, the sky is the bedrock image from which the entire language of the birthchart arises. Astronomers study what the sky is—its structures, motions, and physical properties. Astrologers, by contrast, are concerned with what the sky means. In his memorable phrase, astrology is "the poetry of astronomy": not a rival science, but a discipline focused on significance rather than structure.

The great sphere of space surrounding us evokes awe and reverence in almost everyone, regardless of culture or era. Forrest treats that feeling as central. The sky can be taken as a symbol of God, or more broadly as an image of infinity, perfection, and timelessness. Crucially, it is also universal. People in every country stand beneath the same sky. Like breathing, sex, and death, it is a shared experience that binds us together and reminds us of our common humanity. This sense of a vast, shared background is what the prime symbol contributes to astrology: a reference point beyond any particular culture or personality.

**Complete Chinese Interpretation (Secondary Language)**:
Forrest 讨论「原始象征」时，先把读者的注意力拉回到最日常、也最震撼的对象：天空。在占星里，天空是整套语言的基岩，所有命盘中的复杂结构，最终都可以追溯到它。天文学关心的是「天空是什么」——其物理结构、运行轨道与可测量的性质；占星师则转向另一个维度：天空「意味着什么」。他用一句话总结两者的差别：占星是天文学的诗，是在同一片天之上追问意义，而不是重复测量结构。

那一整片包裹着我们的空间球体，会在几乎所有人心中唤起敬畏与庄严感，不论文化、不论时代。Forrest 把这种情绪视为占星的出发点。天空可以被看作「上帝的象征」，也可以更世俗地理解为「无限、完满、超越时间与个人的普遍性」的意象。更重要的是，它是共享的——美国人、俄罗斯人、欧洲人、非洲人，都站在同一片天空之下。就像呼吸、性与死亡，它把人类串联在一起，提醒我们自己首先是「共同的人」。这种「巨大而共同的背景」正是原始象征为占星提供的底色：一个超越任何具体文化、理论与人格的参照面。

**Core Points**:
- The sky is astrology’s prime symbol and the source of all later symbolic elaboration.
- Astrology is described as the "poetry of astronomy," focusing on meaning rather than structure.
- The sky symbolizes infinity, perfection, timelessness, and universality.
- A shared sky underpins the idea of common humanity across cultures.

**Detailed Explanation**:
This framing establishes astrology on a foundation that is both experiential and trans‑cultural. By rooting the prime symbol in the sky itself—something any person can see—Forrest avoids basing astrology on esoteric doctrines. The emotional response of awe becomes a legitimate starting point for symbolic interpretation. Calling astrology "poetry" also lowers the stakes in the science‑versus‑pseudoscience debate: the point is not to compete with astronomy, but to complement it at the level of meaning.

The universality of the sky is especially important in a multi‑cultural context. If everyone stands under the same sky, then astrological language has a natural claim to address human experience across boundaries, even though its specific expressions are shaped by culture. Content calibration must therefore respect both the universal and the particular: we must preserve the sky as a shared prime symbol while allowing for different cultural metaphors that arise from it.

**Narrative Snippets**:
- `[ns_innersky_068]` `[trigger: prime_symbol]` `[factor_trigger: astro_sky AND astro_symbol]` `[role: 主干]` The sky is astrology's prime symbol—the bedrock from which the entire language of the birthchart arises. → Source Text
- `[ns_innersky_069]` `[trigger: poetry_of_astronomy]` `[factor_trigger: astro_philosophy AND astro_meaning]` `[role: 主干依赖]` Astrology is the poetry of astronomy—it pursues meaning rather than structure. → Source Text
- `[ns_innersky_070]` `[trigger: universal_sky]` `[factor_trigger: astro_sky AND astro_universal]` `[role: 条件分支]` We all stand beneath the same sky—like breathing, like death, it binds us together and reminds us of our common humanity. → Source Text
- `[ns_innersky_071]` `[trigger: meaning_vs_form]` `[factor_trigger: astro_philosophy AND astro_distinction]` `[role: 总结]` Astronomers seek to know the form of the heavens; astrologers pursue their meaning. → Source Text
- `[ns_innersky_072]` `[trigger: infinity_symbol]` `[factor_trigger: astro_sky AND astro_archetype]` `[role: 主干]` The sky represents infinity and perfection, timelessness and universality. → Source Text
- `[ns_innersky_073]` `[trigger: awe_response]` `[factor_trigger: astro_psychology AND astro_emotion]` `[role: 主干依赖]` The emotional response of awe is a legitimate starting point for symbolic interpretation. → Source Text
- `[ns_innersky_074]` `[trigger: common_humanity]` `[factor_trigger: astro_sky AND astro_humanity]` `[role: 条件分支]` A shared sky underpins the idea of common humanity across cultures. → Source Text
- `[ns_innersky_075]` `[trigger: cultural_metaphors]` `[factor_trigger: astro_symbol AND astro_culture]` `[role: 总结]` Different cultural metaphors arise from the shared prime symbol of the sky. → Source Text
- `[ns_innersky_076]` `[trigger: universal_particular]` `[factor_trigger: astro_calibration AND astro_balance]` `[role: 主干]` Content calibration must respect both the universal and the particular. → Source Text
- `[ns_innersky_077]` `[trigger: sky_as_reference]` `[factor_trigger: astro_sky AND astro_reference]` `[role: 主干依赖]` The sky serves as a reference point beyond any particular culture or personality. → Source Text"""
    normalized_text_zh: str = """"""
    subject: str = "The Sky as Absolute and Shared Source of Awe"
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
        book_id="the_inner_sky",
        chapter="",
        l1_anchor="tis_v1.0.0_the_sky_as_absolute_and_shared_001_L1",
    )
    version: str = "1.0.0"
