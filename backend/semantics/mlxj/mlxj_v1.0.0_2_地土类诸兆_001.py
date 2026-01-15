"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.825973
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
    semantic_id="mlxj_v1.0.0_2_地土类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2地土类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 地平旷大吉：阴土广大深厚，富厚福泽
- 赐茅土之地：吴孙坚母梦典故，主王于翼轸之地
- 居地土中大吉：物生于土，人居土中，生发长养
- 入地见天日大吉：屈极...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 地平旷大吉：阴土广大深厚，富厚福泽
- 赐茅土之地：吴孙坚母梦典故，主王于翼轸之地
- 居地土中大吉：物生于土，人居土中，生发长养
- 入地见天日大吉：屈极复伸，阴极回阳
- 堂前地喷金宝：坤厚载物，主家门产业兴隆
- 运土石入家大吉：土厚重为富征，石峻大为贵象

**吉类**：
- 地动吉：迁居移业，改旧图新
- 掘地出土：被人辱侮，口舌之象
- 开土轻土多利：各以类应
- 人自土中起吉：得子招丁之象

**凶类**：
- 地陷：南方无咎，东方休囚，西方不祥，北方沉顿
- 地开裂大凶：土崩之象，家业衰替
- 地高下不平：疾病、讼不胜、姻不成
- 开地坑大凶：大惊大险，大忧大害

**贞吉否凶类**：
- 掘地得金银珠贝：平人主财名遂志，若有贪想则有感无实
- 埋儿入地：埋儿得金，天感其孝（郭巨典故）

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 赐茅土之地 | 孙坚母 | 生孙坚，王于东吴 | 三国 |
| 立冰上与冰下人语 | 令狐策 | 阳语阴泉，当为君作媒 | 晋 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 地土类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_地土类诸兆_001_L1",
    )
    version: str = "1.0.0"
