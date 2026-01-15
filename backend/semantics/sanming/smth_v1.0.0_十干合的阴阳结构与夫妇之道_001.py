"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264374
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
    semantic_id="smth_v1.0.0_十干合的阴阳结构与夫妇之道_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十干合的阴阳结构与夫妇之道(SemanticEntry):
    """
    - **原文（source_text）**：  
  谕十干合夫合者，乃和谐之义。如阳见阳，二阳相竞则为克；阴见阴，二阴不足则为克。惟阴见阳，阳见阴为合，亦如男女相合而成夫妇之道。易曰：一阴一阳之谓道...
    """
    
    original_text: str = """- **原文（source_text）**：  
  谕十干合夫合者，乃和谐之义。如阳见阳，二阳相竞则为克；阴见阴，二阴不足则为克。惟阴见阳，阳见阴为合，亦如男女相合而成夫妇之道。易曰：一阴一阳之谓道，偏阳偏阴之谓疾。是也。

- **分字分词释义**：
  - **十干合**：指甲己、乙庚、丙辛、丁壬、戊癸五组干合，是十天干间最核心的配对结构之一。
  - **阳见阳为克**：同为阳干相遇，多呈竞争与对立，刚强相争，易由“和”转为“克”。
  - **阴见阴为克**：同为阴干相遇，各求依附却彼此牵累，力量不足以互补，亦难成真正之合。
  - **一阴一阳之谓道**：出自《系辞传》，强调阴阳相济才符合“道”，任何一端的偏盛都接近病态。

- **规范化释义（primary_lang_explained）**：  
  本段作为“十干合”一章的总纲，先从阴阳结构界定“何谓合”。作者指出：十干之合绝不是“凡见合字皆主吉”，而是以阴阳相配为前提。两个阳干相见，如两位都要居上的强者，往往互不相下，容易从合作滑向争斗；两个阴干相见，如两人都求倚靠却无一方能真正担当，也会形成牵累与消耗。因此，只有“阴见阳、阳见阴”的组合，才是以互补为基础的真正之合，如夫妇之道，一刚一柔，才能共建稳定结构。引《易》言“一阴一阳之谓道，偏阳偏阴之谓疾”，就是在提醒读者：判断合局时，不能只看表面是否“相合”，而要看其是否实现了阴阳的平衡，是否避免了偏颇与病态。

- **完整对等诠释（secondary_lang_full）**：  
  This opening paragraph lays down the doctrinal foundation for all subsequent discussions of the Heavenly Stem combinations. It emphasizes that "combination" (he) does not mean that whenever two stems meet, auspicious harmony automatically arises. True combination must be grounded in Yin‑Yang complementarity. When Yang meets Yang, two strong, assertive forces compete for dominance; what appears as union easily turns into contention and control. When Yin meets Yin, two yielding, dependent forces lean on each other without sufficient backbone, leading to mutual entanglement and depletion. Only when Yin encounters Yang and Yang encounters Yin do we obtain a genuinely constructive union, likened to the marriage of husband and wife, where roles differ but support each other. The quotation from the Yijing—"one Yin and one Yang is called the Dao; excessive Yang or excessive Yin is called illness"—underscores that balanced polarity is the criterion for a wholesome pattern. Accordingly, the five canonical stem pairings are to be understood as codifications of structurally sound Yin‑Yang matches; whenever polarity is lopsided, the so‑called "combination" degenerates into imbalance and becomes a source of trouble rather than blessing.

- **核心要点**：
  - 十干合的本质是阴阳互补，而非“见合即吉”。
  - 阳见阳、阴见阴往往从“合”转为“克”，表现为竞争、牵累与失衡。
  - 《易经》“一阴一阳之谓道”提供了判断合局是否健康的根本标尺。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_105]` `[trigger: 合者和谐]` `[factor_trigger: hezhe_hexie AND yinyang_xiangpei]` `[role: 主干]` 合者，乃和谐之义。如阳见阳，二阳相竞则为克。 → 《三命通会》卷十#十干合的阴阳结构与夫妇之道
  - `[ns_smth_10_106]` `[trigger: 阴见阳合]` `[factor_trigger: yinjian_yanghe AND fufu_zhidao]` `[role: 主干依赖]` 惟阴见阳，阳见阴为合，亦如男女相合而成夫妇之道。 → 《三命通会》卷十#十干合的阴阳结构与夫妇之道
  - `[ns_smth_10_107]` `[trigger: 一阴一阳]` `[factor_trigger: yiyin_yiyang AND zhiwei_dao]` `[role: 条件分支]` 易曰：一阴一阳之谓道，偏阳偏阴之谓疾。 → 《三命通会》卷十#十干合的阴阳结构与夫妇之道
  - `[ns_smth_10_108]` `[trigger: 偏阴偏阳]` `[factor_trigger: pianyin_pianyang AND zhiwei_ji]` `[role: 总结]` 偏阳偏阴之谓疾。是也。 → 《三命通会》卷十#十干合的阴阳结构与夫妇之道

- **详细解说**：  
  在实际命理实践中，“合”常被初学者简单理解为喜象：凡合必好、凡克必坏。作者在纲领位置就通过阴阳结构为这一误解设定边界：若同性质的力量过度靠拢，不是互补而是偏执，合局也会转成压力源。例如，多阳相会时，个人或结构中“要掌控、要决断”的一面被不断强化，容易导致权力斗争与强硬对撞；多阴相聚时，则是“依赖、犹豫、回避”的一面被放大，容易把关系拖入优柔寡断与互相消耗。工程化时，可以将“是否构成健康的阴阳配对”抽象为一个独立因子：在判定合局吉凶时，先看阴阳是否均衡，再结合五行生克与十神喜忌，避免把所有合一概打包为“吉信号”。

- **校勘与字词辨析（双语）**：
  - **中文**：“偏阳偏阴之谓疾”原是从整体宇宙与人身角度谈阴阳失衡之病，此处借来说明：十干虽合，若偏于一端，即为“带病之合”，不宜简单视作福合。
  - **English**: The term "illness" in the Yijing passage is conceptual rather than strictly medical. It denotes systemic imbalance. The present text borrows it to warn against overvaluing formal combinations that lack real Yin‑Yang complementarity."""
    normalized_text_zh: str = """"""
    subject: str = "十干合的阴阳结构与夫妇之道"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_十干合的阴阳结构与夫妇之道_001_L1",
    )
    version: str = "1.0.0"
