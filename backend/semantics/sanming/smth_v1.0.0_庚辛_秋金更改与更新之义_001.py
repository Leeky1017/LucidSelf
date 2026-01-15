"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227570
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
    semantic_id="smth_v1.0.0_庚辛_秋金更改与更新之义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 庚辛秋金更改与更新之义(SemanticEntry):
    """
    - **原文（source_text）**：
  庚辛其位金，行秋之令。庚，更也，万物肃然更改。辛，新也，秀实新成。

- 分字分词释义：
  - **庚，更也**：更张、改革之意，主大幅调整与裁断。...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚辛其位金，行秋之令。庚，更也，万物肃然更改。辛，新也，秀实新成。

- 分字分词释义：
  - **庚，更也**：更张、改革之意，主大幅调整与裁断。
  - **辛，新也**：新成、新实之意，主成熟之后的定型与更新。

- **规范化释义（primary_lang_explained）**：
  庚辛配秋金：庚金着重「更」，像秋收时的大斧大刀，肃杀而更张旧局；辛金着重「新」，像成熟后的果实与金器，定型、锋利而带辛味。秋金之用，一在肃、一在成，把一年的生长收束为可用之形。

- **完整对等诠释（secondary_lang_full）**：

  Geng and Xin are the Metals of autumn. Geng centres on the idea of “geng”, to change and renew: it is like the great axe or blade at harvest time, cutting back growth, clearing away what is no longer needed and sternly revising the old arrangement. Xin centres on “xin”, new: it is like the fully formed fruit or finished metal vessel, sharp, refined and carrying a biting taste. Thus autumn Metal works in two directions at once—severing and completing. In practice, Geng Metal in a chart points to structural reform, tough decisions and breaking with what has become outdated, while Xin Metal points to evaluation, quality control, aesthetics and the final fixing of shape and value."""
    normalized_text_zh: str = """"""
    subject: str = "庚辛：秋金更改与更新之义"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_庚辛_秋金更改与更新之义_001_L1",
    )
    version: str = "1.0.0"
