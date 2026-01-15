"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228588
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
    semantic_id="smth_v1.0.0_丙申丁酉山下火_自病自死之火须木助_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丙申丁酉山下火自病自死之火须木助(SemanticEntry):
    """
    - **原文（source_text）**：
  丙申自病之火，丁酉自死之火，其气极微，假木相助，其气方生。忌甲申、乙酉、甲寅、乙卯之水。阎东叟云：丙申病火，以木为文明之德，以水为旷达之性，以土为福慧...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙申自病之火，丁酉自死之火，其气极微，假木相助，其气方生。忌甲申、乙酉、甲寅、乙卯之水。阎东叟云：丙申病火，以木为文明之德，以水为旷达之性，以土为福慧之基，惟金为暴虐，纵有吉辰，革为不和之气。五行要论云：丁酉火自死，含韬晦寂静之气，外和内刚。贵格乘之，类为有道君子自然之德行。

- **分字分词释义**：
  - **自病之火**：自己病弱的火。
  - **自死之火**：自己死绝的火。
  - **其气极微**：其气极其微弱。
  - **假木相助**：依靠木来相助。
  - **文明之德**：文明开化的德性。
  - **旷达之性**：开阔豁达的性情。
  - **福慧之基**：福德智慧的基础。
  - **韬晦寂静**：隐藏收敛寂静。

- **规范化释义（primary_lang_explained）**：
  丙申是自病的火，丁酉是自死的火，其气极其微弱，依靠木来相助，其气才能生发。忌讳甲申、乙酉、甲寅、乙卯的水。阎东叟说：丙申病火，以木为文明之德，以水为旷达之性，以土为福慧之基，唯独金为暴虐，纵然有吉辰，也会变成不和之气。五行要论说：丁酉火自死，包含韬光养晦寂静的气质，外在和顺内在刚强。如果贵格乘之，就像有道君子自然的德行。

- **完整对等诠释（secondary_lang_full）**：
  Bingshen is self-sick fire, Dingyou is self-dead fire, their energy extremely faint, relying on Wood assisting, their energy then generates. Avoid Jiashen, Yiyou, Jiayin, Yimao water. Yan Dongsou says: Bingshen sick-fire, takes Wood as civilization virtue, Water as broad-expansive nature, Earth as blessing-wisdom foundation, only Metal as violent-tyrannical, even having auspicious times, transforms into inharmonious energy. Five Elements Essential Discourse says: Dingyou Fire self-dead, contains concealing-retiring tranquil energy, externally harmonious internally firm. Noble pattern riding it, resembles principled-gentleman natural virtue-conduct.

- **核心要点**：
  - 丙申丁酉为山下火，自病自死
  - 气极微弱需木助
  - 丙申：木文明、水旷达、土福慧、金暴虐
  - 丁酉：韬晦寂静、外和内刚
  - 贵格为有道君子

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_231]` `[trigger: 丙申丁酉火性质]` `[factor_trigger: bingshen_dingyou_sick_dead_fire AND concealing_tranquil AND noble_pattern_principled_gentleman]` `[role: 主干]` 丙申自病之火，丁酉自死之火，其气极微，假木相助，其气方生。忌甲申、乙酉、甲寅、乙卯之水。阎东叟云：丙申病火，以木为文明之德，以水为旷达之性，以土为福慧之基，惟金为暴虐，纵有吉辰，革为不和之气。五行要论云：丁酉火自死，含韬晦寂静之气，外和内刚。贵格乘之，类为有道君子自然之德行。 → 《三命通会》卷一#丙申丁酉火性质

- **详细解说**：
  此条详论丙申、丁酉（山下火）的性质。丙申是自病之火（申为火病地），丁酉是自死之火（酉为火死地），气极微弱需木相助才能生发，忌水克制。阎东叟分析丙申病火：木为文明、水为旷达、土为福慧，唯金为暴虐不和。五行要论指出丁酉火自死，韬晦寂静、外和内刚，贵格乘之为有道君子。这是论述病死之火的微弱与转化。

- **校勘与字词辨析（双语）**：
  - **中文**："自病"指申为火病地。"自死"指酉为火死地。"韬晦"指隐藏收敛。"外和内刚"指表面和顺内心刚强。
  - **English**: "Self-sick" means Shen is fire's sickness position. "Self-dead" means You is fire's death position. "Concealing-retiring" means hiding and restraining. "Externally harmonious internally firm" means gentle outside strong inside."""
    normalized_text_zh: str = """"""
    subject: str = "丙申丁酉山下火：自病自死之火须木助"
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
        l1_anchor="smth_v1.0.0_丙申丁酉山下火_自病自死之火须木助_001_L1",
    )
    version: str = "1.0.0"
