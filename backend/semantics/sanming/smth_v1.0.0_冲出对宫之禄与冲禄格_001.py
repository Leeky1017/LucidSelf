"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412374
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
    semantic_id="smth_v1.0.0_冲出对宫之禄与冲禄格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 冲出对宫之禄与冲禄格(SemanticEntry):
    """
    - **原文（source_text）**：

  此格如庚禄在申，柱中无申，得庚寅日，年月时再有寅字，并冲申，为庚之禄。甲禄在寅，柱中无寅，却得甲申日，年月时再有申字，并冲寅，为甲之禄。大忌丙伤庚、...
    """
    
    original_text: str = """- **原文（source_text）**：

  此格如庚禄在申，柱中无申，得庚寅日，年月时再有寅字，并冲申，为庚之禄。甲禄在寅，柱中无寅，却得甲申日，年月时再有申字，并冲寅，为甲之禄。大忌丙伤庚、庚伤甲，填实禄位，则不贵。余以例推。如己巳、丁丑、庚寅、戊寅；辛巳、乙未、甲申、壬申；乙卯、甲申、辛卯、辛卯，三命合格，贵。

- 分字分词释义：

  - 禄在申：指庚金之禄在申位，其他天干各有本禄，如甲禄在寅等。
  - 柱中无申／无寅：命局本身不见禄位所在之支，须以对宫之支冲出。
  - 冲出禄位：如庚寅日再见寅，寅冲申，以多寅之力冲出申中庚禄；甲申日再见申，同理冲出对宫寅中甲禄。
  - 大忌丙伤庚、庚伤甲：指庚金禄被丙火克、甲木禄被庚金伤，当心禄位虽出却遭克制。
  - 填实禄位：禄位本宫若被支神占据或合会过多，则对宫之冲失去落点，难以成格。

- **规范化释义（primary_lang_explained）**：

  冲禄格，是通过对宫之支的重复冲击，把本来不现的禄位从另一侧冲出来的格局。以庚金为例，庚禄在申；若命局中不见申而多见寅，则以寅冲申，由多寅之力“并冲”出申中庚禄，庚金因此得禄。甲木之禄在寅，同理可由多申并冲寅而出。

  与前文“冲合禄马”“飞财”“破财”等格相比较，冲禄单纯强调“冲出禄位”而非同时兼顾财马、官星；因此格局的高下，更依赖于禄位本身是否清纯、有无被克伤，以及日主是否有力承受所冲出的禄气。一旦丙火重重克庚、庚金又重重伤甲，则禄虽出而反成祸机。

- 核心要点：

  - 冲禄格的骨架是“禄不在本宫，而由对宫多支并冲而出”。
  - 身旺、禄清、不被克制，是冲禄由“有禄”转为“有贵”的关键。
  - 丙伤庚、庚伤甲，以及禄位填实、合会、被羊刃七煞占据等，都会使冲禄大打折扣，甚至不成格。

- 详细解说：

  冲禄与拱禄、归禄相比，更带有“主动突破”的意味：

  - 归禄是禄位平移；
  - 拱禄是隔位夹拱；
  - 冲禄则是从对宫直冲而至。

  以原文举例的几命来看，多以寅申对冲为主轴：庚金以寅冲申得禄，甲木则以申冲寅得禄。在这些命局中，往往同时存在比肩、印绶等生扶之力，使被冲出的禄位不至被外力夺走。若再行身旺、禄旺之运，则易有“骤升”的职业与地位变化。

  然而，冲禄本身也带来一定不稳定性：禄位是以冲动而起，若岁运再增冲力、或引来强力克制（如丙火克庚、庚金伤甲），则禄气可能转化为官非、伤灾之源。在实务判断中，宜将冲禄视为一条潜在“快车道”，真正能否把握，还需回到日主强弱与整体格局的调和性上。

- **校勘与字词辨析（双语）**：

  - 原文“此格如庚禄申，柱中无申，得庚寅日，年月时再有寅字，并冲申，为庚之禄”一句，本稿依底本断句，仅在白话中补充“多寅并冲”的含义。
  - “大忌丙伤庚、庚伤甲，填实禄位则不贵”本稿完全保留，并在释义中拆解为“克禄”“填禄”两个不利因素，供后续层级使用。
  - 文末三命例（己巳、丁丑、庚寅、戊寅等），本稿不逐条细拆，只指出其共同点为“多支并冲对宫禄位且无明显克破”，以免在 L1 层过早做细节命例评断。
  - **English**：
    - The sentence explaining "Geng salary is Shen, if no Shen in chart, Geng-Yin day with multiple Yin clashing Shen becomes Geng's salary" is punctuated per the base text; vernacular adds "multiple Yin clashing together."
    - The phrase "greatly taboo Bing harming Geng, Geng harming Jia, filling the salary position makes it not noble" is fully preserved; the glossary breaks it down as "克禄" and "填禄" as two unfavorable factors.
    - The three example charts at the end are not individually analyzed; only their common feature "multiple branches clashing the opposite-palace salary without obvious destruction" is noted to avoid premature detailed case analysis in L1.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_053]` `[trigger: 冲禄格定义]` `[factor_trigger: chonglu_ge_presence]` `[role: 主干]` 此格如庚禄在申，柱中无申，得庚寅日，年月时再有寅字，并冲申，为庚之禄。 → 《三命通会》卷六#冲禄
  - `[ns_smth_06_054]` `[trigger: 甲禄冲出]` `[factor_trigger: jia_lu_yin AND duo_shen_chong]` `[role: 主干依赖]` 甲禄在寅，柱中无寅，却得甲申日，年月时再有申字，并冲寅，为甲之禄。 → 《三命通会》卷六#冲禄
  - `[ns_smth_06_055]` `[trigger: 大忌克禄]` `[factor_trigger: bing_shang_geng OR geng_shang_jia]` `[role: 条件分支]` 大忌丙伤庚、庚伤甲，填实禄位，则不贵。 → 《三命通会》卷六#冲禄
  - `[ns_smth_06_056]` `[trigger: 合格贵]` `[factor_trigger: san_ming_he_ge]` `[role: 总结]` 如己巳、丁丑、庚寅、戊寅...三命合格，贵。 → 《三命通会》卷六#冲禄

- **完整对等诠释（secondary_lang_full）**：
  The "Clashing-Out Salary" pattern applies when the day-master's salary branch does not appear anywhere in the chart, yet is brought into play by clashing from the opposite position. For example, Geng's salary sits in Shen; if Shen is absent but the chart shows Geng-Yin day plus additional Yin branches in the year, month or hour, those multiple Yin branches can collectively clash Shen and release Geng's salary. Similarly, Jia's salary sits in Yin; a Jia-Shen day with multiple Shen branches can clash Yin and draw out Jia's salary.
  
  Compared to "Salary Returns to Hour" (which shifts the salary) or "Embracing Salary" (which flanks and embraces), clashing carries a more aggressive, breakthrough quality—the salary is seized through direct confrontation rather than indirection. This can translate into sudden career leaps when fortune cycles reinforce the clash, but it also introduces instability: if the year or cycle adds even more clashing force, or if a hostile stem conquers the newly released salary (Bing injuring Geng, Geng injuring Jia), the salary energy can flip into lawsuits or accidents.
  
  For the pattern to succeed, the day-master must be strong and the salary must remain "clean"—not conquered by hostile stems and not crowded out by the Blade or Seven-Killer. If the salary's home position is filled by an actual branch or over-combined, the clash has no place to land and the pattern fails. When conditions are right, classic texts describe rapid wealth and position changes; when wrong, the same clash mechanism becomes a source of turmoil."""
    normalized_text_zh: str = """"""
    subject: str = "冲出对宫之禄与冲禄格"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_16', 'bazi_semantic', 'bazi_structure_config_4', 'bazi_semantic', 'bazi_state_factor_10', 'bazi_semantic', 'bazi_state_degree', 'bazi_semantic', 'bazi_condition_factor_146', 'bazi_semantic', 'bazi_condition_factor_147', 'bazi_semantic', 'source_ref', 'rel_smth_06_040', 'chonglu_ge_presence', 'rel_smth_06_041', 'bingchong_lidu', 'rel_smth_06_042', 'kelu_risk', 'evi_smth_06_040', 'chonglu_lujing_config', 'rule_chonglu', 'evi_smth_06_041', 'kelu_risk', 'rule_kelu', 'evi_smth_06_042', 'shenwan_luqing', 'rule_hege', 'map_smth_06_027', 'map_smth_06_028']
    
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
        l1_anchor="smth_v1.0.0_冲出对宫之禄与冲禄格_001_L1",
    )
    version: str = "1.0.0"
