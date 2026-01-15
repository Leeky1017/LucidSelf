"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.919554
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
    semantic_id="zy_v1.0.0_中孚卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 中孚卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  中孚：豚鱼吉，利涉大川，利贞。

  【彖传】
  《彖》曰：“中孚，柔在内而刚得中，说而巽。孚乃化邦也。豚鱼吉，信及豚鱼也。利涉大川...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  中孚：豚鱼吉，利涉大川，利贞。

  【彖传】
  《彖》曰：“中孚，柔在内而刚得中，说而巽。孚乃化邦也。豚鱼吉，信及豚鱼也。利涉大川，乘木舟虚也。中孚以利贞，乃应乎天也。”

  【象传】
  《象》曰：泽上有风，中孚；君子以议狱缓死。

  【爻辞】
  初九，虞吉，有它不燕。
  九二，鸣鹤在阴，其子和之。我有好爵，吾与尔靡之。
  六三，得敌，或鼓或罢，或泣或歌。
  六四，月几望，马匹亡，无咎。
  九五，有孚挛如，无咎。
  上九，翰音登于天，贞凶。

- 分字分词释义：

  - **中孚**：居中的“孚”，孚为诚信、信实；“中孚”指发自内心、居于中道的诚信，而非表面的信用交易。
  - **豚鱼吉**：猪与鱼为质朴微贱之牲，能够因诚信而致吉，象征“信及豚鱼”，诚信之力连最不显要处亦能感通。
  - **利涉大川**：有利于渡过大河，比喻在险阻之中仍能凭借诚信与合宜工具跨越难关。
  - **泽上有风**：上巽为风，下兑为泽，风在泽上吹拂，声音与波纹互相感应，象征在柔和环境中循环往复的感通之气。
  - **议狱缓死**：对刑狱案件多番审议、从宽处理死刑，以诚信与怜悯为司法之本。
  - **虞吉，有它不燕**：“虞”为预虑、慎思；守一事而虞之则吉，若心怀他念则不得安宁。
  - **鸣鹤在阴，其子和之**：鹤在阴处鸣叫，小鹤和之，比喻诚信与真情在上下、父子、师生间自然相感，相与唱和。
  - **得敌**：遇到对立之人或对峙之局面；在中孚卦中提示“在冲突中看见对方”。
  - **月几望**：月将满未满之时，比喻诚信与局势已近圆满，但仍有一线未尽之处。
  - **翰音登于天**：翰为羽鸟，音登于天，象征声音高亢而上，近于夸张与虚浮，失去中孚之实。

- **规范化释义（primary_lang_explained）**：

  中孚卦讲的是“以内心真实的诚信达成感通”。卦辞云：“中孚：豚鱼吉，利涉大川，利贞。”——当诚信居于中道，不偏不倚，它所感通的范围可以细至“豚鱼”之类的小牲，也可以大到“涉大川”的险境；这样的诚信既能带来吉祥，又有利于坚守正道。

  彖传用卦爻结构说明中孚的条件：阴爻居内，阳爻得中，“说而巽”——外表和悦、内里谦巽。诚信不是刚硬的自我坚持，也不是软弱的逢迎，而是有骨有肉、内外相应的真实。这样的诚信可以“化邦”，使邦国风气由内而变。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Zhong Fu (Inner Truth) addresses 诚信中正. This hexagram emphasizes the importance of understanding natural patterns and human responses in specific life situations.

- 核心要点：

  - 中孚卦核心是**“从内心出发的诚信感通”**，不同于表面守信或权宜之信。
  - “豚鱼吉”“利涉大川”展示诚信的双重尺度：既能照顾微小者，也能应对大险。
  - 各爻围绕“是否保持中孚”展开，从虞吉、不燕，到得敌、月几望、翰音登天，呈现诚信在具体关系与处境中的摇摆与考验。

- 详细解说：

  卦象为上巽下兑：风在泽上，风吹泽面，既有荡涤之意，又有声波与水波相感之象。君子“以议狱缓死”，是将中孚落实在制度与实践：在处理争讼与生死大事时，不以冷硬法规断人生，而是以真诚体察、反复讨论，尽力给出宽缓之机。

  初九“虞吉，有它不燕。”强调一开始要“虞”——预虑、慎思，对所守之事保持专注，则吉；若心怀他念，便难以安坐。九二“鸣鹤在阴，其子和之。我有好爵，吾与尔靡之。”则描绘中孚在亲密关系中的自然流露：如鹤鸣而子和，彼此以心声相应；“我有好爵，吾与尔靡之”象征愿与人分享所得，诚信不藏私。

  六三“得敌，或鼓或罢，或泣或歌。”则展示当面对“敌”时，内部反应纷乱——有奋战、有退缩、有哭泣、有歌唱；中孚在冲突中容易被扰动，需要重新回到内心真实。六四“月几望，马匹亡，无咎。”说明在局势接近圆满之时，主动舍弃某些“马匹”——既有依托，以避免过满所致之祸，最终可以无咎。

  九五“有孚挛如，无咎。”代表在尊位者以持续的诚信将众心“挛如”地系在一起，因此无咎；此处的“孚”已非单次表态，而是长期一贯。上九“翰音登于天，贞凶。”则是偏离中孚的终局：声音飞扬到天上，虽似诚挚高亢，实则脱离实际、难以久长；过度的高调与宣示反而削弱了诚信的力量，故虽自以为贞，实则为凶。


#### L2 语义提取

- **主题**：诚信中正，如何在此情境中顺应天道、把握时机、实现人生目标。

- **自然属性**：
  - **象征**：泽上有风、豚鱼吉、利涉大川、鸣鹤在阴其子和之。
  - **特性**：本卦特有的运作方式与吉凶条件。
  - **元素**：上下卦组合的五行与象征意义。

- **功能象义**：

- **校勘与字词辨析（双语）**：
- **叙事素材（narrative_snippets）**：
  - `[ns_zhouyi_551]` `[trigger: 卦=中孚 AND 卦辞=豚鱼吉]` `[factor_trigger: zhouyi_gua_zhongfu AND zhouyi_guaci]` `[role: 主干]` 中孚，豚鱼吉，利涉大川：诚信感化及于豚鱼。 → 《周易·中孚卦·卦辞》
  - `[ns_zhouyi_552]` `[trigger: 卦=中孚 AND 彖传]` `[factor_trigger: zhouyi_gua_zhongfu AND zhouyi_tuan]` `[role: 主干依赖]` 柔在内而刚得中。 → 《周易·中孚卦·彖传》
  - `[ns_zhouyi_553]` `[trigger: 卦=中孚 AND 象传=泽上有风]` `[factor_trigger: zhouyi_gua_zhongfu AND zhouyi_xiang]` `[role: 主干依赖]` 泽上有风，中孚；君子以议狱缓死：诚信如风感泽，议狱宜缓。 → 《周易·中孚卦·象传》
  - `[ns_zhouyi_554]` `[trigger: 卦=中孚 AND 初九=虞吉]` `[factor_trigger: zhouyi_gua_zhongfu]` `[role: 条件分支]` 虞吉，有它不燕：安虞则吉，有变则不安。 → 《周易·中孚卦·爻辞》
  - `[ns_zhouyi_555]` `[trigger: 卦=中孚 AND 九二=鸣鹤在阴]` `[factor_trigger: zhouyi_gua_zhongfu]` `[role: 主干依赖]` 鸣鹤在阴，其子和之：鹤鸣于阴，子声相应。 → 《周易·中孚卦·爻辞》
  - `[ns_zhouyi_556]` `[trigger: 卦=中孚 AND 六三=得敌或鼓或罢]` `[factor_trigger: zhouyi_gua_zhongfu]` `[role: 例外处理]` 得敌，或鼓或罢：遇敌而进退不定。 → 《周易·中孚卦·爻辞》
  - `[ns_zhouyi_557]` `[trigger: 卦=中孚 AND 六四=月几望]` `[factor_trigger: zhouyi_gua_zhongfu]` `[role: 条件分支]` 月几望，马匹亡：月将满，马匹失。 → 《周易·中孚卦·爻辞》
  - `[ns_zhouyi_558]` `[trigger: 卦=中孚 AND 九五=有孚挛如]` `[factor_trigger: zhouyi_gua_zhongfu]` `[role: 主干依赖]` 有孚挛如，无咎：诚信相系，无所咎责。 → 《周易·中孚卦·爻辞》
  - `[ns_zhouyi_559]` `[trigger: 卦=中孚 AND 上九=翰音登于天]` `[factor_trigger: zhouyi_gua_zhongfu]` `[role: 总结]` 翰音登于天，贞凶：鸡鸣登天，守正亦凶。 → 《周易·中孚卦·爻辞》
  - **中文**：
  - 卦辞"中孚：豚鱼吉，利涉大川，利贞"依通行王弼本；"中孚"谓内心诚信，"豚鱼"为微物，诚信可感化微物。
  - "泽上有风"谓巽风在兑泽之上，风感水动，象征诚信之感通力量。
  - "虞吉"之"虞"释为安虞、预备，有备则吉；"有它不燕"之"燕"释为安宁，有变则不安。
  - "鸣鹤在阴，其子和之"以鹤鸣子应喻诚信之感召，声气相通则有应。
  - "翰音登于天"之"翰音"释为鸡鸣，鸡鸣本非可登天之物，过度张扬，守正亦凶。
  - "月几望，马匹亡"中"几望"为将满未满，时机临界；"马匹亡"或释为配偶失去。
  - **English**: Based on Wang Bi commentary edition. "中孚" means inner sincerity. "豚鱼" (pig and fish) are humble creatures—sincerity can move even them. "鸣鹤/翰音" contrast proper vs improper expression of sincerity. "月几望" indicates critical timing."""
    normalized_text_zh: str = """"""
    subject: str = "中孚卦（䷼）"
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_中孚卦_001_L1",
    )
    version: str = "1.0.0"
