"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997769
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
    semantic_id="dts_v1.0.0_秀才不是尘凡子_清气只嫌官不起_001",
    book_id="dts",
    engine_id="bazi"
)
class 秀才不是尘凡子清气只嫌官不起(SemanticEntry):
    """
    - **原文（source_text）**：
  秀才不是尘凡子，清气只嫌官不起。

- 原注（原文注解）：
 　　秀才之命多有清气，但官星不起，故无爵禄。

- 分字分词释义：
  - 秀才：有学问...
    """
    
    original_text: str = """- **原文（source_text）**：
  秀才不是尘凡子，清气只嫌官不起。

- 原注（原文注解）：
 　　秀才之命多有清气，但官星不起，故无爵禄。

- 分字分词释义：
  - 秀才：有学问但未入仕之人。
  - 尘凡子：普通凡俗之人。
  - 清气：命局清雅之气。
  - 官不起：官星无力、难以入仕。

- 规范化释义（primary_lang_explained）：
  所谓“秀才命”，往往文章清雅、气质不俗，自有一股超出凡庸的清气，只是官星无力、仕途不显，终究难得实在爵禄，多见“有才无位”“有名无官”之象。

- **核心要点**：
  - 清气足而官星不起，是“秀才命”的典型结构；
  - 人品学识可佳，现实权位与俸禄却有限；
  - 宜顺势把清气用在学术、教化或自由职业，而不强求官途。

- 详细解说：
  本句将一种常见格局单独拎出：印比清纯、食伤亦能生发文采，却缺乏有力之官星承接，或官星受制、受损，导致清气只能停留在学问与气度层面，难以化成稳定的公职地位。若执着仕途，往往屡试不第或位卑权轻；若能转向教书、著述、专业自由等路径，则更能安顿这股不凡之气。命理上判断此类命局时，要区分“读书有成”与“科第有成”两层，不可混为一谈。

- 校勘与字词辨析：
  - “秀才”：此处泛指有文才、有清气而官不显者，并不限于科举制度下的具体身份。

- **次语种完整诠释（secondary_lang_full）**:
  Xiucai秀才 not-mortal不是尘凡子: clear-qi清气 only-fears只嫌 official-not-rise官不起—scholar-fate学业命 needs清气 clear-energy but官星 official-star must-rise须起 otherwise否则 only-scholar仅秀才 not-higher不更上."""
    normalized_text_zh: str = """"""
    subject: str = "秀才不是尘凡子，清气只嫌官不起。"
    factor_refs: list = ['keju_xiucai_grade', 'common_mortal', 'qingqi', 'official_star_weak', 'keju_rank']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_秀才不是尘凡子_清气只嫌官不起_001_L1",
    )
    version: str = "1.0.0"
