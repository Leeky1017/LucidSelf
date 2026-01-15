"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559001
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
    semantic_id="yhzp_v1.0.0_论日刃_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论日刃(SemanticEntry):
    """
    - **原文（source_text）**：  
  日刃与阳刃同。日刃有戊午、丙午、壬子也，与阳刃同法；不喜刑冲破害，不喜会合、兼受七杀，要行官乡，便为贵命。若四柱中一来会合，必主奇祸。其人眼大须长...
    """
    
    original_text: str = """- **原文（source_text）**：  
  日刃与阳刃同。日刃有戊午、丙午、壬子也，与阳刃同法；不喜刑冲破害，不喜会合、兼受七杀，要行官乡，便为贵命。若四柱中一来会合，必主奇祸。其人眼大须长、性刚果毅，无恻隐惠慈之心、有刻剥不恤之意。三刑自刑魁罡全，发迹疆场。如或无情、或财旺，则主其凶；或有救神，要先审察。如刑害俱全，类皆得地，贵不可言也！安得不举。

- **分字分词释义**：
  - **日刃**：日柱坐刃，特指戊午、丙午、壬子三日。
  - **与阳刃同法**：日刃的论法与阳刃相同。
  - **戊午丙午壬子**：三个日刃日——戊午坐午火（戊禄在巳，午为刃），丙午坐午火，壬子坐子水（壬禄在亥，子为刃）。
  - **刑冲破害**：地支四凶——刑（互相伤害）、冲（对冲相克）、破（破坏）、害（暗害）。
  - **会合**：地支三会或三合，阳刃忌见。
  - **行官乡**：行官星旺相的大运，官杀制刃为贵。
  - **眼大须长性刚果毅**：日刃之人的典型相貌与性格特征。
  - **无恻隐惠慈之心**：日刃之人心狠手辣，缺乏同情心。
  - **三刑自刑魁罡全**：凶神聚集，反成武贵。

- **规范化释义（primary_lang_explained）**：  
  日刃与阳刃同法，指戊午丙午壬子三日。不喜刑冲破害会合，要行官乡为贵命。若四柱会合必主奇祸。日刃之人眼大须长性刚果毅，无恻隐之心有刻剥之意。三刑自刑魁罡全发迹疆场。如无情或财旺主凶，有救神要审察。如刑害俱全类皆得地，贵不可言。

- **完整对等诠释（secondary_lang_full）**：  
  Day Blade follows the same method as Yang Blade, referring specifically to three days: Wu-Wu, Bing-Wu, and Ren-Zi. It does not favor Punishments, Clashes, Breakages, Harms, or Combinations; it desires to travel through Officer regions to become a noble fate. If Four Pillars contain combinations, it certainly indicates strange disasters. People with Day Blade typically have large eyes, long whiskers, and a nature that is rigid, decisive, and resolute, lacking compassion or mercy while harboring intent to exploit without pity. If Three Punishments, Self-Punishment, and Kuigang are all complete, one rises to prominence on the battlefield. If lacking affection or having vigorous Wealth, it indicates inauspiciousness; if there are Rescue Spirits, one must examine carefully. If punishments and harms are all complete and positions are gained, nobility is beyond words! How could one not be uplifted?

- **核心要点**：
  - 日刃与阳刃同法，特指戊午、丙午、壬子三日
  - 日刃不喜刑冲破害，不喜会合
  - 日刃要行官乡，官杀制刃为贵命
  - 日刃之人眼大须长、性刚果毅、无恻隐之心
  - 三刑自刑魁罡全，发迹疆场
  - 刑害俱全类皆得地，贵不可言

- **详细解说**：  
  本条专论日刃的特殊性质。日刃是日柱坐刃的特殊情况，"与阳刃同法"，特指戊午、丙午、壬子三日。日刃的禁忌与阳刃相同："不喜刑冲破害，不喜会合"——地支四凶（刑冲破害）和三会三合都会破坏日刃格局；"要行官乡，便为贵命"——需要官杀制刃才能成格发贵。日刃之人有典型的相貌与性格："眼大须长、性刚果毅，无恻隐惠慈之心、有刻剥不恤之意"——刚毅果决但缺乏温情。值得注意的是凶神反成贵格的情况："三刑自刑魁罡全，发迹疆场"——凶神聚集反主武贵，在军旅疆场发迹。"刑害俱全，类皆得地，贵不可言"——凶神得地反成大贵，这体现了"物极必反"的命理辩证法。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_120]` `[trigger: 日刃定义]` `[factor_trigger: riren_def AND dizhi_wu_zi]` `[role: 主干]` 日刃与阳刃同。日刃有戊午、丙午、壬子也。 → 《渊海子平·论日刃》
  - `[ns_yhzp_121]` `[trigger: 日刃喜忌]` `[factor_trigger: riren AND xiji_xingchong AND guan_xiang]` `[role: 主干依赖]` 不喜刑冲破害，不喜会合、兼受七杀，要行官乡，便为贵命。 → 《渊海子平·论日刃》
  - `[ns_yhzp_122]` `[trigger: 日刃会合]` `[factor_trigger: riren AND huihe AND xiongxiang AND huihe_qihuo]` `[role: 例外处理]` 若四柱中一来会合，必主奇祸。 → 《渊海子平·论日刃》
  - `[ns_yhzp_123]` `[trigger: 日刃性格]` `[factor_trigger: riren AND xingge_gangyi]` `[role: 条件分支]` 其人眼大须长、性刚果毅，无恻隐惠慈之心、有刻剥不恤之意。 → 《渊海子平·论日刃》
  - `[ns_yhzp_124]` `[trigger: 日刃疆场]` `[factor_trigger: riren AND sanxing AND kuigang AND wugui AND anchong_qugui AND angui]` `[role: 条件分支]` 三刑自刑魁罡全，发迹疆场。 → 《渊海子平·论日刃》
  - `[ns_yhzp_125]` `[trigger: 日刃大贵]` `[factor_trigger: riren AND xinghai_quan AND dagui AND anchong_qugui AND angui]` `[role: 总结]` 如刑害俱全，类皆得地，贵不可言也！ → 《渊海子平·论日刃》"""
    normalized_text_zh: str = """"""
    subject: str = "论日刃"
    factor_refs: list = ['day_blade', 'new_candidate']
    
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
        l1_anchor="yhzp_v1.0.0_论日刃_001_L1",
    )
    version: str = "1.0.0"
