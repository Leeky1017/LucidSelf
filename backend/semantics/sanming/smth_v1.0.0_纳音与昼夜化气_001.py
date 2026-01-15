"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264482
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
    semantic_id="smth_v1.0.0_纳音与昼夜化气_001",
    book_id="sanming",
    engine_id="bazi"
)
class 纳音与昼夜化气(SemanticEntry):
    """
    - **原文（source_text）**：
  凡命有五行相克，如壬水克丙火，名鬼。若壬水有纳音是木，丙火纳音是水，则水生木，名鬼变财（应为鬼化为印？或指水克火为财？纳音木生火？原文注：壬水纳音木，...
    """
    
    original_text: str = """- **原文（source_text）**：
  凡命有五行相克，如壬水克丙火，名鬼。若壬水有纳音是木，丙火纳音是水，则水生木，名鬼变财（应为鬼化为印？或指水克火为财？纳音木生火？原文注：壬水纳音木，丙火纳音水，水生木，则壬不受丙之制，反受生）。
  凡看命，五行错陈，本无定法。先看子平，次推五行。
  凡看命，要论五行昼夜。甲乙属木，昼生为刚，夜生为柔。丙丁属火，昼生为刚，夜生为柔（注：日生阳木，夜生阴木？或指气势）。
  凡人问寿，专看冲化。有化神，虽冲无灾。
  凡命有合干，不可见煞。如甲乙木，见庚辛金，是煞。
  
- **分字分词释义**：
  - **纳音救应**：正五行相克，纳音相生，可解。
  - **昼夜刚柔**：阳干昼生刚，夜生柔（或反之，视具体五行）。
  - **冲化**：有冲有合（化）。
  - **合干见煞**：化气格见克神（如甲己化土，见乙木克土，或见庚金合甲争合）。

- **白话原意**：
  命局中如果有正五行相克（如壬克丙），本是七煞（鬼）。但如果壬水的纳音是木（如壬子桑柘木），丙火的纳音是水（如丙子涧下水），纳音变成水生木，鬼（壬）反而受生于被克者（丙），或者转化为有情关系。
  看命没有定法，五行错综复杂。先用子平法（正五行）看，再用纳音五行参考。
  五行要分昼夜。甲乙木昼生刚健，夜生柔顺；丙丁火亦然。
  看寿命，专看冲化。如果有化神（合局），即使有冲，也往往无灾（贪合忘冲）。
  化气格（合干）不可见煞。如甲己化土，怕见乙木（煞）。

- **核心要点**：
  - **纳音补救**：正五行克，纳音生可解。
  - **昼夜之别**：刚柔不同。
  - **冲化解灾**：合能解冲。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_nayin_001]` `[trigger: 纳音救应]` `[factor_trigger: nayin_jiuying AND zhengke_nayinsheng]` `[role: 主干]` 凡命有五行相克，如壬水克丙火名鬼，若壬水纳音是木，丙火纳音是水，则水生木，名鬼变财。 → 《三命通会》卷十#纳音与昼夜化气
  - `[ns_smth_10_nayin_002]` `[trigger: 昼夜刚柔]` `[factor_trigger: zhouye_gangrou AND jiayimu_gangshou]` `[role: 主干依赖]` 凡看命，要论五行昼夜，甲乙属木，昼生为刚，夜生为柔。 → 《三命通会》卷十#纳音与昼夜化气
  - `[ns_smth_10_nayin_003]` `[trigger: 冲化解灾]` `[factor_trigger: chonghua_jiezai AND tanhe_wangchong]` `[role: 总结]` 凡人问寿，专看冲化，有化神虽冲无灾。 → 《三命通会》卷十#纳音与昼夜化气"""
    normalized_text_zh: str = """"""
    subject: str = "纳音与昼夜化气"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_纳音与昼夜化气_001_L1",
    )
    version: str = "1.0.0"
