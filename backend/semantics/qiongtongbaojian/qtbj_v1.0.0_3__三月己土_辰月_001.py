"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597085
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
    semantic_id="qtbj_v1.0.0_3__三月己土_辰月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3三月己土辰月(SemanticEntry):
    """
    - **原文（source_text）**：
  三月己土，正栽培禾稼之时，先丙后癸，土暖而润，随用甲疏，三者俱透天干，必官居黄阁。或三者透一，科甲定然，但要得地。却以庚金为病。
  或有甲无癸，亦可...
    """
    
    original_text: str = """- **原文（source_text）**：
  三月己土，正栽培禾稼之时，先丙后癸，土暖而润，随用甲疏，三者俱透天干，必官居黄阁。或三者透一，科甲定然，但要得地。却以庚金为病。
  或有甲无癸，亦可致富，但不贵显。或有癸而无甲丙，亦有衣衿。或有丙癸无甲，亦系人才。丙癸全无，流俗之辈。
  或一派乙木，无金制伏，贫而且夭也。

- **分字分词释义**：
  - **栽培禾稼**：种植庄稼 / 辰月特点 / 需暖润疏
  - **土暖而润**：土地温暖润泽 / 丙癸配合 / 吉象
  - **官居黄阁**：官居宰相府 / 三者俱透 / 极贵
  - **庚金为病**：庚金是病神 / 克甲 / 忌神
  - **流俗之辈**：庸俗之人 / 丙癸全无 / 凶象
  - **贫而且夭**：贫穷且夭折 / 乙多无制 / 凶象

- **规范化释义（primary_lang_explained）**：
  三月（辰月）的己土，正是栽培禾稼的时候，先用丙火（暖），后用癸水（润），使土温暖而湿润，随后用甲木疏土。丙、癸、甲三者都透出天干，必定官居黄阁（宰相）。或者三者透出一个，科甲是一定的，但要地支得地（有根）。却以庚金（伤官）为病（克甲/泄土）。
  如果有甲木无癸水，也可以致富，但不贵显（有疏无润）。或者有癸水而无甲木丙火，也有秀才（有润无疏暖）。或者有丙火癸水无甲木，也是人才。丙火癸水全无，流俗之辈。
  如果一派乙木（七杀），没有金（食伤）制伏，贫穷而且夭折（杀重攻身）。

- **完整对等诠释（secondary_lang_full）**：
  Ji Earth in the 3rd Month (Dragon Month): Time to cultivate crops. First Bing, then Gui; Earth becomes warm and moist. Then use Jia to dredge. If all three reveal, one occupies the "Yellow Pavilion" (Prime Minister). If one reveals, Civil Service is certain, but must be grounded. Geng Metal is the disease.
  With Jia but no Gui, one can be rich but not noble/prominent. With Gui but no Jia/Bing, one has a degree. With Bing/Gui but no Jia, one is a talent. Without Bing/Gui, a vulgar person.
  If there is a mass of Yi Wood without Metal to control, one is poor and dies prematurely.

- **核心要点**：
  - **辰月三宝**：丙（暖）、癸（润）、甲（疏）。三者全，黄阁客。
  - **忌庚**：庚克甲，坏了疏土之功。
  - **杀重**：乙多无制，贫夭。

- **详细解说**：
  - 辰月己土当令，土厚。
  - “正栽培禾稼”：辰月谷雨，万物生长，需光（丙）、水（癸）、松土（甲）。
  - “黄阁”：宰相办公的地方，喻极贵。
  - 己土怕七杀（乙），因己土柔弱，乙木克之无情，若无金制，必伤身。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_581]` `[trigger: 辰月己土栽培三宝]` `[factor_trigger: month_chen AND tiangan_ji AND likes_bing_gui_jia]` `[role: 主干]` 三月己土，正栽培禾稼之时，先丙后癸，随用甲疏。 → 《穷通宝鉴·三春己土》#25.3
  - `[ns_qttbj_582]` `[trigger: 丙癸甲三透黄阁极贵]` `[factor_trigger: month_chen AND tiangan_ji AND tiangan_bing AND tiangan_gui AND tiangan_jia AND yellow_pavilion]` `[role: 条件分支]` 丙癸甲三者俱透天干，必官居黄阁。 → 《穷通宝鉴·三春己土》#25.3
  - `[ns_qttbj_583]` `[trigger: 三宝透一得地科甲定然]` `[factor_trigger: month_chen AND tiangan_ji AND (tiangan_bing OR tiangan_gui OR tiangan_jia) AND dizhi_rooted AND kejia_scholar]` `[role: 条件分支]` 或三者透一，科甲定然，但要得地。 → 《穷通宝鉴·三春己土》#25.3
  - `[ns_qttbj_584]` `[trigger: 有甲无癸可富不贵显]` `[factor_trigger: month_chen AND tiangan_ji AND tiangan_jia AND NOT tiangan_gui AND NOT tiangan_bing AND wealth_not_noble]` `[role: 条件分支]` 有甲无癸，亦可致富，但不贵显。 → 《穷通宝鉴·三春己土》#25.3
  - `[ns_qttbj_585]` `[trigger: 有癸无甲丙衣衿之士]` `[factor_trigger: month_chen AND tiangan_ji AND tiangan_gui AND NOT tiangan_jia AND NOT tiangan_bing AND degree_holder]` `[role: 条件分支]` 有癸而无甲丙，亦有衣衿。 → 《穷通宝鉴·三春己土》#25.3
  - `[ns_qttbj_586]` `[trigger: 有丙癸无甲亦系人才]` `[factor_trigger: month_chen AND tiangan_ji AND tiangan_bing AND tiangan_gui AND NOT tiangan_jia AND talent_pattern]` `[role: 条件分支]` 有丙癸无甲，亦系人才。 → 《穷通宝鉴·三春己土》#25.3
  - `[ns_qttbj_587]` `[trigger: 丙癸全无流俗之辈]` `[factor_trigger: month_chen AND tiangan_ji AND NOT tiangan_bing AND NOT tiangan_gui AND vulgar_person]` `[role: 例外处理]` 丙癸全无，流俗之辈。 → 《穷通宝鉴·三春己土》#25.3
  - `[ns_qttbj_588]` `[trigger: 一派乙木无金制贫而且夭]` `[factor_trigger: month_chen AND tiangan_ji AND yi_multiple AND NOT tiangan_geng AND yi_killing_no_control]` `[role: 例外处理]` 或一派乙木，无金制伏，贫而且夭也。 → 《穷通宝鉴·三春己土》#25.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 三月己土（辰月）"
    factor_refs: list = ['yellow_pavilion', 'crops_grains']
    
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
        l1_anchor="qtbj_v1.0.0_3__三月己土_辰月_001_L1",
    )
    version: str = "1.0.0"
