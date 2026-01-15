"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619819
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
    semantic_id="qtbj_v1.0.0_4__正月甲木的特例与地支成局_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 4正月甲木的特例与地支成局(SemanticEntry):
    """
    - **原文（source_text）**：
  若庚申、戊寅、甲寅、丙寅。一行金水运，发进士。或甲午日庚午时，此人必贵。但要好运相催，不宜制了庚丁。
  或支成金局，多透庚辛，此又不吉，号曰木被金伤...
    """
    
    original_text: str = """- **原文（source_text）**：
  若庚申、戊寅、甲寅、丙寅。一行金水运，发进士。或甲午日庚午时，此人必贵。但要好运相催，不宜制了庚丁。
  或支成金局，多透庚辛，此又不吉，号曰木被金伤，若无丙丁破金，必主残疾。
  或支成火局，泄露太过，定主愚懦，常有啾唧灾病缠身，终有暗疾。
  支成木局，得庚为贵，无庚必凶，若非僧道，男主鳏孤，女主寡独。
  支成水局，戊透为贵，如无戊制，不但贫贱，且死无棺木。故书曰：甲木若无根，全赖申子辰，干得才杀透，平步上青云。

- **分字分词释义**：
  - **发进士**：考中进士 / 科举及第 / 功名显达
  - **好运相催**：好大运推动 / 时运相助 / 命运配合
  - **木被金伤**：木被金克伤 / 金多克木 / 主残疾
  - **破金**：制服金气 / 丙丁火克金 / 救药
  - **泄露太过**：食伤泄气过度 / 火多木虚 / 愚懦病弱
  - **啾唧**：小病小灾 / 琐碎疾病 / 常年不安
  - **暗疾**：隐藏的疾病 / 内伤慢性病 / 难以根治
  - **鳏孤**：无妻或孤独的男子 / 身旺无制 / 孤寡之象
  - **寡独**：寡居或孤独的女子 / 身旺无制 / 孤寡之象
  - **死无棺木**：死后没有棺材 / 极贫极凶 / 水泛木浮之凶
  - **平步上青云**：平稳升上青云 / 官运亨通 / 飞黄腾达

- **规范化释义（primary_lang_explained）**：
  如果八字是：庚申年、戊寅月、甲寅日、丙寅时（身杀两停，丙火制杀），一行金水大运，发进士。或者甲午日庚午时（死木受胎），此人必贵，但要好运催促，不宜过分制住了庚金和丁火。
  如果地支合成金局，天干多透庚辛，这就不吉利了，叫“木被金伤”，如果没有丙丁火破金，必主残疾。
  如果地支合成火局，泄气太过，定主愚蠢懦弱，常有小病灾祸缠身，终有暗疾。
  如果地支合成木局（曲直仁寿格或身旺），有庚金修剪为贵，没有庚金必然凶，若不是僧道，男主鳏寡孤独，女主寡居独身。
  如果地支合成水局，有戊土透出制水为贵，如果没有戊土制水，不但贫贱，而且死无棺木（水泛木浮）。所以古书说：甲木若无根（指生于申子辰月或水局），全赖申子辰印局生身，若天干财（土）杀（金）齐透，可以平步上青云（此时为杀印相生）。

- **完整对等诠释（secondary_lang_full）**：
  If the pillars are Geng-Shen, Wu-Yin, Jia-Yin, Bing-Yin, entering Metal/Water luck leads to the Jinshi degree. Or Jia-Wu Day Geng-Wu Hour, this person must be noble, but needs good luck to assist, and Geng/Ding should not be over-controlled.
  If branches form a Metal frame and many Geng/Xin appear, this is inauspicious, called "Wood Injured by Metal"; without Bing/Ding to break the Metal, disability is certain.
  If branches form a Fire frame, leaking excessively, it denotes stupidity and cowardice, with constant minor illnesses and eventual hidden diseases.
  If branches form a Wood frame, obtaining Geng is noble; without Geng, it is disastrous. If not a monk/taoist, the man will be a widower/loner, the woman a widow/solitary.
  If branches form a Water frame, Wu Earth revealed is noble. Without Wu to control it, it means not only poverty but death without a coffin. Thus the book says: If Jia Wood has no root (or weak root), relying entirely on Shen-Zi-Chen (Water frame), with Wealth and Killing revealed on stems, one rises rapidly to the blue clouds.

- **核心要点**：
  - **支成金局**：木被金伤，必残。解救：丙丁破金。
  - **支成火局**：泄气太过，愚懦病疾。
  - **支成木局**：身极旺，无庚凶（比劫争财/旺极无依），有庚贵（曲直格例外，此处指普通身旺）。
  - **支成水局**：水泛，有戊贵，无戊死。
  - **特殊引用**：甲木无根全赖申子辰，配合财杀可贵（杀印相生）。

- **详细解说**：
  这段讨论了地支三合局对正月甲木的影响。
  - 寅月本气木，若再合木局（寅卯辰/亥卯未），必须用金制（剪裁），否则木旺无依，主孤寡。
  - 若合火局（寅午戌），火泄木气太过，木虚则病，主愚懦。
  - 若合水局（申子辰），水多木漂，必须戊土堤坝。
  - 所谓"甲木无根..."一句其实是引用《滴天髓》或古诀，通常指生于水旺之月或局，此时杀（金）生印（水）生身，若有财（土）制印生杀，则成大格。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_088]` `[trigger: 春甲贵格]` `[factor_trigger: tiangan_jia AND tiangan_geng AND tiangan_wu AND tiangan_bing]` `[role: 主干]` 庚申戊寅甲寅丙寅，一行金水运，发进士。 → 《穷通宝鉴·三春甲木》#3.4
  - `[ns_qttbj_089]` `[trigger: 春甲贵格]` `[factor_trigger: tiangan_jia AND dizhi_wu AND tiangan_geng AND dayun_favorable]` `[role: 主干依赖]` 甲午日庚午时，此人必贵，但要好运相催。 → 《穷通宝鉴·三春甲木》#3.4
  - `[ns_qttbj_090]` `[trigger: 支成金局]` `[factor_trigger: dizhi_metal_frame AND metal_excessive AND NOT element_fire]` `[role: 条件分支]` 支成金局，多透庚辛，号曰木被金伤，无丙丁必主残疾。 → 《穷通宝鉴·三春甲木》#3.4
  - `[ns_qttbj_091]` `[trigger: 支成火局]` `[factor_trigger: dizhi_fire_frame AND tiangan_jia]` `[role: 条件分支]` 支成火局，泄露太过，定主愚懦，终有暗疾。 → 《穷通宝鉴·三春甲木》#3.4
  - `[ns_qttbj_092]` `[trigger: 支成木局]` `[factor_trigger: dizhi_wood_frame AND tiangan_jia AND (tiangan_geng OR NOT tiangan_geng)]` `[role: 条件分支]` 支成木局，得庚为贵，无庚必凶，男主鳏孤，女主寡独。 → 《穷通宝鉴·三春甲木》#3.4
  - `[ns_qttbj_093]` `[trigger: 支成水局]` `[factor_trigger: dizhi_water_frame AND tiangan_jia AND (tiangan_wu OR NOT tiangan_wu)]` `[role: 条件分支]` 支成水局，戊透为贵，无戊制，死无棺木。 → 《穷通宝鉴·三春甲木》#3.4
  - `[ns_qttbj_094]` `[trigger: 甲木无根]` `[factor_trigger: tiangan_jia AND wood_rootless AND dizhi_water_frame AND shishen_wealth AND shishen_killing]` `[role: 总结]` 甲木若无根，全赖申子辰，干得才杀透，平步上青云。 → 《穷通宝鉴·三春甲木》#3.4"""
    normalized_text_zh: str = """"""
    subject: str = "4. 正月甲木的特例与地支成局"
    factor_refs: list = ['wood_injured_by_metal', 'excessive_leakage', 'widower_loner', 'rapid_rise_blue_clouds']
    
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
        l1_anchor="qtbj_v1.0.0_4__正月甲木的特例与地支成局_001_L1",
    )
    version: str = "1.0.0"
