"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.636772
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
    semantic_id="zw_v1.0.0_田宅宫诸星论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 田宅宫诸星论(SemanticEntry):
    """
    #### 原文（断句）：

田宅宫诸星论。凡看田宅，先看田宅宫星曜庙旺、落陷，以定一生祖业有无、田产多寡与自置能力；次看吉星、煞星会照，以辨承祖、退祖、破祖、无祖业，以及自创置业之易难；又看三方四正与...
    """
    
    original_text: str = """#### 原文（断句）：

田宅宫诸星论。凡看田宅，先看田宅宫星曜庙旺、落陷，以定一生祖业有无、田产多寡与自置能力；次看吉星、煞星会照，以辨承祖、退祖、破祖、无祖业，以及自创置业之易难；又看三方四正与对宫，推其先无后有、先有后无、有进有退与守祖荣昌、破荡飘零诸象。星曜庙旺加吉者，多主祖业可承、田园茂盛并能再自置；陷地又逢羊陀火铃空劫等煞者，多主退祖、破祖，或终身田少、置业艰难。

#### 分字分词释义：

- **田宅宫**：十二宫之一，主不动产、家宅、田园、房地产与居住稳定性。
- **承祖 / 退祖 / 破祖**：承祖指承受祖辈留下的产业；退祖指逐渐远离或失去祖业；破祖则是祖业被挥霍或失守。
- **自置**：靠自身努力购置房产、土地等，不依赖祖业。
- **有进有退**：田产时增时减，置业与卖房并存，整体呈波动状态。
- **飘零**：居无定所、频繁搬迁、家宅不稳，或祖业不守。

#### 规范化释义（primary_lang_explained）：

田宅宫专门论命主的一生居住环境与不动产格局，包括：是否有祖业可承、是否擅长自力置业、房产多寡，以及家业是否稳固或易有破荡。判断时，首先看田宅宫主星庙旺或陷弱：

- 主星庙旺又会吉星，多主祖业丰厚或居住条件较好，即使早年退祖，亦能中晚年自创稳定家业；
- 主星陷地或煞星重重，则多主祖业不守、破祖或田产少，居住环境多变，甚至有"飘零"之象。

其次看吉凶星组合：禄存、吉星聚会田宅宫，多主田产渐丰，购置能力佳；羊陀火铃空劫等煞曜会合，则多主田宅有进有退、买得起守不住，甚至有因房产招非的情况。再配合三方四正与对宫（如财帛宫、福德宫），可以判断命主是靠祖业、靠自身打拼，还是两者兼有，以及在哪个阶段更容易实现置业。

#### 完整对等诠释（secondary_lang_full·9田宅宫）：

The Property Palace describes how roots, land and dwellings show up in a life: whether there is ancestral estate to inherit, how easily one can buy or build, how often homes change, and how stable the domestic base feels. Strong, dignified stars with supportive benefics show charts that either receive substantial family property or, even without much inheritance, are able over time to gather houses and land and keep them. Fallen placements, especially when entangled with harsh and loss stars, point instead to thin or vanishing ancestral resources, repeated moves, or owning assets that are hard to hold onto.

Classical phrases about "breaking the ancestral home" or "having nothing" are better read today as patterns of volatility rather than literal homelessness: selling in the wrong cycle, over‑leveraging on mortgages, family disputes over real estate, or simply choosing a mobile, root‑light lifestyle. When read together with the Wealth and Fortune palaces, the Property Palace signals how much of a person’s sense of security is tied to bricks and land, and when it is wise to focus on consolidating a base versus staying flexible and light. It also reminds us that for some charts, the truest home is not where they were born, but where they eventually choose to plant themselves.

#### 核心要点（整理）：

1. **祖业 vs 自置**：区分承祖守成型和白手置业型，或先退祖后自置等组合路径。
2. **数量与规模**：根据主星庙陷与吉煞多少，判断田产是茂盛、一般、偏少还是几乎全无。
3. **时间结构**：看是先有后无、先无后有，还是一生有进有退，对应不同的人生置业节奏。
4. **稳定与飘零**：吉星多者多主家宅安稳，煞星重者多主搬迁频繁、家业起落大。
5. **现代延伸**：从传统田园扩展到现代房地产、资产配置与"居住安全感"。

#### 校勘与字词辨析：

- **田宅**：传统偏田产、屋舍，现代可泛指一切不动产及其衍生的居住条件与资产属性。
- **退祖**：不必理解为不孝，而多指客观上离开家乡或难以承接祖业。
- **冢业**：家族墓地与相关产业，原文中与田宅一体论之，现代可简化为"家族不动产"的一部分。
- **破荡家产**：指因挥霍、经营不善或外部灾祸等导致家产流失。

#### 详细解说：

田宅宫是紫微斗数中专论不动产与家业的宫位，古人视之为"安身立命之本"，现代则可理解为一个人在居住、置业与家族资产层面的模式与潜力。

**判断逻辑有三层**：
1. **祖业基底**：看主星与吉凶星的组合，判断是否有祖业可承。紫微、天府、太阴等守田宅宫，多主祖业丰厚或居住条件优越；破军、七杀、贪狼等守之，多主退祖或自创为主。
2. **自置能力**：结合财帛宫与田宅宫，判断命主自力置业的能力。禄存、化禄会田宅宫，多主置业能力强，能逐渐积累房产；空劫耗忌会之，则买得起守不住，或一生田产少。
3. **稳定与飘零**：吉星多者家宅安稳，煞星重者搬迁频繁。"有进有退"是常见模式，需看最终是进多于退，还是退多于进。

**时间层次的区分**：
- **先有后无**：早年有祖业可依，但中晚年逐渐败落或离散。
- **先无后有**：早年无祖业或退祖，但靠自身努力中晚年置业成功。
- **一生有进有退**：房产买卖并存，整体呈波动状态。
- **守祖荣昌**：祖业丰厚且能守住，一生居住稳定。
- **破祖飘零**：祖业不守，居无定所，频繁搬迁。

**现代应用**：
古代的"田园茂盛"在现代可理解为：房产投资成功、家族不动产丰厚、居住条件优越。"破祖飘零"则可理解为：租房为主、频繁搬迁、置业困难或因房产招非。田宅宫不仅是物质层面的房产问题，也反映命主对"家"与"根"的心理需求。煞重者往往居无定所但内心渴望安定；吉多者则安土重迁，以家为核心。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："紫府太阴守田宅，祖业丰厚田园广，自置更添锦上花，一生安稳守家邦。"此句常用于吉星守田宅宫的上佳格局描述。
- **反面叙事**："破军羊陀临田宅，退祖破祖难安歇，买得起来守不住，一生飘零如落叶。"此句警示煞星重临田宅宫的居住不稳风险。
- **现代转化**：某企业主命主田宅宫天府禄存同宫，早年承继祖业一套老房，中年自购三套商铺，晚年资产稳固，验证"库星主守祖自置两旺"。另一命主田宅宫破军火星同宫，一生搬家十余次，中年终于购房后又因经营失败被迫出售，验证"破军主退祖、有进有退"的特性。"""
    normalized_text_zh: str = """"""
    subject: str = "田宅宫诸星论"
    factor_refs: list = ['palace_property', 'pattern_zuye', 'pattern_zizhi', 'pattern_youjinyoutui', 'state_piaoling', 'source_ref', 'rel_tianzhai_001', 'star_tianfu', 'rel_tianzhai_002', 'group_liusha', 'rel_tianzhai_003', 'star_pojun', 'evi_tianzhai_001', 'star_tianfu', 'rule_tianzhai_tianfu', 'evi_tianzhai_002', 'group_liusha', 'rule_tianzhai_sha', 'concept_property', 'concept_roots']
    
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
        l1_anchor="zw_v1.0.0_田宅宫诸星论_001_L1",
    )
    version: str = "1.0.0"
