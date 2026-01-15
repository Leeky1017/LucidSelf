"""
Auto-generated semantic module for christian_astrology
Generated at: 2025-12-05T13:30:20.147421
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
    semantic_id="ca_v1.0.0_career_and_finance_questions___001",
    book_id="christian_astrology",
    engine_id="astro"
)
class CareerAndFinanceQuestions(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Latin/English | Definition | Significance |
|------|---------------|------------|---------------|
| 10th house | Domus X / Medium Coeli | Career, profession, public status | Employer, position sought |
| 6th house | Domus VI | Daily work, service | Job itself, labor conditions |
| 2nd house | Domus II | Movable wealth, income | Salary, personal resources |
| 11th house | Domus XI | Hopes, gains | Benefits from profession |

**English Paraphrase (Primary Language)**:

**Career/Job questions** primarily use:

| House | Meaning |
|-------|---------|
| 10th | Career, profession, reputation, employer |
| 6th | Daily work, service, subordinates |
| 2nd | Personal income, movable wealth |
| 11th | Hopes, gains from profession |

**Job application pattern**:

| Significator | Meaning |
|--------------|---------|
| L1 | Querent (applicant) |
| L10 | Employer/position |
| L6 | The job itself (daily work) |

**Judgment patterns**:

| Configuration | Outcome |
|--------------|---------|
| L1 applying to L10 with reception | Good chance; employer receptive |
| L10 applying to L1 | Employer seeks querent |
| L1 in 10th, dignified | Strong position; success |
| L1/L10 afflicted or retrograde | Obstacles; delays |

**Complete Chinese Interpretation (Secondary Language)**:

**职业/工作问题**主要使用：

| 宫位 | 含义 |
|------|------|
| 第10宫 | 事业、职业、声誉、雇主 |
| 第6宫 | 日常工作、服务、下属 |
| 第2宫 | 个人收入、动产 |
| 第11宫 | 希望、职业所得 |

**求职模式**：

| 象征星 | 含义 |
|--------|------|
| L1 | 问卜者（申请人） |
| L10 | 雇主/职位 |
| L6 | 工作本身（日常劳动） |

**Core Points**:
- 10th = employer/profession; 6th = daily work; 2nd = income.
- Application with reception = favorable hiring.
- L1 in 10th dignified = strong candidacy.

#### Narrative Snippets

- `[ns_lilly_027]` `[trigger: horary_career]` `[factor_trigger: horary_10th_house]` `[role: 主干]` For career questions: 10th house = employer/profession/status; 6th house = daily work itself; 2nd house = income. → Christian Astrology Career
- `[ns_lilly_028]` `[trigger: job_application]` `[factor_trigger: L1_L10_aspect AND astro_employer_receptive]` `[role: 主干依赖]` L1 applying to L10 with reception indicates employer is receptive; L10 applying to L1 means employer seeks the querent. → Christian Astrology Career
- `[ns_lilly_029]` `[trigger: career_success]` `[factor_trigger: L1_in_10th AND dignity AND astro_career_success]` `[role: 总结]` L1 in 10th house dignified = strong candidacy, favorable position for professional success. → Christian Astrology Career

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: The 10th house for career derives from its position at the meridian (highest visibility). The 6th house for daily labor comes from its traditional association with servants and service. Lilly's distinction (10th = status/employer, 6th = actual work) remains standard. Modern adaptations address self-employment (1st-10th blend) and gig economy.
- **中文**: 第10宫用于事业源于其在子午线的位置（最高可见度）。第6宫用于日常劳动源于其与仆人和服务的传统关联。Lilly的区分（第10宫=地位/雇主，第6宫=实际工作）仍是标准。现代改编处理自雇（1-10宫混合）和零工经济。"""
    normalized_text_zh: str = """"""
    subject: str = "Career and Finance Questions – Job and Wealth"
    factor_refs: list = ['house_10_mc', 'house_6_service', 'house_2_wealth', 'house_11_gains']
    
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
        l1_anchor="ca_v1.0.0_career_and_finance_questions___001_L1",
    )
    version: str = "1.0.0"
