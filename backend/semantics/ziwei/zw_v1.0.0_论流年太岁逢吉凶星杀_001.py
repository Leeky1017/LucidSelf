"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755788
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
    semantic_id="zw_v1.0.0_论流年太岁逢吉凶星杀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论流年太岁逢吉凶星杀(SemanticEntry):
    """
    - 分字分词释义：

  - **流年太岁**：每年地支所定的年度运势主宰，是判断当年祸福的核心时间因子。
  - **吉凶星杀**：流年中所遇的吉星与凶煞星，决定太岁落点的实际效果。
  - **三...
    """
    
    original_text: str = """- 分字分词释义：

  - **流年太岁**：每年地支所定的年度运势主宰，是判断当年祸福的核心时间因子。
  - **吉凶星杀**：流年中所遇的吉星与凶煞星，决定太岁落点的实际效果。
  - **三方对照**：太岁所在宫位与三合宫位的星曜配合，是综合判断的基本框架。
  - **太岁在命宫行**：太岁直接行至命宫，把年度主气压在生命中心，影响尤为关键。
  - **逢吉则吉遇凶则凶**：太岁本身为中性放大器，遇吉星则吉意倍增，遇凶星则凶意倍增。
  - **祸福尤紧**：太岁行命宫时祸福感受最强烈、最直接，需特别关注。
  - **年度放大器**：太岁不是凭空制造事件，而是把当年环境放大到特定宫位与星曜组合上。

- 原文（断句）：

  论流年太岁逢吉凶星杀：

  凡太岁看三方对照星辰，吉凶何如，以定祸福。太岁在命宫行，看祸福尤紧。如命在子宫，太岁到子，又癸生人，逢吉则吉，遇凶则凶。

- 规范化释义（primary_lang_explained）：

  本条聚焦在「流年太岁」这一年运主轴，说明如何在命盘结构之上评估当年的祸福强度。第一句提出基本方法：看太岁所在之宫，与其三方四正所会星辰为何，以综合吉凶来判断当年的大致走向。若太岁所到之宫与三方多会吉曜，且结构清朗，则多主这一年顺遂和平；若太岁行到的宫位本身陷地，又与多重恶杀相对照，则这一年多见烦扰、冲突乃至大病大祸。

  随后又强调一个特殊情况：当太岁直接行至命宫时，其影响尤为关键——因为它等于把当年的主气，直接压在命主自身的生命中心上。原文以「命在子宫，太岁到子，又癸生人」为例，说明若同一宫位聚焦于命宫、太岁与日主三者，且所会为吉星，则吉意大增；若所会为凶星，则凶意倍增。换句话说，流年太岁既不是单独的「凶神」，也非自动的「吉星」，而是一个把当年整体环境放大到特定宫位与星曜组合上的放大器，需要与命宫、大限、小限和星曜配置一并合参，才能做出负责的判断。

- 完整对等诠释（secondary_lang_full）：

  This rule focuses on the annual Tai Sui, the ruler of each year. It advises
  first to look at the house where the Tai Sui stands and the stars that form
  triads and oppositions with it. If these are largely benefic and well
  arranged, the year tends to be smoother; if the house is weak and packed with
  harsh stars, the year is more prone to troubles and crises. The text then
  singles out the case where the Tai Sui runs through the Life palace, noting
  that this placement makes its influence especially intense. When the annual
  ruler, the Life palace and the year’s stem–branch come together and meet good
  stars, blessings are magnified; when they meet malefics, difficulties are
  likewise magnified.

  In contemporary terms, Tai Sui itself is neither purely lucky nor purely
  unlucky. It acts as an amplifier that highlights certain houses and star
  patterns for a given year. To judge a year responsibly, one must read its Tai
  Sui placement together with the ten-year major period, shorter sub-periods and
  the underlying natal structure. Treated this way, the annual ruler becomes a
  core part of an "annual check-up": showing where attention, restraint or bold
  action is most needed in that specific year, without turning every difficult
  configuration into a doom sentence.

- 核心要点：

  1. 流年太岁行到何宫，以及与三方对照星辰的吉凶组合，是判断当年大势的关键入口。
  2. 太岁行到命宫时，其影响尤为放大，所会吉星则吉上加吉，所会凶星则凶上加凶。
  3. 太岁既非天生吉，也非天生凶，而是一个把当年环境投射到命盘结构上的「放大器」。
  4. 具体断年时，应将太岁位置与大限、小限和本命格局一起考量，避免只凭一处就武断下结论。
  5. 实务中可把本条视为「年度体检」的核心：先看太岁落点与三方，再看其是否正压命宫与重度凶星。"""
    normalized_text_zh: str = """"""
    subject: str = "论流年太岁逢吉凶星杀"
    factor_refs: list = ['system_liuniantaisui', 'relation_sanfangduizhao', 'state_taisuixingminggong', 'state_jixionghuihe', 'role_niandufangdaqi', 'source_ref', 'rel_taisui_001', 'system_liuniantaisui', 'rel_taisui_002', 'state_taisuixingminggong', 'rel_taisui_003', 'state_jixionghuihe', 'evi_taisui_001', 'relation_sanfangduizhao', 'rule_taisui_sanfang', 'evi_taisui_002', 'state_taisuixingminggong', 'rule_taisui_minggong', 'concept_annual_ruler', 'concept_amplifier']
    
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
        l1_anchor="zw_v1.0.0_论流年太岁逢吉凶星杀_001_L1",
    )
    version: str = "1.0.0"
