"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755815
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
    semantic_id="zw_v1.0.0_论羊陀迭并_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论羊陀迭并(SemanticEntry):
    """
    - 分字分词释义：

  - **羊陀迭并**：本命已见擎羊或陀罗，又在流年再遇流羊、流陀同轴重叠的极端凶格局。
  - **擎羊**：流年在禄前一位，主刀刃、血光、突发冲突与风险骤增。
  - **...
    """
    
    original_text: str = """- 分字分词释义：

  - **羊陀迭并**：本命已见擎羊或陀罗，又在流年再遇流羊、流陀同轴重叠的极端凶格局。
  - **擎羊**：流年在禄前一位，主刀刃、血光、突发冲突与风险骤增。
  - **陀罗**：流年在禄后一位，主拖延、缠绕、慢性损耗与反复折腾。
  - **流羊流陀**：流年运行到擎羊或陀罗的位置，与本命羊陀叠加时形成迭并。
  - **命迁轴线**：命宫与迁移宫的对宫轴线，象征自我与外境之间的关系，被羊陀夹击时冲突风险最高。
  - **为祸最毒**：羊陀迭并与七杀重逢并列为「为祸最毒」的两大极端凶格局。
  - **极端风险信号**：羊陀迭并是高度事故风险、大祸可能的警讯指标。

- 原文（断句）：

  论羊陀迭并：

  如庚生人，命在卯宫，迁移在酉宫，如遇羊陀流年，亦庚禄居申，流羊在酉，流陀在未，是命在卯宫，原有酉宫擎羊冲合流年，又遇流羊流陀，谓之羊陀迭并。

- 规范化释义（primary_lang_explained）：

  本条通过一个具体例子，说明何谓「羊陀迭并」：以庚年出生，命宫在卯、迁移在酉为例，本命三合原本就有擎羊落在酉宫，与命宫成冲。若又逢某流年，天干禄星居申，流年擎羊落酉，流年陀罗落未，则形成「本命酉宫有羊」再叠加「流羊在酉」「流陀在未」，命宫卯与迁移酉一带被羊陀重重夹击，这种本命与流年恶星在同一轴线上反复叠加的局面，即叫「羊陀迭并」。

  传统认为，羊刃与陀罗本身就主突发之祸、血光冲突与风险骤增，一旦出现「迭并」——既有本命恶星，又遇流年同类恶星重叠——则相关宫位所主领域（自身安全、迁移出行、对外环境等）在该年或该限中，发生严重事故的概率大幅上升。然则实际应验程度，还需结合星曜庙陷、是否有紫微天相、禄存等吉曜拱照，以及大限、小限的总体吉凶来综合判断，不宜见「羊陀迭并」四字就一概视作必死绝境。

- 完整对等诠释（secondary_lang_full）：

  This rule defines the pattern called "Yang-Tuo overlapping". In the example
  given, a person born in a Geng year has the Life palace in Mao and the Travel
  palace in You, with a natal Qingyang already lodged in You. In a later year,
  the annual salary star for Geng sits in Shen while the flowing Qingyang moves
  into You and flowing Tuoluo into Wei, so that the Life–Travel axis is struck
  repeatedly by the same pair of cutting stars. This piling up of natal and
  annual malefics on one line is what the text calls Yang-Tuo overlapping.

  Traditionally such stacking is read as a strong warning sign for accidents,
  injuries and sudden disruptions, especially in matters of movement, travel and
  dealings with the outside world. In practice, however, its severity still
  depends on dignity, house context and the presence or absence of powerful
  benefics. Used carefully, the pattern points to a year when extra caution and
  conservative choices are wise, rather than a sentence that disaster cannot be
  avoided.

- 核心要点：

  1. 「羊陀迭并」指本命已见擎羊、陀罗等恶星，又在流年再遇流羊、流陀同轴重叠的格局。
  2. 这种局面多发生在命宫与迁移宫一带，象征自我与外在环境之间的冲突风险陡增。
  3. 羊陀象征突发、锋利与破坏力，迭并时对血光、意外与大事故的指向通常更强。
  4. 实务判断时，应合看庙旺/陷地、是否有吉曜拱照以及大限小限整体趋势，避免机械恐吓。
  5. 可将「羊陀迭并」视为极端风险信号之一，提醒当事人在对应年份特别注意出行安全与高危行为。"""
    normalized_text_zh: str = """"""
    subject: str = "论羊陀迭并"
    factor_refs: list = ['pattern_yangtuodiebing', 'star_liuyangtuo', 'axis_mingqian', 'pattern_jiaji', 'signal_jiduanfengxian', 'source_ref', 'rel_yangtuo_001', 'star_liuyangtuo', 'rel_yangtuo_002', 'axis_mingqian', 'rel_yangtuo_003', 'pattern_yangtuodiebing', 'evi_yangtuo_001', 'pattern_yangtuodiebing', 'rule_yangtuo_diebing', 'concept_malefic_overlap', 'concept_axis_attack']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_论羊陀迭并_001_L1",
    )
    version: str = "1.0.0"
