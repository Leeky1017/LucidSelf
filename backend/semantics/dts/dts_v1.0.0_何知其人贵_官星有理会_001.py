"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997801
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
    semantic_id="dts_v1.0.0_何知其人贵_官星有理会_001",
    book_id="dts",
    engine_id="bazi"
)
class 何知其人贵官星有理会(SemanticEntry):
    """
    - 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人贵：此人尊贵、地位高尚。
  - 官星：八字中代表权位与地位的星曜。
  - 有理会：配置得当、有根有位、结构自洽。

- 原注（...
    """
    
    original_text: str = """- 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人贵：此人尊贵、地位高尚。
  - 官星：八字中代表权位与地位的星曜。
  - 有理会：配置得当、有根有位、结构自洽。

- 原注（原文注解）：
 　　官星身旺而印卫官，制劫生印、财官通达、暗成官局等，皆"官星有理会"，故贵。

- 规范化释义（primary_lang_explained）：
  论一个人是否尊贵，首先看"官星是否有理会"：官星有根有位，有印以卫之，有财以生之，或暗成完整官局，使权责与身份相匹配，则多主贵。

- **核心要点**：
  - 贵与否，以官星是否得地、有卫、有源为纲；
  - 官不能孤悬，需印财相辅、格局相承；
  - “理会”包含结构、位置与流通三重含义。

- 详细解说：
  此条把“官星”作为贵贱判断的首要指标：若官星只是孤立一颗、无根无卫，或被财伤、被煞混，则难言真贵；唯有官星扎根于提纲或关键宫位，又得印星护持、财星通达，或在支中暗成官局，方能担得起长期而稳定的权位。实占时还需配合岁运，看官星在关键阶段是否被激活或损伤，以定贵格之深浅。

- 校勘与字词辨析：
  - “有理会”：不仅是“看得见”官星，更是官星在理路上说得通，有生、有卫、有用。

- **次语种完整诠释（secondary_lang_full）**：
  We know a person is noble when the Official star is properly configured: rooted, supported by Resource, well supplied by Wealth, or forming a clear, self-consistent Officer pattern. Such an Official is not just a decorative symbol but a working structure that matches real responsibility and rank."""
    normalized_text_zh: str = """"""
    subject: str = "何知其人贵，官星有理会。"
    factor_refs: list = ['nobility_grade', 'guan_xing', 'proper_meeting', 'principle_alignment', 'proper_position']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_何知其人贵_官星有理会_001_L1",
    )
    version: str = "1.0.0"
