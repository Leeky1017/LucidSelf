"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755836
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
    semantic_id="zw_v1.0.0_论大小二限而辰过十二宫遇十二支人所忌诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论大小二限而辰过十二宫遇十二支人所忌诀(SemanticEntry):
    """
    - 分字分词释义：

  - **大小二限过宫**：大限、小限经过十二宫位的运行过程。
  - **十二支人所忌**：以出生年地支为核心，标记每类人在特定岁限、宫位的禁忌组合。
  - **灾悔官非孝...
    """
    
    original_text: str = """- 分字分词释义：

  - **大小二限过宫**：大限、小限经过十二宫位的运行过程。
  - **十二支人所忌**：以出生年地支为核心，标记每类人在特定岁限、宫位的禁忌组合。
  - **灾悔官非孝服**：触发禁忌组合时易发的典型灾象，包括讼讼、丧亲、打官司等。
  - **火盗破财刑伤**：触发禁忌组合时易发的另一类灾象，包括火灾、盗端、破财、刑伤。
  - **天罗地网**：辰戜两宫形成的束缚格局，巳辰生人行到此宫易遇水厄、官非、忧制连连。
  - **四墓宫**：丑辰未戜四宫，擎羊落此时易主病患与损失。
  - **冲支组合**：寅申、子午、卯酉等对冲关系，冲则动荡、激发、风险骤增。
  - **歌诀警示**：「猪犬莫遇陀，辰戜切忌纲罗」，亥戜生人遇陀罗与天罗地网风险极高。

- 原文（断句）：

  论大小二限星辰过十二宫遇十二夫人所忌诀：

  遇此主灾悔，官非孝服，火盗破财，刑伤，死亡立见。

  人生子命忌寅申，假如子年生人，切忌寅申岁限，灾悔至重。及忌子午岁限相冲。

  丑午生人丑午嗔。假如丑生人忌午丑岁限，午生人亦忌丑午岁限，及忌七杀星，灾悔极重。

  寅卯之人防已亥，假如寅卯人忌己亥岁限，及忌卯酉寅申相冲。

  蛇龙切忌本身临。假如巳生人忌逢巳年，及忌行到巳限；辰生人忌行辰年，及忌行到辰限为天罗，文忌到戍为地纲限，遇此主灾殃水厄之险，官非破财，忧制连连。

  申人铃火灾殃重。假如申生人，忌逢火铃二星，必主灾悔至重，及忌寅年冲。

  未遇猪鸡墓患殷。假如未生忌逢酉亥岁限，又忌见擎羊在四墓宫。

  戍亥羊陀须避忌。假如戍亥生人，忌遇羊陀，灾重。戍生人又忌行到戌宫岁限为地网，又忌行到辰宫岁限为天罗，为之辰戌相冲，不美。

  酉人陀刃亦非亲。假如酉生人亦忌羊陀星岁限，及忌行卯宫限，及卯年岁君相冲。

  歌：猪犬生人莫遇陀，辰戍切忌到纲罗。

  曰：预先整顿衣冠木，未免生人唱挽歌。

- 规范化释义（primary_lang_explained）：

  本条以「十二支人所忌」为纲，从出生年地支出发，列出在大小限与岁限（流年）中最需回避的方位与星曜组合。第一句总括指出：当大小二限或流年走到命主本身忌讳之支位，或遇上特定杀曜时，容易引发灾悔、官非、孝服、火盗、破财、刑伤乃至死亡等重凶事件。后文则逐一分述：如子年生人忌寅申两个冲位及子午相冲之岁限；丑、午年生人互忌对方岁限并忌七杀；寅卯生人忌己亥之岁限及卯酉寅申相冲；巳辰生人忌行到本支及辰戌天罗地网等，皆是通过「出身支」与「行限支」之间的冲击关系，来标记高危年份与十年段。

  对于申、未、戌亥、酉等生人，原文又额外点名某些恶星：如申生人逢火星、铃星则灾象加重；未生人逢酉亥岁限且擎羊在四墓宫，主病患与损失；戌亥生人逢羊陀，或走地网、天罗，则忧患连连；酉生人逢羊陀与卯宫冲限，易见官非、刑伤。最后一首歌谣以「猪犬莫遇陀，辰戍切忌纲罗」收束，提醒亥戌等支生人一旦行到辰戌天罗地网且兼遇陀罗，需以「提前整顿衣冠」的态度对待该年大限。整体而言，此条提供的是一张「出生支 × 行限支 × 杀曜」的危险对照表，用以筛查特别需要谨慎的年份，而非宣告命运必然。

- 完整对等诠释（secondary_lang_full）：

  This rule offers a compact table of taboo combinations between a person's
  birth branch and later periods or annual years. For each of the twelve
  Earthly Branch types it lists the branches and houses that should be treated
  with special caution when major periods, minor periods or the annual ruler
  pass through them, especially when harsh stars such as Qingyang, Tuoluo,
  Mars, Bell or Qisha are also present. The text warns that in these taboo
  combinations one is more prone to lawsuits, mourning, fires and theft,
  financial loss, injuries and in extreme cases death. Verses like "pig and dog
  births must not meet Tuoluo; Chen and Xu must avoid the nets" underline how
  seriously such years were viewed.

  Read as a modern practitioner, this is less a sentence of doom and more a
  list of red-flag configurations. It assumes that one has already judged the
  quality of major and minor periods and then uses birth-branch taboos to
  highlight years where risk is unusually concentrated or where old weaknesses
  are easily triggered. Used this way, the rule becomes a tool for prioritising
  caution and preventive action in specific windows, rather than a reason to
  label whole classes of years as unlivable.

- 核心要点：

  1. 以出生年地支为起点，为每一类人标出在大小限与岁限中需严防的冲支与杀曜组合。
  2. 重点危险标签包括：寅申、子午、巳辰本支、辰戌天罗地网、羊陀、火铃、擎羊在四墓宫等。
  3. 灾象范围涵盖官非孝服、火盗破财、刑伤水厄乃至死亡，是「高危年份筛查表」，不是日常每年的常态描述。
  4. 歌诀「猪犬莫遇陀，辰戍切忌纲罗」强化亥戌生人遇陀罗与天罗地网的极高风险。
  5. 现代应用时，应将本条视为在大限、小限与太岁已经偏凶时的加权指标，而不是单凭出生支与一两个岁限就断大祸必至。"""
    normalized_text_zh: str = """"""
    subject: str = "论大小二限而辰过十二宫遇十二支人所忌诀"
    factor_refs: list = ['system_shiershisuoji', 'system_suixian', 'pattern_tianluodiwang', 'group_simugong', 'star_huoling', 'source_ref', 'rel_suoji_001', 'type_shengnianzhi', 'rel_suoji_002', 'pattern_tianluodiwang', 'rel_suoji_003', 'star_huoling', 'evi_suoji_001', 'system_shiershisuoji', 'rule_suoji_zaihui', 'evi_suoji_002', 'pattern_tianluodiwang', 'rule_suoji_tianluodiwang', 'concept_branch_taboo', 'concept_net_trap']
    
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
        l1_anchor="zw_v1.0.0_论大小二限而辰过十二宫遇十二支人所忌诀_001_L1",
    )
    version: str = "1.0.0"
