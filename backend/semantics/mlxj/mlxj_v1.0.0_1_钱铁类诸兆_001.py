"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.785839
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
    semantic_id="mlxj_v1.0.0_1_钱铁类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1钱铁类诸兆(SemanticEntry):
    """
    #### 钱类汇总

**吉类**：
- 大钱：钱福为会元
- 上清五铢：岑文本典故
- 天雨钱：熊衮典故

**贞吉否凶类**：
- 钱贞吉否凶：通达万变
- 掘地求钱：得不如失

#### 铁类汇...
    """
    
    original_text: str = """#### 钱类汇总

**吉类**：
- 大钱：钱福为会元
- 上清五铢：岑文本典故
- 天雨钱：熊衮典故

**贞吉否凶类**：
- 钱贞吉否凶：通达万变
- 掘地求钱：得不如失

#### 铁类汇总

**吉类**：
- 铁马吉：出行名誉
- 铁拐吉：能持能行
- 铁桶大吉：江山一统
- 镔铁如意吉：凡事如意
- 铁砚：立志钻研

**凶类**：
- 铁锤凶：孙俊民典故

#### 珍宝类汇总

**吉类**：
- 琉璃大吉：日月之精
- 玛瑙大吉：文章魁首
- 琥珀大吉：晋阶秩
- 水晶吉：质地纯粹
- 珊瑚吉：高贵珍物
- 玫瑰吉：文章魁首
- 琨㻍吉：切玉如泥

**凶类**：
- 胭脂凶：阴道盛阳道衰
- 翡翠凶：非义非法"""
    normalized_text_zh: str = """"""
    subject: str = "1 钱铁类诸兆"
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
        l1_anchor="mlxj_v1.0.0_1_钱铁类诸兆_001_L1",
    )
    version: str = "1.0.0"
