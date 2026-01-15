"""
Auto-generated semantic module for tetrabiblos
Generated at: 2025-12-05T13:30:20.182663
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
    semantic_id="tb_v1.0.0_houses_of_the_planets__chapter_001",
    book_id="tetrabiblos",
    engine_id="astro"
)
class HousesOfThePlanetsChapter(SemanticEntry):
    """
    **Source Text** (Lines 2373-2432):
> Those stars which are denominated planetary orbs have particula...
    """
    
    original_text: str = """**Source Text** (Lines 2373-2432):
> Those stars which are denominated planetary orbs have particular familiarity with certain places in the zodiac, by means of parts designated as their houses... Cancer and Leo are the most northerly of all the twelve signs; they approach nearer than the other signs to the zenith of this part of the earth, and thereby cause warmth and heat: they are consequently appropriated as houses for the two principal luminaries; Leo for the Sun, and Cancer for the Moon. Saturn occupies the signs opposite to Cancer and Leo: Aquarius and Capricorn... Jupiter occupies Sagittarius and Pisces... Mars takes Aries and Scorpio... Venus takes Taurus and Libra... Mercury takes Gemini and Virgo.

**English Paraphrase (Primary Language)**:
Ptolemy explains the **domicile (house) system**—each planet rules two signs (except luminaries, which rule one each):

- **Sun**: Leo (masculine, most northerly = warmest)
- **Moon**: Cancer (feminine, nearest Sun's house)
- **Saturn**: Capricorn, Aquarius (opposite luminaries = cold/wintry)
- **Jupiter**: Sagittarius, Pisces (trine to luminaries = harmonious)
- **Mars**: Aries, Scorpio (square to luminaries = discordant)
- **Venus**: Taurus, Libra (sextile to luminaries = harmonious)
- **Mercury**: Gemini, Virgo (adjacent to luminaries = nearest)

The logic is elegant: Cancer/Leo are assigned to Moon/Sun because they're the northernmost (warmest) signs. Other planets are distributed by aspect relationship to these houses and by orbital position (Saturn most remote = opposite; Mercury closest = adjacent).

**Complete Chinese Interpretation (Secondary Language)**:
托勒密解释了**庙旺（主宰）系统**——每颗行星主宰两个星座（发光体除外，各主宰一个）：

- **太阳**：狮子座（阳性，最北=最温暖）
- **月亮**：巨蟹座（阴性，最接近太阳的宫位）
- **土星**：摩羯座、水瓶座（与发光体相对=寒冷/冬季）
- **木星**：射手座、双鱼座（与发光体三分=和谐）
- **火星**：白羊座、天蝎座（与发光体四分=不和谐）
- **金星**：金牛座、天秤座（与发光体六分=和谐）
- **水星**：双子座、室女座（与发光体相邻=最近）

逻辑很优雅：巨蟹座/狮子座被分配给月亮/太阳，因为它们是最北（最温暖）的星座。其他行星按与这些宫位的相位关系和轨道位置分布（土星最远=对面；水星最近=相邻）。

**Core Points**:
- Sun rules Leo; Moon rules Cancer (warmest signs)
- Saturn rules Capricorn, Aquarius (opposite luminaries)
- Jupiter rules Sagittarius, Pisces (trine luminaries)
- Mars rules Aries, Scorpio (square luminaries)
- Venus rules Taurus, Libra (sextile luminaries)
- Mercury rules Gemini, Virgo (adjacent luminaries)
- Distribution follows aspect geometry and orbital sequence

**Narrative Snippets**:
- `[ns_tetra_i047]` `[trigger: domicile_system]` `[factor_trigger: planet_domicile AND planet_dignity_multiple]` `[role: 主干]` Planets have particular familiarity with certain signs designated as their houses (domiciles). → Source Text I.20
- `[ns_tetra_i048]` `[trigger: luminary_houses]` `[factor_trigger: sign_commanding AND sign_obeying]` `[role: 主干依赖]` Leo for the Sun and Cancer for the Moon—the most northerly signs causing warmth. → Source Text I.20
- `[ns_tetra_i049]` `[trigger: saturn_houses]` `[factor_trigger: planet_exaltation AND terms_egyptian]` `[role: 条件分支]` Saturn occupies Aquarius and Capricorn, opposite the luminaries, cold and wintry. → Source Text I.20

**Textual Criticism**: Footnote notes day/night house distinction (e.g., Saturn's day house = Aquarius, night house = Capricorn)."""
    normalized_text_zh: str = """"""
    subject: str = "Houses of the Planets (Chapter XX)"
    factor_refs: list = ['engine_id', 'planet_domicile', 'astrology_classical', 'source_ref', 'rel_i_018', 'planet_domicile', 'amplifying', 'evi_i_014', 'planet_domicile', 'rule_domicile', 'concept_domicile', 'planet_domicile', 'security']
    
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
        book_id="tetrabiblos",
        chapter="",
        l1_anchor="tb_v1.0.0_houses_of_the_planets__chapter_001_L1",
    )
    version: str = "1.0.0"
