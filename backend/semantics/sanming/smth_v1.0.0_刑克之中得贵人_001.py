"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458252
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
    semantic_id="smth_v1.0.0_刑克之中得贵人_001",
    book_id="sanming",
    engine_id="bazi"
)
class 刑克之中得贵人(SemanticEntry):
    """
    - **原文（source_text）**：
  经云：日时相刑，得遇贵，执法有权势。又云：寅刑巳，巳刑申，庚辛逢寅，是贵人；卯刑子，子刑卯，癸乙双双富又清；未刑戌，戌刑未，甲戊逢羊，贵自荣。不利文官...
    """
    
    original_text: str = """- **原文（source_text）**：
  经云：日时相刑，得遇贵，执法有权势。又云：寅刑巳，巳刑申，庚辛逢寅，是贵人；卯刑子，子刑卯，癸乙双双富又清；未刑戌，戌刑未，甲戊逢羊，贵自荣。不利文官，主武权。如刘应节尚书：癸未、乙卯、丙戌、戊子，子卯刑而得乙癸，未戌刑而得戊，所以官历兵、刑，纵有文名，不居学翰。

- 分字分词释义：
  - **日时相刑**：日支与时支形成地支刑克关系，如子卯刑、寅巳刑等，象征内部矛盾、冲突与压力。
  - **得遇贵**：在刑克关系中又见贵人星或官星相扶持，使冲突转化为执法、用刑之权。
  - **庚辛逢寅 / 癸乙双双富又清 / 甲戊逢羊**：分别指金日主遇寅木，水、木日主在子卯刑中得贵，火土日主在未戌刑中得贵；"羊"即未土，为羊刃之地。
  - **不利文官，主武权**：此格多主掌兵、刑、狱等刚猛之职，不利于纯文职、翰林等清文之官。
  - **学翰**：指翰林、国子监等文职清贵之地，此处用来对比兵、刑之官。

- **规范化释义（primary_lang_explained）**：
  本节所说的"相刑遇贵"，是指日支与时支之间构成刑克关系，本属不吉，但命局中又同时得贵人或官星相扶，于是刑克的力量被转化为执法用刑的权势。古文以寅刑巳、巳刑申、卯刑子、子刑卯、未刑戌、戌刑未等为例：庚辛日主逢寅，多得武贵；癸乙日主在子卯刑中得富贵清名；甲戊日主在未戌刑中遇贵，多主以武职自荣。此格一般不利从事纯文职，反而有利于掌兵权、刑狱、执法等刚猛之官。
  
  刘应节尚书的命例说明了这一点：癸未、乙卯、丙戌、戊子一造，子卯相刑而得乙癸之助，未戌相刑而得戊土之力，因此一生官历兵、刑之职，虽有文名，却终不居学翰之位。

- **完整对等诠释（secondary_lang_full）**：
  The pattern "mutual punishment meets a noble" occurs when the day and hour branches stand in a punishing relationship—such as Zi with Mao, Yin with Si or Wei with Xu—yet at the same time noble stars or official stars come in to support the structure. On its own, punishment between branches points to inner tension, conflicts and potential legal trouble, but when a noble presence joins and the overall chart is configured to use it, that hard energy can be redirected into the authority to enforce law and wield punishment. Thus the classics say that when Geng or Xin metal days meet Yin wood, one often finds martial nobility; when Gui water or Yi wood days are caught in the Zi–Mao punishments, they can be both wealthy and clean in reputation; when Jia wood or Wu earth days are involved in the Wei–Xu punishments, they are likely to gain honour through martial posts. Such patterns favour armed, judicial and enforcement roles more than pure civil literary office.


- 核心要点：
  - 相刑本为凶象，但若得贵人、官星相扶，可化为执法之权，是**以刑立威**的格局。
  - 多主兵权、刑狱、执法等职务，不利纯文、柔和之官，性情亦多刚烈。
  - 判断时需兼看日主强弱与制化情况，身弱而刑重、无贵人相扶者，仍以凶论。

- 详细解说：
  传统命理中，"刑"多与是非、官非、刑罚相关，若单独而无制化，多主伤身破财；但若在合适的位置与官贵相配，则可将这种刚猛之气转化为执法之权。本节强调的，正是"以刑立威"这一思路：有刑才有权执法，若无刑，则不足以震慑。
  
  然而，这类格局往往也伴随性情上的急躁与刚烈，若日主过弱或缺乏印绶、比劫等辅佐，则容易从"执法"滑向"横暴"。因此，在实际应用中，应特别注意行运是否进一步加重刑煞，或是否有印星、比肩来调和，才可以决定其倾向于贵格还是祸端。

- 校勘与字词辨析：
  - **"甲戊逢羊"**中的"羊"指未土，为羊刃之地，非泛指生肖羊。
  - "学翰"为古代对翰林、国子监等文职清贵机构的泛称，以此与兵、刑之官对举，凸显此格偏武不偏文的性质。
  - **English**：
    - Highlights martial rather than literary nature of this pattern.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_028]` `[trigger: 相刑遇贵]` `[factor_trigger: ri_shi_xiang_xing AND guiren_presence]` `[role: 主干]` 日时相刑，得遇贵，执法有权势。 → 《三命通会》卷五#相刑遇贵
  - `[ns_smth_05_029]` `[trigger: 刑中贵人]` `[factor_trigger: xing_guan_pei_zhi]` `[role: 主干依赖]` 寅刑巳，巳刑申，庚辛逢寅，是贵人；卯刑子，子刑卯，癸乙双双富又清。 → 《三命通会》卷五#相刑遇贵
  - `[ns_smth_05_030]` `[trigger: 以刑立威]` `[factor_trigger: yi_xing_li_wei]` `[role: 条件分支]` 有刑才有权执法，若无刑，则不足以震慑。 → 《三命通会》卷五#相刑遇贵
  - `[ns_smth_05_031]` `[trigger: 主武权]` `[factor_trigger: wu_quan_tendency AND bu_li_wenguan]` `[role: 总结]` 不利文官，主武权。官历兵、刑，纵有文名，不居学翰。 → 《三命通会》卷五#相刑遇贵"""
    normalized_text_zh: str = """"""
    subject: str = "刑克之中得贵人"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'xiangxing_yugui_presence', 'bazi_semantic', 'xingke_config', 'bazi_semantic', 'guiren_huaxing_score', 'bazi_semantic', 'wuzhi_qingxiang_score', 'bazi_semantic', 'zhihua_tiaohe_condition', 'bazi_semantic', 'ganglie_xingqing_risk', 'bazi_semantic', 'source_ref', 'rel_smth_05_022', 'xiangxing_yugui_presence', 'rel_smth_05_023', 'wuzhi_qingxiang_score', 'rel_smth_05_024', 'ganglie_xingqing_risk', 'evi_smth_05_022', 'guiren_huaxing_score', 'rule_xingui', 'evi_smth_05_023', 'wuzhi_qingxiang_score', 'rule_wuquan', 'evi_smth_05_024', 'ganglie_xingqing_risk', 'rule_bingxing', 'map_smth_05_015', 'map_smth_05_016']
    
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
        l1_anchor="smth_v1.0.0_刑克之中得贵人_001_L1",
    )
    version: str = "1.0.0"
