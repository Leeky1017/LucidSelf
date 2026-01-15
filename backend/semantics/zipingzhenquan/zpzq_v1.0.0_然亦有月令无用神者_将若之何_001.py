"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523922
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
    semantic_id="zpzq_v1.0.0_然亦有月令无用神者_将若之何_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 然亦有月令无用神者将若之何(SemanticEntry):
    """
    - **原文（source_text）**：
  然亦有月令无用神者，将若之何？如木生寅卯，日与月同，本身不可为用，必看四柱有无财官煞食透干会支，另取用神；然终以月令为主，然后寻用，是建禄月劫之格，非...
    """
    
    original_text: str = """- **原文（source_text）**：
  然亦有月令无用神者，将若之何？如木生寅卯，日与月同，本身不可为用，必看四柱有无财官煞食透干会支，另取用神；然终以月令为主，然后寻用，是建禄月劫之格，非用而即用神也。

- 原注（原文注解）：
  　　本段讨论“建禄、月劫”等特殊格局：
  - 日主与月令同类时，月令本身不能再为用神；
  - 需另在四柱中找财官煞食为用，但仍以月令为大环境；
  - 建禄、月劫等格局，是“非用而即用神”的特殊情形。

- 分字分词释义：
  - 月令无用神：月令本身不宜直接作为用神。
  - 日与月同：日干与月令为同一五行或同一类，比劫临月令。

- **规范化释义（primary_lang_explained）**：
  然而也有月令本身无法作为用神的情况，那该怎么办？比如木日主生于寅卯月，日干与月令同属木，月令本身不能再作为用神。此时必须查看四柱中是否有财官煞食透干或会支，另行取用。但始终要以月令为主导大环境，然后在此基础上寻找用神。这就是建禄格、月劫格的情形——月令本身"非用"（不直接为用神），但用神仍须围绕月令展开。

- **完整对等诠释（secondary_lang_full）**：
  However, there are cases where the Month Branch itself cannot serve as the Useful God—what should be done then? For example, when a Wood Day Master is born in the Yin or Mao month, the Day Stem and Month Branch both belong to Wood, so the Month Branch itself cannot be used as the Useful God. In such cases, one must examine whether Wealth, Officer, Killing, or Food stars appear as revealed stems or branch combinations elsewhere in the Four Pillars, and select the Useful God from among them. Yet the Month Branch always remains the dominant environmental context, and only after acknowledging this does one seek the Useful God. This is the situation of the Build-Lu (Jianlu) or Month-Robbing (Yuejie) patterns—the Month Branch is "not used" (not directly the Useful God), but the Useful God must still be determined in relation to the Month Branch.

- 核心要点：
  - 建禄、月劫：日主与月令同类时，月令不再直接为用，需另取财官煞食为用；
  - 然而“终以月令为主，然后寻用”，不可以用神替代提纲。

- **详细解说**：
  月令为取用之提纲，但并非所有月令都能直接成格。若月令所透之神无力、或与日主无情义相承，则需另寻他处取用。此时可看时支、日支、年支中是否有可用之神，或透干之神是否足以成格。关键在于"格局可成"与"用神有力"二者兼备，而非死守月令不放。这是"活看"命局的重要原则。

- 应用推演：
  1) 遇到建禄、月劫格，先确认日干与月令是否同类；
  2) 在四柱中另寻财官煞食透干会支，以这些为用；
  3) 在判断岁运时，仍以月令为大气候，观察所行之运与建禄月劫的互动；
  4) 注意建禄、月劫格在实务中往往与“身强、比劫旺”有关，取用特别依赖财官食伤之调节。

- 反例与边界：
  - 误把建禄月劫当成普通官格、财格、印格来用神，不看日月同类之特性。

- 小例（示意）：
  - 甲寅日生寅月，身旺建禄，四柱透财官、通关得宜，则为建禄用官之贵格；若只按官格看而忽略“身旺建禄”的特殊结构，易误取用神。

- 校勘与字词辨析：
  - “是建禄月劫之格，非用而即用神也”：本精校将其释为“月令本身不作为直接用神，但用神仍围绕月令展开”，以免误解为“月劫一定为用神”。"""
    normalized_text_zh: str = """"""
    subject: str = "然亦有月令无用神者，将若之何？"
    factor_refs: list = ['yueling_wuyongshen', 'jianlu_ge', 'yuejie_ge', 'feiyong_jiyongshen']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_然亦有月令无用神者_将若之何_001_L1",
    )
    version: str = "1.0.0"
