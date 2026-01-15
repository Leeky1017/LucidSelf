"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997781
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
    semantic_id="dts_v1.0.0_台阁勋劳百世传_天然清气显机权_001",
    book_id="dts",
    engine_id="bazi"
)
class 台阁勋劳百世传天然清气显机权(SemanticEntry):
    """
    - **原文（source_text）**：
  台阁勋劳百世传，天然清气显机权。

- 原注（原文注解）：
 　　公卿之任，清中见权。

- 分字分词释义：
  - 台阁：中枢高官、内阁重臣。
  ...
    """
    
    original_text: str = """- **原文（source_text）**：
  台阁勋劳百世传，天然清气显机权。

- 原注（原文注解）：
 　　公卿之任，清中见权。

- 分字分词释义：
  - 台阁：中枢高官、内阁重臣。
  - 勋劳：功勋与劳绩。
  - 百世传：声名流传后世。
  - 天然清气：先天具备的清雅之气。
  - 显机权：显现决策权力。

- 规范化释义（primary_lang_explained）：
  此条描写“台阁之任”：命局清而不浊，又能见到实在之权柄——官星有位、有印卫、有财生，既有清名又握实权，所立勋劳足以流传后世。

- **核心要点**：
  - “清中见权”：清气为体，权柄为用；
  - 官印得位、财官有序，能立大勋；
  - 地位高且可久传，而非一时虚名。

- 详细解说：
  “台阁”象征中枢要职，“勋劳百世传”强调其功绩与位阶皆可传诸久远。命理上，这类格局往往具备：一则官星清正，不受杂煞浊气侵染；二则有印以护官，有财以通官，使权力有根有源，而非空悬之权。若再配合同气之岁运相生相扶，则容易在制度与结构中居于决策中枢，所建功业对族群或组织具有长期影响。

- 校勘与字词辨析：
  - “台阁”：原指朝廷重臣之所居，引申为中枢高位；
  - “机权”：机务与权柄，偏重实际决断力，而非仅有虚衔。

- **次语种完整诠释（secondary_lang_full）**:
  Cabinet-hall台阁 meritorious-service勋劳 hundred-generations百世传: natural-clear-qi天然清气 reveals-authority显机权—highest-official最高官 requires天然 innate清气 clear-energy plus机权 strategic-authority隐显兼备."""
    normalized_text_zh: str = """"""
    subject: str = "台阁勋劳百世传，天然清气显机权。"
    factor_refs: list = ['taige', 'xunlao', 'baishichuan', 'qingqi', 'jiquan']
    
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
        l1_anchor="dts_v1.0.0_台阁勋劳百世传_天然清气显机权_001_L1",
    )
    version: str = "1.0.0"
