"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042650
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
    semantic_id="smth_v1.0.0_午为烽候_001",
    book_id="sanming",
    engine_id="bazi"
)
class 午为烽候(SemanticEntry):
    """
    - **原文（source_text）**：
  午为烽堠。午正位于南，属火、土，其色赤黄，名其曰烽堠者，此也。又午为马，烽堠乃戎马兵火之处所也。午生人时利见辰，真龙出则凡马空矣，谓之马化龙驹。

-...
    """
    
    original_text: str = """- **原文（source_text）**：
  午为烽堠。午正位于南，属火、土，其色赤黄，名其曰烽堠者，此也。又午为马，烽堠乃戎马兵火之处所也。午生人时利见辰，真龙出则凡马空矣，谓之马化龙驹。

- **分字分词释义**：
  - **烽候**：边塞烽火台，象征警戒、军旅与火光。
  - **南方火土赤黄**：午居南方，火土并盛，色赤黄。
  - **马化龙驹**：午为马，辰为龙，马得龙气而贵，喻凡马成龙驹。

- **规范化释义（primary_lang_explained）**：
  午居正南，火土并旺，赤黄之色如烽火与土台，故称「烽堠」。午又为马，烽堠为戎马兵火之所，象征行动、战事与显露之权。午年生人若时见辰龙，有「马化龙驹」之象：普通之马得真龙相助而身价陡增，主有机会从军旅或权力体系中脱颖而出。

- **完整对等诠释（secondary_lang_full）**：
  Wu sits due south where Fire and Earth are both strong, its red‑yellow tones evoking beacon flames on a rammed‑earth tower. Here Wu is called the beacon post: a high, exposed place where signals are lit, troops gather, and news of danger or command is first seen. Wu also corresponds to the Horse, so this becomes a frontline station of men and horses under arms. For someone born in a Wu year who meets Chen at the hour, the text speaks of “the horse transforming into a dragon’s colt”: an ordinary mount that, by standing at the right outpost and receiving true Dragon support, suddenly carries royal messages and prestige. In reading a life, this image points to roles at the visible front—command posts, crisis centres, highly public platforms—where one is both empowered and constantly tested. The same beacon that brings opportunity also concentrates risk and fatigue, so success depends on having enough inner structure to hold such heat."""
    normalized_text_zh: str = """"""
    subject: str = "午为烽候"
    factor_refs: list = ['source_ref', 'rel_smth_wufh_001', 'wu', 'rel_smth_wufh_002', 'wu_chen', 'rel_smth_wufh_003', 'wuxiang', 'evi_smth_wufh_001', 'wu_fenghou', 'rule_wufh', 'concept_command_center']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_午为烽候_001_L1",
    )
    version: str = "1.0.0"
