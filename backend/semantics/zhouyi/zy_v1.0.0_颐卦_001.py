"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899942
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
    semantic_id="zy_v1.0.0_颐卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 颐卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  颐：贞吉；观颐，自求口实。

  【彖传】
  《彖》曰：“颐，贞吉，养正则吉也。观颐，观其所养也；自求口实，观其自养也。天地养万物，...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  颐：贞吉；观颐，自求口实。

  【彖传】
  《彖》曰：“颐，贞吉，养正则吉也。观颐，观其所养也；自求口实，观其自养也。天地养万物，圣人养贤以及万民：颐之时大矣哉！”

  【象传】
  《象》曰：山下有雷，颐；君子以慎言语，节饮食。

  【爻辞】
  初九，舍尔灵龟，观我朵颐，凶。
  六二，颠颐；拂经，于丘颐，征凶。
  六三，拂颐；贞凶，十年勿用，无攸利。
  六四，颠颐，吉；虎视眈眈，其欲逐逐，无咎。
  六五，拂经；居贞吉，不可涉大川。
  上九，由颐；厉吉，利涉大川。

- 分字分词释义：

  - **颐**：本义为颊颐，引申为口与饮食，进一步引申为养生、养德、养人之道。
  - **贞吉**：守正则吉，强调“养”必须以正为前提。
  - **观颐，自求口实**：通过观察一个人如何受养、如何自求饮食，来判断其养生、养德与养人的方式。
  - **养正则吉**：养的内容在“正”，而非单纯满足欲望。
  - **山下有雷**：震雷在下、艮山在上，口在动中有止，象征在欲望活动之中需要节制与规范。
  - **朵颐**：夸张地咀嚼，形容大吃大喝。
  - **颠颐 / 拂颐 / 拂经**：颠倒、违背养之常道与经典法则。
  - **虎视眈眈，其欲逐逐**：如虎一般注视、欲望追逐不止，象征强大欲望之逼迫。
  - **由颐；厉吉，利涉大川**：顺着“颐养之道”而行，即使有危险，终可转吉，并有利于渡险。

- **规范化释义（primary_lang_explained）**：

  颐卦关心的是“养”的问题：如何养自己、养他人、养德与养生。卦辞说：“颐：贞吉；观颐，自求口实。”——守正则吉，通过观察一个人如何被养、如何自求饮食，可以看到其性情与道德状态，也可反观自身的养生方式是否合乎正道。

  彖传进一步指出：“养正则吉也”：养的核心不在于“多”，而在于“正”。“观颐，观其所养也；自求口实，观其自养也”说明：既要看一个人养的是谁（所养之人、所养之道），也要看其如何养自己（自求口实的方法）。天地养万物，圣人养贤以及万民，构成从宇宙到社会的养护体系，颐卦所处的“时”，因而极为重要。

  象传“山下有雷，颐；君子以慎言语，节饮食”则把“颐”具体化为口舌：山为止、雷为动，动中有止，提醒君子特别注意“口之两端”——言语与饮食。慎言、节食，都是“养正而不养妄”的实践。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Yi, "Nourishment" or "Providing Nourishment", concerns both what we take in and what we give out, both physical and spiritual sustenance. The Judgment, "Yi: steadfastness brings good fortune; observe the nourishing; seek what one fills one's own mouth with", emphasizes that one should be careful about what one consumes and how one sustains oneself and others.

- 核心要点：

  - 颐卦核心是**“以正养身、以正养德、以正养人”**，而非单纯追求物质满足。
  - “观颐，自求口实”提供了一种观察方法：从饮食与养护方式，洞见一个人或系统的深层结构。
  - 爻辞中多次出现“颠颐”“拂颐”“拂经”，形成对“错误养法”的连续警示，同时上九“由颐”指出顺着正当养法而行的出路。

- 详细解说：

  卦象山下有雷：雷动于下，山止于上，如同身体内部的欲望、食欲在下翻腾，而上层结构需要稳重以加以调制。与大畜相比，大畜重在“蓄养力量与德行”，颐则更聚焦在“日常饮食与言语行为”这类微观层面的养护。

  初九“舍尔灵龟，观我朵颐，凶”是颐卦的反面起点：舍弃象征长寿与灵性的“灵龟”，只看他人大吃大喝的朵颐之相，象征舍本逐末；六二、六三的“颠颐”“拂颐”“拂经”说明：一旦颠倒或违背养之常理，即便占贞亦凶，还会长期无所用，提示错误养法的惯性危害。

  六四“颠颐，吉；虎视眈眈，其欲逐逐，无咎”则较为复杂：位居上卦之初，既有教化之责，又被下卦之欲所逼迫；在此位上，表面似“颠颐”，实则是从下往上反转，若能以教化之光照下，则虽欲望炽盛，仍可无咎。六五“拂经；居贞吉，不可涉大川”则提醒：在尊位者即便有偏差，只要安分守正、勿涉险境，仍可吉而不致大祸，但不宜贸然跨越大险。上九“由颐；厉吉，利涉大川”总结全卦：顺着正确的养道而行，即使过程有险，终能吉，并有能力渡过大川式的大考。"""
    normalized_text_zh: str = """"""
    subject: str = "颐卦（䷚）"
    factor_refs: list = ['zhouyi_gua_yi']
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_颐卦_001_L1",
    )
    version: str = "1.0.0"
