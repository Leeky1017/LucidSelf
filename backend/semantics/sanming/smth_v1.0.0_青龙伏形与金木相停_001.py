"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.413020
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
    semantic_id="smth_v1.0.0_青龙伏形与金木相停_001",
    book_id="sanming",
    engine_id="bazi"
)
class 青龙伏形与金木相停(SemanticEntry):
    """
    - **原文（source_text）**：

  甲乙木属东方，谓之青龙。伏形者，伏于金也。如甲申、甲戌、乙巳、乙酉、乙丑，此五日生，坐下财官，俱要月令有托，官星得地，不见伤官之神，金木相停为合象。...
    """
    
    original_text: str = """- **原文（source_text）**：

  甲乙木属东方，谓之青龙。伏形者，伏于金也。如甲申、甲戌、乙巳、乙酉、乙丑，此五日生，坐下财官，俱要月令有托，官星得地，不见伤官之神，金木相停为合象。有以乙巳日时，名青龙伏藏，主饮酒有失，暗损福寿，不饮则可。诗曰：甲乙如居申酉乡，木逢春旺最为良，四柱若逢库相助，财官双美不寻常。

- 分字分词释义：

  - **甲乙木属东方，谓之青龙**：以甲乙木喻东方青龙之气，主生发、仁恕。
  - **伏形者，伏于金也**：所谓“伏形”，是指木日坐于申、酉等金地之上，如青龙潜伏于金中。
  - **甲申、甲戌、乙巳、乙酉、乙丑此五日生**：列出青龙伏形的典型日柱，皆为甲乙木坐财官之地。
  - **月令有托，官星得地**：要求月令能为木日与其官星提供正向依托，使财官不致浮虚。
  - **不见伤官之神，金木相停为合象**：忌再见过重伤官来克官或破局，理想状态是金木力量均衡，成“相停”之美。
  - **乙巳日时名青龙伏藏**：乙巳日时另有“青龙伏藏”之名，原文以此象征饮酒失德、损福之虞。

- **规范化释义（primary_lang_explained）**：

  青龙伏形格，是专就甲乙木日坐申、酉、巳、丑等金地的一类组合而言。甲乙木本属东方青龙之象，喜生于春令、得水火之助；然而当其日支却落在申酉等金位时，就好像青龙潜伏于金中，一方面借金为财官之源，一方面又受金之制约。

  原文指出：此类日柱若能在月令上得托（如月令帮扶木或官），并且官星得地、不受伤官破坏，便可形成“金木相停”的合局——既有木之生发，也有金之肃杀，财官俱在而不过分偏枯，自然容易成“财官双美”的命式。反之，若再遇伤官太重，或以饮酒、放纵等方式激化“伏藏之龙”，则容易暗损福寿，甚至以酒色之事破格。

- 核心要点：

  - 以**甲乙木日坐金地**为基础（甲申、甲戌、乙巳、乙酉、乙丑等），象青龙伏于金。
  - 要求月令有托、官星得地、不见伤官，方成“金木相停”的合象。
  - 成局时，多主财官双美、有文名与实权；破局时，则易因伤官、酒色等而损福。

- 详细解说：

  可以把青龙伏形理解为一种“以柔制刚、以刚护柔”的结构：甲乙木若纯居木火之地，虽有生发之美，却可能欠缺权势与节制；当其坐于金地时，一方面金为财官之源，使木日得财官之利，另一方面金又可制木之过伸，使其性情更见沉稳与持重。

  然而，伏形之“伏”也暗含风险：

  1. 若金过重、木过弱，则伏而不发，容易一生多受约束、难展所长；
  2. 若再见伤官过旺，则官星受损，原有的财官双美之象被破；
  3. 原文特别提到“乙巳日时名青龙伏藏，主饮酒有失”，可视为对行为层面的提醒——命局中伏形者，若又沉迷酒色，更易引发隐性损耗。

  因此，在实务判断时，需要同时看：

  - 木气是否得印比扶持，使其不至于被金完全压制；
  - 官星是否稳固，并无伤官、七煞横生；
  - 行运是否有助于“伏龙见头”，即在适当年份与运程中，使财官之利得以舒展，而不被过度克制或诱发伤灾。

- **校勘与字词辨析（双语）**：

  - 原文“甲乙木属东方，谓之青龙伏形者，伏于金也”一句，本稿在释义中拆解为“青龙之象”与“伏于金地”两层，以便理解其象意。
  - “青龙伏藏”一语，本稿理解为“德行与才能藏于内而未显”，在白话中以“饮酒有失、暗损福寿”的例子加以说明，提示此格既有隐藏之德，也有隐藏之祸。
  - 诗句“甲乙如居申酉乡，木逢春旺最为良，四柱若逢库相助，财官双美不寻常”，本稿在白话与核心要点中概括为“春令助木、库地助财官”两重条件，而不逐句拆译。
  - **English**：
    - Dual conditions noted without sentence-by-sentence translation.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_253]` `[trigger: 青龙伏形]` `[factor_trigger: qinglong_fuxing AND jiayi_dongfang]` `[role: 主干]` 甲乙木属东方，谓之青龙。伏形者，伏于金也。 → 《三命通会》卷六#青龙伏形
  - `[ns_smth_06_254]` `[trigger: 坐下财官]` `[factor_trigger: zuoxia_caiguan AND yueling_youtuo]` `[role: 主干依赖]` 坐下财官，俯要月令有托，官星得地。 → 《三命通会》卷六#青龙伏形
  - `[ns_smth_06_255]` `[trigger: 金木相停]` `[factor_trigger: jinmu_xiangting AND hexiang]` `[role: 条件分支]` 不见伤官之神，金木相停为合象。 → 《三命通会》卷六#青龙伏形
  - `[ns_smth_06_256]` `[trigger: 财官双美]` `[factor_trigger: siku_xiangzhu AND caiguan_shuangmei]` `[role: 总结]` 四柱若逢库相助，财官双美不寻常。 → 《三命通会》卷六#青龙伏形"""
    normalized_text_zh: str = """"""
    subject: str = "青龙伏形与金木相停"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_88', 'bazi_semantic', 'bazi_condition_wood_2', 'bazi_semantic', 'bazi_condition_factor_225', 'bazi_semantic', 'bazi_state_metal_4', 'bazi_semantic', 'source_ref', 'rel_smth_06_217', 'qinglongfuxing_presence', 'rel_smth_06_218', 'jinmu_xiangting', 'rel_smth_06_219', 'jinzhong_wuyin', 'evi_smth_06_217', 'qinglongfuxing_presence', 'rule_qinglong', 'evi_smth_06_218', 'jinmu_xiangting', 'rule_xiangting', 'evi_smth_06_219', 'jinzhong_wuyin', 'rule_muzhe', 'map_smth_06_145', 'map_smth_06_146']
    
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
        l1_anchor="smth_v1.0.0_青龙伏形与金木相停_001_L1",
    )
    version: str = "1.0.0"
