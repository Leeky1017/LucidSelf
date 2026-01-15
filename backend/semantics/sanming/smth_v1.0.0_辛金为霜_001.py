"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042606
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
    semantic_id="smth_v1.0.0_辛金为霜_001",
    book_id="sanming",
    engine_id="bazi"
)
class 辛金为霜(SemanticEntry):
    """
    - **原文（source_text）**：
  辛金为霜。八月，辛金建禄之地，是月也天气肃杀，白露为霜，草木黄落而衰，故五行阴木绝在此地，若木经斧斤之斩伐，未有所生焉者也。斧斤以时入山林，严霜以时杀...
    """
    
    original_text: str = """- **原文（source_text）**：
  辛金为霜。八月，辛金建禄之地，是月也天气肃杀，白露为霜，草木黄落而衰，故五行阴木绝在此地，若木经斧斤之斩伐，未有所生焉者也。斧斤以时入山林，严霜以时杀草木，揆之天道，参之人事，信乎辛金之为霜矣。如辛人坐卯，未透乙，大富；坐亥透丙则贵。爱冬生。

- **分字分词释义**：
  - **肃杀、白露为霜**：霜喻辛金肃杀之力，能终结不合时宜之生长。
  - **阴木绝地**：阴木在此地绝，象征柔木于严霜之下难存。
  - **斧斤以时入山林**：比喻辛金之断割需合时令，过与不及皆非。

- **规范化释义（primary_lang_explained）**：
  辛金如秋霜：天气肃杀，白露凝霜，草木黄落。此时阴木之气在五行中绝，柔弱之木难耐霜寒。霜若得其时，则是「以时杀伐」，使万物有节；若失其时，则为摧残。辛日命人坐卯、未透乙，多主富实；坐亥透丙，则偏于贵显，整体偏爱寒令，以衬出霜之清劲。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal is compared to autumn frost: thin, cold crystals that end the growing season. At this point in the year yin Wood has reached its limit and can no longer endure the chill, so tender shoots wither while mature structures harden. When frost comes in its proper season it is a necessary pruning, preventing decay and forcing completion; when it arrives too early or too strong it becomes mere damage. In Xin‑day charts the placements the text praises—sitting on Mao without exposed Yi, or on Hai with Bing—show how this frost can either secure solid wealth or refine status and reputation, especially under cold‑season skies that set off its clean sharpness. The lesson is that Xin’s cutting power should be read as a tool for timely termination and refinement, not as a licence for indiscriminate harshness; whether it protects or harms depends entirely on timing, intensity, and what kind of growth it is freezing."""
    normalized_text_zh: str = """"""
    subject: str = "辛金为霜"
    factor_refs: list = []
    
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
        l1_anchor="smth_v1.0.0_辛金为霜_001_L1",
    )
    version: str = "1.0.0"
