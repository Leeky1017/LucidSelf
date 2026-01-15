"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.796491
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
    semantic_id="mlxj_v1.0.0_1_四季天象_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1四季天象(SemanticEntry):
    """
    #### 春季

| 梦象 | 主应 |
|------|------|
| 青亮大吉 | 家道东升 |
| 入怀 | 得秀子 |
| 大而明朗 | 清宁之兆 |
| 绕屋 | 贵子 |
| 失光 |...
    """
    
    original_text: str = """#### 春季

| 梦象 | 主应 |
|------|------|
| 青亮大吉 | 家道东升 |
| 入怀 | 得秀子 |
| 大而明朗 | 清宁之兆 |
| 绕屋 | 贵子 |
| 失光 | 大凶 |
| 文彩 | 士子大利 |
| 西坠 | 凶 |

#### 夏季

| 梦象 | 主应 |
|------|------|
| 高吉 | 红光射吉 |
| 照户 | 财临 |
| 光芒 | 文显 |
| 红霞 | 得利 |
| 吞入口 | 娠孕 |

#### 秋季

| 梦象 | 主应 |
|------|------|
| 白大吉 | 有财 |
| 西出 | 迁移 |
| 洞见帝庭 | 大吉 |
| 零落 | 死亡 |
| 昏暗 | 忧事 |

#### 冬季

| 梦象 | 主应 |
|------|------|
| 低黑 | 丧事 |
| 映水吉 | 明照清吉 |
| 密而有光 | 进财 |
| 赤烈 | 蒙恩吉 |
| 捧入怀 | 添寿 |
| 昏暗 | 盗贼起 |

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v25_001]` `[trigger: 四季天象]` `[factor_trigger: siji AND dream_tianxiang AND dream_dili]` `[role: 图表框架]` 甘德图按四季分类天地人事梦象，春夏秋冬各有吉凶主应。 → 《梦林玄解·卷二十五》#甘德图"""
    normalized_text_zh: str = """"""
    subject: str = "1 四季天象"
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
        l1_anchor="mlxj_v1.0.0_1_四季天象_001_L1",
    )
    version: str = "1.0.0"
