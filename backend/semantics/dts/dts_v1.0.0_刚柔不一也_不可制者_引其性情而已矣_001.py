"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997496
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
    semantic_id="dts_v1.0.0_刚柔不一也_不可制者_引其性情而已矣_001",
    book_id="dts",
    engine_id="bazi"
)
class 刚柔不一也不可制者引其性情而已矣(SemanticEntry):
    """
    - **原文（source_text）**：
  刚柔不一也，不可制者，引其性情而已矣。

- 原注（原文注解）（节选关键）：
 　　刚柔相济，不必言也，若夫刚者济之以柔，而不得其情，反助其刚矣，譬之...
    """
    
    original_text: str = """- **原文（source_text）**：
  刚柔不一也，不可制者，引其性情而已矣。

- 原注（原文注解）（节选关键）：
 　　刚柔相济，不必言也，若夫刚者济之以柔，而不得其情，反助其刚矣，譬之武人而得士卒，则成杀伐，如庚辛生于七月，遇丁火而激其威，遇乙木而助其暴，遇己土而成其志，遇癸水而益其锐，不如以柔之刚者济之可也。壬水是也，盖壬水有正性，能引通庚之情故也，若以刚者激之，其祸可胜言哉！柔者济之以刚，而不得其情，反其柔矣，譬之妇人而遇恩威，则成淫贱，如乙木生于八月，遇甲丙壬而喜则舒情，遇戊寅庚而畏则失身，不如以刚之柔者济之可也，丁火是也，盖丁火有正性，能定乙木之情故也，若以柔之柔者合之，其弊何所底乎，馀仿此。

- 分字分词释义：
  - 刚：偏于金水之刚劲、决断、克制之性。
  - 柔：偏于木火之柔和、包容、顺应之性。
  - 不可制：不可一味以强力压制。
  - 引其性情：顺其本性，以导引方式调和之。

- **规范化释义（primary_lang_explained）**：
  刚柔之道重在“因性而引”，不可一味“强制”。刚者不宜再以纯刚激之，柔者不宜再以纯柔合之；须取“刚之柔/柔之刚”的中介来引导归中，使其性情有所安顿，而非互相激发成祸。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 刚柔 | Hard-Soft (Gang-Rou) | 阳刚与阴柔 | Yang Hardness and Yin Softness | gangrou | existing |
| 不可制 | Cannot be Controlled | 不可强力压制 | Cannot be forcefully suppressed | bukezhi | new_candidate |
| 引其性情 | Guide its Nature | 顺性导引 | Guide according to nature | yin_qixingqing | new_candidate |
| 刚之柔 | Softness within Hard | 如壬水引庚金 | Like Ren Water guiding Geng Metal | gang_zhirou | new_candidate |
| 柔之刚 | Hardness within Soft | 如丁火定乙木 | Like Ding Fire stabilizing Yi Wood | rou_zhigang | new_candidate |
| 性情 | Nature and Sentiment | 五行本性 | Nature of the elements | xingqing | existing |


- **次语种完整诠释（secondary_lang_full）**:  
  Gang-Rou (Hard-Soft) theory: "Cannot be controlled" (不可制) means do not force it, but "guide its nature" (引其性情). Do not control Hard with Pure Hard (leads to violence), nor Soft with Pure Soft (leads to weakness). Use "Soft within Hard" (e.g. Ren Water for Geng Metal) or "Hard within Soft" (e.g. Ding Fire for Yi Wood) to guide and stabilize."""
    normalized_text_zh: str = """"""
    subject: str = "刚柔不一也，不可制者，引其性情而已矣。"
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_刚柔不一也_不可制者_引其性情而已矣_001_L1",
    )
    version: str = "1.0.0"
