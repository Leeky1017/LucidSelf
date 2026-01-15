"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.817526
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
    semantic_id="mlxj_v1.0.0_1_手足类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1手足类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 盥手濯足大吉：兄弟自新（祖光禄典故）
- 两手足齐折大吉：鞠躬尽性，独占高魁
- 手上生疔毒吉：兄弟添丁
- 手长至足大吉：股肱相佐，富贵征祥
- 掌中草不...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 盥手濯足大吉：兄弟自新（祖光禄典故）
- 两手足齐折大吉：鞠躬尽性，独占高魁
- 手上生疔毒吉：兄弟添丁
- 手长至足大吉：股肱相佐，富贵征祥
- 掌中草不脱大吉：辛夤逊典故
- 脚上生疮大吉：大利商贾
- 足趾添长吉：孙子福寿之征
- 增一足大吉：鼎立之象

**吉类**：
- 洗只手只足吉：半喜半愈
- 合掌吉：事事佳祥
- 刀斫足吉：男得利，女成衣
- 伤脚血出吉：文名入太学

**凶类**：
- 折一手一足大凶：孤力无助
- 足走如飞凶：急难之兆
- 足长凶：知足不辱
- 脚落凶：运不通达
- 脚底穿破凶：无地可立

#### 手足与亲属对应

| 部位 | 对应 |
|------|------|
| 左手 | 兄/子 |
| 右手 | 弟/侄 |
| 左足 | 男 |
| 右足 | 女 |
| 手足 | 兄弟股肱 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 手足类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_手足类诸兆_001_L1",
    )
    version: str = "1.0.0"
