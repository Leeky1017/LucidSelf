"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157439
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
    semantic_id="smth_v1.0.0_六乙日丁亥时断_食神印绶与死处逢生_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六乙日丁亥时断食神印绶与死处逢生(SemanticEntry):
    """
    - 原文（source_text）：

  六乙日丁亥时断。

  六乙日生丁亥时，食神印绶亦奇哉；月气水土无财贵，切忌伤妻与子灾。乙日丁亥时，死处逢生，乙木死，亥却气壬水为生气印绶，乙用丁为食，亥中...
    """
    
    original_text: str = """- 原文（source_text）：

  六乙日丁亥时断。

  六乙日生丁亥时，食神印绶亦奇哉；月气水土无财贵，切忌伤妻与子灾。乙日丁亥时，死处逢生，乙木死，亥却气壬水为生气印绶，乙用丁为食，亥中丁坐无气，喜甲木生，助丁食为福。如遇金局，行水运者，防目疾。四柱见财，或行财运、贪财坏印，主破财。戊为财为妻，庚为官为子，亥上庚绝土病，妻衰子少。

  乙丒日丁亥时秀，生壬子申未卯月，干透财印者，才德兼全，职在风宪。年月干支纯金，身衰煞旺，主凶死。

  乙卯日丁亥时，巳酉丑月偏官，申月正官，俱贵。亥月，东南运，风宪。未月，三合木局，大贵。

  乙未日丁亥时贵，子亥年月，公侯。春生，行西运，郎官。酉孤，贵。年月木火，主发高科。水土金与日干合化有用者，俱吉。

  乙酉日丁亥时，月通金局，行水运，大贵。通木气，发达。土气，称意。

  乙亥日丁亥时，有财自刑，寅卯身旺，天干透财者富；辰丑，行金火运，贵。亥子申，官印双清，更辅以财。大贵。

  时上生逢亥与丁，食神乙木遇长生；月气相扶为最贵，身衰无倚是常人。乙日时逢丁亥，食神印绶相扶。长生得意好无伤，荣显清名贵遇。喜逢丁壬化气，运临冠带迁除。无机妙法实难窥，丙己寅申减贵。

- 分字分词释义：

  - **死处逢生**：乙木在亥虽为死地，但亥中壬水印绶可生扶乙木，形成「死中有生」。
  - **食神印绶相扶**：丁火食神与壬水印绶同在，若能配合，则福寿双全。
  - **贪财坏印**：财星克制印绶，破坏了印绶生身的结构。
  - **丁壬化气**：丁火与壬水合化为木，可助身旺。

- 规范化释义（primary_lang_explained）：

  本节讲「六乙日，丁亥时」：

  - 乙木在亥虽为死地，但亥中壬水印绶可生扶乙木，形成「死处逢生」的结构；
  - 丁火食神虽坐无气之地，但若有甲木生助，仍可为福；
  - 需防四柱见财或行财运时「贪财坏印」，导致印绶被克、破财伤身。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Yi Days with Ding-Hai Hour":

  - Yi Wood at Hai is at death position, but Hai contains Ren Water (Seal) which can nurture Yi Wood, forming a structure of "finding life at death's door."
  - Though Ding Fire (Food God) sits at a powerless position, if assisted by Jia Wood, it can still bring fortune.
  - Beware when four pillars show Wealth or during Wealth fortune cycles—"greedy for wealth damages seal," causing Seal to be overcome, resulting in financial loss and physical harm.

- 核心要点：

  - 本格以「死处逢生」为核心，强调印绶的救助作用。
  - 食神印绶同在，若能配合身旺，则福寿双全。
  - 需防贪财坏印、目疾、妻子不利等问题。

- 详细解说：

  1. **死处逢生的用法**  
     - 乙木在亥为死地，本不佳；但亥中壬水为印绶，可生扶乙木；  
     - 形成「死中有生」的结构，若月令配合，可化险为夷。

  2. **食神印绶的配合**  
     - 丁火食神可生财、泄秀；壬水印绶可生身、化煞；  
     - 若两者能配合得当，则福寿双全。

  3. **贪财坏印的风险**  
     - 若四柱财星重或行财运，财克印绶；  
     - 印绶被伤则生身无源，主破财、健康不利。

- 校勘与字词辨析：

  - 「无机妙法实难窥」形容此格变化微妙，需要综合分析。
  - 「丙己寅申减贵」指某些干支组合会降低贵气，需要注意避免。
  - **English**：
    - May diminish noble qi; requires attention to avoid.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_093]` `[trigger: 死处逢生]` `[factor_trigger: sichu_fengsheng AND yi_qi_zai]` `[role: 主干]` 六乙日生丁亥时，食神印绶亦奇哉。 → 《三命通会》卷八#六乙日丁亥时
  - `[ns_smth_08_094]` `[trigger: 月气相扶]` `[factor_trigger: yueqi_xiangfu AND wu_cai_gui]` `[role: 主干依赖]` 月气水土无财贵，切忌伤妻与子灾。 → 《三命通会》卷八#六乙日丁亥时
  - `[ns_smth_08_095]` `[trigger: 丁壬化气]` `[factor_trigger: dingre_huaqi AND xi_feng]` `[role: 条件分支]` 喜逢丁壬化气，运临冠带迁除。 → 《三命通会》卷八#六乙日丁亥时
  - `[ns_smth_08_096]` `[trigger: 荣显清名]` `[factor_trigger: rongxian_qingming AND changsheng_deyi]` `[role: 总结]` 长生得意好无伤，荣显清名贵遇。 → 《三命通会》卷八#六乙日丁亥时"""
    normalized_text_zh: str = """"""
    subject: str = "六乙日丁亥时断：食神印绶与死处逢生"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_yi', 'bazi_semantic', 'bazi_state_factor_182', 'bazi_semantic', 'bazi_relation_shishen_3', 'bazi_semantic', 'bazi_state_factor_166', 'bazi_semantic', 'hour_branch_hai', 'bazi_semantic', 'bazi_condition_factor_49', 'bazi_semantic', 'source_ref', 'rel_smth_08_070', 'sichu_fengsheng', 'rel_smth_08_071', 'shishen_yinxu', 'rel_smth_08_072', 'yueqi_xiangfu', 'evi_smth_08_070', 'sichu_fengsheng', 'rule_sichu', 'evi_smth_08_071', 'shishen_yinxu', 'rule_shishen', 'evi_smth_08_072', 'tancai_huaiyin', 'rule_tancai', 'map_smth_08_047', 'map_smth_08_048']
    
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
        l1_anchor="smth_v1.0.0_六乙日丁亥时断_食神印绶与死处逢生_001_L1",
    )
    version: str = "1.0.0"
