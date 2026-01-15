"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042230
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
    semantic_id="smth_v1.0.0_河出图_洛出书与汉儒之失_001",
    book_id="sanming",
    engine_id="bazi"
)
class 河出图洛出书与汉儒之失(SemanticEntry):
    """
    - **原文（source_text）**：
  余按：易言「河出图，洛出书，圣人则之」，未尝明言图书之数如汉儒所指。观伏羲定方画卦，大禹第畴首五行，则术家之说是也。况洛书之数，术家以为大挠定之，与吾...
    """
    
    original_text: str = """- **原文（source_text）**：
  余按：易言「河出图，洛出书，圣人则之」，未尝明言图书之数如汉儒所指。观伏羲定方画卦，大禹第畴首五行，则术家之说是也。况洛书之数，术家以为大挠定之，与吾儒之说迥别。宋程、朱以一六居北为河图，戴九履一为洛书，亦因汉儒之旧云尔。浚川王子以伏羲作易，造端于阴阳二画而已，故曰：易有太极，是生两仪，两仪生四象，四象生八卦，先后自然之序，有非人力强为排比。今乃因河图之数以作易，是不从太极以为易，岂不于仲尼「易有太极」之论戾乎？

- **分字分词释义**：
  - **圣人则之**：圣人观河图、洛书而取其意象，并非逐字逐数地模仿。
  - **汉儒所指**：指东汉以来拘泥「图书点数」的解说传统。
  - **造端于阴阳二画**：以阴爻、阳爻二画为本，而非以定死的数字为本。
  - **不从太极以为易**：若只从河图数起卦，便违背「易有太极」之旨，舍本逐末。

- **规范化释义（primary_lang_explained）**：
  作者在这里批评后世汉儒过于执着于河图、洛书的具体数字排列，以为画卦、作易都要直接从数字推起。依其看来，《易经》真正的起点在于太极、阴阳二画，而河图、洛书只是圣人借以「设教」的象征符号。若倒过来把数字当根本，反而违背了「易有太极」的原旨，把一整套活的理气系统变成僵硬的数表。

- **完整对等诠释（secondary_lang_full）**：
  The author critiques later Han Confucian scholars for being overly attached to the specific numerical arrangements of River and Luo Diagrams, mistakenly believing that drawing trigrams and creating the Yi must start directly from numbers. In his view, the true origin of the Yi lies in Taiji and the two yin-yang lines, while River and Luo Diagrams are merely symbolic tools used by sages for teaching. Reversing this by treating numbers as fundamental contradicts the principle that "Yi has Taiji as origin," transforming a living system of principle and qi into rigid numerical tables. This critique emphasizes that destiny analysis should not degenerate into mechanical number-crunching that loses sight of the underlying principles and Taiji, which would prevent holistic understanding of the entire framework.

- **详细解说**：
  1) 解读任何一条「数理格局」前，先在解释链中显式标注：本条依据的是「易理（太极—阴阳）」还是「河洛数」还是「经验统计」，避免混为一谈；
  2) 在工程中，为每条规则增加「来源标签」（经典原文 / 河洛数理 / 经验归纳），推理引擎优先按理气大纲过滤，再用数理与经验做微调；
  3) 推盘时，若出现「数理吉而理气不顺」的矛盾，系统应提示用户：此处数理为辅、理气为主，不可只看数字评分；
  4) 在学习模式下，可引导用户先阅读「太极—阴阳—四象—八卦」的总纲，再逐步接触河洛数，形成由理入数的路径。

- 反例与边界：
  - 将汉儒后世的「点数解河图」视作唯一正统，不允许任何与经典原文不完全相合的解释；
  - 在系统中，以纯数字（如简单打分）替代整个理气结构，使得「命理」退化成一串算术题；
  - 只凭少量样本中某个数字组合的高频出现，就轻率宣称「此数组合必吉/必凶」，忽视时代与样本偏差；
  - 反向误区是，以「不可拘泥数字」为由，完全否认河洛数理的价值，使得模型失去一整套可计算的结构工具。

- 小例（示意）：
  - 系统在给出解释时，将「理气逻辑」与「数理评分」分两层展示：先说明阴阳生克、格局大势，再给出数值化的强弱指标，并附注「数字仅为近似度量」；
  - 某案例中，传统口诀以一组河洛数称极吉，但实际命局长期困顿，系统可通过理气层识别：虽数吉而行运与人事皆不合，从而给出「戒迷信数字」的提示。

- **完整对等诠释（secondary_lang_full）**：
  The author criticizes later Han Confucian scholars for being overly attached to the specific numerical arrangements of River and Luo Diagrams, mistakenly believing that trigram formation and Yi divination must derive directly from numbers. In his view, the true origin of Yi lies in Taiji and the two lines of yin-yang, while River and Luo Diagrams serve merely as symbolic teaching tools employed by sages. Reversing this relationship—treating numbers as fundamental—violates the original principle "Yi has Taiji as origin" and transforms a living system of principle and qi into rigid numerical tables. This critique emphasizes that destiny analysis should not degenerate into mechanical number-crunching that loses sight of the underlying principles and Taiji, which would prevent holistic understanding of the entire framework.

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|----------|-----------|--------|
| 圣人则之 | Sages Follow | 圣人取河洛之象意而非拘泥数字 | Sages take symbolic meaning not literal numbers | - | new_candidate |
| 易有太极 | Yi Has Taiji | 易理以太极为源头非数字为本 | Yi principle originates from Taiji not numbers | - | new_candidate |
| 造端二画 | Origin Two Lines | 易道起于阴阳二爻非河洛数 | Yi begins with yin-yang lines not diagrams | - | new_candidate |
| 理气vs数理 | Principle-Qi vs Numerology | 命理应以理气为主数理为辅 | Destiny should prioritize principle-qi over numbers | - | new_candidate |


<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|---|---|---|---|---|---|---|---|---|
| 概念类 | 太极本源论 | taiji_as_origin | existing | 哲学基础 | 易有太极为本 | bazi_semantic | 易理以太极为根源非数字 |
| 概念类 | 理气主导原则 | principle_qi_primacy | existing | 判断原则 | 理气为主数理为辅 | bazi_semantic | 命理分析的优先级原则 |
| 方法类 | 数理辅助定位 | numerology_as_tool | existing | 工具层 | 数为形迹理为主干 | bazi_semantic | 数理作为辅助工具而非根本 |
| 概念类 | 象征vs机械 | symbolic_vs_mechanical | existing | 解释方式 | 活理气vs死数表 | bazi_semantic | 区分象征系统与机械计算 |
<!-- FACTOR_END -->

#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|------------|
| rel_smth_02_007 | principle_hierarchy | taiji_as_origin | numerology_as_tool | 太极为本数为末 | 论命理时以太极为本数理为用 | 主从关系 | 《三命通会·卷二》#汉儒之失 |
| rel_smth_02_008 | methodology | principle_qi_primacy | symbolic_vs_mechanical | 理气主导避机械 | 理气分析优先于机械数理时 | 方法论 | 《三命通会·卷二》#汉儒之失 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|------------|
| evi_smth_02_005 | "易有太极，是生两仪" | taiji_as_origin | 太极→阴阳→数 | 本末次序 | 高 | ✅ | rule_taiji_primacy |
| evi_smth_02_006 | "造端于阴阳二画而已" | principle_qi_primacy | 阴阳为本非数为本 | 理气优先 | 高 | ✅ | rule_yinyang_origin |

**跨体系概念映射层**：

| 映射ID | 本体系概念 | 目标体系 | 目标概念 | 映射类型 | 映射强度 | 备注 |
|-------|----------|---------|---------|---------|---------|------|
| map_smth_02_005 | taiji_as_origin | 易学 | 太极本体论 | 同源映射 | 强 | 共享太极为本的哲学基础 |
| map_smth_02_006 | principle_qi_primacy | 理学 | 理先气后 | 类比映射 | 中 | 理气关系的优先级原则 |

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_02_hanru_001]` `[trigger: 河洛圣则] [factor_trigger: 河洛圣则]` `[role: 主干]` 易言「河出图，洛出书，圣人则之」，未尝明言图书之数。 → `《三命通会·卷二》#河出图洛出书与汉儒之失`
  - `[ns_smth_02_hanru_002]` `[trigger: 太极为本] [factor_trigger: 太极为本]` `[role: 主干]` 易有太极，是生两仪，两仪生四象，四象生八卦，先后自然之序。 → `《三命通会·卷二》#河出图洛出书与汉儒之失`
  - `[ns_smth_02_hanru_003]` `[trigger: 造端二画] [factor_trigger: 造端二画]` `[role: 主干]` 伏羲作易，造端于阴阳二画而已。 → `《三命通会·卷二》#河出图洛出书与汉儒之失`
  - `[ns_smth_02_hanru_004]` `[trigger: 理气为主] [factor_trigger: 理气为主]` `[role: 主干]` 命理当以理气为主，数理为辅，不可拘泥形迹。 → `《三命通会·卷二》#河出图洛出书与汉儒之失`
  - `[ns_smth_02_hanru_005]` `[trigger: 汉儒之失] [factor_trigger: 汉儒之失]` `[role: 主干]` 汉儒拘泥点数，失圣人取象之本意。 → `《三命通会·卷二》#河出图洛出书与汉儒之失`

---

### 4. 洪范九畴与五行次第

- **原文（source_text）**：
  易系「天一地二」之辞，为作易后立揲而言，非作易之始事，而何以取图为哉？又疑圣人则图、书皆言画卦，非禹则之明畴也。观《洪范》九畴，乃治天下之大经大法，如《周官》九式、九两之义，非数也。箕子首言天锡，不过水土平而五行之政可修，五行之政修，而治天下之庶政可举。故于地平天成之时，天乃锡禹大法曰「天者」，是天予以治天下、叙彝伦，此九者不可缺一云尔。观畴次第：首五行，次五事，次八政，本天而推之于人；次五纪，次三德，次稽疑，以人而合乎天；次庶征，次五福、六极，则人感天应，而皇极乃其主也，故居中焉。

- **分字分词释义**：
  - **洪范九畴**：箕子所陈治道九纲：五行、五事、八政、五纪、三德、稽疑、庶征、五福、六极。
  - **天锡大法**：上天赐予大禹以治天下之法度，不仅是数表，而是伦理与政教的总纲。
  - **五行之政可修**：先把与水、火、木、金、土相关的一切秩序治理好，方能推及人事诸政。
  - **皇极居中**：九畴之主宰，为「中道」与「天子之位」，统摄上下诸项。

- **规范化释义（primary_lang_explained）**：
  此处转入《洪范》九畴，强调五行并非单纯「生克之数」，而是治国安民的纲常之首：先论五行之政，再推及人事、政务、德性与赏罚，最后才归结为皇极中道。用意在说明：河图、洛书之数若不落实到「五行治理」与人伦秩序，只是空谈数字；而《洪范》所立的次第，则把五行放在一整套天人秩序的第一环。
 
- **核心要点**：
  - 《洪范》里的五行观，是「理—政—人事」一体的结构，并非孤立的五行表；命理取用洪范五行，意在贯通天道、人道与命数。
  - 将五行放在九畴之首，意味着任何命局分析若只停留在吉凶祸福，而不顾及德行与人事抉择，都是偏废了经典原意。
  - 河洛数理与洪范五行结合，构成「数—理—政—命」的完整框架：数为形迹，理为主干，人事与命运只是其显现。

- **详细解说**：
  1) 在解读命盘时，将《洪范》视作「价值与行为」的大纲：先判断五行是否中和，再讨论人事抉择与德行倾向；
  2) 在系统中，为每条命理解读增加「德行与行为建议」栏，将五行偏胜偏衰与现实中的行为习惯、风险倾向挂钩，而不只给出「吉/凶」标签；
  3) 结合河图洛书的数理结构，将五行偏向映射到具体生活领域，如财务、关系、健康、决策风格等，形成「数—理—政—命」的多层解释；
  4) 对于涉及领导力或公共影响的命局，系统应特别强调「五行之政」的一面，引导用户从公共责任角度思考，而非只看个人得失。

- 反例与边界：
  - 将《洪范》只当作「五行对应五脏、五色」的小表来背，完全忽略其中九畴治道的整体结构；
  - 把命理解读简化成「某行太旺，必发大财」「某行太弱，必多灾祸」之类的单一因果，脱离道德与行为层面的修正可能；
  - 在工程中，只使用五行作为标签特征，而不让它参与「行为建议」生成，导致系统输出与经典精神脱节；
  - 反向误区是，用大道理压倒所有现实判断，拒绝对具体格局与运势做细致区分。

- 小例（示意）：
  - 某命局火土偏盛、金水偏弱，系统除了指出健康与情绪的风险外，还会结合《洪范》提示：在用权与分配资源时须防「偏热偏急」，宜多听冷静之言；
  - 在企业管理场景中，引入《洪范》九畴，借五行结构帮助团队审视「战略（五行）、执行（五事）、制度（八政）」是否失衡，再用个人命局来解释个体在其中的角色与盲点。

- **完整对等诠释（secondary_lang_full）**：
  This passage shifts to the Hongfan Nine Categories, emphasizing that Five Elements are not merely "numerical generation-control relationships" but the foremost principle of governance and moral order: first discussing Five Element governance, then extending to human affairs, administrative matters, virtues and penalties, ultimately culminating in the Imperial Ultimate (Huangji) as the central Way. The intention is to show that if River and Luo Diagram numbers do not ground themselves in "Five Element governance" and human ethical order, they remain empty numerology; whereas the Hongfan sequence places Five Elements as the first link in a complete heaven-human order system. This integrates principle-politics-destiny as one organic framework where numbers are traces, principles are the trunk, and human affairs with destiny are mere manifestations."""
    normalized_text_zh: str = """"""
    subject: str = "河出图、洛出书与汉儒之失"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'hongfan_nine_system', 'bazi_semantic', 'five_element_governance', 'bazi_semantic', 'imperial_ultimate_center', 'bazi_semantic', 'principle_politics_destiny_unity', 'bazi_semantic', 'source_ref', 'rel_smth_02_009', 'hongfan_nine_system', 'rel_smth_02_010', 'five_element_governance', 'rel_smth_02_011', 'principle_politics_destiny_unity', 'evi_smth_02_007', 'five_element_governance', 'rule_wuxing_governance', 'evi_smth_02_008', 'imperial_ultimate_center', 'rule_huangji_center', 'map_smth_02_007', 'map_smth_02_008']
    
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
        l1_anchor="smth_v1.0.0_河出图_洛出书与汉儒之失_001_L1",
    )
    version: str = "1.0.0"
