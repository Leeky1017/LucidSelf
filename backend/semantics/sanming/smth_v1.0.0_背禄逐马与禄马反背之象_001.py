"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412581
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
    semantic_id="smth_v1.0.0_背禄逐马与禄马反背之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 背禄逐马与禄马反背之象(SemanticEntry):
    """
    - **原文（source_text）**：

  背禄者，甲以辛为官为禄，甲生春夏，金绝，则无官矣，故为背禄。逐马者，甲以己土为财为马，被乙及亥卯未劫夺，甲无财矣，故为逐马。余例推。如壬子、壬子、丁...
    """
    
    original_text: str = """- **原文（source_text）**：

  背禄者，甲以辛为官为禄，甲生春夏，金绝，则无官矣，故为背禄。逐马者，甲以己土为财为马，被乙及亥卯未劫夺，甲无财矣，故为逐马。余例推。如壬子、壬子、丁未、乙巳，定取壬为官禄。壬亥月建禄，丁生子月，癸旺是煞，壬禄已过为背，向者有禄，背者无禄；丁取庚为财为马，子月庚死，此为背禄逐马，逢煞运，行劫地，亦不发福，无根元故也。《珞录子》云：“背禄逐马，守穷途而惶惶”，与此不同，能见赋中。

- 分字分词释义：

  - **背禄**：本有官星、禄位可用，却因时节或局势使之绝气、失势，如同“背向禄位”，难以真正承享。
  - **逐马**：本有财星、驿马可资行动与外出求财，却被比劫、劫财或劫夺之神夺去，反成“追逐无着”的奔波之象。
  - **金绝则无官**：以甲木而论，辛金为正官，春夏木旺金绝，虽见辛金，实则官星失根失势。
  - **被乙及亥卯未劫夺**：乙木为比肩，亥卯未为印比同气之地，皆能分夺己土财星，使甲木失其财马。
  - **壬禄已过为背**：以壬水言，亥为建禄之地，子为帝旺之地，例中所用之“禄”已过本位而不在命局要处，故曰“向者有禄，背者无禄”。
  - **煞运、劫地**：行运再逢七煞、比劫等旺地，本已薄弱的官禄、财马更难维系，易应贫困与奔波。
  - **无根元**：官、财皆缺根气与生助，既无印绶比劫作为正向根基，亦无实在根元可依。

- **规范化释义（primary_lang_explained）**：

  背禄逐马格，说的是一种“名义上有官禄、有财马，实际上难以长久享用”的局势。以甲木为例：辛金是它的正官与禄，己土是它的财星与驿马。若甲生于春夏，金气绝灭，即便命局中有辛金，也多属无根之官，难以真正成就；这是“背禄”。又若命局中原本有己土为财、为马，却被乙木比肩和亥卯未等同气之地反复劫夺，则财马虽名存实亡，只剩奔波追逐、难以积累；这是“逐马”。

  原文举壬子、壬子、丁未、乙巳一造说明：表面上壬水有建禄之名、丁火有财马之象，但壬的禄气已过本位而不在根处，丁火所凭的庚金财马又在子月死绝。结果是：过去似乎曾有官禄、财马的机会，如今却皆成“背向而去”，再逢七煞、比劫之运，只见穷途困顿，而难有长久之福。

- 核心要点：

  - 背禄逐马不单看一颗星，而是看**官禄与财马是否同时失根、失势**。
  - 若官星在绝地、死地或被严重泄耗，即便有名号，也多为“背禄”；若财星、驿马被比劫、劫财强夺，则成“逐马”。
  - 此格多主**前路曾有可观机会，却因根基不固、取向不当而错失**，后半生多奔波劳碌。
  - 若命局另有稳固之印绶、比劫根气，或有清纯的财官格成局，则“背禄逐马”只作减分之象，不必夸大为必穷之命。

- 详细解说：

  在格局层面，可以从三个角度理解“背禄逐马”：

  1. **从时令看官禄的背向**  
     官星、禄星需得令、有根方能承担权责。若如甲木生于春夏，木旺金绝，则辛金虽在局中，多半气绝无力，只余名义上的官禄。类似地，壬水离开亥月建禄之地，禄气退行，便有“向者有禄，背者无禄”的意味——人生曾有靠近权位的机会，后却渐行渐远。

  2. **从用神根基看财马的流失**  
     财星与驿马，本是推动人生流动与外求的动力。以甲木言，己土为财马；若己土被乙木比肩与亥卯未等木印所劫夺，则财马名存实亡：表面多在奔波、换工作、走动生计，实则难以真正积累财富或稳固事业基础。

  3. **从岁运触发看“穷途而惶惶”**  
     当大运、流年再临七煞、比劫等旺地时，本就羸弱的官禄与财马更受冲击：  
     - 有煞而无印，不是“化煞为权”，而是徒增压力；  
     - 有比劫而无财库，难成合伙之利，反多内耗与纷争。  
     于是格局所象，往往是“路曾经好过，却因一步步失去根基而走入穷途”。

  在实务判断中，可以将“背禄逐马”作为一种**风险标签**而非单独成格的贵局：

  - 若原局另有清纯的官格、财格成局，且禄、马各有一处牢靠根气，则可仅将此象视为“局中某一段经历的起落”，不必据此定终身贫贱。
  - 反之，若全局官财本就单薄，仅寄托于一处将绝、将亡之禄马，又遭岁运一再冲剥，则需警惕职业反覆、投资失利、迁徙无着等现实问题。

- **校勘与字词辨析（双语）**：

  - 原文“甲以辛为官为禄，甲生春夏，金绝则无官矣，故为背禄”一句，本稿在释义与白话中统一解释为：以**时令绝旺/绝灭**判断官星是否仍能担当其职，而不作单一星曜吉凶之断。
  - “被乙及亥卯未劫夺”一语，底本作“劫夺”，本稿视为比肩、印比同气分夺财马之象，不另改作比劫专业术语，以免与今人“比肩、劫财”名目混淆。
  - 《珞录子》原句“背禄逐马，守穷途而惶惶”，底本字形略讹，本稿据通行语境改作“惶惶”，并在白话中以“穷途困顿、心中惶惑”释之。
  - 例命“壬子、壬子、丁未、乙巳”，本稿仅作结构示意，强调“禄过本位、财马绝地”的组合，不逐条推演具体官阶与寿命，以免与他本异文混淆。
  - **English**：
    - Original text preserved to avoid confusion with variant readings from other editions regarding longevity.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_097]` `[trigger: 背禄定义]` `[factor_trigger: guan_shiling_jue AND lu_wugen]` `[role: 主干]` 甲以辛为官为禄，甲生春夏，金绝，则无官矣，故为背禄。 → 《三命通会》卷六#背禄逐马
  - `[ns_smth_06_098]` `[trigger: 逐马定义]` `[factor_trigger: cai_beijieduo AND ma_mingcunshiwang]` `[role: 主干依赖]` 甲以己土为财为马，被乙及亥卯未劫夺，甲无财矣，故为逐马。 → 《三命通会》卷六#背禄逐马
  - `[ns_smth_06_099]` `[trigger: 向背有无]` `[factor_trigger: lu_guobenwei AND xiangzhe_youlu]` `[role: 条件分支]` 壬禄已过为背，向者有禄，背者无禄。 → 《三命通会》卷六#背禄逐马
  - `[ns_smth_06_100]` `[trigger: 穷途惶惶]` `[factor_trigger: sha_yun AND jie_di AND wugengyuan]` `[role: 总结]` 背禄逐马，守穷途而惶惶。逢煞运，行劫地，亦不发福，无根元故也。 → 《三命通会》卷六#背禄逐马"""
    normalized_text_zh: str = """"""
    subject: str = "背禄逐马与禄马反背之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_82', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_degree_15', 'bazi_semantic', 'bazi_state_geju_1', 'bazi_semantic', 'bazi_condition_factor_175', 'bazi_semantic', 'bazi_condition_factor_176', 'bazi_semantic', 'bazi_condition_factor_177', 'bazi_semantic', 'source_ref', 'rel_smth_06_097', 'beilu_zhuma_risk', 'rel_smth_06_098', 'zhuma_chengdu', 'rel_smth_06_099', 'suiyun_chongbo_risk', 'evi_smth_06_097', 'beilu_zhuma_risk', 'rule_beilu', 'evi_smth_06_098', 'yuanju_lingyou_geju', 'rule_bujiu', 'evi_smth_06_099', 'zhiye_touzi_risk', 'rule_fanfu', 'map_smth_06_065', 'map_smth_06_066']
    
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
        l1_anchor="smth_v1.0.0_背禄逐马与禄马反背之象_001_L1",
    )
    version: str = "1.0.0"
