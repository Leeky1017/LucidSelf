"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559501
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
    semantic_id="yhzp_v1.0.0_万金赋_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 万金赋(SemanticEntry):
    """
    - **原文（source_text）**：  
  万金赋。  
  欲识五行生死诀，容易岂与凡人说，星中但以限为凭，子平但以运为诀；运行先布十二宫，看来何格堕时节，财官印绶与食神，当知轻重审分明。...
    """
    
    original_text: str = """- **原文（source_text）**：  
  万金赋。  
  欲识五行生死诀，容易岂与凡人说，星中但以限为凭，子平但以运为诀；运行先布十二宫，看来何格堕时节，财官印绶与食神，当知轻重审分明。  
  官星怕行七杀运，七杀犹畏官星临。  
  官杀混杂当寿夭，去官留杀仔细寻。  
  留官去杀莫逢杀，留杀去官官莫逢。  
  官杀受伤人必夭，更宜财格定前程。  
  日时偏正问何财，生怕干头带杀来。  
  劫若重逢人夭寿，孰知偏正甚为灾。  
  有财官运须荣发，财地官乡是福胎。  
  只怕日干元自弱，财多生杀赶身衰。  
  财多身弱行财运，此处方知下九台。  
  官不逢伤财不劫，寿山高耸岂能摧。  
  第一限逢印绶乡，运生生旺必荣昌。  
  官乡会合迁官职，死绝当头是祸殃。  
  若是逢财来害印，堕崖落水恶中亡；为官在任他乡死，作客逢之死路傍。  
  印不逢财人不死，如前逐一细推详。  
  财官印绶分明说，莫道食神非易诀；食神有气胜财官，只怕伤残前外截，却分轻重细推详，大忌财官为死绝。  
  伤官命运莫逢官，斩绞徒流祸百端。  
  月德日贵逢克战，此命危亡立马看。  
  飞天拱禄嫌填实，最怕绊神来犯干；子运行年来甲子；壬寅申地见丙申，巳丙一同推祸福；卯宫乙木怕相逢；巳宫戊庚丙辛会；午丁年上午戌凶；丑未年中须是祸，但宜迁运而搜寻。  
  同官同运如逢禄，逢禄刑祸来相侵。  
  外逢仍还逢内敌，其馀官分外方寻；外逢内敌为灾重，内逢外敌祸微侵。  
  戊己土皆分四季，杂气之中难又易，逐一依定数中推，受制受刑随运气，只定其凶此运中，何年月日灾刑重。  
  此是石金玉匣诀，只此泄漏与君知。

- **分字分词释义**：
  - **星中但以限为凭子平但以运为诀**：论命以运限为依凭，子平法以大运为关键。
  - **官星怕行七杀运七杀犹畏官星临**：正官怕行杀运，七杀亦怕官星冲。
  - **官杀混杂当寿夭**：官杀并见混杂，主寿夭之患。
  - **去官留杀仔细寻留官去杀莫逢杀**：去官留杀或留官去杀，需仔细权衡。
  - **财多身弱行财运此处方知下九台**：财多身弱再行财运，沦为最低层。
  - **官不逢伤财不劫寿山高耸岂能摧**：官不被伤财不被劫，寿山稳固。
  - **印不逢财人不死**：印星不被财克，人便不死。
  - **食神有气胜财官**：食神有气可胜过财官。
  - **伤官命运莫逢官斩绞徒流祸百端**：伤官命最忌逢官，主刑戮官非。
  - **此是石金玉匣诀**：此为万金秘诀，轻易不传。

- **规范化释义（primary_lang_explained）**：  
  《万金赋》是对子平命理中“财官印食 + 运限”综合判断的口诀总成，重点是：  
  - **生死诀与运限**：  
    - 欲识五行生死诀：真正懂五行生死旺衰之法，不是泛泛之谈，要结合“星中以限为凭、子平以运为诀”。  
    - 先布十二宫，再看何格堕于何时，把大运、流年与格局轻重一起权衡。  
  - **官杀取舍**：  
    - 官星怕行七杀运，七杀亦畏官星临——官杀互畏，关键在“配合与制化”。  
    - 官杀混杂则寿夭，需分“去官留杀”或“留官去杀”，看谁更适合做用神。  
    - 官杀受伤、人多夭折，此时不如“另立财格”，改以财格论前程。  
  - **财多身弱之祸**：  
    - 日干本弱而财多生杀，行财运则身愈衰，至“下九台”（极低层）。  
    - 官不遇伤、财不遭劫，寿山高耸不易摧，说明“身、财、官”三者平衡为上。  
  - **印绶与死绝**：  
    - 第一限得印绶之乡，大运生旺则荣昌；若财来克印、行死绝运，则有堕崖落水、异乡殒命之象。  
    - 印不逢财，人便不死；细推“谁生谁克”即可见端倪。  
  - **食神与伤官**：  
    - 食神有气胜似财官，是厚福之象；但若食神被伤、被截，反成隐患。  
    - 伤官命最忌再逢官，斩绞徒流之祸百端；月德、日贵若遭克战，亦有立见危亡之嫌。  
  - **细部格局与运中凶期**：  
    - 后文大量例举某干支组合在某运年的祸福、内敌外敌之分、戊己杂气在四季中的判法等，核心思想仍是：  
      - 先定“此运中总体凶吉级别”，再细推“哪一年、哪一月祸福最重”。  

- **完整对等诠释（secondary_lang_full）**：  
  **Ten-Thousand-Gold Secrets (Wan Jin Fu)**:  
  - **Method of Life–Death and Timing**: This ode states that the true key to Five-Element life–death phases lies not only in static structure but in timed movement—decanal limits and Zi Ping luck cycles. One must first lay out the twelve houses of the luck cycle, then see in which periods each pattern becomes strong or falls into critical phases.  
  - **Officer and Killing Management**: Officer and Seven Killings fear each other’s territories. Mixed, injured, or uncontrolled combinations shorten life or bring disasters. Sometimes one must discard Officer and keep Killing (or vice versa), depending on which can be properly supported and controlled, or switch to treating the chart as a Wealth pattern instead.  
  - **Wealth vs. Body Strength**: Charts with abundant Wealth but weak Day Master are especially vulnerable, particularly when walking further Wealth luck—this is "too much load on a frail body". Conversely, if Officer is not injured and Wealth is not robbed, long life and stable prosperity are indicated.  
  - **Seal, Food God, and Harm**: Well-placed Seals in early luck bring flourishing careers, but Seals destroyed by Wealth or falling in death/tomb phases portend accidents, drowning, or deaths in foreign lands. Strong Food God can outperform Wealth or Officer in bringing comfort and blessings, but if cut or harmed it loses its protective role.  
  - **Locating Peak Risk**: Many specific combinations of stems, branches, and luck are listed to illustrate when inner and outer enemies combine, when jail, execution, or violent death are likely, and when seemingly good patterns still contain hidden dangers. The general rule is: determine the overall quality of a luck decade, then pinpoint which year and month within it carry the heaviest blows.  

- **核心要点**：  
  - 真正的“万金秘诀”在于：以格局为体、以运限为用，动态看财官印食与官杀、伤官的组合.  
  - 官杀混杂时，必须分清去留：有时弃官留杀、有时留官去杀，或干脆改从财格.  
  - 财多身弱最怕再行财运，印多逢财则有坠崖溺水等极端风险.  
  - 食神有气可胜财官，伤官见官则“斩绞徒流祸百端”，月德日贵被克战时要高度警觉.  

- **详细解说**：  《万金赋》以"欲识五行生死诀，容易岂与凡人说"开篇，阐述财官印食与运限结合的核心秘诀.**运限为诀**——"星中但以限为凭，子平但以运为诀"确立运限的核心地位.**官杀取舍**——"官星怕行七杀运，七杀犹畏官星临"；"官杀混杂当寿夭，去官留杀仔细寻"揭示官杀配合与取舍之法.**财多身弱**——"财多身弱行财运，此处方知下九台"揭示财多身弱之害；"官不逢伤财不劫，寿山高耸岂能摧"为身财官平衡之吉象.**印绶护身**——"第一限逢印绶乡，运生生旺必荣昌"；"印不逢财人不死"揭示印绶护身之理.**食伤吉凶**——"食神有气胜财官"为食神厚福之象；"伤官命运莫逢官，斩绞徒流祸百端"为伤官见官之大忌.末句"此是石金玉匣诀，只此泄漏与君知"点明此为万金秘诀.

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_446]` `[trigger: 运限为诀]` `[factor_trigger: xingzhong_xianwei_ping AND ziping_yunwei_jue]` `[role: 主干]` 星中但以限为凭，子平但以运为诀；运限判命核心法. → 《渊海子平·万金赋》
  - `[ns_yhzp_447]` `[trigger: 官杀互畏]` `[factor_trigger: guanxing_pa_qishayun AND qisha_wei_guanxing_lin]` `[role: 条件分支]` 官星怕行七杀运，七杀犹畏官星临；官杀互畏之理. → 《渊海子平·万金赋》
  - `[ns_yhzp_448]` `[trigger: 官杀取舍]` `[factor_trigger: guansha_hunza_shouyao AND quguan_liusha AND faze]` `[role: 条件分支]` 官杀混杂当寿夭；去官留杀仔细寻；官杀取舍之法. → 《渊海子平·万金赋》
  - `[ns_yhzp_449]` `[trigger: 财多身弱]` `[factor_trigger: caiduo_shenruo AND xing_caiyun AND xia_jiutai]` `[role: 例外处理]` 财多身弱行财运此处方知下九台；财多身弱之害. → 《渊海子平·万金赋》
  - `[ns_yhzp_450]` `[trigger: 官不逢伤]` `[factor_trigger: guan_bufeng_shang AND cai_bujie AND shoushan_gaosong]` `[role: 条件分支]` 官不逢伤财不劫，寿山高耸岂能摧；身财官平衡之吉. → 《渊海子平·万金赋》
  - `[ns_yhzp_451]` `[trigger: 印绶护身]` `[factor_trigger: diyixian_feng_yinshou AND yunsheng_shengwang_rongchang AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 第一限逢印绶乡运生生旺必荣昌；印不逢财人不死. → 《渊海子平·万金赋》
  - `[ns_yhzp_452]` `[trigger: 伤官见官]` `[factor_trigger: shangguan_mingyun_mofeng_guan AND zhanjiao_tuliu_huobaidan]` `[role: 例外处理]` 伤官命运莫逢官，斩绞徒流祸百端；伤官见官大忌. → 《渊海子平·万金赋》
  - `[ns_yhzp_765]` `[trigger: 食神有气]` `[factor_trigger: shishen AND food_god_vigor]` `[role: 条件分支]` 食神有气胜财官；食神旺则福厚胜过财官. → 《渊海子平·万金赋》
  - `[ns_yhzp_453]` `[trigger: 万金赋纲领]` `[factor_trigger: wanjin_fu AND yunxian_weijue AND guansha_qushe AND shishang_jixxiong]` `[role: 总结]` 万金赋以运限为诀、官杀取舍、财多身弱、食伤吉凶为核心，阐述命运动态配置. → 《渊海子平·万金赋》"""
    normalized_text_zh: str = """"""
    subject: str = "万金赋"
    factor_refs: list = ['life_death_key', 'mixed_officer_killing', 'excess_wealth_weak_body', 'seal_destroyed_wealth', 'injury_meets_officer']
    
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
        l1_anchor="yhzp_v1.0.0_万金赋_001_L1",
    )
    version: str = "1.0.0"
