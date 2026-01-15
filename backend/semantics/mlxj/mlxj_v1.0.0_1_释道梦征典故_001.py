"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.810813
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
    semantic_id="mlxj_v1.0.0_1_释道梦征典故_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1释道梦征典故(SemanticEntry):
    """
    #### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 宋 | 牧牛寺主 | 枉杀贫道 | 抚军自缢 |
| 梁 | 武帝 |...
    """
    
    original_text: str = """#### 典故汇总

| 朝代 | 人物 | 梦象 | 应验 |
|------|------|------|------|
| 宋 | 牧牛寺主 | 枉杀贫道 | 抚军自缢 |
| 梁 | 武帝 | 眇目僧 | 生绎为元帝 |
| 唐 | 司空图 | 二僧授道 | 号耐辱居士 |
| 唐 | 庞严 | 二僧入寝门 | 预言寿数官职 |
| 唐 | 白鹤观钟 | 道士求归 | 钟归本观 |
| 宋 | 邵武徐熙春 | 铁冠道人 | 不复粒食 |
| 宋 | 程夷伯 | 觉海僧授药 | 延寿修桥 |

#### 觉海典故（详）

程夷伯年二十九，梦其父曰：汝今年当死，可问觉海。

后遇蜀僧寤铨字觉海善相术，觉海呵气入水令饮，夜梦官府左右廊：

- 左廊：修桥路人，衣冠严整相欣悦
- 右廊：毁桥路人，枷锁缧袣哀号涕泗

夷伯悟而修桥路道，觉海云寿可延，后果年至九十二。"""
    normalized_text_zh: str = """"""
    subject: str = "1 释道梦征典故"
    factor_refs: list = []
    
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
        l1_anchor="mlxj_v1.0.0_1_释道梦征典故_001_L1",
    )
    version: str = "1.0.0"
