"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458263
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
    semantic_id="smth_v1.0.0_暗官格与三合官局_001",
    book_id="sanming",
    engine_id="bazi"
)
class 暗官格与三合官局(SemanticEntry):
    """
    - **原文（source_text）**：
  经云：三合若是遇贵禄，平生多财谷。如乙巳、乙丑、乙巳、辛巳，乙为日主，用庚为贵，天干无庚，却巳酉丑三合官局，故为三合遇贵，又名暗官格。

- 分字分词...
    """
    
    original_text: str = """- **原文（source_text）**：
  经云：三合若是遇贵禄，平生多财谷。如乙巳、乙丑、乙巳、辛巳，乙为日主，用庚为贵，天干无庚，却巳酉丑三合官局，故为三合遇贵，又名暗官格。

- 分字分词释义：
  - **三合**：如巳酉丑、申子辰、亥卯未等三支合成一局，此处指巳酉丑三合金局。
  - **遇贵禄**：三合局中包含贵人、官星或禄位，使合局所成的五行既为官星，又得禄地。
  - **暗官格**：天干上不见官星，而地支合成官局，官星之力潜藏于支中，故名暗官。
  - **乙为日主，用庚为贵**：乙木以庚金为正官，例中虽天干无庚，然地支巳酉丑合成金局，等同有庚官在局中。

- **规范化释义（primary_lang_explained）**：
  三合遇贵，是指命局地支合成官局，并在其中兼具贵人、禄位，使命主一生多得财谷与贵气。例中乙日生人，以庚金为官；原局天干不见庚金，但地支有巳、酉、丑三支合成金局，于是官星虽不显于干，却隐于支中，故名暗官格。此类命局往往在表面上不见显赫官星，却在实际运势中屡得权贵提携、暗中得力。

- **完整对等诠释（secondary_lang_full）**：
  The saying that 'when a three-harmony combination meets nobles and salary, a person will have grain and wealth throughout life' refers to cases where the branches join into an official bureau that also carries noble and salary positions. In the example with Yi day and branches Si, You and Chou, Yi wood takes Geng metal as its proper official. Although no Geng metal appears on the stems, the three branches Si–You–Chou combine into a full metal structure, so the power of the official star is hidden in the earth rather than openly shown above. Because the official is concealed within a three-harmony combination yet still brings nobility and pay, this is called 'Three-Harmony Meets Nobles' and also known as the Hidden Official pattern.


- 核心要点：
  - 三合遇贵的关键在于**地支三合成官局**，且局中兼具贵人、禄位，而天干官星可显可隐。
  - 暗官格多主贵人相扶、机会暗合，非靠显赫出身或明面权力，而是在关键时刻得助力。
  - 忌三合局受冲破，或局中五行不为日主之官，便失其贵格之本意。

- 详细解说：
  与岁德正官、天元作禄等"明官"格不同，三合遇贵强调的是地支结构的潜在力量。天干上不见官星，表面看似无官贵之象，但地支却通过三合形成一个完整的官局，使官星之力隐藏在命局根基之中。这种结构在实际人生中往往表现为：早年并不显眼，但在关键转折点，会因环境合局、人物配合而突然获得提拔与转机。
  
  然而，暗官之贵也较易受环境影响：一旦三合局遭到冲破或分离，如流年、大运冲散其中一支，则官局之力大减，原本的机遇可能化为寻常，甚至引发官非是非。因此，在分析此格时，需特别留意行运对三合局的冲、合、刑等作用。

- 校勘与字词辨析：
  - 原文"乙巳、乙丑、乙巳、辛巳"一串支名疑有讹脱，现代整理时多参照其他命例，将其视作以巳、酉、丑三支成局的示意，重在说明巳酉丑三合官局之理，而非拘泥具体排列。
  - **"暗官格"**一名，后世命书多有引用，专指天干不见官而支中成官局之类格局，与明显透官者相对。
  - **English**：
    - Similar patterns; contrasted with openly revealed officials.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_032]` `[trigger: 三合遇贵]` `[factor_trigger: sanhe_yugui_presence]` `[role: 主干]` 三合若是遇贵禄，平生多财谷。 → 《三命通会》卷五#三合遇贵
  - `[ns_smth_05_033]` `[trigger: 暗官格]` `[factor_trigger: anguan_pattern AND sanhe_guanju]` `[role: 主干依赖]` 天干无庚，却巳酉丑三合官局，故为三合遇贵，又名暗官格。 → 《三命通会》卷五#三合遇贵
  - `[ns_smth_05_034]` `[trigger: 潜在力量]` `[factor_trigger: di_zhi_qianli AND guan_yin_genji]` `[role: 条件分支]` 表面看似无官贵之象，但地支却通过三合形成一个完整的官局。 → 《三命通会》卷五#三合遇贵
  - `[ns_smth_05_035]` `[trigger: 暗中转机]` `[factor_trigger: guanjian_zhuanzhe AND anzhong_zhuli]` `[role: 总结]` 在关键转折点，会因环境合局、人物配合而突然获得提拔与转机。 → 《三命通会》卷五#三合遇贵"""
    normalized_text_zh: str = """"""
    subject: str = "暗官格与三合官局"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'sanhe_yugui_anguan_presence', 'bazi_semantic', 'sanhe_ju_config', 'bazi_semantic', 'guanxing_xianyin_score', 'bazi_semantic', 'anhe_jiyu_score', 'bazi_semantic', 'sanhe_wengu_condition', 'bazi_semantic', 'huanjing_yingxiang_risk', 'bazi_semantic', 'source_ref', 'rel_smth_05_025', 'sanhe_yugui_anguan_presence', 'rel_smth_05_026', 'guanxing_xianyin_score', 'rel_smth_05_027', 'huanjing_yingxiang_risk', 'evi_smth_05_025', 'sanhe_ju_config', 'rule_anguan', 'evi_smth_05_026', 'guanxing_xianyin_score', 'rule_xianyin', 'evi_smth_05_027', 'anhe_jiyu_score', 'rule_caiku', 'map_smth_05_017', 'map_smth_05_018']
    
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
        l1_anchor="smth_v1.0.0_暗官格与三合官局_001_L1",
    )
    version: str = "1.0.0"
