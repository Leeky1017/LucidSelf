"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227927
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
    semantic_id="smth_v1.0.0_甲乙木之义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 甲乙木之义(SemanticEntry):
    """
    - **原文（source_text）**：
  是以东方甲乙，南方丙丁，西方庚辛，北方壬癸，中央戊己，五行之位也。盖甲乙其位，木，得春之令，甲乃阳内而阴尚包之，草木始甲而出也。乙者，阳过中，然未得正...
    """
    
    original_text: str = """- **原文（source_text）**：
  是以东方甲乙，南方丙丁，西方庚辛，北方壬癸，中央戊己，五行之位也。盖甲乙其位，木，得春之令，甲乃阳内而阴尚包之，草木始甲而出也。乙者，阳过中，然未得正方，尚乙屈也。又云：乙，轧也，万物皆解莩甲，自抽轧而出之。

- **分字分词释义**：
  - **东方甲乙**：甲乙属木，位居东方。
  - **阳内而阴尚包之**：阳气在内，阴气尚包裹之。
  - **草木始甲**：草木开始破壳而出。
  - **阳过中**：阳气过半。
  - **未得正方**：尚未到达正位。
  - **乙屈**：弯曲屈折之状。
  - **轧**：压出、挤出。
  - **解莩甲**：解开种子的外壳。
  - **抽轧**：抽出、挤出。

- **规范化释义（primary_lang_explained）**：
  东方为甲乙木，南方为丙丁火，西方为庚辛金，北方为壬癸水，中央为戊己土，这是五行的方位。甲乙的位置属木，得春季之令。甲为阳气在内而阴气还包裹着，草木开始破甲而出。乙是阳气过半，但还未到达正位，仍处于弯曲屈折的状态。又说：乙就是"轧"，万物都解开种子的外壳，自己挤压而出。

- **完整对等诠释（secondary_lang_full）**：
  East corresponds to Jia-Yi Wood, South to Bing-Ding Fire, West to Geng-Xin Metal, North to Ren-Gui Water, Center to Wu-Ji Earth—these are the Five Elements' directional positions. Jia and Yi occupy the Wood position, commanding Spring's decree. Jia represents yang qi contained within while yin qi still envelops it—vegetation begins to break through its armor. Yi represents yang qi surpassing midpoint yet not reaching proper position, still in a bent and folded state. It is also said: Yi means "rolling out"—myriad things shed their seed coats and press themselves outward.

- **核心要点**：
  - 十干配五方：东甲乙木、南丙丁火、西庚辛金、北壬癸水、中戊己土
  - 甲木：阳内阴包，草木始甲而出
  - 乙木：阳过中但未正，状如屈折
  - 乙为"轧"，万物解壳抽出

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_149]` `[trigger: 甲乙木之义]` `[factor_trigger: jia_wood AND yi_wood AND element_wood]` `[role: 主干]` 甲乃阳内而阴尚包之，草木始甲而出也。乙者，阳过中，然未得正方，尚乙屈也。乙，轧也，万物皆解莙甲，自抽轧而出之。 → 《三命通会》卷一#甲乙木之义

- **详细解说**：
  此条详解甲乙木之义。首先明确十干的五行方位配属。甲木为阳木，春初之时阳气刚从内部萌发，外面还被阴气包裹，就像草木种子破壳而出，称为"始甲"。乙木为阴木，阳气已过半但尚未到达完全伸展的正位，仍处于弯曲屈折状态，如同幼苗刚出土时的弯曲形态。"乙，轧也"是从字义训诂，"轧"指挤压而出，形容万物从种子外壳中挤压抽出的过程。这体现了甲乙木从萌芽（甲）到初长（乙）的两个阶段。

- **校勘与字词辨析（双语）**：
  - **中文**："莩甲"指种子的外壳。"轧"读yà，挤压之意。"阳内阴包"指阳气在内、阴气在外的状态。
  - **English**: "莩甲" (seed coat) refers to the outer shell of seeds; "轧" (yà, rolling/pressing) means to squeeze or press; "yang within, yin enveloping" describes the state of yang qi inside with yin qi outside."""
    normalized_text_zh: str = """"""
    subject: str = "甲乙木之义"
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
        l1_anchor="smth_v1.0.0_甲乙木之义_001_L1",
    )
    version: str = "1.0.0"
