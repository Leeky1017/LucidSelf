"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042661
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
    semantic_id="smth_v1.0.0_酉为寺钟_001",
    book_id="sanming",
    engine_id="bazi"
)
class 酉为寺钟(SemanticEntry):
    """
    - **原文（source_text）**：
  酉为寺钟。酉属金，位近戍亥，戍亥者，天门也。钟，金属也，寺钟敲则响彻天门；又酉居正西，寺则西方佛界也。酉见寅吉，谓之钟鸣谷应。

- **分字分词释义...
    """
    
    original_text: str = """- **原文（source_text）**：
  酉为寺钟。酉属金，位近戍亥，戍亥者，天门也。钟，金属也，寺钟敲则响彻天门；又酉居正西，寺则西方佛界也。酉见寅吉，谓之钟鸣谷应。

- **分字分词释义**：
  - **寺钟**：寺院之钟，象征肃穆、召集与觉悟。
  - **近天门**：酉近戌亥天门，钟声上达天听之象。
  - **钟鸣谷应**：钟声一击，山谷和鸣，比喻呼应与传播力。

- **规范化释义（primary_lang_explained）**：
  酉属金，位近戌亥天门，如寺钟悬于山门，一击则声彻天际。酉居正西，又有西方佛国之象，故称「寺钟」。酉若见寅，如钟声入山谷，回响不绝，象征号召力与影响力远播。地理上，酉多关联宗教场所、司法机构、钟楼等肃静而有号召力的空间。

- **完整对等诠释（secondary_lang_full）**：
  You Metal is compared to the temple bell hung near heaven’s gate. Situated close to Xu and Hai—the gate of heaven—it is like a bell whose single strike resounds up to the sky. Occupying the western position, it also carries the image of the Western Pure Land, so You becomes the bell of a sacred or solemn institution. When You meets Yin, the text calls this “the bell ringing and the valley answering”: sound enters the mountains and is answered from all sides, symbolising broadcast and response. In charts, strong You indicates roles or environments where official announcements, verdicts, calls to assembly or ritual signals matter more than constant chatter: courts, temples, public institutions, broadcasting platforms. The key is not how often one speaks, but whether each strike is clear, legitimate and able to elicit the right kind of echo."""
    normalized_text_zh: str = """"""
    subject: str = "酉为寺钟"
    factor_refs: list = ['source_ref', 'rel_smth_ysz_001', 'you', 'rel_smth_ysz_002', 'you_yin', 'rel_smth_ysz_003', 'youxiang', 'evi_smth_ysz_001', 'you_sizhong', 'rule_ysz', 'concept_signal_broadcast']
    
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
        l1_anchor="smth_v1.0.0_酉为寺钟_001_L1",
    )
    version: str = "1.0.0"
