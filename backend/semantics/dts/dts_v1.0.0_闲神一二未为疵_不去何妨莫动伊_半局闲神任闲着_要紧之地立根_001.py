"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997732
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
    semantic_id="dts_v1.0.0_闲神一二未为疵_不去何妨莫动伊_半局闲神任闲着_要紧之地立根_001",
    book_id="dts",
    engine_id="bazi"
)
class 闲神一二未为疵不去何妨莫动伊半局闲神任闲着要紧之地立根(SemanticEntry):
    """
    - **原文（source_text）**：
  闲神一二未为疵，不去何妨莫动伊，半局闲神任闲着，要紧之地立根基。

- 原注（原文注解）：
  　　喜神不必多，忌神不必多；余者皆闲神。闲神不动无碍；...
    """
    
    original_text: str = """- **原文（source_text）**：
  闲神一二未为疵，不去何妨莫动伊，半局闲神任闲着，要紧之地立根基。

- 原注（原文注解）：
  　　喜神不必多，忌神不必多；余者皆闲神。闲神不动无碍；要紧之地自立根基。运亦以“行己之边界”为妙。

- **规范化释义（primary_lang_explained）**：
  识别闲神、勿妄动；紧要处立根，运随本边界行之。

- 分字分词释义：
  - 闲神：非喜非忌，或暂不入用之神。
  - 要紧之地：体用关键节点与主线。
  - 立根基：在关键处安根立势。

- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 闲神 | Idle God (Xian-Shen) | 闲置之神 | Inactive element | xianshen | existing |
| 未为疵 | Not a Flaw | 不算毛病 | Not a defect | weiweici | new_candidate |
| 莫动伊 | Do Not Move It | 勿扰动 | Don't disturb | modongyi | new_candidate |
| 要紧之地 | Crucial Place | 关键位置 | Key position | yaojinzhidi | new_candidate |
| 立根基 | Establish Foundation | 安身立命 | Set roots | ligenji | new_candidate |
| 边界 | Boundary | 分寸界限 | Limit/Boundary | bianjie | new_candidate |

- **次语种完整诠释（secondary_lang_full）**:  
  Xian-Shen (Idle God) theory: One or two Idle Gods (Xian-Shen) are not a flaw (Wei-Wei-Ci). Do not disturb them (Mo-Dong-Yi). Let them be idle. Establish roots in "Crucial Places" (Yao-Jin-Zhi-Di). Luck should also follow the boundaries."""
    normalized_text_zh: str = """"""
    subject: str = "闲神一二未为疵，不去何妨莫动伊，半局闲神任闲着，要紧之地立根基。"
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
        l1_anchor="dts_v1.0.0_闲神一二未为疵_不去何妨莫动伊_半局闲神任闲着_要紧之地立根_001_L1",
    )
    version: str = "1.0.0"
