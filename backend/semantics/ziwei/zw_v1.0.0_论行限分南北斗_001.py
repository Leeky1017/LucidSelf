"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755776
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
    semantic_id="zw_v1.0.0_论行限分南北斗_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论行限分南北斗(SemanticEntry):
    """
    - 分字分词释义：

  - **行限分南北斗**：根据星曜所属的南斗或北斗系统，细化行限应验的时间段。
  - **南斗**：包括天同、天梁、天机、天相、天府、七杀等星，与寿福护持相关。
  - *...
    """
    
    original_text: str = """- 分字分词释义：

  - **行限分南北斗**：根据星曜所属的南斗或北斗系统，细化行限应验的时间段。
  - **南斗**：包括天同、天梁、天机、天相、天府、七杀等星，与寿福护持相关。
  - **北斗**：包括紫微、贪狼、巨门、廉贞、武曲、破军等星，与权势转折相关。
  - **阳男阴女南斗为福**：阳性男命、阴性女命以南斗星系为福位，行限遇南斗星时增益更直接。
  - **阴男阳女北斗为福**：阴性男命、阳性女命以北斗星系为福位，行限遇北斗星时扶助更明显。
  - **上五年/下五年**：十年大限分为前后两段，北斗吉凶应上五年，南斗吉凶应下五年。
  - **上半年/下半年**：小限一年分为前后两段，北斗应上半年，南斗应下半年。
  - **应期细化**：通过南北斗与上下段的对应，将吉凶事件的时间窗口进一步精准化。

- 原文（断句）：

  论行限分南北斗：

  阳男阴女，南斗为福；阴男阳女，北斗为福。北斗诸星吉凶，大限断上五年应，小限断上半年应。南斗诸星吉凶，大限断下五年应，小限断下半年应。

- 规范化释义（primary_lang_explained）：

  本条在前述限运规则的基础上，引入「南北斗」与性别阴阳的分判方法，用以细化行限应期。首先，从人之阴阳与星系的南、北斗对应出发：阳男、阴女以南斗为福位；阴男、阳女则以北斗为福位。也就是说，同一行限若落在南斗星系，对于阳男与阴女的增益往往更直接；同理，若落在北斗星系，对阴男与阳女的扶助更明显，这是一种按性别与体用阴阳来区分「哪一斗更护持你」的传统视角。

  其次，本条把「一限十年」再切成上下两段：大限十年中，北斗所主的吉凶多应在上五年，而南斗所主的吉凶多应在下五年；小限则以上下半年划分——北斗应上半年，南斗应下半年。换言之，当我们判断某十年或某年中吉凶事情出现的时间点时，不仅要看星宿落在南斗还是北斗，还要结合命主性别阴阳，以及该十年是行限的前半期还是后半期、该年是上半年还是下半年，才能对「何时应验」做出更细致的估计。

- 完整对等诠释（secondary_lang_full）：

  This brief rule refines timing within a period by dividing both people and
  stars into south and north Dipper types. It states that yang men and yin women
  are more strongly blessed by the South Dipper, while yin men and yang women
  are more attuned to the North Dipper. In practice this means that when a
  travelling period falls under the South Dipper system, it tends to favour yang
  males and yin females more directly; when it falls under the North Dipper, it
  more readily supports yin males and yang females.

  The text then splits each major and minor period into two halves. Within a
  ten-year major period, the influences of the North Dipper are said to show
  themselves mainly in the first five years, while South Dipper influences peak
  in the last five. Likewise for a one-year minor period, the North Dipper is
  associated with the first half of the year and the South Dipper with the
  second. Read together with broader judgments about the quality of a period,
  this rule acts as a coarse timing tool, pointing to whether key events are
  likelier to cluster in the earlier or later part of a decade or year.

- 核心要点：

  1. 阳男、阴女以南斗为福；阴男、阳女以北斗为福，是基于性别与阴阳属性对南北斗分福祸。
  2. 北斗诸星的吉凶，多在大限上五年、小限上半年体现；南斗诸星的吉凶，多在大限下五年、小限下半年体现。
  3. 行限判断不仅要看「哪一斗吉凶」，还要看行到十年中的上半段或下半段，以细化时间应期。
  4. 此法主要用于在已有大格局判断后，进一步微调「何年、何半年」较易应吉或应凶。
  5. 现代实务中可结合具体年运、现实环境，将「南北斗 + 上下段」视为应期的加权提示，而非绝对定数。"""
    normalized_text_zh: str = """"""
    subject: str = "论行限分南北斗"
    factor_refs: list = ['group_nandou', 'group_beidou', 'type_yangnanyinnv', 'type_yinnanyangnu', 'timing_shangxia', 'source_ref', 'rel_nanbei_001', 'type_yangnanyinnv', 'rel_nanbei_002', 'type_yinnanyangnu', 'rel_nanbei_003', 'timing_shangxia', 'evi_nanbei_001', 'type_yangnanyinnv', 'rule_nanbei_fuwei', 'evi_nanbei_002', 'timing_shangxia', 'rule_nanbei_wunian', 'concept_dipper_system', 'concept_period_half']
    
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
        l1_anchor="zw_v1.0.0_论行限分南北斗_001_L1",
    )
    version: str = "1.0.0"
