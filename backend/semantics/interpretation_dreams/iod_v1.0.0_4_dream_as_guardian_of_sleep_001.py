"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.461053
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
    semantic_id="iod_v1.0.0_4_dream_as_guardian_of_sleep_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class 4DreamAsGuardianOfSleep(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Guardian of Sleep | Dream's function | Preserves sleep |
| Hallucinatory Satisfaction | Appeases wish | Temporary fulfillment |
| Paradox Resolved | Disturbs yet protects | Censorship struggle |
| Sleep Continuation | Final purpose | Functional role |

**English Paraphrase (Primary Language)**:

**Final function of dreams**: To **preserve sleep** by providing hallucinatory satisfaction to disturbing wishes.

**Logic**:
1. Unconscious wish activates during sleep.
2. If not satisfied, would wake the sleeper.
3. Dream provides **hallucinatory satisfaction**.
4. Wish is (temporarily) appeased → sleep continues.

**Paradox resolved**: Dreams seem to disturb sleep, but actually protect it. The disturbance we feel is from the censored struggle, not the wish-fulfillment itself.

**Complete Chinese Interpretation (Secondary Language)**:

**梦的最终功能**：通过对扰人愿望提供幻觉性满足来**保护睡眠**。

**逻辑**：
1. 无意识愿望在睡眠期间激活。
2. 如不满足，会唤醒睡眠者。
3. 梦提供**幻觉性满足**。
4. 愿望（暂时）被安抚 → 睡眠继续。

**悖论解决**：梦似乎扰乱睡眠，但实际上保护睡眠。我们感到的扰动来自审查的斗争，而非愿望满足本身。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Guardian of Sleep: Dream's final function=preserve sleep via hallucinatory satisfaction. Logic: Ucs wish activates→if unsatisfied would wake→dream provides satisfaction→sleep continues. Paradox: disturbance from censorship struggle, not wish-fulfillment.
- **中文**: 睡眠守护者:梦的最终功能=通过幻觉满足保护睡眠。逻辑:无意识愿望激活→如不满足会醒来→梦提供满足→睡眠继续。悖论:扰动来自审查斗争,非愿望满足。

**Narrative Snippets**:
- `[ns_freud_ch7_010]` `[trigger: guardian_sleep]` `[factor_trigger: dream_function]` `[role: 主干]` Dream's final function: preserve sleep by providing hallucinatory satisfaction to disturbing wishes. → Core
- `[ns_freud_ch7_011]` `[trigger: appeasement_logic]` `[factor_trigger: dream_function AND wish_cycle]` `[role: 条件分支]` Logic: Ucs wish activates→would wake if unsatisfied→dream satisfies→sleep continues. → Mechanism
- `[ns_freud_ch7_012]` `[trigger: paradox_resolved]` `[factor_trigger: dream_function AND disturbance]` `[role: 条件分支]` Paradox: dreams seem to disturb but protect; disturbance from censorship struggle, not fulfillment. → Resolution"""
    normalized_text_zh: str = """"""
    subject: str = "4 Dream as Guardian of Sleep"
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_4_dream_as_guardian_of_sleep_001_L1",
    )
    version: str = "1.0.0"
