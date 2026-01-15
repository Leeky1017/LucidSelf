"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.827614
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
    semantic_id="mlxj_v1.0.0_1_天神命名_名姓类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1天神命名名姓类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

天神命名，上帝所使也。有善有恶，以其字义审之，善者得福禄，恶者𮊔殃咎。或有明示者，或有隐示者，反复详推自能解也。大约梦此，吉多凶少，人当因梦自省。

###...
    """
    
    original_text: str = """#### 原文（source_text）

天神命名，上帝所使也。有善有恶，以其字义审之，善者得福禄，恶者𮊔殃咎。或有明示者，或有隐示者，反复详推自能解也。大约梦此，吉多凶少，人当因梦自省。

#### 规范化释义（primary_lang_explained）

天神命名，乃上帝所使。有善有恶，以字义审之：
- 善者：得福禄
- 恶者：𮊔殃咎

或明示，或隐示，反复详推自能解。大约梦此吉多凶少，人当因梦自省。

#### 完整对等诠释（secondary_lang_full）

When heavenly deities bestow names, it is by the Supreme's command. Good and evil exist—examine by character meaning:
- Good names: Receive blessings and fortune
- Evil names: Invite calamity

May be explicit or implicit; careful analysis reveals meaning. Generally more auspicious than ominous—one should self-reflect upon such dreams.

#### 核心要点

- 天神命名=上帝使命
- 字义定吉凶：善→福禄，恶→殃咎
- 明示/隐示，详推可解
- 因梦自省

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v23_001]` `[trigger: 名数梦象]` `[factor_trigger: dream_mingxing AND dream_baoying AND dream_tianshenminming]` `[role: 名数类]` 名姓、报应、天神命名等名数梦象。 → 《梦林玄解·卷二十三》#名数"""
    normalized_text_zh: str = """"""
    subject: str = "1 天神命名（名姓类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_天神命名_名姓类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
