"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147408
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
    semantic_id="ca_v1.0.0_relationship_questions___marri_001",
    book_id="christian_astrology",
    engine_id="astro"
)
class RelationshipQuestionsMarri(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 1st-7th axis | Self-Other axis | Querent vs partner houses | All relationship questions |
| Reception | Receptio | Planet in another's dignity | Mutual welcome indicator |
| Translation of light | Translatio luminis | Third planet connecting two | Intermediary facilitates |
| Combust | Combustus | Within 8° of Sun | Overwhelmed, weakened |

**Source Text** (Synthesized from Lilly Book II):
> In questions concerning marriage, the Ascendant and its Lord represent the Querent; the 7th House and its Lord the Quesited (proposed spouse). If there be Application between the two Lords by Sextile, Trine, or (in some cases) Conjunction or Square, with Reception, marriage may follow. If separation, or neither application nor reception exists, marriage is denied.

**English Paraphrase (Primary Language)**:

**Marriage/Partnership questions** use the 1st–7th house axis:

| Significator | Meaning |
|--------------|---------|
| Ascendant Lord (L1) | Querent (person asking) |
| 7th House Lord (L7) | Proposed partner |
| Moon | Co-significator of querent, event flow |
| Venus | General significator of love/women |
| Sun | General significator of men |

**Judgment patterns**:

| Configuration | Outcome |
|--------------|---------|
| L1–L7 applying with reception | Marriage likely; mutual interest |
| L1–L7 applying without reception | Marriage possible but one-sided |
| L1–L7 separating | Missed opportunity; relationship ending |
| L1 or L7 combust/retrograde | Party is weakened/unwilling |
| Translation of light (3rd planet) | Third party facilitates union |

**Timing**: Degrees to perfection = time units (context determines days/weeks/months).

**Complete Chinese Interpretation (Secondary Language)**:

**婚姻/合作问题**使用 1–7 宫轴：

| 象征星 | 含义 |
|--------|------|
| 上升主星 (L1) | 问卜者（提问人） |
| 第七宫主星 (L7) | 被问对象（潜在伴侣） |
| 月亮 | 问卜者的副象征星、事件流 |
| 金星 | 爱情/女性的一般象征星 |
| 太阳 | 男性的一般象征星 |

**判断模式**：

| 配置 | 结果 |
|------|------|
| L1–L7 入相且有互容 | 婚姻可能；双方有意 |
| L1–L7 入相但无互容 | 婚姻可能但单方面 |
| L1–L7 出相 | 错过机会；关系结束 |
| L1 或 L7 焦伤/逆行 | 一方弱化/不愿意 |
| 光的传递（第三行星） | 第三方促成结合 |

**时间**：到成相的度数 = 时间单位（语境决定天/周/月）。

**Core Points**:
- 1st–7th axis for all partnership questions.
- Application with reception = mutual interest.
- Translation of light = intermediary facilitates.
- Combust/retrograde = party weakened or unwilling.

#### Narrative Snippets

- `[ns_lilly_023]` `[trigger: horary_marriage]` `[factor_trigger: horary_7th_house]` `[role: 主干]` In questions concerning marriage, the Ascendant and its Lord represent the Querent; the 7th House and its Lord the Quesited spouse. → Christian Astrology Marriage
- `[ns_lilly_024]` `[trigger: application_reception]` `[factor_trigger: aspect_application AND reception AND astro_marriage_success]` `[role: 主干依赖]` If there be Application between the two Lords by Sextile, Trine, or Conjunction with Reception, marriage may follow. If separation, marriage is denied. → Christian Astrology Marriage
- `[ns_lilly_025]` `[trigger: translation_light]` `[factor_trigger: translation_of_light AND astro_intermediary_union]` `[role: 条件分支]` Translation of light: a third planet separating from one significator and applying to another facilitates union through intermediary. → Christian Astrology Marriage
- `[ns_lilly_026]` `[trigger: combust_retrograde]` `[factor_trigger: combust OR retrograde AND astro_party_weakness]` `[role: 总结]` L1 or L7 combust or retrograde indicates that party is weakened, overwhelmed, or unwilling to proceed. → Christian Astrology Marriage

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Lilly devotes extensive chapters to marriage questions, reflecting 17th-century social importance. The 1st-7th axis is universal for "self vs other" questions. "Reception" (planet in another's dignity) indicates mutual welcome—a key medieval Arabic technique. Modern practitioners add outer planets for unconventional relationships.
- **中文**: Lilly用大量章节讨论婚姻问题，反映了17世纪的社会重要性。1-7宫轴适用于所有"自我vs他人"问题。"接纳"（行星在另一行星的尊贵）表示相互欢迎——关键的中世纪阿拉伯技术。现代实践者为非传统关系添加外行星。"""
    normalized_text_zh: str = """"""
    subject: str = "Relationship Questions – Marriage and Partnership"
    factor_refs: list = ['horary_1_7_axis', 'reception', 'translation_of_light', 'combust', 'aspect_application', 'aspect_separation']
    
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
        book_id="christian_astrology",
        chapter="",
        l1_anchor="ca_v1.0.0_relationship_questions___marri_001_L1",
    )
    version: str = "1.0.0"
