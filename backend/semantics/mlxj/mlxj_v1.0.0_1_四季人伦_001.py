"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.846991
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
    semantic_id="mlxj_v1.0.0_1_四季人伦_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1四季人伦(SemanticEntry):
    """
    #### 春季

| 梦象 | 主应 |
|------|------|
| 皇帝入室 | 喜吉怒凶 |
| 双亲并坐 | 大吉有喜事 |
| 圣人为师 | 大贵爵禄 |
| 兄弟左手喜右手怒 | 吉...
    """
    
    original_text: str = """#### 春季

| 梦象 | 主应 |
|------|------|
| 皇帝入室 | 喜吉怒凶 |
| 双亲并坐 | 大吉有喜事 |
| 圣人为师 | 大贵爵禄 |
| 兄弟左手喜右手怒 | 吉凶分 |
| 登朝富贵喜乐 | 父笑神气过旺 |
| 后妃呼召 | 贵人梦大吉 |
| 太子召见 | 大吉得遇贵人 |

#### 夏季

| 梦象 | 主应 |
|------|------|
| 君赐物大吉 | 双亲饮酒吉 |
| 先生教书 | 同胞同坐吉 |
| 后妃入门 | 祖宗言语吉 |
| 两君相争 | 凶事 |
| 母病 | 不吉病患 |

#### 秋季

| 梦象 | 主应 |
|------|------|
| 天子出宫 | 父母衣白吉 |
| 更师吉 | 兄弟化为女子凶 |
| 宰相坐大吉 | 衣红色丧事 |
| 太监同行 | 同饮大吉 |

#### 冬季

| 梦象 | 主应 |
|------|------|
| 君赐酒食 | 大吉 |
| 父母同饮 | 师醉喜事 |
| 兄弟赤身 | 大吉 |
| 君命召 | 吉贵 |
| 王侯入门 | 大利 |

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v26_001]` `[trigger: 甘德图]` `[factor_trigger: tiangan AND dream_hunyin AND ganzhi]` `[role: 术数]` 天干、婚姻、干支等甘德图占断要素。 → 《梦林玄解·卷二十六》#甘德图"""
    normalized_text_zh: str = """"""
    subject: str = "1 四季人伦"
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
        l1_anchor="mlxj_v1.0.0_1_四季人伦_001_L1",
    )
    version: str = "1.0.0"
