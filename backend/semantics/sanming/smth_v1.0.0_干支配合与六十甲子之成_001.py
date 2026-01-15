"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227621
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
    semantic_id="smth_v1.0.0_干支配合与六十甲子之成_001",
    book_id="sanming",
    engine_id="bazi"
)
class 干支配合与六十甲子之成(SemanticEntry):
    """
    - **原文（source_text）**：
  甲之干乃天之五行，以一阴一阳言之；子之支乃地之五行，以地之方隅言之。合而言之，十配十二，共成六十日，复六六而成岁。陈抟曰：天干始于甲而终于癸，地支起于...
    """
    
    original_text: str = """- **原文（source_text）**：
  甲之干乃天之五行，以一阴一阳言之；子之支乃地之五行，以地之方隅言之。合而言之，十配十二，共成六十日，复六六而成岁。陈抟曰：天干始于甲而终于癸，地支起于子而终于亥，阳自复始，六变而乾阳备；阴自姤始，六变而坤阴成，合二六之数而为十二辰也。

- 分字分词释义：
  - **十配十二，共成六十日**：十干与十二支交叉组合成六十甲子，为时间建立细密刻度；
  - **六变而乾阳备/坤阴成**：阳、阴各经六步而成其全体，对应十二支之成。

- **规范化释义（primary_lang_explained）**：
  最后以干支配合收束前文：十干象天之五行、阴阳；十二支象地之方隅、时序。干支互配成六十甲子，周而复始，一轮为岁。陈抟以「阳自复始六变而乾阳备、阴自姤始六变而坤阴成」来说明十二辰背后的阴阳次第，使干支体系与易理完全连在一起。

- **完整对等诠释（secondary_lang_full）**：

  This concluding section gathers the discussion of stems and branches into a single picture. The Ten Heavenly Stems encode heaven’s Five Elements and the alternation of Yin and Yang; the Twelve Earthly Branches encode earth’s directions and seasonal sequence. When paired, they generate the sixty Jiazi, a cycle in which heaven‑principle, earth‑pattern and time are woven together. One full run of sixty marks a year‑type cycle; repeated six times, Yin and Yang each pass through six stages, which commentators like Chen Tuan liken to the hexagrams Qian and Kun gradually completing themselves. In practice, treating each stem–branch pair as a Jiazi index gives destiny work a natural time unit that is richer than a bare calendar date: it carries both cosmological structure and concrete temporal position."""
    normalized_text_zh: str = """"""
    subject: str = "干支配合与六十甲子之成"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_干支配合与六十甲子之成_001_L1",
    )
    version: str = "1.0.0"
