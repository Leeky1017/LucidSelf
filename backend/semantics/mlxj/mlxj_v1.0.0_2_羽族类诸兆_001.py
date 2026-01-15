"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.791057
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
    semantic_id="mlxj_v1.0.0_2_羽族类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2羽族类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 青鸾来自云中吉：寿征
- 鹏飞过海大吉：出类拔萃（沈晦典故）
- 金翅鸟吉：贵显
- 鹊成巢大吉：创造屋宇，良缘
- 檐前鹊噪大吉：喜庆
- 赤乌三足吉：贵...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 青鸾来自云中吉：寿征
- 鹏飞过海大吉：出类拔萃（沈晦典故）
- 金翅鸟吉：贵显
- 鹊成巢大吉：创造屋宇，良缘
- 檐前鹊噪大吉：喜庆
- 赤乌三足吉：贵征
- 白燕入怀大吉：非常之喜

**吉类**：
- 紫翎文鸟降于庭吉：文章显于明庭（张𬸦典故）
- 孔雀舞于庭吉：卿佐之位
- 赤雀衔丹书大吉：圣王之瑞（西伯典故）
- 雁入云中贞吉：姓名标雁塔
- 雎鸠和鸣吉：婚姻嫁娶
- 鸳鸯戏水吉：室家欢庆
- 燕舞梁间大吉：燕会喜乐

**凶类**：
- 鸟食龙蛇凶：子夏诛
- 燕巢林木凶：兵火之灾
- 鸱鸮凶：谗谤侵陵
- 白乌贞吉否凶：丧服疾病

#### 典故

- 张𬸦梦紫翎鸟：后登进士，人称青钱学士
- 沈晦梦跨大鹏：后魁天下
- 西伯梦赤雀衔丹书：兴周之吉兆"""
    normalized_text_zh: str = """"""
    subject: str = "2 羽族类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_羽族类诸兆_001_L1",
    )
    version: str = "1.0.0"
