"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559274
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
    semantic_id="yhzp_v1.0.0_女命贱格_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 女命贱格(SemanticEntry):
    """
    - **原文（source_text）**：  
  官杀混杂。官杀无制。杀星太重。伤官太重。贪财坏印。比肩犯重。无官见合。无印见杀。伤官七杀。带合桃花。八字刑冲。财多身弱。阳刃冲刑。金神带刃。多官多...
    """
    
    original_text: str = """- **原文（source_text）**：  
  官杀混杂。官杀无制。杀星太重。伤官太重。贪财坏印。比肩犯重。无官见合。无印见杀。伤官七杀。带合桃花。八字刑冲。财多身弱。阳刃冲刑。金神带刃。多官多合。倒插桃花。身旺无依。伤官见官。

- **分字分词释义**：
  - **官杀混杂**：正官与七杀同见，夫星混乱，主贱。
  - **官杀无制**：官杀过旺无印化无食制，主极贱。
  - **杀星太重**：七杀过多过旺，压制日主，主贱。
  - **伤官太重**：伤官过旺克制官星（夫星），主克夫。
  - **贪财坏印**：财星克制印绶，贪财而坏名声。
  - **比肩犯重**：比肩过多，争夺财官，主争夫。
  - **无官见合**：命中无官星却多合神，主淫贱。
  - **无印见杀**：命中无印绶却见七杀，杀无化主凶。
  - **伤官七杀**：伤官与七杀同见，克夫且多灾。
  - **带合桃花**：合神配桃花，主淫乱不贞。
  - **八字刑冲**：四柱多刑冲，主灾祸连绵。
  - **财多身弱**：财星过多而日主弱，主为财所累。
  - **阳刃冲刑**：阳刃逢冲逢刑，主血光或刑克。
  - **金神带刃**：金神格配阳刃，凶上加凶。
  - **多官多合**：官星多且合神多，主多夫且淫。
  - **倒插桃花**：桃花在时柱，主晚年失节或子女不肖。
  - **身旺无依**：日主过旺无财官食伤依托，主孤贫。
  - **伤官见官**：伤官见官星，克夫为女命大忌。

- **规范化释义（primary_lang_explained）**：  
  《女命贱格》列举18种女命贱格配置。**官杀系列**：官杀混杂、官杀无制、杀星太重、多官多合、无官见合、无印见杀。**伤官系列**：伤官太重、伤官七杀、伤官见官。**财印系列**：贪财坏印、财多身弱。**比肩刃系列**：比肩犯重、阳刃冲刑、金神带刃。**桃花刑冲系列**：带合桃花、倒插桃花、八字刑冲、身旺无依。

- **完整对等诠释（secondary_lang_full）**：  
  **Women's Fate Base Patterns**: This section enumerates 18 types of base pattern configurations for women's fate. **Officer-Killing Series**: Officer and Killing mixed, Officer and Killing without control, Killing Star too heavy, Multiple Officers and Multiple Combinations, No Officer but seeing Combination, No Seal but seeing Killing. **Injury Officer Series**: Injury Officer too heavy, Injury Officer with Seven Killings, Injury Officer seeing Officer. **Wealth-Seal Series**: Greed for Wealth spoiling Seal, Abundant Wealth with Weak Body. **Parallel-Blade Series**: Parallels committing offense heavily, Yang Blade clashing and punishing, Metal Spirit carrying Blade. **Peach Blossom-Punishment-Clash Series**: Carrying Combination with Peach Blossom, Inverted-Insertion Peach Blossom, Eight Characters punishing and clashing, Body vigorous without reliance.

- **核心要点**：  
  - 列举18种女命贱格配置，涵盖官杀伤官财印比肩刃桃花刑冲等凶险组合  
  - 官杀系列强调混杂无制为大忌：官杀混杂、官杀无制、杀星太重等  
  - 伤官系列强调伤官配置不当：伤官太重、伤官见官、伤官七杀  
  - 桃花刑冲系列强调淫乱不贞：带合桃花、倒插桃花、八字刑冲等

- **详细解说**：  《女命贱格》以条目形式列举18种女命贫贱的凶险格局配置，是女命判断的"负面清单"，与《女命贵格》形成对照。可分为五大系列：**官杀系列**6种——官杀混杂（夫星混乱）、官杀无制（极贱）、杀星太重（被压制）、多官多合（多夫且淫）、无官见合（无夫却淫）、无印见杀（杀无化）。**伤官系列**3种——伤官太重（克夫）、伤官七杀（克夫多灾）、伤官见官（女命大忌）。**财印系列**2种——贪财坏印（坏名声）、财多身弱（为财所累）。**比肩刃系列**3种——比肩犯重（争夫）、阳刃冲刑（血光刑克）、金神带刃（凶上加凶）。**桃花刑冲系列**4种——带合桃花（淫乱）、倒插桃花（晚年失节）、八字刑冲（灾祸连绵）、身旺无依（孤贫）。这18种贱格构成了女命贫贱的警示清单，命师据此可快速识别凶险配置，提前预警。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_276]` `[trigger: 官杀混杂]` `[factor_trigger: nvming AND guansha_hunza AND jian]` `[role: 主干]` 官杀混杂，正官与七杀同见夫星混乱，主贱。 → 《渊海子平·女命贱格》
  - `[ns_yhzp_277]` `[trigger: 官杀无制]` `[factor_trigger: nvming AND guansha_wuzhi AND jijian]` `[role: 条件分支]` 官杀无制，官杀过旺无印化无食制，主极贱。 → 《渊海子平·女命贱格》
  - `[ns_yhzp_278]` `[trigger: 伤官见官]` `[factor_trigger: nvming AND shangguan_jianguan AND kefu_daji]` `[role: 条件分支]` 伤官见官，伤官见官星克夫为女命大忌。 → 《渊海子平·女命贱格》
  - `[ns_yhzp_279]` `[trigger: 贪财坏印]` `[factor_trigger: nvming AND tancai_huaiyin AND huaimingsheng AND caiyin AND caiyin_qing_guansha_zu AND changyin AND greedy_wealth_damages_seal]` `[role: 条件分支]` 贪财坏印，财星克制印绶贪财而坏名声。 → 《渊海子平·女命贱格》
  - `[ns_yhzp_280]` `[trigger: 带合桃花]` `[factor_trigger: nvming AND daihe_taohua AND yinluan AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 带合桃花，合神配桃花主淫乱不贞。 → 《渊海子平·女命贱格》
  - `[ns_yhzp_281]` `[trigger: 多官多合]` `[factor_trigger: nvming AND duoguan_duohe AND duofu_yin AND duo_fu AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 多官多合，官星多且合神多主多夫且淫。 → 《渊海子平·女命贱格》
  - `[ns_yhzp_282]` `[trigger: 阳刃冲刑]` `[factor_trigger: nvming AND yangren_chongxing AND xueguang]` `[role: 条件分支]` 阳刃冲刑，阳刃逢冲逢刑主血光或刑克。 → 《渊海子平·女命贱格》
  - `[ns_yhzp_283]` `[trigger: 身旺无依]` `[factor_trigger: nvming AND shenwang_wuyi AND gupin]` `[role: 条件分支]` 身旺无依，日主过旺无财官食伤依托主孤贫。 → 《渊海子平·女命贱格》
  - `[ns_yhzp_284]` `[trigger: 女命贱格纲领]` `[factor_trigger: nvming AND jiange_gangling AND wudaxilie]` `[role: 总结]` 女命贱格列举18种凶险格局配置，涵盖官杀伤官财印比刃桃花刑冲五大系列。 → 《渊海子平·女命贱格》"""
    normalized_text_zh: str = """"""
    subject: str = "女命贱格"
    factor_refs: list = ['eighteen_women_base_patterns', 'officer_killing_mixed', 'harm_officer_meets_officer', 'greedy_wealth_damages_seal', 'inverted_peach_flower']
    
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
        l1_anchor="yhzp_v1.0.0_女命贱格_001_L1",
    )
    version: str = "1.0.0"
