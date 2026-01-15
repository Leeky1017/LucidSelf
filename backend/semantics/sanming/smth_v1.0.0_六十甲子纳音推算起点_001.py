"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228029
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
    semantic_id="smth_v1.0.0_六十甲子纳音推算起点_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六十甲子纳音推算起点(SemanticEntry):
    """
    - **原文（source_text）**：
  自甲子为首，以六甲五子次第推排，而尽于癸亥，仍以干枝本数而计其成数，总其成数干枝若干，然后以五数除之，遇其有剩者，约之以生五行之音，是为六甲纳音。

...
    """
    
    original_text: str = """- **原文（source_text）**：
  自甲子为首，以六甲五子次第推排，而尽于癸亥，仍以干枝本数而计其成数，总其成数干枝若干，然后以五数除之，遇其有剩者，约之以生五行之音，是为六甲纳音。

- **分字分词释义**：
  - **六甲五子**：六个甲日和五个子日。
  - **次第推排**：依次排列。
  - **干枝本数**：天干地支的本来数字。
  - **计其成数**：计算其成就之数。
  - **总其成数**：总计成数。
  - **以五数除之**：用五来除。
  - **遇其有剩**：遇到有余数。
  - **约之以生**：约定以生。
  - **六甲纳音**：六十甲子的纳音。

- **规范化释义（primary_lang_explained）**：
  从甲子开始，以六个甲和五个子依次排列，一直到癸亥，然后用天干地支的本来数字计算其成数，总计干支的成数有多少，然后用五来除，遇到有余数的，约定用来生五行之音，这就是六十甲子的纳音。

- **完整对等诠释（secondary_lang_full）**：
  Starting from Jiazi, using six Jias and five Zis arranged in sequence until reaching Guihai, then using the original numbers of Stems and Branches to calculate their completion numbers, totaling how many completion numbers the Stems and Branches have, then dividing by five—when there are remainders, these are designated to generate the sounds of the Five Elements. This is the Nayin of Sixty Jiazi.

- **核心要点**：
  - 从甲子开始排列到癸亥
  - 用干支本数计算成数
  - 总计成数后以五除之
  - 余数对应五行之音
  - 形成六十甲子纳音体系

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_163]` `[trigger: 六十甲子纳音推算]` `[factor_trigger: sixty_jiazi AND nayin_calculation AND five_elements_sounds]` `[role: 主干]` 自甲子为首，以六甲五子次第推排，而尽于癸亥，以五数除之，遍其有剩者，约之以生五行之音，是为六甲纳音。 → 《三命通会》卷一#六十甲子纳音推算起点

- **详细解说**：
  此条说明六十甲子纳音的基本推算方法。从甲子开始，按六甲（甲子、甲寅、甲辰、甲午、甲申、甲戌）和五子（子、寅、辰、午、申）的规律依次排列，直到第60个癸亥。每个干支组合都有对应的数字（天干甲1乙2...癸10，地支子1丑2...亥12），将干支数字相加得成数，再用5除，余数对应五行（1水2火3木4金5土），由此确定该干支的纳音五行。这是纳音推算的起点和基本原理，后文将详细展开各种纳音理论。

- **校勘与字词辨析（双语）**：
  - **中文**："六甲"指甲子、甲寅、甲辰、甲午、甲申、甲戌。"五子"指子、寅、辰、午、申五个阳支。
  - **English**: "Six Jias" refers to Jiazi, Jiayin, Jiachen, Jiawu, Jiashen, Jiaxu; "Five Zis" refers to five yang Branches: Zi, Yin, Chen, Wu, Shen."""
    normalized_text_zh: str = """"""
    subject: str = "六十甲子纳音推算起点"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_六十甲子纳音推算起点_001_L1",
    )
    version: str = "1.0.0"
