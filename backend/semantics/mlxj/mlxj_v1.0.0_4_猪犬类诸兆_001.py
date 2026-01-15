"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.823586
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
    semantic_id="mlxj_v1.0.0_4_猪犬类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 4猪犬类诸兆(SemanticEntry):
    """
    #### 猪类汇总

**吉类**：
- 豕从天降：生男之瑞（汉景帝梦赤彘，生武帝）
- 母猪吉：生育聚畜
- 母猪生小猪：致富

**凶类**：
- 猪啮足凶：关羽典故

#### 犬类汇总

**...
    """
    
    original_text: str = """#### 猪类汇总

**吉类**：
- 豕从天降：生男之瑞（汉景帝梦赤彘，生武帝）
- 母猪吉：生育聚畜
- 母猪生小猪：致富

**凶类**：
- 猪啮足凶：关羽典故

#### 犬类汇总

**吉类**：
- 稻米饭为犬所食吉：福至灾消
- 犬死贞吉：有德则吉

**凶类**：
- 犬自天而下凶：天降灾殃（王敦典故）
- 犬噬人凶：凶无可占
- 犬相咬凶：两人相争
- 犬作人言凶：狱讼之事"""
    normalized_text_zh: str = """"""
    subject: str = "4 猪犬类诸兆"
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
        l1_anchor="mlxj_v1.0.0_4_猪犬类诸兆_001_L1",
    )
    version: str = "1.0.0"
