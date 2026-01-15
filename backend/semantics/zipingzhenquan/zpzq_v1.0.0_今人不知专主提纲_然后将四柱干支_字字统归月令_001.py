"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523909
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
    semantic_id="zpzq_v1.0.0_今人不知专主提纲_然后将四柱干支_字字统归月令_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 今人不知专主提纲然后将四柱干支字字统归月令(SemanticEntry):
    """
    - **原文（source_text）**：
  今人不知专主提纲，然后将四柱干支，字字统归月令，以观喜忌。甚至见正官佩印，则以为官印双全，与印绶用官者同论；见财透食神，不以为财逢食生，而以为食神生财...
    """
    
    original_text: str = """- **原文（source_text）**：
  今人不知专主提纲，然后将四柱干支，字字统归月令，以观喜忌。甚至见正官佩印，则以为官印双全，与印绶用官者同论；见财透食神，不以为财逢食生，而以为食神生财，与食神生财同论；见偏印透食，不以为泄身之秀，而以为枭神夺食，宜用财制，与食神逢枭同论；见煞逢食制而露印者，不为去食护煞，而以为煞印相生，与印绶逢煞者同论；更有煞格逢刃，不以为刃可帮身制煞，而以为七煞制刃，与阳刃露煞者同论。此皆由不知月令而妄论之故也。

- 原注（原文注解）：
  　　本段严厉批评几种常见错误：
  - 不以月令为提纲，反以表面配置为判格依据；
  - 误把“官印双全”与“印绶用官”一概而论；
  - 误把“财逢食生”与“食神生财”混为一谈；
  - 把“偏印透食”的泄秀看成“枭神夺食”；
  - 看见“煞逢食制而露印”，不知此为去食护煞，反说成“煞印相生”；
  - 煞格逢刃，不以为刃帮身制煞，反说成“七煞制刃”。

- 分字分词释义：
  - 专主提纲：以月令为纲领，统摄全局判断。
  - 字字统归月令：把四柱所有干支都回到“月令气机”之上来看喜忌与用神。
  - 官印双全：官星与印星同时得位。
  - 印绶用官：以印为用神，官星生印。
  - 财逢食生 vs 食神生财：前者以财为纲，食来生财；后者以食神为纲，食生财。

- **规范化释义（primary_lang_explained）**：
  论用神必须先确立月令为提纲，再将四柱干支统归月令之气来判喜忌。若不问月令，只凭表面上官印同见、财食并存、煞印相逢等名目就立格，往往会把本应作“印绶用官”的格局误当“官印双全”，把“财逢食生”混作“食神生财”，又把偏印泄秀误读成“枭神夺食”，把“煞逢食制而露印”当作“煞印相生”，甚至在煞格逢刃时，不知刃可帮身制煞，反说成“七煞制刃”。凡此皆因不以月令为纲，脱离提纲妄论格局所致。

- **完整对等诠释（secondary_lang_full）**：  
  Likewise, whenever a partial Resource appears alongside Food, many readers automatically label it "Owl seizing Food" and prescribe heavy Wealth to control it, instead of first asking whether that Resource is in fact venting and protecting the Day Master. When Killing is already being held in check by Food and Resource shows on the surface as well, they casually talk of "Killing and Resource mutually generating" and overlook that the true function here is to remove Food in order to protect the Killing pattern. When a Killing chart includes a visible Blade, they invert the logic by saying "Seven Killings controls Blade", rather than recognising that Blade can actually stand on the Day Master's side and help control Killing. All of these examples share one root error: they interpret combinations by name alone, without returning every stem and branch to the Month to see which star is actually acting as the guiding thread.

- 详细解说：
  - 真正的用神判断，必须“从月令出发”，再看官印财食煞刃等如何围绕月令运转。
  - “同样的配对，不同的提纲”会得出完全不同的结论：官印双全，在官格、印格中意义完全不同；食财同见，在财格和食格中功能也不一样。
  - 许多看起来“有名”的格局说法，若不放回月令提纲中审视，很容易变成空洞的标签.

- 核心要点：
  - 所有判断必须先问：“此局以何为提纲？”
  - 财官印食煞刃的组合，只有放在提纲之下，才有意义。
  - 不可只看“显字组合”，而忽略“月令与藏干的根本关系”。

- 应用推演：
  1) 先定月令，为全局提纲；
  2) 再看四柱干支，逐一“统归月令”：看其对月令主神是生、克、泄、耗还是护；
  3) 判断表象组合（官印、财食、煞印、刃煞等）是否与提纲所需一致；
  4) 避免直接套用书上的格名与口诀，而不看本局是否真正符合其前提条件。

- 反例与边界：
  - 看命时只凭几个“漂亮词”（官印双全、财官双美等）下判断，忽视月令与用神，易生大误。

- 小例（示意）：
  - 两命同为“官印双现”，一命月令在印、一命月令在官，前者以印为提纲、官为生印之神，后者以官为提纲、印为护官之神，断法完全不同。

- 校勘与字词辨析：
  - “劫才”一词，在此处沿用原文写法，释义统一作“劫财”。

---




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_280]` `[trigger: 命理要义]` `[factor_trigger: benjie_hexin_mingli AND lunshu_yaodian]` `[role: 主干]` 本节核心命理论述。 → 《子平真诠》#第67节
  - `[ns_zpzy_281]` `[trigger: 实践要领]` `[factor_trigger: duanming_shijian AND yaoling_zonghe]` `[role: 主干]` 断命实践要领。 → 《子平真诠》#上卷
  - `[ns_zpzy_282]` `[trigger: 边界条件]` `[factor_trigger: shiyong_tiaojian AND bianjie_xianzhi]` `[role: 条件分支]` 适用条件与边界。 → 《子平真诠》#上卷
  - `[ns_zpzy_283]` `[trigger: 病重药重]` `[factor_trigger: (bingzhong AND yaozhong) OR (bingqing AND yaoliang)]` `[role: 主干]` 病重药重，病轻药轻。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "今人不知专主提纲，然后将四柱干支，字字统归月令"
    factor_refs: list = ['zhuanzhu_tigang', 'zizi_guiyueling', 'guanyin_shuangquan', 'yinshou_yongguan', 'xiaoshen_duoshi', 'engine_id', 'tigang_first_flag', 'bazi_rule_engine', 'mingxiang_shizhi', 'bazi_rule_engine', 'shicaiyinsha_fengong', 'bazi_rule_engine', 'duanming_kekaodu', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_084', 'tigang_first_flag', 'rel_zpzq_085', 'mingxiang_shizhi', 'evi_zpzq_084', 'tigang_first_flag', 'rule_tigang_first', 'evi_zpzq_085', 'mingxiang_shizhi', 'rule_mingshi_qubie', 'concept_anchor', 'concept_name_vs_reality']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_今人不知专主提纲_然后将四柱干支_字字统归月令_001_L1",
    )
    version: str = "1.0.0"
