"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436555
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
    semantic_id="smth_v1.0.0_福寿两备格与中和长久_001",
    book_id="sanming",
    engine_id="bazi"
)
class 福寿两备格与中和长久(SemanticEntry):
    """
    - 原文（source_text）：

  福寿两备。

  夫福寿两备者，造化之中和，格局之纯粹也。有享用一生，永锡难老，若此者何？乃身坐旺乡，通于月气，支干相辅，更带财官印绶，各得其位，不行脱财、...
    """
    
    original_text: str = """- 原文（source_text）：

  福寿两备。

  夫福寿两备者，造化之中和，格局之纯粹也。有享用一生，永锡难老，若此者何？乃身坐旺乡，通于月气，支干相辅，更带财官印绶，各得其位，不行脱财、坏印、伤官之局，尤喜食神、天厨。若身旺而运行财食之乡，此皆福寿两备之命也。如一命：丙午、庚子、辛酉、癸巳，辛坐酉支，专禄自旺。时癸归禄于子为食神，寿星、子星得地。辛用丙火为官，丙禄归于巳，为夫星得地。又十一月生，人乃金白水清之象，兼支干上下相辅，俱无伤损，身不从化，故主为人美貌端正，夫子相停，福寿两备也，余仿此推。

- 分字分词释义：

  - **福寿两备**：福分与寿命皆较充足，兼顾生活质量与生命长度。
  - **造化之中和，格局之纯粹**：五行气机不偏不倚、结构清晰，是福寿得以并存的关键。
  - **身坐旺乡，通于月气**：日主得旺地，又与月令相通，根基稳固。
  - **财官印绶各得其位**：财、官、印等吉神分布得宜，不互相冲破。
  - **不行脱财、坏印、伤官之局**：行运不大幅破坏原有优势结构。

- **规范化释义（primary_lang_explained）**：

  “福寿两备格”是对一种**整体中和、结构纯粹**命局的称呼：

  - 日主有根有气，又不至于过旺；
  - 财、官、印与食神、天厨各居其位，相互配合，少见严重刑冲克害；
  - 行运多能顺着原有优势发展，而不是频繁破坏根基。

  原例中，辛金专禄自旺，丙火官星得地，癸水食神得禄，支干上下相辅，形成“金白水清”的清润之象，因此被视为“福寿两备”。

- **完整对等诠释（secondary_lang_full）**：

  This configuration shows a life built on clear structure and gentle balance. The Day Master stands in its own lü with solid roots, while Wealth, Officer and Seal each occupy fitting places and support one another without mutual damage. Food God or Heavenly Kitchen adds comfort, nourishment and everyday enjoyment. With few harsh clashes or destructive combinations, the chart describes conditions in which both outer circumstances and inner resources can sustain a long, reasonably steady unfolding.

  In the example, Xin Metal is rooted in You, Bing Fire as Officer and Gui Water as Food each gain appropriate strength, and the overall image of "pure Metal and clear Water" suggests clarity, refinement and lack of heavy pollution. This does not promise a life free of challenge, but it does indicate that when difficulties appear, there is enough resilience, support and opportunity to recover. Read today, a "Fortune and Longevity Both Present" pattern invites conscious cultivation of balance—in health, relationships and work—so that the structural potential of the chart can translate into a stable, well‑resourced old age.

- 核心要点：

  - 中和、清纯的结构是福寿并重的基础。
  - 身有根气，财官印食各得其位，行运不大破格局。
  - 女命中还特别强调“夫子相停”，即伴侣与子女两端亦较平衡。

- 详细解说：

  1. **中和之贵**  
     - 五行不偏不倚，比极端贵格更有利于身心长期稳定；  
     - 结构清洁、少煞少冲，比起一时显赫，更接近“善终”的意象。

  2. **行运与原局的和谐**  
     - 原局虽好，若行运反复脱财坏印，亦难长期安稳；  
     - 福寿两备格强调行运与本局在大体方向上互相成就。

  3. **现代理解**  
     - 可理解为：身心资源、家庭资源与社会资源分配相对均衡；  
     - 命主人格、健康、关系与事业多能维持长期的稳态，而非暴起暴落。

- 校勘与字词辨析：

  - “永锡难老”等语，是古代祝辞式表达，本稿在白话中仅以“长期安稳、老年有养”来呈现。
  - “金白水清”一语在前卷已有专门讨论，此处仅保留为清润格局之象，不再赘述。
  - **English**：
    - Represents clear-smooth pattern image; no further elaboration.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_061]` `[trigger: 福寿两备定义]` `[factor_trigger: fushou_liangbei_ge]` `[role: 主干]` 福寿两备。 → 《三命通会》卷七#福寿两备
  - `[ns_smth_07_062]` `[trigger: 中和纯粹]` `[factor_trigger: zaohua_zhonghe AND geju_chuncui]` `[role: 主干依赖]` 造化之中和，格局之纯粹也。 → 《三命通会》卷七#福寿两备
  - `[ns_smth_07_063]` `[trigger: 财官印得位]` `[factor_trigger: shen_zuo_wangxiang AND caiguanyin_gedeqiwei]` `[role: 条件分支]` 乃身坐旺乡，通于月气，支干相辅，更带财官印绶，各得其位。 → 《三命通会》卷七#福寿两备
  - `[ns_smth_07_064]` `[trigger: 福寿两备]` `[factor_trigger: fushou_liangbei]` `[role: 总结]` 故主为人美貌端正，夫子相停，福寿两备也。 → 《三命通会》卷七#福寿两备"""
    normalized_text_zh: str = """"""
    subject: str = "福寿两备格与中和长久"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_102', 'bazi_semantic', 'bazi_state_factor_356', 'bazi_semantic', 'bazi_factor_13', 'bazi_semantic', 'bazi_state_zi_degree', 'bazi_semantic', 'source_ref', 'rel_smth_07_043', 'jiegou_zhonghe', 'rel_smth_07_044', 'xingyun_xiehe', 'rel_smth_07_045', 'fuzi_xiangting', 'evi_smth_07_043', 'jiegou_zhonghe', 'rule_fushou', 'evi_smth_07_044', 'xingyun_xiehe', 'rule_caishi', 'evi_smth_07_045', 'fuzi_xiangting', 'rule_xiangting', 'map_smth_07_029', 'map_smth_07_030']
    
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
        l1_anchor="smth_v1.0.0_福寿两备格与中和长久_001_L1",
    )
    version: str = "1.0.0"
