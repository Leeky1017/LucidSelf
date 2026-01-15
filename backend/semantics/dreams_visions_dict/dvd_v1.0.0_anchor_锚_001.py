"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439667
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
    semantic_id="dvd_v1.0.0_anchor_锚_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Anchor锚(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: An anchor could represent the Lord, a person or a teaching. ...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: An anchor could represent the Lord, a person or a teaching. It is a picture of security, steadfastness and hope. It can also be a picture of a season of being settled in your life.

**Scripture**: Hebrews 6:19 - "Having this hope as an anchor for the soul, both firm and secure, and which enters into the inside of the veil."

**Positive**: If you have been moving from one thing to the next and then dream of dropping anchor, it means a season is coming of rest and being settled. In a positive light, an anchor could represent the security you have in the Lord. Hope is our anchor—it keeps our eyes set on the goal.

**Negative**: Sometimes an anchor has a negative connotation—the anchor is holding us back! An anchor keeps a ship stationary. When the Lord wants you to move on, you need to hoist that anchor and move on.

**See also**: Ship, Vehicle

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Anchor | Security, steadfastness, hope | Stability or hindrance |
| Dropping anchor | Entering rest season | Settling down |
| Hoisting anchor | Moving forward | Releasing, advancing |

### English Paraphrase

Anchor represents security, steadfastness, and hope—the Lord Himself, a person, or a teaching that keeps you grounded. **Positive**: Dropping anchor indicates a coming season of rest and settling after much movement. Hope is our anchor (Heb 6:19), keeping eyes on the goal. **Negative**: Sometimes the anchor holds you back. Ships need to hoist anchor to move forward. When God calls you to the next phase, release the ministry in the spirit and move full steam ahead.

### Chinese Interpretation（完整对等诠释）

锚代表安全、坚定和盼望——主自己、某人或某教导使你稳固。**正面**：抛锚表示在多次移动后进入休息和安定的季节。盼望是我们的锚（来6:19），使眼目定睛目标。**负面**：有时锚会阻碍你。船需要起锚才能前进。当神呼召你进入下一阶段，在灵里释放事工，全速前进。

### Narrative Snippets

- `[ns_dav_a027]` `[trigger: 梦锚]` `[factor_trigger: dream_symbol_anchor]` `[role: 主干]` Anchor = security, steadfastness, hope—can represent Lord, person, or teaching that grounds you. → Dreams Dictionary #Anchor
- `[ns_dav_a028]` `[trigger: 抛锚]` `[factor_trigger: dream_symbol_anchor AND anchor_action]` `[role: 条件分支]` Dropping anchor = season of rest coming, settling down after movement. → Dreams Dictionary #Anchor
- `[ns_dav_a029]` `[trigger: 锚阻碍]` `[factor_trigger: dream_symbol_anchor AND anchor_action]` `[role: 条件分支]` Anchor holding back = need to hoist and move forward when God calls to next phase. → Dreams Dictionary #Anchor"""
    normalized_text_zh: str = """"""
    subject: str = "Anchor 锚"
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_anchor_锚_001_L1",
    )
    version: str = "1.0.0"
