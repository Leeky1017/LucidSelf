"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559067
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
    semantic_id="yhzp_v1.0.0_论日贵_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论日贵(SemanticEntry):
    """
    - **原文（source_text）**：  
  日贵者何？即甲戊兼牛羊之类。止有四日：丁酉、丁亥、癸巳、癸卯耳；最怕刑冲破害。经曰：'崇为宝也，奇为贵也，所以贵人怕三刑六害也。'贵神要聚于日；运...
    """
    
    original_text: str = """- **原文（source_text）**：  
  日贵者何？即甲戊兼牛羊之类。止有四日：丁酉、丁亥、癸巳、癸卯耳；最怕刑冲破害。经曰：'崇为宝也，奇为贵也，所以贵人怕三刑六害也。'贵神要聚于日；运行怕空亡、及运行太岁，加会不要魁罡。主人纯粹、有仁德、有姿色，不傲物。或犯前刑克贫贱；刑冲太甚，贵人生怒，反成其祸。不可不察！日贵有时法类同，须分昼夜贵；日要日贵，夜要夜贵矣！

- **分字分词释义**：
  - **日贵**：日柱坐天乙贵人，特指四日。
  - **甲戊兼牛羊**：天乙贵人口诀——甲戊庚日见丑未为贵人。
  - **丁酉丁亥癸巳癸卯**：四个日贵日——日支即为日干的天乙贵人。
  - **刑冲破害**：地支四凶，破坏贵人的吉象。
  - **崇为宝奇为贵**：尊贵如宝，奇异为贵，故贵人需保护。
  - **贵神聚于日**：贵人星落在日柱最为得力。
  - **空亡**：六甲旬中无对应地支，贵人落空亡则无力。
  - **魁罡**：辰戌为魁罡，与贵人相冲克。
  - **昼夜贵**：贵人分白天贵人（阳贵）和夜晚贵人（阴贵）。

- **规范化释义（primary_lang_explained）**：  
  日贵指丁酉丁亥癸巳癸卯四日，最怕刑冲破害。贵人怕三刑六害。贵神要聚于日，运行怕空亡太岁加会魁罡。日贵之人纯粹有仁德有姿色不傲物。犯刑克贫贱，刑冲太甚贵人生怒反成其祸。日贵须分昼夜贵，日要日贵夜要夜贵。

- **完整对等诠释（secondary_lang_full）**：  
  What is Day Noble? It refers to Jia and Wu combining with Ox and Sheep (based on Noble Person formula). There are only four such days: Ding-You, Ding-Hai, Gui-Si, and Gui-Mao. It most fears Punishments, Clashes, Breakages, and Harms. The classic says: "Honor is treasure, wonder is noble; thus Noble Persons fear Three Punishments and Six Harms." Noble Spirits must gather upon the Day pillar; when fortune running, they fear Void-Extinction and meeting the Tai Sui (Grand Duke). Additionally, they do not want to meet Kuigang. Day Noble owners are pure, benevolent, virtuous, attractive, and not arrogant. If violating previous conditions or encountering clashes, it indicates poverty and baseness; if Punishments and Clashes are excessive, the Noble Person becomes angry, paradoxically turning into disaster. One must examine carefully! Day Noble also follows time-method similarities; one must distinguish Day-time Noble and Night-time Noble; day birth needs Day Noble, night birth needs Night Noble!

- **核心要点**：
  - 日贵指丁酉、丁亥、癸巳、癸卯四日
  - 日贵最怕刑冲破害，贵人怕三刑六害
  - 贵神要聚于日，运行怕空亡、太岁、魁罡
  - 日贵之人纯粹、有仁德、有姿色、不傲物
  - 刑冲太甚贵人生怒反成其祸
  - 须分昼夜贵，日要日贵夜要夜贵

- **详细解说**：  
  本条论述日贵的性质与禁忌。日贵是日柱坐天乙贵人的特殊日子，"止有四日：丁酉、丁亥、癸巳、癸卯"。日贵"最怕刑冲破害"——"崇为宝也，奇为贵也，所以贵人怕三刑六害"——贵人娇贵如宝，不能受损。日贵的运程禁忌是"运行怕空亡、及运行太岁，加会不要魁罡"——空亡使贵人落空，太岁冲动贵人，魁罡（辰戌）与贵人相冲克。日贵之人的性格是"纯粹、有仁德、有姿色，不傲物"——温文儒雅、品行端正。但"刑冲太甚，贵人生怒，反成其祸"——贵人被伤害过度会"发怒"反噬。特别提示"须分昼夜贵；日要日贵，夜要夜贵"——贵人分阴阳，白天生要用日贵（阳贵），夜晚生要用夜贵（阴贵）。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_126]` `[trigger: 日贵定义]` `[factor_trigger: day_noble AND combine_noble_promiscuity]` `[role: 主干]` 日贵者何？即甲戊兼牛羊之类。止有四日：丁酉、丁亥、癸巳、癸卯耳。 → 《渊海子平·论日贵》
  - `[ns_yhzp_127]` `[trigger: 日贵忌刑冲]` `[factor_trigger: day_noble AND punishment AND combine_noble_promiscuity]` `[role: 主干依赖]` 最怕刑冲破害。 → 《渊海子平·论日贵》
  - `[ns_yhzp_128]` `[trigger: 贵人怕刑害]` `[factor_trigger: day_noble AND punishment AND combine_noble_promiscuity]` `[role: 主干依赖]` 崇为宝也，奇为贵也，所以贵人怕三刑六害也。 → 《渊海子平·论日贵》
  - `[ns_yhzp_129]` `[trigger: 日贵运忌]` `[factor_trigger: day_noble AND punishment AND major_cycle AND combine_noble_promiscuity AND kongwang]` `[role: 条件分支]` 运行怕空亡、及运行太岁，加会不要魁罡。 → 《渊海子平·论日贵》
  - `[ns_yhzp_130]` `[trigger: 日贵性格]` `[factor_trigger: day_noble AND combine_noble_promiscuity]` `[role: 条件分支]` 主人纯粹、有仁德、有姿色，不傲物。 → 《渊海子平·论日贵》
  - `[ns_yhzp_131]` `[trigger: 贵人生怒]` `[factor_trigger: day_noble AND punishment AND combine_noble_promiscuity AND guiren_shengnu]` `[role: 例外处理]` 刑冲太甚，贵人生怒，反成其祸。 → 《渊海子平·论日贵》
  - `[ns_yhzp_132]` `[trigger: 昼夜贵]` `[factor_trigger: pattern_day_night_noble_proposal AND combine_noble_promiscuity]` `[role: 总结]` 须分昼夜贵；日要日贵，夜要夜贵矣！ → 《渊海子平·论日贵》"""
    normalized_text_zh: str = """"""
    subject: str = "论日贵"
    factor_refs: list = ['day_noble', 'pattern_day_night_noble_proposal']
    
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
        l1_anchor="yhzp_v1.0.0_论日贵_001_L1",
    )
    version: str = "1.0.0"
