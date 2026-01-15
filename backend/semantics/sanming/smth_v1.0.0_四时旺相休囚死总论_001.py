"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042751
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
    semantic_id="smth_v1.0.0_四时旺相休囚死总论_001",
    book_id="sanming",
    engine_id="bazi"
)
class 四时旺相休囚死总论(SemanticEntry):
    """
    - **原文（source_text）**：
  盛德乘时曰旺。如春木旺，旺则生火，火乃木之子，子乘父业，故火相。木用水生，生我者父母，今子嗣得时，登高明显赫之地，而生我者当知退矣，故水休。休者，美之...
    """
    
    original_text: str = """- **原文（source_text）**：
  盛德乘时曰旺。如春木旺，旺则生火，火乃木之子，子乘父业，故火相。木用水生，生我者父母，今子嗣得时，登高明显赫之地，而生我者当知退矣，故水休。休者，美之无极，休然无事之义。火能克金，金乃木之鬼，被火克制，不能施设，故金囚。火能生土，土为木之财，财为隐藏之物，草木发生，土散气尘，所以春木克土则死。夏火旺火，生土则土相，木生火则木休，水克火则水囚，火克金则金死。六月土旺，土生金则金相，火生土则火休，木克土则木囚，土克水则水死。秋金旺，金生水则水相，土生金则土休，火克金则火囚，金克木则木死。冬水旺，水生木则木相，金生水则金休，土克水则土囚，水克火则火死。

- **分字分词释义**：
  - **旺 / 相 / 休 / 囚 / 死**：五行在不同季节中的五种状态：旺为当令得时，相为得旺者所生，休为退居幕后的生我者，囚为被制约而难施展，死为气机穷尽之处。
  - **盛德乘时曰旺**：当令之行气得时得势，功用最大。
  - **子乘父业、父知退**：子行得令，父行当退，形象说明「生我者休」的原则。
  - **木之鬼、木之财**：鬼指克我之金，财指我所克之土，用以说明囚与死的状态。

- **规范化释义（primary_lang_explained）**：
  本段用一年四季来总述五行「旺相休囚死」的轮值规律。春令木旺：木为主气，当令为旺；木生火，火是木之子，子得其成故为相；木用水生，水为生我者，子嗣已得时，父母当退，故水休；火克金，金为木之鬼，被火克制而不得用，故金囚；木克土，土为木之财，春木生发时土气被扰，故土死。依此类推，夏火旺、季土旺、秋金旺、冬水旺，每一季中，当令之行气为旺，其所生者为相，生我者为休，被我所制者为死，被对宫制约者为囚，构成一套完整的「旺相休囚死」框架。

- **完整对等诠释（secondary_lang_full）**：
  This section summarises the rotation of the five states—prosperous, active, resting, imprisoned and dead—through the four seasons. In spring, Wood is in command and is said to be prosperous; the Fire it engenders is its child, now taking the stage, so Fire is active. Water, which gives birth to Wood, retreats behind the scenes once the child has risen to prominence, so it is resting. Fire controls Metal, so Metal, as Wood’s “ghost”, is bound and unable to act and is counted as imprisoned. Wood controls Earth, its “wealth”, and in the season of vigorous sprouting the soil is scattered and broken, so Earth is called dead. By the same logic, summer sees Fire prosperous, its products active, its parent resting, its nemesis imprisoned and its resource dead; the long sixth month sees Earth prosperous; autumn grants prosperity to Metal; winter to Water. The point is to treat 旺相休囚死 as a relational framework anchored in seasonal command, not as five fixed labels glued to each element regardless of time.

- **核心要点**：
  - 「旺相休囚死」是以四时节令为轴，对五行强弱状态所做的抽象标注，而非脱离节气的固定标签。
  - 判旺相休囚死必须先定「谁当令」，再据生克关系推导相、休、囚、死，不能只看字面五行多少。
  - 在工程实现中，可以将每一行在四季中的状态映射为数值权重（旺>相>休>囚>死），结合实际气候数据动态调整，而不是死套古表。

- **详细解说**：
  1) 建立「季节—五行状态」基础表：以春木旺、夏火旺、长夏土旺、秋金旺、冬水旺为轴，推导各行的相、休、囚、死；
  2) 推盘时，先判出出生节令所属季节，再据表为每一五行赋予对应状态与权重，并结合干支实占数值进行加权；
  3) 在行运分析中，根据运支所属季节，动态调整各五行的旺衰，使命局中原本偏弱的五行在适当季节获得「相」或「旺」的加持，或反之被压制；
  4) 工程实现时，可将「旺相休囚死」编码为 5 档强度等级，与节气曲线和气象数据融合，形成时间与元素强度的二维特征空间。

- 反例与边界：
  - 不宜在未定节令的情况下，单凭「木多」「火多」就判为旺；必须先看当令之气，再看数量与位置；
  - 不能把「死」理解成绝对无用，很多时候「死地」只是该五行在当前时段不当显用，但仍可在结构上发挥间接作用；
  - 工程上若将传统表格照搬为硬编码，而不考虑地区气候差异与年代变迁，会削弱模型的适用性；
  - 反向误区是完全抛弃旺相休囚表，只靠机器学习自动拟合，导致模型虽能拟合数据，却失去可解释的结构依托。

- 小例（示意）：
  - 某命局木火明显而生于寅卯春月，系统可标记木为旺、火为相、水为休、金为囚、土为死，据此解释其人生阶段中易在春季节令或木火运中获得发展高峰；
  - 另一命局水重而生于午月火旺之时，系统则判断水为囚、火为旺、金为休、木为死、土为相，在输出中提示其「热中有寒、寒中受制」的复杂体感，并为调候提出具体补救建议。

<!-- FACTOR_BEGIN -->
| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|------|
| 状态类 | 旺相休囚死状态 | bazi_state_state_3 | existing | 五行强弱 | 旺>相>休>囚>死 | bazi_semantic | 根据节令动态调整 |
| 时间类 | 当令之气 | bazi_temporal_factor_2 | existing | 节令基准 | 春木夏火秋金冬水 | bazi_semantic | 先定当令再推五行 |
<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_smth_wxqs_001 | generate | wangxing | xiangxing | 旺生相 | 子乘父业 | 传递 | 卷二#旺相休囚死 |
| rel_smth_wxqs_002 | retreat | shengwozhe | xiuxing | 生我者休 | 父知退 | 退让 | 卷二#旺相休囚死 |
| rel_smth_wxqs_003 | constrain | kewozhe | qiuxing | 克我者囚 | 被制不展 | 受制 | 卷二#旺相休囚死 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_smth_wxqs_001 | "盛德乘时曰旺" | wangxiangxiuqiusi | 当令→旺→生克推导 | 五态 | 高 | ✅ | rule_wxqs |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_seasonal_strength | 季节强度 | 旺相休囚死 | 行星庙旺 | 季节梦 | 状态周期 | 节令为纲 |

<!-- L2.5_END -->"""
    normalized_text_zh: str = """"""
    subject: str = "四时旺相休囚死总论"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_四时旺相休囚死总论_001_L1",
    )
    version: str = "1.0.0"
