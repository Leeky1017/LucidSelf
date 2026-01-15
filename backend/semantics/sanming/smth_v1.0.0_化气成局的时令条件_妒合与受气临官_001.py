"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264422
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
    semantic_id="smth_v1.0.0_化气成局的时令条件_妒合与受气临官_001",
    book_id="sanming",
    engine_id="bazi"
)
class 化气成局的时令条件妒合与受气临官(SemanticEntry):
    """
    - **原文（source_text）**：  
  又曰：甲己化土，有二则化，一不能化，仍还本位之性。所谓一不能生，生物必两。此天干一阴一阳，如夫妇配合成偶，方能变化成形，阴阳不合，安得化机之宣哉？...
    """
    
    original_text: str = """- **原文（source_text）**：  
  又曰：甲己化土，有二则化，一不能化，仍还本位之性。所谓一不能生，生物必两。此天干一阴一阳，如夫妇配合成偶，方能变化成形，阴阳不合，安得化机之宣哉？是以有妒化之说。如甲己见乙，乙庚见辛，丁壬见丙，戊癸见壬，丙辛见丁，所谓妒花。自恋其生，遂成一家之好，爱恋亲情，何能从化？故化象须归一方稳。如丁壬化木，柱中见癸，并子虽强成木，不成真物，是化而不化也。又曰：大凡化气，只取日干而言，配合之神，或年月与时皆可用。但要日辰得旺气于时，若不得月中旺气，只时上旺气亦可。倘得月中旺气，而时上不乘旺气，则不可用。若月与日时俱得旺气，方为全吉。甲己化土，非辰戌丑未月不化，其次午月亦化，有戊字间之，则不化，名曰妒合。凡辰戌丑未生人，柱有己亥，为受气临官，主晚年不吉，有官夺官，有财夺财，夫受气临官，长生第四位也，以干为主，双犯则应，余月不应。又曰：甲己化土，切要木为官，得亥卯未为官，戊癸气为福，忌见丁壬日时。乙庚化金，非巳酉丑月不化，其次七月亦化，有甲字间之，则不化，名曰妒合。凡巳酉丑生人，柱有庚申，名曰受气临官，晚年不佳。又曰：乙庚化金，切要火为官，故喜丙丁巳午，甲己为福，忌见戊癸日时。丙辛化水，非申子辰月不化，其次十月亦化。柱有丁字不化，名曰妒合。凡申子辰生人，见癸亥，名曰受气临官，亦主晚年不佳。又曰：丙辛化水，切要土为官，得辰戌丑未为官，乙庚为福，忌见甲己日时。丁壬化木，非亥卯未月不化，其次正月亦化，柱有丙字不化，名曰妒合。亥卯未生人，见甲寅，名曰受气临官，晚年不佳。又曰：丁壬化木，切要庚辛申酉为官，丙辛为福，忌见乙庚日时。戊癸化火，非寅午戌月不化，其次四月亦化。柱有己字不化，名曰妒合。凡寅午戌生人，见丁巳为受气临官，晚年不佳。又曰：戊癸化火，切要壬癸亥子为官，丁壬为福，忌见丙辛日时。

- **规范化释义（primary_lang_explained）**：  
  在把十干化气提升到宏观结构之后，本段回到“成局条件”与典型例外。首先，“化气”必须是一阴一阳成偶，“一则不生”，单干不成化，只能保留本位属性。其次，还需要有合适的时令与地支承接：甲己化土宜在辰戌丑未土月，乙庚化金宜在巳酉丑金月，丙辛化水宜在申子辰水月，丁壬化木宜在亥卯未木月，戊癸化火宜在寅午戌火月，并各有一到两个月作为次优选择。若在这些条件之外，或者被第三干“插足”，就出现“妒化”与“妒合”：例如甲己本欲化土，却又见乙木来争，或在月令间有戊土穿插，都会令化象不成，退回各行本性，或形成“化而不化”的伪象。另一方面，“受气临官”则指某些特殊组合：如辰戌丑未生而柱中见己亥、巳酉丑生而柱中见庚申、申子辰生而见癸亥、亥卯未生而见甲寅、寅午戌生而见丁巳等，形同在某一行的“官位”上承受过重气势，往往在晚年表现为压力过大、职位/财产被夺等不利，需要特别留意。

- **完整对等诠释（secondary_lang_full）**：  

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_huaqi_chengju_001]` `[trigger: 一阴一阳]` `[factor_trigger: yiyin_yiyang AND fufu_zhidao]` `[role: 主干]` 甲己化土，有二则化，一不能化，仍还本位之性。所谓一不能生，生物必两。 → 《三命通会》卷十#化气成局
  - `[ns_smth_10_huaqi_chengju_002]` `[trigger: 妒化之说]` `[factor_trigger: duhua_zhishuo AND disangan_chajiang]` `[role: 主干依赖]` 是以有妒化之说。如甲己见乙，乙庚见辛。 → 《三命通会》卷十#化气成局
  - `[ns_smth_10_huaqi_chengju_003]` `[trigger: 受气临官]` `[factor_trigger: shouqi_linguan AND wannian_buji]` `[role: 条件分支]` 受气临官，长生第四位也，以干为主，双犯则应。 → 《三命通会》卷十#化气成局
  - `[ns_smth_10_huaqi_chengju_004]` `[trigger: 化而不化]` `[factor_trigger: hua_er_buhua AND tiaojian_buquan]` `[role: 总结]` 柱中见癸，并子虽强成木，不成真物，是化而不化也。 → 《三命通会》卷十#化气成局"""
    normalized_text_zh: str = """"""
    subject: str = "化气成局的时令条件、妒合与受气临官"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_化气成局的时令条件_妒合与受气临官_001_L1",
    )
    version: str = "1.0.0"
