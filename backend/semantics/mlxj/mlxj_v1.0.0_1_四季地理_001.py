"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.796560
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
    semantic_id="mlxj_v1.0.0_1_四季地理_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1四季地理(SemanticEntry):
    """
    #### 春季

| 梦象 | 主应 |
|------|------|
| 平野千里 | 高峰清旷大吉 |
| 深广无波 | 大吉心开意旷 |
| 断大凶 | 作事不成 |
| 高卑万丈 | 有远行...
    """
    
    original_text: str = """#### 春季

| 梦象 | 主应 |
|------|------|
| 平野千里 | 高峰清旷大吉 |
| 深广无波 | 大吉心开意旷 |
| 断大凶 | 作事不成 |
| 高卑万丈 | 有远行大凶 |
| 多草木 | 肝病痊旺 |
| 行步渐高 | 得美名 |

#### 夏季

| 梦象 | 主应 |
|------|------|
| 平广无尘 | 高平肺和心吉 |
| 清波直流 | 平湿吉 |
| 仄狭 | 身心不安 |
| 身居洞中 | 水下有人吉 |
| 黑如灰 | 家事不宁 |

#### 秋季

| 梦象 | 主应 |
|------|------|
| 无灰沙心清 | 高广清旷大吉 |
| 草木茂盛 | 大吉心安气足 |
| 震动 | 有迁移事 |
| 浑浊 | 事不成 |
| 波涛汹涌 | 危险心不安 |

#### 冬季

| 梦象 | 主应 |
|------|------|
| 野旷平光 | 冈峻高阔大吉 |
| 深滢无波 | 得寿 |
| 赤灰有惊 | 忧防火烛凶事 |
| 登高望远 | 大吉 |
| 波流绕身 | 得财大吉 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 四季地理"
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
        l1_anchor="mlxj_v1.0.0_1_四季地理_001_L1",
    )
    version: str = "1.0.0"
