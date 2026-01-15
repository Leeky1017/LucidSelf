"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654240
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
    semantic_id="zw_v1.0.0_安封诰诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安封诰诀(SemanticEntry):
    """
    **主题**：论本生时安封诰。

#### 原文（断句）：

从寅宫起子，顺数至本生时安之。

#### 分字分词释义：

- **封诰**：杂曜之一，象征封赠、嘉奖、荣誉称号。
- **从寅宫起子*...
    """
    
    original_text: str = """**主题**：论本生时安封诰。

#### 原文（断句）：

从寅宫起子，顺数至本生时安之。

#### 分字分词释义：

- **封诰**：杂曜之一，象征封赠、嘉奖、荣誉称号。
- **从寅宫起子**：以寅宫作为子时的起点。
- **顺数**：顺时针方向数。
- **本生时**：命主出生的时辰。
- **安之**：安放此星。

#### 安星规则：

- 寅宫起子时，顺数至生时

#### 规范化释义（primary_lang_explained）：

封诰与台辅同为依本生时安放的荣誉星，只是关注点更偏向“受封、受奖与名义上的嘉许”。歌诀“从寅宫起子，顺数至本生时安之”表明：以寅宫视为子时起点，按十二时辰顺推到命主出生之时，即得封诰所在宫位。该宫在当事人的一生之中，更容易出现来自体制、组织或长辈的正式表彰、头衔与光环，也可能只是“名义上的封赠”，未必伴随实权与物质利益。

实务上，封诰落于官禄宫、命宫，多主易得职称、奖章、荣誉称号等，适合作为“履历光环”；落于福德、田宅宫，则偏向家族荣誉或精神层面的“门第光彩”。若与台辅、三台八座、魁钺等同会，荣誉感更强，但也可能出现“虚名重、实权轻”的情况，需要通过主星格局与禄权科来判别。现代解读时，封诰可以拓展为各种证书、资质、奖项乃至网络时代的声望指标，只要其本质是“被正式认可”，都在此象意之内。

#### 完整对等诠释（secondary_lang_full·22封诰）：

Fenggao is an honour star that, like Taifu, is positioned by the birth hour, but it focuses more on titles, decorations and formal recognition. The verse “start from Yin and count from Zi to the native’s hour” instructs us to treat the Yin palace as hosting Zi hour and then move forward through the time branches until we reach the person’s birth hour; that house receives Fenggao. Wherever it lands in the chart, it highlights where life is most likely to accumulate certificates, awards, honorary posts or public praise.

When Fenggao occupies the Career or Life palaces, it often coincides with promotions, professional titles or honours that polish the résumé, even if they do not always expand real power or income. In the Fortune or Property palaces, its influence leans toward family reputation, household prestige or symbolic status markers such as addresses and surroundings. When combined with Taifu, Santai, Bazuo, Kui or Yue, the pattern can show someone who is frequently decorated, appointed to advisory committees or invited into visible roles. In contemporary terms, Fenggao extends to credentials, prizes and even digital-era badges of reputation, as long as they function as formalised recognition rather than quiet, private satisfaction.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 封诰 | Fenggao | 寅宫起子顺数生时主封赠荣誉 | From Yin-Zi by hour bestowals awards | star_fenggao | existing |
| 荣誉系统 | Honour System | 封诰等星描绘头衔奖项认可 | Stars mapping titles awards recognition | system_rongyu | new_candidate |
| 名实落差 | Name-Substance Gap | 荣誉与实权资源不符 | Fame exceeds real power resources | concept_mingshiluocha | new_candidate |
| 生时顺数法 | Hour-Based Forward Counting | 特定宫起子时顺数至生时 | Count forward from palace to hour | algo_shengshishunshuf | existing |

#### 详细解说：

封诰是紫微斗数杂曜系统中与"荣誉嘉奖"相关的星曜，它与台辅同样依据出生时辰定位，但侧重于"封赠、奖章、头衔"等名义上的认可。

**算法原理**：
- 以寅宫为子时的起点
- 从寅宫顺时针数到命主出生时辰
- 落点宫位即为封诰所在

**封诰的象征意义**：
- 封诰主"荣誉"而非"实权"，象征证书、奖章、头衔等
- 入命或官禄的人，容易获得正式的表彰与认可
- 可能存在"名实落差"，即名望高于实际权力

**重要格局**：
- **封诰入命官禄**：主易得职称、荣誉称号
- **封诰配台辅**：荣誉与辅政双全，名副其实
- **封诰配魁钺**：主得贵人提携，荣誉加身

**现代应用**：
封诰可延伸为各类证书、资质、奖项、社会声誉等"被正式认可"的指标。

#### 校勘与字词辨析（bilingual）：

- **"封诰"**：古代指皇帝的封赠文书，引申为荣誉称号。英文："Fenggao, Honor Star, referring to formal recognition and titles"。
- **"寅宫起子"**：以寅宫作为子时的参照点。英文："Yin palace as the anchor for Zi hour"。
- **"名实落差"**：名望与实际权力或资源不符的情况。英文："name-substance gap, where reputation exceeds actual power"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："封诰寅宫起子时，顺数生时便安之，荣誉加身光门第，职称奖章总相宜。"此诀概括了封诰的定位方法与荣誉象征。
- **名实相符**：古人云"封诰配台辅，名实两相符"，形容封诰与台辅同会时荣誉与实权并重。
- **现代应用**：封诰在现代可用于评估"获得正式认可"的潜力。入命或官禄的人，往往容易获得证书、奖项、职称等社会认可。"""
    normalized_text_zh: str = """"""
    subject: str = "安封诰诀"
    factor_refs: list = ['source_ref', 'rel_fenggao_001', 'algo_shengshishunshuf', 'rel_fenggao_002', 'star_fenggao', 'evi_fenggao_001', 'star_fenggao', 'rule_fenggao_dingwei', 'concept_honour_star']
    
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
        l1_anchor="zw_v1.0.0_安封诰诀_001_L1",
    )
    version: str = "1.0.0"
