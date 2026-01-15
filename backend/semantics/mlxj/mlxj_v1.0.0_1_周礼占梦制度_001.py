"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.845069
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
    semantic_id="mlxj_v1.0.0_1_周礼占梦制度_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1周礼占梦制度(SemanticEntry):
    """
    #### 原文（source_text）

周礼春官占梦云：季冬聘王梦，献吉梦于王，王拜而受之，乃舍萌于四方，以赠恶梦，遂令始难作傩，敺疫。

聘，问也。梦者，事之祥，吉凶之占，在日月星辰。季冬日穷于...
    """
    
    original_text: str = """#### 原文（source_text）

周礼春官占梦云：季冬聘王梦，献吉梦于王，王拜而受之，乃舍萌于四方，以赠恶梦，遂令始难作傩，敺疫。

聘，问也。梦者，事之祥，吉凶之占，在日月星辰。季冬日穷于次，星回于天，数将几终，于是发币而聘问乎梦焉，若休庆之云尔。献吉梦于王，以归美于王也，王拜受之，敬天命也。

萌，兆也。赠，送也。其梦恶者，则取莱之始萌而祭之，乃遣恶梦使去也。一云：谓梦不吉，则求其所以不吉之萌兆于四方而舍去之，以赠送其恶梦，使不复效也。始傩，所以迎和气；敺疫，所以送戻气。

#### 规范化释义（primary_lang_explained）

《周礼·春官》占梦篇记载：每年季冬（十二月），占梦官要问询王的梦境。将吉梦献给王，王行拜礼接受，表示敬天命。然后在四方举行「舍萌」仪式，以送走恶梦；最后举行傩仪驱疫。

所谓「聘」是问询之意。梦是事情的征兆，吉凶的占验，与日月星辰相关。季冬时节，太阳行至周天之末，星辰回归本位，年数将尽，于是发礼币问询梦境。献吉梦于王，是将美好归于王；王拜而受之，是敬天命。

「萌」是征兆，「赠」是送走。恶梦者，取初萌之草祭祀，送走恶梦使其离去。另一说法：梦不吉则在四方寻找不吉的萌兆而舍弃之，以送走恶梦使其不再应验。傩仪迎接和气，驱疫送走戾气。

#### 完整对等诠释（secondary_lang_full）

The "Rites of Zhou" chapter on Dream Interpretation records: In the twelfth month (late winter), the Dream Interpreter inquires about the King's dreams. Auspicious dreams are presented to the King, who bows to receive them, showing respect for Heaven's mandate. Then the "Releasing Sprouts" ceremony is performed in all four directions to dismiss bad dreams, followed by the exorcism ritual to drive away pestilence.

"Inquiry" means to ask formally. Dreams are omens of events, divinations of fortune and misfortune, connected to the sun, moon, and stars. In late winter, when the sun completes its cycle and stars return to their positions, the year nears its end—thus ceremonial gifts are sent to inquire about dreams. Presenting auspicious dreams to the King attributes good fortune to him; the King's bowing reception shows respect for Heaven's mandate.

"Sprouts" refers to omens; "dismissal" means sending away. For bad dreams, one offers sacrifice using newly-sprouted plants to send away the bad dreams. Another interpretation: when dreams are inauspicious, one seeks the inauspicious omens in all four directions and releases them, dismissing the bad dreams so they no longer manifest.

#### 核心要点

- **制度来源**：《周礼·春官》占梦官职
- **时间**：季冬（十二月）
- **程序**：聘问王梦 → 献吉梦 → 王拜受 → 舍萌赠恶梦 → 始傩驱疫
- **原理**：献吉归美于王，赠恶使不复效
- **仪式**：舍萌祭草、傩仪迎和气送戾气

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v27_001]` `[trigger: 舍萌赠梦]` `[factor_trigger: dream_ritual AND dream_mengrang AND dream_fufa AND dream_zhoufa AND dream_qinshifa AND zhouli_zhanmeng AND dream_system]` `[role: 制度]` 季冬聘王梦，献吉梦于王，王拜而受之，乃舍萌于四方，以赠恶梦。周礼占梦制度。 → 《梦林玄解·卷二十七》#舍萌赠梦说
- `[ns_mlxj_v27_002]` `[trigger: 梦禳方法]` `[factor_trigger: rangmeng AND meng_yi AND dream_huofu AND xiude AND hucan]` `[role: 禳法]` 禳梦之法，梦意祸福，修德悔惭。 → 《梦林玄解·卷二十七》#梦禳
- `[ns_mlxj_v27_003]` `[trigger: 吉神凶煞]` `[factor_trigger: jishen_xiongsha]` `[role: 术数]` 吉神凶煞之应验。 → 《梦林玄解·卷二十七》#吉凶神煞"""
    normalized_text_zh: str = """"""
    subject: str = "1 周礼占梦制度"
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_1_周礼占梦制度_001_L1",
    )
    version: str = "1.0.0"
