"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228255
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
    semantic_id="smth_v1.0.0_纳音配五行总论_天成人力与生旺死绝_001",
    book_id="sanming",
    engine_id="bazi"
)
class 纳音配五行总论天成人力与生旺死绝(SemanticEntry):
    """
    - **原文（source_text）**：
  以干支而分配五行，论阴阳而大明终始。天成，人力相芜，生旺死绝并类。呜呼！六十甲子，圣人不过借其象以明其理，而五行性情材质、形色功用，无不曲尽，而造化无...
    """
    
    original_text: str = """- **原文（source_text）**：
  以干支而分配五行，论阴阳而大明终始。天成，人力相芜，生旺死绝并类。呜呼！六十甲子，圣人不过借其象以明其理，而五行性情材质、形色功用，无不曲尽，而造化无余蕴矣。

- **分字分词释义**：
  - **天成人力相芜**：天然形成与人力作用互相交织。
  - **生旺死绝并类**：生旺死绝各种状态同时归类。
  - **借其象以明其理**：借用象征来说明道理。
  - **曲尽**：详尽无遗。
  - **造化无余蕴**：造化之理没有遗漏。

- **规范化释义（primary_lang_explained）**：
  用干支来分配五行，论述阴阳来彻底阐明事物的始终。天然形成与人力作用互相交织，生旺死绝各种状态同时归类。啊！六十甲子，圣人不过是借用其象征来说明道理，而五行的性情材质、形色功用，无不详尽无遗，造化之理没有任何遗漏了。

- **完整对等诠释（secondary_lang_full）**：
  Using Stems-Branches to allocate Five Elements, discussing yin-yang to thoroughly illuminate beginning and end. Heaven's formation and human effort interweave, generation-prosperity-death-extinction all categorized together. Alas! The Sixty Jiazi—sages merely borrowed their symbolism to illuminate principles, and Five Elements' temperament-material-quality, form-color-function, all exhaustively complete, leaving no cosmic mysteries unexplained.

- **核心要点**：
  - 干支分配五行，阴阳明终始
  - 天成与人力相互交织
  - 六十甲子象征五行全理
  - 性情材质形色功用曲尽

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_191]` `[trigger: 纳音配五行总论]` `[factor_trigger: stems_branches_five_elements AND heaven_human_interweave AND nayin_complete_system]` `[role: 主干]` 以干支而分配五行，论阴阳而大明终始。天成，人力相芜，生旺死绝并类。六十甲子，圣人不过借其象以明其理，而五行性情材质、形色功用，无不曲尽，而造化无余蕴矣。 → 《三命通会》卷一#纳音配五行总论

- **详细解说**：
  此条总论纳音五行的配置原理。干支分配五行，通过阴阳学说来阐明事物的开始和结束。天然形成（天成）与人力努力（人力）相互交织，生旺死绝等各种状态都可以归类。圣人创立六十甲子纳音体系，借用这些象征来说明天地造化的道理，五行的性情（内在特质）、材质（物质属性）、形色（外在表现）、功用（实际作用）都详尽无遗，完整揭示了宇宙造化的规律。这是对前面纳音理论的总结，强调纳音体系的完备性和深刻性。

- **校勘与字词辨析（双语）**：
  - **中文**："天成"指自然形成。"人力相芜"指人力与天成交织。"曲尽"指详尽无遗。"造化无余蕴"指造化之理完全阐明，无所遗漏。
  - **English**: "Heaven's formation" means natural formation. "Human effort interweave" means human effort intertwined with nature. "Exhaustively complete" means thoroughly detailed. "No cosmic mysteries unexplained" means all principles of creation fully revealed."""
    normalized_text_zh: str = """"""
    subject: str = "纳音配五行总论：天成人力与生旺死绝"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_纳音配五行总论_天成人力与生旺死绝_001_L1",
    )
    version: str = "1.0.0"
