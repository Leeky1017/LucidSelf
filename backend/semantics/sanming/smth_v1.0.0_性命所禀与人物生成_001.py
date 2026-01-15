"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227385
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
    semantic_id="smth_v1.0.0_性命所禀与人物生成_001",
    book_id="sanming",
    engine_id="bazi"
)
class 性命所禀与人物生成(SemanticEntry):
    """
    - **原文（source_text）**：
  故五行各一其性，所谓各具一太极也；四时自有其序，所谓运用一太极也。五行四时，周而复始，所谓统体一太极也。而性之无所不在，又可见矣。夫天下无性外之物，而...
    """
    
    original_text: str = """- **原文（source_text）**：
  故五行各一其性，所谓各具一太极也；四时自有其序，所谓运用一太极也。五行四时，周而复始，所谓统体一太极也。而性之无所不在，又可见矣。夫天下无性外之物，而性无不在，此无极、二五所以混融而无间，所谓妙合者也。无极是理，二五是气。真以理言，太极无妄之谓也；精以气言，阴阳五行，不二之谓也。凝者，聚也，气聚而成形也。盖性为之主，而阴阳五行为之经纬错综，又各以类凝聚而成形焉。阳而健者成男，则父之道也；阴而顺者成女，则母之道也，是人物之始，以气化而生者也。气聚成形，则形交气感，遂以形化，而万物生生变化无穷矣。鲍鲁斋司：大地以气交而生人物，观其所交，则气之所至，可以知其类之所从出矣。天气交乎地，于人为男，于物为牡；地气交乎天，于人为女，于物为牝，男女牝牡，又自交而生生化化不穷。人物既生，气随天地之气升降交感。人得天地之中气，四方之气无不感；物得天地之徧气，而亦各随所感。故观天地之气交，可以知人物之初生矣；观天地之气感，可以知人物之相生矣。朱子曰：乾道成男，坤道成女，凝体于造化之初，二气交感，化生万物，流行于造化之后，此理之常也。若姜嫄、简狄之生稷、契，则又不可以先后言矣，此理之变也。张九韶曰：论人物始生于天地肇判之初，则由气化而后有形化，张子所谓天地之气生之是也。论人物始生于结胎受形之初，则由精气之聚而后有是物，朱子所谓阴精阳气聚而成物是也。由是言之，则人也、物也，气也、形也，孰有出于阴阳之外哉？

- **规范化释义（primary_lang_explained）**：
  五行各守其性，却又各具一太极；四时各守其序，却又共同运用一太极。性无所不在，凝聚为气，气聚为形，形又随气而化，生生不已。人物之生，皆由阴阳二气交感而来：乾道成男，坤道成女，天地之气在不同位次上交感，便生出男女牝牡与万类众生。于是，人和万物在本质上都离不开阴阳与五行，只是各随所感之气而形成不同类型。

- **完整对等诠释（secondary_lang_full）**：

  This passage links the cosmological discussion directly to the birth of living beings. Each of the Five Elements maintains its own nature yet "contains a Taiji", and each season keeps its proper sequence yet jointly "operates one Taiji". Universal nature is present everywhere, condensing into qi, qi condensing into form, and form in turn responding to further movements of qi. Men and women, male and female creatures, all arise from the mutual stimulation of yin and yang: the creative Dry aspect forms males, the receptive Earth aspect forms females. Human beings and the myriad creatures are therefore nothing other than particular condensations of the same yin–yang and Five‑Element field, differentiated according to the kinds of qi they receive at conception and during growth.

- **分字分词释义**：
  - **各具一太极**：每一元素、每一层面都各自完整地体现太极之理。
  - **妙合**：阴阳五行与无极之理融为一体、浑然无间的状态。
  - **气化/形化**：前者指气自行聚散的初始化生，后者指形成后的交感繁衍。
  - **中气/偏气**：人得天地之中气，万物各得偏气，据此分出类型高下。

- **核心要点**：
  - 命局中的「人」，只是天地气机之一种凝聚方式，本质仍是阴阳五行之气；
  - 论命时不能把人抽离开天地，只谈个人欲望或性格，而应放回「人与天地同一气机」的视野里。

- **应用推演（操作顺序）**：
  1) 立命时先看「气从何来」：结合年、月、日、时与地理环境，判断此命所受之气偏向何类（寒热燥湿、清浊厚薄），而不只看十神标签；
  2) 将「人物生成」理解为「类的分化」：在六亲、职业、环境判断中，先按气类（如木气重则向生长、教育、规划；金气重则向裁断、执行、规则）分群，再细分到具体行业与角色；
  3) 推岁运时，把运视作「再受一次天地之气」：考察运气与本命之气是相类相协，还是相反相克，从而判断这一阶段是「同类加强」还是「异类激变」；
  4) 在系统设计中，可为每一类人物/事件建立对应的「气型标签」（如阳健、阴柔、混浊、中和），使算法先按气型归类，再调用对应的规则库。

- **反例与边界**：
  - 只从心理学标签（外向/内向、乐观/悲观）去解释命局，而完全不看其所受天地之气与环境背景，这是将「性」与「气」割裂；
  - 认为命盘可以脱离时代与地理单独成立，例如用同一套解释系统去看古代农耕社会与当代城市信息社会，而不调整「人物生成」的具体载体；
  - 把「性命所禀」理解成绝对的宿命，否认后天修为与选择对气机流向的修正空间，与本段「人物既生，气随天地之气升降交感」的动态观不符；
  - 在工程化中，若只用静态星性表驱动推理，而不引入「气机标签/环境变量」，则难以承载本节所言的「同一性遍在而各随所感」。

- **小例（示意）**：
  - 某命局木火旺、金水弱，生于春夏之间，又居于阳光充足之地，从事教育与内容创作，此即「所禀之性」与「所处之气」同调，人物生成倾向于外放生长；若迁居寒地、久处封闭空间，其气机可能一度郁结，此时调运与修为方向宜偏向「舒展」而非再压抑；
  - 在命理知识库中，将不同地域/时代的典型人物样本按「气类 + 职类」聚类，能更好地体现「同一阴阳五行之气，在不同条件下凝聚为迥异人物」这一节所讲的思想。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_018]` `[trigger: 太极遍在]` `[factor_trigger: taiji_omnipresent=individual_and_collective]` `[role: 主干]` 五行各一其性，所谓各具一太极也。 → 《三命通会》卷一#性命所禀条
  - `[ns_smth_019]` `[trigger: 气聚成形]` `[factor_trigger: qi_condensation=form_generation]` `[role: 主干依赖]` 气聚而成形也。 → 《三命通会》卷一#性命所禀条
  - `[ns_smth_020]` `[trigger: 乾坤生人]` `[factor_trigger: qian_kun=gender_formation]` `[role: 主干依赖]` 乾道成男，坤道成女。 → 《三命通会》卷一#性命所禀条
  - `[ns_smth_021]` `[trigger: 中气偏气]` `[factor_trigger: qi_quality=human_vs_creature]` `[role: 边界条件]` 人得天地之中气，物得天地之偏气。 → 《三命通会》卷一#性命所禀条
  - `[ns_smth_600]` `[trigger: 调候用神]` `[factor_trigger: diaohou_yongshen]` `[role: 条件分支]` 调候用神为寒暖燥湿之调节。 → 《三命通会》卷一
  - `[ns_smth_601]` `[trigger: 调候需求]` `[factor_trigger: diaohou_xuqiu]` `[role: 条件分支]` 调候需求明确主平衡。 → 《三命通会》卷一
  - `[ns_smth_602]` `[trigger: 斗数格局]` `[factor_trigger: doushu_geju]` `[role: 条件分支]` 斗数格局定层次。 → 《三命通会》卷一
  - `[ns_smth_603]` `[trigger: 短命风险]` `[factor_trigger: duanming_fengxian]` `[role: 条件分支]` 短命风险高主夭折。 → 《三命通会》卷一
  - `[ns_smth_604]` `[trigger: 多合多冲]` `[factor_trigger: duohe_duochong]` `[role: 条件分支]` 多合多冲主动荡。 → 《三命通会》卷一
  - `[ns_smth_605]` `[trigger: 夺财效应]` `[factor_trigger: duocai_xiaoying]` `[role: 条件分支]` 夺财效应大主破财。 → 《三命通会》卷一
  - `[ns_smth_606]` `[trigger: 夺禄效应]` `[factor_trigger: duolu_xiaoying]` `[role: 条件分支]` 夺禄效应大主失位。 → 《三命通会》卷一
  - `[ns_smth_607]` `[trigger: 发达层次]` `[factor_trigger: fada_cengci]` `[role: 结果]` 发达层次高主大贵。 → 《三命通会》卷一
  - `[ns_smth_608]` `[trigger: 犯刑冲]` `[factor_trigger: fan_xingchong]` `[role: 条件分支]` 犯刑冲主不顺。 → 《三命通会》卷一
  - `[ns_smth_609]` `[trigger: 犯太岁]` `[factor_trigger: fan_taisui]` `[role: 条件分支]` 犯太岁主凶险。 → 《三命通会》卷一
  - `[ns_smth_610]` `[trigger: 反局效应]` `[factor_trigger: fanju_xiaoying]` `[role: 条件分支]` 反局效应主逆转。 → 《三命通会》卷一
  - `[ns_smth_611]` `[trigger: 仿格成立]` `[factor_trigger: fangge_chengli]` `[role: 条件分支]` 仿格成立主假贵。 → 《三命通会》卷一
  - `[ns_smth_612]` `[trigger: 分析深度]` `[factor_trigger: fenxi_shendu]` `[role: 条件分支]` 分析深度决定准确度。 → 《三命通会》卷一
  - `[ns_smth_613]` `[trigger: 风险评估]` `[factor_trigger: fengxian_pinggu]` `[role: 条件分支]` 风险评估高主谨慎。 → 《三命通会》卷一
  - `[ns_smth_614]` `[trigger: 扶抑格]` `[factor_trigger: fuyige]` `[role: 条件分支]` 扶抑格为正格基本类型。 → 《三命通会》卷一
  - `[ns_smth_615]` `[trigger: 扶抑用神]` `[factor_trigger: fuyi_yongshen]` `[role: 条件分支]` 扶抑用神为平衡之神。 → 《三命通会》卷一
  - `[ns_smth_616]` `[trigger: 富贵层次]` `[factor_trigger: fugui_cengci]` `[role: 结果]` 富贵层次定高低。 → 《三命通会》卷一
  - `[ns_smth_617]` `[trigger: 干支配合]` `[factor_trigger: ganzhi_peihe]` `[role: 条件分支]` 干支配合定吉凶。 → 《三命通会》卷一
  - `[ns_smth_618]` `[trigger: 干支气场]` `[factor_trigger: ganzhi_qichang]` `[role: 条件分支]` 干支气场决定格局。 → 《三命通会》卷一
  - `[ns_smth_619]` `[trigger: 干支五行]` `[factor_trigger: ganzhi_wuxing]` `[role: 主干]` 干支五行为命理基础。 → 《三命通会》卷一
  - `[ns_smth_620]` `[trigger: 干支组合]` `[factor_trigger: ganzhi_zuhe]` `[role: 条件分支]` 干支组合定格局。 → 《三命通会》卷一
  - `[ns_smth_621]` `[trigger: 格局成败]` `[factor_trigger: geju_chengbai]` `[role: 条件分支]` 格局成败决定层次。 → 《三命通会》卷一
  - `[ns_smth_622]` `[trigger: 格局层次]` `[factor_trigger: geju_cengci]` `[role: 条件分支]` 格局层次定富贵程度。 → 《三命通会》卷一
  - `[ns_smth_623]` `[trigger: 格局高低]` `[factor_trigger: geju_gaodi]` `[role: 结果]` 格局高低决定命运。 → 《三命通会》卷一
  - `[ns_smth_624]` `[trigger: 格局类型]` `[factor_trigger: geju_leixing]` `[role: 条件分支]` 格局类型定职业。 → 《三命通会》卷一
  - `[ns_smth_625]` `[trigger: 财官冲刚风险]` `[factor_trigger: caiguan_chonggang_risk]` `[role: 条件分支]` 财官冲刚有风险。 → 《三命通会》卷一
  - `[ns_smth_626]` `[trigger: 财官伏藏条件]` `[factor_trigger: caiguan_fucang_condition]` `[role: 条件分支]` 财官伏藏有条件。 → 《三命通会》卷一
  - `[ns_smth_627]` `[trigger: 财官救助]` `[factor_trigger: caiguan_jiuzhu]` `[role: 条件分支]` 财官救助主贵。 → 《三命通会》卷一
  - `[ns_smth_628]` `[trigger: 财官两成]` `[factor_trigger: caiguan_liangcheng]` `[role: 条件分支]` 财官两成主大贵。 → 《三命通会》卷一
  - `[ns_smth_629]` `[trigger: 财官配置类型]` `[factor_trigger: caiguan_peizhi_leixing]` `[role: 条件分支]` 财官配置类型定格局。 → 《三命通会》卷一
  - `[ns_smth_630]` `[trigger: 财官太旺]` `[factor_trigger: caiguan_taiwang]` `[role: 条件分支]` 财官太旺主克身。 → 《三命通会》卷一
  - `[ns_smth_631]` `[trigger: 财官为本]` `[factor_trigger: caiguan_weiben]` `[role: 主干]` 财官为本主富贵。 → 《三命通会》卷一
  - `[ns_smth_632]` `[trigger: 财官印三奇]` `[factor_trigger: caiguanyin_sanqi]` `[role: 条件分支]` 财官印三奇全主大贵。 → 《三命通会》卷一
  - `[ns_smth_633]` `[trigger: 财官印协同]` `[factor_trigger: caiguanyin_xietong]` `[role: 条件分支]` 财官印协同主贵显。 → 《三命通会》卷一
  - `[ns_smth_634]` `[trigger: 财化横溢]` `[factor_trigger: caihua_hengyi]` `[role: 条件分支]` 财化横溢主大富。 → 《三命通会》卷一
  - `[ns_smth_635]` `[trigger: 财克印风险]` `[factor_trigger: caikeyin_risk]` `[role: 条件分支]` 财克印有风险。 → 《三命通会》卷一
  - `[ns_smth_636]` `[trigger: 财库]` `[factor_trigger: caiku]` `[role: 条件分支]` 财库藏财主富。 → 《三命通会》卷一
  - `[ns_smth_637]` `[trigger: 财库暗藏]` `[factor_trigger: caiku_ancang]` `[role: 条件分支]` 财库暗藏主暗富。 → 《三命通会》卷一
  - `[ns_smth_638]` `[trigger: 财库复载]` `[factor_trigger: caiku_fuzai]` `[role: 条件分支]` 财库复载主大富。 → 《三命通会》卷一
  - `[ns_smth_639]` `[trigger: 财库稳定]` `[factor_trigger: caiku_wending]` `[role: 条件分支]` 财库稳定主持续富。 → 《三命通会》卷一
  - `[ns_smth_640]` `[trigger: 财破印风险]` `[factor_trigger: caipoyin_risk]` `[role: 条件分支]` 财破印有风险。 → 《三命通会》卷一
  - `[ns_smth_641]` `[trigger: 财气傲物风险]` `[factor_trigger: caiqi_aowu_risk]` `[role: 条件分支]` 财气傲物有风险。 → 《三命通会》卷一
  - `[ns_smth_642]` `[trigger: 财气汇聚]` `[factor_trigger: caiqi_huiju]` `[role: 条件分支]` 财气汇聚主富。 → 《三命通会》卷一
  - `[ns_smth_643]` `[trigger: 财入库程度]` `[factor_trigger: cairuku_chengdu]` `[role: 条件分支]` 财入库程度高主藏富。 → 《三命通会》卷一
  - `[ns_smth_644]` `[trigger: 财杀汇合风险]` `[factor_trigger: caisha_huihe_risk]` `[role: 条件分支]` 财杀汇合有风险。 → 《三命通会》卷一
  - `[ns_smth_645]` `[trigger: 财杀同宫]` `[factor_trigger: caisha_tonggong]` `[role: 条件分支]` 财杀同宫主凶险。 → 《三命通会》卷一
  - `[ns_smth_646]` `[trigger: 财身平衡]` `[factor_trigger: caishen_pingheng]` `[role: 条件分支]` 财身平衡主发财。 → 《三命通会》卷一
  - `[ns_smth_647]` `[trigger: 财势聚合]` `[factor_trigger: caishi_juhe]` `[role: 条件分支]` 财势聚合主大富。 → 《三命通会》卷一
  - `[ns_smth_648]` `[trigger: 财土破印风险]` `[factor_trigger: caitu_poyin_risk]` `[role: 条件分支]` 财土破印有风险。 → 《三命通会》卷一
  - `[ns_smth_649]` `[trigger: 财旺程度]` `[factor_trigger: caiwang_chengdu]` `[role: 条件分支]` 财旺程度高主大富。 → 《三命通会》卷一"""
    normalized_text_zh: str = """"""
    subject: str = "性命所禀与人物生成"
    factor_refs: list = ['nature_destiny', 'qi_interaction', 'qi_resonance', 'form_transformation', 'qi_endowment']
    
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
        l1_anchor="smth_v1.0.0_性命所禀与人物生成_001_L1",
    )
    version: str = "1.0.0"
