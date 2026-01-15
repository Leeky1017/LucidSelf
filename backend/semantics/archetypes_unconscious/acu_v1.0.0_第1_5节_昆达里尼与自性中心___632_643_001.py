"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.559134
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
    semantic_id="acu_v1.0.0_第1_5节_昆达里尼与自性中心___632_643_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第15节昆达里尼与自性中心632643(SemanticEntry):
    """
    **原文** (¶632-643, 行9853-9949):

> [632] In kundalini yoga symbolism, Shakti is represented as a snak...
    """
    
    original_text: str = """**原文** (¶632-643, 行9853-9949):

> [632] In kundalini yoga symbolism, Shakti is represented as a snake wound three and a half times round the lingam, which is Shiva in the form of a phallus. This image shows the possibility of manifestation in space. From Shakti comes Maya, the building material of all individual things. Creation begins with an act of division of the opposites that are united in the deity.
>
> [633-634] The goal of contemplating mandala processes is that the yogi shall become inwardly aware of the deity. The basic motif is the premonition of a centre of personality, a kind of central point within the psyche, to which everything is related, by which everything is arranged, and which is itself a source of energy. This centre is not felt as the ego but as the self.
>
> [637-638] The four dorjes in the gates indicate that life's energy is streaming inwards, returning to the centre. When the perfect union of all energies in the four aspects of wholeness is attained, there arises a static state—the "Diamond Body" (Chinese alchemy), corpus incorruptibile (medieval alchemy), corpus glorificationis (Christian tradition).
>
> [640-641] In the I Ching system: ch'ien (heaven/self-generated creative energy) in the centre, four emanations extending through space. Round this masculine power-centre lies the earth (feminine/receptive). The union of heaven with kun produces the tetraktys—underlying all existence.

**英文释义**：
- 昆达里尼：沙克提 = 蛇绕林伽三圈半（湿婆以阳具形式）
- 沙克提 → 摩耶 = 个体事物的建材
- 创造 = 对立统一的分裂
- 曼陀罗冥想目标：瑜伽士内在觉知神性
- 基本母题：人格中心的预感 = 自性（非自我）
- 四金刚杵 → 能量向内流回中心
- 完美统一 = 金刚身/不朽之身/荣耀之身
- 易经：乾（天/创造能量）在中心 + 坤（地/接受）= 四元组

**中文诠释**：
- 昆达里尼瑜伽：沙克提 = 蛇绕林伽（湿婆）三圈半
- 沙克提 → 摩耶（Maya）= 个体事物的建材 = 幻相
- 创造始于对立统一的分裂 → 能量大爆发
- 曼陀罗冥想：瑜伽士内在觉知神性 → 回归神圣整体
- 基本母题 = 人格中心的预感 = 心理中枢
- 此中心 = 自性（非自我）
- 四金刚杵表示能量向内回流中心
- 完美统一 = 静态状态 = 金刚身/不朽之身/荣耀之身
- 易经：乾（天）在中心；坤（地）接受 → 产生四元组

**Narrative Snippets**：
- `[ns_cw9i_X_632]` `[trigger: kundalini_shakti]` `[factor_trigger: jung_jung_shiva_shakti AND jung_opposites_union]` `[role: 主干]` Kundalini: Shakti as snake wound round lingam (Shiva); creation begins with division of opposites united in deity. → ¶632
- `[ns_cw9i_X_634]` `[trigger: personality_centre]` `[factor_trigger: jung_jung_self AND jung_mandala_center]` `[role: 主干]` Basic motif: premonition of personality centre—the self (not ego), source of energy to which everything is related. → ¶634
- `[ns_cw9i_X_637]` `[trigger: diamond_body]` `[factor_trigger: jung_wholeness_symbol AND jung_contemplation_aid]` `[role: 条件分支]` Perfect union of all energies = Diamond Body (Chinese), corpus incorruptibile (medieval), corpus glorificationis (Christian). → ¶637"""
    normalized_text_zh: str = """"""
    subject: str = "第1.5节：昆达里尼与自性中心 (¶632-643)"
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_第1_5节_昆达里尼与自性中心___632_643_001_L1",
    )
    version: str = "1.0.0"
