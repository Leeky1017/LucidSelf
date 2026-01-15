"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228398
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
    semantic_id="smth_v1.0.0_戊寅土性质_受伤之土最为无力_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊寅土性质受伤之土最为无力(SemanticEntry):
    """
    - **原文（source_text）**：
  戊寅土、堤阜城郭，喜木及火伏神棒杖聋哑。

- **分字分词释义**：
  - **堤阜城郭**：堤坝丘陵城墙。
  - **喜木及火**：喜欢木和火...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊寅土、堤阜城郭，喜木及火伏神棒杖聋哑。

- **分字分词释义**：
  - **堤阜城郭**：堤坝丘陵城墙。
  - **喜木及火**：喜欢木和火。
  - **伏神**：伏神煞。
  - **棒杖**：棒杖煞。

- **规范化释义（primary_lang_explained）**：
  戊寅土，是堤坝丘陵城墙之土，喜欢木和火，忌讳伏神煞、棒杖煞、聋哑煞。

- **完整对等诠释（secondary_lang_full）**：
  Wuyin Earth is dike-mound-rampart earth, favoring Wood and Fire, avoiding Concealed-Spirit sha, Club-Staff sha, and Deaf-Mute sha.

- **核心要点**：
  - 戊寅为城头土，如堤阜城郭
  - 喜木（木克土成形）、火（火生土）
  - 忌伏神、棒杖、聋哑

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_209]` `[trigger: 戊寅土性质]` `[factor_trigger: wuyin_earth_rampart AND favor_wood_fire AND concealed_spirit]` `[role: 主干]` 戊寅土、堤阜城郭，喜木及火伏神棒杖聋哑。 → 《三命通会》卷一#戊寅土性质

- **详细解说**：
  此条解释戊寅（城头土）的性质。戊寅纳音为土，如堤坝丘陵城墙，喜欢木（木能使土成形，如建筑材料）和火（火生土），但忌伏神煞、棒杖煞、聋哑煞等凶煞。城头土需要木火配合才能成就功用。

- **校勘与字词辨析（双语）**：
  - **中文**："堤阜城郭"指堤坝、丘陵、城墙等土建工程。"木及火"，木为材料，火为生土。
  - **English**: "Dike-mound-rampart" refers to dikes, mounds, and city walls—earthworks. "Wood and Fire"—wood as material, fire generates earth."""
    normalized_text_zh: str = """"""
    subject: str = "戊寅土性质：受伤之土最为无力"
    factor_refs: list = ['new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_戊寅土性质_受伤之土最为无力_001_L1",
    )
    version: str = "1.0.0"
