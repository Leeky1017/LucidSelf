"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492103
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
    semantic_id="zpzq_v1.0.0_行运与看命同理_以喜忌为总纲_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 行运与看命同理以喜忌为总纲(SemanticEntry):
    """
    - **原文（source_text）**：
  二十五、论行运。
  论运与看命无二法也。看命以四柱干支，配月令之喜忌，而取运则又以运之干，配八字之喜忌。故运中每运行一字，即必以此一字，配命中干支而...
    """
    
    original_text: str = """- **原文（source_text）**：
  二十五、论行运。
  论运与看命无二法也。看命以四柱干支，配月令之喜忌，而取运则又以运之干，配八字之喜忌。故运中每运行一字，即必以此一字，配命中干支而统观之，为喜为忌，吉凶判然矣。

  何为喜？命中所喜之神，我得而助之者是也。如官用印以制伤，而运助印；财生官而身轻，而运助身；印带财以为忌，而运劫财；食带煞以成格，身轻而运逢印，煞重而运助食；伤官佩印，而运行官煞；阳刃用官，而运助财乡；月劫用财，而运行伤食。如此之类，皆美运也。

  何谓忌？命中所忌，我逆而施之者是也。如正官无印，而运行伤；财不透食，而运行煞；印绶用官，而运合官；食神带煞，而运行财；七煞食制，而运逢枭；伤官佩印，而运行财；阳刃用煞，而运逢食；建禄用官，而运逢伤。如此之类，皆败运也。

  其有似喜而实忌者，何也？如官逢印运，而本命有合，印逢官运，而本命用煞之类是也。

  有似忌而实喜者，何也？如官逢伤运，而命透印，财行煞运，而命透食之类是也。

  又有行干而不行支者，何也？如丙生子月亥年，逢丙丁则帮身，逢巳午则相冲是也。

  又有行支而不行干者，何也？如甲生酉月，辛金透而官犹弱，逢申酉则官植根，逢庚辛则混煞重官之类是也。

  又有干同一类而不两行者，何也？如丁生亥月，而年透壬官，逢丙则帮身，逢丁则合官之类是也。

  又有支同一类而不两行者，何也？如戊生卯月，丑年，逢申则自坐长生，逢酉则会丑以伤官之类是也。

  又有同是相冲而分缓急者，何也？冲年月则急，冲日时则缓也。

  又有同是相冲而分轻重者，何也？运本美而逢冲则轻，运既忌而又冲则重也。

  又有逢冲而不冲，何也？如甲用酉官，行卯则冲，而本命巳酉相会，则冲无力；年支亥未，则卯逢年会而不冲月官之类是也。

  又有一冲而得两冲者，何也？如乙用申官，两申并而不冲一寅，运又逢寅，则运与本命，合成二寅，以冲二申之类是也。

- 原注（原文注解）：
  　　本章是全书行运部分的总纲：**行运的判断方法，与看命本身并无二致，仍以“喜忌用神”为唯一核心。**
  - 第一段总论：
    - 看命：以四柱干支配月令之喜忌来定格局和用神；
    - 取运：则以“运之天干、地支”分别去配命局喜忌；
    - 每一运（每一干支）进入命局，都要视作新增一字，与原有八字全面互动，再判吉凶。
  - 接着分两类说明“何为喜、何谓忌”：
    - 喜：命中所喜之神，被运来扶助、补足短板；
    - 忌：命中所忌之神，被运来强化，或运来破坏命局原有平衡。
  - 中段列举数种典型“喜运”组合：
    - 官用印制伤，而运助印；
    - 财生官而身轻，运助身；
    - 印带财为忌，运来劫财以去其病；
    - 食带煞成格，身轻则运逢印，煞重则运助食；
    - 伤官佩印而运遇官煞；
    - 阳刃用官而运助财乡；
    - 月劫用财而运行伤食。
    这些都体现一个原则：**运来之字，能成全本局用神之需**，则为美运。
  - 又列举数种“忌运”组合：
    - 正官无印而运行伤官；
    - 财不透食而运行七煞；
    - 印绶用官而运来合官；
    - 食神带煞而运行财；
    - 七煞食制而运逢枭；
    - 伤官佩印而运行财；
    - 阳刃用煞而运逢食；
    - 建禄用官而运逢伤。
    共同点在于：**运来之字，正好加强命局之病或破坏原有的制衡。**
  - 随后又提出几种“似喜实忌、似忌实喜”的微妙情况，以及“只行干不行支、只行支不行干”“同类不两行”“冲有缓急轻重”等条目，说明：
    - 行运判断不能只看表面“字面配合”，还要看命局原有的合、会、根、局与轻重缓急。

- 分字分词释义：
  - 行运：大运、流年等时序推移所加之干支。
  - 喜忌：命局所喜之神与所忌之神，依据格局与用神体系判定。
  - 我得而助之：对我方格局有帮助，填补需要。
  - 逆而施之：与命局需要相反，反向加重病处。
  - 行干不行支：行运只起天干之作用，地支效应较弱或被合会抵消。
  - 行支不行干：行运只起地支之作用，天干效应弱。
  - 同类不两行：某类字在行运中不宜重复叠加，以免过与不及。
  - 冲之缓急：冲年月者急，冲日时者缓。
  - 冲之轻重：本为美运而逢冲则轻，本已为忌而又逢冲则重。
  - 逢冲不冲：虽有冲字，但因会合、格局等原因，冲力被卸减或转移。
  - 一冲两冲：一支之冲，因本命与行运合化，反而形成两处被冲之格局。

- **规范化释义（primary_lang_explained）**：
  本章核心观点只有一句：**行运之法，与看命完全相同，都是围绕“用神喜忌”打转，只不过行运好比在既有八字上，不断添一笔干支，看它如何与原局互动。**

  首先，何为“喜运”？
  - 命局本来就需要某种力量（如用印制伤、用身承财官、用劫制财等），运来恰好补足这一点：
    - 官用印制伤，印为关键，运助印则伤得制而官得清；
    - 财生官而身轻，运助身则承载力增强；
    - 印带财为忌（财来坏印），运来劫财反而去病；
    - 食带煞成格，身轻宜印、煞重宜食，运来各自所需；
    - 伤官佩印，运来官煞可成“伤官见官，有印能化”的妙局；
    - 阳刃用官，运助财以生官；
    - 月劫用财，运行伤食以生财。

  其次，何为“忌运”？
  - 命局原本忌某种力量，而运又来进一步推进这种力量，或破坏原有制衡：
    - 正官无印，最忌伤官，再行伤运则官伤而贵失；
    - 财不透食，本已难以通关，若又行煞运则煞夺财；
    - 印绶用官，官为印用，运来合官，反成“夺官坏印”；
    - 食神带煞，本要以食制煞，若行财运则变为财助煞；
    - 七煞食制，本靠食神制煞，若运逢枭印则枭夺食，制煞之力消失；
    - 伤官佩印，若运行财，则财来克印、助伤，坏事居多；
    - 阳刃用煞，若运逢食，则食泄煞力，刃煞失衡；
    - 建禄用官，行伤则官受克，难为贵格。

  再者，作者强调行运判断的细腻之处：
  - 有的看似喜而实忌：
    - 如官逢印运，本应印生助官，但若命局中官印有合、用煞为主，则此印运反而扰乱格局；
  - 有的看似忌而实喜：
    - 官逢伤运，若命透印则“伤官见官，有印化伤”，反成历练之机；
    - 财行煞运，若命透食则“食神制煞”，反成权柄与担当。

  最后，作者列举一系列“干支行运差异”的例子：
  - 行干不行支、行支不行干，说明有时只是天干之象作用明显，支象被合会或藏伏；
  - 同类不两行，强调“过犹不及”，如官已透，行同类官运反致混杂或合官；
  - 相冲分缓急与轻重，说明冲动的时间与程度不同，对命局影响也不同；
  - 有时逢冲而不冲，因本命已有会合，使冲力转移或被缓冲；
  - 有时一冲成两冲，因本命与运合成新局，共同冲击另一方.

- **完整对等诠释（secondary_lang_full）**：  
  Luck periods are judged by exactly the same logic as reading the natal chart: each incoming stem–branch is treated as a new character dropped onto the fixed four pillars, and we watch how it interacts with the existing pattern. A period is truly favourable only when it strengthens the useful gods, fills real weaknesses and restores balance; it is unfavourable when it amplifies already excessive forces, cuts off medicines, or disturbs a structure that was previously in good order.

  What looks like a good period on the surface can prove harmful once placed back into the full configuration, and what appears dangerous can become constructive when there are strong counter-balances. An Officer period may spoil the chart if it entangles existing combinations, while a Hurting Officer or Killing period may become a proving ground if robust Printing is present to transform it. Likewise stems and branches, clashes and combinations, differ in speed and depth: stems act quickly and visibly, branches work more slowly through roots and gatherings; a light clash on top of a sound pattern may only cause surface ripples, whereas the same clash hitting a precarious structure can concentrate and expose long-hidden problems. All of this serves to show that timing never replaces structure: it only magnifies what is already latent in the natal chart.

- **详细解说**：
  - 行运并非“另起一套算法”，而是**在同一命理体系中加入时间维度**：
    - 用神喜忌不变，只是“有没有人来帮它或坏它”；
    - 运的作用是动态调节“力量平衡”，而不是简单加分或减分.
  - “似喜实忌、似忌实喜”指出：
    - 行运不能只看符号（如“伤官运一定凶”“财运一定好”）；
    - 必须看这个运与命局中的结构关系：是否强化病处、是否扶助用神、是否触发潜在格局变化.
  - 干支差异与冲合轻重的讨论，则提醒我们：
    - 命理本质是“结构+次序+力度”的综合系统；
    - 同一个字，在不同位置、不同组合中，表现会完全不同.

- **校勘与字词辨析（双语）**：
  - **中文**：本稿据通行本，经文用字保持原貌，标点现代化处理。
  - **English**: Based on standard edition. Original text preserved, punctuation modernized.

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_420]` `[trigger: 杂格论]` `[factor_trigger: zage_bianhua_duoduan AND xu_shen_zhenwei]` `[role: 主干]` 杂格变化多端，须审真伪。 → 《子平真诠》#下卷第47章
  - `[ns_zpzy_421]` `[trigger: 运程喜忌]` `[factor_trigger: (yun_xi AND result=ji) OR (yun_ji AND result=xiong)]` `[role: 主干]` 运喜则吉，运忌则凶。 → 《子平真诠》#下卷
  - `[ns_zpzy_422]` `[trigger: 伤官之忌]` `[factor_trigger: shangguan_jianguan AND weihuo_baiduan]` `[role: 主干]` 伤官见官，为祸百端。 → 《子平真诠》#下卷
  - `[ns_zpzy_423]` `[trigger: 行运喜忌]` `[factor_trigger: (xingyun_xi AND result=ji) OR (xingyun_ji AND result=xiong)]` `[role: 主干]` 运喜则吉，运忌则凶。 → 《子平真诠》#下卷
  - `[ns_zpzy_424]` `[trigger: 运能成格]` `[factor_trigger: yun_neng_cheng_ge AND geju_yugao]` `[role: 主干]` 运能成格，格局愈高。 → 《子平真诠》#下卷
  - `[ns_zpzy_425]` `[trigger: 运助格局]` `[factor_trigger: yun_zhu_geju AND fugui_jiabei]` `[role: 主干]` 运助格局，富贵加倍。 → 《子平真诠》#下卷
  - `[ns_zpzy_426]` `[trigger: 运破格局]` `[factor_trigger: yun_po_geju AND huohuan_linmen]` `[role: 主干]` 运破格局，祸患临门。 → 《子平真诠》#下卷
  - `[ns_zpzy_427]` `[trigger: 正官格运]` `[factor_trigger: zhengguan_ge AND xi_yin_cai_yun]` `[role: 主干]` 正官格喜印财运。 → 《子平真诠》#下卷
  - `[ns_zpzy_428]` `[trigger: 财格行运]` `[factor_trigger: cai_ge AND xi_shishang_shengcai_yun]` `[role: 主干]` 财格喜食伤生财运。 → 《子平真诠》#下卷
  - `[ns_zpzy_429]` `[trigger: 命局组合]` `[factor_trigger: mingju_zuhe AND jiongxiong_zixian]` `[role: 主干]` 命局组合，吉凶自现。 → 《子平真诠》#下卷
  - `[ns_zpzy_430]` `[trigger: 格成格破]` `[factor_trigger: (gecheng=true AND result=ji) OR (gepo=true AND result=xiong)]` `[role: 主干]` 格成则吉，格破则凶。 → 《子平真诠》#下卷
  - `[ns_zpzy_431]` `[trigger: 日主强弱]` `[factor_trigger: rizhu_qiangruo AND ding_geju_zhi_ji]` `[role: 主干]` 日主强弱，定格局之基。 → 《子平真诠》#下卷
  - `[ns_zpzy_432]` `[trigger: 真神假神]` `[factor_trigger: (zhenshen_deyong AND geju_qing) OR (jiashen_hunza AND geju_zhuo)]` `[role: 主干]` 真神得用格局清，假神混杂格局浊。 → 《子平真诠》#下卷
  - `[ns_zpzy_433]` `[trigger: 清浊分辨]` `[factor_trigger: (qingqi_weishang) AND (zhuoqi_weixia) AND guijian_youci_fen]` `[role: 条件分支]` 清气为上浊气为下，贵贱由此分。 → 《子平真诠》#下卷"""
    normalized_text_zh: str = """"""
    subject: str = "行运与看命同理：以喜忌为总纲"
    factor_refs: list = ['xingyun', 'dayun', 'liunian', 'xiyun', 'jiyun', 'engine_id', 'yongshen_dingmao', 'bazi_rule_engine', 'yunbu_ganzhi', 'bazi_rule_engine', 'yun_sizhu_peidui', 'bazi_rule_engine', 'xiji_pingheng', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_130', 'yongshen_dingmao', 'rel_zpzq_131', 'yunbu_ganzhi', 'evi_zpzq_117', 'yongshen_dingmao', 'rule_lunyun_fangfa', 'evi_zpzq_118', 'xiyun', 'rule_xiyun_shibie', 'concept_timing', 'concept_amplification']
    
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
        l1_anchor="zpzq_v1.0.0_行运与看命同理_以喜忌为总纲_001_L1",
    )
    version: str = "1.0.0"
