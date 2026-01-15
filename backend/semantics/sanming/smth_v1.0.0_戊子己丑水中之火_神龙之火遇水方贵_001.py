"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228518
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
    semantic_id="smth_v1.0.0_戊子己丑水中之火_神龙之火遇水方贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊子己丑水中之火神龙之火遇水方贵(SemanticEntry):
    """
    - **原文（source_text）**：
  五行要论云：戊子含精神辉光全实之气，作四时保生之福，入贵格，则为大人君子，器字含弘，富贵终吉。己丑为天将之火，又为天乙本家，含威福光厚之气，发越峻猛，...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行要论云：戊子含精神辉光全实之气，作四时保生之福，入贵格，则为大人君子，器字含弘，富贵终吉。己丑为天将之火，又为天乙本家，含威福光厚之气，发越峻猛，贵局乘之，为将德、为魁名而建功。

- **分字分词释义**：
  - **精神辉光全实之气**：精神辉煌光辉全面充实的气质。
  - **四时保生之福**：四季保护生命的福气。
  - **器字含弘**：器量宏大。
  - **天将之火**：天将星的火。
  - **天乙本家**：天乙贵人的本位。
  - **威福光厚之气**：威严福德光明深厚的气质。
  - **发越峻猛**：发扬迅速而猛烈。

- **规范化释义（primary_lang_explained）**：
  五行要论说：戊子火包含精神辉煌光辉全面充实的气质，是四季保护生命的福气。如果入贵格，就能成为大人君子，器量宏大，富贵善终。己丑火是天将星的火，又是天乙贵人的本位，包含威严福德光明深厚的气质，发扬迅速而猛烈。如果贵格乘之，就能成为将德、魁名而建功立业。

- **完整对等诠释（secondary_lang_full）**：
  Five Elements Essential Discourse says: Wuzi Fire contains spirit-brilliance radiant-complete substantial energy, serving as four-seasons life-protecting blessing. Entering noble pattern becomes great person-gentleman, magnanimous capacity, wealth-nobility ending auspiciously. Jichou Fire is Heaven-General fire, also Heavenly-Yi home position, contains mighty-blessed bright-abundant energy, manifesting swift-fierce. Noble pattern riding it becomes General-Virtue, Chief-Fame establishing achievements.

- **核心要点**：
  - 戊子火（霹雳火）包含精神辉光
  - 四时保生、器字含弘
  - 己丑火（霹雳火）为天将、天乙本家
  - 威福光厚、发越峻猛
  - 入贵格为将德魁名

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_225]` `[trigger: 戊子己丑火详论]` `[factor_trigger: wuzi_spirit_brilliance AND jichou_heaven_general AND four_seasons_blessing]` `[role: 主干]` 五行要论云：戊子含精神辉光全实之气，作四时保生之福，入贵格，则为大人君子，器字含弘，富贵终吉。己丑为天将之火，又为天乙本家，含威福光厚之气，发越峻猛，贵局乘之，为将德、为魁名而建功。 → 《三命通会》卷一#戊子己丑火详论

- **详细解说**：
  此条分论戊子、己丑（霹雳火）各自的特点。戊子火精神辉煌，是四季保生的福气，入贵格则器量宏大、富贵终吉。己丑火是天将之火，又为天乙贵人本位，威福光厚，发越峻猛，入贵格则成将德魁名。两者都是神龙之火，但各有侧重：戊子重在精神气质，己丑重在威猛建功。这是霹雳火的详细格局论述。

- **校勘与字词辨析（双语）**：
  - **中文**："辉光全实"指光辉充实。"四时保生"指四季护佑生命。"器字含弘"指器量宏大。"天将"为星宿名。"发越"指发扬显现。
  - **English**: "Radiant-complete substantial" means brilliance full. "Four-seasons life-protecting" means protecting life throughout seasons. "Magnanimous capacity" means great capacity. "Heaven-General" is star name. "Manifesting" means revealing."""
    normalized_text_zh: str = """"""
    subject: str = "戊子己丑水中之火：神龙之火遇水方贵"
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
        l1_anchor="smth_v1.0.0_戊子己丑水中之火_神龙之火遇水方贵_001_L1",
    )
    version: str = "1.0.0"
