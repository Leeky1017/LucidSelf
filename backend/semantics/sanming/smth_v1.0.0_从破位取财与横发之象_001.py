"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412284
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
    semantic_id="smth_v1.0.0_从破位取财与横发之象_001",
    book_id="sanming",
    engine_id="bazi"
)
class 从破位取财与横发之象(SemanticEntry):
    """
    - **原文（source_text）**：

  此格如乙卯日生，八字不见财官，用卯字破出午未中己土为财用，要寅、戌一字暗合财气为妙，忌劫财填实，但有财位及填实，冲位便破不行矣。如庚申、辛酉日破寅卯...
    """
    
    original_text: str = """- **原文（source_text）**：

  此格如乙卯日生，八字不见财官，用卯字破出午未中己土为财用，要寅、戌一字暗合财气为妙，忌劫财填实，但有财位及填实，冲位便破不行矣。如庚申、辛酉日破寅卯辰之木为财，丙午、丁未日破酉戌之金为财，壬子、癸丑日破巳午中之火为财，此数日本日刃日禄本体自强，故可冲破取财为用，其余日主柔弱，岂能破夺横来财乎。合此格者，多能横发取不意之财。诗曰：命里无财看破财，破来财禄似山堆，运行官印多多福，却怕刑冲填实灾。又：卯破午未取财看，午未破酉总一般，丑破巳午财来广，酉破辰卯福不难。

- 分字分词释义：

  - **八字不见财官**：命局表面无明财、明官，或财官极弱不足用，需从“破位”中取财。
  - **用卯字破出午未中己土为财用**：以乙卯日为例，卯冲午未，破出午未中藏己土，作为乙木之财星。
  - **寅、戌一字暗合财气**：寅、戌可与午、未构成三合局，暗中合住所破之财，使之不致散失。
  - **忌劫财填实**：若比肩、劫财填实财位（如再见午未、寅戌过多），则冲位被堵塞，无法再从破中取财。
  - **庚申、辛酉日破寅卯辰之木为财**：金日主以木为财，通过冲破寅卯辰一带之木局，以取其财。
  - **丙午、丁未日破酉戌之金为财**：火日主以金为财，通过冲破酉戌之金局而得财。
  - **壬子、癸丑日破巳午中之火为财**：水日主以火为财，通过冲破巳午火局取财。
  - **日本日刃日禄本体自强**：仅限于本身旺、临刃临禄之日主，才能承受破财之力；日主柔弱者不宜。

- **规范化释义（primary_lang_explained）**：

  破财格，讲的是“命里无明财，从破中取财”的格局。以乙卯日为例：原局不见财官，但午、未中暗藏己土，可为乙木之财。若命局中卯木有力，以卯去冲午、未，便可把藏在其中的己土冲出，作为可用之财；再得寅、戌等支与午未构成三合，暗中合住财气，则财星既出且能为我所用。
  
  同理，庚申、辛酉日可破寅卯辰之木为财；丙午、丁未日可破酉戌之金为财；壬子、癸丑日可破巳午之火为财。但这些都建立在“日本身强健、临刃临禄”的前提上：本体不强，怎能去破夺横来之财？故原文强调“此数日本日刃日禄本体自强，故可冲破取财为用，其余日主柔弱，岂能破夺横来财乎”。
  
  一旦合格，往往有“横发”的特征：命里本无明财，却因某次破位而突然得财，多见于机会型、搏击型的财运。但若运行官印，能为破财所得提供秩序与约束，则福气更厚；反之，刑冲过度或劫财填实，则破位反成灾源。

- 核心要点：

  - 破财格以前提为**命局无明财**，从冲破、刑破之支中取暗藏财星。
  - 仅当日主本身旺、临刃临禄时，方可承受“破取横财”的动作，身弱者难以驾驭。
  - 冲出之财须有合局暗合之，方能“合住财气”，否则易成来去无踪、破财反多。
  - 劫财填实、刑冲杂乱时，破财格容易转为官司、意外损耗等负面事件。

- 详细解说：

  从技术路径上看，破财格与前一节破官格相似：都以“从隐处破出可用之星”为核心，不同在于前者取官、后者取财。两者都要求：
  
  1. 原局无明用神（财或官）可用；
  2. 有特定破位能冲出支中所藏用神；
  3. 再以三合、拱合等方式合住之。
  
  以乙卯日为例，卯为乙之刃，日主甚旺；午未中己土为财，若卯木有力，破之则财出。若再见寅、戌，构成寅午戌或卯未戌等火土局，则财气不至散失。但若同时劫财重重填实午未、寅戌，则原本可破之位被同类塞满，卯再冲只成比劫相争，反会引起耗损与是非。
  
  在实际命例中，破财格常表现为：平时财源并不显赫，一遇特殊年份或大运冲动某支，财势突然大起；但若同时缺乏印、官的约束，则易有“大进大出”“一夜暴富又一夜破产”之类的极端波动。因此判断破财格时，不仅要看“能否破出财”，更要看“破出的财究竟受谁驾驭”。

- **校勘与字词辨析（双语）**：

  - 原文“命里无财看破财，破来财禄似山堆”一句，为破财格之总纲，本稿据底本保留，在白话中解释为“从破位中取来的财往往成堆而来”。
  - “卯破午未取财看，午未破酉总一般，丑破巳午财来广，酉破辰卯福不难”一联，总结多种破财路径，本稿不改用字，仅在释义中归纳为“以不同组合破出不同方位的财”。
  - 文中“此数日本日刃日禄本体自强”强调日主强弱之分界，本稿在详细解说中反复提示“身弱者不宜强取破财格”。
  - **English**：
    - The couplet "When the chart has no wealth, look at Breaking-Wealth; wealth seized piles up like mountains" is the guiding principle; this edition preserves it.
    - The verses listing multiple breaking-wealth paths are kept unchanged; summarized as "different combinations break out wealth from different positions."
    - The phrase emphasizing day-master strength marks the threshold; reminds "a weak body should not forcibly attempt Breaking-Wealth."

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_025]` `[trigger: 破财格定义]` `[factor_trigger: pocai_ge_presence]` `[role: 主干]` 八字不见财官，用卯字破出午未中己土为财用。 → 《三命通会》卷六#破财格
  - `[ns_smth_06_026]` `[trigger: 暗合财气]` `[factor_trigger: yin_xu_an_he AND ji_jiecai_tianshi]` `[role: 主干依赖]` 要寅、戌一字暗合财气为妙，忌劫财填实。 → 《三命通会》卷六#破财格
  - `[ns_smth_06_027]` `[trigger: 本体自强]` `[factor_trigger: ri_ren_ri_lu AND ben_ti_zi_qiang]` `[role: 条件分支]` 此数日本日刃日禄本体自强，故可冲破取财为用。 → 《三命通会》卷六#破财格
  - `[ns_smth_06_028]` `[trigger: 财禄山堆]` `[factor_trigger: po_lai_cai_lu]` `[role: 总结]` 命里无财看破财，破来财禄似山堆。 → 《三命通会》卷六#破财格

- **完整对等诠释（secondary_lang_full）**：
  The "Breaking-Out Wealth" pattern describes a configuration where the chart contains no openly visible wealth star and wealth must instead be seized from a hidden position through clashing. Taking Yi-Mao day as the example: the chart shows neither obvious wealth nor official, yet Ji earth—which serves as Yi Wood's wealth—lies concealed inside Wu and Wei. If Mao Wood is powerful, it can clash Wu and Wei and crack open the hidden Ji earth so that the wealth star emerges for use. To stabilise the newly released wealth, one further needs Yin or Xu to form a fire-and-earth trine that gathers the dislodged wealth and prevents it from scattering.
  
  The same logic applies to other strong day-pillars: Geng-Shen and Xin-You days can break Yin, Mao and Chen to seize wood as wealth; Bing-Wu and Ding-Wei days can break You and Xu to seize metal as wealth; Ren-Zi and Gui-Chou days can break Si and Wu to seize fire as wealth. In every case the day-master must itself be robust—typically sitting on the Blade or Salary position—because only a strong body can withstand the violent act of breaking and seizing. A weak day-master attempting such an action would be overwhelmed by the turbulence and end up losing rather than gaining.
  
  When the pattern succeeds, wealth often arrives suddenly and in large amounts—what the classics call "windfall wealth piling up like mountains". The ideal follow-up is a fortune cycle that brings official or Seal energy, which imposes order on the seized wealth and converts it into lasting prosperity. If, however, the chart or cycle is dominated by Robbery-of-Wealth stars that fill the target position, or by excessive clashes that never settle, then the breaking action backfires: instead of sudden riches, the native experiences lawsuits, unexpected losses or wild swings between boom and bust."""
    normalized_text_zh: str = """"""
    subject: str = "从破位取财与横发之象"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_11', 'bazi_semantic', 'bazi_structure_config_3', 'bazi_semantic', 'bazi_state_day_master_strength', 'bazi_semantic', 'bazi_state_factor_7', 'bazi_semantic', 'bazi_condition_jiecai_1', 'bazi_semantic', 'bazi_condition_factor_139', 'bazi_semantic', 'source_ref', 'rel_smth_06_019', 'pocai_ge_presence', 'rel_smth_06_020', 'rizhu_linren_linlu', 'rel_smth_06_021', 'jiecai_tianshi_risk', 'evi_smth_06_019', 'powei_ancang_config', 'rule_pocai', 'evi_smth_06_020', 'rizhu_linren_linlu', 'rule_shenqiang', 'evi_smth_06_021', 'heju_anhe_wengu', 'rule_hengfa', 'map_smth_06_013', 'map_smth_06_014']
    
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
        l1_anchor="smth_v1.0.0_从破位取财与横发之象_001_L1",
    )
    version: str = "1.0.0"
