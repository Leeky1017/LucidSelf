"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228102
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
    semantic_id="smth_v1.0.0_太玄数推算法_001",
    book_id="sanming",
    engine_id="bazi"
)
class 太玄数推算法(SemanticEntry):
    """
    - **原文（source_text）**：
  再考太玄数如何，以甲己子午为九数。盖万物者，本乎天地，运乎四时。春以万物滋长于艮，秋以万物凋零于坤，生发归藏，莫离于土。土者，坤、艮也。易曰：艮乃生物...
    """
    
    original_text: str = """- **原文（source_text）**：
  再考太玄数如何，以甲己子午为九数。盖万物者，本乎天地，运乎四时。春以万物滋长于艮，秋以万物凋零于坤，生发归藏，莫离于土。土者，坤、艮也。易曰：艮乃生物之始，坤乃成物之终。甲，天干之首，子地支之首，二义之循环，一阳之来复，故甲子起于天地之数是也。

- **分字分词释义**：
  - **太玄数**：太玄经的数理。
  - **甲己子午为九数**：甲己子午都为九。
  - **本乎天地运乎四时**：根本在天地运行在四季。
  - **生发归藏**：生长发育归藏潜伏。
  - **艮乃生物之始**：艮卦是生物开始。
  - **坤乃成物之终**：坤卦是成物结束。
  - **二义之循环**：两种意义的循环。
  - **一阳来复**：复卦一阳初生。

- **规范化释义（primary_lang_explained）**：
  再考察太玄数是如何的，以甲己子午为九数。万物根本在天地，运行在四季。春季万物在艮卦滋长，秋季万物在坤卦凋零，生长发育和归藏潜伏，都不离开土。土就是坤卦和艮卦。《易经》说：艮卦是生物的开始，坤卦是成物的结束。甲是天干之首，子是地支之首，两种意义循环，一阳来复，所以甲子起于天地之数。

- **完整对等诠释（secondary_lang_full）**：
  Examining further the Taixuan numbers: Jia-Ji and Zi-Wu are nine numbers. Myriad things are rooted in Heaven-Earth, operating through the four seasons. In spring, myriad things grow and flourish at Gen; in autumn, myriad things wither at Kun—generation-development and return-storage all remain within Earth. Earth is Kun and Gen. The Yi states: Gen is the beginning of generating things, Kun is the completion of forming things. Jia is the head of Heavenly Stems, Zi is the head of Earthly Branches—the two meanings cycle, one yang returns (Fu hexagram), thus Jiazi arises from Heaven-Earth's numbers.

- **核心要点**：
  - 太玄数：甲己子午为九
  - 万物本天地，运四时
  - 春生于艮，秋藏于坤
  - 艮为生始，坤为成终
  - 甲子为天干地支之首，循环复始

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_172]` `[trigger: 太玄数推算法]` `[factor_trigger: taixuan_numbers AND gen_kun AND four_seasons]` `[role: 主干]` 太玄数以甲己子午为九数。万物者，本乎天地，运乎四时。春以万物滋长于艮，秋以万物凋零于坤。艮乃生物之始，坤乃成物之终。 → 《三命通会》卷一#太玄数推算法

- **详细解说**：
  此条介绍太玄数推算法的哲学基础。太玄数以甲己和子午都配九数，体现天地循环。万物根本在天地，运行遵循四季规律。春季万物在艮卦（东北，生发之位）滋长，秋季在坤卦（西南，收藏之位）凋零，生发归藏都离不开"土"（坤艮都属土）。《易经》说艮为万物生成的起点，坤为万物完成的终点。甲为天干之首，子为地支之首，两者结合形成循环体系，就像复卦一阳来复，阳气初生。因此甲子作为干支组合的起点，蕴含天地之数的深层意义。这是太玄数理论的哲学根基。

- **校勘与字词辨析（双语）**：
  - **中文**：《太玄经》为西汉扬雄撰。艮卦在东北，主春季生发；坤卦在西南，主秋季收藏。"一阳来复"指复卦。
  - **English**: "Taixuan Jing" (Classic of Supreme Mystery) was written by Yang Xiong in Western Han; Gen hexagram in northeast governs spring generation; Kun hexagram in southwest governs autumn storage; "one yang returns" refers to Fu hexagram."""
    normalized_text_zh: str = """"""
    subject: str = "太玄数推算法"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_太玄数推算法_001_L1",
    )
    version: str = "1.0.0"
