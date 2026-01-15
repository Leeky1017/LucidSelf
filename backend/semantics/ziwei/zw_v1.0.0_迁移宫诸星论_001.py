"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.636735
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
    semantic_id="zw_v1.0.0_迁移宫诸星论_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 迁移宫诸星论(SemanticEntry):
    """
    #### 原文（断句）：

迁移宫诸星论。凡看迁移，先看命宫、迁移宫星曜庙旺、落陷，以定命主宜动宜静；次看吉星、煞星会照，在外有无贵人扶持、多寡是非；又看三方四正与对宫，推断出外求财、仕宦、商旅、艺术...
    """
    
    original_text: str = """#### 原文（断句）：

迁移宫诸星论。凡看迁移，先看命宫、迁移宫星曜庙旺、落陷，以定命主宜动宜静；次看吉星、煞星会照，在外有无贵人扶持、多寡是非；又看三方四正与对宫，推断出外求财、仕宦、商旅、艺术、流荡诸象，以及在外安危吉凶。

#### 分字分词释义：

- **迁移宫**：十二宫之一，主外出、迁居、旅行、异地发展及对外形象。
- **宜动不宜静 / 宜静不宜动**：有的格局适合多动多变、在外发展；有的适合安守本位、少动多稳。
- **闹中求财**：在人多事杂、信息密集的环境中求财，如市井、商场、市场、演艺场所等。
- **流荡天涯**：长期在外奔波、居无定所，难得安稳，与家乡根基疏离。

#### 规范化释义（primary_lang_explained）：

迁移宫专门论命主在"外面的世界"的运势：是否适合在外发展，外出时运气好不好，人际环境是否和谐，以及在外安危如何。判断时，首先综合命宫与迁移宫：

- 命宫与迁移宫都强吉，多主内外兼修，既能在外发展，又能稳住根基；
- 命宫强而迁移宫弱，宜守成不宜过度奔波，动多反生扰动与损耗；
- 命宫弱而迁移宫吉，则适合借外出之机改善环境、扩展空间。

其次看吉凶星：吉星多而煞星少者，在外多遇贵人相助，动中得利；煞星重又见空劫耗忌者，则在外奔波多、是非多，甚至有盗劫、官非之忧。再结合星曜性质，可分辨适合的出路类型：仕宦、公职、商贾、技艺、艺术、流荡等，各有不同。

#### 完整对等诠释（secondary_lang_full·6迁移宫）：

The Travel Palace describes how a person moves through the wider world: whether life pulls them toward staying rooted or constantly being on the road, how supportive or hostile external environments tend to be, and what happens when they leave the familiar home base. A strong pairing of the Life Palace and the Travel Palace paints the image of someone who can go abroad, relocate or change fields without losing their centre, using each move to widen opportunity. When the Life Palace is solid but the Travel Palace is weak, the chart leans toward cultivating depth in one place: too much movement drains energy, disrupts routines and amplifies friction instead of bringing growth.

Conversely, a weaker Life Palace combined with a well‑aspected Travel Palace often suggests that changing cities, cultures or professional arenas is how the native upgrades their circumstances. Benefic stars and noble helpers in this palace speak of useful contacts, mentors and timely chances that appear once they step outside their comfort zone. Heavy malefic clusters, especially with loss and emptiness stars, warn that constant motion may bring lawsuits, scams, accidents or chronic exhaustion rather than progress. In modern practice, this palace helps distinguish people who thrive as frequent travellers, expatriates or digital nomads from those who are better served by building a stable base and choosing movement more selectively.

#### 核心要点（整理）：

1. **动静取向**：命宫+迁移宫强吉者宜动中求进，迁移宫弱而煞重者宜少动多守。
2. **外出发展方向**：紫微、天府、天相等偏仕宦、公职与管理；贪狼、破军、七杀等偏商旅、技艺、演艺等高流动职业。
3. **人际好坏与是非**：吉星多则在外贵人多、小人少；煞星多则多争执是非、人际不安。
4. **安危与风险**：煞重又逢空劫耗忌者，在外须防车马、盗劫、官非等意外；吉星会照则多有惊无险。
5. **本地与异地平衡**：有的命适合长期在外打拼，有的适合阶段性外出后再回本地，迁移宫给出的是趋势与倾向。

#### 详细解说（提要）：

1. **命宫 vs 迁移宫**：命宫代表"我是谁"与内在主干，迁移宫代表"我在外界如何运动"与对外场域。两宫皆吉，则能在变化中保持稳定；若迁移宫弱，则不宜过度追求频繁迁徙。
2. **职业类型与迁移宫**：官禄宫定职业主线，迁移宫定职业的流动方式。迁移宫动而有吉星，多主出差、出行、异地项目频繁；静而有吉星，则适合稳定在一地深耕。
3. **吉星与煞星的调和**：左右魁钺会迁移宫，多主在外得贵人提携；羊陀火铃空劫会合，则须警惕是非纠纷与安全事件。
4. **现代延伸**：可引申至跨城工作、海外留学、远程协作、数字游牧等各种"空间变动"形态。

#### 校勘与字词辨析：

- **闹中**：人多事杂、信息流密集的环境，对应高流量、高噪音的场域。
- **动中则吉**：在行动、变化之中反而顺利，若强行静守反易压抑或错失机会。
- **流荡天涯**：古意多带漂泊感，现代可理解为高频迁徙、缺乏稳定据点的生活方式。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："紫府昌曲守迁移，出门贵人常相随，动中求财财必得，四海声名誉满归。"此句常用于吉星守迁移宫的"动中吉利"格局描述。
- **反面叙事**："七杀羊陀临迁移，出外多灾恐难回，不是盗贼便意外，流荡天涯苦愁眉。"此句警示煞星重临迁移宫的出外风险。
- **现代转化**：某企业高管命主迁移宫紫微天府加会左右，职业生涯中频繁出差、外派，每到一地皆有贵人相助，晚年荣归故里。此例验证"动中吉利、在外有人提携"的论断。"""
    normalized_text_zh: str = """"""
    subject: str = "迁移宫诸星论"
    factor_refs: list = ['palace_travel', 'pattern_naozhongcai', 'pattern_yidong', 'pattern_liudang', 'source_ref', 'rel_qianyi_001', 'star_ziwei', 'rel_qianyi_002', 'group_liusha', 'rel_qianyi_003', 'star_qisha', 'evi_qianyi_001', 'star_ziwei', 'rule_qianyi_ziwei', 'evi_qianyi_002', 'group_liusha', 'rule_qianyi_sha', 'concept_travel', 'concept_adaptation']
    
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
        l1_anchor="zw_v1.0.0_迁移宫诸星论_001_L1",
    )
    version: str = "1.0.0"
