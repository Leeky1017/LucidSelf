"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997594
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
    semantic_id="dts_v1.0.0_抑强扶弱者常理_用强舍弱者元机_001",
    book_id="dts",
    engine_id="bazi"
)
class 抑强扶弱者常理用强舍弱者元机(SemanticEntry):
    """
    - **原文（source_text）**：
  抑强扶弱者常理，用强舍弱者元机。

- 原注（原文注解）：
  　　强众而敌寡者，势在去其寡；强寡而敌众者，势在成乎众。强寡而敌众者，喜强而助强者吉；...
    """
    
    original_text: str = """- **原文（source_text）**：
  抑强扶弱者常理，用强舍弱者元机。

- 原注（原文注解）：
  　　强众而敌寡者，势在去其寡；强寡而敌众者，势在成乎众。强寡而敌众者，喜强而助强者吉；强众而敌寡者，恶敌而敌众者滞也。

- **规范化释义（primary_lang_explained）**：
  常法：抑强扶弱。变法：用强舍弱，择势为机。审“众寡”立法度。

- 分字分词释义：
  - 抑强扶弱：压制强者、扶助弱方以平衡。
  - 用强舍弱：在特定情势下借助强势反成其功。
  - 元机：根本机括、要津。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 众寡 | Many-Few (Zhong-Gua) | 党众与势寡 | Majority and minority | zhonggua | existing |
| 抑强扶弱 | Suppress Strong Support Weak | 平衡常理 | Balance principle | yiqiang_furuo | new_candidate |
| 用强舍弱 | Use Strong Discard Weak | 顺势元机 | Follow power principle | yongqiang_sheruo | new_candidate |
| 元机 | Deep Mechanism (Yuan-Ji) | 根本奥秘 | Fundamental secret | yuanji | existing |
| 强众敌寡 | Strong Many vs Few | 众强寡弱 | Majority strong | qiangzhong_digua | new_candidate |
| 强寡敌众 | Strong Few vs Many | 寡强众弱 | Minority strong | qianggua_dizhong | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Zhong-Gua (Many-Few) theory: Common rule is "Suppress Strong, Support Weak" (Yi-Qiang Fu-Ruo). Deep mechanism (Yuan-Ji) is "Use Strong, Discard Weak" (Yong-Qiang She-Ruo). When Few oppose Many, if Few are Strong, support Few; if Many are Strong, support Many. Context of "Body" and "Use" defines the strategy."""
    normalized_text_zh: str = """"""
    subject: str = "抑强扶弱者常理，用强舍弱者元机。"
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_抑强扶弱者常理_用强舍弱者元机_001_L1",
    )
    version: str = "1.0.0"
