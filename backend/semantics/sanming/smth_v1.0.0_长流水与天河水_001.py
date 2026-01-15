"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228190
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
    semantic_id="smth_v1.0.0_长流水与天河水_001",
    book_id="sanming",
    engine_id="bazi"
)
class 长流水与天河水(SemanticEntry):
    """
    - **原文（source_text）**：
  壬辰癸巳，势极东南，气傍离宫，火明势盛，水得归库，盈科后进，乃曰长流水也。丙午丁未，气当升降，在高明火位有水，沛然作霖，以济火中之水，惟天上乃有，故曰...
    """
    
    original_text: str = """- **原文（source_text）**：
  壬辰癸巳，势极东南，气傍离宫，火明势盛，水得归库，盈科后进，乃曰长流水也。丙午丁未，气当升降，在高明火位有水，沛然作霖，以济火中之水，惟天上乃有，故曰天河水。

- **分字分词释义**：
  - **势极东南**：水势到达东南极点。
  - **气傍离宫**：气靠近离宫（南方火位）。
  - **火明势盛**：火光明亮势头旺盛。
  - **水得归库**：水得以归入库藏。
  - **盈科后进**：充满沟渠然后前进。
  - **气当升降**：气正当升降之时。
  - **高明火位**：高处明亮的火位。
  - **沛然作霖**：充沛地降下甘霖。
  - **以济火中之水**：来补济火中的水。

- **规范化释义（primary_lang_explained）**：
  壬辰癸巳，水势到达东南极点，气靠近离宫（南方），火光明亮势头旺盛，水得以归入库藏，充满沟渠然后前进，就叫长流水。丙午丁未，气正当升降之时，在高处明亮的火位有水，充沛地降下甘霖，来补济火中的水，只有天上才有，所以叫天河水。

- **完整对等诠释（secondary_lang_full）**：
  Renchen-Guisi: water's momentum reaching southeastern extreme, qi approaching Li Palace (south), fire bright and force flourishing, water gaining library storage, filling channels then advancing, thus called Long-Flowing Water. Bingwu-Dingwei: qi at ascending-descending moment, water existing at high bright fire position, abundantly forming sweet rain, relieving water amid fire, only existing in Heaven above, thus called Celestial-River Water.

- **核心要点**：
  - 壬辰癸巳：长流水（势极东南，盈科后进）
  - 丙午丁未：天河水（气当升降，沛然作霖）
  - 长流水为水的持续奔流
  - 天河水为水的高悬天际

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_183]` `[trigger: 长流水与天河水]` `[factor_trigger: long_flowing_water AND celestial_river_water AND nayin_water_continuous]` `[role: 主干]` 壬辰癸巳，势极东南，水得归库，盈科后进，乃曰长流水也。丙午丁未，气当升降，在高明火位有水，沛然作霖，惟天上乃有，故曰天河水。 → 《三命通会》卷一#长流水与天河水

- **详细解说**：
  此条续解水纳音。壬辰癸巳为"长流水"：辰为水库，巳为火旺之地，水势到达东南，虽近火位但水归库藏，充满沟渠持续前进，如长江大河般源源不断，这是水的充沛持续状态。丙午丁未为"天河水"：午未为火土旺地，在火位高处竟有水，如天上银河、天降甘霖，补济火中之水，取其高悬天际之象。从涧下水（潜流）→大溪水（奔流）→长流水（持续）→天河水（高悬），体现了水从地下到地表、从奔流到高悬的过程。命理上，长流水命格持久有力，天河水命格高贵清澈。

- **校勘与字词辨析（双语）**：
  - **中文**："长流水"指持续流动的水。"盈科后进"出自《孟子》，形容水充满坑洼后继续前进。"天河水"指天上银河、甘霖。"沛然"形容水量充沛。
  - **English**: "Long-Flowing Water" refers to continuously flowing water. "Filling channels then advancing" from Mencius, describes water filling depressions before continuing. "Celestial-River Water" refers to heavenly Milky Way, sweet rain. "Abundantly" describes plentiful water volume."""
    normalized_text_zh: str = """"""
    subject: str = "长流水与天河水"
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
        l1_anchor="smth_v1.0.0_长流水与天河水_001_L1",
    )
    version: str = "1.0.0"
