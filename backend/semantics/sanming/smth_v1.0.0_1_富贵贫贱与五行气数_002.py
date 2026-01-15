"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.081200
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
    semantic_id="smth_v1.0.0_1_富贵贫贱与五行气数_002",
    book_id="sanming",
    engine_id="bazi"
)
class 1富贵贫贱与五行气数(SemanticEntry):
    """
    - 原文（source_text）：
  人生有命，得失顿殊；富贵贫贱，那能一体。
  红光满室，五行都聚于贵乡；佳气充庐，四柱并集于福地。
  先贫后富，生时值禄马同乡；始吉终凶，日时犯空破之处。
...
    """
    
    original_text: str = """- 原文（source_text）：
  人生有命，得失顿殊；富贵贫贱，那能一体。
  红光满室，五行都聚于贵乡；佳气充庐，四柱并集于福地。
  先贫后富，生时值禄马同乡；始吉终凶，日时犯空破之处。
  平生坎坷，基薄与凶运交杂；一世荣华，命高逢好运叠至。
  刚金遇火方成器，决定超群；旺火得水为既济，必然出众。
  木须金而不繁，水赖土而不散。
  戊己见寅卯，得位于勾陈；壬癸坐巳午，当权于元武。
  贵神入命，遇奇仪必是公卿；华盖临时，值孤寡定为僧道。
  玉堂拜相，炎炎火秀在离宫；金阙朝元，洋洋水德宅坎位。
  重逢水位，断为云水之仙；累犯纯阳，定作空门之子。
  遇长生而聪明智慧，逢死败而蒙蠢愚顽。
  父母难靠，年月俱陷空亡；妻子易亏，日时并临孤寡。

- 分字分词释义：
  - **禄马同乡**：壬午、癸巳等。
  - **奇仪**：三奇六仪（遁甲术语，此处指三奇贵人）。
  - **勾陈得位**：土生木月（寅卯），官煞得地。
  - **元武当权**：水生火月（巳午），财官得地。
  - **火秀离宫**：火得地（午）。
  - **水德坎位**：水得地（子）。

- **规范化释义（primary_lang_explained）**：
  富贵贫贱，命各不同。五行聚于贵地（财官印食），红光满室。
  生时遇禄马同乡，先贫后富（晚景好）。日时犯空亡破败，始吉终凶。
  命局基础薄弱又行凶运，坎坷一生。命格高强又逢好运，一世荣华。
  金旺遇火成器，火旺遇水既济，木盛见金不繁（成材），水旺见土不散（归库）。
  土（戊己）生寅卯月（官煞），勾陈得位。水（壬癸）生巳午月（财官），元武当权。
  命带贵神奇仪，公卿之命。带华盖孤寡，僧道之命。
  火在离宫（午），文明之象。水在坎位（子），润下之象。
  水多（重逢水位），云水之仙（道士）。纯阳（干支皆阳），空门之子（僧侣）。
  坐长生聪明，坐死败愚顽。
  年月空亡，父母难靠。日时孤寡，妻子受损。

- 核心要点：
  - **五行成器**：金火、水火、木金、水土。
  - **神煞定业**：奇仪公卿，华盖僧道。
  - **六亲**：空亡孤寡。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_045]` `[trigger: 红光满室]` `[factor_trigger: hongguang_manshi AND wuxing_jugugui]` `[role: 主干]` 人生有命，得失顿殊；富贵贫贱，那能一体。红光满室，五行都聚于贵乡。 → 《三命通会》卷十二#富贵贫贱与五行气数
  - `[ns_smth_12_046]` `[trigger: 禄马同乡]` `[factor_trigger: luma_tongxiang AND xianpin_houfu]` `[role: 主干依赖]` 先贫后富，生时值禄马同乡；始吉终凶，日时犯空破之处。 → 《三命通会》卷十二#富贵贫贱与五行气数
  - `[ns_smth_12_047]` `[trigger: 勾陈元武]` `[factor_trigger: gouchen_dewei AND xuanwu_dangquan]` `[role: 条件分支]` 勾陈得位而官职荣升，元武当权而财官两全。 → 《三命通会》卷十二#富贵贫贱与五行气数
  - `[ns_smth_12_048]` `[trigger: 云水之仙]` `[factor_trigger: yunshui_zhixian AND kongmen_zhizi]` `[role: 总结]` 重逢水位，断为云水之仙；累犯纯阳，定作空门之子。 → 《三命通会》卷十二#富贵贫贱与五行气数"""
    normalized_text_zh: str = """"""
    subject: str = "1 富贵贫贱与五行气数"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_state_factor_101', 'bazi_semantic', 'bazi_state_factor_102', 'bazi_semantic', 'bazi_relation_metal_fire', 'bazi_semantic', 'bazi_state_factor_62', 'bazi_semantic', 'bazi_relation_factor_49', 'bazi_semantic', 'bazi_condition_factor_28', 'bazi_semantic', 'source_ref', 'rel_smth_12_040', 'core_factor', 'rel_smth_12_041', 'cond_factor', 'rel_smth_12_042', 'risk_factor', 'evi_smth_12_040', 'core_factor', 'rule_name40', 'evi_smth_12_041', 'cond_factor', 'rule_name41', 'evi_smth_12_042', 'risk_factor', 'rule_name42', 'map_smth_12_027', 'map_smth_12_028']
    
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
        l1_anchor="smth_v1.0.0_1_富贵贫贱与五行气数_002_L1",
    )
    version: str = "1.0.0"
