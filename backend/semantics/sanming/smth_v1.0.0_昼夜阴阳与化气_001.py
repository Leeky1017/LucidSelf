"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264222
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
    semantic_id="smth_v1.0.0_昼夜阴阳与化气_001",
    book_id="sanming",
    engine_id="bazi"
)
class 昼夜阴阳与化气(SemanticEntry):
    """
    - 原文（source_text）：
  凡命先论化气。考《五运篇》，以甲、丙、戊、庚、壬合五阴干为太过；乙、丁、巳、辛、癸合五阳干为不及。太过、不及之间，有权存焉。
  考《天元变化书》，又分昼夜。...
    """
    
    original_text: str = """- 原文（source_text）：
  凡命先论化气。考《五运篇》，以甲、丙、戊、庚、壬合五阴干为太过；乙、丁、巳、辛、癸合五阳干为不及。太过、不及之间，有权存焉。
  考《天元变化书》，又分昼夜。如六甲日生木，夜生化土，故六戊人得甲，取日生为鬼，夜生为官；用六乙人，日生用金，夜生用木。独六己、六庚不变。
  是以五阳干昼生为本体，夜生作化看；五阴干夜生为本体，昼生作化看。

- 分字分词释义：
  - **太过不及**：阳干合阴干（如甲己合），阳气胜，为太过；阴干合阳干（如己甲合），阴气柔，为不及。
  - **昼夜化气**：古法认为，阳干昼生力强，保持本体；夜生力弱，随合而化。阴干反之，夜生力强保本体，昼生从化。

- **规范化释义（primary_lang_explained）**：
  看命先看化气。阳干合阴干往往气势太过，阴干合阳干气势不及。
  根据《天元变化书》，还要分昼夜。如甲木日主，白天生维持木性，晚上生则易化土（甲己化土）。因此，戊土日主见甲木，若甲木昼生，则为七煞（鬼）；若甲木夜生，化为土（或贪合忘煞），则不为鬼，反有情（或化官？原文意指性质变化）。
  原则是：五阳干（甲丙戊庚壬）白天生看原五行，晚上生看化气五行；五阴干（乙丁己辛癸）晚上生看原五行，白天生看化气五行。但六己、六庚日较为特殊，变化较少。

- 核心要点：
  - **化气条件**：除月令外，昼夜亦是关键。
  - **阳昼阴夜**：阳干昼显本性，夜易化；阴干夜显本性，昼易化。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_037]` `[trigger: 先论化气]` `[factor_trigger: xianlun_huaqi AND taiguo_buji]` `[role: 主干]` 凡命先论化气，以甲、丙、戊、庚、壬合五阴干为太过。 → 《三命通会》卷十#昼夜阴阳与化气
  - `[ns_smth_10_038]` `[trigger: 昼夜化气]` `[factor_trigger: zhouye_huaqi AND jiari_muzhi]` `[role: 主干依赖]` 又分昼夜，如六甲日生木，夜生化土。 → 《三命通会》卷十#昼夜阴阳与化气
  - `[ns_smth_10_039]` `[trigger: 阳昼本体]` `[factor_trigger: yangzhou_benti AND yinyehua]` `[role: 条件分支]` 五阳干昼生为本体，夜生作化看；五阴干夜生为本体，昼生作化看。 → 《三命通会》卷十#昼夜阴阳与化气
  - `[ns_smth_10_040]` `[trigger: 独六己庚]` `[factor_trigger: du_liuji_liugeng AND bu_bian]` `[role: 总结]` 独六己、六庚不变。 → 《三命通会》卷十#昼夜阴阳与化气"""
    normalized_text_zh: str = """"""
    subject: str = "昼夜阴阳与化气"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_condition_factor_97', 'bazi_semantic', 'bazi_state_factor_230', 'bazi_semantic', 'bazi_state_factor_231', 'bazi_semantic', 'bazi_condition_factor_98', 'bazi_semantic', 'bazi_condition_factor_99', 'bazi_semantic', 'source_ref', 'rel_smth_10_034', 'taiguo_buji', 'rel_smth_10_035', 'yangzhou_benti', 'rel_smth_10_036', 'yinye_benti', 'evi_smth_10_034', 'taiguo_buji', 'rule_taiguo_buji1', 'evi_smth_10_035', 'yangzhou_benti', 'rule_yangzhou_benti1', 'evi_smth_10_036', 'yinye_benti', 'rule_yinye_benti1', 'map_smth_10_023', 'map_smth_10_024']
    
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
        l1_anchor="smth_v1.0.0_昼夜阴阳与化气_001_L1",
    )
    version: str = "1.0.0"
