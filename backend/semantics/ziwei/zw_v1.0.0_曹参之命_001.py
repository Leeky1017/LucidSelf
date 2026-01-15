"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699244
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
    semantic_id="zw_v1.0.0_曹参之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 曹参之命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫微居午**：紫微星在午宫，无杀凑主极贵。
  - **左右权禄**：左辅右彼与化权化禄会合，主官至三公。
  - **子寅二宫加会**：子宫寅宫吉星会合，主官资清显...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫微居午**：紫微星在午宫，无杀凑主极贵。
  - **左右权禄**：左辅右彼与化权化禄会合，主官至三公。
  - **子寅二宫加会**：子宫寅宫吉星会合，主官资清显。
  - **天伤夹地**：天伤星夹守地网，主凶险。
  - **羊刃照命**：流年擎羊照命宫，主血光官灾。
  - **酉生人忌**：酉年生人于此限尤为高危。
  - **阴男土五局**：曹参命盘的五行局数，土五局主厚重稳健。

- **原文（source_text）**：  
  曹参之命。阴男土五局。紫微居午，无杀凑左右权禄，子寅二宫加曾官资，清题至三公。六十三岁，太岁到天伤夹地，又流年羊刃照命，酉人忌之，为凶也。

- **规范化释义（primary_lang_explained）**：  
  曹参命属阴男土五局，紫微居午无杀凑、左右权禄、子寅二宫加会，主官资清显至三公。六十三岁太岁到天伤夹地，流年羊刃照命，酉生人有忌，故凶而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Cao Can's Yin male Earth Fifth chart has Ziwei at Wu without killers, Left‑Right Authority‑Salary, Zi‑Yin palaces converge—official rank to Three Dukes. At 63 Tai Sui at Wound flanks Earth; annual Blade lights Life; You natives face taboo. Death.

- **核心要点**：  
  1. 紫微居午无杀、左右权禄，主官至三公。  
  2. 太岁天伤夹地、流年羊刃照命。  
  3. 酉生人有忌，为寿终应期。

- **叙事素材（narrative_snippets）**：
  - **三公清题**："紫微居午，无杀凑左右权禄，子寅二宫加曾官资，清题至三公"，曹参命主清望之贵、位极三公。
  - **天伤夹地**："六十三岁，太岁到天伤夹地，又流年羊刃照命"，天伤夹地配羊刃照命，为晚年血光与官灾并见之象。
  - **酉生为忌**："酉人忌之，为凶也"，提示酉年生人于此限尤为高危。
  - **现代应用**：高位公职人员遇天伤夹地、羊刃照命与生年忌限叠加之年，应减少锋芒、谨慎用权，防止因一时决策惹来大祸。"""
    normalized_text_zh: str = """"""
    subject: str = "曹参之命"
    factor_refs: list = ['pattern_ziweiwu', 'pattern_yangrenzhao', 'pattern_tianshangjia', 'source_ref', 'rel_caocan_001', 'pattern_ziweiwu', 'rel_caocan_002', 'pattern_tianshangjia', 'rel_caocan_003', 'taboo_youshengji', 'evi_caocan_001', 'taboo_youshengji', 'rule_tianshang_yangren', 'concept_ziwei_wu', 'concept_blade_light']
    
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
        l1_anchor="zw_v1.0.0_曹参之命_001_L1",
    )
    version: str = "1.0.0"
