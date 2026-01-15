"""
Auto-generated semantic module for pollack_tarot
Generated at: 2025-12-05T13:30:19.994654
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
    semantic_id="pt_v1.0.0_card_20__judgement_001",
    book_id="pollack_tarot",
    engine_id="tarot"
)
class Card20Judgement(SemanticEntry):
    """
    ### Call, Resurrection, New Consciousness

#### Key Term Analysis

| Term | Definition | Significanc...
    """
    
    original_text: str = """### Call, Resurrection, New Consciousness

#### Key Term Analysis

| Term | Definition | Significance |
|------|-----------|---------------|
| Number 20 | 10×2 Wheel×Priestess | True mind awakened |
| Call | Inside + outside | Artificial barrier broken |
| No Personal Liberation | Bodhisattva | Liberates all |
| Hero Mythology | Hidden identity | Finding center |

**Source Text**: Under Sun we see life filled with spiritual light. Now we feel, like call from deep inside, urge to dissolve completely into spirit. Call comes from both inside and outside. The old ways have died without ourselves noticing. One last descent into waters of nothingness to rise up liberated from all partial knowledge. Death showed dissolution with fear; here emphasis on resurrection.

**English Paraphrase**:

**Judgement** = **Call**, **Rising**, **New Self** — inner urge to dissolve, already changed, only recognition remains.

**Core Symbolism**:
- **Number 20**: 10×2 (Wheel mysteries revealed through High Priestess wisdom), Resh = "head" (true mind awakened)
- **Rosh Hashanah**: Not calendar start but creation anniversary = new consciousness

**Visual**:
- **Angel** with trumpet = call from beyond
- **People rising** from coffins/water (3 foreground + 3 background) = no personal liberation, human race as whole
- **Cross banner** = meeting opposites, horizontal (ordinary time) + vertical (eternity) joined
- **Mountains** (background) = "abstract thought", absolute truth beyond ordinary knowledge
- **Child** with back to us = mystery, hidden face = don't know true self until respond to call

**Call nature**: From inside (deepest cells) + outside (greater force), artificial barrier broken (Sun effect). Already decided within, conscious self must follow with action.

**vs. Justice**: Justice = personal past response, Judgement = greater force calling, judgment on true nature of existence

**No personal liberation**: Buddha boddhisatva (can't free self until liberate all), any single liberation liberates everybody (Gautama/Christ changed world)

**Hero mythology**: Separated from parents, raised as ordinary child, true identity hidden (Arthur/Moses/Theseus/Christ), amnesia sci-fi hero discovering great powers, "forgotten" true identities, finding true self = finding center of universe

**完整中文诠释**:
**审判**=**召唤**、**升起**、**新自我**——溶解内在冲动，已然改变，仅剩认知。**数字20**：10×2（轮之谜通过女祭司智慧揭示），Resh="头"（真正心智觉醒）；**新年**（Rosh Hashanah）：非历法开端而是创世纪念=新意识。**图像**（RWS牌）：**天使**持号角=超越之召；**人从棺/水升起**（3前景+3背景）=无个人解放，人类整体；**十字旗帜**=对立相遇，横（常态时间）+竖（永恒）连接；**群山**（背景）="抽象思维"，超常识之绝对真理；**儿童**背对我们=神秘，隐藏面孔=应召前不知真我。**召唤本质**：从内（最深细胞）+外（更大力量），人为屏障破碎（太阳效应）。内在已决定，有意识自我必须以行动随从。**vs正义**：正义=个人过往回应，审判=更大力量召唤，对存在真实本质之审判。**无个人解放**：佛菩萨（未解放一切前无法自由），任何单一解放即解放所有人（乔达摩/基督改变世界）。**英雄神话**：与父母分离，作为普通孩童养育，真实身份隐藏（亚瑟/摩西/特修斯/基督），失忆科幻英雄发现巨大力量，"遗忘"真实身份，寻得真我=寻得宇宙中心（中心无处不在）。太阳下我们见生命充满灵性之光。现我们感受，如从深处召唤，完全溶入灵性之冲动。召唤来自内与外。旧路已死而我们未注意。最后一次下降进虚无之水以从所有偏知解放升起。死神显示带恐惧之溶解；此处强调复活。

#### Textual Criticism & Variant Analysis (Bilingual)

- **English**: Pollack's Judgement: Number 20=10×2. Call inside+outside. No personal liberation. Hero mythology. vs Justice contrast.
- **中文**: Pollack的审判:数字20=10×2。召唤内+外。无个人解放。英雄神话。vs正义对比。

- **English**: Pollack's Sun: Number 19=Hermit+Magician. Lucid=light-filled. Naked child. Eden regained. Universal enlightenment.
- **中文**: Pollack的太阳:数字19=隐士+魔术师。Lucid=充满光。裸童。伊甸重获。普世开悟。

**Narrative Snippets**:
- `[ns_78deg_165]` `[trigger: judgement_major]` `[factor_trigger: tarot_major_judgement AND tarot_number_20 AND state_psychic_wholeness]` `[role: 主干]` Judgement represents the call to dissolution from inside and outside—resurrection emphasized; hidden identity revealed; finding true self. → English Paraphrase
- `[ns_78deg_166]` `[trigger: no_personal_liberation]` `[factor_trigger: principle_no_personal_liberation]` `[role: 主干]` No personal liberation—bodhisattva principle; any single liberation liberates everybody; the whole human race rises together. → Source Text
- `[ns_78deg_167]` `[trigger: hidden_identity]` `[factor_trigger: archetype_hidden_identity]` `[role: 条件分支]` Hero mythology pattern—hidden identity, raised as ordinary, true self revealed; Arthur/Moses/Christ discovering great powers. → English Paraphrase
- `[ns_78deg_168]` `[trigger: living_creatures]` `[factor_trigger: symbol_living_creatures]` `[role: 条件分支]` People rising from coffins/water—foreground and background; collective resurrection; all humanity involved in the call. → English Paraphrase
- `[ns_78deg_358]` `[trigger: judgement_number_20]` `[factor_trigger: tarot_major_judgement AND number_20]` `[role: 条件分支]` Number 20 = 10×2 (Wheel mysteries revealed through High Priestess wisdom); Resh = "head" (true mind awakened); Rosh Hashanah = new consciousness. → Core Symbolism
- `[ns_78deg_359]` `[trigger: call_nature]` `[factor_trigger: tarot_major_judgement AND principle_call]` `[role: 条件分支]` Call comes from inside (deepest cells) + outside (greater force)—artificial barrier broken by Sun; already decided within, conscious self must follow with action. → Call Nature
- `[ns_78deg_360]` `[trigger: cross_banner]` `[factor_trigger: tarot_major_judgement AND symbol_cross]` `[role: 条件分支]` Cross banner = meeting of opposites: horizontal (ordinary time) + vertical (eternity) joined; mountains = absolute truth beyond ordinary knowledge. → Visual Elements
- `[ns_78deg_361]` `[trigger: judgement_vs_justice]` `[factor_trigger: tarot_major_judgement AND tarot_major_justice AND contrast_judgement_justice AND planet_pluto]` `[role: 总结]` Judgement vs Justice: Justice = personal past response; Judgement = greater force calling, judgment on true nature of existence; collective vs individual karma. → vs. Justice
- `[ns_78deg_538]` `[trigger: angel_trumpet]` `[factor_trigger: tarot_major_judgement AND symbol_angel_trumpet]` `[role: 条件分支]` Angel with trumpet—call from beyond that awakens sleepers; the dead rising not through their own will but through divine summons; grace initiates, ego responds. → Visual Elements
- `[ns_78deg_539]` `[trigger: child_hidden_face]` `[factor_trigger: tarot_major_judgement AND symbol_child_back]` `[role: 条件分支]` Child with back to us, hidden face—don't know true self until respond to call; mystery of identity revealed only through answering; the hero's unknown parentage. → Visual Elements

---"""
    normalized_text_zh: str = """"""
    subject: str = "Card 20: Judgement"
    factor_refs: list = ['tarot_major_judgement', 'tarot_number_20', 'state_the_call', 'principle_no_personal_liberation', 'archetype_hidden_identity']
    
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
        book_id="pollack_tarot",
        chapter="",
        l1_anchor="pt_v1.0.0_card_20__judgement_001_L1",
    )
    version: str = "1.0.0"
