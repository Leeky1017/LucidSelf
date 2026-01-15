"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.169580
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
    semantic_id="tb_v1.0.0_friends_and_enemies__chapter_v_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class FriendsAndEnemiesChapterV(SemanticEntry):
    """
    **Source Text** (Lines 7743-7864):
> Indications of great and lasting friendships, or enmities, may ...
    """
    
    original_text: str = """**Source Text** (Lines 7743-7864):
> Indications of great and lasting friendships, or enmities, may be perceived by observation of the ruling places, exhibited in the respective nativities of both the persons... should all these in both nativities be in the same signs, or should they be counterchanged in position, they will create fixed and indissoluble friendship.

**English Paraphrase (Primary Language)**:
**Friendships and enmities** are determined by comparing two nativities:

**Lasting friendship** indicators:
- Sun, Moon, ASC, Part of Fortune in same signs in both charts
- Or counterchanged (swapped positions)
- Ascendants within 17° of each other

**Lasting enmity** indicators:
- Above places in inconjunct signs
- Or in opposition

**Three types of friendship**:
1. **Spontaneous** (from luminaries): Pure goodwill
2. **Profit-based** (from Part of Fortune): Material benefit
3. **Pleasure/Pain** (from Ascendants): Emotional bond

**Casual friendships/strifes** arise from planetary ingresses between nativities.

**Complete Chinese Interpretation (Secondary Language)**:
**友谊和敌意**通过比较两个本命盘确定：

**持久友谊**指标：
- 太阳、月亮、上升、福点在两盘中同星座
- 或互换位置
- 上升点相距17°以内

**持久敌意**指标：
- 上述位置在不合星座
- 或在对分

**三种友谊类型**：
1. **自发的**（来自发光体）：纯粹善意
2. **利益导向**（来自福点）：物质利益
3. **快乐/痛苦**（来自上升点）：情感纽带

**Core Points**:
- Compare Sun, Moon, ASC, Part of Fortune between charts
- Same signs or counterchange = lasting friendship
- Inconjunct or opposition = lasting enmity
- Three friendship types: spontaneous, profit-based, emotional
- Planetary ingresses create temporary friendships/strifes

**Narrative Snippets**:
- `[ns_tetra_iv011]` `[trigger: synastry_friendship]` `[factor_trigger: astro_chart_comparison]` `[role: 主干]` Friendships are judged by comparing the Sun, Moon, ASC, and Part of Fortune between two nativities. → Source Text IV.7
- `[ns_tetra_iv021]` `[trigger: lasting_bond]` `[factor_trigger: astro_same_sign AND astro_counterchange]` `[role: 条件分支]` Same signs or counterchanged positions create fixed and indissoluble friendship; ASCs within 17° = strong bond. → Bond
- `[ns_tetra_iv022]` `[trigger: three_friendships]` `[factor_trigger: astro_luminaries AND astro_fortune AND astro_asc]` `[role: 条件分支]` Three types of friendship: spontaneous (from luminaries), profit-based (from Fortune), emotional (from ASC). → Types"""
    normalized_text_zh: str = """"""
    subject: str = "Friends and Enemies (Chapter VII)"
    factor_refs: list = ['synastry', 'new_candidate']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_friends_and_enemies__chapter_v_001_L1",
    )
    version: str = "1.0.0"
