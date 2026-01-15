"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.821432
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
    semantic_id="mlxj_v1.0.0_1_蚕室_蚕桑类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1蚕室蚕桑类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

夫养蚕之室，为服饰所基，亦侈靡所伏。今人食之不能无衣也，布帛之不能无纨绮也，天乃生蚕焉。使人饲之，以得其利。物虽小而功甚大，事虽微而用甚弘，养之必有其地。此...
    """
    
    original_text: str = """#### 原文（source_text）

夫养蚕之室，为服饰所基，亦侈靡所伏。今人食之不能无衣也，布帛之不能无纨绮也，天乃生蚕焉。使人饲之，以得其利。物虽小而功甚大，事虽微而用甚弘，养之必有其地。此室贵阳明，贵宽敞，贵洁净，忌风气，忌污湿。梦入之者，上人有衣被他人之兆，下人有三春早夜之劳。

#### 规范化释义（primary_lang_explained）

养蚕之室，是服饰的根基，也是奢侈之源。人食不能无衣，布帛不能无纨绮，天生蚕，使人饲养以得其利。物虽小而功甚大，事虽微而用甚弘。

蚕室贵阳明、宽敞、洁净，忌风气、污湿。梦入蚕室者：
- 上人：有衣被他人之兆
- 下人：有三春早夜之劳

#### 完整对等诠释（secondary_lang_full）

The silkworm room is the foundation of clothing and the origin of luxury. People cannot eat without clothes, fabric cannot be without fine silk—thus heaven created silkworms for humans to raise and profit from. Though small, their merit is great; though minor, their use is vast.

The silkworm room values sunlight, spaciousness, and cleanliness; it fears drafts and dampness. Dreaming of entering:
- For superiors: omen of clothing others
- For commoners: labor of early spring nights

#### 核心要点

- 蚕室=服饰之基=生产根本
- 物小功大，事微用弘
- 上人梦之=衣被他人=施恩于人
- 下人梦之=三春劳作=辛勤劳动

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v14_001]` `[trigger: 什物梦象]` `[factor_trigger: dream_gongjui AND dream_canshi AND dream_jizhu AND dream_xiangzheng]` `[role: 什物类]` 弓矩、蚕室、机杼、象征等什物梦象。 → 《梦林玄解·卷十四》#什物"""
    normalized_text_zh: str = """"""
    subject: str = "1 蚕室（蚕桑类首条·完整精校）"
    factor_refs: list = ['source_ref']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_1_蚕室_蚕桑类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
