"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227655
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
    semantic_id="smth_v1.0.0_十二宫与人生阶段_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十二宫与人生阶段(SemanticEntry):
    """
    - **原文（source_text）**：
  何言乎？子丑二位，阴阳始孕，人在胞胎，物藏根，未有涯际；寅卯二位，阴阳渐开，人渐生长，物以拆甲，群葩渐剖，如人将有立身也；辰巳二位，阴阳气盛，物当华秀...
    """
    
    original_text: str = """- **原文（source_text）**：
  何言乎？子丑二位，阴阳始孕，人在胞胎，物藏根，未有涯际；寅卯二位，阴阳渐开，人渐生长，物以拆甲，群葩渐剖，如人将有立身也；辰巳二位，阴阳气盛，物当华秀，如人三十、四十而有立身之地，始有进取之象；午未二位，阴阳彰露，物已成齐，人至五十、六十，富贵贫贱可知，凡百兴衰可见；申酉二位，阴阳肃杀，物已收成，人已龟缩，各得其静矣；戌亥二位，阴阳闭塞，物气归根，人当休息，各有归着。详此十有二位先后，六十甲子可以次第而晓。

- 分字分词释义：
  - **阴阳始孕/渐开/气盛/彰露/肃杀/闭塞**：对应人生六个大阶段，从胎孕到终老归根。
  - **可以次第而晓**：按十二宫顺序，便可把六十甲子的象义看成一生展开的次第。

- **规范化释义（primary_lang_explained）**：
  本段将十二地支宫位分配为人生的六大阶段：子丑为胎孕与根藏，寅卯为出生与成长，辰巳为华秀与事业发端，午未为成就与盛年，申酉为收成与老成，戌亥为归根与休息。六十甲子分布其间，就像把一生的不同阶段细分成六十个刻度，便于用纳音之象描摹人生的进程。

- **完整对等诠释（secondary_lang_full）**：

  The twelve earthly branches are here arranged as six broad stages of life. Zi and Chou mark conception and hidden rooting, when Qi is stored and forms are not yet visible. Yin and Mao cover emergence and growth, as things break shell and shoot upward. Chen and Si correspond to flourishing and display: talents blossom and careers begin to take shape. Wu and Wei stand for full manifestation and settled status—by this phase wealth or poverty, rise or decline, are largely apparent. Shen and You describe harvest and contraction, when results are gathered in and one withdraws to a smaller, steadier posture. Xu and Hai indicate closure and return to root, when Qi sinks back and people move into rest and final belonging. Laying the sixty Jiazi across these twelve positions is like dividing a lifetime into sixty ticks on a dial: Nayin images can then be read not only for what they describe, but also for when in the life‑course they are most active."""
    normalized_text_zh: str = """"""
    subject: str = "十二宫与人生阶段"
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
        l1_anchor="smth_v1.0.0_十二宫与人生阶段_001_L1",
    )
    version: str = "1.0.0"
