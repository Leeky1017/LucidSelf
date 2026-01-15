"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412431
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
    semantic_id="smth_v1.0.0_日德格与阳干坐德_001",
    book_id="sanming",
    engine_id="bazi"
)
class 日德格与阳干坐德(SemanticEntry):
    """
    - **原文（source_text）**：

  此格止有五日：甲寅、丙辰、戊辰、庚辰、壬戌，取甲丙戊庚壬五阳干，甲坐寅得禄，丙坐辰官库，庚作辰财印两全，壬坐戌三奇俱备。寅为三阳之首，辰戌为魁罡之地...
    """
    
    original_text: str = """- **原文（source_text）**：

  此格止有五日：甲寅、丙辰、戊辰、庚辰、壬戌，取甲丙戊庚壬五阳干，甲坐寅得禄，丙坐辰官库，庚作辰财印两全，壬坐戌三奇俱备。寅为三阳之首，辰戌为魁罡之地，干支异于别位，故名日德也。若合日德，主为人性格慈善，体貌魁梧，有怜贫敬老之心，无毒害克剥之意，逢凶有救，遇难有解，不遭非横，福必丰厚。赋云：日德心善多稳厚，而作事慈祥是也。运临身旺，大是奇绝，若旺气已衰，行遇魁罡必死，或未及发福，格局既好，运至魁罡，必生祸患，一脱乎此，亦能再发，终力微。此格只一位，喜财官，日德重叠，不宜见财官，及刑冲破害，空亡、魁罡会合加临，皆为大忌。诗曰：壬戌庚辰日德官，甲寅戊丙要骑龙，运逢身旺心慈善，日德居多福自丰。又：日德不喜见魁罡，化成煞曜最难当，局中重见须还吉，运至魁罡福不昌。又：日午德重重免祸殃，官星且忌见财乡，更无冲破空亡处，堪作朝中一栋梁。又：日德有煞喜身强，不喜财星官旺乡，为性温柔更慈善，一生福寿喜非常。如张烛运同：甲申、戊辰、戊辰、壬戌，由学官而腰金衣紫，得五品官诰，是此格也。一命庚辰、己卯、戊辰、甲寅，三位日德，作此格论，但甲寅忌见庚辰，运行壬午财乡之地，午中阳刃持权，皆犯日德，所忌丁巳年，寅巳相刑，四月死，寿止三十八，平生性重，亦不慈善，恶疾久缠。

- 分字分词释义：

  - **此格止有五日**：指甲寅、丙辰、戊辰、庚辰、壬戌五个阳干日，为日德格的限定日柱。
  - **甲坐寅得禄，丙坐辰官库，庚作辰财印两全，壬坐戌三奇俱备**：逐一说明五日之贵处：甲寅坐禄，丙辰坐官库，庚辰兼得财印，壬戌则会三奇，皆较普通干支更得地。
  - **寅为三阳之首，辰戌为魁罡之地**：以寅为阳气之首，辰戌为天罡、地魁之域，暗示日德与阳刚、魁罡同源而不同用。
  - **性格慈善、体貌魁梧**：日德格的人多性情厚道、体格庄重，有怜贫敬老之心，无克剥之意，这是“德”的具体体现。
  - **逢凶有救，遇难有解**：指命中遇到凶险，多有贵人相助或事态缓解，不致横祸无救。
  - **运临身旺为奇绝，行遇魁罡必死**：当大运行到身旺之地，日德之善得以发挥，往往有特殊福泽；反之若衰弱之时又遇魁罡等刚猛之气，则有折福甚至丧命之虞。
  - **此格只一位，喜财官，日德重叠不宜见财官**：一位日德可再受财官美化；若日德重叠，再加财官过多，则阳刚过盛反生祸端。

- **规范化释义（primary_lang_explained）**：

  日德格，是专就五个阳干日（甲寅、丙辰、戊辰、庚辰、壬戌）而言的一种“阳干坐德”之格。所谓“德”，一方面是干支所处之位与常例不同：甲寅得禄、丙辰坐官库、庚辰财印两全、壬戌会三奇，皆为“位特殊、气有余”；另一方面，则指命主人格上的慈祥厚道：有怜贫敬老之心，无克剥残忍之举，遇凶多有转机，遇难常能化解，是一种以德行护身、以善性积福的格局。

  原文强调，日德格一旦遇到身旺之运，其福力极大，可以在事业、名望、寿命上都显出“稳厚”的一面；但若阳气已衰，又恰行到魁罡等刚猛之地，则因阳刚之气外来冲击，反而激发命局潜藏的凶性，容易在大运转折处出现大祸乃至夭折。因此，此格既“喜财官”来润饰德性，又惧魁罡、刑冲、空亡等来伤损德气，尤其忌在气弱之时再遇刚猛之运。

- 核心要点：

  - 日德格只取甲寅、丙辰、戊辰、庚辰、壬戌五个阳干日，为限定较严的专门格局。
  - 重在“德”，表现为性情慈善稳厚、体貌端庄、有怜贫敬老之心，遇凶多有转圜。
  - 身旺之时行吉运，日德之福力最显；身衰而遇魁罡等猛运，则易有重大祸患。
  - 一位日德可取财官润饰；多位日德再见财官，则阳刚过盛，反易引祸。

- 详细解说：

  从结构上看，日德格兼具“位特殊”与“气厚重”两个维度。一方面，这些日柱的支位本身就带有禄、官库、魁罡、三奇等象征，说明干支组合优于寻常；另一方面，原文花了相当篇幅描写其人“心善多稳厚”“温柔慈善”等性格特征，强调此格的贵处不在权势之烈，而在德性之厚。

  需要特别注意的是日德与魁罡之间的张力：辰戌本身就是魁罡之地，庚辰等日既可以论日德，又可以论魁罡——前者偏重“德厚救灾”，后者偏重“刚烈掌权”。若命局整体偏柔弱，则适合以日德为主，借魁罡之力提振而不至过猛；若本身已多刚强，再遇魁罡重叠、财官旺极，则要提防“以德化煞”之力不足，而被魁罡的刚猛一面主导命运。

- **校勘与字词辨析（双语）**：

  - 原文“寅为三阳之首，辰戌为魁罡之地，干支异于别位，故名日德也”一句，本稿在释义中分拆为“位特殊”与“气厚重”两层含义，以便理解。
  - 经文中“日午德重重免祸殃”一句，“日午”疑作“日德”，本稿依通行本作“日德”，并以全段语意从之。
  - 文中所举命例（如张烛运同等），本稿仅在白话中概括其“多位日德、由学官而贵”的共性，不做逐局拆解。
  - **English**：
    - The sentence "Yin is the head of three Yang, Chen-Xu are Kuigang positions" is split into "special position" and "thick qi" meanings for understanding.
    - The text "Day-Wu virtue repeated avoids calamity," where "Day-Wu" is suspected to be "Day-De"; this edition follows the common version.
    - The example charts are summarized as sharing "multiple Day-Virtue positions, rising through scholarly office" without individual analysis.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_073]` `[trigger: 日德格定义]` `[factor_trigger: ride_ge_presence]` `[role: 主干]` 此格止有五日：甲寅、丙辰、戊辰、庚辰、壬戌。 → 《三命通会》卷六#日德
  - `[ns_smth_06_074]` `[trigger: 五阳干坐德]` `[factor_trigger: wu_yang_gan_zuo_de]` `[role: 主干依赖]` 取甲丙戊庚壬五阳干，甲坐寅得禄，丙坐辰官库，庚作辰财印两全，壬坐戌三奇俱备。 → 《三命通会》卷六#日德
  - `[ns_smth_06_075]` `[trigger: 运临身旺]` `[factor_trigger: yun_lin_shen_wang OR xing_yu_kuigang]` `[role: 条件分支]` 运临身旺，大是奇绝，若旺气已衰，行遇魁罡必死。 → 《三命通会》卷六#日德
  - `[ns_smth_06_076]` `[trigger: 心善多稳厚]` `[factor_trigger: xin_shan_duo_wenhou]` `[role: 总结]` 赋云：日德心善多稳厚，而作事慈祥是也。 → 《三命通会》卷六#日德"""
    normalized_text_zh: str = """"""
    subject: str = "日德格与阳干坐德"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_18', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_degree_2', 'bazi_semantic', 'bazi_state_factor_12', 'bazi_semantic', 'bazi_condition_factor_154', 'bazi_semantic', 'bazi_condition_factor_155', 'bazi_semantic', 'source_ref', 'rel_smth_06_055', 'ride_ge_presence', 'rel_smth_06_056', 'shenwan_deqi', 'rel_smth_06_057', 'kuigang_chongde_risk', 'evi_smth_06_055', 'ride_ge_presence', 'rule_ride', 'evi_smth_06_056', 'shenwan_deqi', 'rule_shenwan', 'evi_smth_06_057', 'kuigang_chongde_risk', 'rule_kuigang_de', 'map_smth_06_037', 'map_smth_06_038']
    
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
        l1_anchor="smth_v1.0.0_日德格与阳干坐德_001_L1",
    )
    version: str = "1.0.0"
