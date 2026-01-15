"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997788
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
    semantic_id="dts_v1.0.0_职掌兵权豸冠客_刃杀神清气势特_001",
    book_id="dts",
    engine_id="bazi"
)
class 职掌兵权豸冠客刃杀神清气势特(SemanticEntry):
    """
    - **原文（source_text）**：
  职掌兵权豸冠客，刃杀神清气势特。

- 原注（原文注解）：
 　　生杀风纪之任，清劲见势，或刃杀两显。

- 分字分词释义：
  - 职掌兵权：掌握军...
    """
    
    original_text: str = """- **原文（source_text）**：
  职掌兵权豸冠客，刃杀神清气势特。

- 原注（原文注解）：
 　　生杀风纪之任，清劲见势，或刃杀两显。

- 分字分词释义：
  - 职掌兵权：掌握军事大权。
  - 豸冠客：御史、监察官（带豸头帽）。
  - 刃杀：羊刃与七杀。
  - 神清：精神清明、理智而不浊乱。
  - 气势特：气势独特、与众不同。

- 规范化释义（primary_lang_explained）：
  此条指掌兵权、执法纪之职：命局中刃杀之神清劲有力，又与官印相配，使人具备刚断果决、能管生杀之势。此类人适合掌军权、司刑法，气势凌厉而不浊乱。

- **核心要点**：
  - 以刃杀为用，须“清而有制”，不可浊乱失控；
  - 适合生杀、风纪、军政等职位；
  - 权力多体现为执行与威慑，而非纯粹文职。

- 详细解说：
  “刃杀神清气势特”并非一味好杀，而是强调刃杀两星在格局中位置得当：或有印化煞、或有官统刃，使其刚而不暴、威而有节。这样的命局，若配合时势，往往出现在军队主官、纪检司法、维稳安全等岗位上。若刃杀虽旺却混浊无制，多为暴戾之气，则已偏离本条所言“清劲见势”的佳象。

- 校勘与字词辨析：
  - “豸冠客”：指执法、司法之官，取其冠饰形状；
  - “刃杀”：泛指七杀、羊刃等带锋锐、执行力之星。

- **次语种完整诠释（secondary_lang_full）**:
  Military-authority职掌兵权 censorate-official豸冠客: blade-killing刃杀 spirit-clear神清 momentum-special气势特—martial武职 or监察 censorate requires刃杀 blade-killing清而特 clear-and-special气势."""
    normalized_text_zh: str = """"""
    subject: str = "职掌兵权豸冠客，刃杀神清气势特。"
    factor_refs: list = ['bingquan', 'zhiguan_hat', 'yangren_qisha', 'shenqing', 'qishite']
    
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
        l1_anchor="dts_v1.0.0_职掌兵权豸冠客_刃杀神清气势特_001_L1",
    )
    version: str = "1.0.0"
