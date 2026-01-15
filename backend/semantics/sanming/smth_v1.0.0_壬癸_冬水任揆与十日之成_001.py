"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227578
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
    semantic_id="smth_v1.0.0_壬癸_冬水任揆与十日之成_001",
    book_id="sanming",
    engine_id="bazi"
)
class 壬癸冬水任揆与十日之成(SemanticEntry):
    """
    - **原文（source_text）**：
  壬癸其位水，行冬之令。壬之言任也，壬而为胎，万物怀妊于壬。癸者，揆也，天令至此，万物闭藏，揆然萌芽。故经曰：天有十日，日六竟而周甲者，此也。盖天地之数...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬癸其位水，行冬之令。壬之言任也，壬而为胎，万物怀妊于壬。癸者，揆也，天令至此，万物闭藏，揆然萌芽。故经曰：天有十日，日六竟而周甲者，此也。盖天地之数，甲丙戊庚壬为阳，乙丁巳辛癸为阴，五行各一阴一阳，故有十日也。

- 分字分词释义：
  - **壬，任也**：承担、怀任之意，主怀妊、载负与潜滋暗长。
  - **癸，揆也**：揆度、筹划之意，主在闭藏中暗中筹划、萌芽未来。
  - **十日之成**：五行各一阴一阳，合成十干，构成十日轮值的天数系统。

- **规范化释义（primary_lang_explained）**：
  壬癸为冬水：壬水如怀妊之母，承担万物种子，暗中孕育；癸水则在闭藏之中揆度未来，预示新一轮生长的萌芽。十干中阴阳各半，形成「天有十日」之制，一方面对应四时寒暑，一方面也为历法与命理提供节奏刻度。

- **完整对等诠释（secondary_lang_full）**：

  Ren and Gui are the Waters of winter. Ren Water is associated with “ren”, to bear and to be entrusted: it is like a pregnant mother or a great river, carrying within it the seeds of myriad beings and nurturing them unseen. Gui Water is linked with “gui”, to gauge and plan: in the closed, hidden phase it measures, evaluates and quietly allows new sprouts to form, pointing toward the next cycle. In the Ten Stems, Yin and Yang divide evenly into five pairs, forming the system of “ten suns”; this both mirrors how cold and heat circulate through the seasons and provides the counting rhythm used by calendars and destiny techniques. In charts, Ren Water tends to signify long‑range burdens, distant journeys and the capacity to shoulder weight, while Gui Water points more to inward reflection, planning and the subtle, intuitive beginnings of future change."""
    normalized_text_zh: str = """"""
    subject: str = "壬癸：冬水任揆与十日之成"
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
        l1_anchor="smth_v1.0.0_壬癸_冬水任揆与十日之成_001_L1",
    )
    version: str = "1.0.0"
