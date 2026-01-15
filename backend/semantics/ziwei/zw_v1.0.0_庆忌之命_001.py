"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699263
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
    semantic_id="zw_v1.0.0_庆忌之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 庆忌之命(SemanticEntry):
    """
    - 分字分词释义：

  - **马头带箭**：特定格局主刑伤而非夷折。
  - **早年限行吉地**：少年限运行吉地，作事峙嵬。
  - **手能捉飞鸟**：形容庆忌武勇过人、身手矫健。
  - *...
    """
    
    original_text: str = """- 分字分词释义：

  - **马头带箭**：特定格局主刑伤而非夷折。
  - **早年限行吉地**：少年限运行吉地，作事峙嵬。
  - **手能捉飞鸟**：形容庆忌武勇过人、身手矫健。
  - **大限天空小限地劫**：大限逢天空、小限逢地劫，空劫齐聚。
  - **天罗流羊流陀迭并**：天罗与流年擎羊陀罗齐聚，主暴亡。
  - **凶星迭并**：多重凶星同时作用，主凶亡。
  - **阳男金四局**：庆忌命盘的五行局数，金四局主刚断勇猛。

- **原文（source_text）**：  
  庆忌之命。阳男金四局。马头带箭，非夭折而刑伤。早年限行吉地，作事峥嵘，手能捉飞鸟。二十三岁，大限到申，值天空，小限到寅，遇地劫，大岁、天罗、流羊、流陀迭并，以至𮞸凶而亡。

- **规范化释义（primary_lang_explained）**：  
  庆忌命属阳男金四局，马头带箭格局主刑伤而非夭折。早年限行吉地，手能捉飞鸟。二十三岁大限到申值天空，小限到寅遇地劫，大岁天罗、流羊流陀迭并，遂凶而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Qing Ji's Yang male Metal Fourth chart has Horse Head with Arrow—injury not early death. Early periods in auspicious positions, could catch flying birds. At 23 major at Shen meets Void; minor at Yin meets Robbery; Tai Sui in Heaven Net with transiting Blade‑Tuo converge. Violent death.

- **核心要点**：  
  1. 马头带箭，主刑伤。  
  2. 早年限行吉地，作事峥嵘。  
  3. 大限天空、小限地劫、流羊流陀迭并，为凶亡应期。

- **叙事素材（narrative_snippets）**：
  - **马头带箭**："马头带箭，非夭折而刑伤"，庆忌命主以刑伤见重，不必然早夭。
  - **手捉飞鸟**："早年限行吉地，作事峥嵘，手能捉飞鸟"，形容其少年武勇过人、身手矫健。
  - **凶星迭并**："二十三岁，大限到申，值天空，小限到寅，遇地劫，大岁、天罗、流羊、流陀迭并，以至𮞸凶而亡"，天空地劫配合天罗流羊流陀，为暴亡应期。
  - **现代应用**：热爱极限运动或高危行为者，在天空地劫与流羊流陀迭并的年份，宜降低危险系数，避免逞强导致无法挽回的事故。"""
    normalized_text_zh: str = """"""
    subject: str = "庆忌之命"
    factor_refs: list = ['pattern_matoudaijian', 'pattern_xiongxingdiebing', 'pattern_tianluoliuyangtuo', 'source_ref', 'rel_qingji_001', 'pattern_matoudaijian', 'rel_qingji_002', 'pattern_kongjiediebing', 'rel_qingji_003', 'pattern_tianluoliuyangtuo', 'evi_qingji_001', 'pattern_tianluoliuyangtuo', 'rule_xiongxingdiebing', 'concept_horse_arrow', 'concept_malefic_converge']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_庆忌之命_001_L1",
    )
    version: str = "1.0.0"
