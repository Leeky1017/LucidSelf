"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.465617
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
    semantic_id="zpzq_v1.0.0_四吉神的反向作用_用之不当亦破格_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 四吉神的反向作用用之不当亦破格(SemanticEntry):
    """
    - **原文（source_text）**：
  十八、论四吉神能破格。
  财官印食，四吉神也，然用之不当，亦能破格。

  如食神带煞，透财为害，财能破格也；春木火旺，见官则忌，官能破格也；煞逢食...
    """
    
    original_text: str = """- **原文（source_text）**：
  十八、论四吉神能破格。
  财官印食，四吉神也，然用之不当，亦能破格。

  如食神带煞，透财为害，财能破格也；春木火旺，见官则忌，官能破格也；煞逢食制，透印无功，印能破格也；财旺生官，露食则杂，食能破格也。

  是故官用食破，印用财破。譬之用药，参苓芪术，本属良材，用之失宜，亦能害人。官忌食伤，财畏比劫，印惧财破，食畏印夺，参合错综，各极其妙。弱者以生扶为喜，强者因生扶而反害；衰者以裁抑为忌，太旺者反以裁抑而得益。吉凶喜忌，全在是否合于需要，不因名称而有分别也。

- 原注（原文注解）：
  　　本章承接“用神格局高低”“因成得败因败得成”，讨论一个很容易被误解的问题：**所谓“四吉神”（财、官、印、食），并非永远只带吉祥，只要用之不当，同样能破格。**
  - 首句点明：财、官、印、食是四种常见的喜用之神，但“用之不当，亦能破格”；
  - 随后列出四种典型的“吉神反破格”情形：
    1) 食神带煞，本可成“食神带煞格”，若再透财过多，财来泄食、助煞，反令财成破格之源；
    2) 春木火旺，本宜用水调候或用财泄火，若再透官星，官火愈旺反成忌神，是官破格；
    3) 煞逢食制本为佳局，若再透印，印来生身、护煞，使食制之力受阻，是印破格；
    4) 财旺生官，本为顺局，若再露食神，则食泄身而生财，格局变成“食生财生官”之杂，食神反成破格之源。
  - 末段以“用药”比喻：
    - 参苓芪术皆为良药，用之失宜亦能伤人；
    - 同理，官喜、财喜、印喜、食喜的前提，都在“合于需要”，而不是因为名字好听就一味加之。
  - 关键总结在最后几句：
    - 弱者应以生扶为喜，强者反因生扶而害；
    - 衰者忌裁抑，太旺者反以裁抑而得益；
    - 吉凶喜忌全在“是否合于需要”，而不在“名称是吉是凶”。

- 分字分词释义：
  - 四吉神：财、官、印、食四类多被视为吉用之神，相对于煞、伤、枭、刃等四凶神而言。
  - 食神带煞：食神与七煞同见且互相作用的格局。
  - 透财为害：财星透出过多或不当，使原本良好的结构失衡。
  - 春木火旺：指春季木盛而火亦旺之局，象征生机过旺、偏躁之象。
  - 煞逢食制：七煞被食神克制，煞不再为害之局。
  - 透印无功：印星透出，却起不到护身、护煞的正面作用，反而碍事。
  - 官用食破：官格被食神破坏。
  - 印用财破：印格被财星破坏。
  - 参苓芪术：人参、茯苓、黄芪、白术等补益之药，比喻吉神。
  - 生扶：生助、扶助某一行或某一用神，使其力量增强。
  - 裁抑：克制、削弱某一行的力量。
  - 合于需要：与整体气候、格局、强弱所需相符合。

- **规范化释义（primary_lang_explained）**：
  作者在这一章中提醒我们：不要因为财、官、印、食往往被称为“吉神”，就认为多多益善。一旦不顾实际需要胡乱添加，即使是“吉神”，也会变成破局的力量。

  文中列举的四种情况，可以概括为：“吉神用过头，反成破格”：
  1) **食神带煞而透财为害**：
     - 食神带煞，本来是“以柔制刚”的格局，食神克煞而生财、泄身成秀；
     - 但若财星透得过多，财一方面泄食、夺食神之力，另一方面又去生煞，使煞得财而更为有力，原本“食制煞”的格局就会被财所破。
  2) **春木火旺而见官则忌**：
     - 春天木旺，若火又旺，局中便容易偏燥、偏烈；
     - 此时再透官星，官火反成引动过旺之气的力量，使局偏于炎上，反而有害。
  3) **煞逢食制而透印无功**：
     - 本来“煞逢食制”是佳局，食神克煞使煞不为害；
     - 若再透印星来生身、护煞，印一方面增强日主，一方面也助煞生身，使食神难以克服煞气，反令格局浑浊，印沦为破格之神。
  4) **财旺生官而露食则杂**：
     - 财旺生官，本为中正之局；
     - 若再露食神，食神生财，财生官，使生克路线变得过长过杂，原本清晰的“财生官”格局被食神搅乱，食神也变为破格之力。

  最后，作者用“用药”来为本章收束：
  - 人参、茯苓、黄芪、白术等药，自身都是补益之品，但若用之失宜，也会伤人；
  - 财、官、印、食亦然：
    - 身弱者喜生扶，身强者却可能因生扶而祸起；
    - 衰者忌克制，太旺者反要靠克制来平衡；
- **完整对等诠释（secondary_lang_full）**：  
  This chapter cautions that the so‑called Four Beneficent Gods—Wealth, Officer, Resource and Food God—are not automatically auspicious, and that adding more of them without regard to need will damage rather than complete the pattern. It first lays out four classic situations in which overusing these "good" stars breaks the structure: (1) in a Food‑controlling‑Killing setup, excessive Wealth drains the Food God's power while simultaneously feeding Killing, so the very star that was meant to produce Wealth becomes the source of imbalance; (2) when Wood and Fire are already blazing in spring, introducing additional Officer Fire only fans the flames, turning what should be upright authority into overheating and scorch; (3) when Killing is already well controlled by Food, exposing strong Resource to protect both the Day Master and Killing weakens Food's restraining force and muddies the pattern; (4) in a chart where Wealth properly generates Officer, exposing Food God on top makes the generating chain Food → Wealth → Officer too long and tangled, so the once‑clear "Wealth generating Officer" structure becomes mixed and unstable.

  To drive the point home, the author uses the analogy of medicine: ginseng, poria, astragalus and atractylodes are all fine tonics, yet if prescribed without reference to the patient's actual condition they can harm rather than heal. In the same way, Officer, Wealth, Resource and Food each have contexts in which they are joyful and contexts in which they are feared: Officer dislikes being attacked by expressive stars such as Food and Hurting Officer, Wealth fears contention from Peers and Rob Wealth, Resource can be broken by excessive Wealth, and Food God can be stolen by Resource. The real criterion is never the label "beneficent" or "malefic" but whether a given star answers what the pattern truly lacks. A weak structure welcomes support, while an already excessive structure may be ruined by further reinforcement; a declining pattern cannot bear harsh control, while an overgrown pattern actually benefits from appropriate restraint. Auspiciousness and inauspiciousness therefore depend entirely on matching the dosage of these stars to the chart's real needs, not on their names.

  - 因此吉凶喜忌的判断，必须建立在“是否合于需要”的基础上，而不是只看“这颗是吉星还是凶星”的标签。

- 详细解说：
  - 本章进一步打破“神煞名称决定吉凶”的迷思：
    - 四吉神固然常为用神，但并非绝不会破坏格局；
    - 四凶神（煞、伤、枭、刃）在后章又被说明“施之得宜亦能成格”。
  - 核心思想与中医用药观念极其相似：
    - 药无绝对之吉凶，惟看“证”之虚实寒热；
    - 星无绝对之贵贱，惟看“局”之强弱寒燥与结构需要。
  - 也承接前文“因成得败、因败得成”的逻辑：
    - 很多时候，破格之力正是由原本“成格之力”演化而来，只因用之过度或方向失当；
    - 同一颗星，在不同局、不同运中可以扮演完全不同的角色。

- 核心要点：
  - 四吉神虽名为吉，但在以下情况下可以破格：
    1) 食神本用于制煞，却被财过度泄力、反助煞；
    2) 火气已盛，又透官星助火，官不再中正；
    3) 煞已受制，印再生身护煞，使制煞之力反弱；
    4) 财官本清，食神再出，使生克线路过长过杂。
  - 判断吉凶时应先问：“日主与格局的虚实如何？当前这颗吉神，是在补不足，还是锦上添花以致过头？”
  - 生扶与裁抑的取舍，必须与“强弱判定”和“调候需要”结合，不能机械套用“见财喜财、见官喜官”的公式。

- 应用推演：
  1) 在判断格局后，列出局中财、官、印、食的强弱与位置；
  2) 对照本章四种典型破格路径，标记潜在“吉神破格点”；
  3) 在岁运分析中，观察对应的岁运是否进一步强化这些“过头”的吉神；
  4) 在用命建议中，提醒当事人：
     - 身弱者勿再贪“旺财旺官”，以免被压垮；
     - 身强者勿盲目追求再扶身，以免破坏格局之平衡。

- 反例与边界：
  - 只要见财官印食就一味称吉，不顾局中是否已经偏旺或结构是否因此变杂；
  - 把“食神带煞”“煞逢食制”等格局当作固定公式，而不看其中财、印是否介入破坏；
  - 把某一颗吉神在某一命例中的良好表现，推广为该神在一切命局中的“万能良药”。


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_327]` `[trigger: 第23章要点]` `[factor_trigger: chapter=23 AND hexin_lunshu]` `[role: 主干]` 本章核心论述。 → 《子平真诠》#中卷第23章
  - `[ns_zpzy_328]` `[trigger: 吉神破格例]` `[factor_trigger: caiduo_shenruo AND jishen_fan_cheng_jishen]` `[role: 主干]` 财多身弱，吉神反成忌神。 → 《子平真诠》#中卷
  - `[ns_zpzy_329]` `[trigger: 辰戌丑未]` `[factor_trigger: branch IN (chen, xu, chou, wei) AND simu_ku]` `[role: 主干]` 辰戌丑未为四墓库。 → 《子平真诠》#中卷
  - `[ns_zpzy_330]` `[trigger: 冲开库门]` `[factor_trigger: chong_kai_kumen AND caiguan_shi_xian]` `[role: 主干]` 冲开库门，财官始显。 → 《子平真诠》#中卷
  - `[ns_zpzy_331]` `[trigger: 库中藏干]` `[factor_trigger: kuzhong_canggan AND tougan_fang_yong]` `[role: 主干]` 库中藏干，透干方用。 → 《子平真诠》#中卷
  - `[ns_zpzy_332]` `[trigger: 库中有物]` `[factor_trigger: kuzhong_youwu AND chong_zhi_ze_chu]` `[role: 主干]` 库中有物，冲之则出。 → 《子平真诠》#中卷
  - `[ns_zpzy_333]` `[trigger: 入墓之忌]` `[factor_trigger: rigan_rumu AND buli_zishen]` `[role: 主干]` 日干入墓，不利自身。 → 《子平真诠》#中卷
  - `[ns_zpzy_334]` `[trigger: 未为木库]` `[factor_trigger: wei=muku AND feng_chong_ze_mu_rong]` `[role: 主干]` 未为木库，逢冲则木荣。 → 《子平真诠》#中卷
  - `[ns_zpzy_335]` `[trigger: 库中透干]` `[factor_trigger: kuzhong_tougan AND geju_nai_cheng]` `[role: 主干]` 库中透干，格局乃成。 → 《子平真诠》#中卷
  - `[ns_zpzy_336]` `[trigger: 库不见冲]` `[factor_trigger: ku_bujian_chong AND caiguan_nan_xian]` `[role: 主干]` 库不见冲，财官难显。 → 《子平真诠》#中卷
  - `[ns_zpzy_337]` `[trigger: 用神有力]` `[factor_trigger: yongshen_youli=true AND result=fugui_keqi]` `[role: 主干]` 用神有力，富贵可期。 → 《子平真诠》#中卷
  - `[ns_zpzy_338]` `[trigger: 月令当权]` `[factor_trigger: yueling_dangquan AND yongshen_zhi_fu]` `[role: 主干]` 月令当权，用神之府。 → 《子平真诠》#中卷"""
    normalized_text_zh: str = """"""
    subject: str = "四吉神的反向作用：用之不当亦破格"
    factor_refs: list = ['engine_id', 'bazi_condition_degree', 'bazi_structure_factor', 'bazi_condition_factor', 'bazi_state_factor', 'bazi_boundary_unnamed', 'source_ref', 'rel_zpzq_sijishen_01', 'jishen_guotou', 'rel_zpzq_sijishen_02', 'jishen_jieru', 'source_ref', 'evi_zpzq_sijishen_01', 'evi_zpzq_sijishen_02', 'map_zpzq_sijishen_01', 'map_zpzq_sijishen_02']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_四吉神的反向作用_用之不当亦破格_001_L1",
    )
    version: str = "1.0.0"
