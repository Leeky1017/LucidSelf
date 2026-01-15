"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778448
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
    semantic_id="zw_v1.0.0_4_星曜组合格局系列_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 4星曜组合格局系列(SemanticEntry):
    """
    ##### 1.4.1 廉贞七杀，反为积富之人

- 原文（断句）：

  廉贞七杀，反为积富之人；廉贞属火，七杀属金，是火能制金为权。如贞居未，杀居午，身命遇之，奇格也，反为积富，或陷也，化忌下格，...
    """
    
    original_text: str = """##### 1.4.1 廉贞七杀，反为积富之人

- 原文（断句）：

  廉贞七杀，反为积富之人；廉贞属火，七杀属金，是火能制金为权。如贞居未，杀居午，身命遇之，奇格也，反为积富，或陷也，化忌下格，贱命。

- 分字分词释义：

  - **廉贞七杀**：廉贞与七杀的组合格局，两星皆带杀气。
  - **反为积富**：看似凶险的组合，反而成为积累财富的格局。
  - **火能制金为权**：廉贞属火克七杀金，形成制化关系，火主权力。
  - **贞居未杀居午**：廉贞在未宫、七杀在午宫，皆为庙旺之地。
  - **奇格**：少见而珍贵的格局，凶星化吉的特殊组合。
  - **陷地化忌**：星曜落入陷弱之地且化忌，吉转凶。
  - **下格贱命**：低等格局，主贫贱之命。
  - **天梁太阴飘蓬**：天梁与太阴陷地同度，主漂泊无依。
  - **武贪先贫后富**：武曲贪狼同宫，金克木成材，早年困苦晚年富贵。
  - **运逢劫杀**：限运遇到劫空杀星，主破败损失。

- 规范化释义（primary_lang_explained）：

  廉贞七杀反为积富之人。廉贞属火七杀属金，火能制金为权。如廉贞居未七杀居午，身命遇之为奇格，反主积富。若陷地或化忌则为下格贱命。

- 核心要点：
  - **火制金为权**：廉贞火克七杀金，形成制化格局
  - **入庙为奇**：贞未杀午，身命遇之为奇格，主积富
  - **陷地化忌**：若陷地或化忌，则为下格贱命

 - 叙事素材（narrative_snippets）：

   - **廉杀积富**："廉贞七杀，反为积富之人"，廉贞属火、七杀属金，火制金成权，贞居未杀居午入庙时，凶星反成积富奇格。
   - **梁阴飘蓬**："天梁太阴却作飘蓬之客"，太阴卯辰巳午陷地，巳亥二宫遇天梁坐命，多主孤寒飘荡、耽恋酒色。
   - **廉贞贫 vs 太阴乐**："廉贞主下贱之孤寒，太阴主一生之快乐"，同条中对比廉贞陷地无吉拱的贫贱，与太阴得地多吉拱的富贵安乐。
   - **武贪先贫后富**："武贪同身命之宫……先虽贫而后方富贵也"，武曲之金克贪狼之木，木逢制化成才，早年辛劳、晚景翻身。
   - **运逢劫杀先富后贫**："先富后贫，只为运逢劫杀"，说明中年限行绝地再遇劫空耗杀，原本富局也会被一点点掏空。
   - **现代应用**：本组格局展示"组合+时序"的思路——同一组星曜，得地有制可成奇富，不得地又逢恶限，则容易从高位跌落。

- 完整对等诠释（secondary_lang_full）：

  This section illustrates the transformation of star combinations through the Five-Element control cycle and positional dignity. Lianzhen (Fire) controlling Qisha (Metal) creates a paradoxical wealth pattern: when both stars occupy temple positions (Lianzhen in Wei, Qisha in Wu), what appears as a malefic combination becomes an "extraordinary pattern" for accumulating wealth. Similarly, Tianliang combined with Taiyin in debilitated positions leads to wandering and hardship. The contrast between Lianzhen's poverty in fallen positions versus Taiyin's happiness when dignified demonstrates how the same star yields opposite outcomes based on palace placement. Wuqu-Tanlang combinations show temporal progression: Metal controlling Wood creates early hardship followed by late prosperity. Conversely, encountering Robbery-Killing stars during mid-life limits reverses fortune from rich to poor. The key insight is that star combinations must be evaluated through both positional dignity and temporal cycles."""
    normalized_text_zh: str = """"""
    subject: str = "4 星曜组合格局系列"
    factor_refs: list = ['engine_id', 'wuxing_zhihua', 'ziwei_calculator', 'zuhe_miaowang', 'ziwei_calculator', 'fugui_shixu', 'ziwei_rule_engine', 'zuhe_geju', 'ziwei_rule_engine', 'combo_liansha', 'wuxing_zhihua', 'combo_wutan', 'fugui_shixu', 'state_piaopeng', 'result_daobi', 'source_ref', 'rel_zuhe_001', 'wuxing_zhihua', 'rel_zuhe_002', 'zuhe_miaowang', 'rel_zuhe_003', 'fugui_shixu', 'evi_zuhe_001', 'rule_liansha_jifu', 'evi_zuhe_002', 'rule_wutan_xianguihoufu', 'concept_element_control', 'concept_time_sequence']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_4_星曜组合格局系列_001_L1",
    )
    version: str = "1.0.0"
