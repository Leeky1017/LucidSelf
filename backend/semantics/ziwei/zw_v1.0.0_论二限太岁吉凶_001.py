"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755766
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
    semantic_id="zw_v1.0.0_论二限太岁吉凶_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论二限太岁吉凶(SemanticEntry):
    """
    - 分字分词释义：

  - **二限太岁**：大限、小限与流年太岁三重时间因子的综合交互关系。
  - **独守吉凶**：大限、小限、太岁各自在所到宫位的星曜组合吉凶程度。
  - **岁限俱凶则凶...
    """
    
    original_text: str = """- 分字分词释义：

  - **二限太岁**：大限、小限与流年太岁三重时间因子的综合交互关系。
  - **独守吉凶**：大限、小限、太岁各自在所到宫位的星曜组合吉凶程度。
  - **岁限俱凶则凶**：当大限、小限、太岁三者同时偏凶时，当期风险极高。
  - **大限与小限相逢**：大小限在同一宫位或三方会合，使事件规模与强度放大。
  - **太岁逢大限/小限**：太岁与大限或小限会合，会吉则加福，会凶则加祸。
  - **太岁冲大限小限**：太岁与大小限宫位形成对冲，产生张力与激发。
  - **冲羊陀七杀**：太岁冲击擎羊、陀罗、七杀等重度凶星，关乎寿夭荣枯。
  - **寿夭荣枯**：寿命长短与地位兴衰的综合评估，是二限太岁判断的核心结论。

- 原文（断句）：

  论二限太岁吉凶：

  须详大限独守吉凶何如，小限独守吉凶何如，太岁独守吉凶何如，岁限俱凶则凶。又看大限与小限相逢吉凶何如，太限逢太岁吉凶何如，小限逢太岁吉凶何如，祸福尤紧。又看太岁冲大限、小限，太岁冲羊陀、七杀，然后可断寿夭荣枯。

- 规范化释义（primary_lang_explained）：

  本条在前一条「大限十年」的框架上，再次强调「二限与太岁」之间的组合判断方法。首先，要分别看大限、小限、太岁的「独守」状态：各自在所到宫位的星曜组合是偏吉、偏凶还是吉凶相半；若三者同时偏凶，则当期总体风险自然大增。其次，要看它们彼此之间的「相逢」情况：大限与小限若同落于吉宫且会吉曜，则为阶段性佳机；若同落凶宫，且恶杀成局，则为阶段性重灾。同理，大限逢太岁、小限逢太岁，若是吉星相会则加福，若是恶杀相会则加凶。

  最后，原文特别强调「冲击关系」：当太岁冲大限或小限所在之宫，尤其是太岁又来冲击羊刃、陀罗、七杀等重度凶星之时，就不只是一般的运势波动，而是与寿夭、荣枯直接相关的关键信号。换言之，判断一段时期的凶吉，不仅要看时间轴上各自的吉凶强弱，还要看它们彼此是会合、对冲还是夹击——会合多主放大，会吉则吉更吉，会凶则凶更凶；对冲多主激发，若冲在凶点，则应期往往更急更重。因此「二限太岁」的组合，实为推断人生重大转折与寿命节点的重要参照轴之一。

- 完整对等诠释（secondary_lang_full）：

  This section refines the previous teaching on ten-year periods by focusing on
  how the major period, minor period and annual ruler interact. First, each must
  be judged on its own: the house it occupies and the stars it carries can be
  broadly favourable, mixed or harsh. When all three are harsh at the same
  time, the baseline risk for that stretch of years rises sharply. The text then
  asks how they meet: if major and minor periods join in a good house with
  benefics, opportunities multiply; if they come together in a bad house loaded
  with malefics, setbacks and crises cluster. The same logic applies when the
  annual ruler meets either period—benefic meetings amplify support, malefic
  meetings amplify strain.

  Finally, the rule highlights oppositional geometry. When the annual ruler
  opposes the houses of the major or minor period, especially if it strikes
  severe stars such as Yang Blade or Tuoluo and Qisha, the issue is no longer
  mere fluctuation of luck but can touch matters of life, death and status. In
  modern terms, "two periods and the year" form three time axes whose
  alignments and clashes signal high-impact windows: golden openings when all
  three are strong and mutually supportive, and danger zones when all three are
  weak and aggressively entangled.  Used carefully, this framework helps
  practitioners distinguish between ordinary ups and downs and the few years in
  a life that truly reshape the long-term story.

- 核心要点：

  1. 大限、小限、太岁先各自评一次「独守吉凶」：三者皆凶时，当期整体风险极高。
  2. 再评估它们的「相逢」：大限与小限会合在吉宫且会吉曜，则为加福；会合在凶宫且恶杀成局，则为加凶。
  3. 太岁与大限、小限若会合于吉星，则多为机会与加持；若会合于恶杀，则多为祸端与压力来源。
  4. 太岁对冲大限、小限之宫，特别是冲到羊陀、七杀等凶星时，是关涉寿夭荣枯的重要信号。
  5. 二限与太岁的关系，实质上提供了一套「时间轴之间如何共振」的视角，帮助识别重大转折点。"""
    normalized_text_zh: str = """"""
    subject: str = "论二限太岁吉凶"
    factor_refs: list = ['system_daxian', 'system_xiaoxian', 'system_taisui', 'relation_huihechong', 'result_shouyaorongku', 'source_ref', 'rel_erxian_001', 'system_daxian', 'rel_erxian_002', 'system_taisui', 'rel_erxian_003', 'relation_huihechong', 'evi_erxian_001', 'system_taisui', 'rule_erxian_sanxiong', 'evi_erxian_002', 'result_shouyaorongku', 'rule_erxian_shouyao', 'concept_period_interaction', 'concept_lifespan_risk']
    
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
        l1_anchor="zw_v1.0.0_论二限太岁吉凶_001_L1",
    )
    version: str = "1.0.0"
