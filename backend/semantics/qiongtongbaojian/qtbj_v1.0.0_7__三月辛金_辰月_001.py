"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578462
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
    semantic_id="qtbj_v1.0.0_7__三月辛金_辰月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 7三月辛金辰月(SemanticEntry):
    """
    - **原文（source_text）**：
  三月辛金，戊土司令，辛承正气，母旺子相，先壬后甲。壬甲两透，富贵必然。壬透甲藏，廪贡不失。甲透壬藏，富则可云。壬甲皆无，平常之格。
  所忌者丙贪合也...
    """
    
    original_text: str = """- **原文（source_text）**：
  三月辛金，戊土司令，辛承正气，母旺子相，先壬后甲。壬甲两透，富贵必然。壬透甲藏，廪贡不失。甲透壬藏，富则可云。壬甲皆无，平常之格。
  所忌者丙贪合也，如月时皆丙，名为争合，主慷慨风流，交游四海。若癸出干制丙，可许采芹。或支坐亥子之乡，支又见申，即非玉堂，亦必高增禄位。若戊出干制水，不见甲乙，清闲之人。
  又或支见四库，名土厚金埋，不见甲制，愚顽之辈。或四柱火多，无水制伏，名火土杂乱，主作缁衣，见癸可解。
  或比劫重重，壬癸浅弱，主夭。有甲出干，则贵，然无庚制方妙。

- **分字分词释义**：
  - **辛承正气**：辛金承受正气 / 辰中戊土生 / 印旺
  - **母旺子相**：母（土）旺子（金）相 / 辰月特点 / 身强
  - **争合**：争相合 / 月时皆丙 / 凶象
  - **慷慨风流**：慷慨大方风流倜傥 / 争合 / 次吉
  - **交游四海**：交往天下 / 社交广泛 / 次吉
  - **土厚金埋**：土多埋金 / 支见四库 / 凶象
  - **愚顽之辈**：愚蠢顽固之人 / 无甲制土 / 凶象
  - **火土杂乱**：火土混杂 / 无水制 / 凶象
  - **高增禄位**：提高俸禄地位 / 申亥子配合 / 吉象

- **规范化释义（primary_lang_explained）**：
  三月（辰月）辛金戊土司令辛承正气母旺子相先壬后甲。壬甲两透富贵必然。壬透甲藏廪贡不失。甲透壬藏富则可云。壬甲皆无平常之格。
  所忌者丙贪合也如月时皆丙名为争合主慷慨风流交游四海。若癸出干制丙可许采芹。或支坐亥子之乡支又见申即非玉堂亦必高增禄位。若戊出干制水不见甲乙清闲之人。
  又或支见四库名土厚金埋不见甲制愚顽之辈。或四柱火多无水制伏名火土杂乱主作缁衣见癸可解。
  或比劫重重壬癸浅弱主夭。有甲出干则贵然无庚制方妙。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal in 3rd Month (Dragon Month): Wu Earth commanding Xin承正气 mother-prosperous child-相 first Ren then Jia. Ren/Jia revealing wealth-nobility certain. Ren revealing Jia hidden廪贡 not lost. Jia revealing Ren hidden wealth possible. Both absent ordinary pattern.
  Fear Bing greedy-合 if month/hour both Bing name争合 main generous romantic travels everywhere. If Gui revealing制Bing possibly scholar. Or branches sit Hai/Zi also見Shen even not Jade-Hall surely high-rank. If Wu revealing制Water not見Jia/Yi leisurely person.
  Or branches見four tombs name earth-thick metal-buried without Jia制 foolish. Or four pillars fire many without water制 name fire-earth chaos main becoming-monk Gui can resolve.
  Or比劫 heavy Ren/Gui shallow main premature-death. Having Jia revealing則贵 but without Geng制 best.

- **核心要点**：
  - **首要用神**：壬水甲木
  - **忌神**：丙火贪合土厚金埋
  - **辰月特点**：土旺需壬洗甲疏（与九月戌月同理）

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_411]` `[trigger: 辛生辰月]` `[factor_trigger: month_chen AND tiangan_xin AND tiangan_ren AND tiangan_jia]` `[role: 主干]` 三月辛金，戊土司令，辛承正气，母旺子相，先壬后甲。壬甲两透，富贵必然。 → 《穷通宝鉴·三春辛金》#34.7
  - `[ns_qttbj_412]` `[trigger: 丙贪合]` `[factor_trigger: month_chen AND tiangan_xin AND bing_multiple AND greedy_he]` `[role: 例外处理]` 所忌者丙贪合也，如月时皆丙，名为争合，主慷慨风流。 → 《穷通宝鉴·三春辛金》#34.7
  - `[ns_qttbj_413]` `[trigger: 土厚金埋]` `[factor_trigger: month_chen AND tiangan_xin AND dizhi_four_tombs AND NOT tiangan_jia AND earth_thick_metal_buried]` `[role: 例外处理]` 又或支见四库，名土厚金埋，不见甲制，愚顽之辈。 → 《穷通宝鉴·三春辛金》#34.7"""
    normalized_text_zh: str = """"""
    subject: str = "7. 三月辛金（辰月）"
    factor_refs: list = ['carrying_proper_qi', 'contending_he']
    
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
        l1_anchor="qtbj_v1.0.0_7__三月辛金_辰月_001_L1",
    )
    version: str = "1.0.0"
