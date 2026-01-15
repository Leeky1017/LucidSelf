"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654384
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
    semantic_id="zw_v1.0.0_诸星分属南北斗化吉凶并五行_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 诸星分属南北斗化吉凶并五行(SemanticEntry):
    """
    - 分字分词释义：

  - **南北斗**：星曜分属南斗或北斗星系。
  - **化象**：星曜的象征意义与转化功能。
  - **主司**：星曜主管的宫位或事务。
  - **紫微帝座**：紫微为...
    """
    
    original_text: str = """- 分字分词释义：

  - **南北斗**：星曜分属南斗或北斗星系。
  - **化象**：星曜的象征意义与转化功能。
  - **主司**：星曜主管的宫位或事务。
  - **紫微帝座**：紫微为帝星，主官禄。
  - **天府禄库**：天府为禄库，主财帛。
  - **天机善**：天机化善，主兄弟。
  - **破军耗**：破军化耗，主奴仆。

#### 主星属性表：

| 星曜 | 五行 | 南北斗 | 化象 | 主司 |
|------|------|--------|------|------|
| 紫微 | 土 | 中天 | 帝座 | 官禄主 |
| 天机 | 木 | 南斗 | 善 | 兄弟主 |
| 太阳 | 火 | 南北斗 | 贵 | 官禄主 |
| 武曲 | 金 | 北斗 | 财 | 财帛主 |
| 天同 | 水金 | 南斗 | 福 | 福德主 |
| 廉贞 | 火 | 北斗 | 囚 | 官禄主/次桃花 |
| 天府 | 土 | 南斗 | 令 | 财帛田宅主 |
| 太阴 | 水 | 南北斗 | 富 | 财帛田宅主 |
| 贪狼 | 水木 | 北斗 | 桃花 | 祸福主 |
| 巨门 | 水 | 北斗 | 暗 | 是非主 |
| 天相 | 水 | 南斗 | 印 | 官禄主 |
| 天梁 | 土 | 南斗 | 荫 | 寿星 |
| 七杀 | 火金 | 南斗 | 将 | 权柄 |
| 破军 | 水 | 北斗 | 耗 | 夫妻子女奴仆 |

#### 辅星属性：

- 文昌文曲：科甲星
- 左辅右弼：善佐帝令
- 天魁天钺、天马：吉星
- 擎羊陀罗：化刑化忌
- 火铃：助星
- 空劫：主败
- 四化：禄土、权木、科水、忌水

#### 完整对等诠释（secondary_lang_full·42南北斗属性表）：

  This comprehensive attribute table classifies all major and auxiliary stars by element, Dipper affiliation, symbolic transformation, and domain of governance. The fourteen major stars range from Ziwei (Earth, Central Heaven, Emperor's Throne, Career governor) through Pojun (Water, North Dipper, Consumption, governing Spouse-Children-Servants). Auxiliary stars include the scholarly pair Wenchang-Wenqu (examination stars), the ministerial pair Zuofu-Youbi (imperial aides), the noble pair Tiankui-Tianyue plus Tianma (auspicious stars), the harsh pair Qingyang-Tuoluo (punishment and hindrance), the fiery pair Huoxing-Lingxing (assistants), and the destructive pair Dikong-Dijie (ruin stars). The Four Transformations assign elements as well: Lu (Salary) is Earth, Quan (Authority) is Wood, Ke (Examination) is Water, Ji (Hindrance) is Water. This table serves as the foundational reference for all subsequent pattern and compatibility analysis."""
    normalized_text_zh: str = """"""
    subject: str = "诸星分属南北斗化吉凶并五行"
    factor_refs: list = ['group_nandou', 'group_beidou', 'concept_huaxiang', 'concept_zhusi']
    
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
        l1_anchor="zw_v1.0.0_诸星分属南北斗化吉凶并五行_001_L1",
    )
    version: str = "1.0.0"
