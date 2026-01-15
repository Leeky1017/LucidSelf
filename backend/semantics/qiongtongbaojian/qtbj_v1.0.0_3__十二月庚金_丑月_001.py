"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578394
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
    semantic_id="qtbj_v1.0.0_3__十二月庚金_丑月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3十二月庚金丑月(SemanticEntry):
    """
    - **原文（source_text）**：
  十二月庚金，寒气太重，且多湿泥，愈寒愈冻，先取丙火解冻，次取丁火炼金，甲亦不可少。
  丙丁甲透者，即不科甲，亦有思荣。有丙无丁甲者，富中取贵。有丁甲...
    """
    
    original_text: str = """- **原文（source_text）**：
  十二月庚金，寒气太重，且多湿泥，愈寒愈冻，先取丙火解冻，次取丁火炼金，甲亦不可少。
  丙丁甲透者，即不科甲，亦有思荣。有丙无丁甲者，富中取贵。有丁甲无丙者，特达才人。有丙丁无甲者，白手成家，刀笔亨通，乏金更美。
  或支成金局无火，僧道之流。

- **分字分词释义**：
  - **十二月**：丑月 / 农历十二月 / 己土当令
  - **寒气太重**：寒冷气息过重 / 严冬 / 需丙火
  - **湿泥**：湿润泥土 / 丑土寒湿 / 不生金
  - **解冻**：融化冰冻 / 丙火作用 / 调候
  - **恩荣**：皇恩荣耀 / 封赠 / 吉象
  - **特达才人**：特别通达的人才 / 丁甲无丙 / 次吉
  - **白手成家**：白手起家 / 靠己努力 / 自力更生
  - **刀笔亨通**：文书职位亨通 / 吏职 / 吉象
  - **乏金更美**：缺少金更好 / 无比劫争夺 / 吉象
  - **僧道之流**：出家修道之人 / 金局无火 / 凶象

- **规范化释义（primary_lang_explained）**：
  十二月（丑月）的庚金，寒气太重，而且多湿泥（丑为湿土），愈寒愈冻（冻土不生金，反埋金），先取丙火解冻（暖土），次取丁火炼金（成器），甲木（疏土/引丁）也不可少。
  丙火、丁火、甲木透出者，即使不是科甲，也有恩荣（封典）。有丙火无丁甲者，富中取贵。有丁甲无丙者，特达才人。有丙丁无甲者，白手成家，刀笔（文职）亨通，缺乏金（比劫）更美（？乏金指身弱？或指用财官不喜比劫争夺）。
  如果地支合成金局无火，僧道之流（身旺无依，寒苦）。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal in the 12th Month (Ox Month): Cold Qi is too heavy; much wet mud; the colder it gets, the more it freezes. First take Bing to unfreeze, then Ding to smelt, Jia cannot be lacking.
  If Bing/Ding/Jia reveal, even if not Civil Service, there are honors. With Bing but no Ding/Jia, nobility amidst wealth. With Ding/Jia but no Bing, an outstanding talent. With Bing/Ding but no Jia, self-made family, success via pen/knife; lacking Metal is even better.
  If branches form a Metal Frame without Fire, a monk/Taoist.

- **核心要点**：
  - **首要用神**：丙火（解冻）。丑月湿泥冻金，非丙不暖。
  - **配合**：丁（炼）、甲（疏）。
  - **三者全**：丙丁甲全，富贵。

- **详细解说**：
  - 丑月庚金墓库。
  - 关键在“解冻”。冻土不能生金，且土多埋金。
  - 丙火解冻，甲木疏土，丁火炼金，三者缺一不可。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_367]` `[trigger: 庚生丑月]` `[factor_trigger: month_chou AND tiangan_geng AND tiangan_bing AND tiangan_ding AND tiangan_jia]` `[role: 主干]` 十二月庚金，寒气太重，且多湿泥，愈寒愈冻，先取丙火解冻，次取丁火炼金，甲亦不可少。 → 《穷通宝鉴·三冬庚金》#33.3
  - `[ns_qttbj_368]` `[trigger: 丙丁甲全]` `[factor_trigger: month_chou AND tiangan_geng AND bing_revealed AND ding_revealed AND jia_revealed]` `[role: 条件分支]` 丙丁甲透者，即不科甲，亦有恩荣。 → 《穷通宝鉴·三冬庚金》#33.3
  - `[ns_qttbj_369]` `[trigger: 金局无火]` `[factor_trigger: month_chou AND tiangan_geng AND dizhi_metal_frame AND NOT element_fire]` `[role: 例外处理]` 或支成金局无火，僧道之流。 → 《穷通宝鉴·三冬庚金》#33.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 十二月庚金（丑月）"
    factor_refs: list = ['wet_mud_chou', 'en_rong_honors', 'self_made']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_3__十二月庚金_丑月_001_L1",
    )
    version: str = "1.0.0"
