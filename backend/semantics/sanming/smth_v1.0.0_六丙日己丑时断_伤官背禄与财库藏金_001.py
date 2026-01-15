"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157460
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
    semantic_id="smth_v1.0.0_六丙日己丑时断_伤官背禄与财库藏金_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丙日己丑时断伤官背禄与财库藏金(SemanticEntry):
    """
    - 原文（source_text）：

  六丙日己丑时断（以下六丙日所忌月分与上同。时亦并论）。

  六丙日生时己丑，官鬼相生禄不成；若见申庚并乙旺，不求财禄过平生。丙日己丑时，伤官背禄，傲物志高...
    """
    
    original_text: str = """- 原文（source_text）：

  六丙日己丑时断（以下六丙日所忌月分与上同。时亦并论）。

  六丙日生时己丑，官鬼相生禄不成；若见申庚并乙旺，不求财禄过平生。丙日己丑时，伤官背禄，傲物志高。丙用癸为官，丑中有癸余气，被明暗土伤，柱透癸为祸。若见庚辛，伤官生财，却为福庆。

  丙子日己丑时，寅亥申辰年月，天干透财印食者贵。

  丙寅日己丑时，平常，生乙酉月，正财格，有乙庚健旺者贵。巳丑年月，干透官印者贵。

  丙辰日己丑时，申亥年月，化水则吉；不化寿促，戌月冲库，无人不发。寅午身旺，成火上格，大贵。

  丙午日己丑时，春月，行火金运，官至极品。夏平，秋富，冬贵，难为妻子，午酉年月，五六品，此月禄生财之验。

  丙申日己丑时，血疾。申月，文学儒官成。卯贵。子辰会官，寅卯会印，俱吉。

  丙戌日己丑时高，武刑后发旺。生亥卯月，火金运，大贵。辰未四库全，火土成局，大富。

  丙日财官库里藏，戌辰未字显文章；身衰若也无匙钥，求名求利总平常。丙日时逢己丑，伤官财库暗藏。运交未戌不寻常。破出财官必旺。近贵谋夺劫财，算来虽有害。六亲真假少和谐，直断依时莫怪。

- 分字分词释义：

  - **伤官背禄**：己土伤官克制癸水正官，破坏官禄根基。
  - **财库藏金**：丑为金库，辛金偏财入库，财源有储藏。
  - **傲物志高**：伤官旺盛者性格傲慢，志向远大但不易与人合作。
  - **冲库发财**：戌冲丑库，冲开财库则财源涌出。

- 规范化释义（primary_lang_explained）：

  本节讲「六丙日，己丑时」：

  - 己土伤官明见，克制丑中癸水官星余气，形成「伤官背禄」之象；
  - 若柱中再透癸水，伤官见官，为祸更重；若见庚辛金，伤官生财，反为福庆；
  - 丑为财库，若能冲开或行运配合，财源可发。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Bing Days with Ji-Chou Hour":

  - Ji Earth (Hurting Official) is visibly present, overcoming Gui Water (Official) residual energy in Chou, forming a pattern of "hurting official against fortune."
  - If the pillar further reveals Gui Water, hurting official meets official brings greater misfortune; if Geng-Xin Metal appears, hurting official generates wealth, bringing fortune instead.
  - Chou serves as wealth treasury; if clashed open or aligned with fortune cycles, wealth sources can flourish.

- 核心要点：

  - 本格以「伤官背禄」为核心，结构偏凶。
  - 若能转为「伤官生财」，则凶转吉。
  - 财库需冲开方能发用，否则财源受限。

- 详细解说：

  1. **伤官背禄的困境**  
     - 己土伤官克制癸水正官，破坏了官禄的根基；  
     - 伤官旺者性格傲慢，容易与人产生矛盾。

  2. **伤官生财的转机**  
     - 若柱中有庚辛金，伤官生财，财星得用；  
     - 形成「伤官生财」的良性结构，凶转吉。

  3. **财库的运用**  
     - 丑为金库（辛金偏财），财源有储藏；  
     - 需要戌冲或行运冲开，方能发挥财库的价值。

- 校勘与字词辨析：

  - 「无匙钥」比喻财库未开，财源受限。
  - 「近贵谋夺劫财」指接近贵人但可能有财务纠纷。
  - **English**：
    - Close to nobles but may have financial disputes.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_101]` `[trigger: 伤官背禄]` `[factor_trigger: shangguan_beilu AND aowu_zhigao]` `[role: 主干]` 六丙日生时己丑，伤官背禄傲物志高。 → 《三命通会》卷八#六丙日己丑时
  - `[ns_smth_08_102]` `[trigger: 财库藏金]` `[factor_trigger: caiku_cangjin AND chou_wei_jinku]` `[role: 主干依赖]` 丙日财官库里藏，戌辰未字显文章。 → 《三命通会》卷八#六丙日己丑时
  - `[ns_smth_08_103]` `[trigger: 无匙钥]` `[factor_trigger: wu_chiyao AND caiku_bujin]` `[role: 条件分支]` 身衰若也无匙钥，求名求利总平常。 → 《三命通会》卷八#六丙日己丑时
  - `[ns_smth_08_104]` `[trigger: 破出财官]` `[factor_trigger: pochu_caiguan AND bi_wang]` `[role: 总结]` 运交未戌不寻常，破出财官必旺。 → 《三命通会》卷八#六丙日己丑时"""
    normalized_text_zh: str = """"""
    subject: str = "六丙日己丑时断：伤官背禄与财库藏金"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_bing', 'bazi_semantic', 'bazi_state_shangguan_5', 'bazi_semantic', 'bazi_relation_metal_1', 'bazi_semantic', 'bazi_state_shangguan_8', 'bazi_semantic', 'hour_branch_chou', 'bazi_semantic', 'bazi_condition_geng_xin_metal', 'bazi_semantic', 'source_ref', 'rel_smth_08_076', 'shangguan_beilu', 'rel_smth_08_077', 'caiku_cangjin', 'rel_smth_08_078', 'jiangengxin_jin', 'evi_smth_08_076', 'shangguan_beilu', 'rule_beilu', 'evi_smth_08_077', 'caiku_cangjin', 'rule_caiku', 'evi_smth_08_078', 'shangguan_shengcai', 'rule_shengcai', 'map_smth_08_051', 'map_smth_08_052']
    
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
        l1_anchor="smth_v1.0.0_六丙日己丑时断_伤官背禄与财库藏金_001_L1",
    )
    version: str = "1.0.0"
