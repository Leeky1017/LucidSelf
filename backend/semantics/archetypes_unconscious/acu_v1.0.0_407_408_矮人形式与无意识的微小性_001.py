"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.498242
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
    semantic_id="acu_v1.0.0_407_408_矮人形式与无意识的微小性_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 407408矮人形式与无意识的微小性(SemanticEntry):
    """
    **原文** (§407-408, 行6264-6313):

> [407] There is equally a connection with the unconscious when the ...
    """
    
    original_text: str = """**原文** (§407-408, 行6264-6313):

> [407] There is equally a connection with the unconscious when the old man appears as a dwarf. In a Swiss fairytale, the peasant's son encounters "a little iron man" (es chlis isigs Männdli). There are little ice men and little metal men; in a modern dream I have encountered a little black iron man at a critical juncture.
>
> [408] In a modern series of visions, the wise old man was on one occasion of normal size at the bottom of a crater; on another, a tiny figure on a mountaintop. We might mention the Anthroparion (little leaden man of the Zosimos vision), the metallic men who dwell in mines, the crafty dactyls of antiquity, the homunculi of the alchemists, and the gnomic throng of hobgoblins. The unconscious seems to be the world of the infinitesimally small. The atman is "smaller than small and bigger than big." The archetypes share this peculiarity with the atomic world—the more deeply one penetrates microphysics, the more devastating the forces enchained there.

**英文释义**：
- 老人以矮人形式出现 = 与无意识的联系
- 铁小人、冰小人、金属小人 = 无意识意象
- Anthroparion（佐西莫斯幻象中的小铅人）
- 指环精灵、炼金术的人工小人、地精等
- 无意识 = 无限小的世界
- Atman = "比小更小，比大更大"
- 原型与原子世界共享此特性：越深入，力量越巨大

**中文诠释**：
- 老人以矮人形式出现表明与无意识的联系
- 瑞士童话中的"铁小人"
- 现代梦中的黑铁小人在关键时刻出现
- 现代幻象系列中老人时而正常大小（火山口底部），时而微小（山顶）
- 相关意象：佐西莫斯的小铅人、矿中金属人、古代指环精灵、炼金术人工小人、地精群
- 无意识似乎是无限小的世界
- Atman悖论："比小更小，比大更大"
- 原型与原子物理学的共同特性：越微小，力量越毁灭性

**Narrative Snippets**:
- `[ns_cw9i_VI_407]` `[trigger: old_man_dwarf]` `[factor_trigger: jung_archetype AND jung_unconscious]` `[role: 主干]` Old man as dwarf = connection to unconscious; little iron man appears at critical junctures. → §407
- `[ns_cw9i_VI_408]` `[trigger: atomic_unconscious]` `[factor_trigger: jung_unconscious AND jung_archetype]` `[role: 主干依赖]` Unconscious = world of infinitesimally small; archetypes share this with atomic world—smallest causes, greatest effects. → §408"""
    normalized_text_zh: str = """"""
    subject: str = "§407-408 矮人形式与无意识的微小性"
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_407_408_矮人形式与无意识的微小性_001_L1",
    )
    version: str = "1.0.0"
