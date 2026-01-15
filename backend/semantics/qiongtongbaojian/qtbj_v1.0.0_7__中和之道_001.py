"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619723
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
    semantic_id="qtbj_v1.0.0_7__中和之道_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 7中和之道(SemanticEntry):
    """
    - **原文（source_text）**：
  以义推之，夫万物负阴而抱阳，冲气以和。过与不及，皆为乖道。故高者抑之使平，下者举之使崇，或益其不及，或损其太过。所以贵在折衷，归于中道，使无有余不足之...
    """
    
    original_text: str = """- **原文（source_text）**：
  以义推之，夫万物负阴而抱阳，冲气以和。过与不及，皆为乖道。故高者抑之使平，下者举之使崇，或益其不及，或损其太过。所以贵在折衷，归于中道，使无有余不足之累，即才官印食贵人驿马之微意也。行运亦如之，识其微意，则于命理之说，思过半矣。

- **分字分词释义**：
  - **负阴抱阳**：背负阴气、怀抱阳气 / 万物阴阳共存 / 来自《道德经》
  - **冲气以和**：阴阳二气激荡交融达到和谐 / 动态平衡 / 生命力的来源
  - **乖道**：违背大道 / 失去平衡 / 偏颇之弊
  - **抑**：压抑、抑制 / 降低过高之势 / 平衡手段
  - **举**：抬举、提升 / 增强过低之气 / 平衡手段
  - **益**：增益、补足 / 补不足 / 扶抑之法
  - **损**：减损、削弱 / 损有余 / 扶抑之法
  - **折衷**：折中调和 / 不偏不倚 / 取平衡之道
  - **中道**：中正之道 / 不过不及的平衡状态 / 命理核心目标
  - **微意**：微妙的深意 / 术语背后的真谛 / 财官印等的本质

- **规范化释义（primary_lang_explained）**：
  从道理上推演，万物都背阴而向阳，在阴阳二气的激荡中达到和谐。太过与不及，都是违背大道。所以高的要压抑使之平，低的要抬举使之高，或者补足其不及，或者减损其太过。所以贵在折中调和，回归中道，使没有多余或不足的拖累，这就是财、官、印、食、贵人、驿马等术语背后的微言大义。行运的判断也是如此，若能识得这个微妙旨意，对于命理学说，就领悟过半了。

- **完整对等诠释（secondary_lang_full）**：
  Reasoning by principle, all things carry Yin and embrace Yang, achieving harmony through the blending of Qi. Excess and deficiency are both contrary to the Dao. Therefore, the high should be suppressed to make it level, and the low should be raised to make it lofty; either supplement the deficiency or reduce the excess. Value lies in compromise and returning to the Middle Path (Zhongdao), ensuring no burden of surplus or shortage. This is the subtle meaning behind Wealth, Officer, Seal, Food, Nobles, and Post Horses. The same applies to Luck Pillars; if one understands this subtle meaning, one has comprehended more than half of destiny reasoning.

- **核心要点**：
  - 核心哲学：负阴抱阳，冲气以和（来自《道德经》）。
  - 操作原则：抑强扶弱，损有余补不足。
  - 最终目标：中道（Balance/Middle Path）。
  - 结论：所有神煞术语（财官印等）皆为此服务。

- **详细解说**：
  这是《穷通宝鉴》的总纲领。它强调命理不是玩弄术语（财官印马），而是通过这些工具去调整五行的阴阳平衡。所谓"中道"，不是绝对的平均，而是动态的和谐。这一段直接点出了子平命理的精髓——"平衡用神"。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_031]` `[trigger: 阴阳哲学]` `[factor_trigger: yin_yang_balance]` `[role: 主干]` 万物负阴而抱阳，冲气以和。 → 《穷通宝鉴·五行总论》#1.7
  - `[ns_qttbj_032]` `[trigger: 乖道警示]` `[factor_trigger: NOT principle_balance]` `[role: 例外处理]` 过与不及，皆为乖道。 → 《穷通宝鉴·五行总论》#1.7
  - `[ns_qttbj_033]` `[trigger: 平衡方法]` `[factor_trigger: principle_suppress_support]` `[role: 主干依赖]` 高者抑之使平，下者举之使崇。 → 《穷通宝鉴·五行总论》#1.7
  - `[ns_qttbj_034]` `[trigger: 扶抑原则]` `[factor_trigger: principle_suppress_support]` `[role: 主干依赖]` 益其不及，损其太过。 → 《穷通宝鉴·五行总论》#1.7
  - `[ns_qttbj_035]` `[trigger: 中道要旨]` `[factor_trigger: principle_balance]` `[role: 总结]` 贵在折衷，归于中道，使无有余不足之累，即才官印食贵人驿马之微意也。 → 《穷通宝鉴·五行总论》#1.7
  - `[ns_qttbj_036]` `[trigger: 神煞本质]` `[factor_trigger: shensha_all AND principle_balance]` `[role: 主干依赖]` 财官印食贵人驿马之微意，皆为中道服务。 → 《穷通宝鉴·五行总论》#1.7
  - `[ns_qttbj_037]` `[trigger: 命理精髓]` `[factor_trigger: principle_balance]` `[role: 总结]` 识其微意，则于命理之说，思过半矣。 → 《穷通宝鉴·五行总论》#1.7"""
    normalized_text_zh: str = """"""
    subject: str = "7. 中和之道"
    factor_refs: list = ['yin_yang_balance', 'contrary_to_dao', 'compromise_balance', 'principle_balance', 'supplement_increase', 'reduce_excess']
    
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
        l1_anchor="qtbj_v1.0.0_7__中和之道_001_L1",
    )
    version: str = "1.0.0"
