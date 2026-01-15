"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559586
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
    semantic_id="yhzp_v1.0.0_论八字撮要法_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论八字撮要法(SemanticEntry):
    """
    - **原文（source_text）**：  
  论八字撮要法。  
  用之为官，不可伤。用之为财，不可劫。用之为印，不可破。用之食神，不可破。用之为禄，不可冲。若有七杀须要制，制伏太过反为凶；...
    """
    
    original_text: str = """- **原文（source_text）**：  
  论八字撮要法。  
  用之为官，不可伤。用之为财，不可劫。用之为印，不可破。用之食神，不可破。用之为禄，不可冲。若有七杀须要制，制伏太过反为凶；若遇伤官须要静，此是子平万法宗。伤官最怕为官运。正官尤忌见财星。印绶好杀，嫌财位。阳刃怕冲，宜合迎。比肩要逢七杀制。七杀喜见食神刑。有禄怕见官星到。食神最喜偏财临。此是子平撮要法，江湖术者仔细明。

- **分字分词释义**：
  - **用之为官不可伤**：用官星不可被伤官克伤。
  - **用之为财不可劫**：用财星不可被劫财夺。
  - **用之为印不可破**：用印绶不可被财星破。
  - **用之为禄不可冲**：用禄不可被冲。
  - **若有七杀须要制制伏太过反为凶**：七杀须制但太过反凶。
  - **若遇伤官须要静此是子平万法宗**：伤官须静，为万法之宗。
  - **伤官最怕为官运**：伤官最怕行官运。
  - **印绶好杀嫌财位**：印绶喜杀嫌财。
  - **阳刃怕冲宜合迎**：阳刃怕冲宜合。
  - **此是子平撮要法江湖术者仔细明**：此为撮要法，须仔细明了。

- **规范化释义（primary_lang_explained）**：  
  《论八字撮要法》以极简口诀总结子平法用神取用与忌讳的核心要点，是实务判命的"速查表"。**用神不可伤破劫冲**：用官不可伤、用财不可劫、用印不可破、用食神不可破、用禄不可冲；强调用神保护第一要务。**七杀与伤官处理**：七杀须制但制伏太过反凶，伤官须静；此为子平万法宗。**各用神喜忌**：伤官最怕官运、正官尤忌见财（应为忌伤官）、印绶好杀嫌财位、阳刃怕冲宜合迎、比肩要逢七杀制、七杀喜见食神刑（制）、有禄怕见官星、食神最喜偏财临。**江湖术者须仔细明**：此为子平撮要法精髓，江湖术者需仔细明了。

- **完整对等诠释（secondary_lang_full）**：  
  **Discussion on Eight Characters Essential Summary Method**: Summarizes Zi Ping method use-god selection-taboos core points in extremely concise formulas—a quick reference for practical fate judgment. **Use-God Cannot Be Harmed-Broken-Robbed-Clashed**: Using Officer cannot harm; using Wealth cannot rob; using Seal cannot break; using Food God cannot break; using Salary cannot clash. This emphasizes use-god protection as first priority. **Seven Killings and Injury Officer Handling**: Seven Killings require control, but excessive control paradoxically brings fierceness; Injury Officer requires stillness. This is the root principle of Zi Ping's ten thousand methods. **Each Use-God Likes-Dislikes**: Injury Officer most fears Officer fortune; Proper Officer especially taboos seeing Wealth (should be taboos Injury Officer); Seal favors Killing but dislikes Wealth position; Yang Blade fears clash and should meet harmony; Parallel needs to meet Seven Killings for control; Seven Killings delights in seeing Food God for punishment (control); having Salary fears seeing Officer Star; Food God most delights in Indirect Wealth arriving. **River-Lake Practitioners Must Carefully Understand**: This is the essence of Zi Ping's essential summary method—river-lake practitioners need to carefully understand.

- **核心要点**：  
  - 以极简口诀总结用神取用与忌讳的核心要点  
  - 用神不可伤破劫冲为第一要务，强调用神保护  
  - 七杀须制但不可太过，伤官须静，为子平万法宗  
  - 各用神具体喜忌：官怕伤、财怕劫、印怕财、刃怕冲、比肩要杀制等

- **详细解说**：  《论八字撮要法》以极简口诀总结用神喜忌。**用神保护**——"用之为官不可伤，用之为财不可劫，用之为印不可破，用之为禄不可冲"确立用神保护第一要务。**七杀伤官**——"若有七杀须要制，制伏太过反为凶；若遇伤官须要静，此是子平万法宗"揭示七杀伤官的处理法则。**各用神喜忌**——"伤官最怕为官运，正官尤忌见财星，印绶好杀嫌财位，阳刃怕冲宜合迎"；"比肩要逢七杀制，七杀喜见食神刑，有禄怕见官星到，食神最喜偏财临"罗列各用神的具体喜忌。末句"此是子平撮要法，江湖术者仔细明"点明此为撮要精髓。
- **语义提取（L2）**：  
  - **主题**：用神取用与忌讳的核心撮要  
  - **自然属性**：象征以"撮要"指代精炼总结与核心要点；特性为口诀式极简高效；元素包括用神保护、七杀制伏、伤官静养、各用神喜忌等  
  - **功能象义**：为命师提供用神判断的速查口诀；串联用神理论与实务操作  
  - **条件结构**：必要条件为识别用神及其喜忌；增强条件为七杀有制伤官静养；失效条件为用神被伤破劫冲、七杀制过、伤官动等  
  - **多层解释**：字面层罗列用神喜忌口诀；象征层以"撮要"象征命理精髓提炼；实践层为命师提供快速判断用神的口诀工具

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|----------|-----------|--------|
| 八字撮要法 | Eight Characters Essential Summary Method | 用神取用与忌讳的核心口诀总结 | Core formula summary of use-god selection and taboos | essential_summary | existing |
| 用神不可伤破劫冲 | Use-God Cannot Be Harmed-Broken-Robbed-Clashed | 用神保护第一要务 | Use-god protection as first priority | use_god_protection | existing |
| 七杀须制不可太过 | Seven Killings Must Control Not Excessive | 七杀需制伏但制过反凶 | Seven Killings need control but excessive control反fierce | killing_control | existing |
| 伤官须静 | Injury Officer Must Be Quiet | 伤官不宜动旺需静养 | Injury Officer not宜vigorous需quiet cultivation | injury_quiet | existing |
| 子平万法宗 | Zi Ping Ten Thousand Methods Patriarch | 子平法核心宗旨 | Zi Ping method core tenet | ziping_core | existing |

<!-- L2_END -->
<!-- FACTOR_BEGIN -->
- **因子层（语义因子八列表）**：

| 因子类型 | 因子标签（人话） | 因子ID（如已存在） | 因子来源 | 角色/位置 | 取值/约束 | engine_id | 备注 |
|----------|------------------|--------------------|----------|----------|----------|-----------|------|
| 判断类 | 用神保护原则 | use_god_protection | existing | 用神第一要务 | 不可伤破劫冲 | bazi_rule_engine | 核心原则 |
| 判断类 | 七杀制伏原则 | seven_killings_control | existing | 七杀处理 | 须制但不可太过 | bazi_rule_engine | 平衡法则 |
| 判断类 | 伤官静养原则 | injury_officer_quiet | existing | 伤官处理 | 须静不宜动 | bazi_rule_engine | 伤官特性 |
| 关系类 | 各用神具体喜忌 | each_use_god_likes_dislikes | existing | 用神配置 | 官怕伤/财怕劫/印怕财等 | bazi_rule_engine | 喜忌细则 |
| 理论类 | 子平万法宗 | ziping_core_tenet | existing | 理论宗旨 | 七杀制伏伤官静养 | bazi_rule_engine | 核心宗旨 |

<!-- FACTOR_END -->

<!-- L2.5_BEGIN -->
#### L2.5 桥接层
**因子关系层**：
| 关系ID | 关系类型 | 因子A | 因子B | 关系性质 | 条件约束 | 效果方向 | source_ref |
|--------|---------|-------|-------|---------|---------|---------|------------|
| rel_yhzp_149 | condition_relation | use_god | harm_break | 用神保护 | 不可伤破劫冲 | 损害 | 《渊海子平·论八字撮要法》 |
| rel_yhzp_150 | condition_relation | killing | control | 七杀须制 | 不可太过 | 平衡 | 《渊海子平·论八字撮要法》 |
| rel_yhzp_cy_001 | preference | shangguan | shangguan | 伤官最怕官运 | 伤官格 | 大忌 | 《渊海子平·论八字撮要法》 |
| rel_yhzp_cy_002 | preference | yinshou | yinshou | 印绶好杀嫌财 | 印绶格 | 喜忌 | 《渊海子平·论八字撮要法》 |
| rel_yhzp_cy_003 | preference | yangren | anhe | 阳刃怕冲宜合 | 阳刃格 | 喜忌 | 《渊海子平·论八字撮要法》 |
| rel_yhzp_cy_004 | preference | shishen | shishen_piancai | 食神最喜偏财临 | 食神格 | 喜配 | 《渊海子平·论八字撮要法》 |
**推理溯源层**：
| 证据ID | 原文锚点 | 涉及因子 | 推理步骤 | 结论方向 | 置信度 | 可生成规则 | 目标规则ID |
|--------|---------|---------|---------|---------|-------|----------|------------|
| evi_yhzp_149 | "用之为官不可伤，用之为财不可劫，用之为印不可破" | use_god_protection | 用神→保护→不可伤破劫冲 | 用神保护 | 高 | ✅ | rule_use_god_protection |
| evi_yhzp_cy_001 | "若遇伤官须要静，此是子平万法宗" | injury_officer_quiet | 伤官须静→万法宗 | 伤官静养 | 高 | ✅ | rule_injury_quiet |
| evi_yhzp_cy_002 | "印绶好杀，嫌财位；阳刃怕冲，宜合迎" | seal_blade_likes | 印好杀/刃怕冲 | 印刃喜忌 | 高 | ✅ | rule_seal_blade_preference |
**跨体系概念映射层**：
| 概念ID | 共通语义 | 八字对应 | 占星对应 | 梦学对应 | 心理学对应 | 备注 |
|--------|---------|---------|---------|---------|-----------|------|
| concept_summary | 撮要与精髓 | essential_summary | chart_summary | key_points | synthesis | 八字撮要法 |
<!-- L2.5_END -->

---

### 70. 格局生死引用"""
    normalized_text_zh: str = """"""
    subject: str = "论八字撮要法"
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_论八字撮要法_001_L1",
    )
    version: str = "1.0.0"
