"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228501
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
    semantic_id="smth_v1.0.0_癸亥水性质_百川喜金土火_001",
    book_id="sanming",
    engine_id="bazi"
)
class 癸亥水性质百川喜金土火(SemanticEntry):
    """
    - **原文（source_text）**：
  癸亥水、百川喜金土火，伏马大败，破字截路。

- **分字分词释义**：
  - **百川**：百川汇聚。
  - **喜金土火**：喜欢金土火。
 ...
    """
    
    original_text: str = """- **原文（source_text）**：
  癸亥水、百川喜金土火，伏马大败，破字截路。

- **分字分词释义**：
  - **百川**：百川汇聚。
  - **喜金土火**：喜欢金土火。
  - **伏马**：伏马煞。
  - **截路**：截路煞。

- **规范化释义（primary_lang_explained）**：
  癸亥水，是百川汇聚，喜欢金、土、火，忌讳伏马煞、大败煞、破字煞、截路煞。

- **完整对等诠释（secondary_lang_full）**：
  Guihai Water is hundred rivers converging, favors Metal, Earth, Fire, avoids Concealed-Horse sha, Great-Defeat sha, Broken-Character sha, Road-Blocking sha.

- **核心要点**：
  - 癸亥为大海水，如百川
  - 喜金（金生）、土（土制）、火（火暖）
  - 忌伏马、大败、破字、截路

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_223]` `[trigger: 癸亥水性质]` `[factor_trigger: guihai_water_hundred_rivers AND favor_metal_earth_fire AND concealed_horse_blocking]` `[role: 主干]` 癸亥水、百川喜金土火，伏马大败，破字截路。 → 《三命通会》卷一#癸亥水性质

- **详细解说**：
  此条解释癸亥（大海水）的性质。癸亥纳音也是水，如百川汇聚，喜欢金（金生水有源）、土（土制水不泛滥）、火（火暖水有情），但忌伏马煞、大败煞、破字煞、截路煞等凶煞。百川汇聚需要金生、土制、火暖的平衡。

- **校勘与字词辨析（双语）**：
  - **中文**："百川"指众多河流汇聚。"伏马"为伏马煞，主潜伏不显。"截路"为截路煞，主阻滞。
  - **English**: "Hundred rivers converging" refers to many rivers gathering. "Concealed-Horse" is Concealed-Horse sha, indicating hidden and inactive. "Road-Blocking" is Road-Blocking sha, indicating obstruction."""
    normalized_text_zh: str = """"""
    subject: str = "癸亥水性质：百川喜金土火"
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
        l1_anchor="smth_v1.0.0_癸亥水性质_百川喜金土火_001_L1",
    )
    version: str = "1.0.0"
