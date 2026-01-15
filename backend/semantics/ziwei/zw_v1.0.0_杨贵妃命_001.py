"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.700007
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
    semantic_id="zw_v1.0.0_杨贵妃命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 杨贵妃命(SemanticEntry):
    """
    - 分字分词释义：

  - **坐贵向贵**：命局同时坐于贵人星并面向贵人位。
  - **得贵人宠爱**：获得权贵或上位者的宠爱。
  - **文昌文曲加会女命不宜**：文昌文曲同会对女命带来桃花...
    """
    
    original_text: str = """- 分字分词释义：

  - **坐贵向贵**：命局同时坐于贵人星并面向贵人位。
  - **得贵人宠爱**：获得权贵或上位者的宠爱。
  - **文昌文曲加会女命不宜**：文昌文曲同会对女命带来桃花是非。
  - **杨妃好色**：杨贵妃型女命的情欲特征。
  - **羊陀太岁迭并**：擎羊陀罗与太岁同时叠加。
  - **小限子午相冲**：小限处于子午对冲位置，主冲动变故。
  - **阳女土五局**：杨贵妃命盘的五行局数，土五局主厚重悲剧。

- **原文（source_text）**：  
  杨贵妃命。阳女土五局。坐贵向贵，得贵人宠爱。文昌、文曲加会，女命不宜见之。经云：杨妃好色，三合文昌、文曲、太岁、羊陀迭并小限子午相冲，故损寿。

- **规范化释义（primary_lang_explained）**：  
  杨贵妃命为阳女土五局，「坐贵向贵」说明命局同时坐于贵人星并面向贵人位，「得贵人宠爱」。「文昌、文曲加会，女命不宜见之」，对女命而言文昌文曲同会反而不利。「经云：杨妃好色」，点明其情欲特征。「三合文昌、文曲、太岁、羊陀迭并小限子午相冲」，在特定流年小限配合下，最终「故损寿」。

- **完整对等诠释（secondary_lang_full）**：  
  Yang Guifei's chart is that of a Yang Earth female. "Sitting noble, facing noble"—she receives favor from the powerful. Wen Chang and Wen Qu converge, yet for a female this is unfavorable. The classic notes her sensuality. When Flowing Chang‑Qu, Tai Sui, and Yang‑Tuo all pile up, and the minor period clashes along the Zi‑Wu axis, her lifespan is cut short.

- **核心要点**：  
  1. 坐贵向贵得贵人宠爱，但文昌文曲对女命不宜。  
  2. 杨妃好色的情欲特征。  
  3. 羊陀太岁迭并，小限子午相冲，最终损寿。"""
    normalized_text_zh: str = """"""
    subject: str = "杨贵妃命"
    factor_refs: list = ['pattern_zuogui_xianggui', 'quality_de_guiren_chongai', 'malefic_changqu_nvming_buyi', 'quality_yangfei_haose', 'malefic_yangtuo_taisui_diebing', 'timing_xiaoxian_ziwu_chong']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_杨贵妃命_001_L1",
    )
    version: str = "1.0.0"
