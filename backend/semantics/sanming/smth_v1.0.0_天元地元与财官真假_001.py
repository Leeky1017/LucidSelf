"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264155
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
    semantic_id="smth_v1.0.0_天元地元与财官真假_001",
    book_id="sanming",
    engine_id="bazi"
)
class 天元地元与财官真假(SemanticEntry):
    """
    - **原文（source_text）**：
  凡看命以日干用为天元，是以干为禄；日支、月支用为地元，是以支为命。假如壬癸日己未月，干支透出财官是也。
  财官论原有原无。地支原有财官，天干不露出者...
    """
    
    original_text: str = """- **原文（source_text）**：
  凡看命以日干用为天元，是以干为禄；日支、月支用为地元，是以支为命。假如壬癸日己未月，干支透出财官是也。
  财官论原有原无。地支原有财官，天干不露出者，不问。若地支无财官，只是天干透出，虽行好运，亦不济事。看流年岁君，只用天元。若行运虽重地支，亦要看运天元。
  人命柱中或有官星，或有偏官，有制伏太过，而运干见官煞可发。运支无财而运干是财，亦可为福；运支无煞而运干是煞，亦可为祸。

- **分字分词释义**：
  - **天元/地元**：此处指天干为禄（表象、官禄），地支为命（根基、实财）。
  - **原有原无**：指命局地支中是否藏有根气。
  - **透出**：天干显露。
  - **不问**：意指不用太担心，或者指如果只藏不透，力量稍逊但仍有根；若只透不藏，则为虚。

- **白话原意**：
  看命以日干为天元，代表禄（爵禄、表象）；以日支、月支为地元，代表命（根基、实利）。例如壬癸日生于己未月，未中藏有己土官星、丁火财星，这叫干支财官透出（或暗藏）。
  论财官，关键看地支有没有根气（原有）。如果地支本来就藏有财官，即使天干不透出，也算有财官（只是名气不大）。但如果地支全无财官根气，只是天干虚透，即使行好运，也不济事（虚名虚利，易破败）。
  看流年太岁，主要看天干（岁君）。看大运，虽然重地支（运方），但也要看运干（盖头）。
  命局中如果有官星或七煞，被制伏太过（如食伤太重），如果大运行到天干见官煞之地，反而可以发福（去制存煞）。大运地支无财但运干是财，也主有福（虚财亦可用）；运支无煞但运干是煞，也主有祸（虚煞亦攻身）。

- **核心要点**：
  - **重地支**：财官必须通根地支方为真。
  - **虚透无用**：支无财官干虚透，好运亦难发。
  - **岁运看法**：流年重干，大运重支兼看干。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_017]` `[trigger: 天元地元]` `[factor_trigger: tianyuan_diyuan AND ganlu_zhibing]` `[role: 主干]` 凡看命以日干用为天元，是以干为禄；日支、月支用为地元，是以支为命。 → 《三命通会》卷十#天元地元与财官真假
  - `[ns_smth_10_018]` `[trigger: 原有原无]` `[factor_trigger: yuanyou_yuanwu AND zhiyou_caiguan]` `[role: 主干依赖]` 财官论原有原无。地支原有财官，天干不露出者，不问。 → 《三命通会》卷十#天元地元与财官真假
  - `[ns_smth_10_019]` `[trigger: 支无干透]` `[factor_trigger: zhiwu_gantou AND haoyun_buji]` `[role: 条件分支]` 若地支无财官，只是天干透出，虽行好运，亦不济事。 → 《三命通会》卷十#天元地元与财官真假
  - `[ns_smth_10_020]` `[trigger: 岁运看法]` `[factor_trigger: suiyun_kanfa AND liuyan_gan_dayun_zhi]` `[role: 总结]` 看流年岁君，只用天元。若行运虽重地支，亦要看运天元。 → 《三命通会》卷十#天元地元与财官真假"""
    normalized_text_zh: str = """"""
    subject: str = "天元地元与财官真假"
    factor_refs: list = ['engine_id', 'bazi_factor_29', 'bazi_semantic', 'bazi_condition_factor_88', 'bazi_semantic', 'bazi_state_factor_223', 'bazi_semantic', 'bazi_condition_factor_89', 'bazi_semantic', 'bazi_condition_factor_90', 'bazi_semantic', 'source_ref', 'rel_smth_10_013', 'tianyuan_diyuan', 'rel_smth_10_014', 'xuutou', 'rel_smth_10_015', 'zhiyougen', 'evi_smth_10_013', 'tianyuan_diyuan', 'rule_tianyuan_diyuan1', 'evi_smth_10_014', 'haoyu_nanji', 'rule_xuutou1', 'evi_smth_10_015', 'zhen_caiguan', 'rule_zhiyougen1', 'map_smth_10_009', 'map_smth_10_010']
    
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
        l1_anchor="smth_v1.0.0_天元地元与财官真假_001_L1",
    )
    version: str = "1.0.0"
