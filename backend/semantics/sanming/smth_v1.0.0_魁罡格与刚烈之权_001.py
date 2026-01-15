"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412443
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
    semantic_id="smth_v1.0.0_魁罡格与刚烈之权_001",
    book_id="sanming",
    engine_id="bazi"
)
class 魁罡格与刚烈之权(SemanticEntry):
    """
    - **原文（source_text）**：

  此格有四日：庚辰、壬辰、戊戌、庚戌。辰为天罡，戌为河魁，乃阴阳绝灭之地，故名。独除甲干，以居干之首，在辰为青龙，在戊为禄堂，有吉而无凶故也。此格须叠...
    """
    
    original_text: str = """- **原文（source_text）**：

  此格有四日：庚辰、壬辰、戊戌、庚戌。辰为天罡，戌为河魁，乃阴阳绝灭之地，故名。独除甲干，以居干之首，在辰为青龙，在戊为禄堂，有吉而无凶故也。此格须叠化重逢日位，加临者众，以伏为贵。经云：魁罡聚众，发福非常，主为人性格聪明，文章振发，临事果断，秉权好杀。赋云：魁罡性严有操持，而为人聪敏是也。运行身旺，发福百端，一见财官，祸患立至，或带刑煞尤甚，倘日位独处，刑冲克制重临，必是小人，刑责不巳，穷必彻骨，运临财官旺处，主防奇祸。若月令见财官印绶，日主一位，即以财官印食取用，虽微有破败，财官印食得位，亦无大害，须斟酌提纲，当用者取之，不可拘以小节。又曰：庚戌、庚辰二日，无官星，若魁罡重叠有情，主富高于名，但见财则不成局，岁运再见财旺之乡，祸不可测。庚辰日生九月，虽辰戌相冲，运行南方，柱中有火，亦可言贵。庚戌日生三月，纵有官星印绶亦不用，盖庚用戌中火为官库，戊土为印，辰中癸水伤官，又泄庚气，不成格矣。戊戌日无财不贵，不宜见官，若魁罡重叠有情，富贵两全。壬辰日怕见财官，大喜印绶、却财与煞，岁运同。又曰：辰是水库属天罡，戌是火库属地魁，辰戌相见，为天冲地击。《子平总论》云：身值天罡地魁，衰则彻骨贫寒，强则绝伦贵显。诗曰：壬辰庚戌与庚辰，戊戌魁罡四座神，不见财官刑煞并，身行旺地贵夫伦。又：魁罡四日最为先，叠叠相逢掌大权，庚戌庚辰怕官显，戊戌壬辰畏财连。又：魁罡四柱日多同，贵气朝来在此中，日主独逢冲克重，财官显露祸无穷。按此格，俱用辰戌，独天干少异，内庚辰二日，既曰日德，又曰魁罡，论其格局，迥然不同，不必拘论。如张时佥事：庚午、丁亥、戊戌、丙辰；刘大受少卿：丁亥、癸丑、庚戌、戊寅，二命魁罡日，只取财官印是也。

- 分字分词释义：

  - **辰为天罡，戌为河魁，乃阴阳绝灭之地**：辰、戌分别为水库、火库，象征阴阳极点之处，故以“天罡、地魁”名之。
  - **四日：庚辰、壬辰、戊戌、庚戌**：限定四个日柱，为魁罡格的基础条件。
  - **叠化重逢日位，加临者众，以伏为贵**：魁罡之气重叠出现，若能“伏而不发”，为暗藏权势；若过于张扬，则易成祸源。
  - **性格聪明、果断、秉权好杀**：描述魁罡日主的典型性格：聪慧而果断，敢于执权，但也易偏向刚烈与好胜。
  - **一见财官，祸患立至**：魁罡之气本已刚猛，再逢财官旺极，容易因权势、利欲而招祸，尤忌刑煞同来。
  - **辰戌相见，为天冲地击**：辰戌对冲，象征天罡地魁对撞，若制约失衡，则主剧烈波动与大起大落。
  - **庚辰既曰日德，又曰魁罡**：提示同一日柱可被不同格局吸纳：日德看其德厚，魁罡看其刚烈掌权，用法并不相同。

- **规范化释义（primary_lang_explained）**：

  魁罡格，是以庚辰、壬辰、戊戌、庚戌四日为核心的一种“刚烈掌权之格”。辰为天罡、戌为地魁，皆属阴阳极处之地，故四日之人多带有强烈的阳刚之气：聪明、果断、能执权、好决断，但亦可能有好杀、刚猛的一面。原文强调，“魁罡聚众，发福非常”，当身旺、运旺而魁罡之气得以善用时，往往有非常之富贵与权势；但若财官过重、刑煞并见，则刚猛之气易由“为我所用”转为“反噬自身”，祸患顿起。

  文中多次提醒：魁罡怕见财官与刑煞同来，尤其在身弱或大运不利时，更容易表现为官灾、刑罚、贫困乃至夭折。反之，若月令带财官印绶而能为日主所用，或魁罡之气得以伏藏、不过度张扬，则可以在强势中兼具文才与操持能力，成为掌权而不乱权的人物。因此，魁罡之贵与其说是“格局使然”，不如说更依赖于日主强弱与整体格局的收放得当。

- 核心要点：

  - 魁罡格只取庚辰、壬辰、戊戌、庚戌四日，重在“刚烈、掌权”。
  - 身旺、魁罡聚而能伏、能为我用，则富贵非常；身弱或魁罡过重而再见财官刑煞，则多祸患。
  - 同一日柱（如庚辰）既可论日德、亦可论魁罡，取用时须结合整体局势决定偏重何者。
  - 辰戌相冲为“天冲地击”，一旦调和失当，往往主大起大落甚至奇祸。

- 详细解说：

  与日德格相比，魁罡格更强调“力”而非“德”。日德讲的是阳干坐德、以德行护身；魁罡讲的是辰戌之刚、以强势开路。若将两者放在同一命局中考察，就会发现一个简单的原则：德足以载权，则魁罡成其为“大权在握、而不滥用”；德不足以载权，则魁罡易流于“刚愎自用、招祸惹非”。

  因此，在实务判断时，解读魁罡格不可只看“四日入格”，还要细看：
  
  1. 日主强弱：身强则能驭罡，身弱则易被罡气所伤；
  2. 财官多寡：财官得宜则成名利之阶，过多则成祸患之源；
  3. 印绶有无：印足则能约束魁罡的刚烈，使之转化为担当与操持；
  4. 与其他格局的关系：如同时具备日德等柔和格局，则宜以德节制魁罡之力。

- **校勘与字词辨析（双语）**：

  - 原文“辰为天罡，戌为河魁，乃阴阳绝灭之地”一句，本稿在释义中以“水库、火库”加以解释，便于理解其“极点”含义。
  - 对“魁罡聚众，发福非常”之语，本稿在白话中解释为“魁罡之气重叠、且能为我所用时，富贵与权势往往非常”，避免误解为凡见魁罡必大贵。
  - 文末对庚辰既属日德又属魁罡的说明，本稿在详细解说中明确“用德、用罡”两种不同取法，以提醒后续层级判断时不可混为一谈。
  - **English**：
    - The sentence "Chen is Tiangang, Xu is Hekui, the places where Yin-Yang terminate" is explained with "water storage, fire storage" to clarify the "extreme point" meaning.
    - The explanation that Geng-Chen belongs to both Day-Virtue and Kuigang is clarified in the detailed commentary as "using Virtue" vs "using Gang" — two different approaches that should not be confused.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_077]` `[trigger: 魁罡格定义]` `[factor_trigger: kuigang_ge_presence]` `[role: 主干]` 此格有四日：庚辰、壬辰、戊戌、庚戌。辰为天罡，戌为河魁，乃阴阳绝灭之地。 → 《三命通会》卷六#魁罡
  - `[ns_smth_06_078]` `[trigger: 魁罡聚众]` `[factor_trigger: kuigang_ju_zhong AND fa_fu_fei_chang]` `[role: 主干依赖]` 魁罡聚众，发福非常，主为人性格聪明，文章振发，临事果断，秉权好杀。 → 《三命通会》卷六#魁罡
  - `[ns_smth_06_079]` `[trigger: 忌见财官]` `[factor_trigger: yi_jian_cai_guan OR dai_xing_sha]` `[role: 条件分支]` 一见财官，祸患立至，或带刑煞尤甚。 → 《三命通会》卷六#魁罡
  - `[ns_smth_06_080]` `[trigger: 衰则贫强则贵]` `[factor_trigger: shuai_ze_pin_qiang_ze_gui]` `[role: 总结]` 身值天罡地魁，衰则彻骨贫寒，强则绝伦贵显。 → 《三命通会》卷六#魁罡"""
    normalized_text_zh: str = """"""
    subject: str = "魁罡格与刚烈之权"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_19', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_degree_3', 'bazi_semantic', 'bazi_state_factor_13', 'bazi_semantic', 'bazi_condition_factor_156', 'bazi_semantic', 'bazi_condition_chongke_1', 'bazi_semantic', 'source_ref', 'rel_smth_06_058', 'kuigang_ge_presence', 'rel_smth_06_059', 'kuigang_chongdie_fucang', 'rel_smth_06_060', 'caiguan_chonggang_risk', 'evi_smth_06_058', 'kuigang_ge_presence', 'rule_kuigang', 'evi_smth_06_059', 'kuigang_chongdie_fucang', 'rule_kuigang_ji', 'evi_smth_06_060', 'caiguan_chonggang_risk', 'rule_caiguan_huo', 'map_smth_06_039', 'map_smth_06_040']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_魁罡格与刚烈之权_001_L1",
    )
    version: str = "1.0.0"
