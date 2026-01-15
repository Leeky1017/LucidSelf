"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.847047
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
    semantic_id="mlxj_v1.0.0_1_四季婚姻_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1四季婚姻(SemanticEntry):
    """
    #### 春季

| 梦象 | 主应 |
|------|------|
| 并坐大吉 | 绕膝和顺吉 |
| 妻亲相唤 | 得财忧事至 |
| 嫁娶未婚者梦之吉 | 既婚者梦之凶 |
| 男梦妻嫁他...
    """
    
    original_text: str = """#### 春季

| 梦象 | 主应 |
|------|------|
| 并坐大吉 | 绕膝和顺吉 |
| 妻亲相唤 | 得财忧事至 |
| 嫁娶未婚者梦之吉 | 既婚者梦之凶 |
| 男梦妻嫁他人 | 身凶 |
| 鳏旷者梦娶 | 得财 |
| 寡居者梦之 | 大吉 |

#### 夏季

| 梦象 | 主应 |
|------|------|
| 同行花下 | 怀抱得财吉 |
| 观鱼得财 | 解劝斗殴得喜吉 |
| 送酒殽来 | 得财 |
| 生女口舌 | 得钱共分同席吉 |
| 妻妾相争 | 赤脚走得失脱凶 |

#### 秋季

| 梦象 | 主应 |
|------|------|
| 孀妇生产 | 有忧疑 |
| 怀双胎子 | 喜事重重吉 |
| 子跪孙立 | 大笑官讼口舌 |
| 簪花合卺 | 大吉 |

#### 冬季

| 梦象 | 主应 |
|------|------|
| 同烧香礼 | 饮酒增福吉 |
| 同舟行水 | 送冰来得西北方大财 |
| 相打血出吉 | 作事大成 |
| 娶妇家庆 | 吉有远信 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 四季婚姻"
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
        l1_anchor="mlxj_v1.0.0_1_四季婚姻_001_L1",
    )
    version: str = "1.0.0"
