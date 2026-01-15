"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699974
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
    semantic_id="zw_v1.0.0_小儿夭命_阴男木三局_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 小儿夭命阴男木三局(SemanticEntry):
    """
    - 分字分词释义：

  - **日月反背**：太阳与太阴处于反背之势，光明之气相冲。
  - **太阴守命失陷**：太阴星守命宫却落陷，主星虚弱。
  - **天刑地劫同临**：天刑与地劫两凶同时临...
    """
    
    original_text: str = """- 分字分词释义：

  - **日月反背**：太阳与太阴处于反背之势，光明之气相冲。
  - **太阴守命失陷**：太阴星守命宫却落陷，主星虚弱。
  - **天刑地劫同临**：天刑与地劫两凶同时临命，加剧凶象。
  - **其难养必矣**：婴幼儿期存在严重养育风险。
  - **天使铁蛇关冲**：小儿关煎中的天使、铁蛇关同时冲克。
  - **死于三岁**：三岁时因多重凶象叠加而夭亡。
  - **阴男木三局**：小儿夭命盘的五行局数，木三局主生发受阻。

- **原文（source_text）**：  
  小儿夭命。阴男木三局。此命日月反背，太阴守命，失陷，又临天刑地劫，其难养必矣。况三岁，行童限在亥，夘生人防已亥岁限，又遇天使铁蛇关冲，故死于三岁。

- **规范化释义（primary_lang_explained）**：  
  小儿夭命为阴男木三局，「日月反背，太阴守命，失陷」，说明日月处于反背之势而太阴守命却落陷，形成主星虚弱的格局。再加「又临天刑地劫」，天刑与地劫两凶同临，命局自出生起便带有严重的养育风险，「其难养必矣」。原文点明应期：「况三岁，行童限在亥，夘生人防已亥岁限，又遇天使铁蛇关冲」，三岁时童限行至亥宫，卯年生人在己亥岁又逢天使、铁蛇关等小儿关煞冲克，多重凶象叠加，最终「死于三岁」。

- **完整对等诠释（secondary_lang_full）**：  
  This "Infant Death" chart for a Yin Wood native features the Sun and Moon in opposition ("ri yue fan bei"), with the Moon guarding Life yet fallen. Tian Xing and Di Jie add further affliction, making the child "certain to be hard to raise." At three, the childhood limit enters Hai; for someone born in Mao year, the ji‑hai year‑limit is especially dangerous; and the Heavenly Envoy and Iron Serpent infant gates clash. Under this convergence, the child dies at three.

- **核心要点**：  
  1. 日月反背、太阴守命失陷，主星与光明之气皆虚弱。  
  2. 天刑地劫同临，自出生即难养。  
  3. 三岁童限入亥，逢天使铁蛇关冲，小儿关煞齐发而夭。"""
    normalized_text_zh: str = """"""
    subject: str = "小儿夭命（阴男木三局）"
    factor_refs: list = ['pattern_riyue_fanbei', 'star_taiyin_shixian', 'malefic_tianxing_dijie', 'quality_nanyang_biyi', 'malefic_tianshi_tieshe', 'result_si_yu_sansui']
    
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
        l1_anchor="zw_v1.0.0_小儿夭命_阴男木三局_001_L1",
    )
    version: str = "1.0.0"
