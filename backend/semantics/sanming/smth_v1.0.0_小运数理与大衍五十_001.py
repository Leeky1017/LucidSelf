"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264324
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
    semantic_id="smth_v1.0.0_小运数理与大衍五十_001",
    book_id="sanming",
    engine_id="bazi"
)
class 小运数理与大衍五十(SemanticEntry):
    """
    - **原文（source_text）**：  
  此其数也。白虎通谓：男三十，筋骨坚强，任为人父；女二十，肌肤充盛，任为人母。合为五十，应大衍之数，以生万物。阳奇而舒，故三终；阴偶而促，故再终。参...
    """
    
    original_text: str = """- **原文（source_text）**：  
  此其数也。白虎通谓：男三十，筋骨坚强，任为人父；女二十，肌肤充盛，任为人母。合为五十，应大衍之数，以生万物。阳奇而舒，故三终；阴偶而促，故再终。参天两地之道，此其理也。

- **规范化释义（primary_lang_explained）**：  
  承接前文小运起点之说，作者以《白虎通》的“男三十、女二十”来说明阴阳成熟期的差异：男子至三十岁筋骨方坚，可任人父；女子至二十岁肌肤丰腴，可任人母。二者相加为五十，对应《易》中“大衍之数五十”，象征阴阳交泰、生生不息的根本数理。又曰“阳奇而舒，故三终；阴偶而促，故再终”，即阳道绵长、以三为节奏推演，阴道相对紧促、以二为节奏收束，将这种节律映射到小运体系中，便构成前文所谓“男左行三十，女右行二十”的数目依据。如此一来，小运不只是技术层面的算法，而是被嵌入了“参天两地”的宇宙秩序之中。

- **完整对等诠释（secondary_lang_full）**：  
  Here the author anchors the minor‑luck scheme in classical numerology. Citing the Baihu Tong, he notes that a man reaches full physical strength at thirty, capable of becoming a father, while a woman reaches mature fullness at twenty, capable of becoming a mother. Together they make fifty, corresponding to the "Great Expansion" number in the Yijing, from which the myriad beings arise. The statement "Yang, being odd, extends and relaxes, thus it ends in three cycles; Yin, being even, is compact, thus it ends in two" describes the different pacing of yang and yin processes. These cycles are then mapped onto the earlier construction of "male path thirty steps, female path twenty steps" in minor luck. In this way, xiao yun is not just a counting trick but an expression of the same Daoist‑cosmological logic that "joins Heaven above and Earth below".

- **核心要点**：
  - 男三十、女二十之说，用以比附阴阳成熟节奏与小运步数。
  - 五十为大衍之数，象征阴阳合德以生万物。
  - 小运数理被纳入“参天两地”的宇宙秩序，而非孤立算法。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_081]` `[trigger: 男三十女二十]` `[factor_trigger: nan_sanshi AND nu_ershi]` `[role: 主干]` 男三十，筋骨坚强，任为人父；女二十，肌肤充盛，任为人母。 → 《三命通会》卷十#小运数理与大衍五十
  - `[ns_smth_10_082]` `[trigger: 大衍之数]` `[factor_trigger: dayan_zhishu AND sheng_wanwu]` `[role: 主干依赖]` 合为五十，应大衍之数，以生万物。 → 《三命通会》卷十#小运数理与大衍五十
  - `[ns_smth_10_083]` `[trigger: 阳奇而舒]` `[factor_trigger: yangqi_ershu AND yinou_ercu]` `[role: 条件分支]` 阳奇而舒，故三终；阴偶而促，故再终。 → 《三命通会》卷十#小运数理与大衍五十
  - `[ns_smth_10_084]` `[trigger: 此其理也]` `[factor_trigger: ciqi_liye AND cantian_liangdi_zhi_dao]` `[role: 总结]` 参天两地之道，此其理也。 → 《三命通会》卷十#小运数理与大衍五十

- **详细解说**：  
  从工程视角看，这一段实际上是为“小运参数”提供一套语义解释：男三十、女二十可以理解为“阳向外展开的时间跨度较长，阴向内收成的节奏较快”，进而把这种差异编码进小运起步的步数安排之中，用来表达性别角色在传统社会中的分工与期望。若将来在系统中尝试其他行年算法，也可以把“是否仍保留大衍五十的结构”作为一个评估维度，判断新算法与传统数理之间的偏离程度。

- **校勘与字词辨析（双语）**：
  - **中文**：“大衍之数五十”出自《系辞传》，传统多以五十象征天地生成之数，此处借来支撑小运之数理框架，并非在讨论具体筮法操作。
  - **English**: The "Great Expansion number fifty" refers to a cosmological constant in the Yijing, not a literal count of stalks in divination practice here. The text appropriates it to legitimize the structure of minor‑luck counting."""
    normalized_text_zh: str = """"""
    subject: str = "小运数理与大衍五十"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_小运数理与大衍五十_001_L1",
    )
    version: str = "1.0.0"
