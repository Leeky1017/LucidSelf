"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101292
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
    semantic_id="smth_v1.0.0_丁禄午_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丁禄午(SemanticEntry):
    """
    - **原文（source_text）**：
  丁禄午。见庚午，截路空亡，凶。壬午为德合禄，甲午为进神禄，俱凶。丙午为喜神禄，交羊刃，半吉。戊午，伏羊刃禄，多凶。

- **分字分词释义**：
  ...
    """
    
    original_text: str = """- **原文（source_text）**：
  丁禄午。见庚午，截路空亡，凶。壬午为德合禄，甲午为进神禄，俱凶。丙午为喜神禄，交羊刃，半吉。戊午，伏羊刃禄，多凶。

- **分字分词释义**：
  - **德合禄 / 进神禄**：名义上有德、有进，实则多夹杂凶性，需要结合全局判断。
  - **交羊刃 / 伏羊刃**：禄中含刃，力量大而风险亦大。

- **规范化释义（primary_lang_explained）**：
  丁火禄在午。庚午为截路空亡，庚金克火，又有路断之象，多凶。壬午、甲午虽分别名为「德合禄」「进神禄」，但丁火禄地再见壬水、甲木，易引发水火、木火的过度对抗，原文视为凶象。丙午为「喜神禄」，但夹带羊刃，力量虽强却有折损之虞，只能算半吉。戊午为「伏羊刃禄」，刃性伏藏于禄中，更易失控，多为凶。

- **完整对等诠释（secondary_lang_full）**：
  Ding Fire has its Lu in Wu. Geng-Wu corresponds to the "Cut-Path Void" configuration: strong Metal restrains Fire and the image of the road being chopped off is clear, so it is sharply inauspicious.
  Ren-Wu and Jia-Wu are named the "Virtue-Merge Lu" and "Advancing-Spirit Lu", yet in the territory of Ding-Wu these added Water and Wood easily provoke excessive clashes between Fire and what controls or feeds it, so the tradition still treats them as harmful forms.
  Bing-Wu is the "Joy-Spirit Lu", but it is combined with the blade configuration called Yangren; power and drive are very strong, yet the risk of damage and loss is high, so it is only half auspicious. Wu-Wu is the "Hidden-Yangren Lu": the blade quality is buried inside the Lu position and becomes even harder to control, so it is mostly judged as dangerous.
- **核心要点**：
  - 丁禄午一节强调：禄位若夹带羊刃与强克，容易从「锋芒」变成「伤身」，不能仅凭禄名论吉。
  - 工程上可将丁禄午视作「高风险高收益位」，需同时考察制约与调候条件才下结论。

- **详细解说**：
  1) 确认日主为丁火后，检查命局中午支情况，并识别午上所透天干（庚、壬、甲、丙、戊）；
  2) 将庚午、壬午、甲午、丙午、戊午分别编码为截路空亡禄、德合禄、进神禄、喜神禄（带羊刃）、伏羊刃禄，在系统中同步记录「刃强度」「克战强度」等参数；
  3) 结合全局判断此刃是被印星、官星、食伤合理引导，还是落于无制状态：前者可作为突破性执行力，后者则偏向事故风险；
  4) 在风险预测中，对丁禄午命局适当提高与意气用事、急躁决策、健康透支相关事件的预警，同时在运筹中建议其引入团队制衡与制度护栏。

- 反例与边界：
  - 不宜见「羊刃」就简单判为凶命，应先看日主强弱、是否成「身强刃旺而有制」之格；
  - 不能把「德合禄」「进神禄」全数否定，尽管原文偏凶，在调候得当的结构中，仍可能表现为有担当、有魄力；
  - 工程上若只以「有刃=高危」简单处理，会误杀许多高执行力、高承压的格局，削弱系统对「破局者」的识别能力；
  - 反向误区则是沉迷于「刃格英气」的叙事，忽略现实中的身心代价与人际冲突成本。

- 小例（示意）：
  - 某丁日命，命局丁禄午见丙午喜神禄，且有正官、印星贴身，系统可解读为「锋芒内收、有序发力」的格局，适合在组织中承担关键突击任务，但需注意劳逸；
  - 另一丁日命，庚午截路空亡又逢七煞无制，行火金交战之运，系统则给出「高风险」标签，提示在高压行业中尤需警惕突发事件与硬碰硬冲突。"""
    normalized_text_zh: str = """"""
    subject: str = "丁禄午"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_ding_wu', 'bazi_semantic', 'bazi_state_yangren_marker', 'bazi_semantic', 'bazi_state_strength_8', 'bazi_semantic', 'bazi_condition_factor_29', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_丁禄午_001_L1",
    )
    version: str = "1.0.0"
