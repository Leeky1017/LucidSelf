"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654221
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
    semantic_id="zw_v1.0.0_安龙池凤阁诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安龙池凤阁诀(SemanticEntry):
    """
    **主题**：论本生年支安龙池凤阁。

#### 原文（断句）：

龙池子顺辰，凤阁子戌逆。

#### 分字分词释义：

- **龙池**：杂曜之一，象征文章、学问、才华。
- **子顺辰**：子年...
    """
    
    original_text: str = """**主题**：论本生年支安龙池凤阁。

#### 原文（断句）：

龙池子顺辰，凤阁子戌逆。

#### 分字分词释义：

- **龙池**：杂曜之一，象征文章、学问、才华。
- **子顺辰**：子年在辰宫，顺时针数到生年。
- **凤阁**：杂曜之一，象征艺术、风雅、审美。
- **子戌逆**：子年在戌宫，逆时针数到生年。

#### 安星规则：

- **龙池**：子年在辰，顺数至生年
- **凤阁**：子年在戌，逆数至生年

#### 规范化释义（primary_lang_explained）：

龙池、凤阁是一对与文章才华、艺术风雅有关的吉曜，皆随生年地支安放：子年起点一落辰宫、一落戌宫，再顺逆各行一圈，直到本生年为止。龙池偏向文字、学问与笔下功夫，凤阁偏向审美、艺术与仪态气度，两星所在宫位，往往就是命主比较容易通过文化资本、审美品味来加分的领域。

实务中，龙池、凤阁落入命宫、官禄宫，多主本人有书卷气与艺术修养，适合从事与写作、教学、设计、文化传播相关的工作；落入福德、田宅宫，则更像是把“风雅”安在生活方式与居住环境中，易有美感空间与文化氛围。若再会合昌曲、魁钺等文星与贵星，则“台阁清要”之象更浓，表示有机会因才华与风度而受上级赏识、出入核心场合。

#### 完整对等诠释（secondary_lang_full·20龙池凤阁）：

Longchi and Fengge are a refined pair of stars that speak to cultural literacy and artistic grace rather than raw power. Both are tied to the birth year: Longchi is found by treating Zi year as seated in Chen and counting forward, while Fengge treats Zi as seated in Xu and counts backward, each landing on the native’s branch. Wherever they reside in the chart, they mark places where style, language and aesthetic awareness become key resources.

When Longchi and Fengge occupy the Life or Career palaces, they often show people who move comfortably in educated or artistic circles—writers, teachers, designers, curators, or professionals whose work depends on elegant communication. In the Fortune or Property palaces, they point more to cultivated living: pleasant homes, taste in objects and a preference for environments with cultural depth. When supported by stars such as Changqu, Kui and Yue, the configuration can lift the native into positions where being articulate, poised and aesthetically sensitive is precisely what grants access to influential rooms.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 龙池 | Longchi | 辰宫起子顺数主文章学问 | From Chen forward literary scholarly | star_longchi | existing |
| 凤阁 | Fengge | 戌宫起子逆数主艺术风雅 | From Xu backward artistic grace | star_fengge | existing |
| 文艺辅贵星 | Cultural-Artistic Aides | 龙凤主文化审美贴近核心 | Culture aesthetics near power | group_wenyifugui | new_candidate |
| 生年定位法 | Year-Branch Placement | 以生年支为落点一顺一逆 | By year branch forward-backward | principle_shengniandinwei | existing |

#### 详细解说：

龙池与凤阁是紫微斗数杂曜系统中与文艺才华相关的一对吉曜，龙池主文章学问，凤阁主艺术风雅，二者都依据生年地支定位。

**算法原理**：
- 龙池以辰宫为子年起点，顺时针数到生年地支
- 凤阁以戌宫为子年起点，逆时针数到生年地支
- 辰戌为对冲宫位，龙池凤阁一顺一逆，形成对称分布

**龙池与凤阁的象征意义**：
- **龙池**：主文章、学问、书卷气、笔下功夫。入命的人往往有文学才华或学术倾向。
- **凤阁**：主艺术、审美、风雅、仪态。入命的人往往有艺术气质或审美品位。

**重要格局**：
- **龙凤入命**：龙池或凤阁入命宫，主人有文艺才华，气质不凡
- **龙凤配昌曲**：与文昌文曲同会，文章秀丽，才华横溢
- **龙凤入官禄**：主从事文艺相关工作，如写作、教学、设计等

**现代应用**：
龙池凤阁可延伸为"文化资本"与"审美素养"的指标。入命或官禄的人，往往能够通过文化、艺术、品位等软实力获得成功。

#### 校勘与字词辨析（bilingual）：

- **"龙池"**：古代皇宫中的池塘名，引申为文华之地。英文："Longchi, Literary Pool, referring to scholarly refinement"。
- **"凤阁"**：古代皇宫中的楼阁名，引申为风雅之所。英文："Fengge, Phoenix Pavilion, referring to artistic grace"。
- **"辰戌对冲"**：辰宫与戌宫在十二宫中相对，龙池凤阁分别从此起点。英文："Chen and Xu as opposing palaces"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："龙池子顺辰，凤阁子戌逆，二星主文艺，才华不可测。"此诀概括了龙池凤阁的定位方法与文艺象征。
- **龙凤呈祥**：古人认为龙池凤阁同会或夹命，是"龙凤呈祥"的文艺格局，主人才华出众。
- **现代应用**：龙池凤阁在现代可用于评估文化素养与艺术天赋。从事创意、设计、写作、教育等行业的人，若龙凤入命或官禄，往往更容易脱颖而出。"""
    normalized_text_zh: str = """"""
    subject: str = "安龙池凤阁诀"
    factor_refs: list = ['source_ref', 'rel_longfeng_001', 'principle_shengniandinwei', 'rel_longfeng_002', 'principle_shengniandinwei', 'rel_longfeng_003', 'star_longchi', 'evi_longfeng_001', 'star_longchi', 'rule_longchi_dingwei', 'evi_longfeng_002', 'star_fengge', 'rule_fengge_dingwei', 'concept_literary_star', 'concept_artistic_star']
    
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
        l1_anchor="zw_v1.0.0_安龙池凤阁诀_001_L1",
    )
    version: str = "1.0.0"
