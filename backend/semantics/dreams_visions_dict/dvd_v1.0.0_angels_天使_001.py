"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439676
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
    semantic_id="dvd_v1.0.0_angels_天使_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Angels天使(SemanticEntry):
    """
    ### Source Text

> **Strong's 32**: aggelos—a messenger, an envoy, one who was sent, an angel, a mes...
    """
    
    original_text: str = """### Source Text

> **Strong's 32**: aggelos—a messenger, an envoy, one who was sent, an angel, a messenger from God.

**Guardian Angels** (Psalm 91:11): Issued at birth, larger than life, powerful, dressed in various gear, carry swords, wear sashes.

**Worship Angels** (Psalm 148:2): Worship the Lord in Throne Room, present during praise and worship, usually have wings, sing lovely voices, carry harps, tambourines, trumpets.

**Messenger Angels** (Luke 1:30): Bring messages from Lord, plain looking, flowing robes, often bearing scroll or ram's horn.

**Warrior Angels** (Rev 12:7): Michael leads them, carry swords, eyes of fire, foreboding appearance.

**Negative** (2 Cor 11:14): Satan disguised as angel of light—deception. Such angels don't reveal faces, very bright, accompanied by intense emotion, forceful. They try to get you to receive from them—opening heart to enemy. Warning: New Age cult emphasizes angelic experiences; be cautious of those emphasizing angel experiences without sharing relationship with Lord Jesus.

**See also**: Colossians 2:18 warns against worshipping of angels.

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Guardian Angel | Personal protector from birth | Protection |
| Worship Angel | Throne room worshipper | Praise presence |
| Messenger Angel | Delivers God's messages | Divine communication |
| Warrior Angel | Fights spiritual battles | Warfare |
| Angel of light | Satan's disguise | Deception |

### English Paraphrase

Angels are messengers from God, appearing in various types: **Guardian** (personal protectors, powerful, armed); **Worship** (praise in Throne Room, wings, instruments); **Messenger** (plain, robes, scrolls—like Gabriel to Mary); **Warrior** (Michael's army, swords, fire-eyes). **Negative**: Satan disguises as angel of light (2 Cor 11:14)—these don't show faces, are overly bright/emotional/forceful, trying to get you to open your heart. Discern spirits carefully. New Age emphasizes angels without Christ—be cautious. Colossians 2:18 warns against angel worship.

### Chinese Interpretation（完整对等诠释）

天使是神的使者，有不同类型：**守护天使**（个人保护者，强大，武装）；**敬拜天使**（在宝座室赞美，有翅膀，乐器）；**传信天使**（朴素，袍子，卷轴——如加百列对马利亚）；**争战天使**（米迦勒的军队，刀剑，火焰眼）。**负面**：撒但装作光明天使（林后11:14）——这些不露面，过度明亮/情绪化/强迫性，试图让你打开心门。仔细分辨诸灵。新纪元强调天使而无基督——要谨慎。歌罗西书2:18警告不可敬拜天使。

### Narrative Snippets

- `[ns_dav_a030]` `[trigger: 梦天使]` `[factor_trigger: dream_symbol_angels]` `[role: 主干]` Angels are messengers from God—Guardian, Worship, Messenger, Warrior types. → Dreams Dictionary #Angels
- `[ns_dav_a031]` `[trigger: 天使类型]` `[factor_trigger: dream_symbol_angels AND dream_type]` `[role: 主干依赖]` Guardian (armed, protective), Worship (wings, instruments), Messenger (scrolls), Warrior (swords, fire-eyes). → Dreams Dictionary #Angels
- `[ns_dav_a032]` `[trigger: 假光明天使]` `[factor_trigger: dream_symbol_angels AND angel_authenticity]` `[role: 条件分支]` Angel of light = Satan's disguise—overly bright, forceful, hides face. Discern carefully. → Dreams Dictionary #Angels"""
    normalized_text_zh: str = """"""
    subject: str = "Angels 天使"
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
        l1_anchor="dvd_v1.0.0_angels_天使_001_L1",
    )
    version: str = "1.0.0"
