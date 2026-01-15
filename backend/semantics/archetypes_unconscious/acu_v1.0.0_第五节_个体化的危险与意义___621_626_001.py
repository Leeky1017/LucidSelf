"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.520068
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
    semantic_id="acu_v1.0.0_第五节_个体化的危险与意义___621_626_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第五节个体化的危险与意义621626(SemanticEntry):
    """
    **原文** (¶621-626, 行9600-9691):

> [621] It depends on the correctness of understanding whether the c...
    """
    
    original_text: str = """**原文** (¶621-626, 行9600-9691):

> [621] It depends on the correctness of understanding whether the consequences turn out more pathologically or less. The characteristic feature of a pathological reaction is identification with the archetype. This produces inflation and possession by emergent contents. Identification with the unconscious brings a weakening of consciousness—herein lies the danger. In more difficult cases it is far more necessary to strengthen the ego than to understand the unconscious.
>
> [622] This paper is a groping attempt to make the inner processes of the mandala more intelligible. The pictures represent a kind of ideogram of unconscious contents. One can paint very complicated pictures without having the least idea of their real meaning. The picture seems to develop out of itself and often in opposition to one's conscious intentions.
>
> [623-624] I have used the active imagination method since 1916. For at least thirteen years I kept quiet about the results to avoid suggestion—I wanted to assure myself that mandalas are produced spontaneously. A ten-year-old girl's dream of the four Gods in the four corners describes an unconscious individuation process: the dragon changes into pneuma (divine quaternity), followed by resurrection of the dead.
>
> [625-626] Origen said: "Seek these sacrifices within thyself—understand that thou art another little world, and hast within thee the sun and the moon and the stars." The individuation process subordinates the many to the One. The One is God, and what corresponds to him in us is the imago Dei, the God-image, which expresses itself in the mandala.

**英文释义**：
- 病理反应特征 = 与原型认同 → 膨胀和被附身
- 与无意识认同 → 意识弱化 = 危险所在
- 困难案例：加强自我比理解无意识更重要
- 曼陀罗画作 = 无意识内容的表意符号
- 画作自己发展，常与意识意图相反
- 积极想象法自1916年使用，13年保密以避免暗示
- 10岁女孩梦：四角四神 = 无意识个体化过程
- 俄利根：内有太阳月亮星辰的小世界
- 个体化 = 多归于一；一 = 上帝；上帝意象 = 曼陀罗

**中文诠释**：
- 病理反应 = 与原型认同 → 膨胀/附身 → 意识弱化
- 危险案例需加强自我而非理解无意识
- 曼陀罗 = 无意识内容的表意符号
- 画作自发发展，常违背意识意图
- 荣格1916年开始使用积极想象，13年保密
- 10岁女孩梦境证明曼陀罗的自发性
- 俄利根：人是另一个小世界，内有日月星辰
- 个体化 = 多归于一 = 上帝
- 上帝意象（imago Dei）= 曼陀罗

**Narrative Snippets**:
- `[ns_cw9i_IX_621]` `[trigger: archetype_inflation]` `[factor_trigger: jung_archetype AND jung_pathology]` `[role: 主干]` Pathological reaction = identification with archetype → inflation/possession → weakening of consciousness. → ¶621
- `[ns_cw9i_IX_622]` `[trigger: mandala_ideogram]` `[factor_trigger: jung_mandala AND jung_unconscious]` `[role: 主干依赖]` Mandala paintings are ideograms of unconscious contents—they develop out of themselves, often opposing conscious intentions. → ¶622
- `[ns_cw9i_IX_626]` `[trigger: one_god]` `[factor_trigger: jung_individuation AND jung_god]` `[role: 总结]` Individuation subordinates the many to the One; the One is God; the God-image expresses itself in the mandala. → ¶626"""
    normalized_text_zh: str = """"""
    subject: str = "第五节：个体化的危险与意义 (¶621-626)"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="acu_v1.0.0_第五节_个体化的危险与意义___621_626_001_L1",
    )
    version: str = "1.0.0"
