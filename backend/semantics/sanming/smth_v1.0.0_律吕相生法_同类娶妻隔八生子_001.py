"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228062
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
    semantic_id="smth_v1.0.0_律吕相生法_同类娶妻隔八生子_001",
    book_id="sanming",
    engine_id="bazi"
)
class 律吕相生法同类娶妻隔八生子(SemanticEntry):
    """
    - **原文（source_text）**：
  纳音之法，同类娶妻，隔八生子，此汉志语也。律吕相生之法也。甲子金之仲同位，娶乙丑，隔八下生壬申金之孟。壬申同位，娶癸酉，隔八上生庚辰金之季。庚辰同位娶...
    """
    
    original_text: str = """- **原文（source_text）**：
  纳音之法，同类娶妻，隔八生子，此汉志语也。律吕相生之法也。甲子金之仲同位，娶乙丑，隔八下生壬申金之孟。壬申同位，娶癸酉，隔八上生庚辰金之季。庚辰同位娶辛巳，隔八下生戊子火之仲。

- **分字分词释义**：
  - **同类娶妻**：相同类别配对。
  - **隔八生子**：相隔八位生出。
  - **汉志**：汉书律历志。
  - **律吕相生**：音律阴阳相生。
  - **金之仲**：金的中位。
  - **同位**：相同位置。
  - **下生**：向下生。
  - **上生**：向上生。
  - **金之孟**：金的初位。
  - **金之季**：金的末位。

- **规范化释义（primary_lang_explained）**：
  纳音的方法是：同类相配为夫妻，相隔八位生子，这是《汉书》的说法。这是律吕阴阳相生的方法。甲子是金的中位，与乙丑同位配对，相隔八位向下生出壬申金的初位。壬申与癸酉同位配对，相隔八位向上生出庚辰金的末位。庚辰与辛巳同位配对，相隔八位向下生出戊子火的中位。

- **完整对等诠释（secondary_lang_full）**：
  The Nayin method states: like types marry, separated by eight they bear children—this is the language of Han History. It is the method of pitch-pipe mutual generation. Jiazi is Metal's middle position, paired with Yichou in the same position, separated by eight generates downward to Renshen Metal's beginning. Renshen paired with Guiyou in the same position, separated by eight generates upward to Gengchen Metal's end. Gengchen paired with Xinsi in the same position, separated by eight generates downward to Wuzi Fire's middle.

- **核心要点**：
  - 同类娶妻：阴阳配对（甲子娶乙丑）
  - 隔八生子：相隔八位生下一纳音
  - 律吕相生法：音律阴阳相生原理
  - 上生下生交替：下生→上生→下生循环
  - 孟仲季循环：初中末三位循环

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_167]` `[trigger: 律吕相生法]` `[factor_trigger: lvlv_shengsheng AND tonglei_quqi AND gebaShengzi]` `[role: 主干]` 纳音之法，同类娶妻，隔八生子，此汉志语也。律吕相生之法也。甲子金之仲同位，娶乙丑，隔八下生壬申金之孟。 → 《三命通会》卷一#律吕相生法
  - `[ns_smth_01_170]` `[trigger: 律吕相生法]` `[factor_trigger: lvlv_shengsheng AND tonglei_quqi AND gebaShengzi]` `[role: 补充]` 纳音之法，同类娶妻，隔八生子，律吕相生之法也。甲子金之仲同位，娶乙丑，隔八下生壬申金之孟，壬申同位，娶癸酉，隔八上生庚辰金之季。 → 《三命通会》卷一#律吕相生法

- **详细解说**：
  此条详解纳音推算的核心方法“同类娶妻隔八生子”。同类娶妻：同一纳音五行的阴干支与阳干支配对，如甲子（阳）与乙丑（阴）都属金，形成"夫妻"。隔八生子：从甲子数到第八位是壬申，壬申也属金，是甲子乙丑"生"出的"子"。这样形成律吕相生链：甲子乙丑（金仲）→壬申癸酉（金孟）→庚辰辛巳（金季）→戊子己丑（火仲）。上生下生交替（下生指生下一辈，上生指生上一辈的音律术语），体现阴阳交错。孟仲季（初中末）三位循环，直到六十甲子完整。这是音律学与数理学的完美结合。

- **校勘与字词辨析（双语）**：
  - **中文**：《汉书·律历志》记载律吕相生法。"隔八"指在六十甲子序列中相隔八个位置。上生下生是音律术语。
  - **English**: "Han History: Pitch-Pipe Calendar Records" documents pitch-pipe generation methods; "separated by eight" means eight positions apart in the Sixty Jiazi sequence; shengshang/xiasheng are musical pitch generation terms."""
    normalized_text_zh: str = """"""
    subject: str = "律吕相生法：同类娶妻隔八生子"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_律吕相生法_同类娶妻隔八生子_001_L1",
    )
    version: str = "1.0.0"
