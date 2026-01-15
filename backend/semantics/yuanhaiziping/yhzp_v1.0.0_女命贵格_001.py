"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559258
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
    semantic_id="yhzp_v1.0.0_女命贵格_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 女命贵格(SemanticEntry):
    """
    - **原文（source_text）**：  
  正气官星。财官两旺。印绶天德。独杀有制。伤官生财。坐禄逢财。官星带合。日贵逢财。官贵逢官。官星坐禄。官星桃花。食神生旺。食神生财。杀化印绶。二德扶...
    """
    
    original_text: str = """- **原文（source_text）**：  
  正气官星。财官两旺。印绶天德。独杀有制。伤官生财。坐禄逢财。官星带合。日贵逢财。官贵逢官。官星坐禄。官星桃花。食神生旺。食神生财。杀化印绶。二德扶身。三奇合局。阳刃有制。拱禄拱贵。归禄逢财。

- **分字分词释义**：
  - **正气官星**：官星纯正无杂，无七杀混杂，主夫贵。
  - **财官两旺**：财星与官星皆旺盛，财生官主夫荣妻贵。
  - **印绶天德**：印绶配天德贵人，主名望与庇护。
  - **独杀有制**：唯一七杀有食神或印绶制化，主贵。
  - **伤官生财**：伤官生财星，才华转化为财富。
  - **坐禄逢财**：日主坐禄且逢财星，主富贵稳厚。
  - **官星带合**：官星与日主或他干相合，主夫妻有情。
  - **日贵逢财**：日贵格逢财星，富贵双全。
  - **官贵逢官**：天乙贵人与官星同见，主大贵。
  - **官星坐禄**：官星坐于禄位，主夫禄俸优厚。
  - **官星桃花**：官星配桃花，夫有才貌或风流但不失贵。
  - **食神生旺**：食神得令生旺，主子息荣贵。
  - **食神生财**：食神生财星，子息带财或技艺生财。
  - **杀化印绶**：七杀生印绶，杀气转化为贵气，主大贵。
  - **二德扶身**：天德月德扶助日主，主庇护与名望。
  - **三奇合局**：甲戊庚或乙丙丁等三奇合成局，主奇贵。
  - **阳刃有制**：阳刃有官杀制伏，凶神转吉。
  - **拱禄拱贵**：虚拱禄位或贵人，主暗贵。
  - **归禄逢财**：日主之禄归于时柱且逢财，主晚年富贵。

- **规范化释义（primary_lang_explained）**：  
  《女命贵格》列举19种女命贵格配置。**官星系列**：正气官星（官星纯正）、财官两旺、官星带合、官贵逢官、官星坐禄、官星桃花（官星配桃花反吉）。**印绶杀系列**：印绶天德、独杀有制、杀化印绶。**财禄系列**：坐禄逢财、日贵逢财、归禄逢财。**食伤系列**：伤官生财、食神生旺、食神生财。**格局系列**：二德扶身、三奇合局、阳刃有制、拱禄拱贵。

- **完整对等诠释（secondary_lang_full）**：  
  **Women's Fate Noble Patterns**: This section enumerates 19 types of noble pattern configurations for women's fate. **Officer Star Series**: Proper Qi Officer Star (Officer Star pure and correct), Wealth and Officer both vigorous, Officer Star carrying Combination, Officer Noble meeting Officer, Officer Star sitting on Salary, Officer Star with Peach Blossom (Officer Star combined with Peach Blossom is paradoxically auspicious). **Seal-Killing Series**: Seal with Heaven Virtue, Solitary Killing with control, Killing transforming into Seal. **Wealth-Salary Series**: Sitting on Salary meeting Wealth, Day Noble meeting Wealth, Returning Salary meeting Wealth. **Food-Injury Series**: Injury Officer generating Wealth, Food God born vigorous, Food God generating Wealth. **Pattern Series**: Two Virtues assisting the Body, Three Wonders (Oddities) combining into Bureau, Yang Blade with control, Arched Salary and Arched Noble.

- **核心要点**：  
  - 列举19种女命贵格配置，涵盖官星印绶杀财禄食伤格局等全方位组合  
  - 官星系列强调纯正得位：正气官星、财官两旺、官星坐禄等  
  - 印绶杀系列强调制化得宜：独杀有制、杀化印绶  
  - 财禄食伤系列强调生化有情：伤官生财、食神生财、禄逢财等

- **详细解说**：  《女命贵格》以条目形式列举19种女命富贵的标准格局配置，是女命判断的"正面清单"。可分为五大系列：**官星系列**6种——正气官星（官星纯正无杂为首贵）、财官两旺（财生官主夫荣）、官星带合（夫妻有情）、官贵逢官（贵人护夫）、官星坐禄（夫有禄俸）、官星桃花（夫有才貌）。**印绶杀系列**3种——印绶天德（名望庇护）、独杀有制（杀气受制）、杀化印绶（杀转贵气为最高贵格）。**财禄系列**3种——坐禄逢财（富贵稳厚）、日贵逢财（富贵双全）、归禄逢财（晚年富贵）。**食伤系列**3种——伤官生财（才华转财）、食神生旺（子息荣贵）、食神生财（技艺生财）。**格局系列**4种——二德扶身（庇护名望）、三奇合局（奇贵）、阳刃有制（凶转吉）、拱禄拱贵（暗贵）。这19种贵格构成了女命富贵的标准模板，命师可据此快速识别贵格。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_267]` `[trigger: 正气官星]` `[factor_trigger: nvming AND zhengqi_guanxing AND shougui AND anchong_qugui AND angui]` `[role: 主干]` 正气官星为女命首贵，官星纯正无杂主夫贵。 → 《渊海子平·女命贵格》
  - `[ns_yhzp_268]` `[trigger: 财官两旺]` `[factor_trigger: nvming AND caiguan_liangwang AND fugui AND anchong_qugui AND angui]` `[role: 条件分支]` 财官两旺，财生官旺主夫荣妻贵。 → 《渊海子平·女命贵格》
  - `[ns_yhzp_269]` `[trigger: 独杀有制]` `[factor_trigger: nvming AND dusha_youzhi AND gui AND anchong_qugui AND angui]` `[role: 条件分支]` 独杀有制，唯一七杀有制化主贵。 → 《渊海子平·女命贵格》
  - `[ns_yhzp_270]` `[trigger: 杀化印绶]` `[factor_trigger: nvming AND sha_hua_yinshou AND dagui AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 杀化印绶，七杀生印绶杀气转贵气，主大贵。 → 《渊海子平·女命贵格》
  - `[ns_yhzp_271]` `[trigger: 二德扶身]` `[factor_trigger: nvming AND erde_fushen AND bihu]` `[role: 条件分支]` 二德扶身，天德月德扶助日主主庇护与名望。 → 《渊海子平·女命贵格》
  - `[ns_yhzp_272]` `[trigger: 食神生旺]` `[factor_trigger: nvming AND shishen_shengwang AND zixirongui AND anchong_qugui AND angui]` `[role: 条件分支]` 食神生旺，食神得令生旺主子息荣贵。 → 《渊海子平·女命贵格》
  - `[ns_yhzp_273]` `[trigger: 阳刃有制]` `[factor_trigger: nvming AND yangren_youzhi AND xiong_zhuanji]` `[role: 条件分支]` 阳刃有制，阳刃有官杀制伏凶神转吉。 → 《渊海子平·女命贵格》
  - `[ns_yhzp_274]` `[trigger: 归禄逢财]` `[factor_trigger: nvming AND guilu_fengcai AND wannian_fugui AND anchong_qugui AND angui]` `[role: 条件分支]` 归禄逢财，日主之禄归于时柱且逢财主晚年富贵。 → 《渊海子平·女命贵格》
  - `[ns_yhzp_275]` `[trigger: 女命贵格纲领]` `[factor_trigger: nvming AND guige_gangling AND wudaxilie AND anchong_qugui AND angui]` `[role: 总结]` 女命贵格列举19种标准贵格配置，涵盖官星印杀财禄食伤格局五大系列。 → 《渊海子平·女命贵格》"""
    normalized_text_zh: str = """"""
    subject: str = "女命贵格"
    factor_refs: list = ['nineteen_women_noble_patterns', 'proper_qi_officer', 'killing', 'killing_transforms_seal', 'three_oddities_combined']
    
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
        l1_anchor="yhzp_v1.0.0_女命贵格_001_L1",
    )
    version: str = "1.0.0"
