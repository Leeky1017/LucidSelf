"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227963
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
    semantic_id="smth_v1.0.0_十干阴阳配属总结_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十干阴阳配属总结(SemanticEntry):
    """
    - **原文（source_text）**：
  盖天地之数，甲丙、戊庚壬为阳，乙、丁、己辛癸为阴，五行各一阴一阳，故有十日也。

- **分字分词释义**：
  - **天地之数**：天地的数理。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  盖天地之数，甲丙、戊庚壬为阳，乙、丁、己辛癸为阴，五行各一阴一阳，故有十日也。

- **分字分词释义**：
  - **天地之数**：天地的数理。
  - **五行各一阴一阳**：每个五行都有一阴一阳。
  - **故有十日**：所以有十天干。

- **规范化释义（primary_lang_explained）**：
  天地的数理中，甲丙戊庚壬为阳，乙丁己辛癸为阴，五行各有一阴一阳，所以有十个天干。

- **完整对等诠释（secondary_lang_full）**：
  In the numbers of Heaven and Earth, Jia-Bing-Wu-Geng-Ren are yang; Yi-Ding-Ji-Xin-Gui are yin. Each of the Five Elements has one yang and one yin, thus there are Ten Days (Stems).

- **核心要点**：
  - 甲丙戊庚壬为五阳干
  - 乙丁己辛癸为五阴干
  - 五行各一阴一阳
  - 共成十天干

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_154]` `[trigger: 十干阴阳配属总结]` `[factor_trigger: five_yang_stems AND five_yin_stems AND tiangan_system]` `[role: 主干]` 盖天地之数，甲丙戊庚壬为阳，乙丁己辛癸为阴，五行各一阴一阳，故有十日也。 → 《三命通会》卷一#十干阴阳配属总结

- **详细解说**：
  此条总结十天干的阴阳配属。木火土金水五行，每行各有一阳干一阴干：甲阳乙阴（木），丙阳丁阴（火），戊阳己阴（土），庚阳辛阴（金），壬阳癸阴（水）。五行各配阴阳，共成十干。这是天地数理的体现，也是阴阳平衡的原则。每对阴阳天干虽属同一五行，但阴阳属性不同，功能和象征各有差异，形成完整的干支体系。这为后续十二地支的阴阳配属奠定基础。

- **校勘与字词辨析（双语）**：
  - **中文**："十日"即十天干，以日纪时。阳干为甲丙戊庚壬，阴干为乙丁己辛癸。
  - **English**: "Ten Days" refers to Ten Heavenly Stems used for day counting; yang Stems are Jia-Bing-Wu-Geng-Ren; yin Stems are Yi-Ding-Ji-Xin-Gui."""
    normalized_text_zh: str = """"""
    subject: str = "十干阴阳配属总结"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_十干阴阳配属总结_001_L1",
    )
    version: str = "1.0.0"
