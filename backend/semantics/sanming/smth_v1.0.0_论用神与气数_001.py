"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264263
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
    semantic_id="smth_v1.0.0_论用神与气数_001",
    book_id="sanming",
    engine_id="bazi"
)
class 论用神与气数(SemanticEntry):
    """
    - 原文（source_text）：
  专执用神，切详喜忌。专执一位用神，为尊长，为权神，为号令，为本领，为倚托。此非小可，执而推之，未敢纵求其意。外取用神，或财，或官，或刃，或煞，或食，或贵，或印...
    """
    
    original_text: str = """- 原文（source_text）：
  专执用神，切详喜忌。专执一位用神，为尊长，为权神，为号令，为本领，为倚托。此非小可，执而推之，未敢纵求其意。外取用神，或财，或官，或刃，或煞，或食，或贵，或印，或禄马等件，各类例取，原无定法。其用神最忌损犯，兼怕分窃，不宜太过与不及。
  气气切穷尽理，物物至极转关。金木水火土五气，一阴一阳，共有十般消息。一件件要看衰旺、轻重、明晦、广狭。穷则究理，尽处生何神？克何神？刑何神？合何神之类。被坏之物，得生之物，主系何事？物物推将去，须要有依倚下落。至无可奈何处，便是转关，入何格调？极处一转，即是建功。圆活参透，却要定见下落，断成器不成器何如？

- 分字分词释义：
  - **专执用神**：抓准格局的核心用神（如官格用官，煞格用印等）。
  - **转关**：物极必反，绝处逢生，或格局变化之处。
  - **分窃**：比劫分夺，食伤泄气。

- **规范化释义（primary_lang_explained）**：
  必须紧紧抓住用神，详细分析其喜忌。用神是八字的纲领、号令、依托。取用神无定法，或财或官或印等。用神最怕被克损（损犯）或被泄弱（分窃），也不宜太过或不及，贵在中和。
  对每一个五行气数都要穷尽其理。看它生谁、克谁、合谁。当一种气势达到极点无法发展时，往往会出现转折（转关），形成特殊的格局（如从格、化格、绝处逢生）。要灵活参透，看最终能否成器。

- 核心要点：
  - **用神为尊**：用神不可伤。
  - **物极必反**：关注气势的转折点。
  - **中和为贵**：忌太过不及。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_057]` `[trigger: 专执用神]` `[factor_trigger: zhuanzhi_yongshen AND qiexiang_xiji]` `[role: 主干]` 专执用神，切详喜忌。专执一位用神，为尊长，为权神，为号令。 → 《三命通会》卷十#论用神与气数
  - `[ns_smth_10_058]` `[trigger: 最忌损犯]` `[factor_trigger: zuiji_sunfan AND jianpa_fenqie]` `[role: 主干依赖]` 其用神最忌损犯，兼怕分窃，不宜太过与不及。 → 《三命通会》卷十#论用神与气数
  - `[ns_smth_10_059]` `[trigger: 物物至极]` `[factor_trigger: wuwu_zhiji AND zhuanguan_ruge]` `[role: 条件分支]` 物物至极转关。至无可奈何处，便是转关，入何格调？极处一转，即是建功。 → 《三命通会》卷十#论用神与气数
  - `[ns_smth_10_060]` `[trigger: 圆活参透]` `[factor_trigger: yuanhuo_cantou AND dingjian_xialuo]` `[role: 总结]` 圆活参透，却要定见下落，断成器不成器何如？ → 《三命通会》卷十#论用神与气数"""
    normalized_text_zh: str = """"""
    subject: str = "论用神与气数"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_yongshen_2', 'bazi_semantic', 'bazi_state_yongshen_2', 'bazi_semantic', 'bazi_condition_factor_104', 'bazi_semantic', 'bazi_condition_factor_105', 'bazi_semantic', 'bazi_factor_36', 'bazi_semantic', 'source_ref', 'rel_smth_10_046', 'zhuanzhi_yongshen', 'rel_smth_10_047', 'yongshen_shousun', 'rel_smth_10_048', 'wuji_biran', 'evi_smth_10_046', 'zhuanzhi_yongshen', 'rule_zhuanzhi_yongshen1', 'evi_smth_10_047', 'sunfan_fenqie', 'rule_yongshen_shousun1', 'evi_smth_10_048', 'zhuanguan_biange', 'rule_wuji_biran1', 'map_smth_10_031', 'map_smth_10_032']
    
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
        l1_anchor="smth_v1.0.0_论用神与气数_001_L1",
    )
    version: str = "1.0.0"
