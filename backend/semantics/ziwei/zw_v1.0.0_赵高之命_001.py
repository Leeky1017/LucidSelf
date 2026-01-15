"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699226
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
    semantic_id="zw_v1.0.0_赵高之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 赵高之命(SemanticEntry):
    """
    - 分字分词释义：

  - **禄合左右**：禄存与左辅右彼会合，主爵禄丰税。
  - **紫破辰戌**：紫微破军在辰戌宫，主不忠。
  - **指鹿为马**：赵高指鹿为马的历史事件，为紫破不忠的验...
    """
    
    original_text: str = """- 分字分词释义：

  - **禄合左右**：禄存与左辅右彼会合，主爵禄丰税。
  - **紫破辰戌**：紫微破军在辰戌宫，主不忠。
  - **指鹿为马**：赵高指鹿为马的历史事件，为紫破不忠的验证。
  - **大限夹地遇陀罗**：大限落入夹地又遇陀罗，主凶。
  - **丧门吁客病符**：多重丧吁疾病之星齐聚，主凶亡。
  - **富贵双全**：禄合左右格局的主要效应。
  - **阴男土五局**：赵高命盘的五行局数，土五局主厚重。

- **原文（source_text）**：  
  赵高之命。阴男土五局。此为禄合，左右相会，一生爵禄甚曹盈，富贵双全应有分。紫破辰戌不忠，故有指鹿为马之事。大限夹地遇陀罗，流年小限丧门、吊客、病符作殃，故主凶亡。

- **规范化释义（primary_lang_explained）**：  
  赵高命属阴男土五局，禄合左右相会，主爵禄丰盈、富贵双全。然紫破辰戌主不忠，故有指鹿为马之事。大限夹地遇陀罗，流年小限丧门、吊客、病符作殃，故凶亡。

- **完整对等诠释（secondary_lang_full）**：  
  Zhao Gao's Yin male Earth Fifth chart has Salary combination with Left‑Right—abundant rank and wealth. But Ziwei‑Po Jun in Chen‑Xu indicates disloyalty, hence the deer‑horse incident. Major flanks Earth with Tuo; annual minor with Mourning, Condolence, Illness as calamity. Violent death.

- **核心要点**：  
  1. 禄合左右，主富贵双全。  
  2. 紫破辰戌，主不忠。  
  3. 大限夹地遇陀罗、丧门吊客病符，为凶亡应期。

- **叙事素材（narrative_snippets）**：
  - **富贵双全**："此为禄合，左右相会，一生爵禄甚曹盈，富贵双全应有分"，赵高命主爵禄丰厚、位极权臣。
  - **指鹿为马**："紫破辰戌不忠，故有指鹿为马之事"，紫破辰戌暗示其以权乱政、颠倒是非的性格走向。
  - **凶星作殃**："大限夹地遇陀罗，流年小限丧门、吊客、病符作殃"，多重丧吊与疾病之星齐至，终致身败名裂而死。
  - **现代应用**：位高权重而又背离底线者，在丧门吊客病符齐聚与陀罗夹地的年份，往往面临司法清算或公众讨伐，宜以此命例为鉴。"""
    normalized_text_zh: str = """"""
    subject: str = "赵高之命"
    factor_refs: list = ['pattern_zipochenxu', 'star_diaoke', 'star_sangmenbingfu', 'source_ref', 'rel_zhaogao_001', 'pattern_luhezuoyou', 'rel_zhaogao_002', 'pattern_zipochenxu', 'rel_zhaogao_003', 'star_sangmenbingfu', 'evi_zhaogao_001', 'star_sangmenbingfu', 'rule_sangmendiaoke', 'concept_disloyalty', 'concept_mourning_illness']
    
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
        l1_anchor="zw_v1.0.0_赵高之命_001_L1",
    )
    version: str = "1.0.0"
