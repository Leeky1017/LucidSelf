"""
Auto-generated semantic module for the_inner_sky
Generated at: 2025-12-05T13:30:20.134425
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
    semantic_id="tis_v1.0.0_example___venus_in_virgo_in_th_001",
    book_id="the_inner_sky",
    engine_id="astro"
)
class ExampleVenusInVirgoInTh(SemanticEntry):
    """
    **Source Text**:
"Everybody has a Venus. Everybody is influenced by Virgo. All of us face the dramas...
    """
    
    original_text: str = """**Source Text**:
"Everybody has a Venus. Everybody is influenced by Virgo. All of us face the dramas of the sixth house. Those features mark us as human. But they do not describe us individually. To do that we must take astrology a step further. Venus. Virgo. The sixth house. What are they? Only abstractions, nothing more. But what happens when we put them together like the man in our sample chart? What about Venus in Virgo? And what if the combination of the two expresses itself through the sixth house? That’s when the magic begins. ... A sign-planet-house combination is the most elemental astrological statement applicable to an individual."

"With Venus in his sixth house, the Englishman whose life we are beginning to decode probably does most of his professional work in partnerships. His relationship-forming what expresses itself in the where of his daily livelihood. Throughout his life he finds himself confronted by the need to sustain harmonious personal relationships if he is to cope successfully with the realities of his chosen work. ... Professionally, his fortune lies with the planet Venus. In the world of work, that psychological function is his guiding star. Should he ignore it, he meets only aimlessness and closed doors."

**Key Term Analysis**:
- `abstractions vs bit`: single symbols (Venus, Virgo, sixth house) as general patterns vs their concrete combination.
- `Venus in Virgo in the sixth`: example of a specific planet–sign–house bit.
- `professional partnerships`: sixth-house arena colored by Venusian relating.
- `fortune lies with Venus`: vocational success tied to honoring the Venus function.

**English Paraphrase (Primary Language)**:
Forrest uses the example of the Englishman’s chart to show how separate symbols become personal when combined. Venus alone, Virgo alone, and the sixth house alone are abstractions that apply to everyone. Only when we combine them—Venus in Virgo in the sixth house—do we get a concrete bit that describes one individual.

In this case, Venus (relationship and aesthetic function) is colored by Virgo (perfectionist, servant, analyst) and expressed through the sixth house (work, duty, competence, service). The result is a life in which professional partnerships are central: his ability to sustain harmonious, skill‑based working relationships is critical to his livelihood. If he follows his Venus function—bringing beauty, cooperation, and relational sensitivity into his sixth‑house work—doors open. If he ignores it, he meets aimlessness and closed doors: work without love, service without mutual respect.

**Complete Chinese Interpretation (Secondary Language)**:
Forrest 通过样例命盘中的英国人，示范「从抽象到具体」的过程。单独看金星、处女座、第六宫，这些都只是适用于所有人的一般模式；只有当三者组合成「处女座第六宫金星」时，才真正落到某一个体身上，成为可描述的独特 bit。

在这个例子里，金星代表**关系与审美功能**；处女座赋予它「完美主义、服务、分析」的基调；第六宫则提供「工作、职责、技能、服务他人」的舞台。合在一起，就成为一种生命结构：职业领域中的伙伴关系是命运要他重点练习的课题。如果他顺着金星功能行事——在第六宫的工作中持续带入美感、合作与对他人的细腻体恤——职业通路便更容易打开；若一味忽视金星，只把工作当作义务，他遇到的就会是迷茫、关闭的门，与一份缺乏人味的劳作。

**Core Points**:
- Single symbols (Venus, Virgo, sixth house) become personal only when combined into a bit.
- Venus in Virgo in the sixth = relational function expressed through perfectionist, service‑oriented work.
- Work partnerships are a key arena for this person’s Venusian growth.
- Ignoring the Venus function in sixth‑house contexts leads to vocational frustration and closed opportunities.

**Detailed Explanation**:
This example operationalizes the five‑step method. We start with Venus (what: relationship/aesthetic function), move to Virgo (why/how: perfection, service, analysis), then to resources and distortions (commitment, competence, but also pickiness and over‑idealization), and finally to the sixth house (where: daily work, skills, service).

The configuration does not decree a specific job title. Instead, it narrows the field of meaningful work to contexts where Venusian qualities—cooperation, beauty, human connection—are woven into service and competence. The example also illustrates how distortions work: Virgo’s perfectionism may sabotage both work and relationships if it slides into relentless criticism or martyrdom. Framing these as risks rather than fate preserves free will while still giving clear guidance about where growth is demanded.

**Textual Criticism & Variant Analysis (Bilingual)**:
- **English**: The dramatic metaphors ("eye as cold as an ice‑pick," "shotgun in his hands") are softened in the paraphrase to keep focus on structure rather than shock value. The line "professionally, his fortune lies with the planet Venus" is retained conceptually as vocational guidance, not prediction.
- **中文**：对原文夸张比喻不作直译，而通过「职业通路」「工作中带入金星功能」等表达保留其结构含义。特别强调「不指定职业，只缩小有意义的工作场域」，避免读者将其理解为具体工作清单式占卜。"""
    normalized_text_zh: str = """"""
    subject: str = "Example – Venus in Virgo in the Sixth House (From Theory to Personal Life)"
    factor_refs: list = ['source_ref', 'rel_inner_sky_bit_001', 'concrete_bit', 'evi_inner_sky_bit_001', 'rule_bit_combination', 'concept_astrological_bit', 'mingpan_zuhe', 'dream_symbol_cluster']
    
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
        l1_anchor="tis_v1.0.0_example___venus_in_virgo_in_th_001_L1",
    )
    version: str = "1.0.0"
