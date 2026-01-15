"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699282
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
    semantic_id="zw_v1.0.0_廉颇之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 廉颇之命(SemanticEntry):
    """
    - 分字分词释义：

  - **七杀朝斗**：七杀星朝向斗星，主富贵荣华。
  - **禄合权会**：禄存与化权会合，主文武材能。
  - **大限天伤**：大限行至天伤之地，主凶险。
  - **...
    """
    
    original_text: str = """- 分字分词释义：

  - **七杀朝斗**：七杀星朝向斗星，主富贵荣华。
  - **禄合权会**：禄存与化权会合，主文武材能。
  - **大限天伤**：大限行至天伤之地，主凶险。
  - **太岁伏牛**：太岁在丑宫，主行动受限。
  - **天空天使之地**：太岁又在天空天使宫位，主诸凶齐聚。
  - **流羊冲命**：流年擎羊冲照命垣，主寿终。
  - **阴男土五局**：廉颇命盘的五行局数，土五局主厚重武勇。

- **原文（source_text）**：  
  廉颇之命。阴男土五局。七杀朝斗，富贵荣华，禄合权会，文武材能。七十三岁，大限在天伤之地，太岁伏牛，又在天空天使之地，小限相冲，流羊在戍，冲照命垣，是以凶也。

- **规范化释义（primary_lang_explained）**：  
  廉颇命属阴男土五局，七杀朝斗、禄合权会，主富贵荣华、文武材能。七十三岁大限在天伤之地，太岁伏牛，又在天空天使之地，小限相冲，流羊冲照命垣，故凶而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Lian Po's Yin male Earth Fifth chart has Seven Killings Facing Dipper, Salary‑Authority converge—wealth, honour, civil‑martial talent. At 73 major at Wound; Tai Sui hidden Ox, at Void‑Envoy; minor clashes; transiting Blade at Xu clashes Life. Death.

- **核心要点**：  
  1. 七杀朝斗、禄合权会，主富贵文武。  
  2. 大限天伤、太岁天空天使。  
  3. 小限相冲、流羊冲命，为寿终应期。

- **叙事素材（narrative_snippets）**：
  - **武将贵格**："七杀朝斗，富贵荣华，禄合权会，文武材能"，廉颇命主富贵荣华、武功显赫。
  - **晚年天伤**："七十三岁，大限在天伤之地，太岁伏牛，又在天空天使之地"，晚年限行天伤、天空天使，为高龄多病与战功难再的信号。
  - **流羊冲命**："小限相冲，流羊在戍，冲照命垣，是以凶也"，流羊冲命垣为寿终具体触发点。
  - **现代应用**：高压岗位或长期在一线打拼者，在天伤天空加流羊冲命的年份，应主动减压、调离前线，避免“老骥伏枥”反致伤残。"""
    normalized_text_zh: str = """"""
    subject: str = "廉颇之命"
    factor_refs: list = ['pattern_qishachaodou', 'pattern_liuyangchongming', 'pattern_tianshangtiankongtianshi', 'source_ref', 'rel_lianpo_001', 'pattern_qishachaodou', 'rel_lianpo_002', 'pattern_tianshangtiankongtianshi', 'rel_lianpo_003', 'pattern_liuyangchongming', 'evi_lianpo_001', 'pattern_liuyangchongming', 'rule_liuyang_chongming', 'concept_seven_kill', 'concept_wound_void']
    
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
        l1_anchor="zw_v1.0.0_廉颇之命_001_L1",
    )
    version: str = "1.0.0"
