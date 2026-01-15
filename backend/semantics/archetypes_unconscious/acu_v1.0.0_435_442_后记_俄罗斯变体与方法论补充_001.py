"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.498299
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
    semantic_id="acu_v1.0.0_435_442_后记_俄罗斯变体与方法论补充_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 435442后记俄罗斯变体与方法论补充(SemanticEntry):
    """
    **原文** (§435-442, 行6791-6899):

> [435] Postscript. Only after the completion of my manuscript was m...
    """
    
    original_text: str = """**原文** (§435-442, 行6791-6899):

> [435] Postscript. Only after the completion of my manuscript was my attention drawn by a friend to a Russian variant of our story, "Maria Morevna." The hero is Czarevitch Ivan. The three helpful animals correspond to Ivan's three sisters and their bird-men husbands—a species of angel emphasizing the auxiliary nature of unconscious functions. The evil spirit is called Koschei the Deathless. The witch is Baba Yaga. Princess is Queen Maria Morevna, a martial leader, who has chained up the evil spirit with twelve chains.
>
> [436-437] These remarks are mainly technical. I have dealt with the problem of three- and four-leggedness of magic horses. This piece of psychological reasoning rests on the irrational data of the fairytale, myth, or dream, and the conscious realization of their "latent" rational connections. The three-legged and four-legged horses remind us of the axiom of Maria Prophetissa, which plays a considerable role in alchemy.
>
> [438-439] The three-legged horse assigned to the princess is a mare, a bewitched princess. Threeness is connected with femininity. Three-leggedness as the attribute of an animal denotes the unconscious masculinity immanent in a female creature—the animus representing "spirit."
>
> [440-442] Princess A is the anima of the hero. She possesses the three-legged horse (the shadow, the inferior function-triad). The mare is Princess B, who is bewitched and possessed by a masculine triad (shadow). The hunter/magician has bewitched her. The hunter is connected with the hero, who gradually puts himself in his shoes.

**英文释义**：
- 俄罗斯变体"Maria Morevna"：英雄=伊凡王子
- 三个帮助动物 = 三姐妹及其鸟人丈夫（天使性辅助功能）
- 邪恶精神 = 不死的Koschei；女巫 = Baba Yaga
- 公主 = 女王Maria Morevna（军事领袖）用12条锁链锁住邪恶精神
- 方法论：处理童话中三腿/四腿马的问题
- 基于非理性数据和意识对潜在理性联系的认识
- 三腿马 = 母马 = 被施咒的公主 = 三性与女性相连
- 三腿性 = 女性生物中的无意识男性 = 阿尼姆斯
- 公主A = 英雄的阿尼玛，拥有三腿马（阴影/劣势功能三元组）

**中文诠释**：
- 俄罗斯变体"玛丽亚·莫列芙娜"提供重要补充
- 三个帮助动物对应伊凡的三姐妹及其鸟人丈夫（天使性质）
- 不死的科什切伊 = 邪恶精神；芭芭雅加 = 女巫
- 玛丽亚·莫列芙娜女王 = 军事领袖（呼应东正教圣母"军队统帅"称号）
- 方法论说明：如何解释童话中的非理性数据
- 三腿马 = 母马 = 被施咒的公主B
- 三性与女性相连（尽管在宗教意识中三是男性）
- 三腿性 = 女性中的无意识男性 = 阿尼姆斯
- 公主A（阿尼玛）拥有三腿马（阴影）= 她占据了英雄的弱点

**Narrative Snippets**:
- `[ns_cw9i_VI_435]` `[trigger: maria_morevna]` `[factor_trigger: jung_fairytale AND jung_trinity]` `[role: 主干]` Russian variant "Maria Morevna": three helpful animals = Ivan's three sisters married to bird-men (angelic helpers). → §435
- `[ns_cw9i_VI_439]` `[trigger: three_legged]` `[factor_trigger: jung_animus AND jung_triad]` `[role: 主干依赖]` Three-legged horse = mare = unconscious masculinity in female = animus representing spirit. → §438-439
- `[ns_cw9i_VI_440]` `[trigger: anima_shadow]` `[factor_trigger: jung_anima AND jung_shadow]` `[role: 条件分支]` Princess A (anima) possesses three-legged horse (shadow)—she has caught the hero on his weak side. → §440"""
    normalized_text_zh: str = """"""
    subject: str = "§435-442 后记：俄罗斯变体与方法论补充"
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
        l1_anchor="acu_v1.0.0_435_442_后记_俄罗斯变体与方法论补充_001_L1",
    )
    version: str = "1.0.0"
