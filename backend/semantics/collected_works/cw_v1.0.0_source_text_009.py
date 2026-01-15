"""
Auto-generated semantic module for collected_works
Generated at: 2025-12-05T13:30:20.574958
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
    semantic_id="cw_v1.0.0_source_text_009",
    book_id="collected_works",
    engine_id="psych"
)
class SourceText(SemanticEntry):
    """
    "The coniunctio is the alchemical symbol for the union of opposites—King and Queen, Sol and Luna, co...
    """
    
    original_text: str = """"The coniunctio is the alchemical symbol for the union of opposites—King and Queen, Sol and Luna, conscious and unconscious. Psychologically, it represents the integration of the ego with the Self, the union of masculine and feminine within the individual."

#### English Paraphrase (Primary Language)

**Coniunctio** (Sacred Marriage) = Alchemical symbol for **union of opposites**.

**Alchemical imagery**:
- **Sol (Sun/King)** = Consciousness, masculine principle, gold
- **Luna (Moon/Queen)** = Unconscious, feminine principle, silver
- Union produces **Divine Child** = Individuated Self

**Psychological meaning**:
- Integration of ego and Self
- Union of conscious and unconscious contents
- Masculine-feminine balance within individual
- Opposites reconciled, not eliminated

**Process requires**:
1. Recognition of opposites within psyche
2. Holding tension between them (not choosing)
3. Transcendent function activates
4. New synthesis emerges (tertium non datur → tertium datur)

#### Complete Chinese Interpretation (Secondary Language)

**神圣婚姻** = 炼金术中**对立面合一**的象征。

**炼金意象**：
- **太阳（国王）** = 意识、阳性原则、金
- **月亮（王后）** = 无意识、阴性原则、银
- 结合产生**神圣之子** = 个体化的本我

**心理学含义**：
- 自我与本我的整合
- 意识与无意识内容的合一
- 个体内部男女性平衡
- 对立面和解而非消除

**过程需要**：
1. 认识心灵内的对立面
2. 持住它们之间的张力（不选择）
3. 超越功能激活
4. 新综合涌现（不存在第三者 → 第三者出现）

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Coniunctio | Sacred marriage of opposites | Individuation culmination |
| Sol | Conscious/masculine | Sun/King |
| Luna | Unconscious/feminine | Moon/Queen |
| Divine Child | Individuated Self | Union product |

#### Core Points

- Coniunctio = sacred union of opposites
- Sol (conscious) + Luna (unconscious) = Divine Child
- Psychological: ego-Self integration, masculine-feminine balance
- Central symbol of individuation completion

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Coniunctio: Alchemical sacred marriage. Sol (conscious/masculine) + Luna (unconscious/feminine) = Divine Child. Psychological: ego-Self integration. Opposites reconciled not eliminated. Central individuation symbol.
- **中文**: 神圣婚姻:炼金术神圣结合。太阳(意识/阳性)+月亮(无意识/阴性)=神圣之子。心理学:自我-本我整合。对立面和解而非消除。个体化核心象征。

**Narrative Snippets**:
- `[ns_jung_035]` `[trigger: coniunctio_union]` `[factor_trigger: jung_coniunctio AND jung_opposites]` `[role: 主干]` Coniunctio is the alchemical symbol for union of opposites—King and Queen, Sol and Luna, conscious and unconscious. → Core
- `[ns_jung_036]` `[trigger: ego_self_integration]` `[factor_trigger: jung_ego AND jung_self_integration]` `[role: 条件分支]` Psychologically, it represents integration of ego with Self, union of masculine and feminine within individual. → Psychology
- `[ns_jung_037]` `[trigger: divine_child]` `[factor_trigger: jung_divine_child AND jung_individuation]` `[role: 条件分支]` Union of Sol (consciousness) and Luna (unconscious) produces the Divine Child—the individuated Self. → Product"""
    normalized_text_zh: str = """"""
    subject: str = "Source Text"
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
        book_id="collected_works",
        chapter="",
        l1_anchor="cw_v1.0.0_source_text_009_L1",
    )
    version: str = "1.0.0"
