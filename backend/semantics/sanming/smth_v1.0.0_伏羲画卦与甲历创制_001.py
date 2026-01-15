"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227867
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
    semantic_id="smth_v1.0.0_伏羲画卦与甲历创制_001",
    book_id="sanming",
    engine_id="bazi"
)
class 伏羲画卦与甲历创制(SemanticEntry):
    """
    - **原文（source_text）**：
  至于伏羲，仰观象于天，俯观法于地，中观万物与人，始画八卦，以通神明之德，以类万物之情，以作甲历，而文字生焉。

- **分字分词释义**：
  - *...
    """
    
    original_text: str = """- **原文（source_text）**：
  至于伏羲，仰观象于天，俯观法于地，中观万物与人，始画八卦，以通神明之德，以类万物之情，以作甲历，而文字生焉。

- **分字分词释义**：
  - **仰观象于天**：抬头观察天象。
  - **俯观法于地**：低头观察地理。
  - **中观万物与人**：观察万物与人的关系。
  - **画八卦**：创制八卦。
  - **通神明之德**：沟通神明的德性。
  - **类万物之情**：归类万物的情状。
  - **作甲历**：创制甲历（历法）。

- **规范化释义（primary_lang_explained）**：
  到了伏羲氏，仰头观察天象，俯身观察地理，观察万物与人的关系，开始画出八卦，用来沟通神明的德性，归类万物的情状，创制甲历，从此文字产生。

- **完整对等诠释（secondary_lang_full）**：
  By the time of Fuxi, he observed celestial phenomena above, examined earthly patterns below, and studied the relationships between myriad things and humanity. He first drew the Eight Trigrams to communicate with spiritual virtue and to categorize the conditions of all things. He created the Jia Calendar, and from this, written characters emerged.

- **核心要点**：
  - 伏羲三观：仰观天象、俯观地理、中观万物与人
  - 伏羲画八卦，用于沟通神明、归类万物
  - 伏羲创制甲历（历法系统）
  - 文字从此产生

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_141]` `[trigger: 伏羲画卦制历]` `[factor_trigger: fuxi AND bagua AND jia_calendar]` `[role: 主干]` 至于伏羲，仰观象于天，俯观法于地，中观万物与人，始画八卦，以通神明之德，以类万物之情，以作甲历，而文字生焉。 → 《三命通会》卷一#伏羲画卦与甲历创制

- **详细解说**：
  此条讲述伏羲对干支历法体系的重要贡献。伏羲采用"三观"方法：仰观天象（天文）、俯观地理（地理）、中观万物与人（人事），建立了完整的天地人认知体系。在此基础上画出八卦，作为沟通神明德性、归类万物情状的工具。更重要的是创制甲历，这是中国历法体系的开端。文字也随之产生，标志着从口传到文字记录的文明飞跃。伏羲的贡献在于将干支系统从单纯的时间标记提升为包含天地人三才、涵盖八卦象数的完整体系。

- **校勘与字词辨析（双语）**：
  - **中文**："甲历"即以甲子为首的历法体系。"神明之德"指天地自然规律的神圣性。
  - **English**: "Jia Calendar" refers to the calendar system starting with Jiazi; "spiritual virtue" denotes the sacred patterns of heaven and earth."""
    normalized_text_zh: str = """"""
    subject: str = "伏羲画卦与甲历创制"
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
        l1_anchor="smth_v1.0.0_伏羲画卦与甲历创制_001_L1",
    )
    version: str = "1.0.0"
