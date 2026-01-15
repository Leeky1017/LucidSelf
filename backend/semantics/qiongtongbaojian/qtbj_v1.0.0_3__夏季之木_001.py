"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619756
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
    semantic_id="qtbj_v1.0.0_3__夏季之木_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3夏季之木(SemanticEntry):
    """
    - **原文（source_text）**：
  夏月之木，根干叶燥，盘而且直，屈而能伸。欲得水盛而成滋润之力，诚不可少。切忌火旺而招焚化之忧，故以为凶。土宜在薄，不可厚重，厚则反为灾咎。恶金在多，不...
    """
    
    original_text: str = """- **原文（source_text）**：
  夏月之木，根干叶燥，盘而且直，屈而能伸。欲得水盛而成滋润之力，诚不可少。切忌火旺而招焚化之忧，故以为凶。土宜在薄，不可厚重，厚则反为灾咎。恶金在多，不可欠缺，缺则不能琢削。重重见木，徒以成林，叠叠逢华，终无结果。

- **分字分词释义**：
  - **根干叶燥**：根部干枯、叶片燥热 / 夏木缺水之象 / 急需滋润
  - **盘而且直**：虽盘屈却能挺直 / 夏木的坚韧 / 能屈能伸
  - **滋润之力**：水的润泽功能 / 夏木第一需求 / 救命之水
  - **焚化之忧**：被火烧毁的忧患 / 火多木焚 / 夏木大忌
  - **灾咎**：灾祸、祸害 / 土厚克水 / 雪上加霜
  - **琢削**：雕琢修剪 / 金的作用 / 成器之功
  - **徒以成林**：只是白白成为森林 / 比劫多无用 / 分夺水源
  - **叠叠逢华**：重重开花 / 木多火多 / 热闹但无实
  - **终无结果**：最终不结果实 / 无水则虚耗 / 繁华空转

- **规范化释义（primary_lang_explained）**：
  夏天的木，根干枯叶干燥，虽然盘屈但也挺直，能屈能伸。希望得到盛大的水来滋润，这（水）是绝对不可少的。切忌火太旺而招来焚烧化灰的忧患，所以火旺为凶。土宜薄不宜厚，土太厚重反而是灾祸（因燥土不能生木且止水）。厌恶金太多，但也不可完全欠缺，缺了金就不能修剪雕琢（此时金生水、修木）。如果重重见到比劫木，只是徒然成林，花开得再多，最终也不会结出果实（因为无水干枯）。

- **完整对等诠释（secondary_lang_full）**：
  Wood in Summer has dry roots and leaves; it is coiled yet straight, able to bend and extend. It desires abundant Water for nourishment; this is absolutely indispensable. It strictly dreads excessive Fire, which brings the worry of incineration, hence Fire is ominous. Earth should be thin, not thick; heavy Earth becomes a disaster (blocking Water). It dislikes excessive Metal, yet Metal cannot be entirely absent; without it, there is no pruning. Seeing layers of Wood only forms a forest in vain; flowers bloom repeatedly but ultimately bear no fruit.

- **核心要点**：
  - 首要用神：水（调候、滋润）。夏木无水必死。
  - 大忌：火旺（自焚）。
  - 辅助：金（生水、修剪），但不可多。
  - 忌土厚：厚土克水，加重燥热。

- **详细解说**：
  夏木（巳午未月）火旺木泄，处于"病、死、墓"地，关键在于"活命"。
  - 水是第一救星，不仅润木，还能制火。
  - 金是水源（金生水），故夏木喜微金生水，不喜强金克身。
  - 土是阻碍，尤其是燥土（未戌），吸水且不能生木。
  - "重重见木...终无结果"说明比劫在夏天无水的情况下，只会助燃火势，不仅帮不了身，反而分夺有限的水源。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_052]` `[trigger: 夏木状态]` `[factor_trigger: season_summer AND element_wood]` `[role: 主干]` 夏月之木，根干叶燥，盘而且直，屈而能伸。 → 《穷通宝鉴·论木》#2.3
  - `[ns_qttbj_053]` `[trigger: 夏木喜水]` `[factor_trigger: season_summer AND element_wood AND wood_summer_likes_water]` `[role: 主干依赖]` 欲得水盛而成滋润之力，诚不可少。 → 《穷通宝鉴·论木》#2.3
  - `[ns_qttbj_054]` `[trigger: 夏木忌火]` `[factor_trigger: season_summer AND element_wood AND wood_summer_fears_fire]` `[role: 例外处理]` 切忌火旺而招焚化之忧，故以为凶。 → 《穷通宝鉴·论木》#2.3
  - `[ns_qttbj_055]` `[trigger: 夏木忌土厚]` `[factor_trigger: season_summer AND element_wood AND wood_summer_fears_thick_earth]` `[role: 条件分支]` 土宜在薄，不可厚重，厚则反为灾咎。 → 《穷通宝鉴·论木》#2.3
  - `[ns_qttbj_056]` `[trigger: 夏木需金]` `[factor_trigger: season_summer AND element_wood AND element_metal]` `[role: 条件分支]` 恶金在多，不可欠缺，缺则不能琢削。 → 《穷通宝鉴·论木》#2.3
  - `[ns_qttbj_057]` `[trigger: 夏木比劫无用]` `[factor_trigger: season_summer AND element_wood AND shishen_robbery AND NOT element_water]` `[role: 总结]` 重重见木，徒以成林，叠叠逢华，终无结果。 → 《穷通宝鉴·论木》#2.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 夏季之木"
    factor_refs: list = ['wood_dry_roots_leaves', 'wood_incinerated_by_fire', 'water_moistening_effect', 'metal_pruning_effect']
    
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
        l1_anchor="qtbj_v1.0.0_3__夏季之木_001_L1",
    )
    version: str = "1.0.0"
