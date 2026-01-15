"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997412
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
    semantic_id="dts_v1.0.0_真从之像有几人_假从亦可发其身_001",
    book_id="dts",
    engine_id="bazi"
)
class 真从之像有几人假从亦可发其身(SemanticEntry):
    """
    - **原文（source_text）**：
  真从之像有几人，假从亦可发其身。

- 原注（原文注解）：
  　　日主弱矣，财官强矣，不能不从，中有所助者，便假，至于行运，财官得地，虽是假从，亦可...
    """
    
    original_text: str = """- **原文（source_text）**：
  真从之像有几人，假从亦可发其身。

- 原注（原文注解）：
  　　日主弱矣，财官强矣，不能不从，中有所助者，便假，至于行运，财官得地，虽是假从，亦可富贵，但其人不能免祸，或心术不端耳。

- 分字分词释义：
  - 假从：形式上似从，实则日主仍有根有助，“中有所助”而不真。
  - 真从之像：结构近似真从，但条件不齐全。
  - 发其身：在顺运中仍可发达其人。

- **规范化释义（primary_lang_explained）**：
  假从是“不得不从”而又“从得不彻底”：日主虽弱，财官等一方甚强，却仍有比印、中气暗助，不符合真从“三绝”的条件，只能称“假从”。这类命局逢财官得地之运，仍可因“顺强者之势”而富贵，但因本体与从神夹缠，内里多矛盾，故易有是非、祸患，或性情偏狡、心术不端之类。

- **次语种完整诠释（secondary_lang_full）**:  
  False-Follow假从 semi-dependent structure: 身弱body-weak财官强 one-side-strong yet中有所助 still-has-support creating半从半自立 half-following—假从亦可发 pseudo-cong-can-prosper via顺势运 following-strong-side-transit but伴祸患 with-misfortune+心术偏 moral-ambiguity; 介于真从与身弱 between-true-cong-and-weak requiring辨中有所助 identifying-remaining-support not轻言真从 over-claiming-true-cong."""
    normalized_text_zh: str = """"""
    subject: str = "真从之像有几人，假从亦可发其身。"
    factor_refs: list = ['zhencong_zhixiang', 'jiacong', 'zhong_yousuozhu', 'fa_qishen', 'xinshu_buduan', 'huohuan']
    
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
        l1_anchor="dts_v1.0.0_真从之像有几人_假从亦可发其身_001_L1",
    )
    version: str = "1.0.0"
