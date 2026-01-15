"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997406
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
    semantic_id="dts_v1.0.0_化得真者只论化_化神还有几般话_001",
    book_id="dts",
    engine_id="bazi"
)
class 化得真者只论化化神还有几般话(SemanticEntry):
    """
    - **原文（source_text）**：
  化得真者只论化，化神还有几般话。

- 原注（原文注解）：
  　　如甲日主，生于四季，单遇一位己土，在月时上作合，（在年干不是）不遇壬癸甲乙庚（印，...
    """
    
    original_text: str = """- **原文（source_text）**：
  化得真者只论化，化神还有几般话。

- 原注（原文注解）：
  　　如甲日主，生于四季，单遇一位己土，在月时上作合，（在年干不是）不遇壬癸甲乙庚（印，劫，官），乃为化得真，（庚能克甲）又如丙辛生于冬月，（化神要通月令）戊癸生于夏月，乙庚生于秋月，丁壬生于春月，独相作合，皆为真化，既化矣，又论化神，如甲己化土，土遇阴寒，要火为印，如土太旺，又要水为财，木为官，金为食伤，随其所在意向，合其喜忌，再见甲乙亦不以争合妒合论，盖化者，如烈女不更二囚，岁运遇之，皆闲神也。

- 分字分词释义：
  - 化：由本性转为他性，如甲己化土。
  - 化神：化后的主神（如甲己化土，则土为化神）。
  - 真化：合局专一、通月令、无他神搅扰之化。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 化 | Transform (Hua) | 由本性转为他性 | Original transforms to another | hua | existing |
| 真化 | True Transformation | 合专通令无他助 | Strict transformation | zhenhua | existing |
| 化神 | Transformation Spirit | 化后之主神 | New master after transform | huashen | existing |
| 合神 | Merging Spirit | 与日主相合之神 | Spirit merging with DM | heshen | existing |
| 通令 | Rooted in Season | 得月令之气 | Supported by month | tongling | existing |
| 独合 | Exclusive Merge | 专一相合不杂 | No competition in merge | duhe | new_candidate |

- **规范化释义（primary_lang_explained）**：
  真化之格，重在“合专、通令、无他助”。如甲日生四季，专遇己土在月时上作合，又不见壬癸甲乙庚等来破合，则甲己化土为真；又如丙辛、戊癸、乙庚、丁壬，各依春夏秋冬通令之合，独相作合而不杂，亦为真化。既化之后，原神便不再单独论用，而随化神为主：如甲己化土，则以土为本，看土在阴寒则要火为印，在太旺则要水为财、木为官、金为食伤。再见原来的甲乙等，也不再以“争合、妒合”论之，因为“化者如烈女不更二夫”，原神岁运再现，多为闲神。

- **次语种完整诠释（secondary_lang_full）**:  
  True-Transform真化 requires通令+独合+无他助 ling-exclusive-clean: 甲己/丙辛/戊癸/乙庚/丁壬 five-pairs专一合 exclusive-merge通月令 rooted-in-season无印劫官 no-interference enabling原神转化 original-transforms—化得真 true-hua只论化神 transform-spirit-as-body not原神 original-retired; 化神喜忌 transform-preferences via寒暖财官 temperature-wealth-official requiring助化神 supporting-hua-shen忌破化 avoiding-破structure."""
    normalized_text_zh: str = """"""
    subject: str = "化得真者只论化，化神还有几般话。"
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
        l1_anchor="dts_v1.0.0_化得真者只论化_化神还有几般话_001_L1",
    )
    version: str = "1.0.0"
