"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227628
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
    semantic_id="smth_v1.0.0_六十律与纳音立法_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六十律与纳音立法(SemanticEntry):
    """
    - **原文（source_text）**：
  尝观《笔谈》论六十甲子纳音，本六十律，旋相为宫，法也。纳音与《易》纳甲同法：干纳甲、坤纳癸，始于干而终于坤。纳音始于金，金，干也，终于土，土，坤也。五...
    """
    
    original_text: str = """- **原文（source_text）**：
  尝观《笔谈》论六十甲子纳音，本六十律，旋相为宫，法也。纳音与《易》纳甲同法：干纳甲、坤纳癸，始于干而终于坤。纳音始于金，金，干也，终于土，土，坤也。五行之中，惟有金铸而为器，则音响彰，纳音所以先金。

- 分字分词释义：
  - **六十律，旋相为宫**：以六十条律吕轮流为宫位，构成六十甲子的音律基础。
  - **纳甲同法**：与《易》之纳甲同样，以干支对应卦爻和音律的系统方法。
  - **始于金，终于土**：纳音从金起、以土终，分别象征「干」与「坤」的开合。

- **规范化释义（primary_lang_explained）**：
  本段指出，六十甲子的纳音本于六十条律吕，轮番为宫。它的立法与《易》中的纳甲相同：以干为阳、坤为阴，自干起、以坤终。纳音从金开始、以土收束，因为在五行之中，金可以铸成器物而发出清晰声响，最适合作为「音」的载体，因此纳音体系中以金为先。

- **完整对等诠释（secondary_lang_full）**：

  Here the author explains that the Nayin assigned to the sixty Jiazi rests on a sequence of sixty musical lü (pitch standards), which take turns serving as the "ruler" tone. Its construction follows the same logic as the Yijing practice of "nailing stems" to hexagrams: Qian stands at the Yang end, Kun at the Yin end, and the cycle runs from heaven’s initiative to earth’s completion. Nayin begins with Metal and ends with Earth because, among the Five Elements, only metal can be cast into instruments whose sound rings out clearly, while Earth gathers and contains what has been produced. Nayin is therefore not a separate Five‑Element system but an acoustic overlay on the stem–branch cycle—a way of giving each Jiazi a particular timbre and material quality that enriches, rather than replaces, the underlying structure."""
    normalized_text_zh: str = """"""
    subject: str = "六十律与纳音立法"
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
        l1_anchor="smth_v1.0.0_六十律与纳音立法_001_L1",
    )
    version: str = "1.0.0"
