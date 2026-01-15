"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597044
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
    semantic_id="qtbj_v1.0.0_1__十月戊土_亥月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1十月戊土亥月(SemanticEntry):
    """
    - **原文（source_text）**：
  十月戊土，时值小阳春，阳气略出，先用甲木，次用丙火。非甲土不灵，非丙土不暖，安能生物？甲丙两出，富贵中人。
  或甲得长生而水有根，又得一丙高透，亦主...
    """
    
    original_text: str = """- **原文（source_text）**：
  十月戊土，时值小阳春，阳气略出，先用甲木，次用丙火。非甲土不灵，非丙土不暖，安能生物？甲丙两出，富贵中人。
  或甲得长生而水有根，又得一丙高透，亦主贵名扬。
  若支见庚金，不过秀才之分。不见庚金，甲藏丙透，科甲可期。有庚又见丁透制之，多为典吏之流，异路功名。庚丁不透，而甲丙俱藏，亦主富贵。
  壬透而戊能救丙者，富中取贵。丙甲俱无，必为僧道。

- **分字分词释义**：
  - **小阳春**：十月阳气略回、似春之暖 / 亥月特点 / 调候背景
  - **土灵**：土气灵动、不死滞 / 甲木疏土 / 用神效用
  - **土暖**：土气温暖、能生物 / 丙火照暖 / 调候作用
  - **安能生物**：怎能生养万物 / 反问句 / 强调甲丙必须
  - **甲得长生**：甲木在亥宫长生 / 旺相 / 增强用神
  - **高透**：透于年时高位 / 位置贵重 / 格局提升
  - **典吏**：地方小吏 / 异路功名 / 次等格局

- **完整对等诠释（secondary_lang_full）**：
  Wu Earth in the 10th Month (Pig Month): Time of "Little Spring"; Yang Qi slightly emerges. First use Jia, then Bing. Without Jia, Earth is not active; without Bing, Earth is not warm; how can it generate things? If Jia and Bing are both revealed, one is a wealthy and noble person.
  If Jia gets Birth (in Hai) and meets Water grounded in branches, with one Bing highly revealed, it also implies nobility and fame.
  If branches see Geng Metal, merely a Xiucai. If Geng is not seen, Jia hidden, and Bing revealed, Civil Service is likely. If Geng is present and Ding reveals to control it, implies alternative fame or being a petty official. Even if Geng/Ding are not revealed, with Jia/Bing hidden, it is still called wealth and nobility.
  If Ren reveals and Wu saves Bing, it implies obtaining nobility amidst wealth. Without Bing/Jia, one must be a monk/Taoist.

- **核心要点**：
  - **小阳春**：十月有阳气，故甲丙并用。
  - **甲丙两出**：最佳配置，土灵且暖。
  - **忌庚**：庚金制甲（食神制杀），反坏了甲木疏土之功（亥月甲木长生，杀印相生为贵，制杀反小气）。
  - **救应**：壬多用戊。

- **详细解说**：
  - 亥月戊土绝地，财星（壬）当令。
  - 此时最喜甲木（七杀），因亥中甲木长生，杀印相生（水生木，木生火，火生土）。
  - 丙火是必须的，调候暖局。
  - “非甲土不灵”：指戊土本性厚重，需木疏通才有用。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_539]` `[trigger: 亥月戊土小阳春]` `[factor_trigger: month_hai AND tiangan_wu AND tiangan_jia AND tiangan_bing AND little_yang]` `[role: 主干]` 亥月戊土，小阳春之象，先用甲木使土灵，次用丙火使土暖。 → 《穷通宝鉴·三冬戊土》#24.1
  - `[ns_qttbj_540]` `[trigger: 甲丙两透富贵之人]` `[factor_trigger: month_hai AND tiangan_wu AND tiangan_jia AND tiangan_bing AND wealth_noble]` `[role: 条件分支]` 甲丙两出，土灵且暖，主富贵之人。 → 《穷通宝鉴·三冬戊土》#24.1
  - `[ns_qttbj_541]` `[trigger: 甲长生水有根丙高透贵名扬]` `[factor_trigger: month_hai AND tiangan_wu AND tiangan_jia AND dizhi_hai AND element_water_rooted AND bing_high]` `[role: 条件分支]` 甲得长生而水有根，又得一丙高透，亦主贵名扬。 → 《穷通宝鉴·三冬戊土》#24.1
  - `[ns_qttbj_542]` `[trigger: 支见庚仅秀才]` `[factor_trigger: month_hai AND tiangan_wu AND (tiangan_geng OR dizhi_geng) AND only_xiucai]` `[role: 条件分支]` 若支见庚金，不过秀才之分。 → 《穷通宝鉴·三冬戊土》#24.1
  - `[ns_qttbj_543]` `[trigger: 无庚甲藏丙透科甲]` `[factor_trigger: month_hai AND tiangan_wu AND bing_revealed AND jia_in_branch AND NOT tiangan_geng AND kejia_scholar]` `[role: 条件分支]` 不见庚金，甲藏丙透，科甲可期。 → 《穷通宝鉴·三冬戊土》#24.1
  - `[ns_qttbj_544]` `[trigger: 有庚丁透典吏异路功名]` `[factor_trigger: month_hai AND tiangan_wu AND tiangan_geng AND tiangan_ding AND clerk_official]` `[role: 条件分支]` 有庚又见丁透制之，多为典吏之流，异路功名。 → 《穷通宝鉴·三冬戊土》#24.1
  - `[ns_qttbj_545]` `[trigger: 甲丙俱藏亦主富贵]` `[factor_trigger: month_hai AND tiangan_wu AND jia_in_branch AND bing_in_branch AND NOT tiangan_geng AND wealth_noble]` `[role: 条件分支]` 庚丁不透，而甲丙俱藏，亦主富贵。 → 《穷通宝鉴·三冬戊土》#24.1
  - `[ns_qttbj_546]` `[trigger: 壬透戊救丙富中取贵]` `[factor_trigger: month_hai AND tiangan_wu AND tiangan_ren AND likes_bing_unfreeze AND wu_protects_bing]` `[role: 条件分支]` 壬透而戊能救丙者，富中取贵。 → 《穷通宝鉴·三冬戊土》#24.1
  - `[ns_qttbj_547]` `[trigger: 甲丙全无僧道孤寒]` `[factor_trigger: month_hai AND tiangan_wu AND NOT tiangan_jia AND NOT tiangan_bing AND monk_poor]` `[role: 例外处理]` 丙甲俱无，土寒不灵，多作僧道孤寒之命。 → 《穷通宝鉴·三冬戊土》#24.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 十月戊土（亥月）"
    factor_refs: list = ['little_yang', 'clerk_official']
    
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
        l1_anchor="qtbj_v1.0.0_1__十月戊土_亥月_001_L1",
    )
    version: str = "1.0.0"
