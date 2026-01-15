"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699503
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
    semantic_id="zw_v1.0.0_林御史命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 林御史命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫府同宫**：紫微与天府同居一宫，主清贵、稳重与统摄能力。
  - **科禄加会昌曲俱拱**：科星禄星加会，文昌文曲夹拱，为合格局。
  - **左辅文昌尊居八位**...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫府同宫**：紫微与天府同居一宫，主清贵、稳重与统摄能力。
  - **科禄加会昌曲俱拱**：科星禄星加会，文昌文曲夹拱，为合格局。
  - **左辅文昌尊居八位**：左辅与文昌配合，使命主尊居台谏高位。
  - **子生人忌行寅年**：子宫安命之人忌行寅年太岁，因寅子相冲易动荡。
  - **天空天伤之地**：大限行入天空与天伤同宫之地，主虚耗、伤损与危机。
  - **台谏之职**：以直言弹劾、秉公执法见长的御史之职。
  - **阳男金四局**：林御史命盘的五行局数，金四局主刚断正直。

- **原文（source_text）**：  
  林御史命。阳男金四局。紫府同宫，科禄加会，兼昌曲俱拱，为合格局。又云：左辅文昌，尊居八位。太岁到寅，小限五十一在子，且子生人忌行寅年，大限又在天空天伤之地，故死。

- **规范化释义（primary_lang_explained）**：  
  林御史命为阳男金四局，命宫紫微与天府同宫，科星、禄星又来加会，再兼文昌、昌曲拱照，是典型「紫府同宫、科禄加会」的清贵台谏格，足以「尊居八位」，在朝中以直言弹劾、秉公执法见长。此格局一方面主地位清显、俸禄不薄，另一方面也暗示一生多处高压权力结构之中。  
  原文指出其寿元关键在于五十一岁：太岁行到寅宫，小限亦在子位，而「子生人忌行寅年」，再加大限同时在天空、天伤之地，形成「寅子冲动 + 天空天伤」的高危组合。此时既有时运冲击原有格局，也有台谏之职易触动权贵逆鳞的隐喻，因此最终在此阶段以非自然之方式身亡。此命例刻画的是「清贵御史，敢言持正，但难全身而退」的结构。

- **完整对等诠释（secondary_lang_full）**：  
  The chart of Censor Lin is that of a Yang Metal native in the Fourth Configuration. Zi Wei and Tian Fu share the Life palace, while Academic and Salary stars join in; Wen Chang and Wen Qu further surround the configuration. This "Zi‑Fu with Ke‑Lu" pattern is characteristic of upright censors and high officials whose dignity and income are both substantial. It supports a career built on principled remonstrance—speaking truth to power from within the machinery of state.  
  The text, however, highlights a dangerous turning point around the age of fifty‑one. The Annual Tai Sui moves into Yin while the minor period falls in Zi; for those born under the Zi branch, "walking the year of Yin" is especially inauspicious. At the same time the major period occupies the region of Tian Kong and Tian Shang, stars that signify emptiness, exposure and harm. Together they form a structure of clashing branches and wounded support, suggesting a moment when the censor’s role brings him into fatal collision with prevailing powers. The case portrays a noble but precarious life: high office and integrity, yet little chance of retiring peacefully.

- **核心要点**：  
  1. 紫府同宫、科禄加会再兼昌曲，是典型清贵台谏、言官命格。  
  2. 身处权力中枢、以直言为职，使命主长期在高压结构之下行走。  
  3. 五十一岁太岁到寅、小限在子，大限行天空天伤之地，为难以全身而退的高危年份。

- **叙事素材（narrative_snippets）**：
  - **紫府清议**："紫府同宫，科禄加会，兼昌曲俱拱，为合格局"，林御史命主以紫府清贵、科禄与文星加会，象征台谏高官、清议之臣。
  - **尊居八位**："又云：左辅文昌，尊居八位"，左辅配文昌，说明其不但位高言重，更有文才与辅佐之功。
  - **寅子冲动**："太岁到寅，小限五十一在子，且子生人忌行寅年，大限又在天空天伤之地，故死"，寅子相冲又遇天空天伤，为清流与强权碰撞的致命年份。
  - **现代应用**：现代从事监察、审计、纪检或舆论监督等角色者，若命局类似紫府台谏格，在关键冲克年份应更加注意表达方式与自我保护，做到敢言但不轻身涉险，为原则留底线、也为生命留余地。"""
    normalized_text_zh: str = """"""
    subject: str = "林御史命"
    factor_refs: list = ['pattern_zifu_tonggong', 'pattern_kelu_jiahui', 'pattern_changqu_jugong', 'pattern_zuofu_wenchang_bawei', 'condition_zishengren_ji_yinnian', 'malefic_tiankong_tianshang']
    
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
        l1_anchor="zw_v1.0.0_林御史命_001_L1",
    )
    version: str = "1.0.0"
