"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997393
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
    semantic_id="dts_v1.0.0_伤官见官果难辨_可见不可见_001",
    book_id="dts",
    engine_id="bazi"
)
class 伤官见官果难辨可见不可见(SemanticEntry):
    """
    - **原文（source_text）**：
  伤官见官果难辨，可见不可见。

- 原注（原文注解）：
  　　身弱而伤官旺者，见印而可见官，官以生印，印以扶身也，身旺而伤官旺者，见财而可见官，以财...
    """
    
    original_text: str = """- **原文（source_text）**：
  伤官见官果难辨，可见不可见。

- 原注（原文注解）：
  　　身弱而伤官旺者，见印而可见官，官以生印，印以扶身也，身旺而伤官旺者，见财而可见官，以财生官，且以财泄伤也，伤官旺，财神轻，有比劫而可见官，（官以制劫）日主旺，伤官轻，无印绶而可见官，（伤轻不能害官，无印则官不能印克伤。）伤官旺而无财，一遇官而有祸，（官必遇害）。
  　　伤官旺而身弱，一见官而有祸，（官能克身）。伤官弱而见印，一见官而有祸，（助印克伤）。大抵伤官有财，皆可见官，伤官无财，皆不可见官，又要看身强身弱，不必分金木水火土也，又日伤官用印，无财不宜见财，（身弱用印，见财破印）。伤用财，无印不宜见印，（身旺用财，见印则克伤，战财）。须详辨之。

- 分字分词释义：
  - 伤官：我所生而去克官者，泄身之秀，亦能伤官。
  - 官：正官，为秩序之权。
  - 见官：局中原有官，或运岁再来官，与伤官相遇之象。
  - 可见/不可见：见官而能用者为“可见”，见官多成祸患者为“不可见”。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 伤官 | Hurting Officer | 食神之进克官 | Output spirit hurting officer | shangguan | existing |
| 见官 | Seeing Officer | 遇到正官 | Encountering proper officer | jianguan | new_candidate |
| 可见不可见 | Can See or Cannot | 是否可见官 | Whether officer can be visible | kejian_bukejian | new_candidate |
| 伤官配印 | Shangguan with Seal | 伤官用印格 | Shangguan using seal pattern | shangguan_peiyin | existing |
| 伤官生财 | Shangguan Births Wealth | 伤官转生财 | Shangguan transforms to wealth | shangguan_shengcai | existing |
| 身强身弱 | Self Strong/Weak | 日主强弱 | Strength of Day Master | shenqiang_shenruo | existing |

- **规范化释义（primary_lang_explained）**：
  伤官见官，吉凶全看“身强身弱、伤官轻重、财印配位”。身弱而伤旺，若得印绶扶身，则可借官生印、印扶身，故“见印可见官”；身旺而伤旺，若得财星，一则财生官、二则财泄伤，故“见财可见官”。伤旺财轻而有比劫者，可用官去制劫，有路可走；若伤旺而无财，或身弱伤旺而见官，多成“官被伤或官克身”为祸。又要分“用印”与“用财”：用印者忌见财破印；用财者忌见印战财。故伤官见官“果难辨”，须按势与用细致裁取。

- **次语种完整诠释（secondary_lang_full）**:  
  Shangguan-see-Official伤官见官 context-dependent: 可见 allowed with财印配位 wealth-seal-configuration—身弱伤旺 weak-self-strong-shangguan需印护 seal-protection借官生印 guan-generates-seal; 身旺伤旺 strong-self-strong-shangguan需财泄 wealth-drains生官 generates-official—不可见 forbidden when伤旺无财 strong-shangguan-no-wealth or身弱见官 weak-self-meets-guan causing官伤or官克身 harm; 总纲: 伤官有财多可见 with-wealth-mostly-allowed无财多不可 without-wealth-mostly-forbidden."""
    normalized_text_zh: str = """"""
    subject: str = "伤官见官果难辨，可见不可见。"
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
        l1_anchor="dts_v1.0.0_伤官见官果难辨_可见不可见_001_L1",
    )
    version: str = "1.0.0"
