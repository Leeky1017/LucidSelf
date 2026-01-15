"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.782247
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
    semantic_id="mlxj_v1.0.0_1_头颅诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1头颅诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 头中有两人吉：神灵相依
- 自求其首吉：王琳典故
- 梳头大吉：法通道合，得理有仪

**吉类**：
- 头颅生草：士人加冠，贵人锡缨
- 头上囟门忽开大吉...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 头中有两人吉：神灵相依
- 自求其首吉：王琳典故
- 梳头大吉：法通道合，得理有仪

**吉类**：
- 头颅生草：士人加冠，贵人锡缨
- 头上囟门忽开大吉：远行之兆，性开情达

**凶类**：
- 头中无脑：空虚之象，病者必死
- 被人斩首持去大凶：齐景思王典故

**贞吉否凶类**：
- 将首与人凶：交易不成，功名不进
- 人坐其首：被人欺压/他尊己卑

#### 头部象征体系

头部在形貌梦象中象征：
- **权位**：头=首=第一=领袖
- **智慧**：头脑=思维=智力
- **尊严**：首级=人格=身份
- **命运**：头向=方向=前途"""
    normalized_text_zh: str = """"""
    subject: str = "1 头颅诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_头颅诸兆_001_L1",
    )
    version: str = "1.0.0"
