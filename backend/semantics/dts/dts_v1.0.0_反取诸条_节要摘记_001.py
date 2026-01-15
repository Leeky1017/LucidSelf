"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997623
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
    semantic_id="dts_v1.0.0_反取诸条_节要摘记_001",
    book_id="dts",
    engine_id="bazi"
)
class 反取诸条节要摘记(SemanticEntry):
    """
    - **原文（source_text）**：
  反取诸条（节要摘记）。

- 规范化释义（primary_lang_explained）：
  本节提纲式地汇总若干“反取”格局，如“君赖臣生”“儿能...
    """
    
    original_text: str = """- **原文（source_text）**：
  反取诸条（节要摘记）。

- 规范化释义（primary_lang_explained）：
  本节提纲式地汇总若干“反取”格局，如“君赖臣生”“儿能生母”“母慈灭子”“夫健怕妻”等，强调在常规顺用之外，还可以通过逆向取力，在“制中有生、生中有制”之中恢复整体平衡。

- **核心要点**：
  - 反取并非逆天，而是在失衡时从相反一端借力以达平衡；
  - 多通过“制中生、生中制”实现，避免一端独强或独弱；
  - 关键在能否恢复循环，而非单纯谁克谁、谁生谁。

- 详细解说：
  传统取用多讲顺势，如官赖印、身赖比劫等，而本节特别提出一组看似“逆理”的用法：君反赖臣生、儿能生母、母慈反灭子、夫健反怕妻……这些结构在表层关系上似乎违背常规，却在更高层面维护了系统的闭环。判断时须看这种反向用力是否真能令气机重新流通，而非制造新的堵塞。

- 校勘与字词辨析：
  - “节要摘记”：说明本段为诸条要旨的提要，并非逐条详解。

- 原注（原文注解）：
  　　“君赖臣生”“儿能生母”“母慈灭子”“夫健怕妻”等反取之机，多以“制中生、生中制”达平衡。

 - **规范化释义（primary_lang_explained）**：
  反中有顺，顺中有制；以制化开路，使气机可循环。

- 分字分词释义：
  - 君赖臣生：官赖财生或印赖食生之类的逆取。
  - 儿能生母：食伤反生印的权变。
  - 母慈灭子：印过度而克耗食伤。
  - 夫健怕妻：比劫旺而畏财之反势。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 反取 | Reverse Take (Fan-Qu) | 反向取用 | Using the opposite force | fanqu | existing |
| 君赖臣生 | Ruler Relies on Subject | 官赖财生/印赖食生 | Official relies on Wealth/Resource | junlaichensheng | new_candidate |
| 儿能生母 | Child Generates Mother | 食伤生印 | Output generates Resource | ernengshengmu | new_candidate |
| 母慈灭子 | Mother Smothers Child | 印多克食 | Excessive Resource destroys Output | mucimiezi | new_candidate |
| 夫健怕妻 | Husband Fears Wife | 比劫畏财 | Rival fears Wealth | fujianpaqi | new_candidate |
| 制中生 | Growth in Control | 制约中含生机 | Growth within restraint | zhizhongsheng | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Reverse-Take (Fan-Qu): Includes "Ruler Relies on Subject" (Jun-Lai Chen-Sheng), "Child Generates Mother" (Er-Neng Sheng-Mu), "Mother Smothers Child" (Mu-Ci Mie-Zi), "Husband Fears Wife" (Fu-Jian Pa-Qi). These patterns use "Control within Growth" (Zhi-Zhong-Sheng) or "Growth within Control" (Sheng-Zhong-Zhi) to restore balance."""
    normalized_text_zh: str = """"""
    subject: str = "反取诸条（节要摘记）："
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
        l1_anchor="dts_v1.0.0_反取诸条_节要摘记_001_L1",
    )
    version: str = "1.0.0"
