"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227825
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
    semantic_id="smth_v1.0.0_窃气与相争_001",
    book_id="sanming",
    engine_id="bazi"
)
class 窃气与相争(SemanticEntry):
    """
    - **原文（source_text）**：
  素问所谓水生木，木复生火，是木受窃气，故水怒而克火，即子逢窃气，母乃力争，与母被鬼伤，子来力救，其义一也。

- **分字分词释义**：
  - **...
    """
    
    original_text: str = """- **原文（source_text）**：
  素问所谓水生木，木复生火，是木受窃气，故水怒而克火，即子逢窃气，母乃力争，与母被鬼伤，子来力救，其义一也。

- **分字分词释义**：
  - **窃气**：气被窃取、泄漏。
  - **母乃力争**：母因子被泄而奋力相争。
  - **鬼伤**：被克者称为鬼，鬼伤即被克所伤。
  - **力救**：全力救援。

- **规范化释义（primary_lang_explained）**：
  《黄帝内经·素问》所说的水生木、木又生火，这样木的气就被火窃取了，所以水发怒而去克火。这就是说，当子辈的气被窃取时，母亲就会奋力相争；这与母亲被鬼（克者）所伤、子辈全力来救的道理是一样的。

- **完整对等诠释（secondary_lang_full）**：
  The Suwen (Yellow Emperor's Inner Canon) states that Water generates Wood, and Wood further generates Fire. Here Wood's qi is stolen (by Fire), thus Water angrily restricts Fire. This illustrates: when the child's qi is stolen, the parent strives forcefully; this principle equals when the parent is injured by the ghost (restrictor), the child comes to rescue forcefully—both share the same underlying principle. This depicts the Elements' protective mutual-rescue mechanism through qi-theft and angry-striving, enabling checks and balances through parent-child linkage rather than isolated action. This establishes the Elements' emotionalized interaction in destiny analysis, citing the medical classics as authority.

- **核心要点**：
  - 引用《素问》说明五行之间的护卫机制
  - 子的气被窃取，母会奋力相争
  - 母被克所伤，子会全力来救
  - 两种情形本质相同，都是母子相护

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_134]` `[trigger: 窃气与相争]` `[factor_trigger: qi_theft AND parent_child_protection]` `[role: 主干]` 素问所谓水生木，木复生火，是木受窃气，故水怒而克火，即子逢窃气，母乃力争，与母被鬼伤，子来力救，其义一也。 → 《三命通会》卷一#窃气与相争

- **详细解说**：
  此条引用医经《黄帝内经·素问》，进一步说明五行之间的护卫机制。水生木、木生火，木作为中介，其气被火窃取（泄气），水就会发怒去克火以保护木，这叫"子逢窃气，母乃力争"。另一种情况是，母被克者（称为"鬼"）所伤，子会全力来救，如木被金克，火就会来克金以救木，这叫"母被鬼伤，子来力救"。两种机制本质相同，都体现五行之间的相互护卫。这里将五行关系拟人化，用"怒"、"争"、"救"等情感词汇，使抽象的五行理论更加生动。

- **校勘与字词辨析（双语）**：
  - **中文**："鬼"在五行中指克我者。"窃气"指子行泄母行之气。
  - **English**："鬼" (ghost) in five elements context means "that which restricts me"; "窃气" (stealing qi) refers to child element draining parent's qi."""
    normalized_text_zh: str = """"""
    subject: str = "窃气与相争"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_窃气与相争_001_L1",
    )
    version: str = "1.0.0"
