"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264213
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
    semantic_id="smth_v1.0.0_纳音与真气交互_001",
    book_id="sanming",
    engine_id="bazi"
)
class 纳音与真气交互(SemanticEntry):
    """
    - 原文（source_text）：
  凡命取干支与纳音同类，壬子、壬午真木，己酉、己卯真土，丙子、丙午真水，戊子、戊午真火，乙丑、乙未、庚辰、庚戌真金。
  凡命取五行真气交互，如辛亥金人得丁巳土...
    """
    
    original_text: str = """- 原文（source_text）：
  凡命取干支与纳音同类，壬子、壬午真木，己酉、己卯真土，丙子、丙午真水，戊子、戊午真火，乙丑、乙未、庚辰、庚戌真金。
  凡命取五行真气交互，如辛亥金人得丁巳土，有丁壬合真木往来，有丙辛合真水往来。丁巳土人得癸亥水，有戊癸合真火往来，有丁壬合真木往来。如戊戌、癸亥、丁巳、辛亥，交互真气全，乃宰相命也。

- 分字分词释义：
  - **真五行**：纳音与干支五行属性有特殊关联或强化者（如壬子纳音桑柘木，子为木沐浴？此处真木指干支纳音配合得宜）。其实原文所列皆为纳音五行（壬子木、己酉土等），所谓“真”，指干支气势与纳音相辅。
  - **真气交互**：四柱干支通过天干五合、地支六合、纳音生克等，形成复杂而有情的网络。

- **规范化释义（primary_lang_explained）**：
  有些命局取纳音与干支同类或有特殊感应者为贵。如壬子（纳音木，干水支水生木？）等。
  更重要的是“真气交互”，即四柱干支纳音之间，通过合化、互换禄马贵人等，形成紧密联系。如辛亥（纳音金）见丁巳（纳音土），天干丁壬（亥中壬）合木，丙（巳中丙）辛合水，地支巳亥冲出气，纳音土生金，这种交互往来，主大贵。

- 核心要点：
  - **纳音补气**：纳音可补正五行不足。
  - **交互得贵**：干支暗合、换禄、换贵。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_033]` `[trigger: 真五行]` `[factor_trigger: zhen_wuxing AND ganzhi_nayin]` `[role: 主干]` 凡命取干支与纳音同类，壬子、壬午真木，己酉、己卯真土。 → 《三命通会》卷十#纳音与真气交互
  - `[ns_smth_10_034]` `[trigger: 真气交互]` `[factor_trigger: zhenqi_jiaohu AND dingrenhe_bingxinhe]` `[role: 主干依赖]` 凡命取五行真气交互，有丁壬合真木往来，有丙辛合真水往来。 → 《三命通会》卷十#纳音与真气交互
  - `[ns_smth_10_035]` `[trigger: 交互全备]` `[factor_trigger: jiaohu_quanbei AND zaixiang_ming]` `[role: 条件分支]` 如戊戌、癸亥、丁巳、辛亥，交互真气全，乃宰相命也。 → 《三命通会》卷十#纳音与真气交互
  - `[ns_smth_10_036]` `[trigger: 纳音补气]` `[factor_trigger: nayin_buqi AND wuxing_buzu]` `[role: 总结]` 纳音可补正五行不足，干支暗合、换禄、换贵为交互得贵。 → 《三命通会》卷十#纳音与真气交互"""
    normalized_text_zh: str = """"""
    subject: str = "纳音与真气交互"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_68', 'bazi_semantic', 'bazi_condition_factor_96', 'bazi_semantic', 'bazi_state_factor_229', 'bazi_semantic', 'bazi_relation_factor_105', 'bazi_semantic', 'source_ref', 'rel_smth_10_031', 'nayin_tongzhi', 'rel_smth_10_032', 'zhenqi_quanbei', 'rel_smth_10_033', 'nayin_buqi', 'evi_smth_10_031', 'nayin_tongzhi', 'rule_nayin_tongzhi1', 'evi_smth_10_032', 'jigui_mingzao', 'rule_zhenqi_quanbei1', 'evi_smth_10_033', 'nayin_buqi', 'rule_nayin_buqi1', 'map_smth_10_021', 'map_smth_10_022']
    
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
        l1_anchor="smth_v1.0.0_纳音与真气交互_001_L1",
    )
    version: str = "1.0.0"
