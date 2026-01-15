"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264080
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
    semantic_id="smth_v1.0.0_看命总纲与月令提纲_001",
    book_id="sanming",
    engine_id="bazi"
)
class 看命总纲与月令提纲(SemanticEntry):
    """
    - 原文（source_text）：
  大凡看命，先看月支有无财官，方看其他。月令为命也。月取支神，年取天干，日取天干，流岁取天干，大运取支神。年为本，日为主。
  如月有正官及偏官，而时又入他格，...
    """
    
    original_text: str = """- 原文（source_text）：
  大凡看命，先看月支有无财官，方看其他。月令为命也。月取支神，年取天干，日取天干，流岁取天干，大运取支神。年为本，日为主。
  如月有正官及偏官，而时又入他格，只以月中取，他格无用。如月令全无可用，方看他格。古歌云：“三宫带格混难详，不晓凭谁是贵方。一任三宫皆带格，除非只得用提纲”是也。
  月令用地支，假如官星，须要上下干支透出为妙。或干透出，支中不透，主聪俊。忌年与时冲月支，日支自冲不妨。大运及岁君来冲月支，则祸。

- 分字分词释义：
  - **月令为命**：月支（提纲）是命局的核心，决定五行旺衰和格局高低。
  - **年本日主**：年柱为根基（本），日柱为自身（主）。
  - **透出**：天干透出，地支通根，为有力。
  - **冲月支**：月令提纲最怕刑冲，冲则根基动摇。

- **规范化释义（primary_lang_explained）**：
  看命的方法，首先要看月令地支中是否藏有财星或官星，然后再看其他干支。月令是命局的纲领。取格时，月令取地支，年、日、流年取天干，大运重地支。年是根本，日是命主。
  如果月令中有正官或偏官，即使时柱或其他柱成了别的格局，也应先以月令格局为主，其他格局暂不取用。只有当月令中全无财官印食等可用之物时，才看其他干支是否成格。古歌说：如果年月日时三宫都带格局，很难分辨哪个是贵气所在；不管有多少格局，首先必须看月令提纲。
  月令取用神重在地支，如果取官星，最好天干透出，地支有根。如果只透天干而地支无根，主聪明俊秀，但福气较薄。最忌年支或时支冲克月令，日支自冲（如日坐财库）有时不妨。但大运和流年来冲月令，则主有祸。

- 核心要点：
  - **提纲为重**：月令是八字格局的首要依据。
  - **透干通根**：用神需干透支藏，方为有力。
  - **忌冲提纲**：月令受冲，格局大损。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_001]` `[trigger: 月令为命]` `[factor_trigger: yuelingweiming AND tigang_weizhong]` `[role: 主干]` 大凡看命，先看月支有无财官，方看其他。月令为命也。 → 《三命通会》卷十#看命总纲与月令提纲
  - `[ns_smth_10_002]` `[trigger: 三宫带格]` `[factor_trigger: sangong_daige AND yong_tigang]` `[role: 主干依赖]` 一任三宫皆带格，除非只得用提纲。 → 《三命通会》卷十#看命总纲与月令提纲
  - `[ns_smth_10_003]` `[trigger: 透出为妙]` `[factor_trigger: touchu_weimiao AND zhijun_bugui]` `[role: 条件分支]` 月令用地支，假如官星，须要上下干支透出为妙。 → 《三命通会》卷十#看命总纲与月令提纲
  - `[ns_smth_10_004]` `[trigger: 冲月支祸]` `[factor_trigger: chong_yuezhi_huo AND dayun_suijun]` `[role: 总结]` 忌年与时冲月支，日支自冲不妨。大运及岁君来冲月支，则祸。 → 《三命通会》卷十#看命总纲与月令提纲

- 详细解说：
  此节确立了子平法“以月令为纲”的核心原则。月令掌管一月之令，五行旺衰皆由月令决定。凡格先看月令，若月令成格（如财官印食），则为正格，其余外格（如从格、化格、遥巳等）皆为次要。只有月令无用（如月令比劫或无财官），才寻外格。同时强调了“根”的重要性，天干虚浮不如地支有根。

- **校勘与字词辨析（双语）**：
  - **“三宫”**：指年、日、时三柱，或指除月令外的其他位置。
  - **“日支自冲”**：指日支与月支相冲，或日支被冲。原文“日支自冲不妨”可能指日支冲月支（如子月午日），若冲出财官或冲去忌神，有时为喜，但一般仍忌冲提纲。或指“日支与时支冲”，对月令无碍。需结合上下文，此处意在强调月令不可伤。
  - **English**：
    - Life phase analysis terms explained; fortune-misfortune indicators treated as developmental tendencies."""
    normalized_text_zh: str = """"""
    subject: str = "看命总纲与月令提纲"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_month_command', 'bazi_semantic', 'bazi_condition_tougan_tonggen', 'bazi_semantic', 'bazi_state_factor_218', 'bazi_semantic', 'bazi_relation_day_master', 'bazi_semantic', 'bazi_condition_factor_81', 'bazi_semantic', 'source_ref', 'rel_smth_10_001', 'yuelingweiming', 'rel_smth_10_002', 'tigangwuyong', 'rel_smth_10_003', 'chongtigang', 'evi_smth_10_001', 'yuelingweiming', 'rule_yuelingweiming1', 'evi_smth_10_002', 'xunwaige', 'rule_xunwaige1', 'evi_smth_10_003', 'geju_dasun', 'rule_chongtigang1', 'map_smth_10_001', 'map_smth_10_002']
    
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
        l1_anchor="smth_v1.0.0_看命总纲与月令提纲_001_L1",
    )
    version: str = "1.0.0"
