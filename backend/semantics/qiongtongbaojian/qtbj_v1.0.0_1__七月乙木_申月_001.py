"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620085
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
    semantic_id="qtbj_v1.0.0_1__七月乙木_申月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1七月乙木申月(SemanticEntry):
    """
    - **原文（source_text）**：
  三秋乙木，金神司令，先丙后癸，惟九月耑用癸水，恐丙暖戊土为病也。

  七月乙木，庚金乘令，庚虽输情于乙妹，怎奈干乙难合支金。柱见庚多，乙难受载。
 ...
    """
    
    original_text: str = """- **原文（source_text）**：
  三秋乙木，金神司令，先丙后癸，惟九月耑用癸水，恐丙暖戊土为病也。

  七月乙木，庚金乘令，庚虽输情于乙妹，怎奈干乙难合支金。柱见庚多，乙难受载。
  或丙透干，又加己出埋金，此格可云科甲。有己透、加丙，亦是上命。七月喜己土为用，或不见丙癸，己土必不可少，此则以火为妻，土为子。
  或癸透、丙藏、庚少，此不用己，可许贡拔。无丙、有癸透者，不失刀笔门户。有支下庚多，癸又藏者，无丙己二神，平常人物。
  或生辰时，此为从化，反主富贵。凡化合格皆以所生之神为用。化金者，戊为用神，特忌丙丁煅炼破格。

- **分字分词释义**：
  - **金神司令**：金神当令主事 / 秋季特征 / 金旺
  - **输情于乙妹**：输送感情给乙木妹妹 / 乙庚合 / 有情
  - **干乙难合支金**：天干的乙难合住地支的金 / 合而不化 / 力弱
  - **乙难受载**：乙木难以承受 / 庚多 / 身弱
  - **埋金**：掩埋金气 / 己土功能 / 争议
  - **己土为用**：以己土为用神 / 七月特殊 / 培木
  - **从化**：从属化气格 / 乙庚化金 / 变格
  - **煅炼破格**：锻炼破坏格局 / 丙丁忌 / 火克金

- **规范化释义（primary_lang_explained）**：
  秋季三个月的乙木，金神司令（金旺），先用丙火（制金暖木），后用癸水（泄金润木）。只有九月（戌月）专门用癸水，恐怕丙火温暖戊土（燥土）反而成病。

  七月（申月）乙木，庚金当令，庚金虽然对乙木妹妹有情（乙庚合），但天干的乙木很难合住地支的庚金。如果柱中庚金多，乙木难以承受（克身太过）。
  如果丙火透干（制杀），又加上己土透出埋金（生金？此处疑为混局或生官），此格可以说是科甲。有己土透出，加上丙火，也是上等命。七月喜欢用己土（培木生金），或者不见丙癸时，己土必不可少。
  如果癸水透出、丙火藏支、庚金少，此时不用己土，可以许诺贡拔（推荐入仕）。没有丙火、只有癸水透出的人，也不失为刀笔吏的门户。如果地支下庚金多，癸水又藏，没有丙己二神，是平常人物。
  如果生于庚辰时，这是“从化格”（化金），反而主富贵。凡是化合格都以“化神所生之神”（土生金）为用神（即用戊土）。化金格，戊土为用，特别忌讳丙丁火煅炼破格。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood in the Three Autumn Months: Metal God commands; first use Bing, then Gui. Only in the 9th Month, use Gui exclusively, fearing Bing might warm the Wu Earth and cause disease.

  In the 7th Month (Monkey), Geng Metal takes charge. Although Geng has affection for Sister Yi, Stem Yi cannot easily combine with Branch Metal. If Geng is numerous, Yi cannot bear the burden.
  If Bing is revealed, and Ji appears to bury Metal, this pattern implies Civil Service. Having Ji revealed plus Bing is also a superior life. The 7th Month likes Ji Earth as Useful God; or if Bing/Gui are not seen, Ji Earth is indispensable.
  If Gui is revealed, Bing hidden, and Geng scarce, do not use Ji; this allows for Tribute selection. Without Bing but with Gui revealed, one remains in the class of clerks. If Geng is abundant in branches and Gui is hidden, without Bing/Ji, one is ordinary.
  If born in Geng-Chen Hour, it is "Follow Transformation" (Transform to Metal), implying wealth and nobility. All Transformation patterns take the element that generates the Transformed Spirit as the Useful God. For Transforming into Metal, Wu Earth is the Useful God; it specifically dreads Bing/丁 Fire refining and breaking the pattern.

- **核心要点**：
  - **乙庚合**：申月庚旺，乙木若弱，喜从化（化金）。
  - **不化**：若不化，喜丙火制杀，或癸水化杀。
  - **己土之用**：七月乙木喜己土（湿土生金或培木），不同于其他月。
  - **化气格**：乙庚化金，喜土生，忌火克。

- **详细解说**：
  申月是乙木死绝之地。
  - "输情于乙妹"：指乙庚相合有情，不作七杀无情论。
  - 化气格在此月最易成。若化金，则金为体，土（印）为用，火（官杀）为忌。
  - 若不化，则视为身弱杀重，需丙火制杀或癸水化杀。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_195]` `[trigger: 三秋乙木]` `[factor_trigger: season_autumn AND tiangan_yi AND tiangan_bing AND tiangan_gui]` `[role: 主干]` 三秋乙木，金神司令，先丙后癸，惟九月耑用癸水。 → 《穷通宝鉴·三秋乙木》#9.1
  - `[ns_qttbj_196]` `[trigger: 乙庚合]` `[factor_trigger: month_shen AND tiangan_yi AND tiangan_geng AND yi_geng_combine]` `[role: 主干依赖]` 庚虽输情于乙妹，怎奈干乙难合支金，柱见庚多，乙难受载。 → 《穷通宝鉴·三秋乙木》#9.1
  - `[ns_qttbj_197]` `[trigger: 化金格]` `[factor_trigger: month_shen AND tiangan_yi AND tiangan_geng AND dizhi_chen AND pattern_transform_metal]` `[role: 条件分支]` 生辰时，此为从化，反主富贵。化金者，戊为用神，特忌丙丁煅炼破格。 → 《穷通宝鉴·三秋乙木》#9.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 七月乙木（申月）"
    factor_refs: list = ['conveying_affection', 'burying_metal', 'pattern_transform_metal']
    
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
        l1_anchor="qtbj_v1.0.0_1__七月乙木_申月_001_L1",
    )
    version: str = "1.0.0"
