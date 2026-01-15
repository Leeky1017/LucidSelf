"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997438
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
    semantic_id="dts_v1.0.0_何谓战_001",
    book_id="dts",
    engine_id="bazi"
)
class 何谓战(SemanticEntry):
    """
    - **原文（source_text）**：
  何谓战。

- **核心要点**：
  - 运与岁相克为“战”，关键在“谁降谁让”；
  - 以喜忌为根，配合势与根判“孰降”；
  - 借泄、克、通...
    """
    
    original_text: str = """- **原文（source_text）**：
  何谓战。

- **核心要点**：
  - 运与岁相克为“战”，关键在“谁降谁让”；
  - 以喜忌为根，配合势与根判“孰降”；
  - 借泄、克、通关三法，使喜神一方得胜。

- 详细解说：
  本条专门解释“战”的定义：当大运与太岁形成明显克战时，要先分清哪一方代表喜用、哪一方代表忌神，再结合根气深浅与得令与否，判断谁有资格“降”。有力一方若是喜神，则通过戊己壬等泄克或通关，使忌神一方退让，则战而有功；若有力一方反为忌神，则战多成祸。

- 校勘与字词辨析：
  - “战”：此处专指运岁之间的克战格局，不泛指一切六冲。

- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 战 | War (Zhan) | 岁运冲克 | Conflict between Sui and Yun | zhan_suiyun | new_candidate |
| 运伐岁 | Yun Attacks Sui | 大运克太岁 | Decade luck controls annual year | yun_fa_sui | new_candidate |
| 岁伐运 | Sui Attacks Yun | 太岁克大运 | Annual year controls decade luck | sui_fa_yun | new_candidate |
| 孰降 | Who Yields | 强迫弱者服从 | Stronger side forces weaker to yield | shu_jiang | new_candidate |
| 通关 | Mediation (Tong Guan) | 泄克使之和 | Mediation via draining or controlling | tongguan_status | existing |
| 势大 | Great Power | 坐旺得令 | Sitting on prosperity and season | shi_da | new_candidate |

- 原注（原文注解）：
  　　如丙运庚年，谓之运伐（克）岁。  
  　　日主喜庚，要丙降，在得戊（泄）得壬（克）者吉。（以克泄忌神之物为吉）  
  　　如日主喜丙，岁不肯降，得戊己和之为妙。（太岁为专神，故以和解为上）  
  　　如庚坐寅年，则丙之力量大，岁自不得不降。（势大则太岁无权）可保无祸。  
  　　如庚运丙年，谓之岁伐（克）运，日主喜庚，得戊己以和丙者吉（通关）。  
  　　如日主喜丙，运不肯降，岁又不可制，（运管十年，与命较亲）。  
  　　得戊己泄而助庚亦吉，若庚坐寅午，则丙之力量，大运自不得不降，亦保无患。

- **规范化释义（primary_lang_explained）**：
  运与岁相克为“战”。关键在“谁降”。喜庚时，要令丙降（以戊泄丙、以壬克丙）；喜丙时，要岁或运降（以戊己通关）。势在谁方、根在何处，决定“降者”。运掌十年，往往较亲于命，岁力不及则须通关使降。


- **次语种完整诠释（secondary_lang_full）**:  
  Zhan (War) refers to Yun-Sui conflict运岁相克: 运伐岁 Yun-attacks-Sui or 岁伐运 Sui-attacks-Yun; outcome hinges on 孰降 who-yields determined by 势与根 power-and-root. If Yun attacks Sui but Sui is strong, Sui resists; if Sui attacks Yun but Yun is dominant, Yun resists. 喜庚 prefer-Geng requires 丙降 Bing-yields via 戊泄 Wu-drains or 壬克 Ren-controls; 喜丙 prefer-Bing requires 岁运降 yield via 戊己通关 Wu-Ji-mediates. Victory belongs to the side with 党援 support and 干头 heaven-stem-backing, ensuring 吉auspice via correct mediation."""
    normalized_text_zh: str = """"""
    subject: str = "何谓战"
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
        l1_anchor="dts_v1.0.0_何谓战_001_L1",
    )
    version: str = "1.0.0"
