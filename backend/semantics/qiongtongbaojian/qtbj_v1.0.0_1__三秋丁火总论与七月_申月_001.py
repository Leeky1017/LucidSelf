"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596909
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
    semantic_id="qtbj_v1.0.0_1__三秋丁火总论与七月_申月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三秋丁火总论与七月申月(SemanticEntry):
    """
    - **原文（source_text）**：
  三秋丁火，退气柔弱，耑用甲木，金虽乘旺司权，无伤丁之理，仍取庚噼甲，为引火之物，或借丙暖金晒木，不虑丙夺丁火。凡两丙夹丁者，夏月忌之，余月不忌。但此格...
    """
    
    original_text: str = """- **原文（source_text）**：
  三秋丁火，退气柔弱，耑用甲木，金虽乘旺司权，无伤丁之理，仍取庚噼甲，为引火之物，或借丙暖金晒木，不虑丙夺丁火。凡两丙夹丁者，夏月忌之，余月不忌。但此格少年困苦刑克，中年富贵，必要地支见水制丙、方妙。
  三秋甲庚丙并用，仍分优劣，何也？七月甲丙，申中有庚，八月甲丙庚皆用，七八月或无甲木，乙亦可用，为枯草引灯，却不离丙晒也。九月耑用甲庚。
  大扺甲不离庚，乙不离丙，其理极明。或见甲庚丙皆透，必主科甲。无甲用乙者，富贵皆小，且富而不贵者多。
  或一重壬水，又多见癸水，必以戊土为制，自然富贵光辉。
  或一派庚金，名财多身弱，主富屋贫人，妻多主事。或壬多泄庚，丁壬化杀，反成富贵。若庚多无壬，奔流下贱。

  七月丁火，退气柔弱，端用甲木，金虽乘旺司权，无伤丁之理，仍取庚劈甲，为引火之物，或借丙暖金晒甲，不虑丙夺丁光，凡两丙夹丁者，夏月忌之，余月不忌，但此格少年困苦刑克中年富贵，必要地支见水制丙，方妙。

- **分字分词释义**：
  - **退气柔弱**：气势退缩柔弱 / 秋丁 / 衰象
  - **金虽乘旺司权**：金虽然乘旺掌权 / 秋金当令 / 财旺
  - **暖金晒木**：温暖金气晒干木气 / 丙火功用 / 解湿
  - **两丙夹丁**：两个丙火夹着丁火 / 劫帮身 / 秋喜
  - **枯草引灯**：枯草引燃灯火 / 乙木功用 / 次佳
  - **甲不离庚**：甲木不离开庚金 / 劈甲 / 核心
  - **乙不离丙**：乙木不离开丙火 / 晒木 / 核心
  - **富屋贫人**：富有的房屋贫穷的人 / 财多身弱 / 凶象
  - **妻多主事**：妻子多主持事务 / 财旺夺权 / 凶象
  - **奔流下贱**：四处奔波地位低下 / 庚多无壬 / 极凶

- **规范化释义（primary_lang_explained）**：
  秋季三个月的丁火，气势退缩柔弱，专用甲木（印），金虽然乘旺掌权，但没有伤害丁火的道理（金不能克火，只能耗火），仍然取庚金劈甲，作为引火的工具。或者借丙火暖金晒木（甲木秋湿），不用担心丙火夺丁火的光（秋火已弱，喜比劫帮身）。
  凡是两丙夹丁的格局，夏月忌讳（火太旺），其余月不忌讳。但这种格局（两丙夹丁）少年困苦刑克，中年富贵，必须地支见水制丙才妙。
  三秋甲木、庚金、丙火并用，仍分优劣。七月（申月）用甲丙，申中自带庚金。八月（酉月）甲丙庚都用。七八月如果无甲木，乙木也可以用（枯草引灯），但离不开丙火暴晒（乙湿）。九月（戌月）专用甲庚。
  大抵甲不离庚（劈甲），乙不离丙（晒乙），这个道理极明。如果甲庚丙都透出，必主科甲。无甲用乙的人，富贵都小，而且富而不贵者多。
  如果一重壬水，又多见癸水（官杀混杂），必须用戊土制约（去杀留官/制杀），自然富贵光辉。
  如果一派庚金，叫“财多身弱”，主富屋贫人，妻子多主事（妻夺夫权）。如果壬水多泄庚金之气，丁壬化杀（化木），反成富贵。如果庚多无壬，奔流下贱。

- **完整对等诠释（secondary_lang_full）**：
  Ding Fire in the Three Autumn Months: Qi retreats and is weak; exclusively use Jia Wood. Although Metal is prosperous and commanding, it cannot injure Ding. Still take Geng to split Jia as the igniter. Or borrow Bing to warm Metal and dry Wood; do not worry about Bing stealing Ding's light. Generally, "Two Bings flanking Ding" is dreaded in Summer, but not in other months. However, this pattern implies suffering and punishment in youth, and wealth/nobility in middle age; it is best if branches see Water to control Bing.
  Using Jia/Geng/Bing in Autumn still has distinctions. In the 7th Month, use Jia/Bing (Shen contains Geng). In the 8th Month, use Jia/Bing/Geng. In the 7th/8th Months, if Jia is absent, Yi is usable ("Withered Grass Igniting Lamp"), but cannot do without Bing to dry it. In the 9th Month, exclusively use Jia/Geng.
  Generally, Jia does not leave Geng; Yi does not leave Bing. If Jia/Geng/Bing are all revealed, Civil Service is certain. Using Yi without Jia implies small wealth/nobility, mostly rich but not noble.
  If one Ren and many Gui appear, must use Wu to control; naturally wealthy and glorious.
  If a mass of Geng Metal appears, it is "Abundant Wealth Weak Body"; Rich House Poor Man, wife rules the house. If Ren is abundant to leak Geng, Ding-Ren transform into Killing (Wood), conversely becoming wealthy and noble. If Geng is abundant without Ren, one wanders and is lowly.

- **核心要点**：
  - **首要用神**：甲木（引火）。秋丁气弱，非甲不生。
  - **配合**：庚（劈甲）、丙（晒木/帮身）。
  - **乙木之用**：枯草引灯，必须见丙晒干。
  - **财多身弱**：庚多无印比，富屋贫人。
  - **化杀**：丁壬化木，秋月虽不当令，但若金水旺极，从势或化气可成。

- **详细解说**：
  - 申月丁火，正财当令。
  - “甲不离庚，乙不离丙”是丁火的要诀。甲大需劈，乙湿需晒。
  - "两丙夹丁"：秋丁弱，喜比劫，故不忌丙夺光，反助火势。但火多克金（财），故少年（运未至水地）刑克，中年（运至水地制劫护财）富贵。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_282]` `[trigger: 秋丁火]` `[factor_trigger: season_autumn AND tiangan_ding AND tiangan_jia AND tiangan_geng AND autumn_ding_retreat]` `[role: 主干]` 三秋丁火，退气柔弱，耑用甲木，金虽乘旺司权，无伤丁之理，仍取庚噼甲，为引火之物。 → 《穷通宝鉴·三秋丁火》#18.1
  - `[ns_qttbj_283]` `[trigger: 甲不离庚]` `[factor_trigger: tiangan_jia AND tiangan_geng AND jia_needs_geng]` `[role: 主干依赖]` 甲不离庚，乙不离丙，其理极明。 → 《穷通宝鉴·三秋丁火》#18.1
  - `[ns_qttbj_284]` `[trigger: 财多身弱]` `[factor_trigger: season_autumn AND tiangan_ding AND geng_multiple AND NOT tiangan_jia AND wealth_heavy_body_weak]` `[role: 例外处理]` 一派庚金，名财多身弱，主富屋贫人，妻多主事。 → 《穷通宝鉴·三秋丁火》#18.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三秋丁火总论与七月（申月）"
    factor_refs: list = ['withered_grass_lamp', 'wife_rules', 'rich_house_poor']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_1__三秋丁火总论与七月_申月_001_L1",
    )
    version: str = "1.0.0"
