"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654261
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
    semantic_id="zw_v1.0.0_安红鸾天喜诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安红鸾天喜诀(SemanticEntry):
    """
    **主题**：论当生太岁支安红鸾天喜。

#### 原文（断句）：

卯上起子，逆数之，数到当生太岁支，坐守此宫红鸾位，对宫天喜不差移。年少婚姻喜事奇，老人必主丧其妻。三十年前为吉曜，五十年后不相宜。...
    """
    
    original_text: str = """**主题**：论当生太岁支安红鸾天喜。

#### 原文（断句）：

卯上起子，逆数之，数到当生太岁支，坐守此宫红鸾位，对宫天喜不差移。年少婚姻喜事奇，老人必主丧其妻。三十年前为吉曜，五十年后不相宜。

#### 分字分词释义：

- **红鸾**：婚姻喜星，主婚嫁、姻缘、情感。
- **天喜**：喜庆吉星，主喜事、庆典、吉利。
- **卯上起子**：以卯宫作为子年的起点。
- **逆数之**：逆时针方向数。
- **当生太岁支**：命主出生年的地支。
- **对宫天喜**：红鸾的对宫（相隔六位）安放天喜。
- **年少婚姻喜事奇**：年轻时遇到红鸾天喜主婚姻喜事。
- **老人必主丧其妻**：老年时遇到可能主丧偶。
- **三十年前为吉曜**：30岁前是吉星。
- **五十年后不相宜**：50岁后需谨慎解读。

#### 安星规则：

- 卯宫起子年，逆数至生年为**红鸾**
- 红鸾对宫为**天喜**

#### 对照表：

| 生年支 | 红鸾 | 天喜 |
|-------|------|------|
| 子 | 卯 | 酉 |
| 丑 | 寅 | 申 |
| 寅 | 丑 | 未 |
| 卯 | 子 | 午 |
| 辰 | 亥 | 巳 |
| 巳 | 戌 | 辰 |
| 午 | 酉 | 卯 |
| 未 | 申 | 寅 |
| 申 | 未 | 丑 |
| 酉 | 午 | 子 |
| 戌 | 巳 | 亥 |
| 亥 | 辰 | 戌 |

#### 作用：
- 主婚姻喜事
- 年少逢之吉，老人逢之凶（丧偶）

#### 规范化释义（primary_lang_explained）：

红鸾、天喜是一对以太岁支为锚点的喜庆桃花星：以卯宫起子年逆数安红鸾，对宫即为天喜，一主姻缘婚嫁，一主喜庆吉利。歌诀特别点出“年少婚姻喜事奇，老人必主丧其妻”，提醒占验时要将年龄维度一并纳入——同一颗星，在不同人生阶段，可能代表“喜宴良缘”，也可能代表“告别与送终”。

在古法中，红鸾天喜落入命宫、夫妻宫、迁移宫，多主早年易遇桃花良缘，适合成婚办喜事；落入父母、疾厄等宫，则常被视为“红白喜事并见”的信号，需要细看行运与整体格局。现代应用时，更强调它们指向的是“情感与关系的节点”：订婚、结婚、同居、分手后的重新开启，乃至有意识地调整亲密关系模式，都可视作红鸾天喜象征层面的应期，而不必拘泥于婚宴本身。

#### 完整对等诠释（secondary_lang_full·24红鸾天喜）：

Hongluan and Tianxi form a classic pair of celebration and romance stars anchored to the annual branch. By treating Mao as the starting point for Zi year and counting backward to the native’s year, Hongluan is fixed; its opposite house automatically hosts Tianxi. Together they mark where the chart is most likely to stage ceremonies, commitments and emotionally significant turning points.

Traditional texts emphasise a stark age contrast: for the young, these stars often coincide with courtship, engagement, marriage or other joyful milestones; for the elderly, especially when mixed with heavy malefics, they can point to funerals, farewells or the closing of long relationships. In contemporary practice, it is more useful to read Hongluan and Tianxi as timing indicators for shifts in intimacy—moving in together, redefining partnership, entering or leaving important bonds—whether or not there is a formal wedding. Their presence in particular houses shows which life arenas become saturated with feelings of union, joy, loss or bittersweet transition during key years.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 红鸾 | Hongluan | 卯宫起子逆数主婚姻姻缘 | From Mao backward marriage romance | star_hongluan | existing |
| 天喜 | Tianxi | 红鸾对宫主喜庆吉利 | Opposite Hongluan celebrations joy | star_tianxi | existing |
| 红鸾天喜成对 | Hongluan-Tianxi Pairing | 对宫成对标记情感节点 | Paired configuration relational milestones | pattern_hongluantianxi | existing |
| 年龄吉凶分界 | Age-Dependent Reading | 少吉老凶同星不同解 | Youth joy old age bereavement | principle_nianlingjiexiong | new_candidate |

#### 详细解说：

红鸾与天喜是紫微斗数中最重要的婚姻喜星，它们以对宫形式成对出现，共同标记命盘中与情感、婚姻、喜事相关的敏感宫位。

**算法原理**：
- 以卯宫为子年的起点
- 从卯宫逆时针数到命主生年地支，即为红鸾位置
- 红鸾的对宫（相隔六位）即为天喜位置

**红鸾与天喜的象征意义**：
- **红鸾**：主婚姻、姻缘、情感关系的确立与转变
- **天喜**：主喜庆、宴饮、吉利场合

**年龄吉凶分界**：
这是红鸾天喜的重要特征——同一颗星，在不同年龄段有截然不同的含义：
- **30岁前**：主婚姻喜事，订婚、结婚、喜宴
- **50岁后**：需谨慎解读，可能主丧偶、告别、离别

**现代应用**：
红鸾天喜可延伸为"情感关系节点"的指标，不仅限于婚姻。恋爱、同居、分手后的新开始、亲密关系的重新定义等，都在其象意范围内。

#### 校勘与字词辨析（bilingual）：

- **"红鸾"**：古代婚嫁时的红色喜鸾，象征婚姻喜事。英文："Hongluan, Marriage Star, symbolizing wedding and romance"。
- **"天喜"**：天赐之喜，象征喜庆吉利。英文："Tianxi, Joy Star, symbolizing celebration and auspiciousness"。
- **"对宫"**：相隔六位的宫位，如卯与酉、子与午。英文："opposite palace, houses that are six positions apart"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："红鸾天喜照命宫，年少婚姻喜事逢，三十之前为吉曜，五十之后须斟酌。"此诀概括了红鸾天喜的年龄分界特征。
- **对宫成对**：古人云"红鸾坐守，天喜对照，喜事成双，姻缘早到"，形容红鸾天喜的成对作用。
- **现代应用**：红鸾天喜在现代可用于评估"情感关系转折点"的时机。流年红鸾入命或夫妻宫时，往往是情感关系发生重要变化的时期。"""
    normalized_text_zh: str = """"""
    subject: str = "安红鸾天喜诀"
    factor_refs: list = ['source_ref', 'rel_hongluan_001', 'principle_shengniandinwei', 'rel_hongluan_002', 'star_hongluan', 'rel_hongluan_003', 'principle_nianlingjiexiong', 'evi_hongluan_001', 'star_hongluan', 'rule_hongluan_dingwei', 'evi_hongluan_002', 'star_tianxi', 'rule_tianxi_dingwei', 'concept_marriage_star', 'concept_joy_star']
    
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
        l1_anchor="zw_v1.0.0_安红鸾天喜诀_001_L1",
    )
    version: str = "1.0.0"
