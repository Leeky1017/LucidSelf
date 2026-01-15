"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997724
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
    semantic_id="dts_v1.0.0_诸症杂论_择要_001",
    book_id="dts",
    engine_id="bazi"
)
class 诸症杂论择要(SemanticEntry):
    """
    - **原文（source_text）**：
  诸症杂论（择要）。

- 规范化释义（primary_lang_explained）：
  本节对前面“和/乱、入脏/游经”等原则作综合补充，从“血”...
    """
    
    original_text: str = """- **原文（source_text）**：
  诸症杂论（择要）。

- 规范化释义（primary_lang_explained）：
  本节对前面“和/乱、入脏/游经”等原则作综合补充，从“血”“气”“寒热燥湿”等角度列举多种杂症的五行归类，并提示有时六亲之灾会以病症代偿应现。

- **核心要点**：
  - 将多种临床症状回收至“五行配脏腑+寒热燥湿”框架；
  - 强调“木不受水”“土不受火”等错配所致之病；
  - 提醒有些六亲之灾，会通过疾病方式在本人身上应验。

- 详细解说：
  在前三条从“和/乱”“入五脏”“游六经”分别建模之后，本条以杂论形式补充细节：例如金水伤官在寒时主冷嗽，在热时主痰火；火土印绶在热时主风痰，在燥时主皮痒等。通过这些例子，将抽象的五行失衡具体映射到血、气、痰、毒、脏腑功能失调等层面，并指出某些本应落在六亲身上的灾，可能转而以病灾由本人承受。

- 校勘与字词辨析：
  - “杂论（择要）”：表示仅择要录出代表性症候，并非穷尽所有组合。

- 原注（原文注解）：
  　　木不受水者血病；土不受火者气伤。金水伤官：寒则冷嗽、热则痰火；火土印绶：热则风痰、燥则皮痒；痰多木火，毒郁火金；金水枯伤肾虚，水土相胜脾胃泄。应六亲而不验者，或以病当之（如妻土被伤，本应克妻，实以脾病当之）。

- **规范化释义（primary_lang_explained）**：
  疾病从五行模块化审视：脏腑、经部、冷热燥湿，皆可从喜忌入手校正。

- 分字分词释义：
  - 和：五行各得其所、调衡有序。
  - 乱：来往不顺、上下不通、反逆冲伐。
  - 忌神入脏：喜忌错位深入五脏而成大病。
  - 客神游经：客气行于经部，多为小灾易治。
  - 冷热燥湿：体质与病性之四象。

- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 疾病 | Disease (Ji-Bing) | 病痛疾苦 | Illness and suffering | jibing_general_disease | new_candidate |
| 五行和 | Five Elements Harmonious | 五行调和 | Elements balanced | wuxing_balance | existing |
| 血气乱 | Blood and Qi Disordered | 气血紊乱 | Chaotic Qi and Blood | xueqiluan | new_candidate |
| 忌神入五脏 | Malicious God Entering Viscera | 病深入脏 | Deep illness in organs | jibing_harmful_qi_organ_layer | new_candidate |
| 客神游六经 | Guest God Wandering Meridians | 病在经络 | Superficial illness | jibing_guest_qi_layer | new_candidate |
| 一世无灾 | Lifelong No Disaster | 一生平安 | Safe whole life | outcome_lifelong_no_disaster | new_candidate |
<!-- L2_BEGIN -->

- 语义提取（L2）：
  - **主题**：建立基于五行“和/乱”与“脏/腑”对应关系的疾病诊断模型
  - **自然属性**：
    - 象征：人身为小宇宙，五行即五脏六腑之气；和则健，乱则病；
    - 特性：
      - 忌神入五脏（阴/里）：病深而凶；
      - 客神游六经（阳/表）：病浅而小；
      - 寒暖燥湿失衡（如金水寒、火土燥）：引发特定体质病变；
    - 元素：五行对应脏腑（木肝、火心、土脾、金肺、水肾等）。
  - **功能象义**：
    - 为规则侧提供“jibing_diagnosis_frame”，映射五行失衡到具体身体部位；
    - 现实应用：中医养生指导，通过补泄五行来调理身体；
    - 代偿机制：六亲之灾有时以病灾形式应验（以身当劫）。
  - **必要条件**：
    - 能准确对应五行与脏腑经络关系。

<!-- L2_END -->

#### L2.5 桥接层

**因子关系层**：

| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|-------|---------|-------|-------|---------|---------|---------|-----------|
| rel_dts_jb3_001 | pattern | jibing_susceptible_organ_profile | jibing_severity_level | 五行错配定位病位与病性 | 木不受水者血病；土不受火者气伤 | 肝血与脾气系统更易出现中重度疾病 | 《滴天髓》疾病论#诸症 |
| rel_dts_jb3_002 | pattern | jibing_susceptible_organ_profile | jibing_severity_level | 寒热燥湿分型 | 金水伤官、火土印绶在寒/热、燥/湿不同背景下 | 病象分别偏于冷嗽、痰火、风痰或皮肤瘙痒等类型 | 《滴天髓》疾病论#诸症 |
| rel_dts_jb3_003 | aggregation | jibing_susceptible_organ_profile | jibing_health_index | 多点器官受累拉低整体健康指数 | 痰多木火、毒郁火金、金水枯伤肾虚、水土相胜脾胃泄等组合并见 | 器官系统受累点越多、失衡越重，则整体健康指数越低 | 《滴天髓》疾病论#诸症 |

**推理溯源层**：

| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|-------|---------|---------|---------|---------|-------|----------|-----------|
| evi_dts_jb3_001 | "木不受水者血病；土不受火者气伤" | jibing_susceptible_organ_profile | 原文以“木不受水者血病；土不受火者气伤”点名两组错配，将木水、火土的失衡分别对应到血与气系统→工程上需在jibing_susceptible_organ_profile中显式标注“木水错配→血病”“火土错配→气伤”这类映射，用于后续病位推断 | 通过五行错配，可以把抽象组合直接落到“血病/气伤”等具体系统上 | 高 | ✅ | rule_jibing_blood_qi_mismatch |
| evi_dts_jb3_002 | "金水伤官：寒则冷嗽、热则痰火；火土印绶：热则风痰、燥则皮痒" | jibing_susceptible_organ_profile, jibing_severity_level | 原文将同一组合（金水伤官、火土印绶）按“寒/热、燥/湿”分型，分别对应冷嗽、痰火、风痰、皮痒等症→工程上需借助jibing_susceptible_organ_profile标注受累系统，并用jibing_severity_level区分不同体质与失衡程度下的症状深浅 | 同一五行组合在不同寒热燥湿背景下，会呈现不同病象与严重度，需在模型中区分表示 | 高 | ✅ | rule_jibing_cold_hot_dry_damp_pattern |
| evi_dts_jb3_003 | "痰多木火，毒郁火金；金水枯伤肾虚，水土相胜脾胃泄。应六亲而不验者，或以病当之" | jibing_health_index, jibing_susceptible_organ_profile | 原文进一步举出“痰多木火，毒郁火金；金水枯伤肾虚，水土相胜脾胃泄”等例，并指出有时六亲之灾会转化为病灾由本人承受→工程上需在jibing_susceptible_organ_profile中记录这些典型器官受累组合，并在jibing_health_index中加入“代偿承灾”这一下调因子，用以解释某些盘局中六亲不显灾而本人多病的情况 | 多处典型受累组合并见，且有“以病当灾”的代偿现象时，整体健康指数应被显著下调 | 高 | ✅ | rule_jibing_kin_disaster_substitution |

**跨体系概念映射层**：

| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|-------|---------|---------|---------|---------|-----------|------|
| concept_element_mismatch_illness | 元素错配致病 | 木不受水、土不受火等组合导致血病气伤 | 四元素/体液严重失衡，冷湿/热燥体质过偏引发顽疾 | 梦中反复出现溺水、窒息、灼烧、干裂等极端体感意象 | 长期生活方式与内在冲突导致身体系统错配、代偿失调 | 将五行错配视为“系统配置错误”引发的疾病模型 |
| concept_toxin_phlegm_accumulation | 痰毒郁结与慢性损耗 | 痰多木火、毒郁火金、金水枯伤肾虚、水土相胜脾胃泄 | 海王星/冥王星等受克于第六宫或与身体象征行星形成困难相位，指向毒素、药物、潜伏病灶 | 梦见混浊之水、黏稠痰涎、体内有毒物难以排出 | 长期压抑情绪与压力无法宣泄，转化为“身体承载毒素”的感觉 | 体现“痰毒郁结→慢性消耗”的跨体系原型 |
| concept_kin_disaster_substitution | 以身代亲之灾 | 应六亲而不验者，以病当之 | 家宅/亲属宫位受克但力量投射到命主身体宫位，亲人无大灾而本人多病 | 反复梦见亲人遭难但现实中多转为自己生病或受伤 | 过度认同家人、替他人承担责任与罪疚，最终由身体出面“替偿” | 描述“六亲之灾内摄为自身病灾”的代偿机制 |

#### 语义因子提取（因子层）

<!-- FACTOR_BEGIN -->

| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 结构类 | 疾病健康指数 | jibing_health_index | existing | health_index | 高/中/低 | bazi_semantic | 元素和谐时高 |
| 结构类 | 疾病易感器官状态 | jibing_susceptible_organ_profile | existing | organ_profile | 肝心脾肺肾风险 | bazi_semantic | 基于元素错配与脏腑易感性 |
| 态势类 | 疾病严重度 | jibing_severity_level | existing | severity | 重/中/轻 | bazi_semantic | 结合入脏/游经与寒热燥湿综合评估 |
| 时间类 | 疾病发作窗口 | jibing_onset_window | existing | timing | 运岁时段 | bazi_rule_engine | 元素冲突与运岁叠加时更易发作 |

<!-- FACTOR_END -->

- **核心要点**：
  - 病从“喜忌+配伍”来：去病先辨“错位与过/不及”。
  - 诊断层次：藏象（脏腑）→ 经络（部位）→ 体质（冷热燥湿）→ 外境（岁运）。

- **详细解说**：
  1) 定体用与喜忌，标出病位（脏/经）。
  2) 判冷热燥湿倾向，选“泄/生/制/通”之法。
  3) 以岁运校正：先急后缓、先重后轻。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_456]` `[trigger: 论命诸症]` `[factor_trigger: zhuzheng_intro]` `[role: 主干]` 诸症杂论从血气寒热燥湿角度列举多种杂症. → 《滴天髓·疾病论》#诸症
  - `[ns_dts_457]` `[trigger: 木不受水]` `[factor_trigger: mubushoushui]` `[role: 主干依赖]` 木不受水者血病，土不受火者气伤. → 《滴天髓·疾病论》#诸症
  - `[ns_dts_458]` `[trigger: 金水伤官]` `[factor_trigger: jinshui_shangguan]` `[role: 条件分支]` 金水伤官寒则冷嗽热则痰火，火土印绶热则风痰燥则皮痒. → 《滴天髓·疾病论》#诸症
  - `[ns_dts_459]` `[trigger: 六亲代偿]` `[factor_trigger: liuqin_daichang]` `[role: 例外处理]` 应六亲而不验者或以病当之，如妻土被伤实以脾病当之. → 《滴天髓·疾病论》#诸症
  - `[ns_dts_460]` `[trigger: 诸症总则]` `[factor_trigger: zhuzheng_rule]` `[role: 总结]` 疾病从五行模块化审视，脏腑经部冷热燥湿皆可从喜忌入手校正. → 《滴天髓·疾病论》#诸症"""
    normalized_text_zh: str = """"""
    subject: str = "诸症杂论（择要）。"
    factor_refs: list = []
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_诸症杂论_择要_001_L1",
    )
    version: str = "1.0.0"
