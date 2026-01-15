"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725747
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
    semantic_id="zw_v1.0.0_23_其他杂曜_空劫_天刑_天姚等_003",
    book_id="ziwei",
    engine_id="ziwei"
)
class 23其他杂曜空劫天刑天姚等(SemanticEntry):
    """
    - 原文（source_text）：

  问：天刑星所主若何？

  希夷先生答曰：天刑守命，身不为僧道，定主孤刑，不贫则夭，父母不得全。二限逢之，主出家官事，牢狱失财。入庙则吉。

  歌曰：天刑...
    """
    
    original_text: str = """- 原文（source_text）：

  问：天刑星所主若何？

  希夷先生答曰：天刑守命，身不为僧道，定主孤刑，不贫则夭，父母不得全。二限逢之，主出家官事，牢狱失财。入庙则吉。

  歌曰：天刑未必是凶星，入庙名为天喜神。昌曲吉星来凑合，定然献策到王庭。刑居寅上并酉戌，更临卯位自光明，必遇文星成大业，掌握边强百万兵。

- 分字分词释义：

  - **天刑**：掌“刑罚、约束”之星，主孤立、牺牲与因是非而受限。
  - **孤刑**：既无依托又受约束之象，既可能是牢狱、官事，也可能是责任所致的自我封闭。
  - **天喜神**：天刑入庙、得吉曜会时的转化名，象征“以刑成德”，在制度中被信任为谋臣与执法者。
  - **出家官事**：一面指出家、离俗；一面指卷入官司、公权力运作，常伴随财物损耗。
  - **牢狱失财**：因是非、诉讼或权力纠纷带来的自由与财富双重损失。

- 规范化释义（primary_lang_explained）：

  天刑是一颗把“刑罚”与“孤立”合并在一起的星：当它守命而又缺乏清晰的出路时，命主往往既不愿、也不容易走向僧道或高度规范的生活，却又在现实中屡屡被规则、关系和事件束缚——不是贫困奔波，就是中途早夭，父母缘分也不圆满。原文所说“不贫则夭，父母不得全”，强调的是一种“有一端必有所折”的代价结构：要么以物质亏损承受压力，要么以寿元、人伦为代价，难得两全。

  同时，经文也留下了天刑的“高配版本”：当天刑入庙、得昌曲等文星拱照时，它不再只是给自己带来刑厄，而是转化为“天喜神”——懂法度、能为权力中枢献策的谋臣之星。此时所谓“献策到王庭、掌握边强百万兵”，并非单纯主富贵，而是指出：只有当天刑被安放在制度内部、并配合文星与吉曜时，它的“刑”才会变成对他人和局面的规训，而非单纯砍向自己与亲人。整体来看，天刑提示的是：命主如何在“自我约束”与“外在惩罚”之间做选择——若无法主动走向有纪律的道路，这股力量往往会以更被动、更痛的方式显形。

- 完整对等诠释（secondary_lang_full）：

  In Ziwei Doushu, Tianxing represents the convergence of punishment, isolation and moral testing. When placed in the Life palace without a clear channel, it often describes a person who lives under pressure from rules and consequences yet struggles to internalise discipline. The text’s phrase "if not poor then short‑lived, and parents cannot both remain" points to a structure of inevitable cost: either resources are drained through toil, fines and setbacks, or vitality and family bonds are consumed by the weight of circumstances. Encounters with this star during major periods are associated with court cases, imprisonment, forced separation or being drawn into heavy responsibilities that feel more like sentences than choices.

  Yet Tianxing is not framed as purely malignant. When it is dignified—"entering the temple"—and accompanied by scholarly benefics such as Changqu, it transforms into Tianxishen, a "Heavenly Joy" figure who brings order rather than merely suffering. In such charts, the same capacity to endure and understand hardship can be redirected into advising rulers, handling legal matters with integrity, or commanding forces at the frontier. Tianxing then marks those who must learn to work with law rather than against it, turning personal exposure to harshness into wisdom about limits and consequences. Whether this star manifests as prison walls, self‑chosen vows or the disciplined edge of leadership depends largely on how consciously the native accepts responsibility and uses constraint as a tool rather than merely a fate.

- 核心要点：

  1. **孤刑之星**：天刑守命，多主孤刑、不贫则夭、父母缘分不全。
  2. **官事牢狱**：大运流年逢之，易卷入官事、牢狱与失财事件。
  3. **入庙成喜**：入庙配吉，天刑可化为天喜神，主献策王庭、掌兵理法。
  4. **文星相扶**：昌曲等文星相会，可将刑气转为谋略与制度智慧。
  5. **自律与惩罚**：提示命主要在自我约束与被动受罚之间做选择。

- 叙事素材（narrative_snippets）：

  - **孤刑代价**："天刑守命……定主孤刑，不贫则夭，父母不得全"，提示一生必在贫困、寿元或亲缘上付出代价.
  - **二限逢之**："二限逢之，主出家官事，牢狱失财"，大运流年再遇天刑，多见官司、拘系或被迫离群.
  - **天喜转化**："天刑未必是凶星，入庙名为天喜神"，在庙旺及吉曜扶持下，可转为秉法行德的结构.
  - **献策王庭**："昌曲吉星来凑合，定然献策到王庭"，刑星与文星同会时，更像以严谨与体制感服务大局.
  - **现代应用**：天刑可作为评估"规则/法律压力"的指标——看一个人是被动被惩治，还是主动把纪律内化为责任."""
    normalized_text_zh: str = """"""
    subject: str = "23 其他杂曜（空劫、天刑、天姚等）"
    factor_refs: list = ['star_tianxing', 'pattern_guxing', 'state_tianxi', 'pattern_chujia_guanshi', 'pattern_laoyu_shicai']
    
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
        l1_anchor="zw_v1.0.0_23_其他杂曜_空劫_天刑_天姚等_003_L1",
    )
    version: str = "1.0.0"
