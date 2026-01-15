"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412712
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
    semantic_id="smth_v1.0.0_印绶与资身之本_001",
    book_id="sanming",
    engine_id="bazi"
)
class 印绶与资身之本(SemanticEntry):
    """
    - **原文（source_text）**：

  论印绶：印绶者，乃五行生我之名。如甲乙在亥子月，丙丁在寅卯月之类，乃我气之源，为生气，为父母，能护我官星，使无伤克。譬人生得物相助相养，受现成之福，...
    """
    
    original_text: str = """- **原文（source_text）**：

  论印绶：印绶者，乃五行生我之名。如甲乙在亥子月，丙丁在寅卯月之类，乃我气之源，为生气，为父母，能护我官星，使无伤克。譬人生得物相助相养，受现成之福，岂不为妙？此格主聪明，多智慧，性慈惠，语善良，迟讷体，貌丰厚，能饮食，平生少病，不逢凶横，但吝财耳。为官多为正官，受宣敕，不拘文武，皆掌印信。喜官星，以官能生印。《经》云：印赖官生。又云：有官无印，即非真官；有印有官，方成厚福是也。忌财星，以财能破印。《经》云：印绶生月岁时，忌见财星，运入财乡，却宜退身避位是也。岁运同论。印绶不逢损伤，多受父母倚荫，资财见成，安享富贵。诸命相比，当以印绶多者为上，月最要，日时次之。年干虽重，须归禄月日时，方可取用。若年露印，月日时无，亦不济事。四柱元有官星为妙；若印绶少、官鬼多，或入他格，又不可专言印绶。若印绶复遇拱禄、专禄、归禄、鼠贵、夹贵、时贵等格，尤为奇特，但主少子或无子，印绶多者清孤。凡印绶，喜七煞，但煞不可太多，多则伤身。原无七煞，行运遇之则发；原有七煞，行财运，或印绶死绝，或临墓地，皆凶。《经》云：煞能生印，畏行财乡，破印助鬼，决主不详。凡格喜身旺，惟印绶喜生弱。若元局带财伤印，运行比劫身旺，亦能发福，无则不宜。如无官煞财神，又行身旺，主平常。

- 分字分词释义：

  - **印绶**：五行生我之气，既为父母、长辈之象，也为学历、资格、文凭、凭证之象。
  - **护官星，使无伤克**：印能护官，使官不受伤官、七煞的破坏，故“有官无印，即非真官”。
  - **喜官星、忌财星**：官能生印，财能破印，印格以官为友、以财为敌。
  - **印绶多者清孤、少子或无子**：印过多则偏向清冷、孤高，易减损子嗣缘分或与后代距离感较大。

- **规范化释义（primary_lang_explained）**：

  印绶格重在“资身”二字：

  - 一方面，它象征父母家世、长辈扶持、学历文凭、制度内的资格与认可；
  - 另一方面，它也代表内在的思考能力、学习能力与自我修养。

  命局印旺而得官生者，多主：

  - 聪明有学，适合走文教、制度、专业技术等道路；
  - 依靠正当路径与体制资源获得稳定地位；
  - 一生较少大病与横祸，但在金钱运用上偏于保守、吝财。

- 核心要点：

  - 印绶是**身之根与官之护**，以护官、养身为主。
  - 喜见官星生印，忌财星破印；七煞若能生印亦可为用，但不可太过。
  - 印多则清高孤独，印少则难以承接父母与制度资源。

- 详细解说：

  在现代环境中，可以把印绶理解为“系统内的认可”与“学习—认证体系”：

  - 印旺而有官，多主重视学历、证书、职称、编制等，并以此作为人生主线；
  - 财旺破印，则常在追逐现实利益与体制规范之间拉扯，需要特别注意不以短期收益损害长期资质与信誉。

  另外，印绶还与健康、免疫力、恢复力相关。印旺者往往更能承受压力、调动资源自救；印弱而财煞过盛者，则在遭遇打击时更难恢复。

- **校勘与字词辨析（双语）**：

  - 原文中关于“印绶多者清孤、少子或无子”的说法，本稿仅作性格与缘分层面的提示，不以此作简单断绝后代之命。
  - 对“煞能生印，畏行财乡”一条，本稿在释义中强调“七煞—印—财”的能量流向，以免读者误以为七煞本身即必凶。
  - **English**：
    - Balanced view provided to prevent misunderstanding that Seven-Kill is inherently inauspicious.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_141]` `[trigger: 印纶定义]` `[factor_trigger: yinshou_presence AND shengwo_zhiming]` `[role: 主干]` 印纶者，乃五行生我之名。乃我气之源，为生气，为父母。 → 《三命通会》卷六#论印纶
  - `[ns_smth_06_142]` `[trigger: 印赖官生]` `[factor_trigger: guan_shengyin AND youguan_youyin]` `[role: 主干依赖]` 印赖官生。有官无印，即非真官；有印有官，方成厚福。 → 《三命通会》卷六#论印纶
  - `[ns_smth_06_143]` `[trigger: 忌财破印]` `[factor_trigger: ji_caixing AND cai_poyin]` `[role: 条件分支]` 忌财星，以财能破印。运入财乡，却宜退身避位。 → 《三命通会》卷六#论印纶
  - `[ns_smth_06_144]` `[trigger: 印多清孤]` `[factor_trigger: yin_duo AND qinggu_shaozi]` `[role: 总结]` 印纶多者清孤，主少子或无子。 → 《三命通会》卷六#论印纶"""
    normalized_text_zh: str = """"""
    subject: str = "印绶与资身之本"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_37', 'bazi_semantic', 'bazi_structure_factor_83', 'bazi_semantic', 'bazi_state_factor_27', 'bazi_semantic', 'bazi_state_degree_25', 'bazi_semantic', 'bazi_condition_factor_197', 'bazi_semantic', 'bazi_condition_factor_198', 'bazi_semantic', 'source_ref', 'rel_smth_06_133', 'yinshou_ge_presence', 'rel_smth_06_134', 'yinguan_peihe', 'rel_smth_06_135', 'caipoyin_risk', 'evi_smth_06_133', 'yinshou_ge_presence', 'rule_yinshou', 'evi_smth_06_134', 'yinguan_peihe', 'rule_guansheng', 'evi_smth_06_135', 'caipoyin_risk', 'rule_poyin', 'map_smth_06_089', 'map_smth_06_090']
    
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
        l1_anchor="smth_v1.0.0_印绶与资身之本_001_L1",
    )
    version: str = "1.0.0"
