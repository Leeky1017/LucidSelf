"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699652
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
    semantic_id="zw_v1.0.0_皇雨安命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 皇雨安命(SemanticEntry):
    """
    - 分字分词释义：

  - **左右同宫**：左辅、右彼同宫，主贵人扶持与内部助力强。
  - **日月夹垣**：太阳太阴夹拱命垣，主光明与阴柔双济。
  - **羊人限行酉地**：属羊之人限行酉位...
    """
    
    original_text: str = """- 分字分词释义：

  - **左右同宫**：左辅、右彼同宫，主贵人扶持与内部助力强。
  - **日月夹垣**：太阳太阴夹拱命垣，主光明与阴柔双济。
  - **羊人限行酉地**：属羊之人限行酉位，形成支冲之象。
  - **地劫相凑**：地劫与其他凶曜同聚，主破耗与意外损失。
  - **陀罗天使夹地**：陀罗与天使在地支形成夹困之象，主制度与凶星双重压力。
  - **病符流羊**：病符星与流年羊刃同临，主病伤与血光之患。
  - **阴男木三局**：皇雨安命盘的五行局数，木三局主生发清贵。

- **原文（source_text）**：  
  皇雨安命。阴男木三局。左右同宫，日月夹垣，其贵格是乎。柰羊人限行酉地，地劫相凑，大限陀罗、天使夹地，且命垣有病符流羊，故主中道而亡，死于四十五岁而巳。

- **规范化释义（primary_lang_explained）**：  
  皇雨安命为阴男木三局，左右同宫、日月夹垣，是典型的高贵官格：左右辅弼与日月同来拱照命垣，一生多主地位显赫、声名清贵。  
  然而对属羊（未）之人而言，行运至酉地，地支成刑冲之象，再加地劫相凑，大限逢陀罗与天使夹地，命垣又带病符与流羊诸凶曜，是「酉地刑冲 + 地劫 + 陀罗天使夹地 + 病符流羊」的高度危险结构。结果是在四十五岁中年阶段中道而亡，寿数明显短于本可承载的格局。此命例呈现「贵格之身却折于中年重凶运」的反差。

- **完整对等诠释（secondary_lang_full）**：  
  Huang Yu’an’s chart is that of a Yin Wood native in the Third Configuration. With Left and Right Assistants in the same palace and the Sun and Moon flanking the court, the pattern is one of high nobility and honour, promising a distinguished status and refined reputation.  
  For a Goat native, however, when time cycles move to You, clashes arise in the earthly branches. Di Jie gathers, the major period encounters Tuo Luo and a "Heavenly Office" clamping the earth, and the Life sector itself carries Bing Fu and flowing Yang. This combination—clashing You, Di Jie, Tuo Luo plus official pressure and illness/Blade indicators—constitutes a highly dangerous configuration. The result is a midlife death around forty‑five, well before the full potential lifespan suggested by the noble pattern. The case contrasts an elevated chart with a sharply curtailed life due to dense malefic transits.

- **核心要点**：  
  1. 左右同宫、日月夹垣，为典型高贵官格，一生多主清显与荣宠。  
  2. 羊人限行酉地，配合地劫、陀罗天使夹地与病符流羊，使中年运势极为险恶。  
  3. 命例呈现「贵格不免中道而亡」的命局张力。

- **叙事素材（narrative_snippets）**：  
  - **左右日月贵格**："左右同宫，日月夹垣，其贵格是乎"，皇雨安命主以左右同宫、日月夹垣成高贵官格，一生清显。  
  - **羊人酉地之忌**："柰羊人限行酉地，地劫相凑"，属羊之人在限行酉地、又见地劫时，原有贵格被结构性冲击。  
  - **夹地病符流羊**："大限陀罗、天使夹地，且命垣有病符流羊，故主中道而亡"，陀罗天使夹地配病符流羊，意味着在中年被制度与身体双重拖垮。  
  - **现代应用**：对中年仍在高位、又背负大量制度责任的人而言，若命局已有贵格再逢「支冲 + 病符 + 羊刃」叠加年份，应主动减负、远离权力中心锋线，把注意力从「继续上升」转为「守成与保命」。"""
    normalized_text_zh: str = """"""
    subject: str = "皇雨安命"
    factor_refs: list = ['pattern_zuoyou_tonggong', 'pattern_riyue_jiayuan', 'condition_yangren_youdi', 'malefic_dijie_xiangcou', 'malefic_tuoluo_tianshi', 'malefic_bingfu_liuyang']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_皇雨安命_001_L1",
    )
    version: str = "1.0.0"
