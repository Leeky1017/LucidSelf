"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.795225
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
    semantic_id="mlxj_v1.0.0_1_桌椅凳抬_家伙类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1桌椅凳抬家伙类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

古者席地而坐，引几而竟。至于楚汉，驾木为桌，斲木为椅，迄今晋魏之制，乡居旅邸，桌凳森列，或游戏于山林苑囿之中，布席于地而坐者，则效太古之遗风。梦此二者皆为嘉...
    """
    
    original_text: str = """#### 原文（source_text）

古者席地而坐，引几而竟。至于楚汉，驾木为桌，斲木为椅，迄今晋魏之制，乡居旅邸，桌凳森列，或游戏于山林苑囿之中，布席于地而坐者，则效太古之遗风。梦此二者皆为嘉祥之兆。桌者，高抬之意；卓者，有所立之谓也；椅者，依椅之称；凳者，为登、为等、为顿，为安居高坐，为舟车坛阘中正物，为知止能定也。

#### 规范化释义（primary_lang_explained）

古人席地而坐，引几案而从事。到了楚汉时期，架木为桌，斲木为椅。至今晋魏制度延续，乡间旅邸桌凳排列。或游戏于山林苑囿中布席于地而坐，则是效仿太古遗风。

梦见桌椅凳，皆为嘉祥之兆：
- **桌**：高抬之意
- **卓**：有所立之谓
- **椅**：依倚之称
- **凳**：登、等、顿，安居高坐，知止能定

#### 完整对等诠释（secondary_lang_full）

Ancients sat on mats on the ground, drawing side tables for work. From Chu-Han times, wood was fashioned into tables and chairs. The Jin-Wei system continues today with tables and benches arrayed in villages and inns. Those who spread mats in forests and gardens follow ancient customs.

Dreaming of tables and chairs are all auspicious omens:
- **Table (zhuo)**: meaning elevation
- **Tall (zhuo)**: having something established
- **Chair (yi)**: meaning to lean upon
- **Stool (deng)**: ascending, equaling, pausing—sitting in peace, knowing when to stop

#### 核心要点

- 桌椅凳=嘉祥之兆
- 桌=高抬=提升
- 椅=依倚=依靠
- 凳=登等顿=安居、知止能定
- 位置象征：天际→朝皇，云中→登第，舟中→远行

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v13_001]` `[trigger: 什物梦象]` `[factor_trigger: weizhi AND dream_zhuoyideng]` `[role: 什物类]` 位置、桌椅凳等什物梦象。 → 《梦林玄解·卷十三》#什物"""
    normalized_text_zh: str = """"""
    subject: str = "1 桌椅凳抬（家伙类首条·完整精校）"
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_1_桌椅凳抬_家伙类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
