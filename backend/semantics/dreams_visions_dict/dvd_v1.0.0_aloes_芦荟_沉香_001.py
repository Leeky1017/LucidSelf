"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439628
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
    semantic_id="dvd_v1.0.0_aloes_芦荟_沉香_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Aloes芦荟沉香(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: The aloe was used as a perfume in bible times. Women used it...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: The aloe was used as a perfume in bible times. Women used it to perfume themselves, but it was also used for the embalming of the dead, as in the case of Jesus. Aloes also have a healing quality so can also represent a season of rest and healing.

**Positive**: Song of Solomon 4:14-16 - "Spikenard and saffron; calamus and cinnamon, with all trees of frankincense; myrrh and aloes, with all the chief spices... Let my beloved come into his garden, and eat his pleasant fruits."

This speaks of the love of romance and the intimate relationship the bride has with the groom. It refers to the Lord Jesus and our relationship with Him as His bride.

**Negative**: Proverbs 7:17 - "I have perfumed my bed with myrrh, aloes, and cinnamon."

This speaks of seduction of the world. To trust more in the world than you do in the Lord to heal you.

**See also**: Balm, Perfume, Plants

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Aloes | Perfume/healing plant | Dual: intimacy or seduction |
| Embalming | Preparation for burial | Death/transition |
| Bride-groom | Intimate relationship | Christ and Church |

### English Paraphrase

Aloes has dual meaning based on context. **Positive (Song of Solomon)**: represents intimate relationship between bride and groom—the believer's romance with Christ. Aloes' healing quality also indicates a season of rest and healing. **Negative (Proverbs 7)**: the seductress's perfumed bed—represents worldly seduction, trusting the world rather than God for healing. Also used for embalming (death/transition).

### Chinese Interpretation（完整对等诠释）

芦荟/沉香根据语境有双重含义。**正面（雅歌）**：代表新娘与新郎的亲密关系——信徒与基督的浪漫。芦荟的医治特质也表示休息和医治的季节。**负面（箴言7）**：淫妇熏香的床——代表世俗诱惑，信靠世界而非神来医治。也用于防腐（死亡/过渡）。

### Core Points

- 芦荟 = 双重含义符号
- 正面：与基督的亲密关系、医治季节
- 负面：世俗诱惑、信靠世界
- 圣经对比：雅歌（正） vs 箴言7（负）
- 也与防腐/死亡相关

### Narrative Snippets

- `[ns_dav_a013]` `[trigger: 梦芦荟]` `[factor_trigger: dream_symbol_aloes AND intimacy_target]` `[role: 主干]` Aloes = dual symbol: intimate relationship with Christ (positive) or worldly seduction (negative). → Dreams Dictionary #Aloes
- `[ns_dav_a014]` `[trigger: 芦荟正面]` `[factor_trigger: dream_symbol_aloes_positive AND healing_season]` `[role: 条件分支]` Song of Solomon context: bride-groom intimacy, rest and healing season. → Dreams Dictionary #Aloes
- `[ns_dav_a015]` `[trigger: 芦荟负面]` `[factor_trigger: dream_symbol_aloes_negative]` `[role: 条件分支]` Proverbs 7 context: seductress's bed, worldly trust over God. → Dreams Dictionary #Aloes"""
    normalized_text_zh: str = """"""
    subject: str = "Aloes 芦荟/沉香"
    factor_refs: list = ['dream_symbol_aloes', 'concept_bride_groom', 'concept_seduction']
    
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
        l1_anchor="dvd_v1.0.0_aloes_芦荟_沉香_001_L1",
    )
    version: str = "1.0.0"
