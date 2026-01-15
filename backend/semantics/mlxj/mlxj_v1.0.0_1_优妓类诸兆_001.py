"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.840331
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
    semantic_id="mlxj_v1.0.0_1_优妓类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1优妓类诸兆(SemanticEntry):
    """
    #### 分类汇总

**凶类**：
- 身是优人搬戏：闲非闲气，门户不宁
- 涂面为优人：防欺侮诞诈，有灾病耻辱
- 演戏身衣冕服凶：外孝服动，内虚惊事
- 门首吊傀儡大凶：家有横祸

**吉类**...
    """
    
    original_text: str = """#### 分类汇总

**凶类**：
- 身是优人搬戏：闲非闲气，门户不宁
- 涂面为优人：防欺侮诞诈，有灾病耻辱
- 演戏身衣冕服凶：外孝服动，内虚惊事
- 门首吊傀儡大凶：家有横祸

**吉类**：
- 优人迎拜：文人身贵富
- 与妓相别吉：阴非远弃之象

**贞吉否凶类**：
- 见提傀儡：有人提掇，病人凶
- 呼妓陪席饮酒：口舌悲哀，破财招祸
- 挟妓游山：士人奇遇，平人失财

#### 奴隶类诸兆

**吉类**：
- 身为人奴隶：倚人得力，附势争光
- 身作婢吉：谦尊而光，卑以自牧

**凶类**：
- 被奴仆欺侮凶：阳消阴长，上替下陵
- 婢女诟骂：小口不宁

**贞吉否凶类**：
- 买人为仆：失财得人，有凶有吉
- 隶卒忽作官吉：运泰时来"""
    normalized_text_zh: str = """"""
    subject: str = "1 优妓类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_优妓类诸兆_001_L1",
    )
    version: str = "1.0.0"
