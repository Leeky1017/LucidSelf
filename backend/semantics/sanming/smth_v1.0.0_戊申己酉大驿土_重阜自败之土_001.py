"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228652
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
    semantic_id="smth_v1.0.0_戊申己酉大驿土_重阜自败之土_001",
    book_id="sanming",
    engine_id="bazi"
)
class 戊申己酉大驿土重阜自败之土(SemanticEntry):
    """
    - **原文（source_text）**：
  戊申重阜之土，木绝于申，不能克，若见金水多助，则富贵尊荣之格也。己酉自败之土，其气不足，藉火以相助之。见丁卯、丁酉火则吉，切忌死绝，畏辛卯、辛酉木，灾...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊申重阜之土，木绝于申，不能克，若见金水多助，则富贵尊荣之格也。己酉自败之土，其气不足，藉火以相助之。见丁卯、丁酉火则吉，切忌死绝，畏辛卯、辛酉木，灾蹇夭折。

- **分字分词释义**：
  - **重阜之土**：重叠高厚的土。
  - **木绝于申**：木在申位绝灭。
  - **金水多助**：金水众多帮助。
  - **富贵尊荣**：富贵尊贵荣耀。
  - **自败之土**：自己败落的土。
  - **其气不足**：其气不够充足。
  - **藉火相助**：依靠火来相助。
  - **切忌死绝**：切记忌讳死绝。
  - **灾蹇夭折**：灾难困顿短命。

- **规范化释义（primary_lang_explained）**：
  戊申是重叠高厚的土，木在申位绝灭，不能克制。如果见到金水众多帮助，就是富贵尊贵荣耀的格局。己酉是自败的土，其气不够充足，依靠火来相助。见到丁卯、丁酉火就吉利，切记忌讳死绝，畏惧辛卯、辛酉木，会有灾难困顿短命。

- **完整对等诠释（secondary_lang_full）**：
  Wushen is layered-mound earth, wood extinct at Shen, cannot overcome. If seeing Metal-Water abundantly assisting, then wealth-nobility honored-glory pattern. Jiyou is self-defeated earth, its energy insufficient, relying on Fire mutually-assisting. Seeing Dingmao, Dingyou Fire then auspicious, absolutely avoid dead-extinct, fears Xinmao, Xinyou Wood, disaster-obstruction premature-death.

- **核心要点**：
  - 戊申为大驿土，重阜之土
  - 木绝于申不能克
  - 见金水多助富贵尊荣
  - 己酉自败之土气不足
  - 藉火相助、见特定火吉
  - 忌死绝、畏特定木灾蹇夭折

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_239]` `[trigger: 戊申己酉土性质]` `[factor_trigger: wushen_layered_mound_earth AND jiyou_self_defeated_earth AND fire_assists_water_metal_helps]` `[role: 主干]` 戊申重阜之土，木绝于申，不能克，若见金水多助，则富贵尊荣之格也。己酉自败之土，其气不足，藉火以相助之。见丁卯、丁酉火则吉，切忌死绝，畏辛卯、辛酉木，灾蹇夭折。 → 《三命通会》卷一#戊申己酉土性质

- **详细解说**：
  此条详论戊申、己酉（大驿土）的性质。戊申是重阜之土（厚重高大），木绝于申不能克，见金水多助（金生水、水润土）则富贵尊荣。己酉是自败之土（酉为土败地），气不足需火相助（火生土），见丁卯（炉中火）、丁酉（山下火）吉，但忌死绝，畏辛卯（松柏木）、辛酉（石榴木）等木克则灾蹇夭折。这是论述厚土与败土的不同特性。

- **校勘与字词辨析（双语）**：
  - **中文**："重阜"指高大厚重的土丘。"木绝于申"，申为木绝地。"自败"指酉为土败地。"灾蹇"指灾难困顿。
  - **English**: "Layered-mound" means tall and thick earth mound. "Wood extinct at Shen" means Shen is wood's extinction position. "Self-defeated" means You is earth's defeat position. "Disaster-obstruction" means calamity and difficulty."""
    normalized_text_zh: str = """"""
    subject: str = "戊申己酉大驿土：重阜自败之土"
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
        l1_anchor="smth_v1.0.0_戊申己酉大驿土_重阜自败之土_001_L1",
    )
    version: str = "1.0.0"
