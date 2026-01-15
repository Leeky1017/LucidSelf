"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157489
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
    semantic_id="smth_v1.0.0_六丙日壬辰时断_水火未济与煞星坐库_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六丙日壬辰时断水火未济与煞星坐库(SemanticEntry):
    """
    - 原文（source_text）：

  六丙日壬辰时断。

  六丙日生时壬辰，煞星坐库火难亲；身强反主为官贵，如弱定为贫夭人。丙日壬辰时，水火未济。丙见壬偏官，辰上壬水合局，火死无光。若生春夏，...
    """
    
    original_text: str = """- 原文（source_text）：

  六丙日壬辰时断。

  六丙日生时壬辰，煞星坐库火难亲；身强反主为官贵，如弱定为贫夭人。丙日壬辰时，水火未济。丙见壬偏官，辰上壬水合局，火死无光。若生春夏，身旺化鬼为官，复行身旺运，贵。秋冬，身衰鬼旺，更无倚托，贫下残疾。

  丙子日壬辰时，辰戌丑未月，偏官有制，吉。亥卯年月，富贵。寅午，行子运；子，行寅午运，俱贵。不然僧道。

  丙寅日壬辰时，身煞两旺，寅卯辰丑未年月，大贵。巳午戌年月亦贵。

  丙辰日壬辰时，身孤有财，主恶死。春生，行北运；夏，东运，俱贵。秋，南运，官至三品。

  丙午日壬辰时贵，身旺煞浅，若辰戌丑未月，偏官有制，贵；无制，平常。

  丙申日壬辰时，旺中灾。春平，夏福，秋富，冬寿促。若申子辰木局，干透印比助，大贵，食制煞亦贵。嫌煞透无制，财党煞强，夭死非命。

  丙戌日壬辰时，凶。卯未年月，运行火土，官至三品，妻贤子孝。辰戌丑月，平稳。寅午子巳年月，风宪。

  丙日壬辰怕见申，再逢阳水定灾屯；柱中若得寅午戌，变凶为吉贵绝伦。丙日壬辰时墓，身衰耗鬼当途。雁行难倚不相扶，妻子何须缘误。君子文章福助，常人恩反成疏。运行官禄任谋图，无破不贵即富。

- 分字分词释义：

  - **水火未济**：水火不能相济，壬水与丙火对立，形成冲突结构。
  - **煞星坐库**：壬水七煞入辰库，煞星有收藏但仍有威胁。
  - **化鬼为官**：七煞在有制有化的条件下，转为有用的官星。
  - **财党煞强**：财星生助七煞，使煞星更加强旺。

- 规范化释义（primary_lang_explained）：

  本节讲「六丙日，壬辰时」：

  - 壬水七煞在辰上有库，与丙火形成「水火未济」的对立结构；
  - 若春夏身旺，可化鬼为官，行身旺运则贵；若秋冬身衰，煞旺身弱，则贫夭残疾；
  - 歌诀提示：若柱中有寅午戌火局，可变凶为吉。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Six Bing Days with Ren-Chen Hour":

  - Ren Water Seven-Killing has its treasury at Chen, forming a "water-fire unfulfilled" opposing structure with Bing Fire.
  - If spring-summer with strong body, one can transform ghost into official; with strong-body fortune cycles, this becomes noble. If autumn-winter with weak body and strong killing, with no support, this leads to poverty, early death, or disability.
  - The verse indicates: if the chart contains Yin-Wu-Xu fire formation, bad can transform to good.

- 核心要点：

  - 本格以「水火未济」为核心，结构有冲突。
  - 身旺可化煞，身弱则受煞克。
  - 需防「财党煞强」导致的夭死非命。

- 详细解说：

  1. **水火未济的困境**  
     - 壬水七煞与丙火日主对立；  
     - 辰为水库，煞星有根，对日主构成威胁。

  2. **化鬼为官的转机**  
     - 若身旺且有制化，七煞可转为有用的官星；  
     - 行身旺运，可发挥煞星的执行力与权威。

  3. **身弱煞旺的风险**  
     - 秋冬丙火无气，壬水得令；  
     - 身弱煞旺，若无救助，主贫夭残疾。

- 校勘与字词辨析：

  - 「雁行难倚」形容兄弟姐妹各自发展，难以依靠。
  - 「无破不贵即富」强调若无刑冲克害，可得富贵。
  - **English**：
    - Without punishment-clash-control-harm, wealth and nobility attainable.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_113]` `[trigger: 水火未济]` `[factor_trigger: shuihuo_weiji AND huo_nan_qin]` `[role: 主干]` 六丙日生时壬辰，煞星坐库火难亲。 → 《三命通会》卷八#六丙日壬辰时
  - `[ns_smth_08_114]` `[trigger: 化鬼为官]` `[factor_trigger: huagui_weiguan AND shenwang_gui]` `[role: 主干依赖]` 身强反主为官贵，如弱定为贫夭人。 → 《三命通会》卷八#六丙日壬辰时
  - `[ns_smth_08_115]` `[trigger: 寅午戌火局]` `[factor_trigger: yinwuxu_huoju AND bian_xiong_wei_ji]` `[role: 条件分支]` 柱中若得寅午戌，变凶为吉贵绝伦。 → 《三命通会》卷八#六丙日壬辰时
  - `[ns_smth_08_116]` `[trigger: 无破即富]` `[factor_trigger: wupo_jifu AND ren_moutu]` `[role: 总结]` 运行官禄任谋图，无破不贵即富。 → 《三命通会》卷八#六丙日壬辰时"""
    normalized_text_zh: str = """"""
    subject: str = "六丙日壬辰时断：水火未济与煞星坐库"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_bing', 'bazi_semantic', 'bazi_state_water_fire_wei', 'bazi_semantic', 'bazi_relation_factor_78', 'bazi_semantic', 'bazi_state_factor_173', 'bazi_semantic', 'hour_branch_chen', 'bazi_semantic', 'bazi_condition_factor_51', 'bazi_semantic', 'source_ref', 'rel_smth_08_085', 'shuihuo_weiji', 'rel_smth_08_086', 'shaxing_zuoku', 'rel_smth_08_087', 'shenwang_youzhi', 'evi_smth_08_085', 'shuihuo_weiji', 'rule_weiji', 'evi_smth_08_086', 'shaxing_zuoku', 'rule_zuoku', 'evi_smth_08_087', 'huagui_weiguan', 'rule_huagui', 'map_smth_08_057', 'map_smth_08_058']
    
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
        l1_anchor="smth_v1.0.0_六丙日壬辰时断_水火未济与煞星坐库_001_L1",
    )
    version: str = "1.0.0"
