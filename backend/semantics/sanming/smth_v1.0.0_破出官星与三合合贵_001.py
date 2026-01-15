"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412255
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
    semantic_id="smth_v1.0.0_破出官星与三合合贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 破出官星与三合合贵(SemanticEntry):
    """
    - **原文（source_text）**：
    四柱元无财官印绶，却有破官之辰，如癸卯日破出午中己土为官，癸酉日破出辰中戊土为官，甲午日破出酉中辛金为官，柱中须得一字三合合住贵气为妙。《元理赋》...
    """
    
    original_text: str = """- **原文（source_text）**：
    四柱元无财官印绶，却有破官之辰，如癸卯日破出午中己土为官，癸酉日破出辰中戊土为官，甲午日破出酉中辛金为官，柱中须得一字三合合住贵气为妙。《元理赋》云：卯破午，午破酉，财官双美。又云：年日支无破官之辰，月时支有破官合官之辰，主贵。如甲寅日无破，月逢丙午，时临己巳，此取午破酉中辛官，有巳合之，又用巳中丙戊合辛，为贵。诗曰：卯破午未有大官，午未破酉一般看，丑破巳午不为例，子破卯辰用不难。
    - 分字分词释义：
    - **四柱元无财官印绶**：命局表面不见财星、官星、印绶等用神，只能从“破出”的支神中取官。
  - **破官之辰**：通过刑冲合会，破开某支，冲出其内所藏之官星，使之由暗转明的关键支位。
  - **癸卯破午中己土为官**：癸水日主本无明官，却以卯破午，冲出午中己土为官星。
  - **一字三合合住贵气**：须有一字（如巳、亥等）与所破之支配合三合、拱合，将冲出的官星贵气合住，不致散失。
  - **卯破午，午破酉，财官双美**：《元理赋》总结破官与财官双美的格局关系：卯破午、午破酉，既得官又兼得财。
  - **年日支无破官之辰，月时支有破官合官之辰**：年、日两支本无破官位置，而在月、时支出现既能破官又能合官的支位，主贵。
  - **不为例 / 用不难**：丑破巳午不为例，子破卯辰用不难，说明不同组合中破出的官星力量与可用程度有差异。
    - 白话原意：
    破官格，专讲“本局无官而从破中取官”。凡四柱表面不见财、官、印绶，却有特定的“破官之辰”，可以通过刑冲把某支中的官星冲破引出，再以三合合住，使之成为可用的官星。原文以癸卯日、癸酉日、甲午日为例：
    - 癸卯日：卯破午，破出午中己土为官；
  - 癸酉日：某支破辰，破出辰中戊土为官；
  - 甲午日：破出酉中辛金为官。
    但仅破出官星还不够，柱中还须有一字能与被破之支构成三合或拱合，将贵气“合住”。例如甲寅日原无破，若月逢丙午、时临己巳，则以午破酉中辛官，再用巳合午、丙戊合辛，使官星得地而成贵格。古人以“卯破午未有大官，午未破酉一般看，丑破巳午不为例，子破卯辰用不难”一首歌诀，总结不同破官组合的高低与难易。
    - **完整对等诠释（secondary_lang_full）**：
      The "Breaking-Out Official" pattern addresses charts where the four pillars show no obvious wealth, official or Seal stars on the surface, yet contain particular "breaking-out" branches that can crack open another branch and release the hidden official star within. The classical examples include Gui-Mao day where Mao breaks Wu and draws out Ji earth as Gui's official; Gui-You day where the chart breaks Chen to extract Wu earth as official; and Jia-Wu day where the structure breaks You to reveal Xin metal as official. The key requirement is that once the official is broken out, the chart must also contain a branch that can form a three-harmony or arching combination with the broken branch to "clasp and hold" the released noble qi, preventing it from scattering. The Yuanli Fu summarises the principle as "Mao breaks Wu, Wu breaks You—wealth and official both beautiful", indicating that certain breaking sequences can simultaneously access both wealth and official stars from concealment.

      The text emphasises that the most auspicious configuration occurs when the year and day branches carry no breaking positions, while the month and hour branches contain branches that both break and combine officials. This places the dynamic action in the timing sectors rather than the foundation. For instance, a Jia-Yin day that originally shows no breaking action may gain it when the month brings Bing-Wu and the hour brings Ji-Si: Wu breaks the hidden Xin official in You, Si then combines with Wu to stabilise the released qi, and the Bing and Wu within Si further harmonise with Xin to create a coherent official structure. The verse "Mao breaks Wu-Wei to find great official, Wu-Wei breaking You is judged the same; Chou breaking Si-Wu is not the usual case, Zi breaking Mao-Chen is easy to use" catalogues different breaking pathways and their varying power. In practice we must weigh not only whether the official can be broken out, but also whether the body is strong enough to shoulder it, whether the breaking force is excessive, and whether later fortunes reinforce or damage the delicate balance between break and hold.

    - 核心要点：
    - 破官格以**无明官、从破中取官**为前提，若命局已有官星透干，则不必再以破官论。
  - 仅“破出”官星还不够，必须有三合、拱合或合局来“合住贵气”，否则官星易散难用。
  - 破官之辰多在月、时支，年、日为本体，月、时为机缘，故“年日支无破官之辰，月时支有破官合官之辰”尤主发贵。
  - 不同破法（卯破午、午破酉、丑破巳午、子破卯辰）力量不一，应结合日主强弱与全局气势来权衡。
    - 详细解说：
    与前文“冲合禄马”“遥巳禄”等格局类似，破官格同样属于“从隐处起用”的类型，只是这里起用的是官星而非禄马。其思路可分为三步：
    1. **确立前提**：四柱本无明财官印绶，或有之极弱，不足以担当大用；
  2. **寻找破官之辰**：找出能冲破官星所藏之支的关键支位，如卯破午、午破酉、子破卯辰等；
  3. **合住贵气**：以三合、拱合或合局之字，将破出的官星摄住，使其不致再受冲散或刑害。
    以甲寅日例来看：本无破官之辰，若月逢丙午、时临己巳，则午可破酉中辛官，巳又与午合局，并以巳中丙戊去合辛，使官星既得根，又得印与财的配合，从而成就贵格。若只见破而无合，则官星虽出，反易被视为冲动是非、官灾之源。
    实务中，判断破官格时需特别注意：
  - 一方面，破官之力不可过重，以免伤及本体，尤其在日主身弱时，破官易变为官煞交侵；
  - 另一方面，若命局本已有清正之官星，强行再以破官格论之，往往会夸大冲动之力，而忽视原有官格的清贵稳重。
    - **校勘与字词辨析（双语）**：
    - 原文“卯破午，午破酉，财官双美”承自《元理赋》，本稿据底本保留，仅在释义与白话中指出其所指为“从破中同时得财官”的格局。
  - “丑破巳午不为例，子破卯辰用不难”一联，提示某些破法不宜轻用，某些则较易成格，本稿不另作改训，仅在详细解说中强调“需结合全局气势判断”。
  - 文中“年日支无破官之辰，月时支有破官合官之辰，主贵”一句，概括了破官格的发力位置，本稿在释义与详细解说中予以展开。
  - **English**：
    - The phrase "Mao breaks Wu, Wu breaks You, wealth-official double beauty" from Yuanli Fu is preserved; this edition notes it refers to obtaining both wealth and official through breaking.
    - The couplet warning that some breaking methods should not be used lightly is kept without alteration; detailed explanation emphasizes "judge according to overall momentum."
    - The sentence summarizing the activation positions for Breaking-Official pattern is expanded in the glossary and detailed explanation.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_017]` `[trigger: 破官格定义]` `[factor_trigger: poguan_ge_presence]` `[role: 主干]` 四柱元无财官印绶，却有破官之辰。 → 《三命通会》卷六#破官格
  - `[ns_smth_06_018]` `[trigger: 三合合住]` `[factor_trigger: sanhe_hezhu AND gui_qi_wei_miao]` `[role: 主干依赖]` 癸卯日破出午中己土为官，柱中须得一字三合合住贵气为妙。 → 《三命通会》卷六#破官格
  - `[ns_smth_06_019]` `[trigger: 财官双美]` `[factor_trigger: mao_po_wu OR wu_po_you]` `[role: 条件分支]` 卯破午，午破酉，财官双美。 → 《三命通会》卷六#破官格
  - `[ns_smth_06_020]` `[trigger: 月时发力]` `[factor_trigger: yue_shi_po_he AND zhu_gui]` `[role: 总结]` 年日支无破官之辰，月时支有破官合官之辰，主贵。 → 《三命通会》卷六#破官格"""
    normalized_text_zh: str = """"""
    subject: str = "破出官星与三合合贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_9', 'bazi_semantic', 'bazi_structure_chen_1', 'bazi_semantic', 'bazi_state_factor_6', 'bazi_semantic', 'bazi_state_sanhe', 'bazi_semantic', 'bazi_condition_factor_136', 'bazi_semantic', 'bazi_condition_jiecai', 'bazi_semantic', 'source_ref', 'rel_smth_06_013', 'poguan_ge_presence', 'rel_smth_06_014', 'sanhe_hezhu_wengu', 'rel_smth_06_015', 'jiecai_tianshi_risk', 'evi_smth_06_013', 'zhuwu_mingguan', 'rule_poguan', 'evi_smth_06_014', 'sanhe_hezhu_wengu', 'rule_hezhu', 'evi_smth_06_015', 'poguan_liliang', 'rule_shuangmei', 'map_smth_06_009', 'map_smth_06_010']
    
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
        l1_anchor="smth_v1.0.0_破出官星与三合合贵_001_L1",
    )
    version: str = "1.0.0"
