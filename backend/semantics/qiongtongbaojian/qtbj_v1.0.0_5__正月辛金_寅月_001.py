"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578442
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
    semantic_id="qtbj_v1.0.0_5__正月辛金_寅月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 5正月辛金寅月(SemanticEntry):
    """
    - **原文（source_text）**：
  正月辛金，阳气舒而寒气未除，不知正月建寅，中有长生之丙，解去寒气，忌甲木司权，辛金失令，取己土为生身之本，欲得辛金发现，全赖壬水之功，己壬两透，支见庚...
    """
    
    original_text: str = """- **原文（source_text）**：
  正月辛金，阳气舒而寒气未除，不知正月建寅，中有长生之丙，解去寒气，忌甲木司权，辛金失令，取己土为生身之本，欲得辛金发现，全赖壬水之功，己壬两透，支见庚制甲，科甲定然。或己土透干，支中有甲，异路恩荣。或己土不全，号曰君臣失势，富贵难全。或有丙火出干，亦主武学。或见壬、无己庚者，贫贱之徒。
  或支成火局，即壬水出干，不克己土，亦寻常之人。或庚壬两透，破局制火，必为显达之人。
  或支成水局，不见丙火，名为金弱沉寒，平常之士，书曰：金水性寒寒到底，凄凉难免少年忧。得丙照暖，反主富贵。
  故正月辛金，先己后壬。己为君，庚为佐。如用丙火须参看。用己，火妻土子。用壬，金妻水子。
  辛金珠玉，最怕红炉，辛逢卯日子时，名曰朝阳。

- **分字分词释义**：
  - **阳气舒**：阳气舒展 / 春回大地 / 寅月特点
  - **长生之丙**：丙火长生于寅 / 寅中藏丙 / 暖局
  - **生身之本**：生养日主的根本 / 己土印绶 / 用神
  - **君臣失势**：君与臣皆失势 / 己土不全 / 凶象
  - **异路恩荣**：非正途的荣耀 / 武职 / 次吉
  - **金弱沉寒**：金气衰弱沉陷寒冷 / 水局无火 / 凶象
  - **朝阳格**：早晨太阳格 / 辛卯日子时 / 贵格
  - **珠玉**：珍珠美玉 / 辛金象征 / 属性
  - **红炉**：红色火炉 / 火多克金 / 忌象
  - **科甲定然**：功名必定 / 己壬庚配合 / 吉象

- **规范化释义（primary_lang_explained）**：
  正月（寅月）辛金，阳气舒展而寒气未除。正月建寅中有长生之丙火解去寒气。忌甲木司权辛金失令。取己土为生身之本（印绶生身），欲得辛金发现全赖壬水之功（洗淘）。己壬两透支见庚制甲科甲定然。或己土透干支中有甲异路恩荣。或己土不全号曰君臣失势富贵难全。或有丙火出干亦主武学。或见壬无己庚者贫贱之徒。
  或支成火局即壬水出干不克己土亦寻常之人。或庚壬两透破局制火必为显达之人。
  或支成水局不见丙火名为金弱沉寒平常之士。书曰：金水性寒寒到底凄凉难免少年忧。得丙照暖反主富贵。
  故正月辛金先己后壬。己为君庚为佐。如用丙火须参看。用己火妻土子。用壬金妻水子。
  辛金珠玉最怕红炉。辛逢卯日子时名曰朝阳。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal in 1st Month (Tiger Month): yang qi stretching cold qi not removed. 1st month Tiger contains longevity Bing Fire dissolving cold qi. Fear Jia Wood commanding Xin Metal losing season. Take Ji Earth as body-生 root (Seal generating body), wanting Xin Metal manifest entirely relying on Ren Water功 (washing). Ji/Ren revealing branches見Geng制Jia imperial exam certain. Or Ji Earth revealing branches containing Jia alternative honors. Or Ji Earth incomplete name sovereign-minister losing势 wealth-nobility incomplete. Or Bing Fire revealing also main military. Or見Ren without Ji/Geng poor lowly.
  Or branches form Fire Frame even Ren revealing not克Ji Earth also ordinary. Or Geng/Ren revealing breaking frame制Fire surely prominent.
  Or branches form Water Frame not見Bing Fire name Metal-weak sinking-cold ordinary scholar. Book says: Metal-Water nature cold cold-to-bottom misery unavoidable youth worry. Gaining Bing warming conversely main wealth-nobility.
  Therefore 1st month Xin Metal: first Ji then Ren. Ji as sovereign Geng as assistant. If using Bing Fire must參看. Using Ji Fire-wife Earth-child. Using Ren Metal-wife Water-child.
  Xin Metal pearl-jade most fears red-furnace. Xin meeting Mao-day Zi-hour name Morning-Sun.

- **核心要点**：
  - **配合**：庚金（制甲）、丙火（暖局）
  - **寅月特点**：甲木司权需己土制木生金，壬水洗淘

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_401]` `[trigger: 辛生寅月]` `[factor_trigger: month_yin AND tiangan_xin AND tiangan_ji AND tiangan_ren]` `[role: 主干]` 正月辛金，阳气舒而寒气未除，取己土为生身之本，欲得辛金发现，全赖壬水之功。 → 《穷通宝鉴·三春辛金》#34.5
  - `[ns_qttbj_402]` `[trigger: 己壬庚全]` `[factor_trigger: month_yin AND tiangan_xin AND ji_revealed AND ren_revealed AND geng_in_branch]` `[role: 条件分支]` 己壬两透，支见庚制甲，科甲定然。 → 《穷通宝鉴·三春辛金》#34.5
  - `[ns_qttbj_403]` `[trigger: 金弱沉寒]` `[factor_trigger: month_yin AND tiangan_xin AND dizhi_water_frame AND NOT tiangan_bing AND metal_weak_sinking_cold]` `[role: 例外处理]` 支成水局，不见丙火，名为金弱沉寒，平常之士。 → 《穷通宝鉴·三春辛金》#34.5
  - `[ns_qttbj_404]` `[trigger: 朝阳格]` `[factor_trigger: daymaster_xin_mao AND hour_zi AND morning_sun_pattern]` `[role: 条件分支]` 辛逢卯日子时，名曰朝阳。 → 《穷通宝鉴·三春辛金》#34.5"""
    normalized_text_zh: str = """"""
    subject: str = "5. 正月辛金（寅月）"
    factor_refs: list = ['sovereign_minister_loss', 'metal_weak_sinking_cold', 'morning_sun_pattern']
    
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
        l1_anchor="qtbj_v1.0.0_5__正月辛金_寅月_001_L1",
    )
    version: str = "1.0.0"
