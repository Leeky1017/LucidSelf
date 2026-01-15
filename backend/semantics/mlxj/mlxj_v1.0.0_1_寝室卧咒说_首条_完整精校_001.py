"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.816045
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
    semantic_id="mlxj_v1.0.0_1_寝室卧咒说_首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1寝室卧咒说首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

寝室卧咒说：人之寝室卧处，须令高爽洁净，则地气不及，鬼吹不干。凡鬼气侵人，每因卧榻低湿，阴气逆上，以致神魄少宁，外与内涉，邪厉游行，遂多妄梦。故必遵忌行之，...
    """
    
    original_text: str = """#### 原文（source_text）

寝室卧咒说：人之寝室卧处，须令高爽洁净，则地气不及，鬼吹不干。凡鬼气侵人，每因卧榻低湿，阴气逆上，以致神魄少宁，外与内涉，邪厉游行，遂多妄梦。故必遵忌行之，乃获宁寝矣。

#### 规范化释义（primary_lang_explained）

寝室卧处须令高爽洁净：
- 地气不及
- 鬼吹不干

凡鬼气侵人，每因：
- 卧榻低湿
- 阴气逆上
- 神魄少宁
- 外与内涉
- 邪厉游行
- 遂多妄梦

故必遵忌行之，乃获宁寝。

#### 完整对等诠释（secondary_lang_full）

Regarding the sleeping chamber incantation: One's bedroom and sleeping area must be kept elevated, airy, and clean—so ground vapors cannot reach and ghost-winds cannot intrude.

When ghostly energies invade, it is often because:
- The sleeping couch is low and damp
- Yin energy rises in reverse
- Spirit and soul find little peace
- External and internal interfere
- Evil spirits roam freely
- Thus many delusional dreams arise

Therefore, one must follow these precautions to achieve peaceful sleep.

#### 核心要点

- 寝室须高爽洁净
- 低湿→阴气逆上→妄梦
- 遵忌行之→宁寝

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v28_001]` `[trigger: 梦禳方法]` `[factor_trigger: dream_rangfa AND fuzhou AND dream_qinshi AND dream_zhouyu AND dream_effect]` `[role: 禳法]` 禳梦之法、符咒、寝室、咒语、梦效。 → 《梦林玄解·卷二十八》#梦禳"""
    normalized_text_zh: str = """"""
    subject: str = "1 寝室卧咒说（首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_寝室卧咒说_首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
