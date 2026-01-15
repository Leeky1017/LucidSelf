"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.520045
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
    semantic_id="acu_v1.0.0_第四_5节_波墨曼陀罗与对立统一___603_614_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第四5节波墨曼陀罗与对立统一603614(SemanticEntry):
    """
    **原文** (¶603-614, 行9361-9498):

> [603] Böhme was the first to try to organize the Christian cosmos ...
    """
    
    original_text: str = """**原文** (¶603-614, 行9361-9498):

> [603] Böhme was the first to try to organize the Christian cosmos as a total reality into a mandala. The attempt failed because he was unable to unite the two halves in a circle. Miss X's mandala, on the other hand, comprises and contains the opposites—aided by the Chinese doctrine of Yang and Yin.
>
> [604-608] In Picture 10, dualities are always inwardly balanced, losing their sharpness. Two crabs appear in the lower hemisphere. Cancer is a feminine and watery sign; it signifies resurrection (the crab sheds its shell). Miss X was born in the first degrees of Cancer. The essential conclusion: dualities are counterbalanced by the unity of the centre where the lamp shines. This climax where universal opposites clash is when synchronistic phenomena occur—sixteen years later, Miss X became fatally ill with cancer of the breast.
>
> [609-611] The sun is sinking, moon coming out. The mandala's radiation has ceased, but sun, moon, and earth have been assimilated into it. Animation by human figures and animals. The source of radiation is now outside—the full moon radiating rainbow-coloured light in concentric circles.
>
> [612-614] The mandala floats over Fifth Avenue, New York. The coniunctio of the royal pair represented by sacrificial fire—a typical marriage quaternio. The mandala floats between Manhattan and sea. Blue snakes penetrate into red flesh: enantiodromia setting in. An eye motif appears, linking to polyophthalmia and the "multiple consciousness" of the unconscious.

**英文释义**：
- 波墨首次尝试将基督教宇宙组织为曼陀罗，但失败（无法统一两半）
- X小姐的曼陀罗包含对立——借助阴阳学说
- 画作10中二元性内在平衡，失去尖锐性
- 螃蟹出现：巨蟹座 = 女性/水象；复活象征
- X小姐生于巨蟹座；16年后死于乳腺癌（共时性）
- 太阳下沉，月亮出现；曼陀罗辐射停止
- 曼陀罗飘浮于曼哈顿上空
- 王室对结合（coniunctio）= 婚姻四元组
- 蓝蛇穿透红肉 = 对极转化（enantiodromia）
- 眼睛母题 = 多眼性 = 无意识的"多重意识"

**中文诠释**：
- 波墨首创基督教宇宙曼陀罗，但失败——无法统一两半
- X小姐曼陀罗成功包含对立（借助阴阳）
- 画作10：二元性内在平衡
- 螃蟹象征：巨蟹座 = 女性/水象 = 复活（蟹脱壳）
- X小姐生于巨蟹座初度；16年后乳腺癌去世
- 这是共时性现象的典型案例
- 太阳下沉/月亮升起；辐射停止但日月地被同化入曼陀罗
- 曼陀罗飘浮于纽约第五大道上空
- 王室对结合 = 移情心理学的婚姻四元组
- 蓝蛇穿透红肉 = 对极转化开始
- 眼睛母题 = 多眼性 = 无意识的多重意识

**Narrative Snippets**:
- `[ns_cw9i_IX_603]` `[trigger: opposites_union]` `[factor_trigger: jung_opposites AND jung_yinyang]` `[role: 主干]` Böhme failed to unite opposites in mandala; Miss X succeeded aided by Chinese Yin-Yang doctrine. → ¶603
- `[ns_cw9i_IX_608]` `[trigger: synchronicity_cancer]` `[factor_trigger: jung_synchronicity AND jung_symbol]` `[role: 主干依赖]` Cancer sign appeared; 16 years later Miss X died of breast cancer—a synchronistic phenomenon at the climax of opposites. → ¶608
- `[ns_cw9i_IX_614]` `[trigger: polyophthalmia]` `[factor_trigger: jung_eye AND jung_unconscious]` `[role: 条件分支]` Eye motif = polyophthalmia = "multiple consciousness" of the unconscious. → ¶614"""
    normalized_text_zh: str = """"""
    subject: str = "第四.5节：波墨曼陀罗与对立统一 (¶603-614)"
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
        l1_anchor="acu_v1.0.0_第四_5节_波墨曼陀罗与对立统一___603_614_001_L1",
    )
    version: str = "1.0.0"
