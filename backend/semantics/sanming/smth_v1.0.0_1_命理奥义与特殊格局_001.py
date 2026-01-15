"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.080933
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
    semantic_id="smth_v1.0.0_1_命理奥义与特殊格局_001",
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
  - **English**：
    - Summary evaluation terms explained; overall life trajectory described as tendency rather than destiny.


- **规范化释义（primary_lang_explained）**：  
  本节金声玉振赋先从“受命之不同”“测理之难精”落笔，指出命理之学如测海探渊，既要承认气数盈虚自有定数，又必须在有限文字中寻找判断的“纲领”。赋文用“类属从化”与“照伏拱遥”概括高级格局的两大维度：一是看五行与十神是否能够归类成势、顺从化气之流（由散乱而成为“类属从化”的整体），二是分辨明局与暗局——哪些用神是直接透出、看得见的，哪些则是伏藏、拱合、遥接而成局。只有在这两层结构清楚之后，谈用神、谈日主的宜忌才有落脚点。  
  继而，赋文提出“去留舒配，决意于喜忌爱憎”的实践原则：论命者必须在保留与舍弃之间做出取舍，不能只看表面强弱，而要结合“源浊流清”“根甜裔苦”之类比喻，体察格局是先凶后吉，还是先吉后凶。鸳鸯比翼、蝴蝶双飞等形象，则把双合、多合、木火相生等结构，转译为现实中的情缘与境遇——见水则鸳鸯得所，见木则蝴蝶有栖。沙中采精金、盘根别利器的比喻，强调在看似平凡甚至浊杂的组合里，仍能淘洗出可用的贵格。最后，通过“我生者/生我者”“克我者/我克者”与“三正三偏”的比较，赋文给出十神取舍的价值次序：相较于泛滥的食伤与难控的官煞，稳定的印绶与可主主动作为的财星，更适合作为高层格局的重心；同时也提醒，秀气太过、比劫争斗会把好局拉向奔波与牢狱，而刃重官轻、财弱印破，则把人推向屠沽、刀笔这一类行业。  

- **完整对等诠释（secondary_lang_full）**：  
  This section of the "Golden Sound and Jade Resonance" ode opens by stressing how difficult fate‑reading truly is. To "receive life" is as varied as taking on different forms, and to "measure principle" is said to be harder than sounding the depths of the sea. The text therefore insists that one must both acknowledge a pre‑given rhythm of waxing and waning qi and still search for governing rules within it. The idea of "class and follow‑transformation" points to charts in which the Five Elements and the Ten Spirits can be gathered into coherent formations that either obey or resist transformative flows; "shine, hide, arch, and remote" describes whether useful spirits are openly visible, hidden in branches, formed by virtual arches, or connected at a distance. Only once these structural questions are answered does it make sense to speak about which spirit to use and how the Day Master should be treated.  
  The ode then moves to practical decision‑making. To "let the mind wander among what is to be retained or released, and to decide according to likes and dislikes" is not a call for whimsy, but a reminder that a chart is judged by which parts are allowed to flourish and which are deliberately constrained. Images such as "turbid source, clear flow" or "sweet root, bitter fruit" summarize life patterns that begin in hardship and end in clarity, or start in privilege and decline into strain. Paired motifs like "mandarin ducks flying together" and "butterflies flying in pairs" translate double combinations and Wood‑Fire symbolism into concrete experiences of relationship and environment—certain unions come fully into their element only when they meet the right surroundings. Likewise, the metaphor of extracting fine metal from coarse sand and picking out tools from among knotted roots highlights the work of recognizing truly exceptional structures within what first appears to be muddled or crude.  
  Finally, the passage compares different Ten Spirits and their roles. It suggests that productions of the self (Eating and Wounded spirits) are less reliable as long‑term supports than the Seal that nourishes the self; that those who control the self (Officials and Killings) are less conducive to autonomous achievement than the Wealth the self controls in turn; and that internal configurations of three proper and three partial stars can confer blessing even when they are not prominently revealed or explicitly reinforced. At the same time, it warns that overly exuberant talent (excessive Eating/Wounded qi) and fierce contention among Peers can lead to lives spent chasing and losing, even to imprisonment. Heavy Blades with light Officials and tired Wealth with broken Seals point toward butchers, tavern‑keepers, low scribes, and craftsmen—occupations carved out by particular mixtures of strength and compromise. When all stems and branches return to their positions of salary and stipend, by contrast, the person is portrayed as enjoying long life and broad fortune.  

- 核心要点：
  - **格局辨析**：明暗、从化、拱遥。
  - **十神比较**：印财优于食官（相对而言）。
  - **职业推断**：屠沽、刀笔、工匠。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_017]` `[trigger: 类属从化]` `[factor_trigger: leishu_conghua AND gepan_wangshuai]` `[role: 主干]` 且如类属从化，格判旺衰；照伏拱遥，局分明暗。 → 《三命通会》卷十二#命理奥义与特殊格局
  - `[ns_smth_12_018]` `[trigger: 鸳鸯比翼]` `[factor_trigger: yuanyang_biyi AND hudie_shuangfei]` `[role: 主干依赖]` 鸳鸯比翼，见江湖必遂平生；蝴蝶双飞，逢园囿方为得所。 → 《三命通会》卷十二#命理奥义与特殊格局
  - `[ns_smth_12_019]` `[trigger: 采精金]` `[factor_trigger: caijingjin_qingshahuangqi AND bieliqi_cuojie]` `[role: 条件分支]` 采精金于青沙黄碛，别利器于错节盘根。 → 《三命通会》卷十二#命理奥义与特殊格局
  - `[ns_smth_12_020]` `[trigger: 刃重官轻]` `[factor_trigger: renzhong_guanging AND tugu_shijing]` `[role: 总结]` 刃重官轻，业屠沽于市井；马疲印破，弄刀笔于公堂。 → 《三命通会》卷十二#命理奥义与特殊格局"""
    normalized_text_zh: str = """"""
    subject: str = "1 命理奥义与特殊格局"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'new_candidate', 'bazi_semantic', 'bazi_structure_config_1', 'bazi_semantic', 'bazi_state_factor_97', 'bazi_semantic', 'bazi_relation_unnamed_1', 'bazi_semantic', 'bazi_relation_unnamed_2', 'bazi_semantic', 'bazi_level', 'bazi_semantic', 'source_ref', 'rel_smth_12_016', 'core_factor', 'rel_smth_12_017', 'cond_factor', 'rel_smth_12_018', 'risk_factor', 'evi_smth_12_016', 'core_factor', 'rule_name16', 'evi_smth_12_017', 'cond_factor', 'rule_name17', 'evi_smth_12_018', 'risk_factor', 'rule_name18', 'map_smth_12_011', 'map_smth_12_012']
    
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
        l1_anchor="smth_v1.0.0_1_命理奥义与特殊格局_001_L1",
    )
    version: str = "1.0.0"
