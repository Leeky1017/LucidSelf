"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228441
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
    semantic_id="smth_v1.0.0_甲申水性质_自生之水其气流衍_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲申水性质自生之水其气流衍(SemanticEntry):
    """
    - **原文（source_text）**：
  甲申水、自生之水，其气流衍，宜有所归，亦藉金生，不忌众土，特嫌戊申庚子之土。

- **分字分词释义**：
  - **自生之水**：自己生长的水。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲申水、自生之水，其气流衍，宜有所归，亦藉金生，不忌众土，特嫌戊申庚子之土。

- **分字分词释义**：
  - **自生之水**：自己生长的水。
  - **其气流衍**：其气流动衍化。
  - **宜有所归**：应该有所归宿。
  - **藉金生**：依靠金来生。
  - **特嫌**：特别忌讳。

- **规范化释义（primary_lang_explained）**：
  甲申水，是自己生长的水，其气流动衍化，应该有所归宿，也依靠金来生，不忌讳众多的土，特别忌讳戊申、庚子的土。

- **完整对等诠释（secondary_lang_full）**：
  Jiashen Water is self-born water, its energy flowing-evolving, should have destination, also relies on Metal to generate, does not fear many Earths, particularly avoids Wushen and Gengzi Earth.

- **核心要点**：
  - 甲申为泉中水，自生之水
  - 气流衍需归宿
  - 藉金生、不忌众土
  - 特嫌戊申、庚子土

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_215]` `[trigger: 甲申水性质]` `[factor_trigger: jiashen_water_self_born AND energy_flowing_evolving AND relies_metal_generate]` `[role: 主干]` 甲申水、自生之水，其气流衍，宜有所归，亦藉金生，不忌众土，特嫌戊申庚子之土。 → 《三命通会》卷一#甲申水性质

- **详细解说**：
  此条解释甲申（泉中水）的性质。甲申纳音为水，是自己生长的水（申为水长生），其气流动衍化需要有归宿，依靠金来生（金生水），一般不忌讳土（因为水气旺），但特别忌讳戊申（大驿土）、庚子（壁上土）这两种土的克制。自生之水有生命力，需要合适的流向。

- **校勘与字词辨析（双语）**：
  - **中文**："自生"指申为水的长生位。"流衍"指流动演化。"有所归"指有归宿方向。"藉"同"借"，依靠。
  - **English**: "Self-born" means Shen is water's longevity position. "Flowing-evolving" means flowing and evolving. "Have destination" means having direction. "Relies on" means depends on."""
    normalized_text_zh: str = """"""
    subject: str = "甲申水性质：自生之水其气流衍"
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
        l1_anchor="smth_v1.0.0_甲申水性质_自生之水其气流衍_001_L1",
    )
    version: str = "1.0.0"
