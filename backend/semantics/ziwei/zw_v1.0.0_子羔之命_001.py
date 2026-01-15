"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699071
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
    semantic_id="zw_v1.0.0_子羔之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 子羔之命(SemanticEntry):
    """
    - 分字分词释义：

  - **府相朝垣格**：天府天相拱照命宫的贵格，主食禄千钟、富贵双全。
  - **子生人有忌**：子年生人于申宫有特定禁忌。
  - **天伤天刑夹地**：天伤天刑二凶星夹...
    """
    
    original_text: str = """- 分字分词释义：

  - **府相朝垣格**：天府天相拱照命宫的贵格，主食禄千钟、富贵双全。
  - **子生人有忌**：子年生人于申宫有特定禁忌。
  - **天伤天刑夹地**：天伤天刑二凶星夹守限运宫位，主凶险。
  - **天哭天虚**：二星主哀伤虚耗，小限逢此加重凶象。
  - **沐浴败地**：十二长生位之一，主衰弱不利。
  - **食禄千钟**：富贵之象，享受丰厚俸禄。
  - **阳男金四局**：子羔命盘的五行局数，金四局主刚断决绝。

- **原文（source_text）**：  
  子羔之命。阳男金四局。此为府相朝垣格，食禄千钟，富贵双全，一生顺美。四十四岁入大限在申宫，子生人有忌。申限天伤、天刑夹地，小限四十五岁，逢天哭、天虚，沐浴败地，故命亡。

- **规范化释义（primary_lang_explained）**：  
  子羔命属阳男金四局，府相朝垣格，主食禄千钟、富贵双全。四十四岁大限入申宫，子生人于申有忌；天伤天刑夹守，小限四十五岁逢天哭天虚、沐浴败地，诸凶齐聚而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Zi Gao's Yang male Metal Fourth chart forms Fu Xiang Facing Court—stipends by thousands, dual blessings. At 44 major period enters Shen—Zi natives face taboos. Celestial Wound and Punishment flank; minor at 45 meets Crying and Void at Bathing‑Defeat. Malefics converge, causing death.

- **核心要点**：  
  1. 府相朝垣格主富贵双全。  
  2. 子生人忌申限，天伤天刑夹守为凶。  
  3. 天哭天虚、沐浴败地叠加，为命亡应期。

- **叙事素材（narrative_snippets）**：
  - **富贵格局**："府相朝垣，食禄千钟"，子羔命主富贵双全。
  - **生年忌限**："子生人于申有忌"，子年生人忌申限。
  - **凶星夹守**："天伤天刑夹守，天哭天虚沐浴败地"，诸凶齐聚致亡。
  - **现代应用**：富贵命亦需关注生年忌限与凶星夹守的组合风险。"""
    normalized_text_zh: str = """"""
    subject: str = "子羔之命"
    factor_refs: list = ['star_tianshangxing', 'star_tiankuxu', 'pos_muyubai', 'source_ref', 'rel_zigao_001', 'pattern_fuxiangchaoyuan', 'rel_zigao_002', 'star_tianshangxing', 'rel_zigao_003', 'pos_muyubai', 'evi_zigao_001', 'star_tianshangxing', 'rule_zishengji', 'evi_zigao_002', 'pos_muyubai', 'rule_muyubai_wang', 'concept_flanking_malefics', 'concept_life_stage_weak']
    
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
        l1_anchor="zw_v1.0.0_子羔之命_001_L1",
    )
    version: str = "1.0.0"
