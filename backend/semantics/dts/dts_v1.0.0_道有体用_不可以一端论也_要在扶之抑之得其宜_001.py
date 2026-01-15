"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997465
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
    semantic_id="dts_v1.0.0_道有体用_不可以一端论也_要在扶之抑之得其宜_001",
    book_id="dts",
    engine_id="bazi"
)
class 道有体用不可以一端论也要在扶之抑之得其宜(SemanticEntry):
    """
    - **原文（source_text）**：
  道有体用，不可以一端论也，要在扶之抑之得其宜。

- 原注（原文注解）：
  　　有以日主为体，提纲之食神财官，皆为我用。日主弱，则提纲有物帮身，以制...
    """
    
    original_text: str = """- **原文（source_text）**：
  道有体用，不可以一端论也，要在扶之抑之得其宜。

- 原注（原文注解）：
  　　有以日主为体，提纲之食神财官，皆为我用。日主弱，则提纲有物帮身，以制其强神者，亦皆为我用。
  　　有以提纲为体，喜神为用者，日主不能用乎提纲矣。提纲财官食神太旺，则取年月时上印比生助为喜神而用之。提纲印比太旺，则取年月时上食伤财官为喜神而用之，此二者，乃体用之正法也。
  　　有以四柱为体，暗神为用者，必四柱俱无可用，方取暗冲暗合之神。
  　　有以四柱为体，化神为用者，四柱有合神，无用神，即以四柱为体，而以化合之神为用。
  　　有以化神为体四柱为用者，盖化之真者，化神即为体，取四柱中与化神相生相克者为用。
  　　有以四柱为体岁运为用者，四柱中太过不及，用岁运琢削滋助有之。
  　　有以喜神为体辅喜之神为用者，盖所喜之神，不能自用，则以为体，而用辅喜之神。
  　　有以格象为体日主为用者，格局气象，及暗神化神忌神克神，皆成一个体段，郤是一面气象，与日主无干，或伤克日主太过，或帮扶日主寸过，中间要辨体月，又无形迹，只得用日主自引生喜之神，别求一个活路，有用过于体者，如用食神，而财官尽行隐伏，则太发露浮散，有体用角立者，体用皆旺，不分胜负，行运又无轻重上下，则角立之，有体用俱滞者，如木火俱旺，不遇金土，则俱滞之，不可一端定也，然体用之用，与用神之用，有分别，若以体用之用为用神，固不可，舍此别求用神亦不可，只要斟酌体用真确，而取其最要紧者为用神，即二三用神亦得，须抑扬其轻重，母使有馀不足可也。

- 分字分词释义：
  - 道：命理之道、规律法则。
  - 体：本体、主体（如日主、提纲、四柱等）。
  - 用：功用、作用（如用神、喜神、化神等）。
  - 一端：单一角度、片面。
  - 扶：扶助弱者。
  - 抑：抑制强者。
  - 得其宜：恰到好处、适宜得当。

- **规范化释义（primary_lang_explained）**：
  体与用需因局而定：或以日主为体、以提纲为体、以四柱为体、以化神为体、以喜神为体、乃至以格象为体……其关键在"扶抑得宜"。不可执一端，必须辨体定用，并随势抑扬，使之不偏不枯。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 体用 | Body and Function (Ti-Yong) | 核心与功用 | Core entity and its application | ti_yong | new_candidate |
| 以日主为体 | Day Master as Body | 传统扶抑法 | Traditional support/restrain method | ri_zhu | existing |
| 以提纲为体 | Month Commander as Body | 格局法核心 | Core of pattern method | yueling_key_god | existing |
| 以化神为体 | Transformation Spirit as Body | 化格取用法 | Method for transformation patterns | huashen_weiti | new_candidate |
| 扶之抑之 | Support or Restrain | 扶抑手段 | Methods of balancing | fuyi_shouduan | new_candidate |
| 得其宜 | Appropriate | 恰当得体 | Fitting and proper | de_qi_yi | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Ti-Yong (Body-Function) theory: Ti is the core, Yong is the tool. Ti can be 日主 Day-Master, 提纲 Month-Commander, 四柱 Four-Pillars, 化神 Transformation-Spirit, 喜神 Favored-Spirit, or 格象 Pattern-Image. Once Ti is defined, Yong is chosen to 扶 support or 抑 restrain it appropriately (得其宜). Cannot stick to one perspective; must adapt to the structure."""
    normalized_text_zh: str = """"""
    subject: str = "道有体用，不可以一端论也，要在扶之抑之得其宜。"
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
        l1_anchor="dts_v1.0.0_道有体用_不可以一端论也_要在扶之抑之得其宜_001_L1",
    )
    version: str = "1.0.0"
