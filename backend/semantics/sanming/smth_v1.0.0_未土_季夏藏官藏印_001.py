"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042498
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
    semantic_id="smth_v1.0.0_未土_季夏藏官藏印_001",
    book_id="sanming",
    engine_id="bazi"
)
class 未土季夏藏官藏印(SemanticEntry):
    """
    - **原文（source_text）**：
  未当季夏，则阴深而火渐衰。未中有乙木，有丁火，是藏官，藏印，不藏财也。无亥卯以会之，则形难变，只作火土论；无丑戌以刑冲之，则库不开，难得金印。柱中无火...
    """
    
    original_text: str = """- **原文（source_text）**：
  未当季夏，则阴深而火渐衰。未中有乙木，有丁火，是藏官，藏印，不藏财也。无亥卯以会之，则形难变，只作火土论；无丑戌以刑冲之，则库不开，难得金印。柱中无火，怕行金水之运，日时多寒，偏爱丙丁之乡。盖用神之喜忌最当分晓，不可毫发误也。

- **分字分词释义**：
  - **阴深火衰**：季夏已过，火气渐收，阴气暗生。
  - **藏官、藏印**：未中乙木为官星，丁火为印绶，皆藏而未露。
  - **库不开**：未为火土之库，不经刑冲则库中之物难以出用。

- **规范化释义（primary_lang_explained）**：
  未月为季夏，火势渐退而阴气渐深。未土内部藏有乙木官星与丁火印绶，所以称为「藏官、藏印」，唯独不藏财。若不见亥卯来会，则偏于火土之象难以转化；不见丑戌刑冲，则库门紧闭，金印难出。若柱中本就缺火，反怕再行金水之运使土寒木枯；日时气候偏寒者，更宜走丙丁火乡。此处强调：取用之神喜忌当分明，不可稍有差池。

- **完整对等诠释（secondary_lang_full）**：
  Wei occupies late summer, when the outer blaze of fire is ebbing but yin is deepening within the soil. Inside this earth live Yi Wood as the Officer star and Ding Fire as Seal, both present yet concealed, so Wei is called a storehouse of rank and credentials rather than of open Wealth. Without Hai or Mao to link it into wider Wood configurations, Wei tends to remain a pure Fire–Earth enclosure that is hard to transform; without clashes from Chou or Xu the vault door may never be opened, leaving its contents dormant. In charts already lacking fire, further entry into Metal–Water phases chills the earth and dries the hidden Wood, whereas movement toward Bing and Ding territories can warm and activate what is stored. The passage therefore treats Wei Earth as a reservoir of latent authority, learning, or reputation: its benefit depends not only on having such resources inside but also on whether the structure of combinations and punishments provides appropriate keys to release them, instead of leaving the person sitting beside a locked, unused vault."""
    normalized_text_zh: str = """"""
    subject: str = "未土：季夏藏官藏印"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_wei_presence', 'bazi_calculator', 'hai_mao_wei_combo', 'bazi_calculator', 'chou_wei_chong', 'bazi_calculator', 'seasonal_phase', 'bazi_calculator', 'fire_earth_wood_balance', 'bazi_calculator', 'wu_ji_transition_window', 'bazi_calculator', 'bing_ding_yun_flag', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator', 'source_ref', 'rel_smth_02_066', 'dizhi_wei_presence', 'rel_smth_02_067', 'chou_wei_chong', 'rel_smth_02_068', 'dizhi_wei_presence', 'evi_smth_02_062', 'hai_mao_wei_combo', 'rule_hai_mao_wei_wood', 'evi_smth_02_063', 'chou_wei_chong', 'rule_chou_wei_open', 'evi_smth_02_064', 'fire_earth_wood_balance', 'rule_wei_store_officer_seal', 'map_smth_02_045', 'map_smth_02_046']
    
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
        l1_anchor="smth_v1.0.0_未土_季夏藏官藏印_001_L1",
    )
    version: str = "1.0.0"
