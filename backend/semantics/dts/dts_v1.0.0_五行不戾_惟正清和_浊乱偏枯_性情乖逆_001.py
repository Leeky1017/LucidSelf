"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997694
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
    semantic_id="dts_v1.0.0_五行不戾_惟正清和_浊乱偏枯_性情乖逆_001",
    book_id="dts",
    engine_id="bazi"
)
class 五行不戾惟正清和浊乱偏枯性情乖逆(SemanticEntry):
    """
    - **原文（source_text）**：
  五行不戾，惟正清和，浊乱偏枯，性情乖逆。

- 原注（原文注解）（兼列性情变例）：
  　　火烈而性燥者，遇金水之激，则燥急转患；水奔而性柔者，全金木...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行不戾，惟正清和，浊乱偏枯，性情乖逆。

- 原注（原文注解）（兼列性情变例）：
  　　火烈而性燥者，遇金水之激，则燥急转患；水奔而性柔者，全金木之神；木奔南而软怯；金见水以流通；最拗者，西水还南；至刚者，东火转北；顺生之机，遇击神而抗；逆折之序，见闲神而狂；阳明遇金，郁而多烦；阴浊藏火，包而多滞。又：阳刃局战则逞威，弱则怕事；伤官局清则谦和，浊则刚猛；用神多者性情不常，支格浊者作为多滞……凡此皆性情之异，喜恶之殊，不得以日主论，观其情性可知施为，观其施为可知吉凶。

- **规范化释义（primary_lang_explained）**：
  性情系于五行之“清、和、顺、通”。从“性→行→吉凶”可逆推断，勿拘日主一端。

- 分字分词释义：
  - 不戾：不悖、不逆。
  - 正清和：正气、清明、和缓。
  - 偏枯：偏颇枯槁。

- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 性情 | Temperament (Xing-Qing) | 性格与情操 | Personality and character | xingqing | existing |
| 五行不戾 | Five Elements Not Conflicted | 五行顺遂 | Elements not fighting | wuxing_buli | new_candidate |
| 正清和 | Upright Clear Harmonious | 中正平和 | Balanced and peaceful | zhengqinghe | new_candidate |
| 浊乱偏枯 | Turbid Chaotic Biased Withered | 混乱失衡 | Chaotic and unbalanced | zhuoluan_pianku | new_candidate |
| 乖逆 | Perverse/Rebellious | 乖张悖逆 | Rebellious nature | guaini | new_candidate |
| 施为 | Behavior/Action | 行为举止 | Action and conduct | shiwei | new_candidate |

- **次语种完整诠释（secondary_lang_full）**:  
  Xing-Qing (Temperament) theory: "Five Elements Not Conflicted" (Wu-Xing Bu-Li) leads to Upright, Clear, Harmonious (Zheng-Qing-He). "Turbid, Chaotic, Biased, Withered" (Zhuo-Luan Pian-Ku) leads to Perverse Temperament (Xing-Qing Guai-Ni). Judge by global Qi, not just Daymaster."""
    normalized_text_zh: str = """"""
    subject: str = "五行不戾，惟正清和，浊乱偏枯，性情乖逆。"
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
        l1_anchor="dts_v1.0.0_五行不戾_惟正清和_浊乱偏枯_性情乖逆_001_L1",
    )
    version: str = "1.0.0"
