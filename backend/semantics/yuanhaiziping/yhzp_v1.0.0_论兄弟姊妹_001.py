"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559144
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
    semantic_id="yhzp_v1.0.0_论兄弟姊妹_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论兄弟姊妹(SemanticEntry):
    """
    - **原文（source_text）**：
  比肩者，兄弟也。且如，甲见甲为兄，乙为弟妹；寅卯亦然。见庚则克兄，见辛则伤弟。甲木旺相，兄姊争财；甲乙寅卯既多，则兄弟姊妹夺财不和，争斗是非。见己合甲...
    """
    
    original_text: str = """- **原文（source_text）**：
  比肩者，兄弟也。且如，甲见甲为兄，乙为弟妹；寅卯亦然。见庚则克兄，见辛则伤弟。甲木旺相，兄姊争财；甲乙寅卯既多，则兄弟姊妹夺财不和，争斗是非。见己合甲，兄姊不正。见庚，弟妹不正。如见杀多，乙木得局，是杀合会乙木而伤甲；此兄不若弟之福，借弟之力而加恃。甲木寅月，乙木受制，主兄旺弟衰。其馀和顺不睦，但以八字休旺死绝推之，无不应验矣！

- **分字分词释义**：
  - **比肩**：与日主同类且阴阳相同者，代表兄弟姊妹中的同性（如甲见甲为兄）。
  - **甲见甲为兄乙为弟妹**：甲木日主见甲为比肩（兄），见乙为劫财（弟妹）。
  - **寅卯亦然**：地支寅卯木亦代表兄弟姊妹。
  - **见庚克兄**：七杀庚金克甲木（兄），主兄受克。
  - **见辛伤弟**：正官辛金克乙木（弟妹），主弟受伤。
  - **甲木旺相兄姊争财**：比肩旺相，主兄弟姊妹争夺财产。
  - **夺财不和争斗是非**：比劫过多，主兄弟争财不和、是非争斗。
  - **见己合甲兄姊不正**：己土合甲木（兄），主兄姊行为不正。
  - **见庚弟妹不正**：庚金合乙木（弟妹），主弟妹行为不正。
  - **杀多乙木得局**：七杀多而弟（乙木）成局得势，借弟之力。
  - **兄旺弟衰**：甲木得令则兄旺，乙木受制则弟衰。
  - **休旺死绝推之**：以五行旺衰推断兄弟姊妹的情况。

- **规范化释义（primary_lang_explained）**：
  论兄弟姊妹以比肩劫财为本。甲见甲为比肩（兄），乙为劫财（弟妹），地支寅卯亦然。见庚克兄，见辛伤弟。比肩旺相则兄姊争财，比劫过多则兄弟争财不和、是非争斗。干合不正：己合甲主兄姊不正，庚合乙主弟妹不正。杀多而劫财得局，则弟福过兄，兄反借弟之力。甲木寅月则兄旺弟衰（甲得令乙受制）。兄弟和顺与否，以八字休旺死绝推之。

- **完整对等诠释（secondary_lang_full）**：
  Siblings are analyzed through Parallel and Rob Wealth. Jia seeing Jia is Parallel (elder brother), Yi is Rob Wealth (younger siblings); Yin and Mao branches likewise. Seeing Geng harms elder brother, seeing Xin injures younger siblings. When Parallel is prosperous, elder siblings compete for wealth; when Parallel and Rob Wealth are abundant, siblings fight over wealth with discord and conflict. Improper combinations: Ji combining Jia indicates improper elder siblings; Geng combining Yi indicates improper younger siblings. When Killing is abundant but Rob Wealth achieves formation, younger sibling's fortune exceeds elder's—elder borrows younger's strength. Jia Wood in Yin month means elder thrives while younger declines (Jia gains command while Yi is suppressed). Whether siblings are harmonious or discordant is determined by analyzing the eight characters' flourishing-resting-death-extinction states, invariably accurate!

- **核心要点**：
  - 比肩为兄，劫财为弟妹
  - 见庚克兄，见辛伤弟
  - 比劫旺多主兄弟争财不和
  - 干合主兄弟姊妹不正
  - 杀多劫财得局，弟福过兄
  - 以休旺死绝推断兄弟情况

- **详细解说**：
  本条专论兄弟姊妹的命理取法。以比肩劫财代表兄弟姊妹："甲见甲为兄，乙为弟妹"——比肩（阴阳相同）为兄姊，劫财（阴阳相异）为弟妹，"寅卯亦然"——地支比劫同理。兄弟的克害以七杀正官论："见庚则克兄，见辛则伤弟"——庚金七杀克甲木（兄），辛金正官克乙木（弟妹）。比劫过多的应验是争财不和："甲木旺相，兄姊争财；甲乙寅卯既多，则兄弟姊妹夺财不和，争斗是非"。干合主不正："见己合甲，兄姊不正；见庚，弟妹不正"——己土合甲主兄姊因合而行为不端，庚金合乙主弟妹因合而行为不端。特殊情况是弟福过兄："如见杀多，乙木得局，是杀合会乙木而伤甲；此兄不若弟之福，借弟之力而加恃"——七杀多而弟（乙木）成局，杀反生弟而伤兄，兄反要借弟之力。兄弟旺衰的判断以月令为主："甲木寅月，乙木受制，主兄旺弟衰"——甲木得令则兄旺，乙木受制则弟衰。总则是"以八字休旺死绝推之，无不应验"。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_582]` `[trigger: 比肩为兄]` `[factor_trigger: parallel AND sibling]` `[role: 主干]` 比肩者，兄弟也。甲见甲为兄，乙为弟妹。 → 《渊海子平·论兄弟姊妹》
  - `[ns_yhzp_583]` `[trigger: 庚克兄辛伤弟]` `[factor_trigger: seven_killings AND direct_officer AND sibling]` `[role: 主干依赖]` 见庚则克兄，见辛则伤弟。 → 《渊海子平·论兄弟姊妹》
  - `[ns_yhzp_584]` `[trigger: 比劫争财不和]` `[factor_trigger: parallel AND rob_wealth AND direct_wealth]` `[role: 条件分支]` 甲乙寅卯既多，则兄弟姊妹夺财不和，争斗是非。 → 《渊海子平·论兄弟姊妹》
  - `[ns_yhzp_585]` `[trigger: 干合兄弟不正]` `[factor_trigger: combination AND parallel AND rob_wealth AND combination_peach_promiscuity AND ji_he_jia]` `[role: 条件分支]` 见己合甲，兄姊不正。见庚，弟妹不正。 → 《渊海子平·论兄弟姊妹》
  - `[ns_yhzp_586]` `[trigger: 弟福过兄]` `[factor_trigger: seven_killings AND rob_wealth AND di_fu_guo_xiong]` `[role: 例外处理]` 如见杀多，乙木得局，是杀合会乙木而伤甲；此兄不若弟之福。 → 《渊海子平·论兄弟姊妹》
  - `[ns_yhzp_587]` `[trigger: 兄旺弟衰]` `[factor_trigger: parallel AND month_command]` `[role: 条件分支]` 甲木寅月，乙木受制，主兄旺弟衰。 → 《渊海子平·论兄弟姊妹》
  - `[ns_yhzp_588]` `[trigger: 休旺死绝推之]` `[factor_trigger: parallel AND rob_wealth AND twelve_stages]` `[role: 总结]` 其馀和顺不睦，但以八字休旺死绝推之，无不应验矣！ → 《渊海子平·论兄弟姊妹》"""
    normalized_text_zh: str = """"""
    subject: str = "论兄弟姊妹"
    factor_refs: list = ['parallel', 'rob_wealth', 'sibling']
    
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
        l1_anchor="yhzp_v1.0.0_论兄弟姊妹_001_L1",
    )
    version: str = "1.0.0"
