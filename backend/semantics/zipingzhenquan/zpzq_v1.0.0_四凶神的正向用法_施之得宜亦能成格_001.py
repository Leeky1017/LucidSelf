"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.465631
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
    semantic_id="zpzq_v1.0.0_四凶神的正向用法_施之得宜亦能成格_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 四凶神的正向用法施之得宜亦能成格(SemanticEntry):
    """
    - **原文（source_text）**：
  十九、论四凶神能成格。
  煞伤枭刃，四凶神也，然施之得宜，亦能成格。如印绶根轻，透煞为助，煞能成格也。财逢比劫，伤官可解，伤能成格也。食神带煞，灵枭...
    """
    
    original_text: str = """- **原文（source_text）**：
  十九、论四凶神能成格。
  煞伤枭刃，四凶神也，然施之得宜，亦能成格。如印绶根轻，透煞为助，煞能成格也。财逢比劫，伤官可解，伤能成格也。食神带煞，灵枭得用，枭能成格也。财逢七煞，刃可解厄，刃能成格也。

  是故财不忌伤，官不忌枭，煞不忌刃，如治国长抢大戟，本非美具，而施之得宜，可以戡乱。

- 原注（原文注解）：
  　　在上一章指出“四吉神用之不当亦能破格”之后，本章转而说明：**四凶神（煞、伤、枭、刃），若用得其所，亦能成格。**
  - 首句“煞伤枭刃，四凶神也”，点明这四类十神常被视为凶神：
    - 煞：七煞，偏刚之权；
    - 伤：伤官，刚烈之才；
    - 枭：偏印，夺食之印；
    - 刃：阳刃，与日主同旺而争强。
  - 然而，作者接着指出：“然施之得宜，亦能成格”，并给出四类典型用法：
    1) 印绶根轻，透煞为助，煞能成格：身弱印轻，若透煞生印、扶正，七煞反成印格之助；
    2) 财逢比劫，伤官可解，伤能成格：财多而比劫争财，若伤官出面分化比劫、泄身以护财，伤官便有其正用；
    3) 食神带煞，灵枭得用，枭能成格：食神带煞之局，若枭印得势，一方面制食、一方面生身，使局化险为奇；
    4) 财逢七煞，刃可解厄，刃能成格：财被七煞所夺，若阳刃既帮身又制煞，便能解厄，使财煞得其平衡。
  - 末句以“治国长抢大戟”作比：
    - 长枪大戟本非乐器，而是战乱之用；
    - 然而在乱世，用之得宜，可以平定叛乱；
    - 同理，煞伤枭刃平时多为凶，然在合适的情境与结构中，却是成格之关键。

- 分字分词释义：
  - 四凶神：煞、伤、枭（偏印）、刃四类十神，通常被视为凶险之力。
  - 印绶根轻：印星根气不足、力量不够。
  - 透煞为助：七煞透出干头用以生印或扶格。
  - 财逢比劫：财星遭遇比肩劫财争夺之局。
  - 伤官可解：以伤官泄身、分化比劫之力，从而护财。
  - 食神带煞：食神格中见七煞相随，食与煞并见。
  - 灵枭得用：枭印用得其所，既制食，又扶身。
  - 财逢七煞：财星与七煞同时出现，财常被煞夺。
  - 刃可解厄：阳刃帮助日主抵御七煞之攻，充当“挡刀”的角色。
  - 戡乱：平定叛乱、治理动乱局势。

- **规范化释义（primary_lang_explained）**：
  前一章讲“财官印食等吉神若用失宜亦能破格”，本章则反过来说明：“煞伤枭刃等凶神，若施用得当，也能成就格局”。

  作者用四种情形概括四凶神的正向用法：
  1) **印弱逢煞生印**：
     - 印绶根轻，本难护身护格；
     - 若七煞透出，生印相扶，使印格得以成立，则“煞”反而成了格局所赖之助神。
  2) **财逢比劫而伤官解之**：
     - 财多而比劫兴旺，为争财之象；
     - 若伤官出面，一方面泄身、一方面牵制比劫，使比劫无力全抢财，反令财得其用，伤官便由“凶”转“功”。
  3) **食神带煞而枭印得用**：
     - 食神带煞，本有风险：食泄身又克官煞，容易偏离正统；
     - 若枭印透出，一方面制食、稳住身，一方面化煞生印，便形成“灵枭得用”的奇格。
  4) **财逢七煞而刃解其厄**：
     - 财星遇七煞，本主“煞夺财”；
     - 若阳刃同时有力，一则帮身、一则制煞，使煞无力尽夺财，反令财、煞、身三者在紧张中取得平衡。

  - 四凶神的正用，往往出现在：
    - 局中已有潜在失衡（如印弱、财被劫、食带煞而无制、财遭七煞）；
    - 凶神提供了一条“逆向支撑”的路径，使局得以维持动态平衡。
  4) 在岁运分析中，观察运来是否强化或削弱这些正用：
     - 正用被扶助，则格局更显奇贵；
     - 正用被破坏，则原来维持平衡的“兵器”失灵，局易失守。

- **完整对等诠释（secondary_lang_full）**：  
  This chapter pairs with the previous discussion of the Four Beneficent Gods by turning the lens toward the Four Malefic Gods—Seven Killings, Hurting Officer, Indirect Resource and Yang Blade—and asking when they can in fact rescue a pattern rather than ruin it. The key idea is that in a chart which already has a structural weakness, a carefully placed "dangerous" star can supply exactly the counter‑force that the usual gentle stars cannot provide. Killing that generates Resource for a weak Ink structure, Hurting Officer that disperses Rob Wealth in a chart where Wealth is under siege, Indirect Resource that reins in an over‑strong Food God while quietly nurturing the Day Master, or Yang Blade that both supports the Day Master and stands up to Seven Killings—each of these is an example of using sharp weapons in a time of disorder.

  As with medicine, dosage, timing and indication are everything. When these Malefic Gods are rooted, acting through clear, emotionally coherent links to the Useful Gods, and aimed precisely at the chart's main shortcoming, they become tools for restoring balance in a high‑tension system. When they lack roots, pile on top of an already aggressive structure, or attack the Day Master or Useful God directly without any buffering, they remain pure sources of harm. The author therefore urges us to move beyond the reflex of "seeing evil, immediately fearing it" and instead to ask: what is actually missing here, and is this harsh star filling that gap or merely increasing volatility? Only in the former case does a so‑called凶神 truly "form a noble pattern".

- 详细解说：
  - 本章与前一章成对出现，意在打破“吉神永远吉、凶神永远凶”的二元划分：
    - 财官印食若用失宜，可以从补益变为累赘；
    - 煞伤枭刃若用得其所，则能在失衡之处搭起一根“钢梁”，托住全局。
  - 所谓“四凶神能成格”，并非鼓吹追求奇险，而是指出几个明确的前提：
    - 原局必须先有清楚的短板与倾斜（如印根太轻、财被比劫、食带煞而无制、财遭七煞）；
    - 凶神须有根、有源，且与用神之间是“有情”的生克，不是孤立横冲直撞；
    - 凶神的力量要“恰到好处”，只是补上缺口，而不是反向压垮整体。
  - 文中四个典型情形，各自展示了“以恶制恶、以偏扶正”的思路：
    - 煞生印：看似凶狠的七煞，若用来生印，反而扶起本来不足的印格；
    - 伤解劫：本为凶星的伤官，在财被比劫争夺时，反而可泄身、牵制比劫，护住财源；
    - 枭制食：枭印多被畏惧为夺食之神，在食神过旺、带煞时，却可一面制食、一面化煞生印；
    - 刃解厄：阳刃本与日主争强，置于财逢七煞之局中，却可一手扶身、一手牵制七煞，减轻“煞夺财”的剧烈度。
  - 从实务角度看，本章的用意不在于罗列新名目，而在于训练一种判断顺序：
    1) 先看局中真正的短板与隐患在哪里；
    2) 再看凶神与该短板之间是否形成有根、有情的补位关系；
    3) 最后才评估其力度是否过轻、过重，能否经得起岁运的反复放大。

- 核心要点：
  - 四凶神“能成格”的前提：
    - 原局已有明确短板（印弱、财被劫、食带煞、财遭七煞）；
    - 煞、伤、枭、刃有根有情，与用神之间形成“有情”生克，而非孤立暴烈之攻伐；
    - 力量适中，只是扶偏、补缺，而非另起一个更大的偏激中心。
  - 四个典型路径可概括为：
    1) 煞生印 → 在印弱局中，以七煞生印扶格；
    2) 伤解劫 → 在财被比劫之局中，以伤官泄身、牵制比劫护财；
    3) 枭制食 → 在食神带煞且食过旺时，以枭印制食、化煞生印；
    4) 刃解厄 → 在财逢七煞时，以阳刃扶身并牵制七煞，平衡财煞身三者。
  - 判断四凶神时，必须先问：“它是在补哪一块短板？”而非只看“名为凶神便一概弃之”。
  - 岁运分析中，应特别观察：
    - 运来是否扶助这条“险中求平衡”的链条，使其更稳；
    - 还是削弱了关键一环，令原本勉强维持的平衡被打破。

- 反例与边界：
  - 见煞、伤、枭、刃就一概断为凶，不看其是否在结构上有正用；
  - 反过来，一见这些“奇格”就硬说成贵格，不看身、用、相三者是否真能承受；
  - 把“煞生印”“伤解劫”“枭制食”“刃解厄”等口诀当作随处可用，而不检视是否有根、有情、有度。

- 小例（示意）：
  - 一命印轻而煞旺，煞生印格成，行印煞相生之运反而发科甲，是“煞能成格”的写照；
  - 一命财重比劫亦重，伤官透出泄身解劫，行伤官运反而财源渐稳，是“伤能成格”的实际例子；
  - 某命食神带煞而枭印有根，行枭印之运，往往以专业研究、逆向思维见长，枭神反成才华之根；
  - 又一命财逢七煞而身有阳刃，青年行刃煞制衡之运，可见历练与突破；若中晚运刃衰煞盛，则需防“刀已钝而敌犹在”。

- 校勘与字词辨析：
  - “煞伤枭刃，四凶神也”一句，与下文“财官印食，四吉神也”相对，构成对子，提示读者两章需联系阅读；
  - “如治国长抢大戟，本非美具，而施之得宜，可以戡乱”中“抢”多本作“枪”，今从底本“抢”字，释义仍按“长枪大戟”理解。


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_339]` `[trigger: 第22章要点]` `[factor_trigger: chapter=22 AND hexin_lunshu]` `[role: 主干]` 本章核心论述。 → 《子平真诠》#中卷第22章
  - `[ns_zpzy_340]` `[trigger: 凶神成格例]` `[factor_trigger: sha_feng_shi_zhi AND xiongshen_zhuan_cheng_guiqi]` `[role: 主干]` 煞逢食制，凶神转成贵气。 → 《子平真诠》#中卷
  - `[ns_zpzy_341]` `[trigger: 辰戌丑未]` `[factor_trigger: branch IN (chen, xu, chou, wei) AND simu_ku]` `[role: 主干]` 辰戌丑未为四墓库。 → 《子平真诠》#中卷
  - `[ns_zpzy_342]` `[trigger: 冲开库门]` `[factor_trigger: chong_kai_kumen AND caiguan_shi_xian]` `[role: 主干]` 冲开库门，财官始显。 → 《子平真诠》#中卷
  - `[ns_zpzy_343]` `[trigger: 库中藏干]` `[factor_trigger: kuzhong_canggan AND tougan_fang_yong]` `[role: 主干]` 库中藏干，透干方用。 → 《子平真诠》#中卷
  - `[ns_zpzy_344]` `[trigger: 财官入库]` `[factor_trigger: caiguan_ruku AND feng_chong_ze_fa]` `[role: 主干]` 财官入库，逢冲则发。 → 《子平真诠》#中卷
  - `[ns_zpzy_345]` `[trigger: 印绶入库]` `[factor_trigger: yinshou_ruku AND xueye_nan_cheng]` `[role: 主干]` 印绶入库，学业难成。 → 《子平真诠》#中卷
  - `[ns_zpzy_346]` `[trigger: 财入库中]` `[factor_trigger: cai_ru_kuzhong AND fu_er_neng_shou]` `[role: 主干]` 财入库中，富而能守。 → 《子平真诠》#中卷
  - `[ns_zpzy_347]` `[trigger: 官入库中]` `[factor_trigger: guan_ru_kuzhong AND quan_zai_anchu]` `[role: 主干]` 官入库中，权在暗处。 → 《子平真诠》#中卷
  - `[ns_zpzy_348]` `[trigger: 印入库中]` `[factor_trigger: yin_ru_kuzhong AND xueye_chi_cheng]` `[role: 主干]` 印入库中，学业迟成。 → 《子平真诠》#中卷
  - `[ns_zpzy_349]` `[trigger: 用神无力]` `[factor_trigger: yongshen_wuli=true AND result=pinjian_nanmian]` `[role: 主干]` 用神无力，贫贱难免。 → 《子平真诠》#中卷
  - `[ns_zpzy_350]` `[trigger: 年柱根基]` `[factor_trigger: nianzhu_genji AND zuye_zhigong]` `[role: 主干]` 年柱根基，祖业之宫。 → 《子平真诠》#中卷"""
    normalized_text_zh: str = """"""
    subject: str = "四凶神的正向用法：施之得宜亦能成格"
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_四凶神的正向用法_施之得宜亦能成格_001_L1",
    )
    version: str = "1.0.0"
