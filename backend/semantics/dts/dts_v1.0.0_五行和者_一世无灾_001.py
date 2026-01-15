"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997700
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
    semantic_id="dts_v1.0.0_五行和者_一世无灾_001",
    book_id="dts",
    engine_id="bazi"
)
class 五行和者一世无灾(SemanticEntry):
    """
    - **原文（source_text）**：
  五行和者，一世无灾。

- 原注（原文注解）：
 　　和者不特全不缺、生不克，贵在"各得其所"。

- 分字分词释义：
  - 五行：金木水火土五种基...
    """
    
    original_text: str = """- **原文（source_text）**：
  五行和者，一世无灾。

- 原注（原文注解）：
 　　和者不特全不缺、生不克，贵在"各得其所"。

- 分字分词释义：
  - 五行：金木水火土五种基本元素。
  - 和：和谐、协调、各得其所。
  - 一世：一生、终生。
  - 无灾：无大灾大病。

- 规范化释义（primary_lang_explained）：
  所谓"五行和"，不仅是五行俱全、不偏不缺，更在于各行各安其位——生克有序、寒热得中、燥湿适度。此等格局，气机平稳，体质多健，一生少大灾重病。

- **核心要点**：
  - “和”重在“各得其所”，非单纯数量均衡；
  - 生克有节、寒热中和、燥湿得宜；
  - 以整体和局为病灾轻重的总纲。

- 详细解说：
  “全不缺、生不克”只是基础条件，更高一层是“各得其所”：如木得春生、火居夏旺、金水相涵、土居中宫，各安其职，不相侵凌。这样的命局，即便偶有小病小灾，多属调候之需，不易发展为致命重疾。命理上以“五行和”作健康评估的第一道门槛，是在提醒我们先看整体配伍，再谈局部偏胜。

- 校勘与字词辨析：
  - “和者不特全不缺、生不克”：指出“和”超越“全与生”，强调结构位置与配伍。

- **次语种完整诠释（secondary_lang_full）**：  
  "Five Elements in Harmony" means more than all five being present. Each element must sit in its proper place, neither excessive nor deficient, so that production and control, warmth and coolness, dryness and moisture all stay in balance. When this background qi is even and well seated, the native tends to enjoy a lifetime without major calamity, with illnesses remaining minor and recoverable."""
    normalized_text_zh: str = """"""
    subject: str = "五行和者，一世无灾。"
    factor_refs: list = ['wuxinghe', 'gedeqisuo', 'qiji_pingwen', 'tiaohou', 'dazai_zhongbing']
    
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
        l1_anchor="dts_v1.0.0_五行和者_一世无灾_001_L1",
    )
    version: str = "1.0.0"
