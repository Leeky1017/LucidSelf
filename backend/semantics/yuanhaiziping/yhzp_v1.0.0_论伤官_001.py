"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558787
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
    semantic_id="yhzp_v1.0.0_论伤官_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论伤官(SemanticEntry):
    """
    - **原文（source_text）**：伤官者，其验如神。伤官务要伤尽；伤之不尽，官来乘旺，其祸不可胜言。伤官见官，为祸百端。倘月令在伤官之位，及四柱配合、作事皆在伤官之处；又行身旺乡，真贵人也。...
    """
    
    original_text: str = """- **原文（source_text）**：伤官者，其验如神。伤官务要伤尽；伤之不尽，官来乘旺，其祸不可胜言。伤官见官，为祸百端。倘月令在伤官之位，及四柱配合、作事皆在伤官之处；又行身旺乡，真贵人也。伤官主人多才艺、傲物气高，常以天下之人不如己；而贵人亦惮之，众人亦恶之。运一逢官，祸不可言；或有吉神可解，必生恶疾以残其躯；不然运遭官事。年带伤官，父母不全；月带伤官，兄弟不完；日带伤官，妻妾不完；时带伤官，子息无传。

- **分字分词释义**：
  - **伤官**：我生之神且阴阳相同者，如甲木生丁火，丁火为甲木之伤官，能克制正官。
  - **伤尽**：命中官星被伤官完全克制，无一残留，方为纯格。
  - **伤官见官**：伤官格中再见官星，官星不被伤尽，反而官来克身，大凶。
  - **月令**：月支当令之气，为格局判断的核心依据。
  - **身旺乡**：日主旺相的大运方向，伤官格行身旺运为吉。
  - **傲物气高**：恃才傲物，自视甚高，伤官之人的典型性格。
  - **官事**：官司诉讼，伤官见官的典型凶象。
  - **六亲不全**：父母、兄弟、妻妾、子息各有缺损，对应年月日时各柱。

- **规范化释义（primary_lang_explained）**：伤官是我生之神且阴阳相同，其效验如神。伤官格要求伤尽官星，若伤之不尽则官来克身，为祸百端。月令伤官且四柱配合得当，行身旺运则为贵命。伤官之人多才多艺但傲气高，贵人畏之众人恶之。伤官格最忌行官运，主灾祸官非或恶疾。年月日时各柱见伤官，分别主父母、兄弟、妻妾、子息不全。

- **完整对等诠释（secondary_lang_full）**：Injuring Officer is what-I-generate with same polarity, its verification divine. Injuring Officer pattern requires completely injuring Officer Star; if incompletely injured, Officer comes controlling Self bringing endless calamities. Month Command in Injuring Officer with proper Four-Pillar configuration, moving through strong-Self cycles brings nobility. Injuring-Officer individuals possess multiple talents but arrogant temperament—nobles fear them, masses dislike them. This pattern most taboos meeting Officer cycles, bringing disasters, official troubles or serious illness. Year/Month/Day/Hour pillars containing Injuring Officer respectively indicate incomplete parents/siblings/spouse/children.

- **核心要点**：
  - 伤官务要伤尽，伤之不尽则官来乘旺为祸
  - 伤官见官，为祸百端
  - 月令伤官配合得当，行身旺运为贵
  - 伤官之人多才艺傲物气高
  - 年月日时带伤官，主六亲各有不全

- **详细解说**：  
  本条系统论述伤官的性质、格局、性格与六亲。伤官为我生之神且阴阳相同（如甲木生丁火），其本质是"泄身之气"而克制官星。"伤官务要伤尽"是本格的核心法则：若命中伤官不能完全克制官星，残存的官星反而会乘势克身，形成"伤官见官，为祸百端"的凶局。但若月令伤官且四柱配合得当，再行身旺大运，则是"真贵人"——身旺能任伤官之泄，伤官能制官显才，反成清贵。伤官之人的性格特征是"多才艺、傲物气高"，自命不凡，虽有真才实学，但贵人畏之、众人恶之，人际关系较差。伤官格最忌行官运，主官非诉讼或恶疾。年月日时各柱见伤官，分别主父母不全、兄弟不完、妻妾不完、子息无传，体现伤官的"六亲克破"特性。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_040]` `[trigger: 伤官性质]` `[factor_trigger: injuring_officer]` `[role: 主干]` 伤官者，其验如神。 → 《渊海子平·论伤官》
  - `[ns_yhzp_041]` `[trigger: 伤官伤尽]` `[factor_trigger: injuring_officer AND direct_officer AND pattern_injuring_officer_complete]` `[role: 主干依赖]` 伤官务要伤尽；伤之不尽，官来乘旺，其祸不可胜言。 → 《渊海子平·论伤官》
  - `[ns_yhzp_042]` `[trigger: 伤官见官]` `[factor_trigger: injuring_officer AND direct_officer AND pattern_injuring_meets_officer]` `[role: 条件分支]` 伤官见官，为祸百端。 → 《渊海子平·论伤官》
  - `[ns_yhzp_043]` `[trigger: 伤官成格]` `[factor_trigger: injuring_officer AND month_command AND day_master_strength]` `[role: 条件分支]` 月令在伤官之位，又行身旺乡，真贵人也。 → 《渊海子平·论伤官》
  - `[ns_yhzp_044]` `[trigger: 伤官性格]` `[factor_trigger: injuring_officer]` `[role: 主干依赖]` 伤官主人多才艺、傲物气高，常以天下之人不如己。 → 《渊海子平·论伤官》
  - `[ns_yhzp_045]` `[trigger: 伤官人际]` `[factor_trigger: injuring_officer]` `[role: 条件分支]` 贵人亦惮之，众人亦恶之。 → 《渊海子平·论伤官》
  - `[ns_yhzp_046]` `[trigger: 伤官忌官运]` `[factor_trigger: injuring_officer AND direct_officer AND major_cycle]` `[role: 条件分支]` 运一逢官，祸不可言。 → 《渊海子平·论伤官》
  - `[ns_yhzp_047]` `[trigger: 伤官克六亲]` `[factor_trigger: injuring_officer]` `[role: 条件分支]` 年带伤官，父母不全；月带伤官，兄弟不完；日带伤官，妻妾不完；时带伤官，子息无传。 → 《渊海子平·论伤官》"""
    normalized_text_zh: str = """"""
    subject: str = "论伤官"
    factor_refs: list = ['injuring_officer', 'pattern_injuring_officer_complete_proposal', 'pattern_injuring_meets_officer_proposal', 'pattern_injuring_officer_pattern_proposal']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_论伤官_001_L1",
    )
    version: str = "1.0.0"
