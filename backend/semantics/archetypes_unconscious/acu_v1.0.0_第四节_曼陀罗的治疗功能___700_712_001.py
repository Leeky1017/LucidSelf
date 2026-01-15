"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.559242
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
    semantic_id="acu_v1.0.0_第四节_曼陀罗的治疗功能___700_712_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第四节曼陀罗的治疗功能700712(SemanticEntry):
    """
    **原文** (¶700-712, 行10631-10765):

> [700-702] Navaho Indians prepare mandalas from coloured sand for...
    """
    
    original_text: str = """**原文** (¶700-712, 行10631-10765):

> [700-702] Navaho Indians prepare mandalas from coloured sand for curative purposes (Mountain Chant Rite). Around the centre runs the body of the Rainbow Goddess. The Egyptian Sky Mother bends, like the Rainbow Goddess, over the "Land" with its round horizon. Hildegard of Bingen shows the earth surrounded by ocean, realm of air, and starry heaven.
>
> [705-708] Figure 49 shows the patient's shadow problem—a female figure representing her dark, chthonic side, standing in front of a wheel with four spokes. Fire expresses an intense transformation process—the prima materia symbolized by the salamander in fire. Individuation is neither a summum bonum nor a summum desideratum, but the painful experience of the union of opposites. The cross in the circle shows evil that it is already included and has therefore lost its destructive power.
>
> [709-710] I hope I have given some idea of mandala symbolism. They are yantras in the Indian sense—instruments of meditation, concentration, and self-immersion for realizing inner experience. At the same time they serve to produce an inner order—following chaotic, disordered states marked by conflict and anxiety. They express the idea of a safe refuge, of inner reconciliation and wholeness.
>
> [711-712] These symbols are governed by the same fundamental laws that can be observed in individual mandalas. There must be a transconscious disposition in every individual which is able to produce the same symbols at all times and in all places—the collective unconscious, with its primordial images, the archetypes. Knowledge of the common origin of these symbols has been totally lost to us. When we penetrate below the surface of the psyche, we come upon historical layers which are not just dead dust, but alive and continuously active in everyone.

**英文释义**:

曼陀罗 = 诊断工具 + 治疗工具。为心理混乱提供秩序。为分裂人格提供整合点。制作过程本身是治疗性的：给予无意识内容形式 → 可被意识整合。曼陀罗 = 集体无意识产物，但在每个个体中活生生、持续活跃。不仅是历史遗迹——是活的心理力量。

**完整中文诠释**:

**曼陀罗的双重功能**：
1. **诊断功能**：显示心理状态和发展阶段
2. **治疗功能**：提供秩序和整合

**治疗机制**：
- 为心理混乱提供秩序
- 为分裂人格提供整合点
- 给予无意识内容形式
- 使无意识可被意识整合

**制作过程的治疗性**：
- 绘画/编织/制作曼陀罗本身是治疗
- 如Penelope式的编织（对抗生活困难）
- 围绕自己编织"魔法圆"

**集体与个体**：
- 曼陀罗 = 集体无意识产物
- 但在每个个体中活生生
- 不是历史遗迹——是活的心理力量
- 持续活跃到无法想象的程度

**核心要点**:
- 曼陀罗具有诊断和治疗双重功能
- 为混乱提供秩序，为分裂提供整合
- 制作过程本身是治疗性的
- 是活的心理力量，非历史遗迹

**叙事片段**:
- `[ns_cw9i_X_005]` `[trigger: 治疗功能]` `[factor_trigger: jung_mandala AND jung_healing]` `[role: 主干]` 曼陀罗为心理混乱提供秩序，为分裂人格提供整合——制作过程本身就是治疗。→ ¶700-712"""
    normalized_text_zh: str = """"""
    subject: str = "第四节：曼陀罗的治疗功能 (¶700-712)"
    factor_refs: list = ['diagnostic_function', 'therapeutic_function', 'active_creation', 'living_force', 'jung_mandala', 'creation_process']
    
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
        l1_anchor="acu_v1.0.0_第四节_曼陀罗的治疗功能___700_712_001_L1",
    )
    version: str = "1.0.0"
