"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620045
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
    semantic_id="qtbj_v1.0.0_4__三月乙木_辰月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 4三月乙木辰月(SemanticEntry):
    """
    - **原文（source_text）**：
  三月乙木，阳气愈炽，先癸后丙。
  癸丙两透，不见己庚，玉堂之客。见己庚者，平常之人。
  或一乙逢庚，不见己者，亦主小富贵，但不显达。或多水见己，只...
    """
    
    original_text: str = """- **原文（source_text）**：
  三月乙木，阳气愈炽，先癸后丙。
  癸丙两透，不见己庚，玉堂之客。见己庚者，平常之人。
  或一乙逢庚，不见己者，亦主小富贵，但不显达。或多水见己，只恐高才不第。见戊堪发异途。或庚己混杂，丙癸全，则为下格。
  或见水局，丙戊高透，亦主科甲。或柱中全无丙戊，支合水局，此离乡之命。
  或见一派癸水，又有辛金，则作旺看。得一戊己制癸，亦可云小富贵。若一派壬水，不特贫贱，而且夭折。有一戊己，方云有寿，但终为技术之人。
  又或庚辰时月，名二庚争合，乃贫贱之辈。如年干见丁破庚，可云从化，亦不失武职之权。

- **分字分词释义**：
  - **阳气愈炽**：阳气更加炽热 / 辰月特征 / 土燥
  - **先癸后丙**：先用癸水后用丙火 / 用神次序 / 润燥
  - **玉堂之客**：翰林院的贵客 / 清贵 / 癸丙透无己庚
  - **高才不第**：才高却考不中 / 己混癸 / 凶象
  - **离乡之命**：离开家乡的命 / 水局无丙戊 / 漂泊
  - **二庚争合**：两个庚金争着合乙 / 贫贱 / 情意不专
  - **技术之人**：从事技术的人 / 中下等 / 壬多戊制

- **规范化释义（primary_lang_explained）**：
  三月（辰月）的乙木，阳气更加炽热，先用癸水（润燥），后用丙火（泄秀）。
  癸水和丙火都透出，且不见己土（克癸）和庚金（合乙），是玉堂（翰林院）的清贵之客。如果见到己土庚金，只是平常人。
  如果一个乙木遇到庚金（合），不见己土，也主小富贵，但不显达（因合而羁绊）。如果水多而见到己土（混杂），恐怕才高而考不中。如果见到戊土（制水），可以异途发达。如果庚金己土混杂，即使丙癸全备，也是下等格局。
  如果地支合成水局，丙火戊土高透（戊止水，丙暖局），也主科甲。如果柱中全无丙戊，地支合成水局，这是离乡背井的命（水泛浮萍）。
  如果见到一派癸水，又有辛金（杀印相生），则当作身旺看。得一个戊己土制癸水，也可以说小富贵。如果是一派壬水，不只贫贱，而且夭折（水大木漂）。有一个戊己土，才可以说有寿，但终究是搞技术的人。
  又或者生于庚辰月或庚辰时，叫“二庚争合”（争合乙木），是贫贱之辈。如果年干见到丁火破庚金，可以按“化气格”论（或强行制杀留官），也不失武职的权力。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood in the 3rd Month (Dragon Month): Yang Qi becomes more blazing; first use Gui, then Bing.
  If Gui and Bing are both revealed, and Ji/Geng are not seen, one is a guest of the Jade Hall (Hanlin Academy). If Ji/Geng are seen, one is an ordinary person.
  If one Yi meets Geng without Ji, it implies small wealth and nobility, but not prominence. If there is much Water and Ji appears, one fears having high talent but failing exams. Seeing Wu Earth allows success via alternative paths. If Geng and Ji are mixed, even with Bing/Gui present, it is a lower pattern.
  If a Water Frame appears, and Bing/Wu are highly revealed, it also implies Civil Service. If there is absolutely no Bing/Wu and a Water Frame exists, it is a life of leaving one's hometown.
  If a mass of Gui Water and Xin Metal appears, view it as Prosperous. Obtaining one Wu/Ji to control Gui can imply small wealth and nobility. If there is a mass of Ren Water, it means not only poverty but premature death. Having one Wu/Ji implies longevity, but one remains a technician.
  Or if Geng-Chen Month/Hour appears, it is "Two Gengs Competing to Combine", denoting a poor and lowly class. If Ding Fire appears on the Year Stem to break Geng, it can be discussed as Transformation or control, not losing military authority.

- **核心要点**：
  - **先癸后丙**：辰月土燥，先润后暄。
  - **忌己庚**：己混壬癸，庚合乙木，皆破格。
  - **二庚争合**：贫贱。
  - **水多之患**：水局无丙戊，离乡/夭折。

- **详细解说**：
  辰月是季春，木气已竭。
  - “玉堂之客”：丙癸无伤，水火既济，文采斐然。
  - “离乡之命”：水多木漂，乙木如浮萍。
  - “二庚争合”：乙木最怕二庚争合，情意不专，或者是被金所伤。此时丁火破庚，或许能解救，或成“化杀”格。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_180]` `[trigger: 辰月乙木]` `[factor_trigger: month_chen AND tiangan_yi AND gui_revealed AND bing_revealed AND NOT tiangan_ji AND NOT tiangan_geng]` `[role: 主干]` 三月乙木，阳气愈炽，先癸后丙，癸丙两透，不见己庚，玉堂之客。 → 《穷通宝鉴·三春乙木》#7.4
  - `[ns_qttbj_181]` `[trigger: 离乡之命]` `[factor_trigger: month_chen AND tiangan_yi AND dizhi_water_frame AND NOT tiangan_bing AND NOT tiangan_wu]` `[role: 例外处理]` 柱中全无丙戊，支合水局，此离乡之命。 → 《穷通宝鉴·三春乙木》#7.4
  - `[ns_qttbj_182]` `[trigger: 二庚争合]` `[factor_trigger: tiangan_yi AND geng_multiple AND two_gengs_competing]` `[role: 例外处理]` 庚辰时月，名二庚争合，乃贫贱之辈。 → 《穷通宝鉴·三春乙木》#7.4
  - `[ns_qttbj_183]` `[trigger: 壬多夭折]` `[factor_trigger: month_chen AND tiangan_yi AND ren_excessive AND NOT (tiangan_wu OR tiangan_ji)]` `[role: 例外处理]` 若一派壬水，不特贫贱，而且夭折。有一戊己，方云有寿，但终为技术之人。 → 《穷通宝鉴·三春乙木》#7.4"""
    normalized_text_zh: str = """"""
    subject: str = "4. 三月乙木（辰月）"
    factor_refs: list = ['guest_jade_hall', 'two_gengs_competing', 'leaving_hometown']
    
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
        l1_anchor="qtbj_v1.0.0_4__三月乙木_辰月_001_L1",
    )
    version: str = "1.0.0"
