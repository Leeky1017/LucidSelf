"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228086
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
    semantic_id="smth_v1.0.0_五行气性材位的配合原理_001",
    book_id="sanming",
    engine_id="bazi"
)
class 五行气性材位的配合原理(SemanticEntry):
    """
    - **原文（source_text）**：
  盖五行之在天下，各有气性，有材位，或相济，或相克，若成器、木成器，旺中受绝，绝中受气，惟相配而取之为不同耳。此金数之所以难同，而又有海中、沙中之异。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  盖五行之在天下，各有气性，有材位，或相济，或相克，若成器、木成器，旺中受绝，绝中受气，惟相配而取之为不同耳。此金数之所以难同，而又有海中、沙中之异。

- **分字分词释义**：
  - **气性**：气质属性。
  - **材位**：材质地位。
  - **相济**：相互辅助。
  - **相克**：相互克制。
  - **成器**：成为器物。
  - **旺中受绝**：旺盛中受绝。
  - **绝中受气**：绝灭中受气。
  - **相配而取**：相互配合而取用。
  - **金数难同**：金的数理难以相同。
  - **海中沙中**：海中金和沙中金。

- **规范化释义（primary_lang_explained）**：
  五行在天下，各有气质属性和材质地位，有的相互辅助，有的相互克制，如果成为器物、木成为器物，在旺盛中受到绝灭，在绝灭中受到生气，只是相互配合取用的方式不同罢了。这就是金的数理难以相同，而又有海中金、沙中金等区别的原因。

- **完整对等诠释（secondary_lang_full）**：
  The Five Elements in the world each possess qi-nature and material-position—some mutually assist, some mutually restrain. When formed into implements or wood into tools, receiving extinction amid flourishing, receiving qi amid extinction—it is only that their mutual pairing and utilization differ. This is why Metal's numbers are difficult to uniformize, and why there are distinctions like Sea-Center Metal and Sand-Center Metal.

- **核心要点**：
  - 五行各有气性和材位
  - 或相济或相克
  - 旺中受绝，绝中受气
  - 相配取用方式不同
  - 金数难同，有海中沙中之异

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_170]` `[trigger: 五行气性材位配合]` `[factor_trigger: five_elements_qixing AND material_position AND mutual_assist_restrain]` `[role: 主干]` 五行之在天下，各有气性，有材位，或相济，或相克。旺中受绝，绝中受气，惟相配而取之为不同耳。此金数之所以难同，而又有海中、沙中之异。 → 《三命通会》卷一#五行气性材位的配合原理

- **详细解说**：
  此条论五行配合的复杂性和纳音金的多样性。五行不是静态单一的，各有独特的"气性"（气质属性）和"材位"（材质地位），在配合时既可能相济（相生）也可能相克。"旺中受绝，绝中受气"是辩证观点：看似旺盛时实际暗含衰绝，看似绝灭时实际孕育生机。因此同样是金纳音，由于干支配合方式不同，产生不同类型的金，如海中金（甲子乙丑，水旺之地的阳金）、沙中金（甲午乙未，火旺之地的阴金）。这体现了纳音体系的精细分类和中国哲学的辩证智慧。

- **校勘与字词辨析（双语）**：
  - **中文**："旺中受绝"指物极必反。"海中金"指甲子乙丑纳音，"沙中金"指甲午乙未纳音。
  - **English**: "Receiving extinction amid flourishing" indicates reversal at extremes; "Sea-Center Metal" refers to Jiazi-Yichou Nayin; "Sand-Center Metal" refers to Jiawu-Yiwei Nayin."""
    normalized_text_zh: str = """"""
    subject: str = "五行气性材位的配合原理"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_五行气性材位的配合原理_001_L1",
    )
    version: str = "1.0.0"
