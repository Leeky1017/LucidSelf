"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.473133
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
    semantic_id="iod_v1.0.0_1_the_simplest_cases_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 1TheSimplestCases(SemanticEntry):
    """
    **Source Text**:
"If we call to our aid the dreams of children, we shall find in them the simplest w...
    """
    
    original_text: str = """**Source Text**:
"If we call to our aid the dreams of children, we shall find in them the simplest wish-fulfilments. They are almost always undisguised wish-fulfilments."

"My youngest daughter, then nineteen months old, had had an attack of vomiting one morning, and had consequently been kept without food all day. During the night she was heard to call out excitedly in her sleep: 'Anna Fweud, stwawbewwies, wild stwawbewwies, omblet, pudden!'"

"The dream of another child, a boy of twenty-two months, conveyed a present which had been bestowed on him the previous day—a basketful of cherries."

"A boy of five and a quarter years, on an excursion to the foot of the Dachstein, at first objected to go. But the more beautiful did the view become... the more enthusiastic did he become. On the way home he kept asking whether there were higher mountains. The next morning he related: 'Last night I dreamed that we were at such a height that we saw all Italy.'"

**Key Term Analysis**:

| Term | Definition | Significance |
|------|-----------|---------------|
| Children's Dreams | 儿童梦 | Undisguised wish fulfillment | Simplest proof |
| Anna Freud Dream | 安娜·弗洛伊德之梦 | Food denied → dream of feast | Direct fulfillment |
| Cherry Dream | 樱桃梦 | Gift received → dream repeats | Pleasure prolongation |
| Dachstein Dream | 达赫施泰因梦 | Limited view → dream of Italy | Wish for more |

**English Paraphrase (Primary Language)**:

Children's dreams are **transparent**—undisguised wish fulfillments requiring no interpretation. Little Anna, denied food all day, dreams of a feast: "strawberries, wild strawberries, omblet, pudden!" The boy given cherries dreams of eating them again. The child disappointed by limited mountain views dreams of seeing "all Italy."

These dreams show the **formula in pure form**:
1. A wish arises (hunger, pleasure, curiosity)
2. Reality frustrates the wish (no food, excursion ends, view limited)
3. The dream fulfills the wish (feast, cherries again, Italy panorama)

Children's dreams lack **disguise** because children lack the complex repressions of adults. The censor is weak or absent. What adults achieve through dream-work (condensation, displacement, symbolization), children achieve directly.

This is why children's dreams are **pedagogically essential**: they reveal the dream's basic function before complications obscure it.

**Complete Chinese Interpretation (Secondary Language)**:

儿童梦是**透明的**——不加伪装的愿望满足，无需解释。小安娜整天被禁食，梦见盛宴："草莓，野草莓，煎蛋卷，布丁！"得到樱桃的男孩梦见再次吃樱桃。对有限山景失望的孩子梦见看到"整个意大利"。

这些梦展示了**纯粹形式的公式**：
1. 愿望产生（饥饿、快乐、好奇）
2. 现实挫败愿望（无食物、旅行结束、视野有限）
3. 梦满足愿望（盛宴、再次樱桃、意大利全景）

儿童梦缺乏**伪装**因为儿童缺乏成人的复杂压抑。审查者薄弱或不存在。成人通过梦工作（凝缩、移置、象征化）实现的，儿童直接实现。

这就是为什么儿童梦具有**教学本质意义**：它们揭示了梦的基本功能，在复杂性遮蔽之前。

**Narrative Snippets**:

- `[ns_freud_wish_003]` `[trigger: children_dreams]` `[factor_trigger: dream_wishfulfillment AND dream_child AND children_dreams AND undisguised]` `[role: 主干]` Children's dreams are the simplest wish-fulfillments—almost always undisguised, requiring no interpretation. The child denied food dreams of a feast. → Freud Ch.III #Children
- `[ns_freud_wish_004]` `[trigger: anna_dream]` `[factor_trigger: dream_wishfulfillment AND dream_specimen]` `[role: 主干依赖]` Anna Freud (19 months), kept without food all day, dreamed: "Anna Fweud, stwawbewwies, wild stwawbewwies, omblet, pudden!"—direct, undisguised wish fulfillment. → Freud Ch.III #Children
- `[ns_freud_wish_005]` `[trigger: dachstein_dream]` `[factor_trigger: waking_frustration AND dream_content]` `[role: 条件分支]` Boy disappointed by limited mountain view dreamed of standing at such a height that he "saw all Italy"—the dream compensates for waking frustration. → Freud Ch.III #Children
- `[ns_freud_wish_006]` `[trigger: no_disguise]` `[factor_trigger: dream_child AND dream_censor]` `[role: 条件分支]` Children's dreams lack disguise because children lack complex repressions—the censor is weak or absent, revealing wish fulfillment in pure form. → Freud Ch.III #Children"""
    normalized_text_zh: str = """"""
    subject: str = "1 The Simplest Cases"
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
        l1_anchor="iod_v1.0.0_1_the_simplest_cases_001_L1",
    )
    version: str = "1.0.0"
