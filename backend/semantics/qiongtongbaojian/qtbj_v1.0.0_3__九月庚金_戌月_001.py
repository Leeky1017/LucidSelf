"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578360
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
    semantic_id="qtbj_v1.0.0_3__九月庚金_戌月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3九月庚金戌月(SemanticEntry):
    """
    - **原文（source_text）**：
  九月庚金，戊土司令，最怕土厚埋金，宜先用甲疏，后用壬洗，则金自出矣。忌见己土浊壬。
  壬甲两透，科甲相宜。或甲透壬藏，乡魁可望。甲藏壬透，廪贡堪谋。...
    """
    
    original_text: str = """- **原文（source_text）**：
  九月庚金，戊土司令，最怕土厚埋金，宜先用甲疏，后用壬洗，则金自出矣。忌见己土浊壬。
  壬甲两透，科甲相宜。或甲透壬藏，乡魁可望。甲藏壬透，廪贡堪谋。有甲无壬，犹有学问。有壬无甲，莫问衣衿。壬甲两无，则为下格。
  或支成水局，丙透救之，此人才高迈众，名重乡闾，不见癸水，一榜可许。
  或四柱戊多金旺，全无甲壬者，即有衣禄，亦不能久。或庚戊多而无壬甲者，愚顽之辈。

- **分字分词释义**：
  - **戊土司令**：戊土当令 / 戌月土旺 / 月令特点
  - **土厚埋金**：土太厚掩埋金 / 印多身弱 / 凶象
  - **甲疏**：甲木疏通 / 疏土透金 / 用神
  - **壬洗**：壬水淘洗 / 洗去泥土 / 用神
  - **金自出矣**：金自然显露 / 疏洗后 / 吉象
  - **己土浊壬**：己土混浊壬水 / 用神受损 / 忌讳
  - **乡魁**：乡试第一 / 举人 / 贵格
  - **廪贡**：廪生贡生 / 中等功名 / 中格
  - **才高迈众**：才华超越众人 / 水局丙透 / 贵格
  - **愚顽之辈**：愚蠢顽固的人 / 戊多无甲壬 / 下格

- **规范化释义（primary_lang_explained）**：
  九月（戌月）的庚金，戊土当令，最怕土厚埋金（印多反而掩埋日主），适宜先用甲木疏通，后用壬水淘洗，则金自然显露出来。忌讳己土混浊壬水。
  壬水甲木两透，科甲相宜。或甲木透出壬水藏支，乡试第一可望。甲木藏支壬水透出，廪生贡生可谋。有甲木无壬水，尚有学问。有壬水无甲木，不要问秀才。壬甲两无，就是下格。
  如果地支合成水局，丙火透出救助，此人才华超越众人，名重乡里，不见癸水，一榜可许。
  如果四柱戊土多金旺，全无甲木壬水者，即使有衣禄，也不能长久。或庚金戊土多而无壬甲者，愚顽之辈。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal in the 9th Month (Dog Month): Wu Earth commands. Most fears thick Earth burying Metal. Should first use Jia to dredge, then Ren to wash, so Metal naturally emerges. Avoid Ji Earth muddying Ren.
  If Ren and Jia both reveal, Civil Service suitable. If Jia reveals Ren hidden, provincial champion possible. Jia hidden Ren revealed, stipend scholar attainable. With Jia no Ren, still has learning. With Ren no Jia, don't ask about scholar status. Without both Ren and Jia, a lower pattern.
  If branches form Water Frame with Bing revealed to rescue, this person's talent surpasses the crowd, famous in the village. Without Gui, one exam passing is possible.
  If four pillars have much Wu and Metal prosperous, completely without Jia/Ren, even with clothes/salary, it cannot last. If Geng/Wu are heavy without Ren/Jia, a stupid and stubborn person.

- **核心要点**：
  - **首要用神**：甲木（疏土）、壬水（洗金）。戌月土旺，须疏洗方显。
  - **配合**：丙火（水局救应）。
  - **忌讳**：己土（浊壬）、土多（埋金）。

- **详细解说**：
  - 戌月为土库，戊土当权。
  - 金虽有土生，但土太旺反而埋没金的光辉。
  - "甲疏壬洗"：甲木克土使土松，壬水洗去泥土使金显。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_358]` `[trigger: 庚生戌月]` `[factor_trigger: month_xu AND tiangan_geng AND tiangan_jia AND tiangan_ren]` `[role: 主干]` 九月庚金，戊土司令，最怕土厚埋金，宜先用甲疏，后用壬洗。 → 《穷通宝鉴·三秋庚金》#32.3
  - `[ns_qttbj_359]` `[trigger: 壬甲两透]` `[factor_trigger: month_xu AND tiangan_geng AND ren_revealed AND jia_revealed]` `[role: 条件分支]` 壬甲两透，科甲相宜。 → 《穷通宝鉴·三秋庚金》#32.3
  - `[ns_qttbj_360]` `[trigger: 土厚埋金]` `[factor_trigger: month_xu AND tiangan_geng AND wu_excessive AND NOT jia_revealed AND NOT ren_revealed]` `[role: 例外处理]` 四柱戊多金旺，全无甲壬者，即有衣禄，亦不能久。 → 《穷通宝鉴·三秋庚金》#32.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 九月庚金（戌月）"
    factor_refs: list = ['earth_buries_metal', 'dredge_wash', 'xiangkui']
    
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
        l1_anchor="qtbj_v1.0.0_3__九月庚金_戌月_001_L1",
    )
    version: str = "1.0.0"
