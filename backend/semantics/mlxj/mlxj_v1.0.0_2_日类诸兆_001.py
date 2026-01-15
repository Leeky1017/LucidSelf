"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.793466
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
    semantic_id="mlxj_v1.0.0_2_日类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2日类诸兆(SemanticEntry):
    """
    #### 原文摘要与分类

**大吉类**：
- 日中天大吉：太阳方中，万物光明，世运熙隆
- 日初升吉：位将升，福将至，业将兴
- 日出云霞映射吉：孤阳初振，佳气萌生
- 云开见日吉：臣遇君，仆得主...
    """
    
    original_text: str = """#### 原文摘要与分类

**大吉类**：
- 日中天大吉：太阳方中，万物光明，世运熙隆
- 日初升吉：位将升，福将至，业将兴
- 日出云霞映射吉：孤阳初振，佳气萌生
- 云开见日吉：臣遇君，仆得主，讼有理
- 登山捧日大吉：履帝居而辅圣君（程昱典故）
- 吞日大吉：仕者登相位，文人擢魁元，孕者生贵子
- 日光入户吉：贵人来也
- 日光照身吉：君恩也，宠至也
- 双手捧日大吉：元首明，股肱良

**凶类**：
- 日黑暗凶：诸事不佳，奸邪欺蔽
- 日蚀凶：帝王主夷虏相侵，平人主椿萱忧患
- 日缺半轮凶：至尊驾幸，双亲身损
- 山衔日大凶：下人怀欺，臣弑君

**贞吉否凶类**：
- 日斗：天无二日，斗者争雄之象
- 骑日上天：贵人登宝位，老人不祥
- 日坠复升：职落复起，家业中兴

#### 典故素材

| 梦象 | 梦者 | 应验 | 出处 |
|------|------|------|------|
| 登山捧日 | 程立 | 事魏太祖，改名程昱 | 三国 |
| 登山视日 | 杨炎 | 登宰相之位 | 唐 |
| 吞日 | 陈霸先 | 登宰相之位 | 南朝 |
| 日出室内 | 拓跋圭母贺后 | 生魏道武帝 | 北魏 |
| 日化龙绕己 | 高夫人 | 生世宗 | 北魏 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 日类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_日类诸兆_001_L1",
    )
    version: str = "1.0.0"
