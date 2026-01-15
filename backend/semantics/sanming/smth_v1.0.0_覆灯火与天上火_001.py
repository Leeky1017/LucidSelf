"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228217
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
    semantic_id="smth_v1.0.0_覆灯火与天上火_001",
    book_id="sanming",
    engine_id="bazi"
)
class 覆灯火与天上火(SemanticEntry):
    """
    - **原文（source_text）**：
  甲辰乙巳，气形盛地，势定高冈，传明继晦，子母相承，乃曰覆灯火也。戊午己未，气过阳宫，重离相会，炳灵交光，发辉炎上，乃曰天上火也。

- **分字分词释...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲辰乙巳，气形盛地，势定高冈，传明继晦，子母相承，乃曰覆灯火也。戊午己未，气过阳宫，重离相会，炳灵交光，发辉炎上，乃曰天上火也。

- **分字分词释义**：
  - **覆灯火**：罩着灯罩的灯火。
  - **气形盛地**：气形旺盛的地方。
  - **势定高冈**：势头确定在高岗。
  - **传明继晦**：传递光明接续昏暗。
  - **子母相承**：子时母时相互承接。
  - **气过阳宫**：气经过阳宫（午位）。
  - **重离相会**：两个离卦相会。
  - **炳灵交光**：明亮的灵光交相辉映。
  - **发辉炎上**：发出光辉向上炎升。

- **规范化释义（primary_lang_explained）**：
  甲辰乙巳，气形旺盛的地方，势头确定在高岗，传递光明接续昏暗，子时母时相互承接，就叫覆灯火。戊午己未，气经过阳宫，两个离卦相会，明亮的灵光交相辉映，发出光辉向上炎升，就叫天上火。

- **完整对等诠释（secondary_lang_full）**：
  Jiachen-Yisi: qi-form flourishing ground, momentum fixed on high ridge, transmitting brightness continuing through darkness, child-mother mutually succeeding, thus called Covered-Lamp Fire. Wuwu-Jiwei: qi passing through yang palace, double Li meeting, radiant spirits crossing illumination, radiating brilliance flaming upward, thus called Heaven-Above Fire.

- **核心要点**：
  - 甲辰乙巳：覆灯火（势定高冈，传明继晦）
  - 戊午己未：天上火（重离相会，发辉炎上）
  - 覆灯火为火的持续照明
  - 天上火为火的极盛炎上

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_186]` `[trigger: 覆灯火与天上火]` `[factor_trigger: covered_lamp_fire AND heaven_above_fire AND nayin_fire_flourishing]` `[role: 主干]` 甲辰乙巳，气形盛地，势定高冈，传明继晦，子母相承，乃曰覆灯火也。戊午己未，气过阳宫，重离相会，炳灵交光，发辉炎上，乃曰天上火也。 → 《三命通会》卷一#覆灯火与天上火

- **详细解说**：
  此条续解火纳音。甲辰乙巳为"覆灯火"：辰为土库，巳为火旺，火在高处如灯，有灯罩遮覆，传明继晦（白天黑夜都照明），子母相承（持续不断），这是火的照明功用。戊午己未为"天上火"：午未为火土极旺之地，两离相会（离为火），火光炽盛，炎上升腾如太阳，这是火的极盛状态。从霹雳火（神异）→炉中火（冶炼）→覆灯火（照明）→天上火（极盛），体现了火从罕见到实用再到极盛的过程。命理上，覆灯火命格持续稳定，天上火命格炽热显耀。

- **校勘与字词辨析（双语）**：
  - **中文**："覆灯火"指有灯罩的灯火。"传明继晦"指持续照明。"重离相会"，离为火卦，重离指午未火旺。"炳灵"指明亮的灵光。"炎上"是火的性质，向上燃烧。
  - **English**: "Covered-Lamp Fire" refers to lamp with shade. "Transmitting brightness continuing darkness" means continuous illumination. "Double Li meeting"—Li is Fire trigram, double Li means Wu-Wei fire prosperity. "Radiant spirits" means bright spiritual light. "Flaming upward" is fire's nature, burning upward."""
    normalized_text_zh: str = """"""
    subject: str = "覆灯火与天上火"
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
        l1_anchor="smth_v1.0.0_覆灯火与天上火_001_L1",
    )
    version: str = "1.0.0"
