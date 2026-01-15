"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042599
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
    semantic_id="smth_v1.0.0_庚金为月_001",
    book_id="sanming",
    engine_id="bazi"
)
class 庚金为月(SemanticEntry):
    """
    - **原文（source_text）**：
  庚金为月。庚乃酉方阳金，何以知其配月乎？曰：五行之有庚，犹四时之有月也。庚不待秋而长生，然必秋而始盛；月不待秋而后月，然必秋而益明。以色言，月固白也，...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚金为月。庚乃酉方阳金，何以知其配月乎？曰：五行之有庚，犹四时之有月也。庚不待秋而长生，然必秋而始盛；月不待秋而后月，然必秋而益明。以色言，月固白也，其色同矣；以气言，金生水也，潮应月也，其气同矣。经云：「金沉在子。」见其与月沉波也，三日月见庚方见，月初生与庚为位也，故曰庚金为月。如人庚日生者，四柱有乙巳字出，谓之「月白风清」：秋为上，冬次之，春夏无取。

- **分字分词释义**：
  - **庚金为月**：以秋月喻庚金之清白与肃杀。
  - **潮应月也**：金生水、潮汐随月，说明气机关联。
  - **月白风清**：乙木为风、巳火为光，与庚月相映成清朗之象。

- **规范化释义（primary_lang_explained）**：
  庚金比作明月：虽全年存在，却以秋夜最为清朗。月色本白，如庚金之色；金生水，潮氐随月涨落，亦表金水与月之关系。庚日命人若柱有乙巳等字，形成「月白风清」之象，尤以秋令为佳，冬次之，春夏则不相宜。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal is likened to the bright autumn moon: it is present throughout the year, but shines with greatest clarity in still, cool nights. The moon’s inherent whiteness matches Geng’s colour, and the way tides respond to the moon reflects Metal’s power to give rise to Water and govern its rhythms. In a chart where a Geng day is set in autumn, especially when Yi Wood and Si Fire appear to form the pattern called “moon white, wind clear”, rules, timing, and aesthetic sense can work together so that authority is cool but not cruel, strict yet transparent. Spring and summer, by contrast, blur this clear edge: excessive heat and growth make the same Metal feel harsh or misplaced. Read this way, Geng‑as‑moon is less about raw cutting force and more about cyclical regulation, measured light, and the ability to illuminate patterns without burning, provided the season and surrounding elements support that role."""
    normalized_text_zh: str = """"""
    subject: str = "庚金为月"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_庚金为月_001_L1",
    )
    version: str = "1.0.0"
