"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439556
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
    semantic_id="dvd_v1.0.0_adultery_淫乱_外遇_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Adultery淫乱外遇(SemanticEntry):
    """
    ### Source Text

> The sexual act is a very intimate one. In fact in the Word when a couple made lov...
    """
    
    original_text: str = """### Source Text

> The sexual act is a very intimate one. In fact in the Word when a couple made love, they were considered married. It meant that they were one. When you dream of having adultery, you need to ask yourself, "What am I becoming one with right now?"

**General Meaning**: Becoming one with something; intimacy; joining yourself to something new.

**Dreams - Positive**: If you dream that you are embracing an unfamiliar man or woman, but it feels 'right' in the dream, then it could mean that the Lord is leading you to embrace something new in your life.

**Dreams - Negative**: When you wake up feeling unclean and negative from your dream, then it is likely negative. If you continue having this kind of dream, then the Lord is trying to tell you that you are marrying yourself to something that is not of Him.

**Visions - Negative**: If the vision you see is symbolic, then it means that person is joining themselves to something that is not of the Lord. Either they are walking in the flesh or they are embracing the things of the world.

**Scripture**: Proverbs 7:21-22 - "With her much fair speech she caused him to yield; with the flattering of her lips she forced him. He goes after her immediately as an ox goes to the slaughter."

**See also**: Bed, Bedroom

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Adultery | Sexual intimacy outside marriage | Becoming one with something |
| Embrace | Physical/spiritual joining | Union, acceptance |
| One flesh | Biblical marriage concept | Complete union |

### English Paraphrase

Dreaming of adultery symbolizes "becoming one with" something—the question is whether that union is godly or worldly. The sexual act represents complete intimacy and joining. When the dream feels right, it may indicate God leading you to embrace something new (ministry, calling, relationship). When it feels wrong or unclean, it warns you're joining yourself to something not of God—worldliness, flesh, or deception. The key interpretive question: "What am I becoming one with right now?"

### Chinese Interpretation（完整对等诠释）

梦见淫乱/外遇象征「与某事物合一」——关键问题是这种结合是属神还是属世。性行为代表完全的亲密和结合。当梦境感觉正确时，可能表示神在引导你拥抱新事物（事工、呼召、关系）。当感觉错误或不洁时，警告你正在与不属神的事物结合——世俗、肉体或欺骗。核心解释问题：「我现在正与什么合一？」

### Core Points

- 淫乱梦象 = 「合一」的象征，非字面意义
- 正面：拥抱神所引导的新事物
- 负面：与世俗/肉体/不属神的事物结合
- 解释关键：梦中感受（正确 vs 不洁）
- 核心问题：「我正与什么合一？」

### Narrative Snippets

- `[ns_dav_a001]` `[trigger: 梦淫乱]` `[factor_trigger: dream_symbol_adultery AND union_target]` `[role: 主干]` Dreaming of adultery symbolizes becoming one with something—ask "What am I becoming one with right now?" → Dreams Dictionary #Adultery
- `[ns_dav_a002]` `[trigger: 淫乱正面]` `[factor_trigger: dream_symbol_adultery AND dream_feeling]` `[role: 条件分支]` If embracing unfamiliar person feels 'right', Lord may be leading you to embrace something new. → Dreams Dictionary #Adultery
- `[ns_dav_a003]` `[trigger: 淫乱负面]` `[factor_trigger: dream_symbol_adultery AND dream_feeling]` `[role: 条件分支]` Waking unclean/negative = warning you're marrying yourself to something not of God. → Dreams Dictionary #Adultery"""
    normalized_text_zh: str = """"""
    subject: str = "Adultery 淫乱/外遇"
    factor_refs: list = ['dream_symbol_adultery', 'concept_one_flesh', 'action_embrace']
    
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_adultery_淫乱_外遇_001_L1",
    )
    version: str = "1.0.0"
