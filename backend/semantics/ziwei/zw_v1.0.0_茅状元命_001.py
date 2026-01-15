"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699848
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
    semantic_id="zw_v1.0.0_茅状元命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 茅状元命(SemanticEntry):
    """
    - 分字分词释义：

  - **日月照命**：日、月同来照拱命宫，主名望与光彩。
  - **昌曲夹命**：文昌、文曲夹住命宫或贵星，主文章科第。
  - **前后三方吉集**：命宫前后及三方皆有吉...
    """
    
    original_text: str = """- 分字分词释义：

  - **日月照命**：日、月同来照拱命宫，主名望与光彩。
  - **昌曲夹命**：文昌、文曲夹住命宫或贵星，主文章科第。
  - **前后三方吉集**：命宫前后及三方皆有吉星聚会，主格局纯净强大。
  - **允为大贵**：格局被认定为允当大贵之命。
  - **对宫羊刃入庙**：羊刃落于对宫得地之位，锋芒强而可用。
  - **阴男水二局**：茅状元命盘的五行局数，水二局主智慧状元。

- **原文（source_text）**：  
  茅状元命。阴男水二局。曰月照命，昌曲夹命，且前后三方吉集，允为大贵。其对宫羊刃入庙不妨。

- **规范化释义（primary_lang_explained）**：  
  茅状元为阴男水二局，「日月照命」主日月同来照拱命宫，光彩夺目；「昌曲夹命」指文昌、文曲分列命宫两侧，为文名与科第之象；前后与三方又皆吉星聚会，是典型的「日月昌曲齐集」的科甲大贵格局，因此得「状元」之名。  
  原文特别说明「对宫羊刃入庙不妨」，表示虽有羊刃星在对宫落庙而带来锐利与冲劲，但由于整体格局吉星太强，羊刃反而转化为破题而出的气魄与竞争力，而非致命之凶。整体来看，此命重在以文名登科甲之巅，再以正统仕途渐进高位。

- **完整对等诠释（secondary_lang_full）**：  
  The "Mao Zhuangyuan" chart belongs to a Yin Water native in the Second Configuration. With the Sun and Moon illuminating the Life palace and Wen Chang/Wen Qu flanking it, the set‑up clearly points to scholarly brilliance and examination success. Auspicious stars gather not only at the core but also in the tri‑palaces, forming a "Sun‑Moon with Chang‑Qu" pattern that is explicitly labelled as worthy of high nobility—the title "Zhuangyuan" marks the top degree in the imperial examinations.  
  The text notes that a Yang Blade star, though present in the opposite palace and in its temple strength, "does no harm." Here the Blade provides courage, competitiveness and cutting through obstacles rather than pure destruction, because the chart is so heavily supported by benefics. This is a paradigm of a literary‑examination destiny that climbs through institutional channels to prominent civil office.

- **核心要点**：  
  1. 日月照命、昌曲夹命，前后三方吉集，是典型科甲状元格。  
  2. 对宫羊刃入庙，在强吉格局中转为竞争力与锋芒，而非绝对凶灾。  
  3. 命例代表「以科第极高起点进入清贵仕途」的路径。"""
    normalized_text_zh: str = """"""
    subject: str = "茅状元命"
    factor_refs: list = ['pattern_riyue_zhaoming', 'pattern_changqu_jiaming', 'pattern_sanfang_jiji', 'quality_yunwei_dagui', 'star_yangren_duigong_rumiao']
    
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
        l1_anchor="zw_v1.0.0_茅状元命_001_L1",
    )
    version: str = "1.0.0"
