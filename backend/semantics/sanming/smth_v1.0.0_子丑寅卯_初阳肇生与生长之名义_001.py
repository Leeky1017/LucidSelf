"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227596
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
    semantic_id="smth_v1.0.0_子丑寅卯_初阳肇生与生长之名义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 子丑寅卯初阳肇生与生长之名义(SemanticEntry):
    """
    - **原文（source_text）**：
  子者，北方至阴寒水之位，而一阳肇生之始，此十一月之辰也。至丑，阴尚执而纽之，又丑，阴也，助也，谓十二月终始之际，以结纽为名焉。寅，正月也，阳已在上，阴...
    """
    
    original_text: str = """- **原文（source_text）**：
  子者，北方至阴寒水之位，而一阳肇生之始，此十一月之辰也。至丑，阴尚执而纽之，又丑，阴也，助也，谓十二月终始之际，以结纽为名焉。寅，正月也，阳已在上，阴已在下，又寅，演也，津也。卯，日升之时也，又卯，茂也，言二月阳气盛而孳茂。

- 分字分词释义：
  - **子：至阴中一阳肇生**：在最寒之处，一阳初动，故为始胎之位；
  - **丑：结纽、助阴**：承接终始、系结前后，起承转合之处；
  - **寅：演、津**：演进、津梁之义，为万物开端之门；
  - **卯：茂**：日出东方，万物孳茂生长。

- **规范化释义（primary_lang_explained）**：
  子月是冬至之后，一阳在至阴之中偷偷发动；丑月像把一年首尾打结的纽带，仍以阴气为主，却在为新一轮作准备。到寅月，阳气上升、阴气下降，万物开始从冬藏中被「演」出来；卯则如朝日升起、草木繁茂，是春生之气正式铺开之处。

- **完整对等诠释（secondary_lang_full）**：

  Zi marks the point just after the winter solstice when, in the depths of extreme Yin and cold, the first spark of Yang quietly stirs: it is the womb‑like stage of hidden gestation. Chou is like the knot that ties the end of one year to the beginning of the next—still Yin‑dominated, but already binding together what has finished and what is about to start. By Yin month, Yang has risen above and Yin has sunk below; the gate opens, and things begin to emerge from winter storage. Mao corresponds to sunrise and luxuriant vegetation, when spring Qi is fully unfurled and visible growth begins in earnest. In reading charts, these four branches together describe the shift from deep accumulation and preparation (Zi, Chou) to overt launching and early expansion (Yin, Mao), rather than merely indicating zodiac animals."""
    normalized_text_zh: str = """"""
    subject: str = "子丑寅卯：初阳肇生与生长之名义"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_子丑寅卯_初阳肇生与生长之名义_001_L1",
    )
    version: str = "1.0.0"
