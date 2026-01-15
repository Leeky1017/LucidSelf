"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134309
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
    semantic_id="tis_v1.0.0_interpretive_grammar___planet__001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class InterpretiveGrammarPlanet(SemanticEntry):
    """
    **Source Text**:
To understand how a planet operates we must see it in the context of a sign and a h...
    """
    
    original_text: str = """**Source Text**:
To understand how a planet operates we must see it in the context of a sign and a house. An aggressive planet might lie in a sign that refers to the process of developing courage. That is a powerful combination and it produces a distinctly assertive personality. But how does that assertiveness become visible? Where do we see it?
To answer that, we look at the house. That is where the sign-planet dynamic is released. Perhaps that assertiveness is most clearly expressed within the career. Maybe we see it in marriage and friendship. Or perhaps that assertiveness is not outwardly visible at all. Maybe it is blazing away in one of the hidden departments of life. That question can only be answered by a house.
Unlocking the interactions of these three kinds of symbols—signs, planets, and houses—is the key to unlocking the secrets of the individual birthchart. To put it all briefly, the three systems of symbols answer the questions what, how and why, and where. Always look first to the planet, which is the what. It lets us know which part of the mind we are considering. Then use the sign to determine exactly what that planet wants and what methods it might best use to achieve those goals—the why and the how. Finally, look at the house. It answers the where, telling us in precisely which department of life the battle is taking place.

**Key Term Analysis**:
- `what / how and why / where`: the three interpretive questions mapped respectively to planet, sign, and house.
- `sign–planet dynamic`: the combined pattern of a planetary function operating through a sign’s growth process.
- `release in the house`: the idea that the combined energy becomes visible in a particular life arena.
- `interpretive grammar`: the ordered procedure of looking first to planet, then sign, then house.

**English Paraphrase (Primary Language)**:
Here Forrest turns the triad into a concrete interpretive grammar. To understand any placement, we must always see the planet in the context of both sign and house. The planet tells us what part of the mind is active—what function is involved. The sign tells us how and why that function behaves as it does: what it wants and which methods it prefers. The house tells us where this combined pattern becomes visible in life: in which department of experience the "battle" is taking place.

He illustrates this with an "aggressive planet" placed in a sign of courage, producing an assertive personality. On its own, this describes inner potential, but not its arena. The house shows whether that assertiveness plays out primarily in career, in intimate relationships, or in more hidden zones of life. Without the house, we only know that a certain kind of energy exists; with the house, we see where others are likely to notice it and where the person must consciously work.

**Complete Chinese Interpretation (Secondary Language)**:
在这里，Forrest 把前面的三元结构变成一套可以实际操作的「解读语法」。要理解任何一个配置，我们必须同时考虑行星、星座与宫位。行星先告诉我们「是什么」——也就是哪一部分心智机能在起作用。星座再告诉我们「为什么、如何」：这颗行星在这里究竟想要什么、倾向用什么方式去追求。最后，宫位回答「在哪里」：这种行星×星座的组合，会在生命中的哪一个领域被看见、被体验到。

他用一个「富有攻击性的行星」举例：如果这颗行星落在一个与勇气相关的星座，会促成一种十分有冲劲的性格。但光知道「有冲劲」，还不知道这股力量要往哪里去——是主要体现在事业与公众角色上，还是在亲密关系中显形，抑或更多地燃烧在隐秘领域乃至潜意识之中？这一切只有宫位能回答。没有宫位，我们只知道存在某种能量；有了宫位，我们才知道这股能量会在哪些场景里被他人感知、又在哪些地方需要当事人有意识地工作。

**Core Points**:
- Planet, sign, and house correspond to the questions what, how/why, and where.
- Interpretation should follow the order: planet first, then sign, then house.
- The house describes the life arena where the sign–planet dynamic is released and observed.
- This grammar turns the symbolic triad into a repeatable interpretive method.

**Detailed Explanation**:
By framing the triad as a grammar of what–how/why–where, Forrest gives students and practitioners a simple but powerful algorithm for reading charts. Starting with the planet prevents interpretations from drifting into vague typology; we are always anchored in a specific psychological function. Moving to the sign then adds motivational color and style. Ending with the house ties everything back to concrete life situations where the pattern will matter.

The concept of "release" in the house is especially useful for counseling. Clients often feel confused when they recognize an inner trait but cannot see where it belongs. Showing them the relevant house clarifies both opportunities and risks in that life area. For engine design, this grammar implies that any interpretive module should be structured around the same sequence: identify function (planet), characterize process (sign), then assign domain (house).

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The triad "what, how and why, and where" is preserved exactly, and the instruction "Always look first to the planet" is emphasized as a procedural rule. The military metaphor of "battle" is kept but de‑dramatized in the paraphrase as "where the battle is taking place" to retain structure without over‑emphasizing conflict.
- **中文**："what / how and why / where" 直接以「是什么 / 为什么与如何 / 在哪里」表达，并在译文中通过「先行星、再星座、后宫位」反复强调顺序感。"where the battle is taking place" 则译为「斗争所在的生命领域」，同时在详细说明中弱化战争感、强化「工作与课题所在」的含义。

**Narrative Snippets**:
- `[ns_innersky_048]` `[trigger: interpretive_method]` `[factor_trigger: astro_what_function AND astro_astro_how_style AND astro_astro_where_arena]` `[role: 主干]` Always look first to the planet (the what), then use the sign (how and why), finally look at the house (where). → Source Text
- `[ns_innersky_049]` `[trigger: planet_sign_combo]` `[factor_trigger: astro_astro_sign AND astro_astro_house]` `[role: 主干依赖]` An aggressive planet in a sign of courage produces an assertive personality—but we need the house to see where it manifests. → Source Text
- `[ns_innersky_050]` `[trigger: house_release]` `[factor_trigger: astro_house AND astro_arena]` `[role: 条件分支]` The house tells us precisely which department of life the battle is taking place. → Source Text
- `[ns_innersky_051]` `[trigger: reading_sequence]` `[factor_trigger: astro_complete_meaning AND astro_synthesis]` `[role: 总结]` Unlocking the interactions of signs, planets, and houses is the key to unlocking the secrets of the birthchart. → Source Text
- `[ns_innersky_052]` `[trigger: where_question]` `[factor_trigger: astro_house AND astro_expression]` `[role: 主干]` Without the house, we only know energy exists; with the house, we see where it expresses and where work is needed. → English Paraphrase"""
    normalized_text_zh: str = """"""
    subject: str = "Interpretive Grammar – Planet = What, Sign = How/Why, House = Where"
    factor_refs: list = ['source_ref', 'rel_inner_sky_001', 'astro_chart_interpretation', 'rel_inner_sky_002', 'astro_complete_meaning', 'l1_anchor', 'confidence', 'evi_inner_sky_001', 'evi_inner_sky_002', 'astro_planet', 'mapping_id', 'source_factor', 'target_factor', 'notes', 'map_inner_sky_001', 'astro_planet', 'tarot_major_arcana', 'map_inner_sky_002', 'astro_house', 'bazi_gong']
    
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
        l1_anchor="tis_v1.0.0_interpretive_grammar___planet__001_L1",
    )
    version: str = "1.0.0"
