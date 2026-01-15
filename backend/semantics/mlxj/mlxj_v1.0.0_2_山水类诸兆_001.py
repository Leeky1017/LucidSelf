"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.825993
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
    semantic_id="mlxj_v1.0.0_2_山水类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2山水类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 山行大吉：履高山居高位，亨通尊贵
- 登须弥山/昆仑：主居天下之镇，非平等兆
- 上山捧日：程昱、杨炎典故，辅君登相
- 青山大吉：青春佳偶，老还童
- 大...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 山行大吉：履高山居高位，亨通尊贵
- 登须弥山/昆仑：主居天下之镇，非平等兆
- 上山捧日：程昱、杨炎典故，辅君登相
- 青山大吉：青春佳偶，老还童
- 大水澄清大吉：贫而富，贱而贵
- 水流汪洋：新婚喜庆，财源涌来

**吉类**：
- 开山：主得通达
- 山上流泉：利见大人
- 饮水不止：利无穷，财源通达
- 流水绕身：祸患突临，争讼入狱

**凶类**：
- 土山坏：眉鼻有伤，家园废败
- 山崩裂：陨坠开离之象
- 天下大水：主兵戈水患
- 溺水沉：没入者凶

**贞吉否凶类**：
- 升山坠地：升至半山坠地，前吉后凶
- 立水上：凡事虚浮危险，女人梦之主倾国之誉

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 上山捧日 | 程立（昱） | 辅魏太祖，改名程昱 | 三国 |
| 上山捧日 | 杨炎 | 登宰相之位 | 唐 |
| 山上流泉 | 邓艾 | 克蜀身不返 | 三国 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 山水类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_山水类诸兆_001_L1",
    )
    version: str = "1.0.0"
