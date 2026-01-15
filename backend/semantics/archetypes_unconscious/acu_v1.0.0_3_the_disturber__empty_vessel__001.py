"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.491631
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
    semantic_id="acu_v1.0.0_3_the_disturber__empty_vessel__001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 3TheDisturberEmptyVessel(SemanticEntry):
    """
    **Source Text** (¶180-186, Lines 2910-2995):

> [180] The woman whose fate it is to be a disturbing ...
    """
    
    original_text: str = """**Source Text** (¶180-186, Lines 2910-2995):

> [180] The woman whose fate it is to be a disturbing element is not solely destructive, except in pathological cases. Normally the disturber is herself caught in the disturbance; the worker of change is herself changed, and the glare of the fire she ignites both illuminates and enlightens all the victims of the entanglement.
>
> [181] If a woman of this type remains unconscious of the meaning of her function, she will herself perish by the sword she brings. But consciousness transforms her into a deliverer and redeemer.
>
> [182] The woman of the third type, who is so identified with the mother that her own instincts are paralysed, need not remain a hopeless nonentity forever. If she is at all normal, there is a good chance of the empty vessel being filled by a potent anima projection. Such women may become devoted wives of husbands identified with profession or talent—Cherchez la femme, and you have the secret of his success.
>
> [183] Emptiness is a great feminine secret—the chasm, the unplumbed depths, the yin. Such a female is fate itself. A man falls, absurdly happy, into this pit, or if he doesn't, he has missed his only chance of making a man of himself.
>
> [184-186] The negative mother-complex type is an unpleasant partner who rebels against everything natural. But at her best she cultivates everything certain, clear, and reasonable. She may become the friend, sister, and competent adviser of her husband, with a human understanding transcending the erotic. She has the best chance for marriage success in the second half of life—if she overcomes the chaos of the maternal womb. A complex can only be overcome if lived out to the full.

**English Paraphrase**:
- Disturber is herself changed; fire illuminates all victims
- Unconscious disturber perishes; conscious becomes deliverer
- Empty vessel can be filled by anima projection → husband's success
- Emptiness = feminine secret, yin, fate
- Negative type: rebels against natural → but at best = adviser, friend
- Best marriage success in second half—if overcomes maternal chaos

**中文诠释**:
- 扰乱者自己也改变；火照亮所有受害者
- 无意识扰乱者灭亡；有意识者成为救赎者
- 空容器可被阿尼玛投射填满 → 丈夫的成功
- 空虚 = 女性秘密，阴，命运
- 负面类型：反抗自然 → 但最佳状态 = 顾问、朋友
- 后半生婚姻最成功——若克服母性混沌

**Narrative Snippets**:
- `[ns_cw9i_III_180]` `[trigger: disturber_purification]` `[factor_trigger: jung_transformation AND jung_feminine]` `[role: 主干]` Disturber is herself changed; what seemed senseless upheaval becomes purification. → ¶180
- `[ns_cw9i_III_182]` `[trigger: empty_vessel]` `[factor_trigger: jung_anima AND jung_projection]` `[role: 主干依赖]` Empty vessel filled by anima projection—Cherchez la femme, secret of his success. → ¶182
- `[ns_cw9i_III_183]` `[trigger: feminine_yin]` `[factor_trigger: jung_feminine AND jung_yin]` `[role: 条件分支]` Emptiness is great feminine secret—the yin. Such female is fate itself. → ¶183
- `[ns_cw9i_III_184]` `[trigger: negative_marriage]` `[factor_trigger: jung_feminine AND jung_development]` `[role: 总结]` Negative type has best chance for marriage success in second half of life. → ¶184"""
    normalized_text_zh: str = """"""
    subject: str = "3 The Disturber, Empty Vessel, and Negative Complex (¶180-186)"
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
        l1_anchor="acu_v1.0.0_3_the_disturber__empty_vessel__001_L1",
    )
    version: str = "1.0.0"
