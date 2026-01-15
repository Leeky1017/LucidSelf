"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227535
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
    semantic_id="smth_v1.0.0_十干体系与阴阳方位_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十干体系与阴阳方位(SemanticEntry):
    """
    - **原文（source_text）**：
  天气始于甲干，地气始于干支者，乃圣人究乎阴阳重轻之用也。著名以彰其德，立号以表其事。由是于甲相合，然后成纪，远可步于岁而统六十年，近可推于日而明十二时...
    """
    
    original_text: str = """- **原文（source_text）**：
  天气始于甲干，地气始于干支者，乃圣人究乎阴阳重轻之用也。著名以彰其德，立号以表其事。由是于甲相合，然后成纪，远可步于岁而统六十年，近可推于日而明十二时。岁运之盈虚，气令之早晏，万物生死，将今验古，或得而知之，则精微之义，可谓大矣哉。

- 分字分词释义：
  - **天气始于甲干，地气始于干支**：十干、干支是承载天、地气机的最基础记号，不是随意命名。
  - **著名以彰其德，立号以表其事**：通过命名来标明每一个干的德性与所主之事。
  - **远可步于岁，近可推于日**：同一套十干体系，同时适用于纪年与纪日，贯通大、小时间尺度。

- **规范化释义（primary_lang_explained）**：
  这一段总论十干制度的意义：十干并非单纯记号，而是用来承载天地阴阳轻重之用的框架。圣人给每一干立名，是为了显出它的德性与职掌，使人可以用这一套符号来推步岁运与日时，观察气令早晚、万物生死，从而在理与数之间搭起桥梁。

- **完整对等诠释（secondary_lang_full）**：

  This concluding remark on the Ten Heavenly Stems stresses that they are not arbitrary codes but a framework for carrying the operations of Heaven and Earth. "Heavenly Qi begins with Jia" and "Earthly Qi begins with the stems and branches" means that change is tracked and expressed through this system. The sages gave each stem a name to reveal its particular virtue and function, so that people could use these symbols to project the rise and fall of yearly and daily cycles, to see whether Qi arrives early or late, and to observe the life and death of things. In doing so they built a bridge between principle and number: the stems simultaneously encode temporal sequence and qualitative character. In destiny analysis, reading the stems is thus reading how time, direction and moral tenor are woven together, not merely processing a string of numerical indices."""
    normalized_text_zh: str = """"""
    subject: str = "十干体系与阴阳方位"
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
        l1_anchor="smth_v1.0.0_十干体系与阴阳方位_001_L1",
    )
    version: str = "1.0.0"
