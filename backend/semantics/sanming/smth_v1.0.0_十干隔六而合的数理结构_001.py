"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264404
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
    semantic_id="smth_v1.0.0_十干隔六而合的数理结构_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十干隔六而合的数理结构(SemanticEntry):
    """
    - **原文（source_text）**：  
  或斗十干必隔六位一合，何也？余答曰：天地之数，各不过五，上五位为生数，下五位为成数，生数与成数相遇，然后合。天一生壬，地二生丁，天三生甲，地四生辛...
    """
    
    original_text: str = """- **原文（source_text）**：  
  或斗十干必隔六位一合，何也？余答曰：天地之数，各不过五，上五位为生数，下五位为成数，生数与成数相遇，然后合。天一生壬，地二生丁，天三生甲，地四生辛，天五生戊，地六成癸，天七成丙，地八成乙，天九成庚，地十成己，天一数见，地二数然后合，所以必隔六也。易曰：天数五，地数五，五位相得而各有合是也。五行要论云：天一生水，其于物为精，精者，一之所生也。地二生火，其于物为神，神者，二之所生也。天三生木，其于物为魂，魂从神者也。地四生金，其于物为魄，魄从精者也。天五生土，其于物为体。体者，精神魂魄具而后有者也。自天一至天五，五行之生数；自地六至地十，五行之成数。以奇生者成而偶，以偶生者成而奇，其成之者皆五五天数之中，所以成于物也。

- **规范化释义（primary_lang_explained）**：  
  此段解释“十干为何隔六位而合”的数理基础。作者以“天数五、地数五”为框架，将十干拆为“生数”与“成数”两组：天一生壬、水为“精”；地二生丁、火为“神”；天三生甲、木为“魂”；地四生辛、金为“魄”；天五生戊、土为“体”。这五者构成五行的生成面。地六成癸、水之成；天七成丙、火之成；地八成乙、木之成；天九成庚、金之成；地十成己、土之成，则是五行的完成面。所谓“必隔六位一合”，就是让“生数”与对应的“成数”相遇：如甲在天三，其成数在地八乙；戊在天五，其成数在地十己，等等。如此，每一对干合都在数理上实现了“自生而自成”的闭环，象征在一个体系内部精、神、魂、魄、体俱全，才算真正完满的结合。
  - **中文**：“精、神、魂、魄、体”的分配方式源自传统五行心性论，本精校在释义中保留原顺序，不尝试以现代心理学术语强行对照。
  - **English**: The mapping of Water to essence, Fire to spirit, Wood to soul, Metal to corporeal soul and Earth to body reflects a pre‐modern cosmology. In contemporary usage it can be treated as a layered model of potentials and manifestations rather than literal anatomy.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_geliu_001]` `[trigger: 隔六而合]` `[factor_trigger: geliu_erhe AND tiandi_zhishu]` `[role: 主干]` 天地之数，各不过五，上五位为生数，下五位为成数，生数与成数相遇，然后合。 → 《三命通会》卷十#十干隔六而合
  - `[ns_smth_10_geliu_002]` `[trigger: 精神魂魄体]` `[factor_trigger: jingshen_hunpo_ti AND wuxing_wuceng]` `[role: 主干依赖]` 天一生水其于物为精，地二生火其于物为神，天三生木其于物为魂，地四生金其于物为魄，天五生土其于物为体。 → 《三命通会》卷十#十干隔六而合
  - `[ns_smth_10_geliu_003]` `[trigger: 必隔六也]` `[factor_trigger: bi_geliu_ye AND shengcheng_bihuan]` `[role: 总结]` 天一数见，地二数然后合，所以必隔六也。 → 《三命通会》卷十#十干隔六而合"""
    normalized_text_zh: str = """"""
    subject: str = "十干隔六而合的数理结构"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_十干隔六而合的数理结构_001_L1",
    )
    version: str = "1.0.0"
