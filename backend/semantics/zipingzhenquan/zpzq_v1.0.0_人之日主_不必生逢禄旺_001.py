"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523704
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
    semantic_id="zpzq_v1.0.0_人之日主_不必生逢禄旺_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 人之日主不必生逢禄旺(SemanticEntry):
    """
    - **原文（source_text）**：
  人之日主，不必生逢禄旺，即月令休囚，而年日时中，得长禄旺，便不为弱；就使逢库，亦为有根。时产谓投库而必冲者，俗书之谬也；但阳长生有力，而阴长生不甚有力...
    """
    
    original_text: str = """- **原文（source_text）**：
  人之日主，不必生逢禄旺，即月令休囚，而年日时中，得长禄旺，便不为弱；就使逢库，亦为有根。时产谓投库而必冲者，俗书之谬也；但阳长生有力，而阴长生不甚有力，然亦不弱。若是逢库，则阳为有根，而阴为无用。盖阳大阴小，阳得兼阴，阴不能兼阳，自然之理也。

- 原注（原文注解）：
  　　此段将“生旺墓绝”的理论落实到实际判命上，纠正坊间几个常见误解：
  1）不必拘泥“生于禄旺”才算身强；
  2）入墓不必一律视为坏；
  3）所谓“时上入库必需刑冲开库”之说，多属俗解。

- 分字分词释义：
  - 日主：以日干为命局之主。
  - 月令休囚：月令上日主气弱、不得令。
  - 年日时中得长禄旺：在年支、日支、时支等处得长生、禄位、旺地。
  - 逢库：入墓、入库之地，如辰戌丑未等。
  - 时产谓投库而必冲者：坊间所谓“时柱入库，必须以刑冲开库”之说。
  - 阳长生有力，阴长生不甚有力：阳干的长生之地力量较足，阴干稍逊，但也不算弱。
  - 阳得兼阴，阴不能兼阳：阳气可摄阴，阴气难兼阳，喻力量包容度不同。

- **规范化释义（primary_lang_explained）**：
  论一个人的日主强弱，不必死着着“出生月份是否在禄旺之地”。即便日主在月令上是休囚的，只要在年、日、时等其他位置上还得了长生、禄位或旺地，就不能轻易说它弱；即使入了“库”，也仍旧算是有根，不必因为“入墓”就武断判为不吉。俗书中常说“时上入库者，必须以刑冲开库”，这是很大的误解。作者指出：阳干在长生之地，一般力量较足；阴干在长生之地，力量虽稍弱一些，但也并非就无根无力。真正要小心的是：如果恰好逢“库”，阳干仍可视为有根，而阴干在此处则往往难以发挥作用。原因在于：阳大阴小，阳气可以兼摄阴气，而阴气却很难反过来统摄阳气，这是自然之理。

- **完整对等诠释（secondary_lang_full）**：  
  This paragraph brings the life-cycle theory down to practical judgement of strength. The power of the Day Master cannot be decided solely by asking whether it was born in a month of prosperity or stipend. Even if the month branch leaves the stem in a weak state, the chart may still have solid support if the year, day or hour branches hold its life, stipend or prosperous positions. A branch that serves as a "storehouse" or "tomb" for the stem still counts as a place where its qi is rooted and preserved rather than destroyed. Popular manuals sometimes claim that when the hour pillar falls into such a storehouse it must always be broken open by clashes and punishments, but the author calls this a vulgar error. In general, a yang stem in its birth position has considerable force; a yin stem in its birth position is somewhat lighter, but still not without strength. When a storage position is involved, a yang stem buried there can often be treated as having usable roots, whereas a yin stem in the same place is more likely to be shut away and hard to mobilise. The underlying principle is that yang is broad and encompassing and can carry yin along with it, while yin is small and cannot easily command yang. In assessment we must therefore look at the whole pattern of roots across the four pillars, and treat tomb positions as potential reserves whose usefulness depends on context, not as automatic misfortune that has to be smashed open.

- 详细解说：
  - 身强身弱不能只看月令一处，也要看年、日、时其他支上的根气分布。
  - “入库/入墓”未必就是坏，关键在于是否有后续生化与通关，以及在全局中担任什么角色。
  - 阳干与阴干在“得根”的意义上有差异：阳根更易发挥，阴根有时虽然存在，却未必足以支撑格局用法。

- 核心要点：
  - 判断身强弱：月令为纲，但不能抹杀其他支上的禄旺与长生。
  - 对待“入库入墓”：以“有根/无根、有用/无用”来看，而不是机械视为凶象。
  - 阳干得长生、入库，多可视为有根；阴干则需更谨慎审查是否真的发挥作用。

- 应用推演：
  1) 先看月令：判断日主在月令上是得令还是休囚。
  2) 再查年、日、时支：有无长生、禄旺或通根之地。
  3) 对入库位置，区分阳干与阴干：阳干入库多视为根重，阴干入库需看是否真能通透发挥。
  4) 结合干支配合，看这些根是否真正“在用”，还是虽有其名而无其力。

- 反例与边界：
  - 一见“月令休囚”便断弱身，忽略其他根气，导致取用失误。
  - 机械地“逢库必冲”，导致在实务中乱求刑冲，反破本局调和。

- 小例（示意）：
  - 甲日生酉月，月令金旺木弱，但年支寅、时支辰，皆通甲根；若再有印生，甲木并不是真弱。
  - 乙日生戌月，乙根入库而无其他木根，且局中又多金克木，此时“有库”但未必有用，当慎论其强弱。

- 校勘与字词辨析：
  - “时产谓投库而必冲者”：各本大致如此，今按义解为“坊间常说，时柱入库者必需刑冲开库”，作者明言为谬说。


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_181]` `[trigger: 格局高低]` `[factor_trigger: geju_level IN (gao, di) AND (gao_zhe_yongshen_youli) AND (di_zhe_yongshen_wuqi)]` `[role: 主干]` 格局有高有低，高者用神有力，低者用神无气。 → 《子平真诠·论用神格局高低》#高低
  - `[ns_zpzy_182]` `[trigger: 高低之辨]` `[factor_trigger: geju_gaodi AND zaihu_yongshen_qingzhuo]` `[role: 主干]` 格局高低，在乎用神清浊。 → 《子平真诠·论用神格局高低》#清浊
  - `[ns_zpzy_183]` `[trigger: 高格条件]` `[factor_trigger: yongshen_deling=true AND yongshen_dedi=true AND yongshen_deshi=true AND result=gaoge]` `[role: 主干]` 用神得令得地得势，三者兼备为高。 → 《子平真诠·论用神格局高低》#条件
  - `[ns_zpzy_184]` `[trigger: 低格可救]` `[factor_trigger: geju_sui_di AND yun_neng_tixie AND result=ke_zhuangao]` `[role: 主干]` 格局虽低，运能提携则可转高。 → 《子平真诠·论用神格局高低》#可救
  - `[ns_zpzy_185]` `[trigger: 透干为用]` `[factor_trigger: tougan_weiyong AND liliang_xianzhu]` `[role: 主干]` 透干为用，力量显著。 → 《子平真诠》#上卷
  - `[ns_zpzy_186]` `[trigger: 用神为纲]` `[factor_trigger: bazi_yongshen AND zhuanqiu_yueling]` `[role: 主干]` 八字用神，专求月令。 → 《子平真诠》#论用神
  - `[ns_zpzy_187]` `[trigger: 月令司权]` `[factor_trigger: yueling_siquan AND tigang_zhi_fu]` `[role: 主干]` 月令司权，提纲之府。 → 《子平真诠》#论用神
  - `[ns_zpzy_188]` `[trigger: 用神取法]` `[factor_trigger: yongshen_qufa AND yi_yueling_wei_zhu]` `[role: 主干]` 用神取法，以月令为主。 → 《子平真诠》#论用神
  - `[ns_zpzy_189]` `[trigger: 失令无力]` `[factor_trigger: shiling_zhi_gan AND xu_de_shengfu]` `[role: 主干]` 失令之干，须得生扶。 → 《子平真诠》#上卷
  - `[ns_zpzy_190]` `[trigger: 身旺任财]` `[factor_trigger: shenwang=true AND fang_neng_ren_caiguan]` `[role: 主干]` 身旺方能任财官。 → 《子平真诠》#上卷
  - `[ns_zpzy_191]` `[trigger: 用神无力]` `[factor_trigger: yongshen_wuli=true AND result=pinjian_nanmian]` `[role: 主干]` 用神无力，贫贱难免。 → 《子平真诠》#上卷
  - `[ns_zpzy_192]` `[trigger: 年柱根基]` `[factor_trigger: pillar=nian AND role=genji_zuye]` `[role: 主干]` 年柱根基，祖业之宫。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "人之日主，不必生逢禄旺"
    factor_refs: list = ['shenqiang_shenruo', 'yueling_xiuqiu', 'tonggen', 'ruku', 'fengku_bichong', 'yang_de_jianyin', 'sizhu_genqi']
    
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
        l1_anchor="zpzq_v1.0.0_人之日主_不必生逢禄旺_001_L1",
    )
    version: str = "1.0.0"
