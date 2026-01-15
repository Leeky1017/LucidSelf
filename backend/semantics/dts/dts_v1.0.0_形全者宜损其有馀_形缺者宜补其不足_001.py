"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997315
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
    semantic_id="dts_v1.0.0_形全者宜损其有馀_形缺者宜补其不足_001",
    book_id="dts",
    engine_id="bazi"
)
class 形全者宜损其有馀形缺者宜补其不足(SemanticEntry):
    """
    - **原文（source_text）**：
  形全者宜损其有馀，形缺者宜补其不足。

- 原注（原文注解）：
  　　如甲木生于寅卯辰月，丙火生于巳午未月，皆为形全。
  　　戊土生于寅卯辰月，庚...
    """
    
    original_text: str = """- **原文（source_text）**：
  形全者宜损其有馀，形缺者宜补其不足。

- 原注（原文注解）：
  　　如甲木生于寅卯辰月，丙火生于巳午未月，皆为形全。
  　　戊土生于寅卯辰月，庚金生于巳午未月，皆为形缺，馀仿此。

- 分字分词释义：
  - 形全：某行之形气纯全.
  - 有馀：偏多之处.
  - 形缺：某行之形气不足.

- **规范化释义（primary_lang_explained）**：
  形全则多，宜损其有馀；形缺则少，宜补其不足.以季节与方局判断"全/缺"，再施以损/补之法.


- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 形全 | Full Form | 某五行在季节与局势上得到充分支持 | An element fully supported by season and configuration | xingquan | new_candidate |
| 形缺 | Deficient Form | 某五行在季节或局势中明显偏弱 | An element clearly weak or missing | xingque | new_candidate |
| 有馀 | Surplus Qi | 某一行之力偏多 | Surplus of a given element | youyu | new_candidate |
| 不足 | Deficient Qi | 某一行明显偏少 | Clear lack of a given element | buzu | new_candidate |
| 损补策略 | Drain-Tonify Strategy | 通过泄多补少以恢复平衡 | Strategy of draining excess and tonifying deficiency | sunbu_celue | new_candidate |

- **次语种完整诠释（secondary_lang_full）**:
  This verse takes the idea of "form" one step further. When a particular element is already fully formed – strongly supported by season, direction, and surrounding branches – it tends to overflow and dominate. In such cases, the right move is to trim what is excessive: let some of that qi leak, be spent, or be gently controlled so that it does not harden into stubborn imbalance. When an element is clearly under-formed and weak, the rule reverses: one should protect and supplement it, giving it warmth, resources, or structural backing until it can stand in proper proportion to the rest. All judgments of "full" and "deficient" must be made in the context of time and spatial configuration, not from a single branch in isolation. The practical art is to recognise which lines in the chart carry surplus and which suffer lack, then design draining and tonifying accordingly."""
    normalized_text_zh: str = """"""
    subject: str = "形全者宜损其有馀，形缺者宜补其不足。"
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
        l1_anchor="dts_v1.0.0_形全者宜损其有馀_形缺者宜补其不足_001_L1",
    )
    version: str = "1.0.0"
