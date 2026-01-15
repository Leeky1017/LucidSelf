"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997420
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
    semantic_id="dts_v1.0.0_假化之人亦可贵_孤儿异姓能出类_001",
    book_id="dts",
    engine_id="bazi"
)
class 假化之人亦可贵孤儿异姓能出类(SemanticEntry):
    """
    - **原文（source_text）**：
  假化之人亦可贵，孤儿异姓能出类。

- 原注（原文注解）：
  　　日主孤弱，而遇合神，不能不化，但有暗扶日主，如合神虚弱，则化不真，至岁运扶起合神，...
    """
    
    original_text: str = """- **原文（source_text）**：
  假化之人亦可贵，孤儿异姓能出类。

- 原注（原文注解）：
  　　日主孤弱，而遇合神，不能不化，但有暗扶日主，如合神虚弱，则化不真，至岁运扶起合神，制伏忌神，虽为假化，亦可取用，异姓孤儿，亦能出类，但其人多执滞偏拗，作事迍邅，骨肉刑克耳。

- 分字分词释义：
  - 假化：形式上有合局，但合神不强，且日主仍有扶助之根。
  - 合神：与日主相合之神，为化的媒介。
  - 孤儿异姓：象征隔阂、离族而自成一格之人。

- **次语种完整诠释（secondary_lang_full）**:  
  False-Transform假化 staged-transformation: 合神虚弱 merge-god-weak+日主暗扶 body-has-support causing化不真 incomplete-transformation—假化亦可贵 pseudo-hua-can-prosper via运扶合神制忌 transit-strengthens-merge-restrains-ji as阶段性可用 staged-utility; 孤儿异姓 orphan-outsider象征离本环境 leaving-origin achieving出类 distinction with执滞偏拗 obstinacy+骨肉刑克 family-conflict requiring待运助 awaiting-favorable-transit."""
    normalized_text_zh: str = """假化之局，日主孤弱而遇合神，看似要化；但合神本身虚弱，或日主仍有暗扶根气，使化不真。此时要等岁运再扶起合神、并制伏忌神，化象才可运用，虽为假化，仍能出贵，往往表现为“离本族而投他门”，如异姓收养、离乡出走等；但性情多执滞偏拗，与骨肉间多刑克不和。"""
    subject: str = "假化之人亦可贵，孤儿异姓能出类。"
    factor_refs: list = ['jiahua', 'yikegui', 'guer_yixing', 'zhizhi_pianniu', 'gurou_xingke', 'daiyunzhu']
    
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
        l1_anchor="dts_v1.0.0_假化之人亦可贵_孤儿异姓能出类_001_L1",
    )
    version: str = "1.0.0"
