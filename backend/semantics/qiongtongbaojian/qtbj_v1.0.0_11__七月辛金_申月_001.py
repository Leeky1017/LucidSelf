"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578503
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
    semantic_id="qtbj_v1.0.0_11__七月辛金_申月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 11七月辛金申月(SemanticEntry):
    """
    - **原文（source_text）**：
  七月辛金，值庚司令，不旺自旺，且壬水居申，四柱不见戊土，胎元戊藏申内，为壬堤岸，人命得此，为官清正，但不富耳。
  或有土无甲，为有病无药，常人。有甲...
    """
    
    original_text: str = """- **原文（source_text）**：
  七月辛金，值庚司令，不旺自旺，且壬水居申，四柱不见戊土，胎元戊藏申内，为壬堤岸，人命得此，为官清正，但不富耳。
  或有土无甲，为有病无药，常人。有甲者，衣衿可望。或四柱金多，宜水泄之。若一派金水，得一戊土，反为辛用，又宜甲制，自然富贵。或干支水多，重见戊土，逢生得位，福寿之造。
  七月辛金，壬不在多，故书云：水浅金多，号曰体全之象，壬水为尊，甲戊酌用可也，癸水不可为用。

- **分字分词释义**：
  - **不旺自旺**：不需旺也自然旺 / 庚司令 / 身强
  - **壬水居申**：壬水在申长生 / 水源充足 / 吉象
  - **堤岸**：堤坝河岸 / 戊土止水 / 用神
  - **官清正**：做官清廉正直 / 格局特点 / 吉象
  - **有病无药**：有病症无药医 / 有土无甲 / 凶象
  - **水泄**：水泄金气 / 金多用水 / 配合
  - **体全之象**：身体完整之象 / 水浅金多 / 格局名
  - **壬水为尊**：壬水最为尊贵 / 首要用神 / 原则
  - **福寿之造**：福气寿命之命 / 戊水得位 / 吉象

- **规范化释义（primary_lang_explained）**：
  七月（申月）辛金值庚司令不旺自旺且壬水居申四柱不见戊土胎元戊藏申内为壬堤岸人命得此为官清正但不富耳。
  或有土无甲为有病无药常人。有甲者衣衿可望。或四柱金多宜水泄之。若一派金水得一戊土反为辛用又宜甲制自然富贵。或干支水多重见戊土逢生得位福寿之造。
  七月辛金壬不在多故书云：水浅金多号曰体全之象壬水为尊甲戊酌用可也癸水不可为用。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal in 7th Month (Monkey Month): meeting Geng commanding not-prosperous self-prosperous also Ren Water residing Shen four pillars not見Wu Earth fetal-element Wu hidden Shen-inside為Ren embankment person-destiny gaining-this為official clear-upright but not-wealthy only.
  Or having Earth without Jia為having-病 without-medicine ordinary. Having Jia衣衿 can-hope. Or four pillars Metal many suitable Water泄. If all Metal/Water gaining one Wu Earth conversely為Xin use also suitable Jia制 naturally wealth-nobility. Or stems-branches Water many重見Wu Earth meeting生 gaining position fortune-longevity造.
  7th month Xin Metal Ren not在多 therefore book says: Water-shallow Metal-many name body-complete象 Ren Water revered Jia/Wu discretionary-use possible Gui Water cannot為use.

- **核心要点**：
  - **首要用神**：壬水（为尊不在多）
  - **配合**：甲木戊土酌用
  - **申月特点**：庚金司令不旺自旺壬水居申体全之象

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_428]` `[trigger: 辛生申月]` `[factor_trigger: month_shen AND tiangan_xin AND geng_commanding AND ren_residing_shen]` `[role: 主干]` 七月辛金，值庚司令，不旺自旺，且壬水居申，为官清正。 → 《穷通宝鉴·三秋辛金》#34.11
  - `[ns_qttbj_429]` `[trigger: 体全之象]` `[factor_trigger: month_shen AND tiangan_xin AND water_shallow AND metal_many AND body_complete_xiang]` `[role: 条件分支]` 水浅金多，号曰体全之象，壬水为尊，甲戊酌用可也。 → 《穷通宝鉴·三秋辛金》#34.11
  - `[ns_qttbj_430]` `[trigger: 有土无甲]` `[factor_trigger: month_shen AND tiangan_xin AND element_earth AND NOT tiangan_jia]` `[role: 例外处理]` 或有土无甲，为有病无药，常人。有甲者，衣衿可望。 → 《穷通宝鉴·三秋辛金》#34.11"""
    normalized_text_zh: str = """"""
    subject: str = "11. 七月辛金（申月）"
    factor_refs: list = ['body_complete_xiang', 'ren_not_excess']
    
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
        l1_anchor="qtbj_v1.0.0_11__七月辛金_申月_001_L1",
    )
    version: str = "1.0.0"
