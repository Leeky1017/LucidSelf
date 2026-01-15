"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.636784
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
    semantic_id="zw_v1.0.0_福德宫诸星论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 福德宫诸星论(SemanticEntry):
    """
    #### 原文（断句）：

福德宫诸星论。凡看福德，先看福德宫星曜庙旺、落陷，以定一生福气厚薄与心境安乐程度；次看吉星、煞星会合，以辨快乐安逸、操心劳力、忧喜参半与奔走不安；又看三方四正与田宅、官禄、...
    """
    
    original_text: str = """#### 原文（断句）：

福德宫诸星论。凡看福德，先看福德宫星曜庙旺、落陷，以定一生福气厚薄与心境安乐程度；次看吉星、煞星会合，以辨快乐安逸、操心劳力、忧喜参半与奔走不安；又看三方四正与田宅、官禄、命宫等宫位，推断先劳后逸、先逸后劳，及晚年是否能享清福。星曜庙旺加吉者，多主福厚寿长、身心安宁；陷地又逢羊陀火铃空劫等煞者，多主劳心费力、难得宁静，即有成就亦多操劳。

#### 分字分词释义：

- **福德宫**：十二宫之一，主福气、心境、享受能力与身心操劳程度，可视作心理与生活品质的指标。
- **福厚 / 福薄**：福厚指顺境较多、能享受生活；福薄指多劳少享、身心常感吃力。
- **忙中发福 / 忙中吉**：在忙碌、奔走中反而容易得利或感到充实，而非在静守中。
- **安静享福**：环境与内心皆相对宁静、不必过度奔波即可安然度日。
- **忧喜参半**：有好处也有烦恼，既有福分亦有操劳。

#### 规范化释义（primary_lang_explained）：

福德宫不专论物质多寡，而是着重于命主是否能真正享受人生，以及内在心境是安宁还是多忧。判断时，首先看福德宫主星庙旺或陷弱：

- 主星庙旺又会吉星，多主福厚，心境相对开朗，能在有限资源中感到满足，或在忙碌中仍能享受过程；
- 主星陷地又多煞，则多主心神不宁、忧虑较多，即使条件不差，主观体验也偏紧绷、操心。

其次看吉凶星组合：如天同、太阴、天府等福星守福德，多主快乐、安逸与清福；七杀、破军、羊陀火铃空劫等凶煞重重，则多主奔走不安、心身劳苦。部分组合主先劳后逸，中晚年方见安乐；部分则是一生劳心劳力，虽有小福但不易完全放松。原文中还特意提到女子福德的特殊情况，提示女性命盘在福德宫上常兼论婚姻与生活方式的选择。

#### 完整对等诠释（secondary_lang_full·10福德宫）：

The Fortune Palace traces the quality of a person’s inner life: how easily they feel content, how much room there is for rest and pleasure, and whether blessings arrive in ways they can actually appreciate. Strong, well‑supported stars here describe charts where, even amid work and responsibility, there is an underlying buoyancy—good company, hobbies, spiritual or aesthetic nourishment, and a capacity to let go. Afflicted placements tend to point toward chronic worry, difficulty relaxing, or a sense that joy must always be earned and can be taken away at any moment.

This house also encodes the timing of relief: some configurations labour hard first and only taste spaciousness in later years; others are born into easier circumstances but must eventually shoulder heavier emotional or karmic loads. Benevolent stars emphasise the ability to draw comfort from simple things and to recover psychologically after setbacks; heavy malefics highlight the importance of therapy, spiritual practice or conscious rest to prevent burnout. In contemporary reading, the Fortune Palace is less about "predestined luck" and more a map of what nourishes the soul, how much psychological slack exists in the system, and how to design a life where effort and enjoyment can coexist.

#### 核心要点（整理）：

1. **福气厚薄**：看庙旺与吉煞轻重，判断是福厚享福型，还是福薄劳苦型。
2. **心境状态**：区分快乐安逸、操心劳力、忧喜参半与忙中吉等不同心态结构。
3. **动静取向**：有的格局在忙碌奔波中反而发福；有的则适合安静享受，不宜过劳。
4. **早晚差异**：通过星曜与行运，看先劳后逸、先逸后劳，尤其关注中晚年是否能真正放松。
5. **性别差异**：部分组合在古籍中对女人福德另有强调，现代应用时需与现实性别角色和生活选择结合。

#### 校勘与字词辨析：

- **福德**：传统兼有福分与德行之意，此处侧重福分与享受能力，德行部分不作道德评判。
- **劳心费力**：不只是体力劳动，也包括过度思虑、精神压力与责任负担。
- **忙中发福**：强调在行动与忙碌之中获得机会或幸福，不一定等于过劳。

#### 详细解说：

福德宫是紫微斗数中专论心境与福气的宫位，与财帛宫的"物质财富"不同，福德宫侧重于"主观幸福感"——即命主能否真正享受人生，内心是安宁还是焦虑。

**判断逻辑有三层**：
1. **福气厚薄**：看主星与吉凶星的组合。天同、太阴、天府等福星守福德宫，多主福厚，心境开朗，能在有限资源中感到满足；七杀、破军、擎羊等孤克之星守之，多主福薄，劳心费力，即使物质条件不差，主观体验也偏紧绷。
2. **动静取向**：有的命适合在忙碌中发福（"忙中吉"），闲下来反而不适应；有的命适合安静享福（"静中福"），过度劳碌会透支身心。贪狼、武曲等动星守福德，多主前者；太阴、天同等静星守福德，多主后者。
3. **时间结构**：看先劳后逸还是先逸后劳。有的命年轻时辛苦奔波，中晚年才能放松享福；有的命早年顺遂，晚年却要承担更多责任与压力。

**与其他宫位的联动**：
- **福德宫 vs 命宫**：命宫是"我是谁"，福德宫是"我感觉如何"。命宫强而福德弱，外在成功但内心疲惫；命宫弱而福德强，虽无大成就但心态平和。
- **福德宫 vs 财帛宫**：财帛宫是"我有多少钱"，福德宫是"我能享受多少"。财帛丰而福德弱，赚得多却花不出去或不敢花；财帛薄而福德强，虽不富裕但知足常乐。
- **福德宫 vs 疾厄宫**：福德宫煞重者，常表现为情绪问题、焦虑抑郁、睡眠障碍等身心疾病，与疾厄宫互相印证。

**现代应用**：
福德宫在现代可用于评估命主的心理健康倾向与压力管理需求。煞重者需要更多的休息、放松与心理疏导；吉多者则心态自然开朗，容易从挫折中恢复。福德宫也提示命主适合的生活节奏：是高强度工作配合定期休假，还是细水长流的平稳生活。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："天同太阴守福德，一生福厚心无忧，安静享福多清闲，晚年更比早年优。"此句常用于福星守福德宫的上佳格局描述。
- **反面叙事**："七杀羊陀临福德，劳心费力福难多，即有衣禄心不宁，一生操劳似推磨。"此句警示煞星重临福德宫的身心劳苦风险。
- **现代转化**：某企业高管命主福德宫天同太阴同宫，虽工作繁忙但心态平和，周末必休息，年年出游，晚年退休后生活惬意，验证"福星主心宁能享"。另一命主福德宫七杀擎羊同宫，事业成功但焦虑严重，长期失眠服药，验证"杀星主劳心福薄"的特性，后通过心理咨询与生活调整逐渐改善。"""
    normalized_text_zh: str = """"""
    subject: str = "福德宫诸星论"
    factor_refs: list = ['palace_fortune', 'level_fuhou', 'pattern_mangzhongfafu', 'pattern_anjingxiangfu', 'state_youxichanban', 'source_ref', 'rel_fude_001', 'star_ziwei', 'rel_fude_002', 'star_tiantong', 'rel_fude_003', 'group_liusha', 'evi_fude_001', 'star_ziwei', 'rule_fude_ziwei', 'evi_fude_002', 'group_liusha', 'rule_fude_sha', 'concept_fortune', 'concept_peace']
    
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
        l1_anchor="zw_v1.0.0_福德宫诸星论_001_L1",
    )
    version: str = "1.0.0"
