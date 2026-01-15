"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523632
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
    semantic_id="zpzq_v1.0.0_然以五行而统论之_则水木相生_金木相克_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 然以五行而统论之则水木相生金木相克(SemanticEntry):
    """
    - **原文（source_text）**：
  然以五行而统论之，则水木相生，金木相克。以五行之阴阳而分配之，则生克之中，又有异同。此所以水同生木，而印有偏正；金同克木，而局有官煞也。印绶之中，偏正...
    """
    
    original_text: str = """- **原文（source_text）**：
  然以五行而统论之，则水木相生，金木相克。以五行之阴阳而分配之，则生克之中，又有异同。此所以水同生木，而印有偏正；金同克木，而局有官煞也。印绶之中，偏正相似，生克之殊，可置勿论；而相克之内，一官一煞，淑慝判然，其理不可不细详也。

- 原注（原文注解）：
  　　此段由四时相生相克转入具体五行关系，特别指出：同是水生木，却有正印、偏印之别；同是金克木，却有官、煞之分。印之偏正，可以暂且不论；官煞之内，淑与慝、善与凶、贵与险，却必须细加辨析。

- 分字分词释义：
  - 统论：从整体上、概括地说。
  - 水木相生：水能生木，为印生身之象。
  - 金木相克：金能克木，为官杀克身之象。
  - 五行之阴阳而分配：把每一行再分阴阳，如壬癸水、甲乙木、庚辛金等。
  - 印有偏正：正印与偏印（枭印）之别。
  - 局有官煞：同属克身的金，对日主却可能是正官，也可能是七煞。
  - 印绶：印星，正印；偏印常称“枭”。
  - 偏正相似：偏印与正印在表面功能上相似，都是生身、助身。
  - 一官一煞：同一类五行克来之象，一为官、一为煞，性质差异极大。
  - 淑慝判然：淑善与凶恶泾渭分明。

- **规范化释义（primary_lang_explained）**：
  前一节从四季之运讲“生与克同功”，这一节则从具体五行着手。总体来看，水生木、金克木，这是人人都知道的。但如果考虑到水、木、金各自内部还有阴阳之分，情况就复杂起来了：同是水生木，有的形成“正印”，有的则形成“偏印”；同是金克木，有的是“正官”，有的则是“七煞”。印星中，偏印与正印在功能上相似，都是生扶日主之气，二者差别虽有，却不急于在此展开；可是在“克”的一边，正官与七煞的性质却截然不同——一个代表中正之权，一个代表偏激之力，吉凶与成败的差别非常大，因此必须格外仔细地分辨。

- **完整对等诠释（secondary_lang_full）**：  
  The previous passage showed, by means of the seasons, that generating and controlling forces work together. Here the focus narrows to specific Five-Element relationships. Taken in broad strokes, everyone knows that Water generates Wood and Metal controls Wood. But once we remember that each element itself divides into yin and yang, the picture becomes more intricate. When Water generates Wood, it may appear as a proper Resource star that steadily nourishes the Day Master, or as an indirect Resource whose help comes in more skewed, eccentric or unstable forms. When Metal controls Wood, it may appear as a Direct Officer, representing rightful authority and orderly restraint, or as Seven Killings, representing more aggressive, dangerous, and anxiety-producing pressures. Among the Resource stars, the distinction between proper and indirect can be deferred because both essentially nourish and support the self. Among the controlling stars, however, the line between Officer and Killing must be drawn very carefully: one tends toward legitimate, stabilizing power, the other toward volatility and risk. Much of the later discussion of officer and killing patterns rests on this point: first affirm the basic fact that Metal controls Wood, then differentiate sharply within that control between what is upright and what is excessive.

- 详细解说：
  - 单靠“五行相生相克”的表层知识是不足以断命的，必须深入到“同一类五行内部的阴阳差异”。
  - 印星之偏正，虽然重要，但本质上都属“生扶日主”；官与煞则直接关系到权力的合法性与凶险程度，属于性质差异极大的两端，所以作者强调“理不可不细详”。
  - 后文大量关于官煞格局的论述，都以此为基点：先承认“金克木”，再在“官/煞”之间做精细切分。

- 核心要点：
  - 同行不同性：同一水生木、金克木，在阴阳层面拆开看，会变成正印/偏印、正官/七煞等不同角色。
  - 生中之别轻于克中之别：印的偏正之别，可以稍后细论；官煞一线，则必须先分清，否则吉凶易倒置。
  - 阴阳细分是“格局精度”的来源，不分则只能粗看格局，难入精微。

- 应用推演：
  1) 先按五行粗看：谁生身、谁克身，得出一个大致图景（印、官杀、比劫、财等）。
  2) 再按阴阳细分：如壬/癸、甲/乙、庚/辛，区分正印/枭印、正官/七煞。
  3) 权衡轻重：印之偏正可后看，官煞必须先分；在用神与格局判断中，把官煞区分视为优先步骤。

- 反例与边界：
  - 把一切“克身之金”一概视为“官星”，而不分官煞，容易把险格误判为贵格。
  - 把一切“生身之水/火/土”一概视为“印”，不分偏正，在某些关键命例中会丢失对性情与取用的精细描述。
- 小例（示意）：
  - 甲木遇庚金为官，得制有情，多主中正之权；若同为金而为辛煞，又无制伏，则偏激之象倍增。

- 校勘与字词辨析：
  - "印绶之中，偏正相似，生克之殊，可置勿论"：此处"生克之殊"指偏印与正印在具体生克细节上的差异，作者选择暂不展开，而把重点压在"官煞淑慝判然"上。

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_102]` `[trigger: 官煞分辨]` `[factor_trigger: jin_ke_mu AND (ten_god=zhengguan OR ten_god=qisha) AND shute_panran]` `[role: 例外处理]` 同是金克木，一官一煞，淑慝判然。 → 《子平真诠·论阴阳生克》#官煞分野
  - `[ns_zpzy_103]` `[trigger: 印星偏正]` `[factor_trigger: (shui_sheng_mu AND yin_you_pian_zheng) AND (jin_ke_mu AND ju_you_guan_sha)]` `[role: 主干]` 水同生木，而印有偏正；金同克木，而局有官煞。 → 《子平真诠·论阴阳生克》#阴阳细分
  - `[ns_zpzy_104]` `[trigger: 官煞优先]` `[factor_trigger: yin_pianzheng_priority=low AND guansha_bie_priority=high]` `[role: 主干]` 印之偏正可置勿论，官煞之别不可不细详。 → 《子平真诠·论阴阳生克》#判断优先级
  - `[ns_zpzy_105]` `[trigger: 阴阳互根]` `[factor_trigger: yinyang_hugen AND gangrou_xiangji]` `[role: 主干]` 阴阳互根，刚柔相济。 → 《子平真诠》#论阴阳生克
  - `[ns_zpzy_106]` `[trigger: 生克之理]` `[factor_trigger: sheng_wo_zhe=yin AND ke_wo_zhe=guansha]` `[role: 主干]` 生我者为印，克我者为官煞。 → 《子平真诠》#论阴阳生克
  - `[ns_zpzy_107]` `[trigger: 五行相生]` `[factor_trigger: wuxing_xiangsheng_sequence=(mu_huo_tu_jin_shui)]` `[role: 主干]` 木生火、火生土、土生金、金生水、水生木。 → 《子平真诠》#论阴阳生克
  - `[ns_zpzy_108]` `[trigger: 寅申冲]` `[factor_trigger: branch_chong=(yin, shen) AND jinmu_jiaozhan]` `[role: 主干]` 寅申冲，金木交战。 → 《子平真诠》#上卷
  - `[ns_zpzy_109]` `[trigger: 巳亥冲]` `[factor_trigger: branch_chong=(si, hai) AND shuihuo_xiangji]` `[role: 主干]` 巳亥冲，水火相激。 → 《子平真诠》#上卷
  - `[ns_zpzy_110]` `[trigger: 得地有根]` `[factor_trigger: dedi=true AND yougen=true AND strength=chongpei]` `[role: 主干]` 得地有根，力量充沛。 → 《子平真诠》#上卷
  - `[ns_zpzy_111]` `[trigger: 失地无根]` `[factor_trigger: dedi=false AND yougen=false AND strength=wuli]` `[role: 主干]` 失地无根，虚浮无力。 → 《子平真诠》#上卷
  - `[ns_zpzy_112]` `[trigger: 得时当令]` `[factor_trigger: deshi=true AND dangling=true AND qishi=zhengsheng]` `[role: 主干]` 得时当令，气势正盛。 → 《子平真诠》#上卷
  - `[ns_zpzy_113]` `[trigger: 旺衰定论]` `[factor_trigger: wangshuai_determined=true AND geju_clarity=ziming]` `[role: 主干]` 旺衰定论，格局自明。 → 《子平真诠》#上卷
  - `[ns_zpzy_114]` `[trigger: 病重药重]` `[factor_trigger: (bing_level=zhong AND yao_level=zhong) OR (bing_level=qing AND yao_level=qing)]` `[role: 主干]` 病重药重，病轻药轻。 → 《子平真诠》#上卷
  - `[ns_zpzy_115]` `[trigger: 干支一体]` `[factor_trigger: ganzhi_yiti=true AND analysis_mode=tongcan_helun]` `[role: 主干]` 干支一体，统参合论。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """- 甲者阳木，木之生气：甲偏重于“生气”与“行乎天”的一面。"""
    subject: str = "然以五行而统论之，则水木相生，金木相克"
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_然以五行而统论之_则水木相生_金木相克_001_L1",
    )
    version: str = "1.0.0"
