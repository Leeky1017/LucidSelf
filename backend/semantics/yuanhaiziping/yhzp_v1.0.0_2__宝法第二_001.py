"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559366
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
    semantic_id="yhzp_v1.0.0_2__宝法第二_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 2宝法第二(SemanticEntry):
    """
    - **原文（source_text）**：
  子平之法，以日为主；先看提纲为重，次用年日时支，合成格局，方可断之；皆以月令为用，不可以年取格。凡看子平之数，取格不定，十有九差。
  惟易鉴先生之法...
    """
    
    original_text: str = """- **原文（source_text）**：
  子平之法，以日为主；先看提纲为重，次用年日时支，合成格局，方可断之；皆以月令为用，不可以年取格。凡看子平之数，取格不定，十有九差。
  惟易鉴先生之法，月令用金只用金，用火只用火；八字水多却取水，不来取火，况此差矣！
  是西山易鉴参透玄机，十八格内取六格为重，用相生，定格合局；仍用年日下，以推轻重浅深，万无一失。
  六格法曰：'逢官看财'，'逢财看杀'，'逢杀看印'，'逢印看官'。如用印不怕杀；是杀拘印，印拘身，还作上格取之。如四柱逢印看七杀；但有官杀在，运行官杀乡，亦作贵格。
  月令通官，柱中遇财，财生官妙矣！乃富贵之格。
  柱中见财，要人财旺，至兴发福矣！
  但见一杀，则以杀为重，不可又行财旺之乡；乃财生杀旺，当作贫贱之格。
  凡格当以杀官言之。

- **分字分词释义**：
  - **月令用金只用金**：月令本气为金则定为金格，不可改换。
  - **取格不定十有九差**：格局取用不准确则十有九误。
  - **十八格内取六格为重**：从众多格局中提炼六格为核心。
  - **逢财看杀**：见财星需查七杀是否被财星生助。
  - **用印不怕杀**：印格不惧七杀，因杀生印为贵。
  - **杀拘印印拘身**：七杀生印绶，印绶生日主，形成吉配。
  - **财生官妙**：财星生助官星，富贵之格。
  - **财生杀旺贫贱**：财星生助七杀，七杀太旺反主贫贱。
  - **凡格当以杀官言之**：论格局首重官杀二星的配置。

- **规范化释义（primary_lang_explained）**：
  本篇继续阐述六格法的应用：
  1. **取格定例**：必须以月令为主，不可被八字中其他多出的五行迷惑。月令是金就用金，不可因水多而改取水格（除非从格）。
  2. **六格口诀**：逢官看财，逢财看杀（财生杀需制），逢杀看印，逢印看官。
  3. **杀印相生**：用印不怕杀，杀生印，印生身，为上格。印格喜行官杀运。
  4. **财官双美**：月令官星遇财，财生官，富贵之格。
  5. **财杀之忌**：见杀则杀为重，忌行财乡（党杀），财生杀旺主贫贱。

- **完整对等诠释（secondary_lang_full）**：
  **Precious Method II**:
  - **Strict Month Command**: If Month Command is Metal, use Metal; do not switch to Water just because Water is abundant elsewhere (unless following).
  - **Six Patterns Mnemonics**: "Meeting Officer check Wealth; Meeting Wealth check Killing; Meeting Killing check Seal; Meeting Seal check Officer."
  - **Seal & Killing**: Seal fears no Killing; Killing generates Seal, Seal generates Self—forming a High Pattern. Seal patterns favor Officer/Killing luck.
  - **Wealth & Officer**: Month Officer meeting Wealth is "Wealth generating Officer," a noble pattern.
  - **Wealth & Killing**: If a Killing appears, it takes precedence. Do NOT go to Wealth luck, as Wealth generating Killing leads to poverty and baseness.

- **核心要点**：
  - **定格不乱**：坚守月令本气
  - **杀印有情**：杀生印为贵
  - **财杀无情**：财生杀为贫

- **详细解说**：  《宝法第二》延续第一篇的定格原则，进一步细化六格法的应用。"月令用金只用金，用火只用火"强调坚守月令本气，不可被八字中其他旺盛的五行迷惑而改取格局，"取格不定，十有九差"。本篇扩展了六格口诀为"逢官看财，逢财看杀，逢杀看印，逢印看官"，增加了"逢财看杀"——财格需警惕七杀，若财生杀则反主贫贱。**杀印相生**是本篇重点："用印不怕杀，是杀拘印，印拘身，还作上格取之"，揭示了七杀生印、印生身的连续相生为贵格。**财官双美**——"月令通官，柱中遇财，财生官妙矣"，财生官为富贵之格。**财杀相忌**——"但见一杀，则以杀为重，不可又行财旺之乡"，财生杀旺反主贫贱。末句"凡格当以杀官言之"点明论格首重官杀二星的配置。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_651]` `[trigger: 月令定格不乱]` `[factor_trigger: yueling_dingge AND buluan AND dingge]` `[role: 主干]` 月令用金只用金，用火只用火；取格不定十有九差。 → 《渊海子平·宝法第二》
  - `[ns_yhzp_652]` `[trigger: 四看口诀]` `[factor_trigger: sikan_koujue AND guan_cai_sha_yin AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 主干依赖]` 逢官看财，逢财看杀，逢杀看印，逢印看官；六格法扩展口诀。 → 《渊海子平·宝法第二》
  - `[ns_yhzp_661]` `[trigger: 用印不怕杀]` `[factor_trigger: yongyin_bupasha AND shayin_xiangsheng AND gui AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin AND guansha_yun]` `[role: 条件分支]` 用印不怕杀，是杀拘印印拘身，还作上格取之。 → 《渊海子平·宝法第二》
  - `[ns_yhzp_662]` `[trigger: 财生官妙]` `[factor_trigger: caisheng_guan AND fugui_ge AND anchong_qugui AND angui]` `[role: 条件分支]` 月令通官，柱中遇财，财生官妙矣！乃富贵之格。 → 《渊海子平·宝法第二》
  - `[ns_yhzp_663]` `[trigger: 财生杀贫]` `[factor_trigger: caisheng_sha AND pinjian_ge]` `[role: 例外处理]` 但见一杀则以杀为重，不可又行财旺之乡；财生杀旺当作贫贱之格。 → 《渊海子平·宝法第二》
  - `[ns_yhzp_664]` `[trigger: 宝法二纲领]` `[factor_trigger: baofa_dier AND shayin_youqing AND caisha_wuqing AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 总结]` 宝法第二以月令定格不乱，杀印有情为贵，财杀无情为贫。 → 《渊海子平·宝法第二》"""
    normalized_text_zh: str = """"""
    subject: str = "2. 宝法第二"
    factor_refs: list = ['killing_generating_seal', 'wealth_generates_killing']
    
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
        l1_anchor="yhzp_v1.0.0_2__宝法第二_001_L1",
    )
    version: str = "1.0.0"
