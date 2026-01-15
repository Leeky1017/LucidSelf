"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042214
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
    semantic_id="smth_v1.0.0_河图龙龟与伏羲画卦_001",
    book_id="sanming",
    engine_id="bazi"
)
class 河图龙龟与伏羲画卦(SemanticEntry):
    """
    - **原文（source_text）**：
  夫河龙负图者，非龙也，乃大龟也。其背上所有之纹，一长书、二短画，白墨近尾，九紫点近颈，四碧点在肩之左，二黑点在肩之右，六白点近足之右，一白点近足之左，...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫河龙负图者，非龙也，乃大龟也。其背上所有之纹，一长书、二短画，白墨近尾，九紫点近颈，四碧点在肩之左，二黑点在肩之右，六白点近足之右，一白点近足之左，三绿点在胁之左，七赤点在胁之右，五黄点在背之中，几九所而七色焉。羲皇以九位而定方，以二长画二短画而生爻，以三才而设位，易道凡是而生矣。

- **分字分词释义**：
  - **河龙负图 / 大龟**：黄河水中负图而出的神兽，实指「龙龟」之背纹，与洛书神龟相对。
  - **长书短画**：背上纵横纹理，被视为点画与数目的原始形态。
  - **九位定方**：以九个关键位置来划分方位与中宫，为后世「九宫」之源。
  - **生爻、设位**：由图中线画抽象出阴阳爻象，并据三才（天、地、人）安立卦位。

- **规范化释义（primary_lang_explained）**：
  本段转而描述「河图」：黄河之中浮出龙龟，龟背上有纵横纹与彩点，被解释为数与象的原始载体。伏羲据此九个关键位置来划分方位，进一步以长短之画抽象为阴阳爻，再据三才而设八卦之位。也就是说，卦爻之画不是凭空创造，而是对「河图」这一自然纹理的抽象与制度化。
 
- **核心要点**：
  - 河图提供的是「象位」与「九宫」的雏形，是卦爻体系与五行方位的图像基础。
  - 从命理角度看，干支、宫位等所有「格局」的划分，都可追溯到这一套「图像—数位—卦爻」的结构链条。
  - 河图与洛书一静一动：前者重在方位与图象，后者重在数列与运行，共同构成后世术数的底层坐标系。

- **详细解说**：
  1) 研读命理或易学时，可先按「河图—九宫—卦爻」的顺序梳理框架：由图像认识方位，再由方位认识卦象与五行；
  2) 在系统建模中，将河图视作「象位层」，洛书视作「数位层」，卦爻视作「逻辑层」，三者分离又可互相映射；
  3) 推命时，先看宫位与格局（象位层），再看强弱与数理（数位层），最后看卦爻或规则逻辑（逻辑层），避免直接从零散条文跳到结论；
  4) 工程上可引入「图像模板」概念，把典型的河图—九宫分布固化为配置，由可视化模块直接调用，增强可解释性。

- 反例与边界：
  - 不宜把河图简化为几句口号式「先天八卦图」，所有具体结构都不看，只凭记忆形状来断命；
  - 也不应把卦爻的任何变化都硬说成「河图必然如此」，用后天演绎去倒扣先天架构；
  - 在工程实现中，如果把河图、洛书、卦爻揉在一堆数据结构里，既不利于调试，也难以解释「这一条规则究竟依赖哪一层象理」；
  - 反向误区是，为追求「纯图像化」，只画图不落到任何数值或规则，最终无法支持严谨推理。

- 小例（示意）：
  - 某用户只熟背「先天八卦图」，却无法说明命盘中某宫为何为用、某宫为何为忌，系统可提示其补足「河图九宫—方位—卦爻」的结构知识，而不是再给更多零散口诀；
  - 在知识图谱中，将「河图节点」与「宫位」「卦爻」分别建边，可让模型自动学习「哪些卦爻组合在某些方位上出现频率更高」，从而验证或修正传统经验。

- **完整对等诠释（secondary_lang_full）**：
  This passage describes the River Diagram: a dragon-turtle emerged from the Yellow River, bearing patterns of lines and colored dots on its back, interpreted as the primordial carrier of numerical and symbolic systems. Fu Xi used these nine key positions to define cardinal directions, abstracted the long and short lines into yin and yang trigram lines, and established the Eight Trigrams positions according to the Three Powers (Heaven, Earth, Human). The trigram lines were not arbitrarily invented but abstracted and systematized from natural patterns. The River Diagram provides the prototype of "image-positions" and "Nine Palaces," serving as the foundational imagery for both trigram systems and Five Element orientation, forming together with Luo Diagram the dual coordinate system underlying all later numerological arts."""
    normalized_text_zh: str = """"""
    subject: str = "河图龙龟与伏羲画卦"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_河图龙龟与伏羲画卦_001_L1",
    )
    version: str = "1.0.0"
