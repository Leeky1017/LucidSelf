"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558846
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
    semantic_id="yhzp_v1.0.0_2__正官论_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 2正官论(SemanticEntry):
    """
    - **原文（source_text）**：
  夫正官者，甲见辛之类；乃阴见阳为官，阳见阴为鬼，阴阳配合成其道也。大抵要行官旺乡，月令是也。月令者，提纲也。看命先看提纲，方看其馀。既曰正官，运复行得...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫正官者，甲见辛之类；乃阴见阳为官，阳见阴为鬼，阴阳配合成其道也。大抵要行官旺乡，月令是也。月令者，提纲也。看命先看提纲，方看其馀。既曰正官，运复行得官旺之乡、或是有成局；又行不得伤官之地，并金财旺之乡，皆是作福之处。正官乃贵气之物，大忌刑冲破害；及于年月时干，皆有官星隐露，恐福渺矣！又须看年时上别有是何入格？作福去处，方可断其吉凶。茍一途而执取之，则不能通变，必有差之毫厘，谬以千里之患。正官或多，反不为福。何以言之？盖人之命，宜得中和之气，太过与不及同；中和之气为福厚，偏党之克为灾殃。既用提纲作正官，年时支干位，或有一偏官便杂矣！不可不仔细以轻重推测也。又曰，于月令得之是也，喜身旺、印绶。如甲用辛官，喜土生官；最怕刑冲破害、阳刃七杀，为贫命；如时干逢杀，乃官杀混杂。盖四柱有刑冲破害，皆未为贵命看。官来克我，我去克官不为害。一位若两官不妨。若月令中有正官，时干支有偏官，便难以正官言之。

- **分字分词释义**：
  - **正官**：克我且阴阳相异者，如甲木见辛金，辛金为甲木之正官，阴阳配合成其道。
  - **阴见阳为官阳见阴为鬼**：阴日主见阳官为正官，阳日主见阴官为正官，阴阳配偶之义。
  - **月令提纲**：月支为命局之提纲，看命先看月令定格局旺衰。
  - **官旺之乡**：官星得旺之地支或大运。
  - **刑冲破害**：地支四凶——刑、冲、破、害，正官最忌此四者破坏。
  - **官星隐露**：官星或藏于地支或透于天干。
  - **正官或多反不为福**：官多则杂，失去正官清贵之象。
  - **中和之气**：不偏不倚、不太过不及的平衡状态。
  - **官杀混杂**：正官与七杀同见，混乱不清，为命之大忌。
  - **一位若两官不妨**：一个正官，虽有两处出现亦无妨，因皆为正官。
  - **喜身旺印绶**：正官格喜日主旺相、印星护身生身。

- **规范化释义（primary_lang_explained）**：
  正官是克我且阴阳相异者，如甲木见辛金为正官，阴阳配合成其道。正官格最重月令，"月令者，提纲也，看命先看提纲"。正官喜行官旺之乡，不喜行伤官之地、刑冲破害之运，"正官乃贵气之物，大忌刑冲破害"。正官宜单不宜多，"正官或多，反不为福"，因"人之命，宜得中和之气"。用提纲作正官，年时干支若有偏官则杂，"官杀混杂"为大忌。正官喜身旺印绶，"官来克我"需身旺能担；最怕刑冲破害、阳刃七杀混入。"一位若两官不妨"——同一正官多处出现不算混杂，但若正官与七杀同见则难以正官论。

- **完整对等诠释（secondary_lang_full）**：
  Direct Officer is that which controls me with opposite polarity, such as Jia Wood seeing Xin Metal as Direct Officer—Yin-Yang pairing completes its proper way. The Direct Officer pattern most emphasizes the Month Command: "The Month Command is the guiding principle; examining fate begins with examining the guiding principle." Direct Officer favors traveling through Officer-flourishing regions, disfavors going through Injuring Officer territory or regions of Punishment-Clash-Breakage-Harm. "Direct Officer is a noble-energy entity, greatly taboos Punishment-Clash-Breakage-Harm." Direct Officer prefers singularity over multiplicity: "If Direct Officer is abundant, it conversely brings no fortune," because "human fate appropriately obtains harmonious-balanced energy." When using the Guiding Principle as Direct Officer, if year-hour stems-branches contain a Partial Officer, it becomes mixed—"Mixed Officer-Killing" is a great taboo. Direct Officer favors strong Self and Seal: "Officer coming to control me" requires strong Self to bear it; most fears Punishment-Clash-Breakage-Harm and Yang Blade-Seven Killing mixing in. "One position with two Officers is unproblematic"—the same Direct Officer appearing in multiple places doesn't count as mixed, but if Direct Officer and Seven Killing appear together, it becomes difficult to analyze as Direct Officer pattern.

- **核心要点**：
  - 正官是克我且阴阳相异者，阴阳配合成其道
  - 月令为提纲，看命先看月令
  - 正官乃贵气之物，大忌刑冲破害
  - 正官或多反不为福，宜中和之气
  - 官杀混杂为大忌
  - 正官喜身旺印绶
  - 一位两官不妨，官杀同见则混

- **详细解说**：
  本条详论正官的性质与取用。正官是克我且阴阳相异者，"乃阴见阳为官，阳见阴为鬼，阴阳配合成其道"——正官与日主形成阴阳配偶关系，故为"正"而非"偏"。正官格以月令为重："月令者，提纲也，看命先看提纲，方看其馀"——这是命理的基本法则。正官"乃贵气之物"，最怕刑冲破害破坏其贵气。正官宜单不宜多，"正官或多，反不为福"——官多则杂，失其清贵。"人之命，宜得中和之气，太过与不及同"——这是命理中和之道的精髓。官杀混杂是正官格的大忌："既用提纲作正官，年时支干位，或有一偏官便杂矣"。正官喜身旺印绶，"官来克我"需要身强能担，"喜土生官"表明需要有力量承载官星。"一位若两官不妨"说明同一正官重见不算混杂，但正官与七杀同见则难以正官格论。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_561]` `[trigger: 正官定义]` `[factor_trigger: direct_officer]` `[role: 主干]` 夫正官者，甲见辛之类；乃阴见阳为官，阳见阴为鬼，阴阳配合成其道也。 → 《渊海子平·正官论》
  - `[ns_yhzp_562]` `[trigger: 月令提纲]` `[factor_trigger: month_command]` `[role: 主干依赖]` 月令者，提纲也。看命先看提纲，方看其馀。 → 《渊海子平·正官论》
  - `[ns_yhzp_563]` `[trigger: 正官忌刑冲]` `[factor_trigger: direct_officer AND punishment]` `[role: 条件分支]` 正官乃贵气之物，大忌刑冲破害。 → 《渊海子平·正官论》
  - `[ns_yhzp_564]` `[trigger: 官多不福]` `[factor_trigger: direct_officer]` `[role: 例外处理]` 正官或多，反不为福。 → 《渊海子平·正官论》
  - `[ns_yhzp_565]` `[trigger: 中和之气]` `[factor_trigger: balance]` `[role: 总结]` 人之命，宜得中和之气，太过与不及同；中和之气为福厚，偏党之克为灾殃。 → 《渊海子平·正官论》
  - `[ns_yhzp_566]` `[trigger: 官杀混杂]` `[factor_trigger: direct_officer AND seven_killings]` `[role: 条件分支]` 既用提纲作正官，年时支干位，或有一偏官便杂矣！ → 《渊海子平·正官论》
  - `[ns_yhzp_567]` `[trigger: 正官喜身旺]` `[factor_trigger: direct_officer AND day_master_strength AND direct_seal]` `[role: 条件分支]` 喜身旺、印绶。如甲用辛官，喜土生官。 → 《渊海子平·正官论》"""
    normalized_text_zh: str = """"""
    subject: str = "2. 正官论"
    factor_refs: list = ['direct_officer', 'month_command', 'pattern_mixed_officer_killing', 'balance']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_2__正官论_001_L1",
    )
    version: str = "1.0.0"
