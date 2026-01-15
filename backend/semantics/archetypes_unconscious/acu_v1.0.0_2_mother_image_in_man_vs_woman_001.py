"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491653
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
    semantic_id="acu_v1.0.0_2_mother_image_in_man_vs_woman_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 2MotherImageInManVsWoman(SemanticEntry):
    """
    **Source Text** (¶191-194, Lines 3146-3200):

> [191] I have tried to give a survey of the psychic p...
    """
    
    original_text: str = """**Source Text** (¶191-194, Lines 3146-3200):

> [191] I have tried to give a survey of the psychic phenomena attributable to the predominance of the mother-image. When we ask patients influenced by the mother-image to express what "Mother" means to them, we invariably get symbolical figures which are direct analogies of the mythological mother-image.
>
> [192] The mother-image in a man's psychology is entirely different from a woman's. For a woman, the mother typifies her own conscious life as conditioned by her sex. But for a man the mother typifies something alien, filled with imagery latent in the unconscious. The mother has a decidedly symbolical significance for a man, which accounts for his strong tendency to idealize her. Idealization is a hidden apotropaism; one idealizes whenever there is a secret fear to be exorcized.
>
> [193] For a man the mother is ipso facto symbolical; for a woman she becomes a symbol only in the course of development. The Urania type predominates in masculine psychology; the chthonic Earth Mother is most frequent in women. A woman can identify directly with the Earth Mother, but a man cannot. The man identifies with the son-lover—puer aeternus or filius sapientiae. But the companion of the chthonic mother is an ithyphallic Hermes or lingam.
>
> [194] As soon as we touch on these identifications we enter the realm of the syzygies, paired opposites, where the One is never separated from the Other. It is a field leading directly to individuation, the attainment of the self. This realm is so entirely one of immediate experience that it cannot be captured by formula. The terrifying paradox of the primordial mother-image.

**English Paraphrase**:
- Man's mother-image ≠ woman's: for man = alien, symbolical, unconscious imagery
- Man idealizes mother = apotropaism (fear of unconscious)
- Man = Urania type; woman = chthonic Earth Mother
- Man identifies with son-lover (puer aeternus); woman with Earth Mother directly
- Syzygies → individuation → attainment of self
- Primordial mother-image = terrifying paradox

**中文诠释**:
- 男人的母亲意象 ≠ 女人的：对男人 = 异质的、象征性的、无意识意象
- 男人理想化母亲 = 驱邪（对无意识的恐惧）
- 男人 = 天王星类型；女人 = 地母类型
- 男人认同儿子-情人（永恒少年）；女人直接认同地母
- 配对 → 个体化 → 自性实现
- 原始母亲意象 = 可怕的悖论

**Narrative Snippets**:
- `[ns_cw9i_III_192]` `[trigger: mother_alien]` `[factor_trigger: jung_mother AND jung_fear]` `[role: 主干]` Man's mother-image is alien, symbolical; his idealization is hidden fear of unconscious. → ¶192
- `[ns_cw9i_III_193]` `[trigger: urania_chthonic]` `[factor_trigger: jung_anima AND jung_animus]` `[role: 主干依赖]` Man = Urania type, identifies with puer aeternus; woman = chthonic, identifies with Earth Mother. → ¶193
- `[ns_cw9i_III_194]` `[trigger: syzygy_individuation]` `[factor_trigger: jung_syzygy AND jung_individuation]` `[role: 条件分支]` Syzygies lead to individuation—realm of immediate experience, terrifying paradox. → ¶194"""
    normalized_text_zh: str = """"""
    subject: str = "2 Mother-Image in Man vs Woman (¶191-194)"
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_2_mother_image_in_man_vs_woman_001_L1",
    )
    version: str = "1.0.0"
