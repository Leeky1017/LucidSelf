"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228135
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
    semantic_id="smth_v1.0.0_海中金与金泊金_001",
    book_id="sanming",
    engine_id="bazi"
)
class 海中金与金泊金(SemanticEntry):
    """
    - **原文（source_text）**：
  详此十有二位，先后六十甲子，可以次第而晓。甲子乙丑何以取象为海中之金？盖气在包藏，有名无形，犹人之在母腹也。壬寅癸卯，绝地存金，气尚柔弱，薄若缯缟，故...
    """
    
    original_text: str = """- **原文（source_text）**：
  详此十有二位，先后六十甲子，可以次第而晓。甲子乙丑何以取象为海中之金？盖气在包藏，有名无形，犹人之在母腹也。壬寅癸卯，绝地存金，气尚柔弱，薄若缯缟，故曰金泊金。

- **分字分词释义**：
  - **次第而晓**：按顺序可以明白。
  - **海中之金**：海中的金，指甲子乙丑纳音。
  - **气在包藏**：气在包裹隐藏中。
  - **有名无形**：有其名但无形体。
  - **绝地存金**：在绝地中存留的金。
  - **缯缟**：细绸白绢，形容薄。

- **规范化释义（primary_lang_explained）**：
  详察这十二个位置，依次排列六十甲子，可以按顺序明白。甲子乙丑为什么取象为海中的金？因为气在包藏之中，有其名称但没有形体，就像人在母亲腹中一样。壬寅癸卯，在绝地中存留的金，气还很柔弱，薄得像细绸白绢，所以叫金泊金。

- **完整对等诠释（secondary_lang_full）**：
  Examining these twelve positions in detail, the sixty Jiazi arranged in sequence can be understood in order. Why do Jiazi-Yichou symbolize Sea-Center Metal? Because their qi resides in concealment—having name but no form, like humans in mother's womb. Renyin-Guimao: Metal existing in extinction-ground, qi still soft and weak, thin as fine silk gauze, thus called Gold-Foil Metal.

- **核心要点**：
  - 甲子乙丑：海中金（气在包藏，有名无形）
  - 壬寅癸卯：金泊金（绝地存金，薄若缯缟）
  - 海中金如胎儿在母腹
  - 金泊金如薄弱的金箔

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_176]` `[trigger: 海中金与金泊金]` `[factor_trigger: sea_center_metal AND gold_foil_metal AND nayin_metal]` `[role: 主干]` 甲子乙丑何以取象为海中之金？盖气在包藏，有名无形，犹人之在母腹也。壬寅癸卯，绝地存金，气尚柔弱，薄若缯缟，故曰金泊金。 → 《三命通会》卷一#海中金与金泊金

- **详细解说**：
  此条开始详解六十甲子纳音。甲子乙丑为"海中金"：子为水旺之地，丑为土旺之地，金在水土之中被包藏，就像金矿沉在海底，有金之名而无金之形，正如胎儿在母腹中，虽是生命但未成形。壬寅癸卯为"金泊金"：寅卯为木旺之地，是金的"绝地"（五行相克），金在这里极其柔弱，薄得像金箔纸，如同细绸白绢。这两种金都处于初始阶段，海中金是完全隐藏，金泊金是刚刚显现但极弱。体现了纳音五行不同于正五行，有具体的形态和力量差异。

- **校勘与字词辨析（双语）**：
  - **中文**："海中金"指甲子乙丑纳音属金，因子属水、丑属土，金在水土中如海中之金。"金泊金"又作"金箔金"，泊即薄，形容金极薄。"绝地"指五行的绝位，寅卯木旺则金绝。
  - **English**: "Sea-Center Metal" refers to Jiazi-Yichou Nayin Metal, because Zi is Water and Chou is Earth—Metal in water-earth like metal in the sea. "Gold-Foil Metal" also written as gold leaf, "bo" means thin, describing extremely thin metal. "Extinction-ground" refers to Five Element exhaustion position—Yin-Mao Wood prosperity means Metal extinction."""
    normalized_text_zh: str = """"""
    subject: str = "海中金与金泊金"
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
        l1_anchor="smth_v1.0.0_海中金与金泊金_001_L1",
    )
    version: str = "1.0.0"
