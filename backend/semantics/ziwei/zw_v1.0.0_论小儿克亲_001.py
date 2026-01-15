"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755733
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
    semantic_id="zw_v1.0.0_论小儿克亲_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论小儿克亲(SemanticEntry):
    """
    - 分字分词释义：

  - **小儿克亲**：小儿命局中对父母有刑克风险的格局，多指早年可能出现亲子分离、丧亲或家庭变故。
  - **辰戌丑未生人**：生年地支为四墓（辰、戌、丑、未）的人，属于"...
    """
    
    original_text: str = """- 分字分词释义：

  - **小儿克亲**：小儿命局中对父母有刑克风险的格局，多指早年可能出现亲子分离、丧亲或家庭变故。
  - **辰戌丑未生人**：生年地支为四墓（辰、戌、丑、未）的人，属于"土重困亲"的敏感群体。
  - **见辰戌丑未时最毒**：生年与生时同属四墓组，形成"墓对墓"的叠加，对家道与亲缘打击最重。
  - **先克父**：子寅卯巳一组逢午申酉亥一组的时支或岁运，古法认为父系亲缘先受冲击。
  - **先克母**：辰巳丑未一组逢子午卯或巳亥申酉一组，古法认为母系亲缘先受损害。
  - **出十六岁不论**：十六岁为古法强调的"克亲应验窗口"，过此年龄则不再以此规则严格判断。
  - **地支分组**：将十二地支分为若干组别（四墓、子寅卯巳、午申酉亥等），用于简化克亲判断。
  - **克亲风险指标**：现代解读应将"克亲"理解为早年亲子关系脆弱的风险信号，而非必然的丧亲宣判。

- 原文（断句）：

  论小儿克亲：

  如辰戌丑未生人，见辰戌丑未时最毒。如子寅卯巳生人，见午申酉亥时，主先克父，出十六岁不论。如辰巳丑未生人，见子午卯、巳亥申酉生时者，主先克母。

- 规范化释义（primary_lang_explained）：

  本条以十二支的分组与生时、岁运的交会，来提醒小儿命中「克亲」的敏感组合。第一句说：若命局以辰、戌、丑、未四墓地为生年支，且又在生时或早年大运流年反复遇到同为辰戌丑未一组的时支或岁运，古法认为这是对父母、家道打击最重的一类「土重困亲」格局，易见早年家庭灾变或亲缘不稳。第二句与第三句，则将地支分成几组：子、寅、卯、巳一组在命局或行运中又重叠午、申、酉、亥一组时，被视为「先克父」的信号；辰、巳、丑、未一组逢子、午、卯与巳、亥、申、酉一组，则被视为「先克母」的信号，并特别强调十六岁以前为应验高峰，出此年龄则不再作严格论断。

- 完整对等诠释（secondary_lang_full）：

  This section describes combinations that are said to make an infant "cut off"
  or severely afflict their parents. It groups the twelve branches into sets and
  then looks at how the child's natal branch and key hours or periods repeat or
  clash. Charts rooted in the four grave branches (Chen, Xu, Chou, Wei) and
  repeatedly meeting the same group are treated as especially heavy on the
  family. Another pattern links children born under Zi, Yin, Mao or Si with
  later encounters with Wu, Shen, You or Hai, which tradition associates with a
  greater risk of early harm to the father. A third pattern links births in
  Chen, Si, Chou or Wei to meetings with Zi, Wu, Mao or with Si, Hai, Shen, You,
  which is framed as "first harming the mother". The age of sixteen is taken as
  a threshold beyond which these specific warnings are no longer applied.

  In a contemporary reading, such "parent-clashing" indications are better
  understood as markers of vulnerability in early family bonds rather than fixed
  sentences of parental death. They may point to higher chances of illness,
  separation, divorce, migration, fosterage or other forms of disruption to the
  parent–child relationship. Even when the combinations look severe, they must
  be judged together with the parents' palaces, protective stars and the actual
  social context. These patterns are most useful as prompts for extra care and
  support around parent–child connection, not as curses that must inevitably be
  fulfilled.

- 核心要点：

  1. 以地支分组观小儿对双亲的刑克趋势，辰戌丑未反复相逢被视为对家道打击最重的组合。
  2. 子寅卯巳一组逢午申酉亥时支或岁运，多被古书归为「先克父」的高风险配置。
  3. 辰巳丑未一组逢子午卯与巳亥申酉一组，则被视为「先克母」的高风险组合。
  4. 十六岁以前为古法强调的应验窗口，过此年龄则不再以「先克父母」论之。
  5. 现代解读应把「克亲」扩展为早年亲子关系与家庭结构的脆弱性指标，须合盘与现实条件谨慎使用。"""
    normalized_text_zh: str = """"""
    subject: str = "论小儿克亲"
    factor_refs: list = ['pattern_xiaoerkeqin', 'group_simudi', 'pattern_xianke', 'timing_shiliusui', 'system_xingyunzhizu', 'source_ref', 'rel_keqin_001', 'group_simudi', 'rel_keqin_002', 'pattern_xianke', 'rel_keqin_003', 'timing_shiliusui', 'evi_keqin_001', 'group_simudi', 'rule_keqin_simudi', 'evi_keqin_002', 'timing_shiliusui', 'rule_keqin_shiliusui', 'concept_parent_harm', 'concept_childhood']
    
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
        l1_anchor="zw_v1.0.0_论小儿克亲_001_L1",
    )
    version: str = "1.0.0"
