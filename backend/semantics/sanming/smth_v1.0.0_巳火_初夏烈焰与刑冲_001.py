"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042476
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
    semantic_id="smth_v1.0.0_巳火_初夏烈焰与刑冲_001",
    book_id="sanming",
    engine_id="bazi"
)
class 巳火初夏烈焰与刑冲(SemanticEntry):
    """
    - **原文（source_text）**：
  巳当初夏，其火增光，是六阳之极也。庚金寄生，困顿戊母。戊土归禄，乃随火娘。见申则刑，刑中有合，翻为无害；见亥则冲，冲而必破便为有伤。若运再行东南生发之...
    """
    
    original_text: str = """- **原文（source_text）**：
  巳当初夏，其火增光，是六阳之极也。庚金寄生，困顿戊母。戊土归禄，乃随火娘。见申则刑，刑中有合，翻为无害；见亥则冲，冲而必破便为有伤。若运再行东南生发之地，便成烧天烈焰之势矣。

- **分字分词释义**：
  - **六阳之极**：指巳月阳气已极盛，火势大增。
  - **庚金寄生，困顿戊母**：庚金寄生于巳火之中，而戊土因随火而受困。
  - **刑中有合**：巳申相刑，但申与巳又有合金火之象，故刑中带合。

- **规范化释义（primary_lang_explained）**：
  巳月为初夏，火势渐强而至六阳之极，好比烈焰高腾。庚金寄生其中，得火炼而成器；戊土则随火而动，既有生化之功，也有受困之虑。巳见申为刑，但因申中庚金与巳中戊土相互生合，往往刑中带合，未必全凶；见亥则纯属冲克，且必有破败之象。若大运再行东南木火之地，火势愈烈，易成「烧天烈焰」，气机过刚。

- **完整对等诠释（secondary_lang_full）**：
  Si marks early summer, when yang has climbed to its sixth and final step and fire flares upward like a blast furnace. Within this blaze Geng Metal is carried and refined, turning raw ore into tools and weapons, while Wu Earth follows the fire and can either be strengthened by baking or scorched and exhausted. When Si encounters Shen, there is a formal punishment between the two, yet because Shen also contains Geng and Ren that can link productively with the Bing and Wu inside Si, the pattern often mixes tension with cooperation—damage and refinement occurring together. By contrast, a clash with Hai is pure opposition between surging fire and deep water and easily produces rupture and loss. If the life further runs into eastern and southern Wood–Fire regions, the heat may become "sky‑burning flames": training, ambition, and pressure all pile up beyond what the body or circumstances can safely hold. This passage therefore frames Si Fire as the pivot between beneficial tempering and destructive over‑firing, urging us to read Metal, Earth, and Water as the cooling and containing factors that decide which side manifests."""
    normalized_text_zh: str = """"""
    subject: str = "巳火：初夏烈焰与刑冲"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'dizhi_si_presence', 'bazi_calculator', 'si_shen_xing', 'bazi_calculator', 'si_hai_chong', 'bazi_calculator', 'seasonal_phase', 'summer', 'fire_metal_earth_balance', 'bazi_calculator', 'bing_ding_yun_flag', 'bazi_calculator', 'dizhi_layer_loss_flag', 'bazi_calculator', 'source_ref', 'rel_smth_02_060', 'dizhi_si_presence', 'rel_smth_02_061', 'si_shen_xing', 'rel_smth_02_062', 'si_hai_chong', 'evi_smth_02_056', 'si_shen_xing', 'rule_si_shen_xing_he', 'evi_smth_02_057', 'si_hai_chong', 'rule_si_hai_clash', 'evi_smth_02_058', 'bing_ding_yun_flag', 'rule_si_fire_extreme', 'map_smth_02_041', 'map_smth_02_042']
    
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
        l1_anchor="smth_v1.0.0_巳火_初夏烈焰与刑冲_001_L1",
    )
    version: str = "1.0.0"
