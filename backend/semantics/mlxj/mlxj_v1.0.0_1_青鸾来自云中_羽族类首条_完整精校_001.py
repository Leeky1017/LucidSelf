"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.790999
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
    semantic_id="mlxj_v1.0.0_1_青鸾来自云中_羽族类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1青鸾来自云中羽族类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

青鸾来自云中吉。青鸾凤属，西王母所乘者。梦此为寿征。势壮者逾古稀而臻耄耋，高年者过期颐而比篯铿。儿孙戏彩，子女称觞，共祝长生之庆也。

#### 规范化释义...
    """
    
    original_text: str = """#### 原文（source_text）

青鸾来自云中吉。青鸾凤属，西王母所乘者。梦此为寿征。势壮者逾古稀而臻耄耋，高年者过期颐而比篯铿。儿孙戏彩，子女称觞，共祝长生之庆也。

#### 规范化释义（primary_lang_explained）

梦青鸾来自云中，吉。青鸾是凤凰之属，为西王母所乘。

梦此为寿征：
- 势壮者：逾古稀而臻耄耋
- 高年者：过期颐而比篯铿
- 儿孙戏彩，子女称觞，共祝长生之庆

#### 完整对等诠释（secondary_lang_full）

Dreaming of a blue luan bird coming from the clouds is auspicious. The blue luan belongs to the phoenix family, ridden by the Queen Mother of the West.

This dream signifies longevity:
- The vigorous: Surpass seventy to reach eighty or ninety
- The elderly: Exceed one hundred, rivaling Pengzu
- Children and grandchildren celebrate, sons and daughters toast—all rejoice in long life

#### 核心要点

- 青鸾=凤属=西王母所乘
- 寿征=长生之庆
- 古稀→耄耋，期颐→比篯铿

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v20_001]` `[trigger: 飞走梦象]` `[factor_trigger: dream_qingluan]` `[role: 飞走类]` 青鸾等飞走梦象。 → 《梦林玄解·卷二十》#飞走"""
    normalized_text_zh: str = """"""
    subject: str = "1 青鸾来自云中（羽族类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_青鸾来自云中_羽族类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
