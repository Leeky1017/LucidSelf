"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.520036
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
    semantic_id="acu_v1.0.0_第四_25节_眼睛曼陀罗与接受黑暗___591_602_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 第四25节眼睛曼陀罗与接受黑暗591602(SemanticEntry):
    """
    **原文** (¶591-602, 行9220-9360):

> [591-592] Four days before painting the mandala, Miss X had a drea...
    """
    
    original_text: str = """**原文** (¶591-602, 行9220-9360):

> [591-592] Four days before painting the mandala, Miss X had a dream: She removed a black fleck from a young man's eye with white oil, and a golden lamp became visible in the centre of the pupil. She woke saying: "If thine eye be single, thy whole body shall be full of light." The animus has become her patient—he had "seen things too blackly." The eye is the prototype of the mandala. Böhme calls his mandala "The Philosophique Globe, or Eye of the Wonders of Eternity."
>
> [593-595] The mandala is indeed an "eye"—the structure symbolizes the centre of order in the unconscious. Böhme calls it a "fiery eye." The eye stands for consciousness looking into its own background, seeing its own light. By accepting the darkness, the patient has kindled a light that illuminates the darkness within. The transition from Picture 7 to Picture 8 gives a working idea of "accepting the dark principle."
>
> [596-597] In Picture 9 we see for the first time the blue "soul-flower" on a red background. In the centre is the golden light in the form of a lamp. The cortices radiate outwards composed of rainbow hues—a real cauda pavonis. The mandala is divided into upper and lower halves: above, three white birds (pneumata = Trinity); below, a goat rising up with two ravens (Wotan's birds) and twining snakes. This is a Western person with Christian background whose light throws a dark shadow.

**英文释义**：
- 梦：从年轻人眼中除去黑斑 → 金灯在瞳孔中央显现
- "眼若明亮，全身光明"（马太福音6:22）
- 阿尼姆斯成为病人——他"看事物太黑暗"
- 眼睛 = 曼陀罗原型；波墨："哲学圆球"或"永恒奇迹之眼"
- 曼陀罗 = "眼睛" = 无意识秩序中心
- 接受黑暗 → 点燃照亮黑暗的光
- 灵魂之花（蓝色）在红色背景上
- 孔雀尾（cauda pavonis）= 彩虹色光芒
- 上半部：三白鸟（圣灵/三位一体）
- 下半部：山羊+两乌鸦（沃坦之鸟）+缠绕的蛇

**中文诠释**：
- 梦境：白油除去年轻人眼中黑斑 → 金灯显现
- 醒来时说："眼若明亮，全身光明"
- 阿尼姆斯成为病人——他看事物太黑暗
- 眼睛 = 曼陀罗原型
- 波墨："哲学圆球/永恒奇迹之眼/智慧之镜"
- 曼陀罗 = 眼睛 = 无意识秩序中心
- 接受黑暗不是将其变为光，而是点燃照亮黑暗的光
- 画作9：蓝色灵魂之花+红色背景+金灯
- 孔雀尾 = 彩虹色日出光芒
- 上下分裂：上=三白鸟（三位一体）；下=山羊+乌鸦+蛇
- 西方基督教背景：光投射暗影

**Narrative Snippets**:
- `[ns_cw9i_IX_592]` `[trigger: eye_mandala]` `[factor_trigger: jung_eye AND jung_mandala]` `[role: 主干]` Eye = prototype of mandala; Böhme calls it "Eye of the Wonders of Eternity"—animus had "seen things too blackly." → ¶591-592
- `[ns_cw9i_IX_595]` `[trigger: accepting_darkness]` `[factor_trigger: jung_shadow AND jung_light]` `[role: 主干依赖]` Accepting darkness = kindling a light that illuminates the darkness within. → ¶595
- `[ns_cw9i_IX_597]` `[trigger: trinity_wotan]` `[factor_trigger: jung_mandala AND jung_religion]` `[role: 条件分支]` Mandala divided: above, three white birds (Trinity); below, goat with ravens (Wotan's birds)—Western Christian background. → ¶597"""
    normalized_text_zh: str = """"""
    subject: str = "第四.25节：眼睛曼陀罗与接受黑暗 (¶591-602)"
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
        l1_anchor="acu_v1.0.0_第四_25节_眼睛曼陀罗与接受黑暗___591_602_001_L1",
    )
    version: str = "1.0.0"
