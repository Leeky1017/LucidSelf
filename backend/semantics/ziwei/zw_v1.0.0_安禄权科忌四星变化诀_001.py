"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654146
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
    semantic_id="zw_v1.0.0_安禄权科忌四星变化诀_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 安禄权科忌四星变化诀(SemanticEntry):
    """
    **主题**：论生年天干四化星（禄权科忌）。

#### 原文（断句）：

甲廉破武阳为伴，乙机梁紫月交侵。丙同机昌廉贞位，丁月同机巨门寻。戊贪月弼机为主，己武贪梁曲最平。庚日武同相为首，辛巨阳曲昌至...
    """
    
    original_text: str = """**主题**：论生年天干四化星（禄权科忌）。

#### 原文（断句）：

甲廉破武阳为伴，乙机梁紫月交侵。丙同机昌廉贞位，丁月同机巨门寻。戊贪月弼机为主，己武贪梁曲最平。庚日武同相为首，辛巨阳曲昌至临，壬梁紫府武宿是，癸破巨阴贪狼停。

#### 分字分词释义：

- **甲廉破武阳为伴**：甲年生人，廉贞化禄、破军化权、武曲化科、太阳化忌。
- **乙机梁紫月交侵**：乙年生人，天机化禄、天梁化权、紫微化科、太阴化忌。
- **丙同机昌廉贞位**：丙年生人，天同化禄、天机化权、文昌化科、廉贞化忌。
- **丁月同机巨门寻**：丁年生人，太阴化禄、天同化权、天机化科、巨门化忌。
- **戊贪月弼机为主**：戊年生人，贪狼化禄、太阴化权、右弼化科、天机化忌。
- **己武贪梁曲最平**：己年生人，武曲化禄、贪狼化权、天梁化科、文曲化忌。
- **庚日武同相为首**：庚年生人，太阳化禄、武曲化权、天同化科、天相化忌。
- **辛巨阳曲昌至临**：辛年生人，巨门化禄、太阳化权、文曲化科、文昌化忌。
- **壬梁紫府武宿是**：壬年生人，天梁化禄、紫微化权、天府化科、武曲化忌。
- **癸破巨阴贪狼停**：癸年生人，破军化禄、巨门化权、太阴化科、贪狼化忌。

#### 四化表：

| 天干 | 化禄 | 化权 | 化科 | 化忌 |
|-----|------|------|------|------|
| 甲 | 廉贞 | 破军 | 武曲 | 太阳 |
| 乙 | 天机 | 天梁 | 紫微 | 太阴 |
| 丙 | 天同 | 天机 | 文昌 | 廉贞 |
| 丁 | 太阴 | 天同 | 天机 | 巨门 |
| 戊 | 贪狼 | 太阴 | 右弼 | 天机 |
| 己 | 武曲 | 贪狼 | 天梁 | 文曲 |
| 庚 | 太阳 | 武曲 | 天同 | 天相 |
| 辛 | 巨门 | 太阳 | 文曲 | 文昌 |
| 壬 | 天梁 | 紫微 | 天府 | 武曲 |
| 癸 | 破军 | 巨门 | 太阴 | 贪狼 |

#### 完整对等诠释（secondary_lang_full·13四化）：

The Four Transformations system overlays a moving layer of emphasis onto the fixed grid of stars by using the birth year stem as a trigger. Each of the ten Heavenly Stems sends four specific stars into transforming states called Lu, Quan, Ke and Ji. These transformations do not create new bodies in the chart; instead, they "light up" existing main and auxiliary stars, colouring their expression with gain, authority, merit or strain. Once the year stem is known, the table of ten stems and four transformations immediately reveals which stars in a given chart are carrying additional weight in the form of wealth, power, reputation or karmic debt.

Lu, or Transforming Benefit, tends to increase a star's sense of ease, resources and attractiveness, making its topics easier to access or more rewarding. Quan, or Transforming Authority, concentrates willpower, control and the capacity to command around its host star, for better or for worse. Ke, or Transforming Merit, refines and dignifies: it is associated with learning, moral standing, credentials and the ability to be recognised and trusted. Ji, or Transforming Obstruction, exposes the shadow side of a configuration, surfacing attachment, imbalance, controversy or the price that must be paid. In interpretation, the Four Transformations are read together: a chart rich in Lu and Ke but with carefully managed Ji suggests resources and reputation that largely work in the native's favour, while excessive Quan and unmanaged Ji can signal tangled power struggles, burnout or reputational risk centred on whichever houses host the transformed stars.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 四化星 | Four Transformations | 生年天干引发的禄权科忌四种变化 | Four transformations Lu-Quan-Ke-Ji | system_sihuaxing | existing |
| 化禄 | Transforming Lu | 使原星财气顺利吸引力增强 | Increases resources ease attractiveness | transform_hualu | existing |
| 化权 | Transforming Quan | 使原星权势主动性掌控力上升 | Heightens authority initiative command | transform_huaquan | existing |
| 化科 | Transforming Ke | 使原星名誉评价文教意味提升 | Emphasises reputation moral esteem | transform_huake | existing |
| 化忌 | Transforming Ji | 使原星压力纠缠代价面放大 | Exposes problematic side friction | transform_huaji | existing |

#### 详细解说：

四化星是紫微斗数中最重要的动态系统，依据生年天干决定哪些主星被"点亮"为禄、权、科、忌四种状态。四化不创造新星，而是给原有星曜赋予额外的吉凶属性。

**四化的本质**：
- **化禄**：增益，使主星的正面特质得到放大，主财喜、顺遂、吸引力
- **化权**：集权，使主星的主动性与掌控力增强，主权贵、威武、支配力
- **化科**：提升，使主星的声望与文教属性增强，主功名、声誉、认可度
- **化忌**：阻滞，使主星的负面特质被激发，主是非、执着、代价

**四化的应用层次**：
1. **生年四化**：固定不变，代表命主一生的基本格局特征
2. **大限四化**：随十年大限变化，代表不同人生阶段的主题
3. **流年四化**：随每年变化，代表当年的吉凶趋势
4. **飞星四化**：由宫位的天干引发，用于高级推断

**重要格局**：
- **双禄交流**：化禄与禄存同宫或会照，财运极佳
- **权禄巡逢**：化权与化禄同宫，主有权有财
- **科权禄拱命**：三吉化会照命宫，是大贵格局
- **化忌入命**：需看制化，无制则一生多阻碍

#### 校勘与字词辨析（bilingual）：

- **"四化"**：化禄、化权、化科、化忌四种变化的统称。英文："Four Transformations"。
- **"为伴/交侵/为主"**：均为文学表达，指四化星与生年天干的关联。英文："poetic expressions for transformation associations"。
- **"化"**：变化、转化之意，指星曜被赋予新的属性。英文："transformation, activation"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："甲廉破武阳，乙机梁紫阴，丙同机昌廉，丁阴同机门。"此为四化口诀的简化版，便于记忆。
- **四化精义**：古人云"禄主财喜，权主威名，科主功名，忌主是非"，是四化最基本的象征意义。
- **现代应用**：四化在现代命理咨询中是最核心的技法之一。化禄可理解为机会与资源，化权可理解为决策权与影响力，化科可理解为专业认可与社会评价，化忌可理解为压力点与需要面对的课题。"""
    normalized_text_zh: str = """"""
    subject: str = "安禄权科忌四星变化诀"
    factor_refs: list = ['source_ref', 'rel_sihua_001', 'principle_tiangansihua', 'rel_sihua_002', 'principle_tiangansihua', 'rel_sihua_003', 'principle_tiangansihua', 'rel_sihua_004', 'principle_tiangansihua', 'evi_sihua_001', 'transform_hualu', 'rule_sihua_jia', 'evi_sihua_002', 'transform_huaquan', 'rule_sihua_yi', 'concept_transformation', 'concept_fortune_boost', 'concept_authority_boost', 'concept_reputation_boost', 'concept_obstruction']
    
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
        l1_anchor="zw_v1.0.0_安禄权科忌四星变化诀_001_L1",
    )
    version: str = "1.0.0"
