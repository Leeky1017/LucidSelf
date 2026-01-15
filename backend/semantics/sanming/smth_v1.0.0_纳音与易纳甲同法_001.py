"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228052
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
    semantic_id="smth_v1.0.0_纳音与易纳甲同法_001",
    book_id="sanming",
    engine_id="bazi"
)
class 纳音与易纳甲同法(SemanticEntry):
    """
    - **原文（source_text）**：
  纳音与易纳甲同法，乾纳甲，坤纳癸，始于乾而终于坤。纳音始于金，金，乾也，终于土，土，坤也。五行之中惟有金，铸而为器，则音声彰，纳音所以先金。白虎通曰：...
    """
    
    original_text: str = """- **原文（source_text）**：
  纳音与易纳甲同法，乾纳甲，坤纳癸，始于乾而终于坤。纳音始于金，金，乾也，终于土，土，坤也。五行之中惟有金，铸而为器，则音声彰，纳音所以先金。白虎通曰：钟，兑音也。

- **分字分词释义**：
  - **易纳甲**：易卦纳天干的方法。
  - **乾纳甲**：乾卦纳入甲干。
  - **坤纳癸**：坤卦纳入癸干。
  - **始于乾终于坤**：从乾卦开始到坤卦结束。
  - **铸而为器**：铸造成器物。
  - **音声彰**：音声显彰。
  - **白虎通**：汉代经学著作。
  - **兑音**：兑卦之音，属金。

- **规范化释义（primary_lang_explained）**：
  纳音与易卦纳天干的方法相同，乾卦纳入甲干，坤卦纳入癸干，从乾卦开始到坤卦结束。纳音从金开始，金就是乾，结束于土，土就是坤。五行之中只有金，铸造成器物后，音声才显彰，所以纳音以金为先。《白虎通》说：钟是兑卦的音，属金。

- **完整对等诠释（secondary_lang_full）**：
  Nayin follows the same method as Yi hexagram's stem incorporation—Qian incorporates Jia, Kun incorporates Gui, beginning with Qian and ending with Kun. Nayin begins with Metal; Metal is Qian. It ends with Earth; Earth is Kun. Among the Five Elements, only Metal, when cast into instruments, manifests sound clearly—thus Nayin begins with Metal first. The Baihutong states: Bells are Dui's sound, belonging to Metal.

- **核心要点**：
  - 纳音与易纳甲同法
  - 乾纳甲、坤纳癸，始乾终坤
  - 纳音始金终土，对应乾坤
  - 金铸器音声彰，故纳音先金
  - 钟为兑音，属金

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_166]` `[trigger: 纳音与易纳甲同法]` `[factor_trigger: nayin AND yi_najia AND qian_kun AND metal_sound]` `[role: 主干]` 纳音与易纳甲同法，乾纳甲，坤纳癸，始于乾而终于坤。纳音始于金，终于土。五行之中惟有金，铸而为器，则音声彰。 → 《三命通会》卷一#纳音与易纳甲同法

- **详细解说**：
  此条说明纳音与易卦纳甲法的对应关系。易卦纳甲法：八卦各纳天干，乾卦纳甲（甲、壬），坤卦纳癸（癸、乙），体现从纯阳（乾）到纯阴（坤）的过程。纳音也遵循这个原则：从金开始（金对应乾卦、西方、秋季，属阳），到土结束（土对应坤卦、中央，属阴）。为什么纳音以金为先？因为五行中只有金铸成器物（如钟鼎）后，才能发出清晰的音声，最适合用来代表"音"。《白虎通》引证钟为兑卦之音，兑属金，进一步证明金与音的关系。这揭示了纳音体系的易理基础和音律基础的统一。

- **校勘与字词辨析（双语）**：
  - **中文**：易卦纳甲法是将天干配入八卦的方法。《白虎通》为汉代班固等撰。兑卦属金，对应西方。
  - **English**: Yi hexagram stem incorporation assigns Heavenly Stems to Eight Trigrams; "Baihutong" (White Tiger Discussions) was written by Ban Gu and others in Han Dynasty; Dui trigram belongs to Metal, corresponding to West."""
    normalized_text_zh: str = """"""
    subject: str = "纳音与易纳甲同法"
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
        l1_anchor="smth_v1.0.0_纳音与易纳甲同法_001_L1",
    )
    version: str = "1.0.0"
