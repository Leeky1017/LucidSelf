"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.840321
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
    semantic_id="mlxj_v1.0.0_2_彝伦类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2彝伦类诸兆(SemanticEntry):
    """
    #### 五伦亲属梦象分类

**登天类**（梦亲属登天）：
- 梦君登天：已崩者为天宫帝君
- 梦臣登天：升天官宰职，位居极品
- 梦父母登天：寿年不永；已故者冥府超升
- 梦夫登天：官宦位高；已故...
    """
    
    original_text: str = """#### 五伦亲属梦象分类

**登天类**（梦亲属登天）：
- 梦君登天：已崩者为天宫帝君
- 梦臣登天：升天官宰职，位居极品
- 梦父母登天：寿年不永；已故者冥府超升
- 梦夫登天：官宦位高；已故者主妇安康
- 梦妻登天：夫荣宠至；已故者无咎
- 梦子登天：初生者大贵，有疾者大凶
- 梦师友登天：应试吉

**生死类**：
- 梦亲属死：有病者宜解禳，无病者主有远行
- 梦亲属复生：已故者主有感应，须详所求

**折花栽木类**：
- 折桂花：功名不进
- 折牡丹：女人不利
- 折桃花：寿命不永
- 折梅花：子嗣生灾
- 折莲花：夫妇不谐
- 栽桂杏：及第
- 栽榴柿：子嗣森贤

**鸟兽类**：
- 乘虎豹麒麟：身荣利遂
- 乘凤鸾鹏鹗：谐偶发祥
- 化龙凤：富贵非常
- 化鸡犬：必为盗贼

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 梦虞世南 | 唐太宗 | 图形凌烟阁 | 唐 |
| 梦惠连 | 谢灵运 | 得「池塘生春草」句 | 南朝 |
| 梦白头翁 | 田千秋 | 拜大鸿胪、丞相 | 汉 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 彝伦类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_彝伦类诸兆_001_L1",
    )
    version: str = "1.0.0"
