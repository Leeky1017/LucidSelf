"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.932730
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
    semantic_id="dts_v1.0.0_五阳从气不从势_五阴从势无情义_001",
    book_id="dts",
    engine_id="bazi"
)
class 五阳从气不从势五阴从势无情义(SemanticEntry):
    """
    - 原文（source_text）：
  五阳从气不从势，五阴从势无情义.

- 原注（原文注解）：
  　　五阳得阳之气，即能成其阳刚，不畏财煞之势，五阴得阴之气，即能成其阴顺，故木盛则从木，火盛则...
    """
    
    original_text: str = """- 原文（source_text）：
  五阳从气不从势，五阴从势无情义.

- 原注（原文注解）：
  　　五阳得阳之气，即能成其阳刚，不畏财煞之势，五阴得阴之气，即能成其阴顺，故木盛则从木，火盛则从火，金盛则从金，水盛则从水，土盛则从土，于情义之所在，见其势衰则忘之，若从得其正，亦未必于无情义也.

- 分字分词释义：
  - 从气：顺其本气（性与根），以气为主.
  - 势：权势外力（财煞之势、强克之势）。
  - 无情义：不主情理之生合，随势而行，情义不固.

- 规范化释义（primary_lang_explained）：
  阳干以“得气”为本，重内在之根与性，不轻随外势；阴干易随外在之势而行，情合不固，偏从势.然“从得其正”，亦可成格，不可执为死法.

- **次语种完整诠释（secondary_lang_full）**：  
  The Five Yang stems (Jia, Bing, Wu, Geng, Ren) are inclined to "follow qi": they stay anchored in their own intrinsic root, seasonal mandate, and native temperament rather than being swept away by external formations of Wealth, Authority, or Killing. Even under strong outside pressure, Yang charts tend to preserve an inner axis, showing a style of keeping their own view and direction.

  The Five Yin stems (Yi, Ding, Ji, Xin, Gui) are more prone to "follow shi": they respond sensitively to the strongest external currents and often adjust their stance according to the prevailing configuration, so that emotional bonds and loyalties are less fixed. This does not make Yin following inherently negative. When the force that is being followed is single, coherent, and upright, such "following" can be proper and form a sound structure; when external forces are mixed, chaotic, or morally skewed, the same tendency easily turns into unhealthy dependence and loss of centre.

  Judgement therefore has to weigh both polarity type (Yang or Yin) and the ratio between inner qi and outer shi, then distinguish correct following from false following, instead of mechanically treating every weak Day Master as a "cong" chart.

- **核心要点**：
  - 气指日主本身的根、令与同气支持，势指外部财官煞的强力结构
  - 阳干从气不从势：阳干以本气为主，根深得令则不轻随外势
  - 阴干从势无情义：阴干本性柔顺，易随外势而行，情合不固
  - 从格有正邪之分：从得其正则成格，从得其邪则失中道
  - 判断从格须审本气与外势的强弱比，不可见弱就判从
  - 阳干在强势中仍可成格，阴干从势亦可从得其用

- **详细解说**：
  本条区分阳干与阴干在面对外势时的不同倾向。"气"指日主本身的根气、当令与同类支持；"势"指财官煞等外在结构对日主形成的环境压力。阳干（甲丙戊庚壬）以本气为主，即便外势强盛，只要根深得令，便不轻易完全随势，表现为"有主之从"；阴干（乙丁己辛癸）本性柔顺，易随外势而行，情义不固，但若"从得其正"——即所从方向单一、纯粹、合理——亦可成格。实占时，须综合日主阴阳属性、本气强弱、外势纯度，判断是"真从""伪从"还是"不从"，避免机械地"见弱就判从"。

 - **narrative_snippets（叙事片段）**：
  - `[ns_dts_022]` `[trigger: 阳干抗势]` `[factor_trigger: cong_qi_pattern]` `[role: 主干]` 阳干以本气为主，根深得令则不畏财煞之势，不轻随外势而转。 → 《滴天髓·通天论》#第8条
  - `[ns_dts_023]` `[trigger: 阴干从势]` `[factor_trigger: cong_shi_pattern]` `[role: 主干依赖]` 阴干本性柔顺，易随外势而行，情义不固，但从得其正亦可成格。 → 《滴天髓·通天论》#第8条
  - `[ns_dts_024]` `[trigger: 从格判断]` `[factor_trigger: cong_validity]` `[role: 总结]` 判断从格须审本气与外势的强弱比、纯度与方向，不可见弱就判从。 → 《滴天髓·通天论》#第8条
  - `[ns_dts_111]` `[trigger: 气与势定义]` `[factor_trigger: qi_vs_shi_ratio]` `[role: 主干依赖]` 气指日主根气与当令同气支持，势指财官煞等外在强力结构，两者消长决定从与不从。 → 《滴天髓·通天论》#第8条
  - `[ns_dts_112]` `[trigger: 伪从警戒]` `[factor_trigger: cong_validity]` `[role: 例外处理]` 阴干若随混乱或邪偏之势，易成伪从失中道，须严辨本气与外势优劣。 → 《滴天髓·通天论》#第8条"""
    normalized_text_zh: str = """"""
    subject: str = "五阳从气不从势，五阴从势无情义."
    factor_refs: list = ['cong_qi_pattern', 'cong_shi_pattern', 'intrinsic_qi', 'external_shi', 'cong_ge', 'qingyi_stability']
    
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
        l1_anchor="dts_v1.0.0_五阳从气不从势_五阴从势无情义_001_L1",
    )
    version: str = "1.0.0"
