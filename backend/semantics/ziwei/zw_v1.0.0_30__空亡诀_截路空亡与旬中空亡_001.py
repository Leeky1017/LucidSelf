"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654315
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
    semantic_id="zw_v1.0.0_30__空亡诀_截路空亡与旬中空亡_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 30空亡诀截路空亡与旬中空亡(SemanticEntry):
    """
    - 分字分词释义：

  - **截路空亡**：论生年天干定位空亡宫位，星曜落入失力。
  - **旬中空亡**：论六十甲子旬头定位空亡宫位。
  - **空亡**：星曜落入空亡宫位，难以发挥正常作用...
    """
    
    original_text: str = """- 分字分词释义：

  - **截路空亡**：论生年天干定位空亡宫位，星曜落入失力。
  - **旬中空亡**：论六十甲子旬头定位空亡宫位。
  - **空亡**：星曜落入空亡宫位，难以发挥正常作用。
  - **甲己申酉**：甲年或己年生人，申酉二宫为截路空亡。
  - **旬头**：六十甲子中每十年一旬的起始干支。
  - **双重空亡**：两种空亡体系同时标记同一宫位，空亡加倍。

#### 截路空亡（论本生年天干）：

- 甲己：申酉宫
- 乙庚：午未宫
- 丙辛：辰巳宫
- 丁壬：寅卯宫
- 戊癸：子丑宫

#### 旬中空亡（论本生年支）：

- 甲子旬：戌亥空
- 甲戌旬：申酉空
- 甲申旬：午未空
- 甲午旬：辰巳空
- 甲辰旬：寅卯空
- 甲寅旬：子丑空

#### 完整对等诠释（secondary_lang_full·29-30空亡诀）：

  Two distinct void algorithms operate in Ziwei Doushu. Jielu Kongwang (Intercepted-Road Void) is derived from the day-stem of the birth year: Jia-Ji natives have Shen-You as void palaces; Yi-Geng have Wu-Wei; Bing-Xin have Chen-Si; Ding-Ren have Yin-Mao; Wu-Gui have Zi-Chou. Xunzhong Kongwang (Decadal Void) is derived from the sixty-year cycle position: the Jia-Zi decade leaves Xu-Hai void; Jia-Xu leaves Shen-You void; Jia-Shen leaves Wu-Wei void; and so on through Jia-Yin which leaves Zi-Chou void. When a palace falls into void status by either system, stars placed there are said to lose much of their effective power—wealth stars become unreliable, authority stars lack traction, and even malefics may dissipate before fully manifesting harm. In practice, the two voids are often read together: if both systems mark the same palace as void, the effect is compounded."""
    normalized_text_zh: str = """"""
    subject: str = "30. 空亡诀（截路空亡与旬中空亡）"
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_30__空亡诀_截路空亡与旬中空亡_001_L1",
    )
    version: str = "1.0.0"
