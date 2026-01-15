"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755677
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
    semantic_id="zw_v1.0.0_论男女命同异_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论男女命同异(SemanticEntry):
    """
    - 分字分词释义：

  - **男女命不同**：男命与女命的判断重点不同。
  - **男命先看**：身命、财帛、官禄、迁移。
  - **女命先看**：身命、福德、夫君、子媳。
  - **贪狼七...
    """
    
    original_text: str = """- 分字分词释义：

  - **男女命不同**：男命与女命的判断重点不同。
  - **男命先看**：身命、财帛、官禄、迁移。
  - **女命先看**：身命、福德、夫君、子媳。
  - **贪狼七杀擎羊**：女命不宜见此三星。
  - **桃花刑杀**：桃花星与刑杀星同度。
  - **因夫贵**：女命以夫君宫定贵贱。
  - **正强次强**：子媳夫君福德为正强，田宅财帛为次强。

- 原文（断句）：

  男女命不同，星辰各别。男命先看身命，次看财帛、官禄、迁移，俱要庙旺为吉，败陷聚凶为凶。三看福德、权禄、劫空庙陷言忌，外看田宅妻妾、疾厄宫，吉凶已录干后。又看父母妻子三宫，俱有劫空杀忌，则僧道之命，否则贫穷孤独，湏要仔细参详，方可断人祸福荣枯。女命先为身命吉凶，如贪狼、七杀、擎羊则不美。次看福德宫吉凶，若七杀单居福德，必为娼婢。三看夫君，四看子媳、财帛、田宅。若桃花刑杀，要败绝空亡为吉；若诸吉庙旺，不佳，虽是艰辛贫困，亦不为下贱夭拆。论女因夫贵，女命贵格反无，用以子媳、夫君、福德为正强，田宅、财帛为次强，以官禄、迁移七宫为陷。

- 规范化释义（primary_lang_explained）：

  本条从男命与女命的不同落点，说明传统断命时观察重点并不相同。男命以身宫、命宫为根本，再看财帛、官禄、迁移三宫是否庙旺得地，若星曜败陷聚凶，则多主行运坎坷。其后须参看福德宫、禄权等宫位的庙旺与否，以及田宅、妻妾、疾厄等宫的吉凶，作为富贵与破败、安康与病弱的背景。若父母、妻子三宫俱见劫空、杀忌，则多偏向出家僧道、远离世缘之命；若虽不出家，却多伴随贫穷孤独，需要细致权衡方能断定祸福高低。

  女命则以身命吉凶为首要，若命宫坐贪狼、七杀、擎羊等刚烈之星，多主性情与境遇不美；其次看福德宫，若七杀单居其间，则古书以「娼娢」论之。再往下依次考察夫君宫、子媳宫，以及财帛、田宅等宫位，以判断婚姻质量、子嗣境遇与家计兴衰。对女命而言，桃花、刑杀一类之星，宁可破败、空亡，以免招惹是非；若诸吉庙旺，则往往只是辛苦贫困，却不至于下贱夭拆。本条最后指出，女命的贵贱不单纯以「因夫贵」而定，而是以子息、夫君、福德三宫为正轴，田宅、财帛为次轴，将官禄、迁移等七宫视为相对次要。

- 完整对等诠释（secondary_lang_full）：

  This section sets out different centres of gravity for reading men's and
  women's charts in the classical framework. For men, judgement starts from
  the Life and Body palaces, then moves to Wealth, Career and Travel, which
  should ideally be in temple dignity and free of heavy malefics. Fortune,
  Power and empty or cutting stars are then used to grade the quality of
  support and the depth of blessing, together with Property, Wives and
  Concubines, and Illness palaces. When the Parents and Spouse palaces are
  all entangled with voids and killing stars, the text points either to a
  monastic path or to poverty and loneliness, and urges the reader to weigh
  these signs carefully before judging rank and fortune.

  For women, the emphasis shifts. Life and Body are still primary, but harsh
  stars such as Tanlang, Qisha or Qingyang in the Life palace are taken as
  unfavourable. Next comes the Fortune palace; if Seven Killings stands there
  alone, the text uses the extreme label of "prostitute or servant". Then one
  examines the Husband palace, the palace of children and daughters-in-law,
  and finally Wealth and Property, to read the quality of marriage, fertility
  and domestic stability. Peach Blossom and punishing or killing stars are
  seen as safer when broken, voided or cut off, while an overabundance of
  benefics may still leave a woman working hard and living modestly, though
  without degradation or early death. Overall, women's nobility is not judged
  solely by "rising through the husband" but by the combined strength of
  children, spouse and Fortune, with Property and Wealth as secondary and
  Career and Travel treated as relatively minor.

- 核心要点：

  1. 男命重身命为根，再看财帛、官禄、迁移与福德、禄权等宫的庙旺与聚凶。
  2. 父母、妻子三宫若多劫空、杀忌，男命易入僧道或一生贫穷孤独。
  3. 女命首先看身命，其次看福德、夫君、子媳，再参财帛、田宅等宫。
  4. 七杀单居福德，在古法中多被视为娼婢之象，属极端用例。
  5. 女命不单以「因夫贵」论贵贱，而以子息、夫君、福德三宫为判断主轴。

- 叙事素材（narrative_snippets）：

  - **男命重点**："男命重身命为根，再看财帛官禄迁移福德"，男命以事业财运为主轴。
  - **僧道之命**："父母妻子三宫多劫空杀忌，男命易入僧道"，三亲宫凶主孤独。
  - **女命次序**："女命首看身命，次看福德夫君子媳"，女命以关系为主轴。
  - **娼婢之象**："七杀单居福德，多被视为娼婢之象"，古法对女命福德宫的极端判断。
  - **现代应用**：本条建立男女命的差异化评估框架——男命重财官，女命重关系与福德。"""
    normalized_text_zh: str = """"""
    subject: str = "论男女命同异"
    factor_refs: list = ['type_nanming', 'type_nvming', 'palace_fortune', 'pattern_qishadanju', 'pattern_yinfugui', 'source_ref', 'rel_nannv_001', 'type_nanming', 'rel_nannv_002', 'type_nvming', 'rel_nannv_003', 'pattern_qishadanju', 'evi_nannv_001', 'type_nanming', 'rule_nannv_nan', 'evi_nannv_002', 'type_nvming', 'rule_nannv_nv', 'concept_gender_frame', 'concept_social_status']
    
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
        l1_anchor="zw_v1.0.0_论男女命同异_001_L1",
    )
    version: str = "1.0.0"
