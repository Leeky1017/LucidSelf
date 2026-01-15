"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.436585
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
    semantic_id="smth_v1.0.0_小儿命格与易养难养之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 小儿命格与易养难养之象(SemanticEntry):
    """
    - 原文（source_text）：

  夫观小儿之命，如种花木之法。善培养者，则根苗茂盛，花果兴隆；不善培养者，反是。何以言之？凡人种花木，必以土栽培其根，根实则苗盛；必以水浇灌其体，体壮则花茂；...
    """
    
    original_text: str = """- 原文（source_text）：

  夫观小儿之命，如种花木之法。善培养者，则根苗茂盛，花果兴隆；不善培养者，反是。何以言之？凡人种花木，必以土栽培其根，根实则苗盛；必以水浇灌其体，体壮则花茂；赖阳火温照其花，花实则果成；假金刃修伐其枝，枝清则本固。设若土虚根浅，水少苗枯，日暴花焦，风摧果落，是皆失中和培养之气，其花木安有不枯之理乎？人之八字，以年为根，月为苗，日为花，时为果，其理皆然。故推小儿之命，要日干有气，月令生扶，年上栽根，印绶无伤，财官有制，七煞得化，伤官遇合，气禀中和，不值刑冲破害，此则易养长寿之命。如煞重身轻，财多身弱，伤官叠遇，食神重逢，日干或旺甚无依，或太柔少印，气失中和，柱中有刑冲破害，此则难养促寿之命。二者类如栽培之法。又曰：小儿之命，当论时辰为正，先看关煞，次看格局。日主强财官旺，有关无煞；日主弱财官少，常病易养；日干弱财官多，有煞有关，难养。夫关者何也？即偏官为关，偏财为煞。专以日干为主，取生成之数断之。关者，譬如今之关隘，乃险阻之地。小儿命犯此关，则为不利。柱中日干强健，制伏纯粹，印绶无伤，如有明文之类，通达顺遂，易养长寿，反之则否。

- 分字分词释义：

  - **年为根，月为苗，日为花，时为果**：以年柱喻根、月柱喻苗、日柱喻花、时柱喻果，说明一生发展各阶段的承接关系。
  - **中和培养之气**：五行得中和、有生有制，如花木得土水火金之相济，象征小儿易养。
  - **煞重身轻 / 财多身弱**：偏官、偏财等外来压力过重，而日主太弱，难以承受，易成难养格。
  - **关煞**：偏官为关、偏财为煞，比喻人生道路上的关隘与险阻，小儿犯关重则多病难养。

- **规范化释义（primary_lang_explained）**：

  本节以“种花木之法”来比喻小儿命局的培养：

  - 年为根、月为苗、日为花、时为果，四者相生相承，则如花木得其土壤、水分、阳光与修剪；
  - 若日主有根有气、关煞有制、印绶护身、财官有度，则小儿多半易养，虽有小病小灾，终能渐趋稳健；
  - 若煞重身轻、刑冲破败成群，又缺乏适当照护与资源，则体质与环境更容易失衡，需要格外用心。

- **完整对等诠释（secondary_lang_full）**：

  This section likens a child's chart to the cultivation of a plant. Year is the root, month the sprout, day the flower and hour the fruit: when all four stages are properly supported, the plant grows with relative ease; when the soil is thin, the water scarce, the sun too harsh or the wind too strong, it struggles. In the same way, a chart with a rooted, qi‑bearing Day Master, moderated killing stars and well‑placed Resource and Officer suggests that, with ordinary care, the child can grow through illnesses and setbacks into a more stable life.

  When killing stars cluster around a weak Day Master and clashes cut repeatedly across the pillars, the text calls this "hard to raise". Read in a modern context, this is not a verdict of short life, but a signal that body, environment and caregiving style all need more attention. It invites parents and caregivers to treat medical support, nutrition, emotional holding and a calm home climate as structural protections for a sensitive constitution, rather than to surrender to fatalism.

- 核心要点：

  - 小儿命局最重“中和”与“承接”，即根苗花果之间要有顺畅的生长链条；
  - 关煞偏重而日主太弱，是古人判断“难养”的主要结构依据；
  - 现代阅读时，更适合将其视为对体质、环境与养育方式的结构提示，而非简单的“寿不寿”判断。

- 详细解说：

  1. **花木比喻与成长条件**  
     - 土喻家庭与环境地基，水喻滋养与照顾，火喻温暖与鼓励，金喻规训与修剪；  
     - 任何一环严重失衡，都会影响孩子在身体与心理上的发展节奏。

  2. **“易养 / 难养”的结构含义**  
     - 易养，并不意味着一生无病，而是整体结构有弹性，有余力应对波折；  
     - 难养，指的是对环境与照护条件依赖度更高，需要更多专业与情感支持。

  3. **现代视角下的转译**  
     - 命局中的关煞与刑冲，可理解为对免疫力、神经系统与环境适应度的敏感提示；  
     - 多病多折腾的童年，并不必然预示短寿，关键在于能否得到持续、适切的照顾与治疗。

- 校勘与字词辨析：

  - 原文后段另引“日阴阳贵贱”等占法，本稿不全文转录，只在详细解说与后续章节中择要提及，以免喧宾夺主。
  - “易养 / 难养 / 促寿”在本稿统一理解为健康与成长条件之优劣，并不作简单寿命预测。
  - **English**：
    - Assesses quality; not simple longevity prediction.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_07_073]` `[trigger: 小儿总纲]` `[factor_trigger: xiaoer_zhonghua_fa]` `[role: 主干]` 夫观小儿之命，如种花木之法。 → 《三命通会》卷七#小儿命
  - `[ns_smth_07_074]` `[trigger: 根苗花果]` `[factor_trigger: nian_wei_gen AND yue_wei_miao]` `[role: 主干依赖]` 人之八字，以年为根，月为苗，日为花，时为果，其理皆然。 → 《三命通会》卷七#小儿命
  - `[ns_smth_07_075]` `[trigger: 易养条件]` `[factor_trigger: rigan_youqi AND guansha_youzhi]` `[role: 条件分支]` 日干有气，月令生扶，年上栽根，印绶无伤，财官有制...此则易养长寿之命。 → 《三命通会》卷七#小儿命
  - `[ns_smth_07_076]` `[trigger: 难养条件]` `[factor_trigger: sha_zhong_shen_qing]` `[role: 总结]` 如煞重身轻，财多身弱，伤官叠遇，食神重逢...此则难养促寿之命。 → 《三命通会》卷七#小儿命"""
    normalized_text_zh: str = """"""
    subject: str = "小儿命格与易养难养之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_106', 'bazi_semantic', 'bazi_state_factor_357', 'bazi_semantic', 'bazi_state_factor_358', 'bazi_semantic', 'bazi_factor_16', 'bazi_semantic', 'source_ref', 'rel_smth_07_052', 'guansha_miji', 'rel_smth_07_053', 'huchi_ziyuan', 'rel_smth_07_054', 'shengzhang_zheteng', 'evi_smth_07_052', 'guansha_miji', 'rule_xiaoer', 'evi_smth_07_053', 'huchi_ziyuan', 'rule_yiyang', 'evi_smth_07_054', 'shengzhang_zheteng', 'rule_zhonghe', 'map_smth_07_035', 'map_smth_07_036']
    
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
        l1_anchor="smth_v1.0.0_小儿命格与易养难养之象_001_L1",
    )
    version: str = "1.0.0"
