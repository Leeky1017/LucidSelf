"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559595
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
    semantic_id="yhzp_v1.0.0_格局生死引用_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 格局生死引用(SemanticEntry):
    """
    - **原文（source_text）**：  
  格局生死引用。  
  夫格局者，自有定论，今略而述之。印绶见财，行财运、又兼死绝，必入黄泉；如柱有比肩，庶几有解。正官见杀，及伤官刑冲破害，岁运...
    """
    
    original_text: str = """- **原文（source_text）**：  
  格局生死引用。  
  夫格局者，自有定论，今略而述之。印绶见财，行财运、又兼死绝，必入黄泉；如柱有比肩，庶几有解。正官见杀，及伤官刑冲破害，岁运相并必死。正财偏财，见比肩分夺、劫财阳刃，又见岁运冲合必死。伤官之格、财旺身弱、官杀重见、混杂冲刃，岁运又见必死；活则残伤。拱禄拱贵填实，又见官空亡冲刃，岁运重见即死。日禄归时，刑冲破害；见七杀官星空亡冲刃必死。杀官大忌，岁运相并必死。其馀诸格，并忌杀及填实，岁运并临必死。会诸凶神恶煞勾绞空亡吊客墓病死宫诸煞，十死九生。官星太岁、财多身弱，元犯七杀，身轻有救则吉，无救则凶。金多夭折，水盛飘流，木旺则夭，土多痴呆，火多顽愚，太过不及。作此论，一不可拘，二须敢断；必须理会推之，求其生死决矣！

- **分字分词释义**：
  - **印绶见财行财运又兼死绝必入黄泉**：印绶见财运又逢死绝，必死。
  - **正官见杀及伤官刑冲破害岁运相并必死**：正官见杀伤刑冲，岁运并临必死。
  - **正财偏财见比肩分夺劫财阳刃又见岁运冲合必死**：财格见劫刃岁运冲必死。
  - **伤官之格财旺身弱官杀重见混杂冲刃岁运又见必死**：伤官财旺身弱官杀混杂必死。
  - **拱禄拱贵填实又见官空亡冲刃岁运重见即死**：拱禄贵填实冲刃必死。
  - **日禄归时刑冲破害见七杀官星空亡冲刃必死**：日禄归时遇刑冲杀官必死。
  - **杀官大忌岁运相并必死**：杀官并临大忌必死。
  - **金多夭折水盛飘流木旺则夭土多痴呆火多顽愚**：五行太过各有其害。
  - **一不可拘二须敢断**：不可拘泥，须敢于判断。
  - **必须理会推之求其生死决矣**：理会推算以决生死。

- **规范化释义（primary_lang_explained）**：  
  《格局生死引用》系统总结各格局在岁运冲破下的生死判断法则，是实务判命中最严峻的"生死关"判断标准。**印绶格生死**：印绶见财行财运又兼死绝必入黄泉，如柱有比肩庶几有解。**正官格生死**：正官见杀及伤官刑冲破害岁运相并必死。**财格生死**：正财偏财见比肩分夺劫财阳刃又见岁运冲合必死。**伤官格生死**：伤官之格财旺身弱官杀重见混杂冲刃岁运又见必死活则残伤。**拱禄拱贵格生死**：填实又见官空亡冲刃岁运重见即死。**日禄归时格生死**：刑冲破害见七杀官星空亡冲刃必死。**杀官格生死**：杀官大忌岁运相并必死。**诸格通则**：其余诸格并忌杀及填实岁运并临必死；会诸凶神恶煞十死九生。**五行太过生死**：金多夭折水盛飘流木旺则夭土多痴呆火多顽愚。**判断原则**：一不可拘二须敢断，必须理会推之求其生死决矣。

- **完整对等诠释（secondary_lang_full）**：  
  **Pattern Life-Death Citation**: This section systematically summarizes the life-death judgment rules for various patterns when year-fortune clashes and breaks them—representing the most severe "life-death threshold" judgment standard in practical fate reading. **Seal Pattern Life-Death**: When Seal encounters Wealth, travels through Wealth fortune, and additionally meets death-extinction phases, one will inevitably enter the Yellow Springs (die); if the pillars contain Parallels, there may be some relief. **Proper Officer Pattern Life-Death**: When Proper Officer encounters Killing or Injury Officer with punishment, clash, breaking-harm, and year-fortune mutually join, death is certain. **Wealth Pattern Life-Death**: When Proper or Indirect Wealth encounters Parallels contending and dividing, Rob Wealth, or Yang Blade, and additionally encounters year-fortune clash-harmony, death is certain. **Injury Officer Pattern Life-Death**: In Injury Officer patterns where Wealth is vigorous but body is weak, Officer-Killing repeatedly appears, or there is mixed-muddled clash-blade, if year-fortune additionally encounters these, death is certain; if alive, severe injury remains. **Arched-Salary-Noble Pattern Life-Death**: When filled-solid and additionally encounters Officer void-extinction or clash-blade, if year-fortune repeatedly encounters, death follows immediately. **Day Salary Returns Time Pattern Life-Death**: With punishment-clash-breaking-harm, encountering Seven Killings or Officer Star in void-extinction or clash-blade, death is certain. **Killing-Officer Pattern Life-Death**: Killing-Officer is greatly taboo; when year-fortune mutually join, death is certain. **All Patterns General Rule**: All remaining patterns avoid Killing and filled-solid; when year-fortune simultaneously arrive, death is certain. Meeting various fierce spirits and evil deities like Gouchen, Jiaoshe, void-extinction, hanging-guest, tomb, illness, death palace, and other malevolent stars—nine out of ten will die. **Five Elements Excess Life-Death**: Excess Metal leads to early death, abundant Water leads to drifting away, vigorous Wood leads to early death, excess Earth leads to dullness, abundant Fire leads to foolishness. **Judgment Principle**: First, do not be rigidly constrained; second, one must dare to judge decisively; one must thoroughly comprehend and deduce to determine matters of life and death with finality!

- **核心要点**：  
  - 系统总结各格局在岁运冲破下的生死判断法则  
  - 印绶怕财运死绝、正官怕杀伤刑冲、财格怕比劫刃冲、伤官格怕财旺身弱官杀混杂  
  - 拱禄拱贵怕填实、日禄归时怕刑冲、杀官大忌岁运相并  
  - 五行太过不及皆有夭折痴呆之忧，判断须理会推之不可拘泥

- **详细解说**：  《格局生死引用》总结各格局的生死判断法则。**印绶格**——"印绶见财行财运又兼死绝必入黄泉"揭示印绶格的生死关。**正官财格**——"正官见杀及伤官刑冲破害岁运相并必死"；"正财偏财见比肩分夺劫财阳刃又见岁运冲合必死"阐述官财格的生死条件。**伤官格**——"伤官之格财旺身弱官杀重见混杂冲刃岁运又见必死活则残伤"揭示伤官格的凶险。**拱禄日禄**——"拱禄拱贵填实又见官空亡冲刃岁运重见即死"；"日禄归时刑冲破害见七杀官星空亡冲刃必死"阐述特殊格局的生死。**五行太过**——"金多夭折水盛飘流木旺则夭土多痴呆火多顽愚"揭示五行太过之害。末句"一不可拘二须敢断，必须理会推之求其生死决矣"点明判断原则。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_519]` `[trigger: 印纶生死]` `[factor_trigger: yinshou_jiancai_caiyun_sijue_ru_huangquan AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 印绶见财行财运又兼死绝必入黄泉；印绶格生死关。 → 《渊海子平·格局生死引用》
  - `[ns_yhzp_520]` `[trigger: 正官财格生死]` `[factor_trigger: zhengguan_jiansha_shangguan_bisi_caige_bijie_renchong_bisi AND bijie_yangren_chong]` `[role: 条件分支]` 正官见杀及伤官刑冲破害岁运相并必死；财格见比劫刃冲必死。 → 《渊海子平·格局生死引用》
  - `[ns_yhzp_521]` `[trigger: 伤官格生死]` `[factor_trigger: shangguan_caiwang_shenruo_guansha_hunza_chongren_bisi]` `[role: 条件分支]` 伤官之格财旺身弱官杀重见混杂冲刃岁运又见必死活则残伤。 → 《渊海子平·格局生死引用》
  - `[ns_yhzp_522]` `[trigger: 拱禄日禄生死]` `[factor_trigger: gonglu_gonggui_tianshi_jisi_rilu_guishi_xingchong_bisi AND anchong_qugui AND angui]` `[role: 条件分支]` 拱禄拱贵填实即死；日禄归时刑冲杀官必死。 → 《渊海子平·格局生死引用》
  - `[ns_yhzp_523]` `[trigger: 五行太过]` `[factor_trigger: jinduo_yaozhe_shuisheng_piaoliu_muwang_yao_tuduo_chidai_huoduo_wanyu]` `[role: 例外处理]` 金多夭折水盛飘流木旺则夭土多痴呆火多顽愚；五行太过之害。 → 《渊海子平·格局生死引用》
  - `[ns_yhzp_524]` `[trigger: 生死判断原则]` `[factor_trigger: buke_ju_xu_ganduan_lihui_tuizhi_shengsi_jue]` `[role: 总结]` 一不可拘二须敢断必须理会推之求其生死决矣。 → 《渊海子平·格局生死引用》"""
    normalized_text_zh: str = """"""
    subject: str = "格局生死引用"
    factor_refs: list = ['pattern_life_death', 'seal_wealth_death', 'year_fortune_join', 'filled_solid', 'dare_judge']
    
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
        l1_anchor="yhzp_v1.0.0_格局生死引用_001_L1",
    )
    version: str = "1.0.0"
