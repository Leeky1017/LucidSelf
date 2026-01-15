"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578403
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
    semantic_id="qtbj_v1.0.0_1__九月辛金_戌月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1九月辛金戌月(SemanticEntry):
    """
    - **原文（source_text）**：
  九月辛金，戊土司令，母旺子相，先壬后甲。壬甲两透，富贵必然。壬透甲藏，廪贡不失。甲透壬藏，富则可云。壬甲皆无，平常之格。
  所忌者丙贪合也，如月时皆...
    """
    
    original_text: str = """- **原文（source_text）**：
  九月辛金，戊土司令，母旺子相，先壬后甲。壬甲两透，富贵必然。壬透甲藏，廪贡不失。甲透壬藏，富则可云。壬甲皆无，平常之格。
  所忌者丙贪合也，如月时皆丙，名为争合，主慷慨风流，交游四海。若癸出干制丙，可许采芹。或支坐亥子之乡,支又见申，即非玉堂，亦必高增禄位。若戊出干制水，不见甲乙，清闲之人。
  又或支见四库，名土厚金埋，不见甲制，愚顽之辈。或四柱火多，无水制伏，名火土杂乱，主作缁衣，见癸可解。
  或比劫重重，壬癸浅弱，主夭。有甲出干，则贵，然无庚制方妙。
  九月辛金，火土为病，水木为药。

- **分字分词释义**：
  - **母旺子相**：母（土）旺子（金）相 / 戌月特点 / 印旺身强
  - **丙贪合**：丙火贪恋合辛 / 辛丙合水 / 忌神
  - **争合**：争相合 / 月时皆丙 / 凶象
  - **采芹**：中秀才 / 功名 / 吉象
  - **玉堂**：翰林院 / 高官 / 吉象
  - **土厚金埋**：土多埋金 / 印多身弱 / 凶象
  - **火土杂乱**：火土混杂 / 官印相争 / 凶象
  - **缁衣**：僧人衣服 / 出家 / 凶象
  - **病药**：病与药 / 火土病水木药 / 用神原则
  - **廪贡**：廪生贡生 / 秀才 / 功名

- **规范化释义（primary_lang_explained）**：
  九月（戌月）辛金，戊土司令，母旺子相，先用壬水，后用甲木。壬水甲木两透，富贵必然。壬透甲藏，廪贡（秀才）不失。甲透壬藏，富可期。壬甲皆无，平常之格。
  所忌者丙火贪合（辛丙合水）。如月时皆丙，名为争合，主慷慨风流、交游四海。若癸水出干制丙，可许采芹（秀才）。或支坐亥子之乡，支又见申（金水相生），即非玉堂（翰林），亦必高增禄位。若戊出干制水，不见甲乙（疏土），清闲之人。
  又或支见四库（辰戌丑未），名土厚金埋，不见甲制，愚顽之辈。或四柱火多，无水制伏，名火土杂乱，主作缁衣（僧人），见癸可解。
  或比劫重重，壬癸浅弱，主夭折。有甲出干则贵，然无庚制（不见庚制甲）方妙。
  九月辛金，火土为病，水木为药。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal in the 9th Month (Dog Month): Wu Earth commands, mother prosperous child相. First Ren, then Jia. Ren/Jia revealing wealth nobility certain. Ren reveals Jia hidden, scholar degree not lost. Jia reveals Ren hidden, wealth possible. Both absent, ordinary pattern.
  Fear Bing greedily合 (Xin-Bing合water). If month/hour both Bing, name争合, main generous romantic travels everywhere. If Gui reveals制Bing, scholar possible. If branches sit Hai/Zi also见申, even not Hanlin, surely high rank. If Wu reveals制water without Jia/Yi, leisurely person.
  If branches见four tombs (Chen/Xu/Chou/Wei), name earth-thick metal-buried, without Jia制foolish. If pillars fire many without water制, name fire-earth chaos, main becoming monk, Gui can resolve.
  If比劫heavy Ren/Gui shallow, main early death. Jia revealing则贵, but without Geng制best.
  9th month Xin Metal: fire-earth病water-wood medicine.

- **核心要点**：
  - **首要用神**：壬水（淘洗）、甲木（疏土）
  - **忌神**：丙火贪合、戊土埋金、火土杂乱
  - **戌月特点**：土旺金相，需水洗木疏

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_370]` `[trigger: 辛生戌月]` `[factor_trigger: month_xu AND tiangan_xin AND tiangan_ren AND tiangan_jia]` `[role: 主干]` 九月辛金，戊土司令，母旺子相，先壬后甲。壬甲两透，富贵必然。 → 《穷通宝鉴·三秋辛金》#34.1
  - `[ns_qttbj_371]` `[trigger: 丙贪合]` `[factor_trigger: month_xu AND tiangan_xin AND tiangan_bing AND greedy_he]` `[role: 例外处理]` 所忌者丙贪合也，如月时皆丙，名为争合，主慷慨风流。 → 《穷通宝鉴·三秋辛金》#34.1
  - `[ns_qttbj_372]` `[trigger: 土厚金埋]` `[factor_trigger: month_xu AND tiangan_xin AND dizhi_four_tombs AND NOT tiangan_jia]` `[role: 例外处理]` 又或支见四库，名土厚金埋，不见甲制，愚顽之辈。 → 《穷通宝鉴·三秋辛金》#34.1
  - `[ns_qttbj_373]` `[trigger: 病药]` `[factor_trigger: month_xu AND tiangan_xin AND disease_fire_earth AND medicine_water_wood]` `[role: 总结]` 九月辛金，火土为病，水木为药。 → 《穷通宝鉴·三秋辛金》#34.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 九月辛金（戌月）"
    factor_refs: list = ['mother_prosper_child', 'greedy_he', 'earth_thick_metal_buried']
    
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
        l1_anchor="qtbj_v1.0.0_1__九月辛金_戌月_001_L1",
    )
    version: str = "1.0.0"
