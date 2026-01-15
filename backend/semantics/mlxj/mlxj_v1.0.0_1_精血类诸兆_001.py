"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.836963
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
    semantic_id="mlxj_v1.0.0_1_精血类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1精血类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 精若水晶大吉：元阳之真，精固旺盛
- 涤精而纳之吉：单熙典故
- 遍身红血大吉：朱衣加身，皇恩爵禄
- 媾精见血大吉：心腹相托

**吉类**：
- 精泄不...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 精若水晶大吉：元阳之真，精固旺盛
- 涤精而纳之吉：单熙典故
- 遍身红血大吉：朱衣加身，皇恩爵禄
- 媾精见血大吉：心腹相托

**吉类**：
- 精泄不泄吉：阳旺火盛
- 血淋身吉：文高武遂
- 吸人血水吉：狠心之象
- 脓血污手足吉：兄弟相干

**凶类**：
- 遗精凶：火旺气寒，元关不固
- 交姤精不泄凶：有谋不遂
- 精寒如石凶：一事无成
- 眼旁流出血凶：悲哀哭泣

#### 魂魄类诸兆

**吉类**：
- 魂飞上九霄吉：名扬寿永
- 无息大吉：太极静生阴，元神旺可长生

**凶类**：
- 喘息不定凶：心不宁
- 气如鬼嘘吁凶：肺气不足

#### 尿粪类诸兆

**吉类**：
- 大便满地吉：得见便宜
- 闻屁人笑大吉：一语骗入
- 屁臭吉：将有生意

**凶类**：
- 屙屎碗内凶：缺食饿死
- 屙出屎尽凶：内空虚
- 大便在灶下凶：燥妄异常
- 蛆满身凶：财费病深"""
    normalized_text_zh: str = """"""
    subject: str = "1 精血类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_精血类诸兆_001_L1",
    )
    version: str = "1.0.0"
