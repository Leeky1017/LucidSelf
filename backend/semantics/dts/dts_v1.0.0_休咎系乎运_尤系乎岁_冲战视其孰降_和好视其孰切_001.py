"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997430
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
    semantic_id="dts_v1.0.0_休咎系乎运_尤系乎岁_冲战视其孰降_和好视其孰切_001",
    book_id="dts",
    engine_id="bazi"
)
class 休咎系乎运尤系乎岁冲战视其孰降和好视其孰切(SemanticEntry):
    """
    - **原文（source_text）**：
  休咎系乎运，尤系乎岁，冲战视其孰降，和好视其孰切。

- 原注（原文注解）：
  　　日主譬如吾身，局中之神譬如舟马引从，大运譬如所历之地，故重地支，...
    """
    
    original_text: str = """- **原文（source_text）**：
  休咎系乎运，尤系乎岁，冲战视其孰降，和好视其孰切。

- 原注（原文注解）：
  　　日主譬如吾身，局中之神譬如舟马引从，大运譬如所历之地，故重地支，未尝无天干，太岁譬如所遇之人，故重天干，未尝无地支。必先明一日主，配合七字，推其轻重，看其行何运，如甲日以气机看春，以人心看仁，以物理看木，大率看气机而物在其中，遇庚辛申酉字，即看其和何令，又看春之喜忌，乃行运生甲伐甲之地，故详论岁运战冲和好之势，而得胜负适从之机，则休咎了然在目。

- 分字分词释义：
  - 运：大运，十年之程，侧重地支（但不无天干）。
  - 岁：太岁，一年之气，侧重天干（但不无地支）。
  - 冲战：冲克相战，须判“孰降”（谁让步）。
  - 和好：和合相好，须判“孰切”（谁更贴切/力量更实）。

- **规范化释义（primary_lang_explained）**：
  祸福之判断，运为大势，岁为当年之键。遇冲战，要看谁降；逢和好，要看谁更贴切有效。先定日主与七字之轻重，再观行何运与遇何岁，胜负去就自然分明。

- **次语种完整诠释（secondary_lang_full）**:  
  Fortune-Year运岁 dual-timing: 休咎系乎运 decade-background尤系乎岁 year-trigger—大运 da-yun as地气 earth-momentum十年背景; 太岁 sui-year as天气 sky-events年度触发; 冲战视孰降 clash-who-yields和好视孰切 harmony-who-closer requiring辨轻重 weight-assessment+看胜负 victory-defeat enabling祸福了然 clear-fortune-judgment via运岁交互 yun-sui-interaction."""
    normalized_text_zh: str = """"""
    subject: str = "休咎系乎运，尤系乎岁，冲战视其孰降，和好视其孰切。"
    factor_refs: list = ['yun', 'sui', 'chongzhan', 'hehao', 'shujiang', 'shuqie']
    
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
        l1_anchor="dts_v1.0.0_休咎系乎运_尤系乎岁_冲战视其孰降_和好视其孰切_001_L1",
    )
    version: str = "1.0.0"
