"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.829284
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
    semantic_id="mlxj_v1.0.0_2_巾带环钗类_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2巾带环钗类(SemanticEntry):
    """
    #### 巾带类汇总

**大吉类**：
- 犀角带大吉：清而灵，品贵清高
- 象牙带吉：位高德重
- 百宝带吉：富利缠身
- 金带吉：孕生贵子
- 银带大吉：初登云路

**吉类**：
- 玉带：晋...
    """
    
    original_text: str = """#### 巾带类汇总

**大吉类**：
- 犀角带大吉：清而灵，品贵清高
- 象牙带吉：位高德重
- 百宝带吉：富利缠身
- 金带吉：孕生贵子
- 银带大吉：初登云路

**吉类**：
- 玉带：晋帝典故
- 红汗巾吉：喜事临身

#### 环钗类汇总

**吉类**：
- 佩白玉玦吉：祸患去，疾病消
- 簪黄金钗吉：贵人相亲
- 簪凤头钗吉：士人登高第
- 双凤玦利吉：喜事重重
- 竹钗吉：闺阃贞烈

**凶类**：
- 钗忽折凶：丧妻之厄"""
    normalized_text_zh: str = """"""
    subject: str = "2 巾带环钗类"
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
        l1_anchor="mlxj_v1.0.0_2_巾带环钗类_001_L1",
    )
    version: str = "1.0.0"
