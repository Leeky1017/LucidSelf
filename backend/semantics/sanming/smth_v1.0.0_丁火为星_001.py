"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042582
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
    semantic_id="smth_v1.0.0_丁火为星_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丁火为星(SemanticEntry):
    """
    - **原文（source_text）**：
  丁火为星。丙火死而丁火遂从生焉，在天之日薄而星回也。类如此：星象惟入夜故灿烂，阴火惟近晦故辉煌，丁不谓之星而何？凡丁日生人，喜遇夜，喜遇秋，如星光之得...
    """
    
    original_text: str = """- **原文（source_text）**：
  丁火为星。丙火死而丁火遂从生焉，在天之日薄而星回也。类如此：星象惟入夜故灿烂，阴火惟近晦故辉煌，丁不谓之星而何？凡丁日生人，喜遇夜，喜遇秋，如星光之得时也；又喜行身弱地，如石里所藏属丁火，石虽在水，即时取击，亦自有火；其丁巳一日，多克父兄妻子，盖财忌比劫，兄屈弟下，巳中有戊土，伤官也。

- **分字分词释义**：
  - **丙死丁生**：阳火退而阴火继之，喻昼尽夜始，日隐星出。
  - **入夜而灿烂**：丁火适宜在暗处显光，如星光、灯烛。
  - **喜遇夜、喜遇秋**：指丁日生于秋令或夜时，更得其「星光」之象。

- **规范化释义（primary_lang_explained）**：
  丁火被比为星光：丙火日落之后，夜空星辰方显，正如阳火息而阴火兴。丁火不宜正午烈照，而宜在暗处、夜里、秋季显其辉煌。丁日命人多适合在相对「光线不足」的场域展现才华，如隐处之火；石中火的比喻，则言丁火常潜藏于质朴环境中，一经触发便可发光。原文略提丁巳日克亲之说，属传统格局层面的具体经验。

- **完整对等诠释（secondary_lang_full）**：
  Ding Fire is likened to starlight and lamplight: it emerges when the great sun of Bing has set, and shines most clearly against a dark background. It is not suited to blasting down at noon, but to glowing in courtyards, rooms, and night skies, especially in the cool clarity of autumn. People born on Ding days often find their gifts recognised not in loud, central positions but in quieter settings where subtle, sustained illumination is needed. The image of fire hidden in stone points to modest, unassuming environments that nonetheless contain a live spark which can be struck into flame when the time comes. Interpreting Ding Fire in this way steers us away from judging it by the standards of grand, all‑encompassing visibility: its value lies in patient craft, small but reliable points of light, and the ability to keep burning where conditions look unpromising, rather than in competing head‑on with the midday sun."""
    normalized_text_zh: str = """"""
    subject: str = "丁火为星"
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
        l1_anchor="smth_v1.0.0_丁火为星_001_L1",
    )
    version: str = "1.0.0"
