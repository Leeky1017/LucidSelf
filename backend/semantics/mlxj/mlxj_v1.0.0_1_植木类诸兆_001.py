"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.802937
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
    semantic_id="mlxj_v1.0.0_1_植木类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1植木类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 松大吉：挺拔峥嵘，位高迁，青云路达（丁固典故）
- 柏吉：凌霜节操，冰霜节操

**吉类**：
- 椿吉：椿庭有庆（父业象征）
- 桑吉：经纬操持，名显利实...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 松大吉：挺拔峥嵘，位高迁，青云路达（丁固典故）
- 柏吉：凌霜节操，冰霜节操

**吉类**：
- 椿吉：椿庭有庆（父业象征）
- 桑吉：经纬操持，名显利实
- 槐吉：位居台辅，生贤贵子（王旦三槐典故）
- 楮吉：五榖丰盈

**贞吉否凶类**：
- 梿：科甲高捷，病未即痊
- 松响：根牢坚固，但须谨密

**凶类**：
- 漆凶：漆戚音同，涕泪沾襟
- 樗栎：非美材，唐愚之人
- 荆棘：作事有阻，病体啾唧

#### 典故

- 丁固梦松出腹：十八年后位公（松=十八公）
- 王旦三槐：手植三槐于庭，后果为三公"""
    normalized_text_zh: str = """"""
    subject: str = "1 植木类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_植木类诸兆_001_L1",
    )
    version: str = "1.0.0"
