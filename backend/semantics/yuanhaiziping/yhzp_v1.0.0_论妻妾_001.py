"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559153
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
    semantic_id="yhzp_v1.0.0_论妻妾_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论妻妾(SemanticEntry):
    """
    - **原文（source_text）**：正财为正妻，偏财妾也。甲木见己土为正财，戊土为偏财。财衰败墓绝，主妻有疾不贤，否则年高再嫁。比肩分夺、财临沐浴桃花，主妻妾私通。日下月下坐财官，主妻多内助，...
    """
    
    original_text: str = """- **原文（source_text）**：正财为正妻，偏财妾也。甲木见己土为正财，戊土为偏财。财衰败墓绝，主妻有疾不贤，否则年高再嫁。比肩分夺、财临沐浴桃花，主妻妾私通。日下月下坐财官，主妻多内助，更得妻财。偏财得位，妾胜于妻。财多身弱，妻反胜夫。财命有气，妻妾和顺，是得妻力。日坐空亡，难为妻妾。

- **分字分词释义**：
  - **正财为正妻**：正财（我克且阴阳相异者）代表正妻。
  - **偏财妾也**：偏财（我克且阴阳相同者）代表妾室。
  - **甲见己为正财**：甲木克己土，阴阳相异为正财。
  - **戊为偏财**：甲木克戊土，阴阳相同为偏财。
  - **财衰败墓绝**：财星临衰败墓绝之地，主妻不利。
  - **比肩分夺**：比劫夺财，主妻妾受损或不贞。
  - **沐浴桃花**：财星临沐浴桃花，主妻妾淫乱。
  - **日下月下坐财官**：日柱月柱坐财官，主妻贤内助。
  - **偏财得位**：偏财旺相得势，妾胜于正妻。
  - **财多身弱**：财星过旺日主太弱，妻强夫弱。
  - **日坐空亡**：日支落空亡，难得妻妾之福。

- **规范化释义（primary_lang_explained）**：妻妾以十神财星定位，正财为正妻偏财为妾。财星衰败墓绝主妻疾病不贤或年长再嫁；比劫分夺或财临桃花主妻妾不贞；财多身弱主妻强夫弱；财有气主妻贤内助。日坐财官得妻财助；日坐空亡难为妻妾。

- **完整对等诠释（secondary_lang_full）**：Wife and concubine positioned via Wealth Stars—Direct Wealth as legitimate wife, Indirect Wealth as concubine. Weak/declining/tomb/extinct Wealth indicates sick/unkind wife or remarrying widow; Rob-Wealth seizing or Wealth in peach-blossom brings unfaithful wife/concubine; abundant Wealth with weak Self brings wife dominating husband; prosperous Wealth brings capable supportive wife. Day sitting Wealth-Officer gains wife's wealth/support; Day sitting void brings difficult marriage.

- **核心要点**：
  - 正财为正妻，偏财为妾
  - 财星衰败墓绝，主妻有疾不贤
  - 比肩分夺、财临桃花，主妻妾私通
  - 日坐财官，主妻多内助，得妻财
  - 偏财得位，妾胜于妻
  - 财多身弱，妻反胜夫
  - 财命有气，妻妾和顺
  - 日坐空亡，难为妻妾

- **详细解说**：  
  本条论述妻妾的判断方法。"正财为正妻，偏财妾也"——以财星定位妻妾，正财（我克且阴阳相异者）代表正妻，偏财（我克且阴阳相同者）代表妾室。妻不利的情况是"财衰败墓绝，主妻有疾不贤"——财星无力主妻不贤或有病；"比肩分夺、财临沐浴桃花，主妻妾私通"——比劫夺财或财临桃花主妻不贞。妻贤的情况是"日下月下坐财官，主妻多内助"——日月坐财官主妻贤能助夫；"财命有气，妻妾和顺，是得妻力"——财星有气主妻贤内助。特殊情况是"偏财得位，妾胜于妻"——偏财旺则妾室得势；"财多身弱，妻反胜夫"——财旺身弱主惧内；"日坐空亡，难为妻妾"——日支空亡主婚姻不顺。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_182]` `[trigger: 正财为妻]` `[factor_trigger: direct_wealth_wife AND indirect_wealth_concubine]` `[role: 主干]` 正财为正妻，偏财妾也。 → 《渊海子平·论妻妾》
  - `[ns_yhzp_183]` `[trigger: 财衰败主妻不贤]` `[factor_trigger: direct_wealth_wife AND wealth_strength]` `[role: 条件分支]` 财衰败墓绝，主妻有疾不贤，否则年高再嫁。 → 《渊海子平·论妻妾》
  - `[ns_yhzp_184]` `[trigger: 妻妾私通]` `[factor_trigger: rob_seizing_wealth AND wealth_peach_blossom]` `[role: 例外处理]` 比肩分夺、财临沐浴桃花，主妻妾私通。 → 《渊海子平·论妻妾》
  - `[ns_yhzp_185]` `[trigger: 妻多内助]` `[factor_trigger: direct_wealth_wife AND direct_officer]` `[role: 条件分支]` 日下月下坐财官，主妻多内助，更得妻财。 → 《渊海子平·论妻妾》
  - `[ns_yhzp_186]` `[trigger: 妾胜于妻]` `[factor_trigger: indirect_wealth_concubine AND concubine]` `[role: 条件分支]` 偏财得位，妾胜于妻。 → 《渊海子平·论妻妾》
  - `[ns_yhzp_187]` `[trigger: 妻胜夫]` `[factor_trigger: abundant_wealth_weak_self]` `[role: 条件分支]` 财多身弱，妻反胜夫。 → 《渊海子平·论妻妾》
  - `[ns_yhzp_188]` `[trigger: 日坐空亡难妻]` `[factor_trigger: day_void AND nan_wei_qiqie]` `[role: 总结]` 日坐空亡，难为妻妾。 → 《渊海子平·论妻妾》

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|----------|-----------|--------|
| 正财为妻 | Direct Wealth as Wife | 我克且阴阳相异者代表正妻 | What-I-control opposite polarity represents legitimate wife | direct_wealth_wife | existing |
| 偏财为妾 | Indirect Wealth as Concubine | 我克且阴阳相同者代表妾室 | What-I-control same polarity represents concubine | indirect_wealth_concubine | existing |
| 财多身弱 | Abundant Wealth Weak Self | 财星过旺日主太弱主妻强夫弱 | Excessive Wealth with weak Day Master brings wife dominating husband | abundant_wealth_weak_self | existing |
| 比劫夺财 | Rob-Wealth Seizing | 比劫克财星主妻妾不贞或多争 | Parallel/Rob controlling Wealth brings unfaithful wives | rob_seizing_wealth | existing |
| 财临桃花 | Wealth in Peach-Blossom | 财星坐沐浴桃花主淫乱 | Wealth sitting bathing/peach-blossom brings promiscuity | wealth_peach_blossom | existing |"""
    normalized_text_zh: str = """"""
    subject: str = "论妻妾"
    factor_refs: list = []
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_论妻妾_001_L1",
    )
    version: str = "1.0.0"
