"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.853811
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
    semantic_id="mlxj_v1.0.0_2_疾疫类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2疾疫类诸兆(SemanticEntry):
    """
    #### 分类汇总

**吉类**：
- 病者梦呕吐：病痊可治
- 应试梦呕吐大吉昌：功名可成
- 衰老梦呕吐：身体康健
- 病忽痊：身无疾而梦病起者吉

**凶类**：
- 病卧床褥：精神虚损
- ...
    """
    
    original_text: str = """#### 分类汇总

**吉类**：
- 病者梦呕吐：病痊可治
- 应试梦呕吐大吉昌：功名可成
- 衰老梦呕吐：身体康健
- 病忽痊：身无疾而梦病起者吉

**凶类**：
- 病卧床褥：精神虚损
- 病坐舟车：风波险阻
- 梦君王疾病：世乱年荒
- 梦宰官病：失直得枉

**亲属病梦对应**：
| 梦象 | 主应 |
|------|------|
| 梦父病 | 精虚 |
| 梦母病 | 血疾 |
| 梦子病 | 神伤 |
| 梦妻病 | 衣破 |
| 梦兄弟病 | 手足有疾 |
| 梦邻里病 | 屋宇损坏 |
| 梦奴仆病 | 行事艰难 |

#### 神授医药典故

- 刘灵哲母病：梦黄衣老人授竹笋方
- 齐竟陵王：梦金像灌神汤而愈
- 齐建安王：梦观音傅药疮愈
- 陈太后：梦神人餽药，生太祖高皇帝"""
    normalized_text_zh: str = """"""
    subject: str = "2 疾疫类诸兆"
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
        l1_anchor="mlxj_v1.0.0_2_疾疫类诸兆_001_L1",
    )
    version: str = "1.0.0"
