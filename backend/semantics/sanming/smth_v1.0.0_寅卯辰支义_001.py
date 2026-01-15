"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227986
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
    semantic_id="smth_v1.0.0_寅卯辰支义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 寅卯辰支义(SemanticEntry):
    """
    - **原文（source_text）**：
  寅，正月也，阳已在上，阴已在下，人始见之时，故律管飞灰以候之，可以述事之始也。又寅，演也，津也，谓物之津涂。卯，日升之时也。又卯，茂也，言二月阳气盛而...
    """
    
    original_text: str = """- **原文（source_text）**：
  寅，正月也，阳已在上，阴已在下，人始见之时，故律管飞灰以候之，可以述事之始也。又寅，演也，津也，谓物之津涂。卯，日升之时也。又卯，茂也，言二月阳气盛而孳茂。辰者，阳已过半，三月之时，物尽震而长，又谓辰言震也。

- **分字分词释义**：
  - **正月**：农历一月，春季开始。
  - **阳已在上阴已在下**：阳气在上阴气在下。
  - **律管飞灰**：律管中的灰飞起，测候节气。
  - **述事之始**：记述事情的开始。
  - **演也津也**：演进、津液流通。
  - **津涂**：津液道路。
  - **日升之时**：太阳升起的时刻。
  - **孳茂**：繁殖茂盛。
  - **震而长**：震动而生长。

- **规范化释义（primary_lang_explained）**：
  寅是正月，阳气已经在上阴气已经在下，人开始看见的时候，所以用律管飞灰来测候节气，可以记述事情的开始。又说：寅就是"演"，也是"津"，指万物津液流通的道路。卯是太阳升起的时刻。又说：卯就是"茂"，指二月阳气旺盛而繁殖茂盛。辰是阳气已过半，三月的时候，万物都震动而生长，又说辰就是"震"。

- **完整对等诠释（secondary_lang_full）**：
  Yin is the first month—yang qi is already above and yin qi below, the time when people first perceive it, thus pitch pipes with flying ash are used to measure seasonal markers, marking the beginning of recorded events. Also said: Yin means "unfolding" and "fluids"—referring to the pathways of things' vital fluids. Mao is the time when the sun rises. Also said: Mao means "flourishing"—indicating the second month when yang qi is vigorous and things multiply luxuriantly. Chen is when yang has passed midpoint, the third month, when all things shake and grow—thus Chen means "shaking."

- **核心要点**：
  - 寅：正月，阳上阴下，人始见，述事之始
  - 寅为"演"（演进）、"津"（津液流通）
  - 卯：日升之时，二月，阳气盛而孳茂
  - 辰：阳过半，三月，物震而长

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_157]` `[trigger: 寅卯辰支义]` `[factor_trigger: yin_branch AND mao_branch AND chen_branch AND spring_season]` `[role: 主干]` 寅，正月也，阳已在上，阴已在下。卯，茂也，言二月阳气盛而孳茂。辰者，阳已过半，三月之时，物尽震而长。 → 《三命通会》卷一#寅卯辰支义

- **详细解说**：
  此条详解寅卯辰三支之义。寅为春季开始的正月，阳气上升阴气下降，阴阳分明可见，用律管飞灰测候（古代测候方法），标志事情的开始。"寅，演也"指春季万物演进展开，"津也"指津液开始流通。卯对应二月卯时（日出时），阳气更加旺盛，万物繁殖茂盛。辰对应三月，阳气已过半（超过一半），万物震动生长，"辰，震也"体现震卦之象。寅卯辰三支完成了从初春萌发（寅）到盛春茂盛（卯）到仲春震长（辰）的过程。

- **校勘与字词辨析（双语）**：
  - **中文**："律管飞灰"是古代测候方法，将芦苇灰放入律管中，阳气至则飞扬。"孳茂"指繁殖茂盛。
  - **English**: "Pitch pipes with flying ash" was an ancient method of measuring seasons—reed ash placed in pitch pipes would fly up when yang qi arrived; "multiply luxuriantly" means reproducing and flourishing."""
    normalized_text_zh: str = """"""
    subject: str = "寅卯辰支义"
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
        l1_anchor="smth_v1.0.0_寅卯辰支义_001_L1",
    )
    version: str = "1.0.0"
