"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228464
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
    semantic_id="smth_v1.0.0_丁亥土性质_临官之土木不能克_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丁亥土性质临官之土木不能克(SemanticEntry):
    """
    - **原文（source_text）**：
  丁亥土、临官之土，木不能克，嫌金多，须得火生救之乃吉。忌己亥、辛卯之木。

- **分字分词释义**：
  - **临官之土**：临官位的土。
  -...
    """
    
    original_text: str = """- **原文（source_text）**：
  丁亥土、临官之土，木不能克，嫌金多，须得火生救之乃吉。忌己亥、辛卯之木。

- **分字分词释义**：
  - **临官之土**：临官位的土。
  - **木不能克**：木不能克制。
  - **嫌金多**：忌讳金太多。
  - **火生救之**：火生来救助。

- **规范化释义（primary_lang_explained）**：
  丁亥土，是临官位的土，木不能克制，忌讳金太多，必须得到火生来救助才吉利。忌讳己亥、辛卯的木。

- **完整对等诠释（secondary_lang_full）**：
  Dinghai Earth is official-position earth, Wood cannot overcome, dislikes excess Metal, must obtain Fire generation to rescue for auspiciousness. Avoids Jihai and Xinmao Wood.

- **核心要点**：
  - 丁亥为屋上土，临官之土
  - 木不能克
  - 嫌金多需火救
  - 忌己亥、辛卯木

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_218]` `[trigger: 丁亥土性质]` `[factor_trigger: dinghai_earth_official AND wood_cannot_overcome AND fire_generation_rescue]` `[role: 主干]` 丁亥土、临官之土，木不能克，嫌金多，须得火生救之乃吉。忌己亥、辛卯之木。 → 《三命通会》卷一#丁亥土性质

- **详细解说**：
  此条解释丁亥（屋上土）的性质。丁亥纳音也是土，是临官位的土（亥为木临官，但土在此不畏木克），木不能克制，但忌讳金太多（金泄土气），必须得到火来生土救助才吉利，忌讳己亥（平地木）、辛卯（松柏木）等木的克制。土需火生金不宜多。

- **校勘与字词辨析（双语）**：
  - **中文**："临官"为十二长生之一，主旺盛。"嫌"指忌讳。"火生救之"指火生土来救助。
  - **English**: "Official-position" is one of Twelve Longevity stages, indicating prosperity. "Dislikes" means avoids. "Fire generation to rescue" means Fire generates Earth to help."""
    normalized_text_zh: str = """"""
    subject: str = "丁亥土性质：临官之土木不能克"
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
        l1_anchor="smth_v1.0.0_丁亥土性质_临官之土木不能克_001_L1",
    )
    version: str = "1.0.0"
