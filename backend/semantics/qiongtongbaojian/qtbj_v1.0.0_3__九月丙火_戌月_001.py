"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596799
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
    semantic_id="qtbj_v1.0.0_3__九月丙火_戌月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3九月丙火戌月(SemanticEntry):
    """
    - **原文（source_text）**：
  九月丙火，火气愈退，所忌土晦光火，必须先用甲木，次取壬水。甲壬两透，富贵非凡。若无壬水，得癸透干，亦可，虽不科甲，异路功名。壬癸藏支，贡监而已。甲藏壬...
    """
    
    original_text: str = """- **原文（source_text）**：
  九月丙火，火气愈退，所忌土晦光火，必须先用甲木，次取壬水。甲壬两透，富贵非凡。若无壬水，得癸透干，亦可，虽不科甲，异路功名。壬癸藏支，贡监而已。甲藏壬透，无庚破甲，可许秀才。或庚戊困了水木，定是庸才。无甲壬癸者，下格。
  或一派火土，虽不太旺，亦自燥矣。如不离乡过继，亦主奔流，加以无庚辛壬癸出干，必为夭命。
  或支成火局，炎上失时，若运入南方，一贫彻骨。

- **分字分词释义**：
  - **火气愈退**：火气愈加衰退 / 戌月特征 / 入墓
  - **土晦光火**：土晦暗火光 / 戌为燥土 / 大忌
  - **富贵非凡**：富贵不寻常 / 甲壬透 / 最贵
  - **异路功名**：非正途的功名 / 癸透 / 次等
  - **离乡过继**：离开家乡或过继别人 / 火土燥 / 凶象
  - **炎上失时**：炎上格不逢时 / 戌月火局 / 假格
  - **一贫彻骨**：极度贫穷 / 火运 / 最凶

- **规范化释义（primary_lang_explained）**：
  九月（戌月）的丙火，火气愈加退缩，最忌讳土晦暗火光（戌为火库，也是燥土），必须先用甲木（疏土），其次取壬水（滋甲/映照）。
  甲木和壬水都透出，富贵非凡。如果没有壬水，得到癸水透干，也可以，虽然不是正途科甲，也有异路功名。壬水癸水藏在地支，只是贡监。甲木藏支壬水透干，没有庚金破甲，可以许诺秀才。如果庚金戊土困住了水木（财坏印/食神制杀），定是庸才。没有甲壬癸的人，下格。
  如果一派火土（火土伤官），虽然不算太旺（戌月火入墓），但也自然燥烈。如果不是离乡背井或过继给别人，也主奔波流浪，加上没有庚辛壬癸出干（无财官），必是夭折的命。
  如果地支合成火局，这是“炎上失时”（戌月火气已衰），如果大运再进入南方（火地），一贫彻骨（火土太燥无收）。

- **完整对等诠释（secondary_lang_full）**：
  Bing Fire in the 9th Month (Dog Month): Fire Qi retreats further. It dreads Earth obscuring its light; must first use Jia Wood, then Ren Water.
  If Jia and Ren are both revealed, wealth and nobility are extraordinary. Without Ren, obtaining Gui revealed is acceptable; though not Civil Service, it is alternative fame. If Ren/Gui are hidden, merely a Gongjian. If Jia is hidden and Ren revealed, without Geng breaking Jia, one can be a Xiucai. If Geng/Wu trap Water/Wood, one is certainly a mediocrity. Without Jia/Ren/Gui, it is a lower pattern.
  If there is a mass of Fire/Earth, though not too prosperous, it is naturally dry. If not leaving home or being adopted, one wanders; adding no Geng/Xin/Ren/Gui revealed implies a premature death.
  If branches form a Fire Frame, it is "Inflamed Upward Out of Season". If Luck enters the South, one is poor to the bone.

- **核心要点**：
  - **首要用神**：甲木（疏土）。戌月土重晦光，甲木为第一救星。
  - **次要用神**：壬水（滋甲）。
  - **忌讳**：土晦（Earth Obscuring）、火炎燥土（Fire Scorching Dry Earth）。
  - **炎上失时**：戌月火局，不作贵格炎上，反主贫。

- **详细解说**：
  - 戌月丙火入墓，光芒最暗。
  - 此时最怕“土重”，如乌云遮日。甲木如风吹云散，故甲木最重要。
  - 壬水在此月的作用是“滋甲”，兼有映照之功。
  - “一贫彻骨”：指戌月火局又行火运，火土枯燥，生机尽灭。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_251]` `[trigger: 戌月丙火]` `[factor_trigger: month_xu AND tiangan_bing AND tiangan_jia AND tiangan_ren AND likes_jia_loosen_earth]` `[role: 主干]` 九月丙火，火气愈退，所忌土晦光火，必须先用甲木，次取壬水。 → 《穷通宝鉴·三秋丙火》#14.3
  - `[ns_qttbj_252]` `[trigger: 甲壬两透]` `[factor_trigger: month_xu AND tiangan_bing AND tiangan_jia AND tiangan_ren AND jia_ren_reveal]` `[role: 条件分支]` 甲壬两透，富贵非凡。 → 《穷通宝鉴·三秋丙火》#14.3
  - `[ns_qttbj_253]` `[trigger: 炎上失时]` `[factor_trigger: month_xu AND tiangan_bing AND dizhi_fire_frame AND luck_south AND yanshang_out_season]` `[role: 例外处理]` 支成火局，炎上失时，若运入南方，一贫彻骨。 → 《穷通宝鉴·三秋丙火》#14.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 九月丙火（戌月）"
    factor_refs: list = ['yanshang_out_season', 'poor_to_bone']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_3__九月丙火_戌月_001_L1",
    )
    version: str = "1.0.0"
