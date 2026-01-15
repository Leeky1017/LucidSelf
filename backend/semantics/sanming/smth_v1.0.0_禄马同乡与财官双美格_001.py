"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412407
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
    semantic_id="smth_v1.0.0_禄马同乡与财官双美格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 禄马同乡与财官双美格(SemanticEntry):
    """
    - **原文（source_text）**：
      《继善篇》云：六壬生临午位，号曰禄马同乡，癸日坐向巳宫，乃是财官双美。禄即官，财即马，二句同一义也。壬以丁火为财马，己土为官禄，俱禄于午；癸以...
    """
    
    original_text: str = """- **原文（source_text）**：
      《继善篇》云：六壬生临午位，号曰禄马同乡，癸日坐向巳宫，乃是财官双美。禄即官，财即马，二句同一义也。壬以丁火为财马，己土为官禄，俱禄于午；癸以丙火为正财，戊土为正官，俱禄于巳。人命禄马财官，难得兼全，况自坐支下，所以为贵。喜秋生金旺永生木死，不能克土，故为远害。若见寅卯旺则秀而不实，冬生玄武当权，贵为王侯。如柱有财官，更得此二日生，尤妙。如己丑、丁卯、壬午、癸卯，年月透出丁己，归禄日下，合此，大贵。《珞??录子》云：禄马同乡，不三台而八座。又云：每见贵人食禄，无非禄马同乡是也。甲戌、乙丑、乙巳、丙申、丁丑、戊辰、己亥、庚寅、辛未、壬戌、癸未，此数日支内自藏财官，亦是禄马同乡，经独取壬午、癸巳二日，以壬癸所坐正财正官，余则或偏或正，不纯一故也。类推之，甲戌、乙丑二日，喜金土月分富贵，但金气不可太多，恐伤身盗气，若无官贵，必发财富。丙申、丁丑二日，生金木月贵，惟忌土重，若会起土克官，主富。己亥日宜生四季月，或有倚托相生为吉。庚寅日喜见火，宜生冬至后一阳生火旺之时，主贵，若得金刚火强炼成锋刃之器，秋生逢火尤佳。唐太宰丙午、庚子、壬午、丙午，壬日生子月身旺，冲起年干丙字，二丙同窠，却冲去日庚枭食，庚既受冲克，则避丙就本日午上，时干丙就月支子，壬是庚之子，就时干午，变成丙午、丙子、庚午、壬午，皆禄马同乡，又为水火既济，又名六壬移换，故主大贵。大凡大贵命合三二格局取之，左右逢源，不可以格多为杂，如渊源之说。古歌曰：禄马同乡无克夺，财官同处最为荣，三台八座真奇贵，克夺如强欠利名。
      - 分字分词释义：
      - **六壬生临午位**：指壬午日，壬水坐午火之位，午中藏己土官、丁火财，禄马同宫。
   - **癸日坐向巳宫**：指癸巳日，癸水坐巳火之位，巳中藏戊土官、丙火财，同样“禄马同乡”。
   - **禄即官，财即马**：这里把“禄”与“官”“马”与“财”互相说明，强调壬午、癸巳两日，财星与官星俱得根气，同居禄马之地。
   - **禄马同乡**：日主之禄与驿马同居一支，既有职位权柄之象，又有动中得利、远方发达之意。
   - **财官双美**：财星与官星同时得地、各居其所，又直接托根于日支之下，故曰“双美”。
   - **喜秋生金旺永生木死**：壬午、癸巳生于秋令金旺之时，木气衰，不能过伤土官，反使官根稳定，远离克害。
   - **寅卯旺则秀而不实**：寅卯木多则文采秀丽而欠实用，财官虽美，却难全守。
   - **冬生玄武当权，贵为王侯**：冬令水旺，壬癸得令，再坐禄马同乡，原文以“玄武当权”形容其贵重，甚至可比王侯。
   - **壬午、癸巳为正，其余日为类推**：壬午、癸巳两日为格局正宗，文中所列甲戌等日，只是日支自带财官、可类比“禄马同乡”的次等格局。
      - 白话原意：
      财官双美格，是以壬午、癸巳两日为核心的“禄马同乡”格局。壬午日，壬水之财丁火与官己土同藏午中；癸巳日，癸水之财丙火与官戊土同居巳位。也就是说，日主一坐下，就把自己的财星、官星、禄马之气统统收入脚下，财与官兼全，而且同在驿马之地，故名“财官双美”。
      原文指出，人命中“禄马财官，难得兼全”，若能自坐支下同时具备，便是难得的贵格。壬午、癸巳若又得月令、岁运相扶，尤其是秋令金旺、冬令水旺之时，不但财官根深而不易被克，且多主远方发迹、职禄高显。文中又以多种日柱类推说明：凡日支自藏财官者，都有“禄马同乡”的影子，但壬午、癸巳因所坐皆为本气正财正官，故列为最纯粹、最具代表性的“财官双美”之象。
      - 核心要点：
      - 本格以**壬午、癸巳两日**为正宗，特点是日支自藏正财正官，并兼具禄马之象。
   - 财星、官星皆得根于日支下，且与日主之禄马同宫，故名“禄马同乡、财官双美”。
   - 喜身旺、月令生扶、岁运不破，尤其秋冬水金旺地，更能发挥其贵气。
   - 其他如甲戌、乙丑、丙申等日支自藏财官者，可类比取用，但多为偏财、偏官，纯粹度不及壬午、癸巳。
      - 详细解说：
      从结构上看，财官双美格有三层含义：
      1. **禄马同宫**：壬午以午为驿马，癸巳以巳为驿马，日主坐驿马，象征一生多变动迁移，但因禄、财、官皆在其位，动中有利，往往“行走即得禄”。
   2. **财官同源**：午、巳二支中，火土相依，财可以生官，官得财助，形成财官互相成就之象，而非互相掣肘。
   3. **根基在身下**：财官与禄马皆在日支之下，代表资源与职位都与自身行止紧密相连，更强调个人行动能力与迁移机会的重要性。
      原文特别强调时令差异：秋令金旺，木枯而难再克土，反使土官根基稳定；冬令水旺，“玄武当权”，壬癸得令，更显富贵。反之，若木气过旺，如寅卯多见，则虽有才华、文采，却可能“秀而不实”，财官难以全守。后文列举的诸多日柱例命，实际上是借“禄马同乡”的思路说明：日支若自带财官、并得适当的月令与岁运配合，皆可视为财官双得之象，只是纯与不纯、厚与不厚的差别。
      - **校勘与字词辨析（双语）**：
      - 原文“禄即官，财即马，二句同一义也”，本稿于白话中解释为：禄与官相通，马与财相连，皆指壬午、癸巳日支下财官并见之义。
   - “禄马同乡，不三台而八座”一句，本稿照录，并在释义中注明“禄马同乡”为本格关键术语，以免误解为单纯驿马格。
   - 原文所列甲戌等一串日柱，本稿酌情归纳为“日支自藏财官的次等禄马同乡”，不逐一拆解命例，以保持 L1 层的简洁。
  - **English**：
    - The sentence "salary means official, wealth means horse, the two phrases have the same meaning" is explained in vernacular: salary and official are interchangeable, horse and wealth are connected, both referring to the hidden stems in Ren-Wu and Gui-Si day branches.
    - The example charts are summarized as "lesser salary-horse-same-village with wealth-official" without individual case analysis, to keep L1 concise.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_065]` `[trigger: 禄马同乡定义]` `[factor_trigger: luma_tongxiang_presence]` `[role: 主干]` 六壬生临午位，号曰禄马同乡，癸日坐向巳宫，乃是财官双美。 → 《三命通会》卷六#财官双美
  - `[ns_smth_06_066]` `[trigger: 禄即官财即马]` `[factor_trigger: lu_ji_guan AND cai_ji_ma]` `[role: 主干依赖]` 禄即官，财即马，二句同一义也。 → 《三命通会》卷六#财官双美
  - `[ns_smth_06_067]` `[trigger: 喜秋生忌木旺]` `[factor_trigger: xi_qiu_sheng OR ji_mu_wang]` `[role: 条件分支]` 喜秋生金旺永生木死，不能克土，故为远害。若见寅卯旺则秀而不实。 → 《三命通会》卷六#财官双美
  - `[ns_smth_06_068]` `[trigger: 不三台而八座]` `[factor_trigger: bu_santai_er_bazuo]` `[role: 总结]` 禄马同乡，不三台而八座。 → 《三命通会》卷六#财官双美"""
    normalized_text_zh: str = """"""
    subject: str = "禄马同乡与财官双美格"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_80', 'bazi_semantic', 'bazi_condition_factor_149', 'bazi_semantic', 'bazi_condition_factor_150', 'bazi_semantic', 'bazi_state_factor_347', 'bazi_semantic', 'bazi_condition_factor_151', 'bazi_semantic', 'source_ref', 'rel_smth_06_049', 'luma_tongxiang_presence', 'rel_smth_06_050', 'qiudong_shenwan', 'rel_smth_06_051', 'xiuer_bushi', 'evi_smth_06_049', 'rizhi_cangcaiguan', 'rule_luma', 'evi_smth_06_050', 'qiudong_shenwan', 'rule_qiujin', 'evi_smth_06_051', 'xuanwu_dangquan', 'rule_xuanwu', 'map_smth_06_033', 'map_smth_06_034']
    
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
        l1_anchor="smth_v1.0.0_禄马同乡与财官双美格_001_L1",
    )
    version: str = "1.0.0"
