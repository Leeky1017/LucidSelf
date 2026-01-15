"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228016
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
    semantic_id="smth_v1.0.0_陈抟论干支源于河洛_001",
    book_id="sanming",
    engine_id="bazi"
)
class 陈抟论干支源于河洛(SemanticEntry):
    """
    - **原文（source_text）**：
  陈抟曰：天干始于甲而终于癸，河图生成之数也；地支起于子而终于亥，洛书奇偶之数也。阳自复始，六变而乾阳备；阴自姤始，六变而坤阴成，合二六之数而为十二辰也...
    """
    
    original_text: str = """- **原文（source_text）**：
  陈抟曰：天干始于甲而终于癸，河图生成之数也；地支起于子而终于亥，洛书奇偶之数也。阳自复始，六变而乾阳备；阴自姤始，六变而坤阴成，合二六之数而为十二辰也。

- **分字分词释义**：
  - **河图生成之数**：河图中的生成数理。
  - **洛书奇偶之数**：洛书中的奇数偶数。
  - **复始**：复卦开始。
  - **六变**：六次变化。
  - **乾阳备**：乾卦纯阳完备。
  - **姤始**：姤卦开始。
  - **坤阴成**：坤卦纯阴完成。
  - **二六之数**：两个六的数。

- **规范化释义（primary_lang_explained）**：
  陈抟说：天干从甲开始到癸结束，是河图的生成之数；地支从子开始到亥结束，是洛书的奇偶之数。阳气从复卦开始，经过六次变化而乾卦纯阳完备；阴气从姤卦开始，经过六次变化而坤卦纯阴完成，合并两个六的数字而成为十二地支。

- **完整对等诠释（secondary_lang_full）**：
  Chen Tuan stated: The Heavenly Stems begin with Jia and end with Gui—these are the generative numbers of Hetu (River Chart). The Earthly Branches start with Zi and end with Hai—these are the odd-even numbers of Luoshu (Luo Writing). Yang begins from Fu hexagram, transforming six times until Qian yang is complete; yin begins from Gou hexagram, transforming six times until Kun yin is complete. Combining these two sixes forms the Twelve Branches.

- **核心要点**：
  - 天干源于河图生成之数
  - 地支源于洛书奇偶之数
  - 阳从复卦六变至乾卦纯阳
  - 阴从姤卦六变至坤卦纯阴
  - 二六合数成十二支

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_161]` `[trigger: 干支源于河洛]` `[factor_trigger: hetu_luoshu AND tiangan_dizhi AND hexagram_transformation]` `[role: 主干]` 天干始于甲而终于癸，河图生成之数也；地支起于子而终于亥，洛书奇偶之数也。 → 《三命通会》卷一#陈抟论干支源于河洛

- **详细解说**：
  此条引陈抟（宋代道士、易学家）论干支的易理基础。天干十数对应河图的生成之数（一六水、二七火、三八木、四九金、五十土），体现生成原理。地支十二数对应洛书的奇偶配置。从易卦角度，复卦（一阳初生）经六次阳长变化到乾卦（纯阳），对应阳支六个；姤卦（一阴初生）经六次阴长变化到坤卦（纯阴），对应阴支六个。两个六合成十二，形成十二地支体系。这将干支与河洛易理深度融合，赋予干支哲学和象数基础。

- **校勘与字词辨析（双语）**：
  - **中文**：陈抟（871-989），宋初道士、易学家。复卦为一阳五阴，姤卦为一阴五阳。乾卦纯阳，坤卦纯阴。
  - **English**: Chen Tuan (871-989 CE) was an early Song Dynasty Daoist and Yi scholar; Fu hexagram has one yang and five yin; Gou hexagram has one yin and five yang; Qian is pure yang, Kun is pure yin."""
    normalized_text_zh: str = """"""
    subject: str = "陈抟论干支源于河洛"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_陈抟论干支源于河洛_001_L1",
    )
    version: str = "1.0.0"
