"""
Auto-generated semantic module for book_of_thoth
Generated at: 2025-12-05T13:30:20.027462
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
    semantic_id="bot_v1.0.0_prince_of_cups__圣杯王子_001",
    book_id="book_of_thoth",
    engine_id="tarot"
)
class PrinceOfCups圣杯王子(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Air of Water | Volatile flow | Steam/catalyst |
| Eagle Chariot | Soaring vehicle | Airy motion over water |
| Serpent from Cup | Scorpio symbol | Hidden transformation |
| Strategic Passion | Calculated intensity | Ruthless manipulator |

**Title**: Prince of the Chariot of the Waters (水之战车的王子)
**Elemental**: The Airy part of Water (水中之气)
**Zodiac**: 21° Libra to 20° Scorpio (天秤座21度至天蝎座20度)

**Source Text**:
> "The Prince of Cups represents the airy part of Water. On the one hand, elasticity, volatility, hydrostatic equilibrium; on the other hand, the catalytic faculty and the energy of steam. He rules the Heavens from the 21st degree of Libra to the 20th degree of Scorpio... He is a warrior partly clad in armour... his helmet is surmounted by an eagle, and his chariot, which resembles a shell, is also drawn by an eagle... In his right hand he bears a Lotus flower... in his left hand is a cup from which issues a serpent... The moral characteristics... subtlety, secret violence, and craft... calm and imperturbable on the surface... accepts [influences] only to transmute them to the advantage of his secret designs... perfectly ruthless."

**English Paraphrase**:
**Alchemical Manipulator** - Represents the **Airy part of Water**: volatility, elasticity, equilibrium, and catalytic transformation (like steam). He rides a shell-like chariot drawn by an **eagle**, wearing an eagle-crested helmet; in one hand he holds a **lotus**, in the other a cup from which a **serpent** emerges, with the hidden **scorpion** implied. This is the Scorpio current in its intellectual and emotional form. Psychologically, he is subtle, secretive, and intense: outwardly calm, inwardly burning with passion and design. He absorbs influences only to **transmute** them toward his own purposes, often without ordinary conscience.

**Core**: **Strategic Passion** - Emotional intelligence, charisma, occult or psychological manipulation, intense focus, but also ruthlessness and hidden agendas.

**Chinese Explanation**:
**圣杯王子**代表**水中之气**（水的挥发性、弹性与平衡），类似**蒸汽**的动力与催化特性。他乘坐贝壳形战车，由**鹰**牵引，头盔上亦饰以鹰，右手持**莲花**，左手举杯，其中伸出**蛇**，暗含未显之**蝎子**（天蝎三重象征）。这体现了天秤-天蝎过渡地带的情感与智力能量。性格上，他极度**细腻、隐秘、善于谋划**：表面冷静、不动声色，内在却充满强烈的渴望与策略。他吸收外界的一切影响，只为**转化为服务自己隐秘目标的燃料**，很少按常规道德标准行事，容易被他人感觉"难以捉摸、隐隐可怕"。

**In Readings**: Deep emotional intelligence, psychological insight, occult work, negotiation, strategy; or, manipulation, obsession, emotional games, hidden motives.

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Crowley's Prince of Cups is Air of Water - volatility and catalysis like steam. Eagle-drawn chariot soars over emotion. Serpent from cup shows Scorpio transformation. Outwardly calm, inwardly ruthless.
- **中文**: Crowley的圣杯王子是水中之气—像蒸汽般挥发和催化。鹰拉战车凌驾情感之上。杯中之蛇显示天蝎转化。外表冷静，内心无情。

**Narrative Snippets**:
- `[ns_thoth_cups_037]` `[trigger: prince_cups_thoth]` `[factor_trigger: thoth_cups_prince]` `[role: 主干]` Prince of Cups = Air of Water—volatility, elasticity, catalytic faculty like steam; Scorpio intellect. → Core
- `[ns_thoth_cups_038]` `[trigger: eagle_chariot]` `[factor_trigger: thoth_cups_prince AND symbol_eagle]` `[role: 条件分支]` Eagle-drawn shell chariot—lotus in one hand, serpent-cup in other; hidden scorpion implied. → Visual
- `[ns_thoth_cups_039]` `[trigger: ruthless_transmutation]` `[factor_trigger: thoth_cups_prince AND state_strategy]` `[role: 条件分支]` Calm surface, inwardly burning—accepts influences only to transmute for secret designs; ruthless. → Character"""
    normalized_text_zh: str = """"""
    subject: str = "Prince of Cups (圣杯王子)"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'source_ref', 'rel_prince_cups_air', 'air_of_water', 'rel_prince_cups_secret', 'subtle_power', 'prince_cups_catalyst']
    
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
        book_id="book_of_thoth",
        chapter="",
        l1_anchor="bot_v1.0.0_prince_of_cups__圣杯王子_001_L1",
    )
    version: str = "1.0.0"
