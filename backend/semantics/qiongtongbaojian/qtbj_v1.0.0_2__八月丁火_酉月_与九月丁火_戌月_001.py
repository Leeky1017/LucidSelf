"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596922
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
    semantic_id="qtbj_v1.0.0_2__八月丁火_酉月_与九月丁火_戌月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2八月丁火酉月与九月丁火戌月(SemanticEntry):
    """
    - **原文（source_text）**：
  或八月一派辛金，不见庚金，又无比劫，此弃命从财，富而且贵，虽不科甲，亦有异途。从财者水为妻。不克。有偏正。木为子。不刑。
  或九月一派戊土，泄丁火之...
    """
    
    original_text: str = """- **原文（source_text）**：
  或八月一派辛金，不见庚金，又无比劫，此弃命从财，富而且贵，虽不科甲，亦有异途。从财者水为妻。不克。有偏正。木为子。不刑。
  或九月一派戊土，泄丁火之气，不见甲木，为伤官伤尽，非寻常可比。或甲木透出，为文书清贵，秋闱可夺。用甲者，庚不可少。水妻木子。

- **分字分词释义**：
  - **弃命从财**：舍弃自身从顺财星 / 辛多无劫 / 富贵
  - **异途**：非正途功名 / 武职/捐官 / 贵
  - **伤官伤尽**：伤官格完全 / 戊多无甲 / 非寻常
  - **文书清贵**：因文章而清贵 / 伤官配印 / 文贵
  - **秋闱可夺**：秋天科举可夺魁 / 乡试 / 举人
  - **水妻木子**：水为妻木为子 / 六亲定位 / 规则

- **规范化释义（primary_lang_explained）**：
  如果八月（酉月）一派辛金（偏财），不见庚金（正财混杂），又无比肩劫财帮身，这是“弃命从财格”，富而且贵，虽然不是科甲出身，也有异途功名。从财格的人，以水（官杀）为妻（因财生官），不克妻，有偏房正妻。以木（印）为子（因官生印），不刑克子。
  如果九月（戌月）一派戊土（伤官），泄尽丁火之气，不见甲木（印），是“伤官伤尽”，非寻常人可比（贵）。如果甲木透出，是“伤官配印”，主文书清贵，秋闱（举人考试）可以夺魁。用甲木的人，庚金（劈甲）不可少。水为妻木为子。

- **完整对等诠释（secondary_lang_full）**：
  Or in the 8th Month (Rooster), if there is a mass of Xin Metal, no Geng, and no Parallel/Rob Wealth, it is "Abandon Life Follow Wealth", rich and noble. Though not Civil Service, one has alternative fame. For Follow Wealth, Water is Wife (not clashing, having concubines/wives), Wood is Child (no punishment).
  Or in the 9th Month (Dog), if there is a mass of Wu Earth leaking Ding, and no Jia Wood, it is "Hurting Officer Exhausted", incomparable to ordinary people. If Jia is revealed, it implies "Literary Pure Nobility", seizing success in Autumn Exams. Using Jia requires Geng. Water as Wife, Wood as Child.

- **核心要点**：
  - **酉月从财**：辛多无劫，真从财。喜行财官运。
  - **戌月伤尽**：戊多无甲，伤官伤尽，贵。
  - **戌月配印**：甲透制伤，文贵。

- **详细解说**：
  - 酉月丁火长生（火长生在寅，但丁火在酉为长生位？不，丁长生在酉是阴长生说，通论丁生酉为死地/财地）。酉月辛金当令，从财最真。
  - 戌月是火库，也是伤官库。伤官气盛，若无印（甲），则从儿（伤官伤尽）；若有印（甲），则伤官配印。两者皆贵，前者异路，后者科甲。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_285]` `[trigger: 弃命从财]` `[factor_trigger: month_you AND tiangan_ding AND xin_multiple AND NOT tiangan_geng AND NOT tiangan_bing AND pattern_follow_wealth]` `[role: 条件分支]` 八月一派辛金，不见庚金，又无比劫，此弃命从财，富而且贵。 → 《穷通宝鉴·三秋丁火》#18.2
  - `[ns_qttbj_286]` `[trigger: 伤官伤尽]` `[factor_trigger: month_xu AND tiangan_ding AND wu_multiple AND NOT tiangan_jia AND hurting_officer_exhausted]` `[role: 条件分支]` 九月一派戊土，泄丁火之气，不见甲木，为伤官伤尽，非寻常可比。 → 《穷通宝鉴·三秋丁火》#18.2
  - `[ns_qttbj_287]` `[trigger: 文书清贵]` `[factor_trigger: month_xu AND tiangan_ding AND tiangan_jia AND hurting_officer_match_seal AND literary_noble]` `[role: 条件分支]` 甲木透出，为文书清贵，秋闱可夺。 → 《穷通宝鉴·三秋丁火》#18.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 八月丁火（酉月）与九月丁火（戌月）"
    factor_refs: list = ['literary_noble', 'autumn_exam']
    
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
        l1_anchor="qtbj_v1.0.0_2__八月丁火_酉月_与九月丁火_戌月_001_L1",
    )
    version: str = "1.0.0"
