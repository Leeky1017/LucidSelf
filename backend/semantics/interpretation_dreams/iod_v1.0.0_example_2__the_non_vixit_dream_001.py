"""
Auto-generated semantic module for interpretation_dreams
Generated at: 2025-12-05T13:30:20.460919
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
    semantic_id="iod_v1.0.0_example_2__the_non_vixit_dream_001",
    book_id="interpretation_dreams",
    engine_id="dream"
)
class Example2TheNonVixitDream(SemanticEntry):
    """
    #### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| ...
    """
    
    original_text: str = """#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Displacement | Emotion shifted to trivial | Evades censorship |
| Non Vixit | "He did not live" | Death-wish revealed |
| Substitute Target | Safe person replaces real | Misdirection |
| Intensity Transfer | Strong→weak element | Disguise mechanism |

**Source Text** (Freud's revenge dream):
"I go into the Brücke Institute, and on seeing me there Professor Fl. becomes alarmed. I calmly explain: 'I am here only in order to bring you the news that you have been reported for some offence.' He goes pale, but I reassure him: 'Only by a colleague—don't be alarmed.' At the same time I see before me an inscription: 'Non vixit.'"

**Analysis Summary**:
- **Manifest content**: Polite professional encounter
- **Latent wish**: Hostile death-wish toward colleague (Fl. = Fliess)
- **"Non vixit"** = "He did not live" (epitaph inscription)
- **Displacement**: Intense hostile emotion → shifted to trivial "offence" report
- True target: Friend who had priority dispute with Freud

**Key Mechanism**: **Displacement** (移置)
- **Emotional intensity** transferred from significant to trivial element
- Allows forbidden hostile wish to escape censorship
- Dream says "offence" but means "death"
- Mechanism makes dream seem innocent while concealing murder wish

**Complete Chinese Interpretation (Secondary Language)**:

“Non vixit”梦从表面看是一场再普通不过的职业场景：走进研究所、向同事传达被检举的消息、口头上还安抚对方“只是同事举报，不必太担心”。如果只停留在显梦层面，很难把它与强烈敌意或死亡愿望联系在一起。然而，梦中突然闯入的拉丁文墓志铭“Non vixit”（“他未曾活过”），却暴露了另一条情绪暗流——那不是一般的“冒犯”或小失误，而是对同行“最好不存在”的极端敌意。

移置在此体现在两层：一是**内容的替换**——真正的潜在对象并非梦中出现的那位教授，而是与弗洛伊德有优先权纠纷的朋友；梦把无法直接承认的复仇冲动转移到了一个相对安全的替身身上。二是**情感重心的错位**——表面上，梦者似乎只是就某种“职业违规”发表冷静通告，情感上却被那句“Non vixit”强烈吸引；真正高浓度的情感重量，被移到了墓志铭这一看似附带的元素上。

通过这样的错位安排，梦一方面让“你应该为此付出终极代价”这样的死亡愿望以隐蔽形式获得表达，另一方面又借由礼貌对话的外壳，维持了表层的体面与无害。对分析者来说，正是这些情绪与内容不成比例的小细节——例如一句突兀的碑文——标示出移置机制正在运作的地方，也是通向真正潜在主题的入口。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Non-Vixit Dream: Classic displacement example. Manifest=polite encounter, Latent=death-wish. "Non vixit" epitaph exposes true target. Emotion transferred from murder wish to trivial "offence."
- **中文**: Non Vixit梦:经典移置示例。显梦=礼貌会面,潜梦=死亡愿望。"他未曾活过"墓志铭暴露真正目标。情感从谋杀愿望转移到琐碎"违规"。

**Narrative Snippets**:
- `[ns_freud_ex_004]` `[trigger: displacement_example]` `[factor_trigger: dream_work_displacement]` `[role: 主干]` Non-Vixit Dream: emotional intensity transferred from death-wish to trivial "offence". → Example
- `[ns_freud_ex_005]` `[trigger: substitute_target]` `[factor_trigger: dream_work_displacement AND misdirection]` `[role: 条件分支]` Safe person replaces real target; polite encounter masks murder wish. → Mechanism
- `[ns_freud_ex_006]` `[trigger: non_vixit_epitaph]` `[factor_trigger: dream_work_displacement AND revelation]` `[role: 条件分支]` "Non vixit" epitaph exposes true hostile intent despite displacement disguise. → Clue"""
    normalized_text_zh: str = """"""
    subject: str = "Example 2: The Non-Vixit Dream (Displacement)"
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
        book_id="interpretation_dreams",
        chapter="",
        l1_anchor="iod_v1.0.0_example_2__the_non_vixit_dream_001_L1",
    )
    version: str = "1.0.0"
