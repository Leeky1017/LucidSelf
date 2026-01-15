"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.799577
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
    semantic_id="mlxj_v1.0.0_2_舟楫类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2舟楫类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 天河中船行：圣君颁诏
- 舟中载日月：大贵
- 乘舟看日月：得官爵
- 舟如飞：大富贵
- 扶母登舟：官位至
- 舟中清水：得大财
- 执火登舟：诸事大吉
...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 天河中船行：圣君颁诏
- 舟中载日月：大贵
- 乘舟看日月：得官爵
- 舟如飞：大富贵
- 扶母登舟：官位至
- 舟中清水：得大财
- 执火登舟：诸事大吉
- 龙舟殿阁旗幡：皇宫御座

**吉类**：
- 云中有船：远行
- 开户见舟楫：时运将达
- 舟泊户外：音信至
- 家中人物同在舟中：迁移
- 舟中饮酒：远客至
- 登舟渡关津：官禄运通
- 舟中泥浊水浆：得小利
- 合两船为舫施华盖：刘穆之典故

**凶类**：
- 舟在庭中：大水
- 舟入堂屋中：鬼神巡辑
- 房内乘舟：作事不利
- 登舟被人物阻隔：事难成就
- 船在岸上：是非之厄
- 一身立二船头上：疑惑忧虑
- 夫妇各坐一舟：离别
- 身卧小舟中：疾病死亡
- 船头破碎：不祥
- 船无尾：子孙凶
- 船舱水漏沾衣：不吉
- 船覆：世事反复

#### 舟船典故

| 梦者 | 梦象 | 应验 |
|------|------|------|
| 刘穆之 | 合两船为舫施华盖 | 官至仆射丹阳尹 |
| 沈嶓 | 渡江船覆水分二 | 授分水县 |
| 大禹 | 乘舟过月中 | 受禅为帝 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 舟楫类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_舟楫类诸兆_001_L1",
    )
    version: str = "1.0.0"
