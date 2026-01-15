"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101536
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
    semantic_id="smth_v1.0.0_劫煞本义与取位_001",
    book_id="sanming",
    engine_id="bazi"
)
class 劫煞本义与取位(SemanticEntry):
    """
    - **原文（source_text）**：
  论劫煞亡神。劫者，夺也，自外夺之之谓夺；亡者，失也，自内失之之谓亡。劫在五行绝处，亡在五行临官，俱属寅申巳亥。水绝在巳，申子辰以巳为劫煞，巳中戊土，劫...
    """
    
    original_text: str = """- **原文（source_text）**：
  论劫煞亡神。劫者，夺也，自外夺之之谓夺；亡者，失也，自内失之之谓亡。劫在五行绝处，亡在五行临官，俱属寅申巳亥。水绝在巳，申子辰以巳为劫煞，巳中戊土，劫水也。火绝在亥，寅午戌以亥为劫煞，亥中壬水，劫火也。金绝在寅，巳酉丑以寅为劫煞，寅中丙火，劫金也。木绝在申，亥卯未以申为劫煞，申中庚金，劫木也。古歌云：「劫煞为灾不可当，徒然奔走名利场；须防祖业消亡尽，妻子如何得久长。」又云：「四位逢生劫又来，当朝振业逞儒魁；若兼官贵在时上，鲠直名标御史台。」又云：「劫神包裹遇官星，主执兵权助圣明；不怒而威人仰慕，须令华夏悉安荣。」又云：「劫煞原来是煞魁，身宫命主不须来；若为魁局应当死，煞曜临之不必猜。若是无星居此位，更于三合细推排；天盘加得凶星到，命似风灯不久摧。」

- **分字分词释义**：
  - **劫者夺也**：指自外而来的强夺之气，多主外力夺财、夺权、夺气机。
  - **五行绝处之劫**：分别以巳、亥、寅、申为水、火、金、木的绝地，是原气将绝之处，故易发极端之变。
  - **劫煞为灾不可当**：点明劫煞本性偏凶，轻则奔波劳碌，重则祖业消亡、妻子不聚。
  - **劫神包裹遇官星**：当劫煞与官星同宫得用时，反主执掌兵权、有肃杀之权柄。

- **规范化释义（primary_lang_explained）**：
  本节先以「夺」与「失」区分劫与亡：劫是外来的夺取，亡是内里的丧失。劫煞安在五行绝地，即各行气机将尽之处，因此带有「极端、断裂」的性质：水局以巳为劫，火局以亥为劫，金局以寅为劫，木局以申为劫。歌诀进一步说明其凶性：有劫煞者，多在名利场中奔波，须防祖业消耗、家庭难守。但若落在官星、贵格之处，则可转为执兵权、辅佐朝廷的力量，成为「以煞为权」之格局。若劫为魁局而又重重聚集，则生死得失皆极端。

- **完整对等诠释（secondary_lang_full）**：
  Robbery Sha is placed at the extinction positions of the elements and symbolises external forces that seize what has already reached the edge of its cycle.
  At its worst it brings hard to resist losses in wealth, security or status, matching the old verses about wasted effort and vanished inheritance.
  Yet when it is harnessed by official stars or seals it can also fuel bold decisive action and military or crisis type roles, so it must be evaluated through both its clustering and its avenues of control.
- **核心要点**：
  - 劫煞是「绝地之煞」，本性偏凶，却也蕴含打破旧局、夺取资源的极端动能；能否化为权柄，关键在于是否与官星、贵神等正用相配。
  - 在工程化分析中，可将劫煞标记为「高风险高波动」因子：一方面提高破财、家庭动荡等事件的概率；另一方面在官星、印绶生扶之下，增加「武权、激进变革」的可能性。

- **详细解说**：
  1) 在五行局与绝地推算中，为命局标注对应的劫煞位置，并记录其与日主、财星、官星、印绶之间的相对关系，形成 `jie_sha_positions` 与相关联特征；
   2) 计算劫煞的「聚集度」与「制化度」：如成魁局、多重同宫则记为高聚集度，有官星、印绶、贵人同宫或夹拱则记为高制化度；
   3) 在风险模型中，将高聚集度且制化度低的劫煞作为「高波动高风险」标签，显著提高破财、事业剧变、家庭不稳等事件的权重；
   4) 在官星、印绶得力且格局清纯时，则将劫煞更多视作执行力与破局能力的来源，在职业与角色标签上偏向武职、执法、危机处理等领域。

 - 反例与边界：
   - 不宜见一颗劫煞就断人生必然大祸，需综合其数量、位置以及制化情况；
   - 若现实中命主处于低风险行业、生活方式平稳，即便命盘劫煞不轻，也不能强行套用「横死」「破家」等极端结论；
   - 工程上若将劫煞一律视为负向特征，会低估在某些行业中「敢于承担风险、敢于破旧立新」的正面价值；
   - 反向误区是为了强调「英雄气概」而浪漫化劫煞，忽视其对家庭稳定与身心健康的潜在伤害。

 - 小例（示意）：
   - 某命局劫煞重而又与官星、印绶同宫，现实中在军警或高风险行业担纲要职，经历多次调动与前线任务，系统可用「高风险 + 高权柄」结构解释其剧烈但有方向的生涯轨迹；
  - 另一命局劫煞聚集且制化不足，又逢财星被劫，现实表现为多次创业或投资失败、家庭资产反复流失，系统则在解释中强调需要谨慎管理风险与分散投资，而不是鼓励继续激进冒险。"""
    normalized_text_zh: str = """"""
    subject: str = "劫煞本义与取位"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_61', 'bazi_semantic', 'bazi_state_factor_138', 'bazi_semantic', 'bazi_state_factor_139', 'bazi_semantic', 'bazi_function_factor_12', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_劫煞本义与取位_001_L1",
    )
    version: str = "1.0.0"
