"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.782261
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
    semantic_id="mlxj_v1.0.0_1_耳鼻诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1耳鼻诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 两眸高出似蟹眼吉：龙睛之象，富贵显荣
- 睛入鼻孔中吉：志在山林
- 纳宝入眸子吉：李古典故
- 鼻頞内生牙大吉：两虎排牙，威振千里

**吉类**：
- ...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 两眸高出似蟹眼吉：龙睛之象，富贵显荣
- 睛入鼻孔中吉：志在山林
- 纳宝入眸子吉：李古典故
- 鼻頞内生牙大吉：两虎排牙，威振千里

**吉类**：
- 鼻无两孔吉：气通畅象
- 鼻口相联吉：心细不发形
- 鼻垂于唇下大吉：年寿增长
- 鼻赤吉：酒醉鼻头红

**凶类**：
- 睛坠凶：主凶丧
- 眼无瞦凶：差讹不识，骄不顾人
- 鼻柱伤大凶：大痛无声，主斗殴劫杀
- 鼻梁破碎凶：无事破败，有财难保

**贞吉否凶类**：
- 黑白异色：世乱身强/家寒身困
- 睫睑生长毛：宋巢元修典故

#### 耳鼻象征体系

| 部位 | 五行 | 象征 | 主应领域 |
|------|------|------|---------|
| 眼 | 火 | 精神/智慧 | 名誉/判断 |
| 耳 | 水 | 聪明/消息 | 信息/人际 |
| 鼻 | 土 | 财帛/寿命 | 财富/健康 |
| 口 | 金 | 言语/禄食 | 口舌/饮食 |"""
    normalized_text_zh: str = """"""
    subject: str = "1 耳鼻诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_耳鼻诸兆_001_L1",
    )
    version: str = "1.0.0"
