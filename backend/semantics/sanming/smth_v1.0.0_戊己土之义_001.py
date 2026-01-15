"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227942
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
    semantic_id="smth_v1.0.0_戊己土之义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊己土之义(SemanticEntry):
    """
    - **原文（source_text）**：
  戊己其位，土，行周四季。戊，阳土也，万物生而出之，万物伐而入之。己，阴土也，无所为而得己者也。又云：戊，茂也。己，起也。土行四季之末，万物含秀者抑屈而...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊己其位，土，行周四季。戊，阳土也，万物生而出之，万物伐而入之。己，阴土也，无所为而得己者也。又云：戊，茂也。己，起也。土行四季之末，万物含秀者抑屈而起也。

- **分字分词释义**：
  - **行周四季**：运行于四季之末。
  - **生而出之**：生长而出土。
  - **伐而入之**：收割而入土。
  - **无所为而得己**：无需作为而自成。
  - **茂**：繁茂。
  - **起**：兴起。
  - **含秀**：含有秀美精华。
  - **抑屈而起**：被抑制而后兴起。

- **规范化释义（primary_lang_explained）**：
  戊己的位置属土，运行于四季之末。戊是阳土，万物生长时从土中出来，万物收割时归入土中。己是阴土，无需作为就能自然成就。又说：戊就是"茂"，己就是"起"。土运行于四季的末尾，万物含有的精华在此时被抑制后又兴起。

- **完整对等诠释（secondary_lang_full）**：
  Wu and Ji occupy the Earth position, operating at the end of each of the Four Seasons. Wu is yang Earth—myriad things emerge from it when growing, return to it when harvested. Ji is yin Earth—achieving completion without deliberate action. It is also said: Wu means "flourishing"; Ji means "rising." Earth operates at the end of each season, when the essential beauty contained in myriad things rises after being suppressed.

- **核心要点**：
  - 戊己属土，运行于四季之末
  - 戊土：阳土，万物生而出、伐而入
  - 己土：阴土，无为而自成
  - 戊为"茂"，己为"起"
  - 土在季末，万物含秀抑屈而起

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_151]` `[trigger: 戊己土之义]` `[factor_trigger: wu_earth AND ji_earth AND element_earth]` `[role: 主干]` 戊己其位，土，行周四季。戊，阳土也，万物生而出之，万物伐而入之。己，阴土也，无所为而得己者也。戊，茂也。己，起也。 → 《三命通会》卷一#戊己土之义

- **详细解说**：
  此条详解戊己土之义。土不独主一季，而是运行于春夏秋冬四季的末尾（辰戌丑未月），起承转合的枢纽作用。戊土为阳土，是万物生长的出处（生而出之）和归宿（伐而入之），如同大地承载万物的生死循环。己土为阴土，以"无为"的方式成就万物，体现道家"无为而无不为"的哲学。"戊，茂也"指万物在土中繁茂生长；"己，起也"指万物从土中兴起。土在每季末尾，万物所含的精华（秀）先被抑制积累，然后在下一季开始时兴起，体现土的转化枢纽功能。

- **校勘与字词辨析（双语）**：
  - **中文**："四季之末"指辰戌丑未月（每季最后一个月）。"含秀"指含有精华。"抑屈"指被抑制压缩。
  - **English**: "End of Four Seasons" refers to Chen-Xu-Chou-Wei months (last month of each season); "containing beauty" refers to essential qualities; "suppressed" means compressed or restrained."""
    normalized_text_zh: str = """"""
    subject: str = "戊己土之义"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_戊己土之义_001_L1",
    )
    version: str = "1.0.0"
