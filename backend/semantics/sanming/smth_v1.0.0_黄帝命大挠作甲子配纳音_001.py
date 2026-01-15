"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227875
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
    semantic_id="smth_v1.0.0_黄帝命大挠作甲子配纳音_001",
    book_id="sanming",
    engine_id="bazi"
)
class 黄帝命大挠作甲子配纳音(SemanticEntry):
    """
    - **原文（source_text）**：
  逮及黄帝授河图，见日月星辰之象，于是始有星官之书。命大挠探五行之情，占斗纲所建，于是始作甲子，配五行纳音之属。

- **分字分词释义**：
  - ...
    """
    
    original_text: str = """- **原文（source_text）**：
  逮及黄帝授河图，见日月星辰之象，于是始有星官之书。命大挠探五行之情，占斗纲所建，于是始作甲子，配五行纳音之属。

- **分字分词释义**：
  - **授河图**：获得河图。
  - **星官之书**：记载星宿官职的典籍。
  - **大挠**：黄帝臣子，创甲子纳音者。
  - **探五行之情**：探究五行的性情。
  - **占斗纲所建**：观察北斗斗柄所指的方位。
  - **配五行纳音**：将五行与纳音相配。

- **规范化释义（primary_lang_explained）**：
  到了黄帝时代，获得河图，看到日月星辰的象征，于是开始有了星官的典籍。黄帝命令大挠探究五行的性情，观察北斗斗柄所建立的方位，于是开始创作甲子，将五行与纳音相配。

- **完整对等诠释（secondary_lang_full）**：
  By the time of the Yellow Emperor, tradition says he received the River Chart, observed the patterned movements of the sun, moon and stars, and on that basis compiled writings on the constellations and celestial offices. He then ordered Da Nao to investigate the inner qualities of the Five Elements and to track the directions marked out by the handle of the Big Dipper. From this work grew the sixty‑pair stem‑branch cycle, with each pair assigned a specific Five‑Element tone in the system later called Nayin, the “received sounds” of the calendar.

- **核心要点**：
  - 黄帝获河图，创星官之书
  - 命大挠探五行之情，观北斗方位
  - 创作六十甲子配纳音体系
  - 纳音为五行与干支的配合系统

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_142]` `[trigger: 黄帝命大挠作纳音]` `[factor_trigger: yellow_emperor AND da_nao AND nayin]` `[role: 主干]` 逄及黄帝授河图，见日月星辰之象，命大挠探五行之情，占斗纲所建，于是始作甲子，配五行纳音之属。 → 《三命通会》卷一#黄帝命大挠作甲子配纳音

- **详细解说**：
  此条讲述黄帝时代对干支体系的重大完善。黄帝获得河图这一神秘图式，从中看到日月星辰的象征意义，创立星官典籍以记录天文。黄帝命臣子大挠深入探究五行的性情，观察北斗斗柄所指方位（斗建），在此基础上创作六十甲子配纳音体系。纳音是将天干地支的组合赋予五行属性（如甲子乙丑海中金），形成一套复杂的干支五行配属系统，成为命理学的核心工具。这标志着干支从历法工具上升为包含五行、星象、音律的综合体系。

- **校勘与字词辨析（双语）**：
  - **中文**："河图"为传说中伏羲时黄河出现的神秘图案。"斗纲"即北斗七星的斗柄。"纳音"将干支配五行音律。
  - **English**: "Hetu" (River Chart) is a legendary mystical diagram; "Dou Gang" refers to the handle of the Big Dipper; "Nayin" matches stems-branches with Five Elements through tonal qualities."""
    normalized_text_zh: str = """"""
    subject: str = "黄帝命大挠作甲子配纳音"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_黄帝命大挠作甲子配纳音_001_L1",
    )
    version: str = "1.0.0"
