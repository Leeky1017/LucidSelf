"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559605
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
    semantic_id="yhzp_v1.0.0_会要命书说_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 会要命书说(SemanticEntry):
    """
    - **原文（source_text）**：  
  会要命书说。  
  夫造命书，先贤已穷尽天地精微之蕴而极矣！自唐李虚中一行禅师、宋徐升东斋、明王诠醉醒子诸公，登觉【渊海】【渊源】，其理雷同，至...
    """
    
    original_text: str = """- **原文（source_text）**：  
  会要命书说。  
  夫造命书，先贤已穷尽天地精微之蕴而极矣！自唐李虚中一行禅师、宋徐升东斋、明王诠醉醒子诸公，登觉【渊海】【渊源】，其理雷同，至矣！尽矣！无非木火土金水之微妙耳。今之后学，加增旨意、口诀；莫非先贤已发之馀意，大同小异。今将【渊海】、【渊源】二书，合成一集，一览便知；不必寻究二书之旨，删繁去简，永为矜式。

- **分字分词释义**：
  - **造命书先贤已穷尽天地精微之蕴而极矣**：命书先贤已穷尽天地精微。
  - **自唐李虚中一行禅师宋徐升东斋明王诠醉醒子诸公**：唐李虚中宋徐升明王诠等先贤。
  - **登觉渊海渊源其理雷同至矣尽矣**：渊海渊源理同已尽。
  - **无非木火土金水之微妙耳**：无非五行之微妙。
  - **今之后学加增旨意口诀**：后学加增旨意口诀。
  - **莫非先贤已发之馀意大同小异**：为先贤馀意大同小异。
  - **今将渊海渊源二书合成一集**：合渊海渊源二书为一。
  - **一览便知**：一览便知其要。
  - **不必寻究二书之旨**：不必分寻二书之旨。
  - **删繁去简永为矜式**：删繁去简，永为典范。

- **规范化释义（primary_lang_explained）**：  
  《会要命书说》为全书总结与编纂说明，阐述本书编纂缘起、传承脉络与编纂原则。**命书传承**：造命书先贤已穷尽天地精微之蕴而极矣，自唐李虚中一行禅师宋徐升东斋明王诠醉醒子诸公，登觉渊海渊源其理雷同至矣尽矣，无非木火土金水之微妙耳。**后学增补**：今之后学加增旨意口诀，莫非先贤已发之馀意大同小异。**编纂原则**：今将渊海渊源二书合成一集一览便知，不必寻究二书之旨删繁去简永为矜式。

- **完整对等诠释（secondary_lang_full）**：  
  **Essentials of Fate Calculation Texts: A Statement**: This final section provides a comprehensive summary and compilation explanation, expounding upon this book's editorial origins, transmission lineage, and compilation principles. **Transmission of Fate Calculation Texts**: In composing fate calculation texts, our predecessors have thoroughly exhausted all subtle essences of heaven and earth to the ultimate degree! From the Tang dynasty's Li Xuzhong and Yixing Zen Master, through the Song dynasty's Xu Sheng (Dongzhai), to the Ming dynasty's Wang Quan (Zuixingzi) and other masters—all came to realize the teachings of *Yuanhai* and *Yuanyuan*, recognizing that their principles are essentially identical. They have reached the utmost and exhausted all! Nothing remains beyond the subtle mysteries of Wood, Fire, Earth, Metal, and Water. **Contributions of Later Scholars**: Today's later scholars have added supplementary intentions and oral formulas; yet these are merely the remaining implications already initiated by our predecessors—broadly similar with minor differences. **Compilation Principles**: Now we merge the two texts *Yuanhai* and *Yuanyuan* into one unified collection, making it comprehensible at a glance. There is no need to separately investigate the aims of the two books. We eliminate redundancies and retain essentials, so this work may eternally serve as an exemplar.

- **核心要点**：  
  - 全书总结与编纂说明，阐述编纂缘起传承脉络编纂原则  
  - 命书传承：唐李虚中宋徐升明王诠等先贤已穷尽天地精微  
  - 后学增补：今之后学加增旨意口诀为先贤馀意  
  - 编纂原则：合渊海渊源二书为一集，删繁去简永为矜式

- **详细解说**：  《会要命书说》为全书总结与编纂说明。**命书传承**——"造命书先贤已穷尽天地精微之蕴而极矣"揭示命书理论已完备；"自唐李虚中一行禅师、宋徐升东斋、明王诠醉醒子诸公"列举传承脉络。**渊海渊源**——"登觉渊海渊源其理雷同至矣尽矣，无非木火土金水之微妙耳"阐明两书理同已尽。**后学增补**——"今之后学加增旨意口诀，莫非先贤已发之馀意大同小异"说明后学贡献。**编纂原则**——"今将渊海渊源二书合成一集，一览便知，不必寻究二书之旨，删繁去简，永为矜式"点明编纂方法与目标。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_525]` `[trigger: 命书传承]` `[factor_trigger: mingshu_xianxian_qiongjin AND tiandi_jingwei_zhiyun AND muhuotujinshui]` `[role: 主干]` 造命书先贤已穷尽天地精微之蕴而极矣；命书理论已完备。 → 《渊海子平·会要命书说》
  - `[ns_yhzp_526]` `[trigger: 传承脉络]` `[factor_trigger: tang_lixuzhong_yixing AND song_xusheng_dongzhai AND ming_wangquan_zuixingzi AND lixuzhong_yixing]` `[role: 主干依赖]` 自唐李虚中一行禅师宋徐升东斋明王诠醉醒子诸公；命书传承脉络。 → 《渊海子平·会要命书说》
  - `[ns_yhzp_527]` `[trigger: 渊海渊源]` `[factor_trigger: yuanhai_yuanyuan_litong AND muhuotujinshui_zhimiao]` `[role: 条件分支]` 登觉渊海渊源其理雷同至矣尽矣；无非木火土金水之微妙耳。 → 《渊海子平·会要命书说》
  - `[ns_yhzp_528]` `[trigger: 后学增补]` `[factor_trigger: houxue_jiazeng_zhiyi_koujue AND xianxian_yifa_datong_xiaoyi AND houxue_jiazeng]` `[role: 条件分支]` 今之后学加增旨意口诀；莫非先贤已发之馀意大同小异。 → 《渊海子平·会要命书说》
  - `[ns_yhzp_529]` `[trigger: 合二为一]` `[factor_trigger: yuanhai_yuanyuan_hechengyiji AND yilan_bianzhi]` `[role: 条件分支]` 今将渊海渊源二书合成一集一览便知；编纂方法。 → 《渊海子平·会要命书说》
  - `[ns_yhzp_530]` `[trigger: 删繁去简]` `[factor_trigger: shanfan_qujian AND yongwei_jinshi AND bianzuan_mubiao]` `[role: 总结]` 删繁去简永为矜式；编纂目标与定位。 → 《渊海子平·会要命书说》"""
    normalized_text_zh: str = """"""
    subject: str = "会要命书说"
    factor_refs: list = ['essentials_statement', 'exhausted_essences', 'yuanhai_yuanyuan', 'eliminate_retain', 'eternal_exemplar']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_会要命书说_001_L1",
    )
    version: str = "1.0.0"
