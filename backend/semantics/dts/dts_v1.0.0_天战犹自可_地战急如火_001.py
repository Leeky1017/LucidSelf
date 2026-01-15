"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997630
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
    semantic_id="dts_v1.0.0_天战犹自可_地战急如火_001",
    book_id="dts",
    engine_id="bazi"
)
class 天战犹自可地战急如火(SemanticEntry):
    """
    - **原文（source_text）**：
  天战犹自可，地战急如火。

- 原注（原文注解）：
  　　天干遇甲庚、乙辛，谓之天战，而得地顺静者无害。支寅申、卯酉，谓之地战，则干不能为力，其势速...
    """
    
    original_text: str = """- **原文（source_text）**：
  天战犹自可，地战急如火。

- 原注（原文注解）：
  　　天干遇甲庚、乙辛，谓之天战，而得地顺静者无害。支寅申、卯酉，谓之地战，则干不能为力，其势速凶。盖天主动，地主静故也。如庚申、甲寅、乙卯、辛酉之类，皆见者，谓之天地交战，必凶无疑。遇运岁合之会之，视其胜负，亦有可存可发者。其有两冲者，只得一个合神有力，或会神，或库神，或贵神，以收其动气，息其争气，亦有佳者。至于喜神伏藏死绝者，又要冲动，引用生发之气。

- **规范化释义（primary_lang_explained）**：
  天干之战可缓，地支之战急迫。天地交战最凶，惟有强合、会、库、贵神能收其动气。若喜神伏绝，反需“冲而引生”。

- 分字分词释义：
  - 天战：天干相战（甲庚、乙辛）。
  - 地战：地支相战（寅申、卯酉）。
  - 交战：干支同时构成战局。
  - 收动气：以合/会/库/贵收敛动荡之气。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 战合 | Battle-Combine (Zhan-He) | 征战与合化 | Conflict and harmony | zhanhe | existing |
| 天战 | Heaven Battle (Tian-Zhan) | 天干相战 | Heavenly Stem clash | tianzhan | new_candidate |
| 地战 | Earth Battle (Di-Zhan) | 地支相战 | Earthly Branch clash | dizhan | new_candidate |
| 急如火 | Urgent as Fire | 势态急迫 | Critical urgency | jiruhuo | new_candidate |
| 收动气 | Collect Moving Qi | 收敛动气 | Absorb active Qi | shoudongqi | new_candidate |
| 天地交战 | Heaven-Earth Combined Battle | 干支俱战 | Total conflict | tiandi_jiaozhan | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Zhan-He (Battle-Combine) theory: Heaven Battle (Tian-Zhan) is manageable (You-Zi-Ke), Earth Battle (Di-Zhan) is urgent (Ji-Ru-Huo). Heaven-Earth Combined Battle (Tian-Di Jiao-Zhan) is most dangerous. Must use Combination (He), Meeting (Hui), Treasury (Ku), or Noble (Gui) to Collect the Moving Qi (Shou-Dong-Qi). If Happy God is buried/dead, use clash to activate, then combine to collect."""
    normalized_text_zh: str = """"""
    subject: str = "天战犹自可，地战急如火。"
    factor_refs: list = []
    
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
        l1_anchor="dts_v1.0.0_天战犹自可_地战急如火_001_L1",
    )
    version: str = "1.0.0"
