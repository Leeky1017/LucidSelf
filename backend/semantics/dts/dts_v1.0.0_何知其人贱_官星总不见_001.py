"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997808
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
    semantic_id="dts_v1.0.0_何知其人贱_官星总不见_001",
    book_id="dts",
    engine_id="bazi"
)
class 何知其人贱官星总不见(SemanticEntry):
    """
    - 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人贱：此人地位卑微、无权无位。
  - 官星：八字中代表权位与地位的星曜。
  - 总不见：完全缺失或如同不存在。

- 原注（原文...
    """
    
    original_text: str = """- 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人贱：此人地位卑微、无权无位。
  - 官星：八字中代表权位与地位的星曜。
  - 总不见：完全缺失或如同不存在。

- 原注（原文注解）：
 　　财轻官重、官轻印重、财重无官、官重无印等，皆“官星不见”；又视用神、忌神、主从及岁运。

- 规范化释义（primary_lang_explained）：
  论一个人是否卑贱，则反从“官星不见”着眼：或官星根气极薄、难以成用，或被印、财、劫等牵制遮蔽，以致在现实结构中缺乏正式身份与社会认可，多表现为位卑权轻、做事不由自己作主。

- **核心要点**：
  - 官星若无根、无位、无卫，即便隐约存在，也近似“不见”；
  - 财重无官、官重无印，皆难构成稳定权位；
  - 仍需结合体用与岁运，看是否有翻身之机。

- 详细解说：
  与前条相对，本条指出“官星不见”的多种形态：有的是官星位置太偏，难以发挥体用；有的是被过重之印或财所夺，使官名有而权实无；有的干脆财旺身弱而无官可依，只能在生计与关系之间辗转奔波。这并非简单断“贫贱”，而是指出其在制度与等级结构中的弱势地位。若后天岁运能补官、扶身，仍可改善；若反而进一步削官、重浊，则贱象加深。

- 校勘与字词辨析：
  - “总不见”：强调的是长期走势，而非短期一时的贫富波动。

- **次语种完整诠释（secondary_lang_full）**：
  We know a person is base in status when the Official star is essentially absent: either no Officer at all, or one that is so weak, scattered, or constantly stolen by other stars that it cannot function. In such charts, there is little formal authority or recognised position; even when titles appear, they tend to be hollow or short-lived."""
    normalized_text_zh: str = """"""
    subject: str = "何知其人贱，官星总不见。"
    factor_refs: list = ['lowly_risk', 'official_star_absent', 'official_star_absent', 'damage_level', 'official_star_damaged']
    
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
        l1_anchor="dts_v1.0.0_何知其人贱_官星总不见_001_L1",
    )
    version: str = "1.0.0"
