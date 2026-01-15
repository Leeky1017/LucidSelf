"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596599
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
    semantic_id="qtbj_v1.0.0_1__火性总论与四时之火_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1火性总论与四时之火(SemanticEntry):
    """
    - **原文（source_text）**：
  炎炎真火，位镇南方，故火无不明之理，辉光不久。全要伏藏，故明无不灭之象。火以木为体。无木、则火不长焰。火以水为用，无水、则火太酷烈。故火多则不实，火烈...
    """
    
    original_text: str = """- **原文（source_text）**：
  炎炎真火，位镇南方，故火无不明之理，辉光不久。全要伏藏，故明无不灭之象。火以木为体。无木、则火不长焰。火以水为用，无水、则火太酷烈。故火多则不实，火烈则伤物。木能藏火，到寅卯方而生火，不利于西，遇申酉而必死。生居离位，木断有为，若居坎宫，谨畏守礼。
  
  金得火和，而能镕铸。水得火和，则成既济。遇土不明，多主蹇塞。逢木旺处，决定为荣。木死火虚，难得永久，纵有功名，必不久长。
  
  春忌见木，恶其焚也。夏忌见土，恶其暗也。秋忌见金，金难克制。冬忌见水，水旺则灭。故春火欲明，不欲炎。炎则不实。秋火欲藏、不欲明。明则太燥，冬火欲生、不欲杀，杀则歇灭。

- **分字分词释义**：
  - **炎炎真火**：熊熊燃烧的真火 / 火性本质 / 光明
  - **位镇南方**：位于坐镇南方 / 火的方位 / 离宫
  - **辉光不久**：辉煌光芒不持久 / 火性虚 / 需伏藏
  - **伏藏**：隐藏潜伏 / 木中藏火 / 持续
  - **火以木为体**：火以木为根本 / 体用论 / 燃料
  - **火以水为用**：火以水为用神 / 体用论 / 调节
  - **酷烈**：残酷猛烈 / 无水之火 / 凶象
  - **离位**：离卦之位 / 南方 / 火旺地
  - **坎宫**：坎卦之宫 / 北方 / 水克火地
  - **既济**：水火配合 / 调和 / 贵格
  - **蹇塞**：困顿阻塞 / 土多 / 凶象

- **规范化释义（primary_lang_explained）**：
  炎炎燃烧的真火，位居南方离宫，所以火没有不光明的道理，但辉光往往不能持久。全靠伏藏（在木中或库中），所以明亮没有不熄灭的现象（需要持续的燃料）。
  火以木为本体（燃料），没有木，火的火焰就不长久。火以水为用神（调节），没有水，火就太酷烈伤人。所以火太多则不实（虚火），火太猛烈则伤害万物。
  木能藏火（木中含火气），到了寅卯东方就生发火，火不利于西方，遇到申酉金地（死地）必然熄灭。火生在南方离位（旺地），若有木生助断定有作为；若生在北方坎宫（克地），则必须谨慎敬畏、遵守礼法（火主礼，受克则守礼）。
  
  金得到火的中和，就能熔铸成器。水得到火的中和，就成就“水火既济”。火遇到土多就会不明亮（晦光），多主困顿蹇塞。遇到木旺的地方，决定是荣耀的。如果木死火虚（无根无源），难得长久，即使有功名，也必定不会长久。
  
  春天的火忌讳见到太多的木，厌恶火势太旺而焚烧（木多火塞/火多木焚）。夏天的火忌讳见到土，厌恶土晦暗火光。秋天的火忌讳见到金，金太旺火难克制（反侮）。冬天的火忌讳见到水，水太旺火会熄灭。
  所以，春火想要明亮，不想要炎烈，炎烈则不实。秋火想要伏藏，不想要太明，太明则太燥。冬火想要生发，不想要肃杀，肃杀则歇灭。

- **完整对等诠释（secondary_lang_full）**：
  The blazing True Fire is positioned in the South; thus, there is no reason for Fire not to be bright, yet its radiance does not last long. It depends entirely on being hidden (stored); thus, there is no brightness that does not eventually extinguish.
  Fire takes Wood as its body (Substance). Without Wood, Fire's flame is not long-lasting. Fire takes Water as its function (Utility). Without Water, Fire is too cruel and intense. Therefore, excessive Fire is insubstantial; intense Fire damages things.
  Wood can store Fire; it generates Fire when reaching the East (Yin/Mao). Fire is unfavorable in the West; meeting Shen/You (Metal lands), it must die. Born in the Li position (South), with Wood, it is certainly capable. If in the Kan Palace (North), one must be cautious and observe propriety.
  
  When Metal is harmonized by Fire, it can be melted and cast. When Water is harmonized by Fire, it achieves "Completion" (Ji Ji). Meeting Earth makes Fire obscure; it often implies obstruction. Meeting prosperous Wood decides glory. If Wood is dead and Fire is hollow, it cannot last forever; even with fame, it won't be long-lasting.
  
  Spring Fire dreads seeing too much Wood, hating incineration (excessive burning). Summer Fire dreads seeing Earth, hating its dimming effect. Autumn Fire dreads seeing Metal, as excessive Metal is hard to control. Winter Fire dreads seeing Water, as prosperous Water extinguishes it.
  Thus, Spring Fire wants to be bright, not scorching; if scorching, it is insubstantial. Autumn Fire wants to be hidden, not bright; if bright, it is too dry. Winter Fire wants to be born, not killed; if killed, it extinguishes.

- **核心要点**：
  - **体用**：以木为体（源头），以水为用（既济）。
  - **十二宫**：生于寅卯，旺于巳午（离），死于申酉。
  - **四时宜忌**："""
    normalized_text_zh: str = """"""
    subject: str = "1. 火性总论与四时之火"
    factor_refs: list = ['fire_hidden', 'obscure_light', 'water_fire_jiji', 'li_position']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__火性总论与四时之火_001_L1",
    )
    version: str = "1.0.0"
