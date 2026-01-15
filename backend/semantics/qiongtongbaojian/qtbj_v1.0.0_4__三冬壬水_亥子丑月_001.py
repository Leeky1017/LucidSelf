"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578637
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
    semantic_id="qtbj_v1.0.0_4__三冬壬水_亥子丑月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 4三冬壬水亥子丑月(SemanticEntry):
    """
    - **原文（source_text）**：
  **十月壬水**，司权，至旺之极，取戊为用，若生辰日干，又见辰时，必须戊透，又须庚制甲，不伤戊土，戊庚两全，定主豋科乃第。或支成木局，有甲乙出干，得庚...
    """
    
    original_text: str = """- **原文（source_text）**：
  **十月壬水**，司权，至旺之极，取戊为用，若生辰日干，又见辰时，必须戊透，又须庚制甲，不伤戊土，戊庚两全，定主豋科乃第。或支成木局，有甲乙出干，得庚透者，富贵。或支成水局，不见戊己，名润下格，运行西北，大富贵。
  **十一月壬水**，阳刃帮身，较前更旺，先取戊土，次用丙火，丙戊两透，富贵荣华。有戊无丙，略可言富。有丙无戊，好谋无成。
  或支成水局，丙不出干，即有戊土，亦是庸人。
  或壬子日、丁未时，虽不能科甲，亦有恩荣，何也？盖用子中癸水为官，号曰用神得地。
  **十二月壬水**，旺极复衰，何也？上半月癸辛主事，故旺，专用丙火。下半月己土主事，故衰。亦用丙火，甲木佐之。
  有丙解冻，名利双全。丙透甲出，科甲之贵。或支成金局，名金寒水冻，一世孤贫，见火略可。
  腊月壬水，先取丙火，丁甲为佐，故水冷金寒爱丙丁。

- **分字分词释义**：
  - **司权**：掌权当令 / 亥月壬水 / 身旺
  - **至旺之极**：极其旺盛 / 临官之地 / 需戊制
  - **戊庚两全**：戊土庚金俱备 / 杀印相生 / 吉象
  - **润下格**：水润下流格 / 水局无土 / 变格
  - **阳刃帮身**：阳刃助身 / 子月壬水 / 身极旺
  - **富贵荣华**：富贵与荣耀 / 丙戊两透 / 吉象
  - **好谋无成**：多谋划无结果 / 有丙无戊 / 凶象
  - **旺极复衰**：极旺转衰 / 丑月上下分 / 节气变化
  - **金寒水冻**：金气寒冷水气冰冻 / 金局无火 / 凶象
  - **一世孤贫**：一辈子孤独贫穷 / 无火 / 凶象

- **规范化释义（primary_lang_explained）**：
  **十月（亥月）壬水**：司权，至旺之极。取戊为用（止水）。戊庚两全（庚制甲护戊），定主登科。或支成水局，不见戊己，名"润下格"，运行西北大富贵。
  **十一月（子月）壬水**：阳刃帮身（子中癸水为刃），较前更旺。先取戊土（制刃），次用丙火（调候）。丙戊两透，富贵荣华。
  **十二月（丑月）壬水**：旺极复衰。上半月癸辛主事故旺，专用丙火；下半月己土主事故衰，亦用丙火，甲木佐之（疏土）。有丙解冻，名利双全。

- **完整对等诠释（secondary_lang_full）**：
  **10th Month (Pig) Ren Water**: Commanding, extremely prosperous. Take Wu as use. Wu/Geng both complete (Geng controls Jia protects Wu), exam success. If Water Frame, no Wu/Ji, "Flowing Downward Pattern", great wealth in NW luck.
  **11th Month (Rat) Ren Water**: YangRen helping body, stronger than before. First Wu (control Ren), then Bing (warm). Bing/Wu both revealing, wealth nobility glory.
  **12th Month (Ox) Ren Water**: Prosperous turning weak. First half Gui/Xin rule, so prosperous, focus Bing. Second half Ji rules, so weak, also use Bing, Jia assist. Having Bing unfreeze, fame/profit complete.

- **核心要点**：
  - **十月十一月**：水旺，喜戊土堤防，丙火暖局。
  - **十二月**：寒湿，首重丙火解冻。
  - **格局**：润下格（水局无土）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_437]` `[trigger: 壬生亥月]` `[factor_trigger: month_hai AND tiangan_ren AND tiangan_wu AND tiangan_geng AND commanding_power]` `[role: 主干]` 十月壬水，壬水司权，至旺之极，取戊为用。戊庚两全，定主登科。 → 《穷通宝鉴·论壬水》#36.4
  - `[ns_qttbj_438]` `[trigger: 润下格]` `[factor_trigger: month_hai AND tiangan_ren AND dizhi_water_frame AND NOT tiangan_wu AND NOT tiangan_ji AND runxia_pattern]` `[role: 条件分支]` 或支成水局，不见戊己，名润下格，运行西北，大富大贵。 → 《穷通宝鉴·论壬水》#36.4
  - `[ns_qttbj_439]` `[trigger: 壬生子月]` `[factor_trigger: month_zi AND tiangan_ren AND tiangan_wu AND tiangan_bing AND yangren_help]` `[role: 主干]` 十一月壬水，阳刃帮身，较前更旺，先取戊土，次用丙火。 → 《穷通宝鉴·论壬水》#36.4
  - `[ns_qttbj_440]` `[trigger: 壬生丑月]` `[factor_trigger: month_chou AND tiangan_ren AND tiangan_bing AND likes_bing_unfreeze]` `[role: 主干]` 十二月壬水，旺极复衰，专用丙火。有丙解冻，名利双全。 → 《穷通宝鉴·论壬水》#36.4
  - `[ns_qttbj_441]` `[trigger: 金寒水冻]` `[factor_trigger: month_chou AND tiangan_ren AND dizhi_metal_frame AND NOT element_fire AND metal_cold_water_frozen]` `[role: 例外处理]` 或支成金局，名金寒水冻，一世孤贫，见火略可。 → 《穷通宝鉴·论壬水》#36.4"""
    normalized_text_zh: str = """"""
    subject: str = "4. 三冬壬水（亥子丑月）"
    factor_refs: list = ['yangren_help', 'runxia_pattern', 'metal_cold_water_frozen']
    
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
        l1_anchor="qtbj_v1.0.0_4__三冬壬水_亥子丑月_001_L1",
    )
    version: str = "1.0.0"
