"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042575
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
    semantic_id="smth_v1.0.0_丙为日_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丙为日(SemanticEntry):
    """
    - **原文（source_text）**：
  丙为日。《说卦传》曰：「离为火，为日。」日与火皆文明之象，是以丙火为日之名不易焉。太阳朝出而夕入，阳火寅生而酉死，而又何异乎？凡六丙生冬夏，不如春秋：...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙为日。《说卦传》曰：「离为火，为日。」日与火皆文明之象，是以丙火为日之名不易焉。太阳朝出而夕入，阳火寅生而酉死，而又何异乎？凡六丙生冬夏，不如春秋：春日有暄万物之功，秋阳有燥万物之用；冬则阴晦，夏则炎蒸，宜细推之。

- **分字分词释义**：
  - **丙为日**：以太阳之日喻丙火的光明与文明属性。
  - **寅生酉死**：对应日出东方、日没西方的运转规律。
  - **春暄秋燥**：春日温煦主生发，秋阳燥烈主收成。

- **规范化释义（primary_lang_explained）**：
  丙火喻为太阳之日，《说卦》言离为火为日，皆文明之象。日出东方似丙火生于寅，日落西方如丙火死于酉。六丙日若生于春秋，比冬夏更得其用：春日温暖、助长万物；秋阳燥烈、助成熟收成；冬日阴晦、夏日炎蒸，则多有不及与过之处，需细细斟酌。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire is explicitly identified with the sun: the bright, visible fire that carries light and civilisation. Rising at Yin and setting at You, it traces a daily arc that mirrors its seasonal variations. When a Bing‑day chart is rooted in spring or autumn, the sun’s work is most constructive: in spring it warms and awakens growth; in autumn it dries and ripens what has already been formed. In deep winter the same sun struggles against heavy clouds and cold, while in high summer its blaze can become oppressive and exhausting. The text therefore measures Bing not by sheer intensity but by whether its light falls at the right time and on the right ground. Well‑placed Bing Fire signifies healthy visibility, leadership, and cultural expression; badly placed, it becomes glare and heat without benefit, leaving the person over‑exposed, drained, or performing in ways that do not truly nourish themselves or others."""
    normalized_text_zh: str = """"""
    subject: str = "丙为日"
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_丙为日_001_L1",
    )
    version: str = "1.0.0"
