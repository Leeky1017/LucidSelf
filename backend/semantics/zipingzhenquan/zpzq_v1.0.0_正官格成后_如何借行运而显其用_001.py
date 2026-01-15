"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492241
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
    semantic_id="zpzq_v1.0.0_正官格成后_如何借行运而显其用_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 正官格成后如何借行运而显其用(SemanticEntry):
    """
    - **原文（source_text）**：
  三十二、论正官取运。
  取运之道，一八字则有一八字这论，其理甚精，其法甚活，只可大略言之。变化在人，不可泥也。

  如正官取运，即以正官所统之格分...
    """
    
    original_text: str = """- **原文（source_text）**：
  三十二、论正官取运。
  取运之道，一八字则有一八字这论，其理甚精，其法甚活，只可大略言之。变化在人，不可泥也。

  如正官取运，即以正官所统之格分而配之。正官而用财印，身稍轻则取助身，官稍轻则助官。若官露而不可逢合，不可杂煞，不可重官。与地支刑冲，不问所就何局，皆不利也。

  正官用财，运喜印受身旺之地，切忌食伤。若身旺而财轻官弱，即仍取财官运可也。

  正官佩印，运喜财乡，伤食反吉。若官重身轻而佩印，则身旺为宜，不必财运也。

  正官带伤食而用印制，运喜官旺印旺之乡，财运切忌。若印绶叠出，财运亦无害矣。

  正官而带煞，伤食反为不碍。其命中用劫合煞，则财运可行，伤食可行，身旺，印绶亦可行，只不过复露七煞。若命用伤官合煞，则伤食与财俱可行，而不宜逢印矣。

  此皆大略言之，其八字各有议论。运中每遇一字，各有研究，随时取用，不可言形。凡格皆然，不独正官也。

- 原注（原文注解）：
  　　本章是在三十一章“论正官”之后，专门讨论：**已经形成正官格局之后，行运如何配合，才能真正发挥或保护正官之用。**
  - 开首先把“取运”原则讲清：
    - “一八字则有一八字之论”：每一个命局的取运方案都是定制的；
    - “其理甚精，其法甚活”：原则精细而运用灵活，不能用死公式；
    - 因此下面的条目都只是“大略言之”，具体仍要回到个盘。

  - 对不同正官格局的取运原则，逐条归纳如下：
    1) **正官而用财印**：
       - 身稍轻 → 运上先帮身，再助官；
       - 官稍轻 → 运上先助官，再顾身；
       - 官星已经“露而可用”时：
         - 忌再逢合（合去官清）；
         - 忌杂煞（官煞混杂）；
         - 忌重官（官多反成压身之病）；
         - 又凡与地支刑冲之运，不论成何局，皆视为不利。
    2) **正官用财**：
       - 以财生官为主线；
       - 行运以“印绶与身旺之地”为佳，可以帮身承受官克；
       - 忌食神伤官之运，以防伤官败官；
       - 若本身已旺而财轻官弱，则仍可直接走财官之运，以补其不足。
    3) **正官佩印**：
       - 命局已经以印护官、护身；
       - 行运宜走财乡，以财生官印，使体系运转；
       - 反而伤食之运，多能起到“泄身而不伤官”的调节作用；
       - 若官重身轻而佩印，则更要行助身之地，不必再贪财运。
    4) **正官带伤食而用印制**：
       - 命局中伤食已见，用印以制之；
       - 行运宜官旺印旺之乡，使“官得印护而制伤”；
       - 财运反而切忌，以免财去印而护伤；
       - 若命中印绶叠出，则财运再来，亦未必有害——盖印有余力。
    5) **正官而带煞**：
       - 官煞并存的局中：
         - 若用劫合煞 → 财运、伤食运、印绶运皆可行，但要防“复露七煞”；
         - 若用伤官合煞 → 则宜行伤食与财运，不宜逢印，以免印护煞而坏官。

  - 结尾再度提醒：
    - 上述皆是“分型后的总则”；
    - 真正取运时，每逢流年、大运之干支，都要单独研究；
    - 不可见某类格局就机械套用同一运程模板。

- 分字分词释义：
  - 取运之道：如何选择大运、流年的用舍与轻重。
  - 一八字则有一八字之论：每个命局有自己的分析框架，不可一概而论。
  - 用财印：以财生官、以印护官护身的综合官格结构。
  - 官露：官星透于天干、明见可用。
  - 杂煞：七煞混入正官体系，使官煞不清。
  - 正官用财：以财生官为主、印为辅的格局重心。
  - 正官佩印：印为主、官为体，以印来维护官与身。
  - 带伤食而用印制：命中有伤官食神，通过印绶加以约束。
  - 劫合煞 / 伤官合煞：以劫财或伤官与七煞相合，用以化煞或调节煞力。

- **规范化释义（primary_lang_explained）**：
  在三十一章中，我们站在“静态命局”的角度，说明了正官格成局与否、高低如何；
  本章则转到“动态行运”的维度，回答问题：
  > 正官格已经成形之后，行运要怎么走，才是“帮忙而不捣乱”？

  可以看出几个共同的原则：
  1) **先认清命局是“财官型”还是“印官型”**：
     - 用财印 → 运上既要顾官，也要顾身；
     - 正官用财 → 重心在财官二者的补充；
     - 正官佩印 → 重心在身印的平衡。
  2) **凡有伤官、七煞参与者，行运尤其要谨慎**：
     - 用印制伤 → 喜印旺之乡；
     - 用劫合煞 → 可走财、伤、印，但需防煞再露；
     - 用伤官合煞 → 应避印运，以免印来护煞。
  3) **身轻身重，是取运时必须先判的前提**：
     - 身轻 → 先补身，再谈助官；
     - 身重 → 可直接行财官运，或以印、食调节。

- 详细解说：
  - 正官格的行运选择，其实是“如何在时间轴上维护一个秩序系统”：
    - 官是规范与权威；
    - 财是资源供给；
    - 印是合法性与支持；
    - 伤官、七煞是挑战与冲击；
    - 大运、流年相当于“外部环境”的变化。
  - 因此：
    - 好的正官运，不只是“走到官星、财星就好”，
    - 而是要看：这些运是否在“整体上”强化了秩序，还是把秩序打乱。
- **完整对等诠释（secondary_lang_full）**：  
  Choosing luck for a Proper Officer chart is essentially choosing how to maintain an order system over time. In some structures, the ideal periods are those that bring Wealth to feed the Officer and Printing to support both body and office; in others, what is needed is help for the Day Master first so that it can carry the Officer’s demands, or gentle Food and Hurting Officer to relieve excessive pressure. What all good Officer periods share is that they keep the framework clean and coherent instead of multiplying competing authorities or introducing chaotic冲刑.

  A luck period that merely passes through an Officer or Wealth sign is not automatically beneficial. We must ask whether, in the concrete structure, it tidies up杂煞, clarifies who holds power, supplies resources and legitimacy to the rightful Officer, and protects the system from destructive clashes, or whether it overloads the chart with too many officials, exposes the Officer to unchecked harms, or invites rebellion through unrestrained Hurting spirits. Seen this way, "good Officer luck" means years in which external conditions help the person play their role within a stable order, not just years when the character 官 happens to appear.

- **核心要点**：
  - 取运之道，一八字则有一八字之论，其理甚精其法甚活
  - 正官用财印：身轻取助身，官轻则助官
  - 官露不可逢合、不可杂煞、不可重官、忌地支刑冲
  - 正官用财：运喜印绶身旺之地，切忌食伤
  - 正官佩印：运喜财乡，伤食反吉
  - 正官带伤食用印制：运喜官旺印旺，财运切忌
  - 正官而带煞：用劫合煞可行财伤印运，用伤官合煞不宜逢印

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_514]` `[trigger: 正官格取运]` `[role: 主干]` `[factor_trigger: quyun_zhidao AND yibazi_youyilun]` 取运之道，一八字则有一八字之论，其理甚精，其法甚活。| 因子类型 | 因子标签（人话） | 因子ID（必填） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 结构类   | 正官格类型         | zhengguan_ge_leixing        | new_candidate | 分类轴         | 用财印 / 用财 / 佩印 / 带伤用印 / 官煞并见        | bazi_rule_engine | 取运前必须先完成的格局分型   |"""
    normalized_text_zh: str = """"""
    subject: str = "正官格成后，如何借行运而显其用"
    factor_refs: list = ['quyun_zhidao', 'yong_caiyin', 'guan_lu', 'za_sha', 'engine_id', 'shen_guan_qiangruo', 'bazi_rule_engine', 'zhengguan_quyun_type', 'bazi_rule_engine', 'guange_jinji', 'bazi_rule_engine', 'source_ref', 'rel_c32_01', 'shen_guan_qiangruo', 'rel_c32_02', 'guange_jinji', 'evi_c32_01', 'shen_guan_qiangruo', 'rule_guange_yunxiang_by_qiangruo', 'evi_c32_02', 'guange_jinji', 'rule_guange_jinji_list', 'evi_c32_03', 'shen_guan_qiangruo', 'rule_guange_shenwang_qucaiguan']
    
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
        l1_anchor="zpzq_v1.0.0_正官格成后_如何借行运而显其用_001_L1",
    )
    version: str = "1.0.0"
