"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228676
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
    semantic_id="smth_v1.0.0_甲寅乙卯大溪水_自病自死之水伏逆阴胜_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲寅乙卯大溪水自病自死之水伏逆阴胜(SemanticEntry):
    """
    - **原文（source_text）**：
  甲寅自病之水，乙卯自死之水，虽然死病，土不能克。盖支干二木，可以制土，若见壬寅、癸卯之金，则为优裕。五行要论云：甲寅、壬戌二水为伏逆，阴胜于阳，主奸邪...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲寅自病之水，乙卯自死之水，虽然死病，土不能克。盖支干二木，可以制土，若见壬寅、癸卯之金，则为优裕。五行要论云：甲寅、壬戌二水为伏逆，阴胜于阳，主奸邪害物，惟济之以火土损益，方成大器。

- **分字分词释义**：
  - **自病之水**：自己病弱的水。
  - **自死之水**：自己死绝的水。
  - **支干二木**：地支天干都是木。
  - **可以制土**：可以克制土。
  - **优裕**：优越富裕。
  - **伏逆**：伏藏逆乱。
  - **阴胜于阳**：阴气胜过阳气。
  - **奸邪害物**：奸邪伤害事物。
  - **损益**：损减和增益。

- **规范化释义（primary_lang_explained）**：
  甲寅是自病的水，乙卯是自死的水，虽然处于死病状态，土不能克制。因为地支天干都是木，可以克制土，如果见到壬寅、癸卯的金，就优越富裕。五行要论说：甲寅、壬戌两种水是伏藏逆乱的，阴气胜过阳气，主要表现为奸邪伤害事物，只有用火土来损减增益调和，才能成就大器。

- **完整对等诠释（secondary_lang_full）**：
  Jiayin is self-sick water, Yimao is self-dead water. Although dead-sick, Earth cannot overcome, since stems-branches both Wood, can control Earth. If seeing Renyin, Guimao Metal, then prosperous-affluent. Five Elements Essential Discourse says: Jiayin, Renxu two waters are concealed-rebellious, yin exceeds yang, governing treacherous-evil harming-things. Only aiding with Fire-Earth diminishing-augmenting, then achieves great-vessel.

- **核心要点**：
  - 甲寅乙卯为大溪水，自病自死
  - 支干二木可制土故土不克
  - 见壬寅癸卯金则优裕
  - 甲寅为伏逆水、阴胜于阳
  - 主奸邪害物、需火土损益成大器

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_242]` `[trigger: 甲寅乙卯水性质]` `[factor_trigger: jiayin_yimao_sick_dead_water AND concealed_rebellious_yin_exceeds_yang AND fire_earth_diminishing_augmenting_great_vessel]` `[role: 主干]` 甲寅自病之水，乙卯自死之水，虽然死病，土不能克。盖支干二木，可以制土，若见壬寅、癸卯之金，则为优裕。五行要论云：甲寅、壬戌二水为伏逆，阴胜于阳，主奸邪害物，惟济之以火土损益，方成大器。 → 《三命通会》卷一#甲寅乙卯水性质

- **详细解说**：
  此条详论甲寅、乙卯（大溪水）的特殊性质。甲寅自病、乙卯自死，虽处病死，但因支干皆木可制土，故土不能克。见壬寅（金箔金）、癸卯（金箔金）则优裕（金生水）。五行要论特别指出甲寅为伏逆之水，阴胜于阳，主奸邪害物，需火土损益调和才能成大器。这是论述病死水的特殊保护机制与阴阳失衡问题。

- **校勘与字词辨析（双语）**：
  - **中文**："自病"指寅为水病地。"自死"指卯为水死地。"支干二木"，甲乙为木、寅卯为木。"伏逆"指潜伏逆乱。"损益"指《易经》损卦、益卦的调和原理。
  - **English**: "Self-sick" means Yin is water's sickness position. "Self-dead" means Mao is water's death position. "Stems-branches both Wood" means Jia-Yi are wood, Yin-Mao are wood. "Concealed-rebellious" means hidden and rebellious. "Diminishing-augmenting" refers to I Ching's Sun and Yi hexagrams' harmonizing principle."""
    normalized_text_zh: str = """"""
    subject: str = "甲寅乙卯大溪水：自病自死之水伏逆阴胜"
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
        l1_anchor="smth_v1.0.0_甲寅乙卯大溪水_自病自死之水伏逆阴胜_001_L1",
    )
    version: str = "1.0.0"
