"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997225
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
    semantic_id="dts_v1.0.0_旺者冲衰衰者拔_衰者冲旺旺神发_001",
    book_id="dts",
    engine_id="bazi"
)
class 旺者冲衰衰者拔衰者冲旺旺神发(SemanticEntry):
    """
    - **原文（source_text）**：
  旺者冲衰，衰者拔；衰者冲旺，旺神发。

- 原注（原文注解）：
  　　子旺午衰，则午因冲而本拔，子衰午旺，则午因冲而发福，馀仿此。

- 分字分词释...
    """
    
    original_text: str = """- **原文（source_text）**：
  旺者冲衰，衰者拔；衰者冲旺，旺神发。

- 原注（原文注解）：
  　　子旺午衰，则午因冲而本拔，子衰午旺，则午因冲而发福，馀仿此。

- 分字分词释义：
  - 旺者/衰者：相对强弱。
  - 拔：拔起、引动之义（得解）。

- **规范化释义（primary_lang_explained）**：
  同样是冲，强冲弱时，弱者反因冲而得拔扶；弱冲强时，强者反借冲而更显其势。冲并非一味为害，而是依双方强弱与方向不同，表现为拔起、显发或单纯扰动等多种效果，关键在于先把强弱与受益方看清。

- **次语种完整诠释（secondary_lang_full）**:  
  When a strong side clashes against a weak one, the movement can actually pull the weaker side up, releasing what was previously stuck or oppressed. When a weak side clashes against a strong one, the clash often makes the stronger side appear even more dominant and visible. Clash therefore has a layered nature: it may lift the weak, amplify the strong, or simply stir things without clear benefit. The outcome depends on relative strength and direction, so any judgment must start from comparing power on both sides and asking who ultimately benefits from the movement.

- **核心要点**：
  - 冲的效果取决于强弱与方向，而非一味为凶。
  - 旺冲衰，多见弱者得拔解，潜力被激发。
  - 衰冲旺，多见强者更显其势，气势被放大。
  - 断事时须先判强弱、再看谁冲谁，最后再评吉凶。

- **详细解说**：
 此条强调的是"冲"的相对论：同样是地支相冲，若一方明显旺盛而另一方偏衰，则强冲弱时，弱者往往因被冲而得解困、被激活，呈现"拔"的效果；反之，当弱者去冲强者时，弱势一方难以真正撼动强势结构，反倒成为引爆点，使强势一方的力量更集中地显发出来。由此可知，冲并不能简单等同于灾祸，还可能意味着激发、显现与转折。实务中必须先评估双方旺衰与用忌定位，再判断这一次冲动究竟是在拔谁、显谁，谁是受益方、谁是代价方。

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_067]` `[trigger: 旺方冲击衰方]` `[factor_trigger: dizhi_relative_strength_comparison==强vs弱 AND clash_effect_type==拔起 AND clash_beneficiary==弱方 AND activation_level==高]` `[role: 主干]` 旺者冲衰，弱势一方往往因冲而得拔解，潜力被激活。 → 《滴天髓·地支论》#旺冲衰衰者拔
  - `[ns_dts_068]` `[trigger: 衰方反向冲旺方]` `[factor_trigger: dizhi_relative_strength_comparison==弱vs强 AND clash_effect_type==发显 AND clash_beneficiary==强方 AND manifestation_level==高]` `[role: 主干依赖]` 衰者冲旺，多成旺神更发之机，强者借冲更显其势。 → 《滴天髓·地支论》#旺冲衰衰者拔
  - `[ns_dts_069]` `[trigger: 判断冲的吉凶效果]` `[factor_trigger: dizhi_relative_strength_comparison!=不确定 AND clash_beneficiary IN {弱方, 强方}]` `[role: 条件分支]` 断冲之吉凶，先比较强弱与方向，再看受益一方是谁。 → 《滴天髓·地支论》#旺冲衰衰者拔
  - `[ns_dts_143]` `[trigger: 冲非一味为凶]` `[factor_trigger: clash_effect_type IN {拔起, 发显, 中性动}]` `[role: 例外处理]` 冲可为拔、可为发、可为激，不可一概论害。 → 《滴天髓·地支论》#旺冲衰衰者拔
  - `[ns_dts_144]` `[trigger: 强弱不明时]` `[factor_trigger: dizhi_relative_strength_comparison==不确定 OR strength_boundary==on]` `[role: 总结]` 若强弱不明，冲之效果难定，宜多看环境与用神再断。 → 《滴天髓·地支论》#旺冲衰衰者拔

**校勘与字词辨析（textual_criticism）**：
  - 中文：无版本差异 / N/A  
  - English: No known textual variants / N/A"""
    normalized_text_zh: str = """"""
    subject: str = "旺者冲衰衰者拔，衰者冲旺旺神发。"
    factor_refs: list = ['tianquan_yiqi', 'didao', 'mozhizai', 'chengzai', 'shiheng', 'tongguan']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_旺者冲衰衰者拔_衰者冲旺旺神发_001_L1",
    )
    version: str = "1.0.0"
