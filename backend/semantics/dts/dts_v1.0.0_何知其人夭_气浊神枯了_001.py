"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997847
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
    semantic_id="dts_v1.0.0_何知其人夭_气浊神枯了_001",
    book_id="dts",
    engine_id="bazi"
)
class 何知其人夭气浊神枯了(SemanticEntry):
    """
    - **原文（source_text）**：
  何知其人夭，气浊神枯了。

- 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人夭：此人夭折、寿命短促。
  - 气浊：气机浑浊、五...
    """
    
    original_text: str = """- **原文（source_text）**：
  何知其人夭，气浊神枯了。

- 分字分词释义：
  - 何知：如何判断、凭什么知道。
  - 其人夭：此人夭折、寿命短促。
  - 气浊：气机浑浊、五行失和。
  - 神枯：元神枯竭、精神无托。
  - 了：事已至此、无可挽回之叹。

- 规范化释义（primary_lang_explained）：
  判断一人是否有夭折之忧，要看全局之气是否浊乱、元神是否枯槁：喜神尽伤、忌神辗转攻身而无以恢复，便是“气浊神枯”的根本图像。

- **核心要点**：
  - 以“气浊神枯”为夭的总纲，而非单凭一两处凶象；
  - 喜神无力、忌神连攻、冲绝滞重者，多有早折之险；
  - 仍须结合岁运，看是否存在挽回与缓和之机。

- 详细解说：
  与前一句“性定元气厚”相对，本句给出寿夭判断的反面标准：当命局中元气不固、喜神多遭冲破、忌神反复得势，导致整体气机浑浊、精神之“神”无以承载，便容易在关键岁运中出现病灾、横祸或气数早尽的情形。判断时既要看先天结构是否清浊分明，也要看后天运势是否一味加重浊气，而毫无开清之机。

- 校勘与字词辨析：
  - “气浊神枯了”中的“了”字，有“事已至此”的感叹意味，强调事态之重。

- 原注（原文注解）（要旨）：
 　　“性静而无冲合缺贪”“元神厚”“不反冲绝滞”者多寿；反之气浊神枯者多夭。

- 分字分词释义（总论）：
  - 官星有理会：官得位、有印卫、财通达。
  - 财气通门户：财路通畅、门户成形。
  - 喜神辅弼：喜神助用为吉。
  - 忌神辗转攻：忌神轮番进攻为凶。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 夭 | Early Death | 夭折、短寿 | Premature death | mortality_risk | new_candidate |
| 气浊 | Qi Turbid | 气机浑浊不清 | Cloudy and disordered energy | qi_clarity | new_candidate |
| 神枯 | Spirit Withered | 元神枯槁 | Exhausted spirit | spirit_vitality | new_candidate |
| 气浊神枯 | Qi Turbid Spirit Withered | 气数已尽 | Energy exhausted | mortality_risk | new_candidate |
| 喜神尽伤 | Joy God Damaged | 喜神被克破 | Favorable god injured | joy_god_strength | existing |
| 忌神辗转攻 | Malicious God Attacks | 忌神肆虐 | Bad god attacks repeatedly | attack_frequency | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Fortune-Judgment: Noble (Gui) if Official God has "Reason/Configuration" (You-Li-Hui). Base (Jian) if Official is unseen. Rich (Fu) if Wealth Qi connects to Gate (Tong-Men-Hu). Poor (Pin) if Wealth is untrue. Auspicious (Ji) if Happy God supports. Ominous (Xiong) if Malicious God attacks. Long Life (Shou) if Nature Stable/Qi Thick. Early Death (Yao) if Qi Turbid/Spirit Withered."""
    normalized_text_zh: str = """"""
    subject: str = "何知其人夭，气浊神枯了。"
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
        l1_anchor="dts_v1.0.0_何知其人夭_气浊神枯了_001_L1",
    )
    version: str = "1.0.0"
