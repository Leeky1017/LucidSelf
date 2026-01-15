"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228553
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
    semantic_id="smth_v1.0.0_癸巳涸流水_自绝之水须金生_001",
    book_id="sanming",
    engine_id="bazi"
)
class 癸巳涸流水自绝之水须金生(SemanticEntry):
    """
    - **原文（source_text）**：
  癸巳为自绝之水，名曰涸流，若丙戌、丁亥、庚子壮厚之土，其涸可待。若得三合生旺之金生之，则源泉混混，盈科而进也。五行要论云：癸巳、乙卯自绝自死之水，乃至...
    """
    
    original_text: str = """- **原文（source_text）**：
  癸巳为自绝之水，名曰涸流，若丙戌、丁亥、庚子壮厚之土，其涸可待。若得三合生旺之金生之，则源泉混混，盈科而进也。五行要论云：癸巳、乙卯自绝自死之水，乃至阴退藏，真精啬养，凝成贵气，贵局乘之，是妙道君子，夙体常德，有功及物。

- **分字分词释义**：
  - **自绝之水**：自己绝灭的水。
  - **涸流**：干涸的流水。
  - **壮厚之土**：强壮深厚的土。
  - **其涸可待**：其干涸可以预期。
  - **三合生旺之金**：三合局生旺的金。
  - **源泉混混**：源泉涌流不绝。
  - **盈科而进**：充满洼地而前进。
  - **至阴退藏**：极阴收藏退隐。
  - **真精啬养**：真精收敛养护。
  - **凝成贵气**：凝聚成贵气。
  - **夙体常德**：素来具备恒常之德。

- **规范化释义（primary_lang_explained）**：
  癸巳是自绝的水，名叫涸流。如果遇到丙戌、丁亥、庚子等强壮深厚的土，其干涸可以预期。如果得到三合局生旺的金来生，则源泉涌流不绝，充满洼地而前进。五行要论说：癸巳、乙卯是自绝自死的水，乃是极阴收藏退隐，真精收敛养护，凝聚成贵气。如果贵格乘之，是妙道君子，素来具备恒常之德，有功于物。

- **完整对等诠释（secondary_lang_full）**：
  Guisi is self-extinct water, named dried-flow. If encountering Bingxu, Dinghai, Gengzi robust-thick earth, its drying predictable. If obtaining Three-Harmony born-prosperous Metal generating it, then source-spring flowing continuously, filling hollows advancing. Five Elements Essential Discourse says: Guisi and Yimao self-extinct self-dead water, being ultimate-yin withdrawing-storing, true-essence conserving-nurturing, condensing into noble-energy. Noble pattern riding it, is subtle-way gentleman, inherently embodies constant-virtue, meritorious benefiting things.

- **核心要点**：
  - 癸巳为长流水，自绝之水
  - 名曰涸流，易干涸
  - 遇壮厚土则涸
  - 得三合金生则源泉不绝
  - 至阴退藏、凝成贵气

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_228]` `[trigger: 癸巳水性质]` `[factor_trigger: guisi_self_extinct_water AND dried_flow AND three_harmony_metal_generate]` `[role: 主干]` 癸巳为自绝之水，名曰涸流，若丙戌、丁亥、庚子壮厚之土，其涸可待。若得三合生旺之金生之，则源泉混混，盈科而进也。五行要论云：癸巳、乙卯自绝自死之水，乃至阴退藏，真精啡养，凝成贵气，贵局乘之，是妙道君子，夙体常德，有功及物。 → 《三命通会》卷一#癸巳水性质

- **详细解说**：
  此条详论癸巳（长流水）的特殊性质。癸巳是自绝的水（巳为水绝地），名为涸流，容易干涸。如果遇到强厚的土（丙戌屋上土、丁亥屋上土、庚子壁上土），其干涸可期。但如果得三合局生旺的金来生（金生水），则源泉涌流，盈科而进。五行要论强调癸巳、乙卯自绝自死之水，是至阴退藏、真精啬养，凝成贵气，入贵格为妙道君子。这是论述绝地水的转化与格局。

- **校勘与字词辨析（双语）**：
  - **中文**："涸流"指干涸的流水。"盈科而进"典出《孟子》，指水充满洼地后再前进。"至阴退藏"指极阴状态的收藏。"啬养"指收敛养护。
  - **English**: "Dried-flow" means dried flowing water. "Filling hollows advancing" from Mencius, means water fills depressions before advancing. "Ultimate-yin withdrawing-storing" means extreme yin state storing. "Conserving-nurturing" means restraining and nurturing."""
    normalized_text_zh: str = """"""
    subject: str = "癸巳涸流水：自绝之水须金生"
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
        l1_anchor="smth_v1.0.0_癸巳涸流水_自绝之水须金生_001_L1",
    )
    version: str = "1.0.0"
