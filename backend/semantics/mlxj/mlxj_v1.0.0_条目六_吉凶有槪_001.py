"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.850588
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
    semantic_id="mlxj_v1.0.0_条目六_吉凶有槪_001",
    book_id="mlxj",
    engine_id="dream"
)
class 条目六吉凶有槪(SemanticEntry):
    """
    ### 原文（source_text）

吉凶有槪，凡梦鲜美开明之象皆吉，污秽倾晦之象皆凶。优俳戏弄之类，虽吉成虚；妖异幻妄之事，虽凶必散。若天清日丽，宫宇庄严，服饰新整等类，吉征也；或天清而忽黯，日...
    """
    
    original_text: str = """### 原文（source_text）

吉凶有槪，凡梦鲜美开明之象皆吉，污秽倾晦之象皆凶。优俳戏弄之类，虽吉成虚；妖异幻妄之事，虽凶必散。若天清日丽，宫宇庄严，服饰新整等类，吉征也；或天清而忽黯，日丽而忽昏，宫宇服饰，初完好而忽颓敝，则吉里藏凶。若涂泞水浊，形体臭秽，草木枯槁等类，凶朕也。或涂泞而忽开，水浊而忽澄，形体草木污朽而忽鲜洁，则凶中带吉。以至吉之为虚，凶之可散，占梦者皆当以类推之，毋庸执泥。

### 规范化释义（primary_lang_explained）

占梦的第六条核心原则是「吉凶有槪」——梦象的吉凶有其基本准则。

凡梦见鲜美、开明的意象都属吉兆；梦见污秽、倾颓、晦暗的意象都属凶兆。但优伶戏弄之类的梦，即使看似吉祥也成空虚；妖异幻妄之事，即使看似凶险也必定消散。

具体来说：梦见天清日丽、宫宇庄严、服饰新整等，是吉征；但若天清忽暗、日丽忽昏、宫宇服饰初完好忽颓敝，则是吉里藏凶。梦见涂泥水浊、形体臭秽、草木枯槁等，是凶朕；但若涂泥忽开、水浊忽澄、污朽忽鲜洁，则是凶中带吉。

至于吉可能成虚、凶可能消散，占梦者都应该以类推之，不可执泥于表面现象。

### 核心要点

- 吉凶有槪是占梦第六核心原则
- 鲜美开明皆吉，污秽倾晦皆凶
- 优俳戏弄虽吉成虚，妖异幻妄虽凶必散
- 吉象忽变暗则吉里藏凶
- 凶象忽转明则凶中带吉
- 需以类推，毋庸执泥

### 叙事素材（narrative_snippets）

- `[ns_mlxj_018]` `[trigger: 吉凶判断]` `[factor_trigger: dream_jixiong AND dream_imagery_quality AND dream_daji AND dream_xiong]` `[role: 基准]` 凡梦鲜美开明之象皆吉，污秽倾晦之象皆凶。 → 《梦林玄解·卷之首》#吉凶有槪
- `[ns_mlxj_019]` `[trigger: 吉凶转化]` `[factor_trigger: dream_jixiong AND dream_imagery_transition]` `[role: 转化规则]` 天清而忽黯，日丽而忽昏，则吉里藏凶。 → 《梦林玄解·卷之首》#吉凶有槪"""
    normalized_text_zh: str = """"""
    subject: str = "条目六：吉凶有槪"
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_条目六_吉凶有槪_001_L1",
    )
    version: str = "1.0.0"
