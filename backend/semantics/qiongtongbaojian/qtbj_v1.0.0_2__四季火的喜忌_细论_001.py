"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596642
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
    semantic_id="qtbj_v1.0.0_2__四季火的喜忌_细论_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2四季火的喜忌细论(SemanticEntry):
    """
    - **原文（source_text）**：
  生于春月，母旺子相，势力并行，喜木生扶，不宜过旺，旺则火炎。欲水既济，不愁兴盛，盛则沾恩。土多则蹇塞埋光。火盛则伤多烈燥。见金可以施功，纵重见用才尤遂...
    """
    
    original_text: str = """- **原文（source_text）**：
  生于春月，母旺子相，势力并行，喜木生扶，不宜过旺，旺则火炎。欲水既济，不愁兴盛，盛则沾恩。土多则蹇塞埋光。火盛则伤多烈燥。见金可以施功，纵重见用才尤遂。
  
  夏月之火，秉令乘权。逢水制则免自焚之咎，见木助必招夭折之患，遇金必作良工，得土遂成稼穑。金土虽为美利，无水则金燥土焦，再加木助，太过倾危。
  
  秋月之火，性息体和，得木生则有复明之庆。遇水克难免陨灭之灾。土重而掩息其光。金多而损伤其势。火见火以光辉，纵叠见而必利。
  
  冬月之火，体绝形亡，喜木生而有救，遇水克以为殃。欲土制为荣，爱火比为利。见金为难任财，无金而不遭害，天地虽倾，火水难成。

- **分字分词释义**：
  - **母旺子相**：母亲（木）旺盛儿子（火）相助 / 春火 / 印旺身强
  - **势力并行**：势力一同运行 / 木火齐旺 / 吉象
  - **盛则沾恩**：兴盛则沾得恩泽 / 火旺得水 / 既济
  - **秉令乘权**：掌握时令拥有权柄 / 夏火 / 当令
  - **自焚之咎**：自己焚烧的罪过 / 无水之火 / 凶象
  - **夭折之患**：早死的祸患 / 夏火见木 / 太过
  - **良工**：优秀的工匠 / 火炼金 / 吉象
  - **稼穑**：播种收获 / 火生土 / 土之功
  - **性息体和**：性情平息本体温和 / 秋火 / 退气
  - **复明之庆**：恢复光明的喜庆 / 火得木生 / 吉象
  - **体绝形亡**：本体绝灭形态消亡 / 冬火 / 极衰

- **规范化释义（primary_lang_explained）**：
  火生于春月（寅卯辰），母（木）旺子（火）相，势力并行。喜欢木来生扶，但不宜过旺，过旺则火势太炎。希望能有水来既济，就不愁火势兴盛，火盛遇到水反而能沾恩（成贵气）。土多则困顿埋没光辉。火太盛则伤身且烈燥。见到金可以施展功用（克金成器），即使重重见到金财，也特别顺遂。
  
  夏天的火（巳午未），当令掌权。遇到水制约就能免除自焚的灾咎，见到木来助燃必招致夭折的祸患（火太旺），遇到金必定能做良工（火炼金），得到土就成就稼穑（火生土，土生金，或从儿）。金土虽然是美好的利益，但如果没有水，则金燥土焦，如果再加上木助火，就太过了，会导致倾覆危险。
  
  秋天的火（申酉戌），性情停息，本体温和。得到木生助就有恢复光明的喜庆。遇到水克制难免有陨灭的灾难（火弱怕水）。土重会掩息它的光芒（晦火）。金多会损伤它的气势（身弱财多）。火见到火（比劫）能增加光辉，即使重叠见到也必定有利。
  
  冬天的火（亥子丑），本体绝灭，形态消亡。喜欢木来生助就有救（印生身），遇到水克制就是灾殃（杀重身轻）。希望有土制水（食伤制杀）为荣耀，喜爱火比肩帮身为有利。见到金难以任财（身弱财党杀），没有金就不遭害。天地虽然倾覆（水旺），若无木土，火水难以达成既济。

- **完整对等诠释（secondary_lang_full）**：
  Fire born in Spring Months: The Mother (Wood) is Prosperous and the Child (Fire) is Strong; their powers run parallel. It likes Wood support but not excessively; if excessive, it becomes scorching. It desires Water for "Completion"; if Water is present, one need not worry about prosperity; prosperity then brings grace. Abundant Earth causes obstruction and buries light. Excessive Fire causes injury and intense dryness. Seeing Metal allows it to perform work; even if Metal is heavy, using Wealth is especially successful.
  
  Fire in Summer Months: It holds command and authority. Meeting Water control avoids the fault of self-incineration. Seeing Wood support invites the disaster of premature death. Meeting Metal makes one a skilled craftsman. Obtaining Earth achieves "Sowing and Reaping" (Productivity). Although Metal and Earth are beneficial, without Water, Metal becomes dry and Earth scorched; adding Wood makes it dangerously excessive.
  
  Fire in Autumn Months: Its nature rests and its body is harmonious. Obtaining Wood generation brings the celebration of restored brightness. Meeting Water control inevitably brings the disaster of extinction. Heavy Earth masks its light. Abundant Metal damages its momentum. Fire seeing Fire adds brilliance; even repeated appearance is beneficial.
  
  Fire in Winter Months: Its body is cut off and form perished. It likes Wood generation for salvation; meeting Water control is a calamity. It desires Earth to control Water for glory, and loves Fire parallel for benefit. Seeing Metal makes it hard to handle Wealth; without Metal, one avoids harm. Even if Heaven and Earth overturn (Water excess), Fire and Water struggle to achieve "Completion" (without Wood/Earth).

- **核心要点**：
  - **春火**：喜金（施功）、水（既济）；忌土（晦光）、木盛（火炎）。
  - **夏火**：专用水（调候/制劫）；忌木（自焚）；喜金（良工）、土（泄秀）。
  - **秋火**：喜木（复明）、火（帮身）；忌水（灭火）、土（晦光）、金（身弱）。
  - **冬火**：喜木（救星）、土（制杀）、火（帮身）；忌水（灭火）、金（党杀）。

- **详细解说**：
  - 夏火最关键是“免自焚”，故必须见水。无水之火，名为“毒火”。
  - 冬火最关键是“防灭”，故必须见木（通关）或土（制杀）。
  - 秋火体休，最喜比劫帮身或印绶生身，即“复明”。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_219]` `[trigger: 春火]` `[factor_trigger: season_spring AND element_fire AND mother_child_strong]` `[role: 主干]` 生于春月，母旺子相，势力并行，喜木生扶，不宜过旺，旺则火炎。 → 《穷通宝鉴·论火》#11.2
  - `[ns_qttbj_220]` `[trigger: 夏火自焚]` `[factor_trigger: season_summer AND element_fire AND summer_fire_likes_water]` `[role: 条件分支]` 夏月之火，秉令乘权，逢水制则免自焚之咎，见木助必招夭折之患。 → 《穷通宝鉴·论火》#11.2
  - `[ns_qttbj_221]` `[trigger: 秋火复明]` `[factor_trigger: season_autumn AND element_fire AND autumn_fire_likes_parallel]` `[role: 条件分支]` 秋月之火，性息体和，得木生则有复明之庆，遇水克难免陨灭之灾。 → 《穷通宝鉴·论火》#11.2
  - `[ns_qttbj_222]` `[trigger: 冬火体绝]` `[factor_trigger: season_winter AND element_fire AND winter_fire_likes_wood]` `[role: 条件分支]` 冬月之火，体绝形亡，喜木生而有救，遇水克以为殃。 → 《穷通宝鉴·论火》#11.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 四季火的喜忌（细论）"
    factor_refs: list = ['mother_child_strong', 'self_incineration', 'restoring_brightness', 'sowing_reaping']
    
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
        l1_anchor="qtbj_v1.0.0_2__四季火的喜忌_细论_001_L1",
    )
    version: str = "1.0.0"
