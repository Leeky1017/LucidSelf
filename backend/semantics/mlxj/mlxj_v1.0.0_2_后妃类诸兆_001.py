"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.819288
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
    semantic_id="mlxj_v1.0.0_2_后妃类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2后妃类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 太任大吉：生明圣之子
- 邑姜大吉：得贤明内助，生女必聪慧过人
- 姜后吉：母后之范，女德之尊
- 邓太后大吉：登政府，宰大邑
- 徐贤妃大吉：博通经史，匡...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 太任大吉：生明圣之子
- 邑姜大吉：得贤明内助，生女必聪慧过人
- 姜后吉：母后之范，女德之尊
- 邓太后大吉：登政府，宰大邑
- 徐贤妃大吉：博通经史，匡主以正

**吉类**：
- 寿阳公主吉：年必高永，名必𫝄垂
- 班婕妤：遭嫉妒受诬，但终得善评
- 马明德皇后吉：大贵人母仪一世

**凶类**：
- 武照凶：阴阳失序，内难几覆
- 戚妃凶：悲哀死丧之应
- 韦后凶：玷污门楣

**贞吉否凶类**：
- 吕后：光明正直者吉，邪佞者贵而凶
- 西施：贞吉否凶，因人而异
- 杨贵妃：贞吉否凶

#### 历代后妃梦象速查

| 后妃 | 吉凶 | 核心主应 |
|------|------|---------|
| 太任 | 大吉 | 生明圣之子 |
| 邑姜 | 大吉 | 得贤内助 |
| 姜后 | 吉 | 母后之范 |
| 邓太后 | 大吉 | 登政府 |
| 徐贤妃 | 大吉 | 匡主以正 |
| 吕后 | 贞吉否凶 | 因人而异 |
| 武照 | 凶 | 阴阳失序 |
| 杨贵妃 | 贞吉否凶 | 色艺超群 |"""
    normalized_text_zh: str = """"""
    subject: str = "2 后妃类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_后妃类诸兆_001_L1",
    )
    version: str = "1.0.0"
