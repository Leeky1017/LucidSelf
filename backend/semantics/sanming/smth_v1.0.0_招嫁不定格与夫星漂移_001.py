"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436575
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
    semantic_id="smth_v1.0.0_招嫁不定格与夫星漂移_001",
    book_id="sanming",
    engine_id="bazi"
)
class 招嫁不定格与夫星漂移(SemanticEntry):
    """
    - 原文（source_text）：

  招嫁不定。

  夫招嫁不定者何也？乃命令中有夫星，透干与己相合，己身从伏，其夫星却无气。时引夫星，或煞星却乘旺地求克己身，又从伏便夫，故谓之招嫁不定。若夫...
    """
    
    original_text: str = """- 原文（source_text）：

  招嫁不定。

  夫招嫁不定者何也？乃命令中有夫星，透干与己相合，己身从伏，其夫星却无气。时引夫星，或煞星却乘旺地求克己身，又从伏便夫，故谓之招嫁不定。若夫星不旺，或受克制，必嫁夫迟，或嫁夫不明，或夫不济事，或有外情。如一命：癸酉、甲子、己未、乙亥。己用甲为夫，生于十一月，失时不旺。时逢亥字，乃甲木长生，是夫旺也，却不合，又被乙木制己未，未为乙木库地。甲生子月，夫坐败地不显，时上乙亥，亥中又有生长之甲，欲甲又招乙也，此招嫁不定，余仿此推。

- 分字分词释义：

  - **招嫁不定**：招夫、婚嫁之事多有反复、延宕或变动。
  - **命令中有夫星，透干与己相合**：日柱与年、月中即有夫星相合，象征婚姻因命主自身条件而被提前关注。
  - **夫星却无气**：夫星位置无力或受制，难以成就稳定婚姻。
  - **时引夫星或煞星乘旺克身**：在时柱再引夫星或煞星，强势一方压过日主，使关系难以均衡。

- **规范化释义（primary_lang_explained）**：

  “招嫁不定格”描写的是一种**婚姻议题被频繁触发，却难以顺利定下**的结构：

  - 夫星早在命局中出现，与日主相合，却多落败地或失时；
  - 时柱再引夫星或煞星，形成“想嫁 / 招夫”的动力，却难以遇到真正匹配、稳定的对象；
  - 于是表现为成婚较迟、婚约反复、或伴侣不甚可靠等情形。

- **完整对等诠释（secondary_lang_full）**：

  This pattern shows that the question of marriage is raised again and again, yet it is difficult to settle into a clear and stable bond. The spouse star appears early and combines with the Day Master, so talk of proposals, engagements or marriage may begin sooner than average, but because that star sits in a weak or unfavourable place, the actual partner is often not yet reliable, mature or truly suitable.

  From a contemporary lens, this points more to a mismatch of timing and readiness than to a fixed "misfortune in love". Later, when the hour branch brings in a stronger spouse star or Killing star, external pressure to marry may intensify, sometimes leading to hurried decisions or repeated changes of plan. The invitation is to slow down enough to feel one's own boundaries and desires, to recognise the difference between wanting companionship and being pushed by others' expectations, and to choose relationships at a pace one can genuinely sustain.

- 核心要点：

  - 夫星早显却无气，是招嫁不定的关键结构之一。
  - 时柱再引夫星或煞星乘旺，表示婚姻议题反复被激活。
  - 现实中多对应为婚恋过程曲折、节奏失衡，而非单一的“多婚”或“克夫”。

- 详细解说：

  1. **早显夫星与心理节奏**  
     - 夫星早显者，往往较早被婚恋与亲密关系议题所牵动；  
     - 然而若夫星失位无气，则实际对象多难成熟，容易出现“有意无缘”。

  2. **时柱激活与外部条件**  
     - 时柱的夫星或煞星乘旺，好比后期环境再次强推婚姻议题；  
     - 若结构失衡，则可能带来仓促决定、外力干预或隐性压力。

  3. **现代应对方向**  
     - 命局示“招嫁不定”时，与其惧怕，不如正视自己在情感中的期待与底线；  
     - 通过放慢节奏、增加了解与自我整合，反而能在多次波折后找到更适合的关系形式。

- 校勘与字词辨析：

  - “夫不济事”“有外情”等语，本稿不作道德判断，仅视为婚姻稳定性不足的象征说法。
  - 例命中“欲甲又招乙也”一语，本稿理解为象征多重夫星、对象选择反复，不做字面事件解读。
  - **English**：
    - Choice-wavering; not literal event interpretation.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_069]` `[trigger: 招嫁不定定义]` `[factor_trigger: zhaojia_buding_ge]` `[role: 主干]` 招嫁不定。 → 《三命通会》卷七#招嫁不定
  - `[ns_smth_07_070]` `[trigger: 夫星早显无气]` `[factor_trigger: fuxing_tougan AND fuxing_wuqi]` `[role: 主干依赖]` 乃命令中有夫星，透干与己相合，己身从伏，其夫星却无气。 → 《三命通会》卷七#招嫁不定
  - `[ns_smth_07_071]` `[trigger: 嫁迟或夫不济]` `[factor_trigger: jia_fu_chi OR fu_buji_shi]` `[role: 条件分支]` 若夫星不旺，或受克制，必嫁夫迟，或嫁夫不明，或夫不济事，或有外情。 → 《三命通会》卷七#招嫁不定
  - `[ns_smth_07_072]` `[trigger: 招嫁不定]` `[factor_trigger: yu_jia_you_zhao]` `[role: 总结]` 欲甲又招乙也，此招嫁不定。 → 《三命通会》卷七#招嫁不定"""
    normalized_text_zh: str = """"""
    subject: str = "招嫁不定格与夫星漂移"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_104', 'bazi_semantic', 'bazi_structure_factor_105', 'bazi_semantic', 'bazi_state_strength_11', 'bazi_semantic', 'bazi_factor_15', 'bazi_semantic', 'source_ref', 'rel_smth_07_049', 'hunyin_jihuo', 'rel_smth_07_050', 'waibu_cuihun', 'rel_smth_07_051', 'hunlian_xietiao', 'evi_smth_07_049', 'hunyin_jihuo', 'rule_zhaojiia', 'evi_smth_07_050', 'waibu_cuihun', 'rule_shiyiin', 'evi_smth_07_051', 'hunlian_xietiao', 'rule_jiachi', 'map_smth_07_033', 'map_smth_07_034']
    
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
        l1_anchor="smth_v1.0.0_招嫁不定格与夫星漂移_001_L1",
    )
    version: str = "1.0.0"
