"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228240
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
    semantic_id="smth_v1.0.0_沙中土与路旁土_001",
    book_id="sanming",
    engine_id="bazi"
)
class 沙中土与路旁土(SemanticEntry):
    """
    - **原文（source_text）**：
  丙辰丁巳，气以承阳，发生已过，成齐未来，乃曰沙中土也。庚午辛未，气当承形，物以路彰，有形可质，有物可彰，乃日路傍土也。

- **分字分词释义**：
...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙辰丁巳，气以承阳，发生已过，成齐未来，乃曰沙中土也。庚午辛未，气当承形，物以路彰，有形可质，有物可彰，乃日路傍土也。

- **分字分词释义**：
  - **沙中土**：沙子中的土。
  - **气以承阳**：气承接阳气。
  - **发生已过**：发生阶段已过。
  - **成齐未来**：成熟阶段未到。
  - **气当承形**：气正当承接形体。
  - **物以路彰**：事物因道路而彰显。
  - **有形可质**：有形体可以质询。
  - **有物可彰**：有事物可以彰显。

- **规范化释义（primary_lang_explained）**：
  丙辰丁巳，气承接阳气，发生阶段已过，成熟阶段未到，就叫沙中土。庚午辛未，气正当承接形体，事物因道路而彰显，有形体可以质询，有事物可以彰显，就叫路旁土。

- **完整对等诠释（secondary_lang_full）**：
  Bingchen-Dingsi: qi receiving yang, generation phase passed, maturation phase not yet arrived, thus called Sand-Center Earth. Gengwu-Xinwei: qi at form-receiving moment, things manifest through pathways, having form that can be examined, having things that can be manifest, thus called Roadside Earth.

- **核心要点**：
  - 丙辰丁巳：沙中土（发生已过，成齐未来）
  - 庚午辛未：路旁土（气当承形，物以路彰）
  - 沙中土为土的过渡阶段
  - 路旁土为土的显化承载

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_189]` `[trigger: 沙中土与路旁土]` `[factor_trigger: sand_center_earth AND roadside_earth AND nayin_earth_transitional]` `[role: 主干]` 丙辰丁巳，气以承阳，发生已过，成齐未来，乃曰沙中土也。庚午辛未，气当承形，物以路彰，有形可质，有物可彰，乃曰路旁土也。 → 《三命通会》卷一#沙中土与路旁土

- **详细解说**：
  此条续解土纳音。丙辰丁巳为"沙中土"：辰巳属春夏之交，土气承阳，处于发生已过、成熟未到的过渡期，如沙中之土，最为润泽（土润则生），这是土的过渡状态。庚午辛未为"路旁土"：午未属夏季，土气承形，万物在路旁显现（播殖百谷），如道路两旁的土地，承载万物，这是土的显化功能。从壁上土（封闭）→城头土（育物）→沙中土（润泽）→路旁土（承载），体现了土从封闭到育物再到承载的过程。命理上，沙中土命格润泽有潜力，路旁土命格显达承载。

- **校勘与字词辨析（双语）**：
  - **中文**："沙中土"为土中最润者，土润则生。"发生已过成齐未来"指处于中间过渡期。"路旁土"指道路两旁的土地，播殖百谷。"气当承形"指气承接形体的时候。
  - **English**: "Sand-Center Earth" is most moist among earths, moist earth generates life. "Generation passed maturation not arrived" means in transitional middle phase. "Roadside Earth" refers to land alongside roads, sowing hundred grains. "Qi at form-receiving" means when qi receives physical form."""
    normalized_text_zh: str = """"""
    subject: str = "沙中土与路旁土"
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
        l1_anchor="smth_v1.0.0_沙中土与路旁土_001_L1",
    )
    version: str = "1.0.0"
