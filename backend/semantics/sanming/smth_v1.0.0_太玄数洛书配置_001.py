"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228110
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
    semantic_id="smth_v1.0.0_太玄数洛书配置_001",
    book_id="sanming",
    engine_id="bazi"
)
class 太玄数洛书配置(SemanticEntry):
    """
    - **原文（source_text）**：
  数止于九，不言十者，十则又起一矣，故凡十数则曰一十。洛书数始于一，终于九，太玄独从四起数，不言一二三者，盖一生二，二生三，三生万物。一为天，二为地，三...
    """
    
    original_text: str = """- **原文（source_text）**：
  数止于九，不言十者，十则又起一矣，故凡十数则曰一十。洛书数始于一，终于九，太玄独从四起数，不言一二三者，盖一生二，二生三，三生万物。一为天，二为地，三为人，有天地而后有万物，故曰三元。且天干十，地支十二，起于九，终于四，天干地支已尽，自无一二三。太玄起数，皆理之自然如此，不可不知。

- **分字分词释义**：
  - **数止于九**：数字止于九。
  - **不言十**：不说十。
  - **十则又起一**：十就又从一开始。
  - **洛书数始于一终于九**：洛书从一到九。
  - **太玄独从四起数**：太玄从四开始数。
  - **一生二二生三三生万物**：老子生成论。
  - **三元**：天地人三元。
  - **理之自然**：道理的自然规律。

- **规范化释义（primary_lang_explained）**：
  数字止于九，不说十，因为十就又从一开始，所以凡是十数就说一十。洛书的数从一开始到九结束，太玄独特地从四开始数，不说一二三，因为一生二，二生三，三生万物。一是天，二是地，三是人，有了天地然后才有万物，所以叫三元。而且天干十个，地支十二个，起于九，终于四，天干地支已经用尽，自然没有一二三。太玄起数，都是道理的自然规律这样，不可不知。

- **完整对等诠释（secondary_lang_full）**：
  Numbers stop at nine, not mentioning ten, because ten would begin again from one—thus any ten is called "one-ten." Luoshu numbers begin at one and end at nine. Taixuan uniquely starts counting from four, not mentioning one-two-three, because one generates two, two generates three, three generates myriad things. One is Heaven, two is Earth, three is Humanity—only after Heaven-Earth exist do myriad things arise, thus called Three Origins. Moreover, ten Heavenly Stems and twelve Earthly Branches, beginning at nine and ending at four, exhaust the Stems-Branches, naturally leaving no one-two-three. Taixuan's number initiation follows natural principles thus—this must be understood.

- **核心要点**：
  - 数止于九，十又起一
  - 洛书数：一至九
  - 太玄数：从四起（不言一二三）
  - 一二三为天地人三元
  - 干支起九终四，已尽一二三

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_173]` `[trigger: 太玄数洛书配置]` `[factor_trigger: taixuan_luoshu AND three_origins AND numbers_nine_four]` `[role: 主干]` 数止于九，不言十者，十则又起一矣。洛书数始于一，终于九，太玄独从四起数，不言一二三者，盖一生二，二生三，三生万物。 → 《三命通会》卷一#太玄数洛书配置

- **详细解说**：
  此条说明太玄数与洛书数的关系和特殊性。洛书数从1到9循环，不说10（因为10=1+0又回到1）。太玄数特殊之处在于从4开始数，不包含1、2、3。为什么？因为1、2、3代表天地人"三元"——老子说"一生二，二生三，三生万物"，1是天，2是地，3是人，有了天地人三才之后才有万物。在太玄数推算中，天干地支的数配从9开始（甲己子午为9），到4结束（巳亥为4），正好用完天干十个、地支十二个的所有配置，自然不包含1、2、3。这是"理之自然"，体现了中国数术的精妙设计——三元作为基础不参与推算，从四开始才是具体应用。

- **校勘与字词辨析（双语）**：
  - **中文**：洛书九宫数。太玄数从四起是因为一二三为三元基础。天干起于九（甲己）终于五（戊癸），地支起于九（子午）终于四（巳亥）。
  - **English**: Luoshu nine-palace numbers; Taixuan starts from four because one-two-three form Three Origins foundation; Stems begin at nine (Jia-Ji) end at five (Wu-Gui); Branches begin at nine (Zi-Wu) end at four (Si-Hai)."""
    normalized_text_zh: str = """"""
    subject: str = "太玄数洛书配置"
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
        l1_anchor="smth_v1.0.0_太玄数洛书配置_001_L1",
    )
    version: str = "1.0.0"
