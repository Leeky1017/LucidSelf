"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227979
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
    semantic_id="smth_v1.0.0_子丑支义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 子丑支义(SemanticEntry):
    """
    - **原文（source_text）**：
  子者，北方至阴寒水之位，而一阳肇生之始，故阴极则阳生，壬而为胎。子之为子，此十一月之辰也。至丑，阴尚执而纽之。又丑，纽也，助也，谓十二月终始之际，以结...
    """
    
    original_text: str = """- **原文（source_text）**：
  子者，北方至阴寒水之位，而一阳肇生之始，故阴极则阳生，壬而为胎。子之为子，此十一月之辰也。至丑，阴尚执而纽之。又丑，纽也，助也，谓十二月终始之际，以结纽为名焉。

- **分字分词释义**：
  - **至阴寒水之位**：极阴寒冷的水之方位。
  - **一阳肇生**：一阳开始萌生。
  - **阴极则阳生**：阴气到极点则阳气开始生长。
  - **壬而为胎**：对应壬水为胎孕。
  - **十一月之辰**：十一月（冬至月）的时辰。
  - **阴尚执而纽之**：阴气还在控制并纠结。
  - **纽**：纠结、结合。
  - **终始之际**：一年终结与开始的交界。

- **规范化释义（primary_lang_explained）**：
  子是北方极阴寒冷的水之方位，而又是一阳开始萌生的时刻，所以阴气到极点则阳气开始生长，对应壬水为胎孕。子就是子，这是十一月（冬至月）的时辰。到了丑，阴气还在控制并纠结。又说：丑就是"纽"，也是"助"，指十二月是一年终结与开始的交界，以结纽为名。

- **完整对等诠释（secondary_lang_full）**：
  Zi is the position of extreme yin and cold Water in the North, yet it is the beginning of one yang's emergence—thus when yin reaches its extreme, yang begins to generate, corresponding to Ren Water as the womb. Zi as Zi is the eleventh lunar month (Winter Solstice month). By Chou, yin still controls and binds. Also said: Chou means "knotting" and "assisting"—referring to the twelfth month as the juncture between year's end and beginning, named for binding and knotting.

- **核心要点**：
  - 子：北方至阴寒水，一阳肇生，十一月冬至
  - 阴极则阳生，壬而为胎
  - 丑：阴尚执而纽，十二月终始之际
  - 丑为"纽"（结纽）、"助"（辅助）

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_156]` `[trigger: 子丑支义]` `[factor_trigger: zi_branch AND chou_branch AND yinyang_transition]` `[role: 主干]` 子者，北方至阴寒水之位，而一阳肇生之始，故阴极则阳生。丑，纽也，助也，谓十二月终始之际。 → 《三命通会》卷一#子丑支义

- **详细解说**：
  此条详解子丑二支之义。子为十二支之首，位北方水位，是极阴寒冷之地，但也是冬至一阳初生的时刻，体现"阴极阳生"的转折。子对应十一月（农历），与壬水的胎孕之义相通，都表示新生命的孕育。丑为第二支，阴气仍在控制但开始纠结转化。丑对应十二月（农历），是一年的终结与新年的开始交界处，"纽"指纠结、结合，"助"指辅助过渡，体现从旧年到新年的转换枢纽。子丑二支完成了阴极生阳（子）到阴助阳生（丑）的过程。

- **校勘与字词辨析（双语）**：
  - **中文**："十一月"指冬至所在月（农历）。"肇生"指开始萌生。"纽"有纠结、结合之意。
  - **English**: "Eleventh month" refers to the lunar month containing Winter Solstice; "肇生" means "beginning to emerge"; "纽" (niu) means "knotting" or "binding.""""
    normalized_text_zh: str = """"""
    subject: str = "子丑支义"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_子丑支义_001_L1",
    )
    version: str = "1.0.0"
