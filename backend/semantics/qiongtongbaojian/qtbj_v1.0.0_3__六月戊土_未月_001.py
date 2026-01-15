"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597014
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
    semantic_id="qtbj_v1.0.0_3__六月戊土_未月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3六月戊土未月(SemanticEntry):
    """
    - **原文（source_text）**：
  六月戊土，遇夏干枯，先看癸水，次用丙火甲木。
  癸丙两透，科甲中人。或有癸无丙，见甲可许秀才。无甲略富。或有丙无癸，假道斯文，衣食颇足。
  或癸透...
    """
    
    original_text: str = """- **原文（source_text）**：
  六月戊土，遇夏干枯，先看癸水，次用丙火甲木。
  癸丙两透，科甲中人。或有癸无丙，见甲可许秀才。无甲略富。或有丙无癸，假道斯文，衣食颇足。
  或癸透辛出，以刀笔之才，可谋异路。
  无癸丙者，常人。若又无甲，下贱之辈。
  或土多得一甲出，不见庚辛，为人作事轩昂，性情谨慎，即不显扬，亦文章惊世。

- **分字分词释义**：
  - **干枯**：干燥枯竭 / 未月土燥 / 需润
  - **假道斯文**：假装斯文有礼 / 有丙无癸 / 次吉
  - **刀笔之才**：文书法律之才 / 癸辛配合 / 异路
  - **轩昂**：气宇轩昂 / 甲透无庚辛 / 吉象
  - **文章惊世**：文章惊动世人 / 杀印相生 / 吉象
  - **下贱之辈**：卑贱之人 / 无癸丙甲 / 凶象

- **规范化释义（primary_lang_explained）**：
  六月（未月）的戊土，遇到夏天干枯（火余气，土燥），先看癸水（润），次用丙火（暖/生）和甲木（疏）。
  癸水丙火两透，科甲中人（水火既济，土得润且得阳）。或者有癸水无丙火，见到甲木可以许诺秀才。无甲木略富。如果有丙火无癸水，是假充斯文，衣食颇足（印旺身强）。
  如果癸水透出辛金出干（伤官生财），凭刀笔（文书/法律）的才能，可以谋求异路功名。
  没有癸水丙火的人，常人。如果又没有甲木，是下贱之辈（土顽无用）。
  如果土多得到一个甲木透出，不见庚辛金（伤官），为人作事气宇轩昂，性情谨慎，即使不显扬名声，文章也会惊世骇俗。

- **完整对等诠释（secondary_lang_full）**：
  Wu Earth in the 6th Month (Goat Month): Meeting Summer dryness; first look for Gui Water, then use Bing and Jia.
  If Gui and Bing are both revealed, one is in the Civil Service. With Gui but no Bing, seeing Jia promises a Xiucai. Without Jia, slightly rich. With Bing but no Gui, pretending to be cultured, with sufficient food/clothing.
  If Gui reveals with Xin, one can seek alternative paths via talent in writing/law.
  Without Gui/Bing, ordinary. If also without Jia, a lowly person.
  If Earth is abundant and one Jia reveals, without Geng/Xin, the person is dignified in action and cautious in nature; even if not famous, their essays will startle the world.

- **核心要点**：
  - **首要用神**：癸水（润土）。未月土燥，非癸不灵。
  - **配合**：丙（配癸既济）、甲（土多疏土）。
  - **土重喜甲**：土多无甲，顽愚；有甲疏通，文章惊世。

- **详细解说**：
  - 未月土当令，且为燥土。
  - 癸水润土是第一要务，所谓“稼穑需水”。
  - 甲木疏土是第二要务，土实需疏。
  - 丙火辅助，因为未月三伏生寒（？此处存疑，未月通常火旺，但《穷通》常提三伏生寒，指阴气滋生），或指土赖火生，保持生机。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_514]` `[trigger: 未月戊土用神次序]` `[factor_trigger: month_wei AND tiangan_wu AND tiangan_gui AND tiangan_bing AND tiangan_jia]` `[role: 主干]` 六月戊土，遇夏干枯，先看癸水，次用丙火甲木。 → 《穷通宝鉴·三夏戊土》#22.3
  - `[ns_qttbj_515]` `[trigger: 癸丙科甲中人]` `[factor_trigger: month_wei AND tiangan_wu AND tiangan_gui AND tiangan_bing AND kejia_scholar]` `[role: 条件分支]` 癸丙两透，科甲中人。 → 《穷通宝鉴·三夏戊土》#22.3
  - `[ns_qttbj_516]` `[trigger: 癸无丙见甲秀才]` `[factor_trigger: month_wei AND tiangan_wu AND tiangan_gui AND NOT tiangan_bing AND tiangan_jia AND xiucai_promise]` `[role: 条件分支]` 或有癸无丙，见甲可许秀才，无甲略富。 → 《穷通宝鉴·三夏戊土》#22.3
  - `[ns_qttbj_517]` `[trigger: 丙无癸假道斯文]` `[factor_trigger: month_wei AND tiangan_wu AND tiangan_bing AND NOT tiangan_gui AND fake_cultured]` `[role: 条件分支]` 或有丙无癸，假道斯文，衣食颇足。 → 《穷通宝鉴·三夏戊土》#22.3
  - `[ns_qttbj_518]` `[trigger: 癸辛刀笔异路]` `[factor_trigger: month_wei AND tiangan_wu AND tiangan_gui AND tiangan_xin AND writing_law_talent]` `[role: 条件分支]` 或癸透辛出，以刀笔之才，可谋异路。 → 《穷通宝鉴·三夏戊土》#22.3
  - `[ns_qttbj_519]` `[trigger: 无癸丙常人下贱]` `[factor_trigger: month_wei AND tiangan_wu AND NOT tiangan_gui AND NOT tiangan_bing AND NOT tiangan_jia AND lowly_status]` `[role: 例外处理]` 无癸丙者常人，若又无甲，下贱之辈。 → 《穷通宝鉴·三夏戊土》#22.3
  - `[ns_qttbj_520]` `[trigger: 土多甲透文章惊世]` `[factor_trigger: month_wei AND tiangan_wu AND earth_excessive AND tiangan_jia AND NOT tiangan_geng AND NOT tiangan_xin AND article_astonish_world]` `[role: 条件分支]` 或土多得一甲出，不见庚辛，为人作事轩昂，性情谨慎，即不显扬，亦文章惊世。 → 《穷通宝鉴·三夏戊土》#22.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 六月戊土（未月）"
    factor_refs: list = ['pretend_cultured', 'knife_pen_talent']
    
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
        l1_anchor="qtbj_v1.0.0_3__六月戊土_未月_001_L1",
    )
    version: str = "1.0.0"
