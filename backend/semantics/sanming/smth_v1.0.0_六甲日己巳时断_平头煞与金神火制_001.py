"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.157223
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
    semantic_id="smth_v1.0.0_六甲日己巳时断_平头煞与金神火制_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六甲日己巳时断平头煞与金神火制(SemanticEntry):
    """
    - 原文（source_text）：

  六甲日己巳时断。

  六甲日生时己巳，病中财物实难任；月通火气方为贵，若是身衰亦不禁。甲日己巳时，食旺身衰，甲木巳上病，虽有暗戊为财，丙为食，不通月气，难...
    """
    
    original_text: str = """- 原文（source_text）：

  六甲日己巳时断。

  六甲日生时己巳，病中财物实难任；月通火气方为贵，若是身衰亦不禁。甲日己巳时，食旺身衰，甲木巳上病，虽有暗戊为财，丙为食，不通月气，难任其福。甲己为平头煞，生逢春月，身旺财衰，主骨肉参商，平生作事，弄巧成拙。己巳金神有火制伏，巳酉丑合局，行南方运，名重禄高。柱不见火，残害化气，主凶恶暴亡。

  甲子日己巳时，先贫后富，祖业轻微，妻勤子拗。生寅未巳丑年月，虽贵防疾；申子辰戌，大贵。甲寅日己巳时，时日相刑，忧伤妻子。生火年月，有明断之才，掌兵权之职；戊子年月，承袭祖荫，主富。

  甲辰日己巳时，丰姿敦厚，一生平安，财帛有成。巳酉丑年月，行火金运，贵。甲午日己巳时，金神入火乡，大贵。酉月，行火木运，武职有权。甲申日己巳时，敦厚聪明，善于决断，身孤清贵，不免破刑。

  甲戌日己巳时，财神贵格，名利两全。子戌年月，五品以上贵。甲己中央作土神，时逢辰巳脱埃尘；局中岁运趋炎火，显远功名富贵人。甲日时逢己巳，火临土厚无光。旱苗得雨叶枝强，火局金神旺相。进士有名无实，常人改祖番庄，为人性格不寻常，运至晚年气象。

- 分字分词释义：

  - **平头煞**：甲己相合为土，古书称为平头煞，多主性格执拗、做事容易「一根筋」。
  - **食旺身衰**：食神过旺而日主反弱，象征福气大于承受力，容易「福不胜受」。
  - **金神有火制伏**：巳酉丑合金局，若有火制，则金气可用；无火则金气太盛而成凶。
  - **弄巧成拙**：聪明反被聪明误，强调在决策与操作上的失误风险。

- 规范化释义（primary_lang_explained）：

  本节讲「六甲日，己巳时」在病地与金神之间的张力：

  - 甲木在巳为病地，食神与偏财虽旺，却可能超过日主承载，引来「福重难任」的情况；
  - 甲己合土为平头煞，性格易偏执，一旦判断失误，就出现「弄巧成拙」的结果；
  - 若巳酉丑合局、有火制金，则金神有用，武职、兵权、财名皆可成；无火则金气过刚，主凶恶暴亡等极端情况。

- 完整对等诠释（secondary_lang_full）：

  This section discusses the tension between Sickness position and Golden Spirit in "Six Jia Days with Ji-Si Hour":

  - Jia Wood at Si is in its Sickness position. Although Food God and Indirect Wealth are strong, they may exceed the Day Master's capacity, creating "blessings too heavy to bear."
  - Jia combining with Ji to form Earth creates the "Flat Head Sha"—a tendency toward stubbornness. Once judgment errs, one becomes "too clever by half."
  - When Si-You-Chou combine into Metal and Fire controls it, the Golden Spirit becomes useful for military positions, military authority, and wealth-fame. Without Fire, excessive Metal becomes fierce, indicating violent death or extreme situations.

- 核心要点：

  - 这是一个**承载力与欲望不易平衡**的结构：食神、财星旺，而日主易弱；
  - 需靠火制金、印生身来调和，否则容易在健康与安全上出问题；
  - 性格上的一往无前，若缺乏充分思考，会放大结构中的风险。

- 详细解说：

  1. **福与祸之间的一线之隔**  
     - 当福气大于承载力时，往往表现为机会很多、资源不少，但身体或心理难以消化；  
     - 适当减少贪求、专注于可稳妥承担的方向，是此类命局的重要课题。

  2. **平头煞与性格刻画**  
     - 平头煞并非绝对的凶星，而是提醒当事人容易固执、难以转弯；  
     - 若能在关键节点多听取他人意见，反而可借此坚韧性格完成艰难任务。

  3. **现代调适路径**  
     - 建议在职业与投资方面避免过度冒险，尤其警惕「一把梭哈」式的决策；  370→     - 在健康上，应注意心火与肝胆系统，以及因压力导致的冲动行为。
  371→
  372→- 校勘与字词辨析：
  373→
  374→  - 「平头煞」在各派解释略有差异，本稿依本书文脉，将其视为甲己合土所示之偏执与起伏，不做恐吓性解读。
  375→  - 「凶恶暴亡」「改祖番庄」等表达，在本稿中一律视作对生活轨迹剧烈变化的比喻，非具体事件预言。
  - **English**：
    - Life stage predictions explained as probability indicators; metaphorical descriptions of fortune and misfortune contextualized; technical shensha terms demystified.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_08_021]` `[trigger: 病中财物]` `[factor_trigger: jiamu_bingdi AND caiwu_nanren]` `[role: 主干]` 六甲日生时己巳，病中财物实难任。 → 《三命通会》卷八#六甲日己巳时
  - `[ns_smth_08_022]` `[trigger: 平头煞]` `[factor_trigger: jiaji_pingtousha AND gugu_canshang]` `[role: 主干依赖]` 甲己为平头煞，生逢春月，身旺财衰，主骨肉参商，平生作事，弄巧成拙。 → 《三命通会》卷八#六甲日己巳时
  - `[ns_smth_08_023]` `[trigger: 金神火制]` `[factor_trigger: jisi_jinshen AND huo_zhifu]` `[role: 条件分支]` 己巳金神有火制伏，巳酉丑合局，行南方运，名重禄高。 → 《三命通会》卷八#六甲日己巳时
  - `[ns_smth_08_024]` `[trigger: 火临土厚]` `[factor_trigger: huolin_tuhou AND hanmiao_deyu]` `[role: 总结]` 火临土厚无光。旱苗得雨叶枝强，火局金神旺相。 → 《三命通会》卷八#六甲日己巳时"""
    normalized_text_zh: str = """"""
    subject: str = "六甲日己巳时断：平头煞与金神火制"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'day_master_jia', 'bazi_semantic', 'bazi_state_day_master_3', 'bazi_semantic', 'bazi_relation_factor_66', 'bazi_semantic', 'bazi_relation_metal_fire_1', 'bazi_semantic', 'hour_branch_si', 'bazi_semantic', 'bazi_condition_factor_42', 'bazi_semantic', 'source_ref', 'rel_smth_08_016', 'rizhu_bingdi', 'rel_smth_08_017', 'jinshen_huozhi', 'rel_smth_08_018', 'shiwang_shenshuai', 'evi_smth_08_016', 'rizhu_bingdi', 'rule_bingdi', 'evi_smth_08_017', 'jinshen_huozhi', 'rule_jinshen_huo', 'evi_smth_08_018', 'shiwang_shenshuai', 'rule_shiwang', 'map_smth_08_011', 'map_smth_08_012']
    
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
        l1_anchor="smth_v1.0.0_六甲日己巳时断_平头煞与金神火制_001_L1",
    )
    version: str = "1.0.0"
