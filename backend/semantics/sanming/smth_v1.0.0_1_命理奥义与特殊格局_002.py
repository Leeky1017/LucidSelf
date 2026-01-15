"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.081185
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
    semantic_id="smth_v1.0.0_1_命理奥义与特殊格局_002",
    book_id="sanming",
    engine_id="bazi"
)
class 1命理奥义与特殊格局(SemanticEntry):
    """
    - 原文（source_text）：
  受命之不同也，有如受形；测理之难精也，过于测海。阴惨阳舒，知盈虚之有数；天高地迥，极覆载之无疆。或升之云汉兮，而非有所私；或坠之渊泉兮，而非有所恶。其气数定于...
    """
    
    original_text: str = """- 原文（source_text）：
  受命之不同也，有如受形；测理之难精也，过于测海。阴惨阳舒，知盈虚之有数；天高地迥，极覆载之无疆。或升之云汉兮，而非有所私；或坠之渊泉兮，而非有所恶。其气数定于太初，其培覆譬诸草木。妙诀不在于多言，至人奚事于强聒。
  且如类属从化，格判旺衰；照伏拱遥，局分明暗。
  论用神，论日主，各有所宜；取地脉，取天元，是或一道。
  游心于去留舒配，决意于喜忌爱憎。
  亦有源浊而流清，岂无根甜而裔苦。
  鸳鸯比翼，见江湖必遂平生；蝴蝶双飞，逢园囿方为得所。
  采精金于青沙黄碛，别利器于错节盘根。
  我生者，岂若生我之为安；克我者，曾如我克者之为显。
  如逢既济未济，休疑冲并，休疑无依。
  内有三正三偏，不必生扶，不必透露。
  奔道途而丧生，盖因秀气繁乱；坐囹圄以亡命，只为比肩争斗。
  刃重官轻，业屠沽于市井；马疲印破，弄刀笔于公堂。
  三奇再犯戌辰，作斵削裁缝之匠。
  四柱尽归禄位，享眉寿景福之人。

- 分字分词释义：
  - **类属从化**：五行归类与从化格。
  - **照伏拱遥**：见不见之形（如拱禄、遥巳）。
  - **鸳鸯比翼**：双合（如丙戌辛丑，丙辛合，丑戌刑？注云：丙辛合，丁壬合，双合为鸳鸯）。
  - **蝴蝶双飞**：木火象（如辛未戊戌，未为木库，戊戌平地木，木多为园囿）。
  - **采精金**：如甲午（沙中金）见巳（金长生）。
  - **我生者/生我者**：食伤不及印绶安稳。
  - **克我者/我克者**：官煞不如财星显达（此说有争议，原注谓用财制人，用官受制于人）。
  - **三正三偏**：正财官印，偏财官印。

- **规范化释义（primary_lang_explained）**：
  命理之深奥，如测海之难。气数盈虚，皆有定数。
  论命要看格局的旺衰（类属从化），分辨明暗的局势（照伏拱遥）。
  用神与日主，各有所宜。去留舒配，喜忌爱憎，是论命的关键。
  源浊流清（先凶后吉），根甜裔苦（先吉后凶）。
  鸳鸯比翼（双合），见水（江湖）则吉。蝴蝶双飞（木象），见木（园囿）则吉。
  从沙中金（青沙黄碛）中采出精金，在错节盘根中辨别利器（指特殊格局的成材）。
  食伤（我生）不如印绶（生我）安稳，官煞（克我）不如财星（我克）显达。
  既济未济之格（水火），不要怀疑其冲并或无依，往往大贵。
  柱中若有三正三偏（财官印），即使不透出，不生扶，也自有福气。
  秀气（食伤）太过繁乱，奔波丧生。比劫争斗，牢狱亡命。
  刃重官轻，屠夫酒保。财星（马）疲弱，印绶被破，公堂刀笔吏。
  三奇（财官印或乙丙丁）若再见辰戌冲，多为工匠。
  四柱干支归禄（日禄归时或各归其禄），主长寿享福。

- 核心要点：
  - **格局辨析**：明暗、从化、拱遥。
  - **十神比较**：印财优于食官（相对而言）。
  - **职业推断**：屠沽、刀笔、工匠。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_041]` `[trigger: 类属从化]` `[factor_trigger: leishu_conghua AND gepan_wangshuai]` `[role: 主干]` 且如类属从化，格判旺衰；照伏拱遥，局分明暗。 → 《三命通会》卷十二#命理奥义与特殊格局
  - `[ns_smth_12_042]` `[trigger: 鸳鸯比翼]` `[factor_trigger: yuanyang_biyi AND hudie_shuangfei]` `[role: 主干依赖]` 鸳鸯比翼，见江湖必遂平生；蝴蝶双飞，逢园囿方为得所。 → 《三命通会》卷十二#命理奥义与特殊格局
  - `[ns_smth_12_043]` `[trigger: 采精金]` `[factor_trigger: caijingjin_qingshahuangqi AND bieliqi_cuojie]` `[role: 条件分支]` 采精金于青沙黄碛，别利器于错节盘根。 → 《三命通会》卷十二#命理奥义与特殊格局
  - `[ns_smth_12_044]` `[trigger: 刃重官轻]` `[factor_trigger: renzhong_guanging AND tugu_shijing]` `[role: 总结]` 刃重官轻，业屠沽于市井；马疲印破，弄刀笔于公堂。 → 《三命通会》卷十二#命理奥义与特殊格局"""
    normalized_text_zh: str = """"""
    subject: str = "1 命理奥义与特殊格局"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'new_candidate', 'bazi_semantic', 'bazi_structure_factor_40', 'bazi_semantic', 'bazi_state_factor_100', 'bazi_semantic', 'bazi_relation_factor_46', 'bazi_semantic', 'bazi_relation_factor_47', 'bazi_semantic', 'bazi_condition_factor_27', 'bazi_semantic', 'source_ref', 'rel_smth_12_037', 'core_factor', 'rel_smth_12_038', 'cond_factor', 'rel_smth_12_039', 'risk_factor', 'evi_smth_12_037', 'core_factor', 'rule_name37', 'evi_smth_12_038', 'cond_factor', 'rule_name38', 'evi_smth_12_039', 'risk_factor', 'rule_name39', 'map_smth_12_025', 'map_smth_12_026']
    
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
        l1_anchor="smth_v1.0.0_1_命理奥义与特殊格局_002_L1",
    )
    version: str = "1.0.0"
