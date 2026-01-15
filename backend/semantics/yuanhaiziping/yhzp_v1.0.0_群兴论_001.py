"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559335
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
    semantic_id="yhzp_v1.0.0_群兴论_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 群兴论(SemanticEntry):
    """
    - **原文（source_text）**：
  **《当兴》** 夫人生有秉富贵之荣，而当兴富贵，而且能享福，而保其终身。其何故也？盖四柱中身主专旺；而其所用吉神，或为财、或为官、或为印绶、或为食神...
    """
    
    original_text: str = """- **原文（source_text）**：
  **《当兴》** 夫人生有秉富贵之荣，而当兴富贵，而且能享福，而保其终身。其何故也？盖四柱中身主专旺；而其所用吉神，或为财、或为官、或为印绶、或为食神，俱各带禄权得令，不偏不杂；又无刑冲伤损克害，方为富贵本源之不杂也。他日能成才，振耀前人之基业，成当代之功名；不招谗谤，不致伤害。又在运上步步皆吉，四柱益加吉利，是谓源清流洁；故能享福以过人，保其中而无悔也。皆由命运一路滔滔，生旺而然。非幸也，乃命也，可不辩乎！
  **《崛起》** 夫人之生，又有穷饿其身，愁苦孤寒颠倒；无何一旦逢时，兴然而起。或当营财满意，白手庄田；或致君泽民，独步台鼎。斯人也，前后异见，其故何如？盖因柱中日主生气未旺，所用贵神，悉皆得位而成旺，又且合格；奈何日主无力，不能胜任其福，亦劳困偃蹇。忽逢运扶，其日干得其强健，用神出虎啸风生；元命用神，方为我用，我得乘之，则勃然而兴。是偏气乘和，衰以遇旺，故迎吉而能崛起。若夫建业创功，有大小之不同；当于所遭命之轻重，辩之可也。
  **《聚兴》** 又有日主强，则四柱五行，杀纯不杂，身杀俱旺；则根本元无制伏，富贵不成，惟待运来制伏，杀神则化为权，方能崛兴，才德动公卿，功名显达，出类超群。是其身旺，杀神逢制化为权也；制神力旺，发福非常，安得其人不显达，以致极品之尊贵乎，实有其命。又要行其运以扶，方见勃兴也；如茍运不至，即常人耳。
  又要四柱中，日主健旺，用神亦旺，各相停均，为富屋朱门，贵命之贤子也。及其长大，成立丰隆，一逢恶曜运，加临元命，见其财而夺之，因其官而伤之，临其印而坏之，逢其食而损之；遭逢此运，祸不胜言，所以中年见倾而不发。如其恶运一去，又逢好运扶身，使我用神一新，譬如枯苗得雨，勃然而兴，鸿毛遇风，飘然而举，不可御也。
  **《中兴》** 又有人生五行身旺，阳刃比肩，俱各争旺，惟有财官格神等物，虚浮轻少，无力成功名矣；出门行运，又非作福之地，所以一生饥寒，劳苦落剥，有志无成。或至中年晚景，顿逢杀运，假杀为权，制伏阳刃；或得权贵以显扬、或招赀财而发福，当随五行清浊，以遇其运而别之。
  **《末兴》** 是一生穷困，忽然兴起于中年晚景也；故知此命元用财官，平生无气，即至运到，方成富贵，一一兴利。故末兴者，乃得运而然也。学者可不勉乎！

- **分字分词释义**：
  - **当兴**：命中本有富贵，自然兴旺发达。
  - **崛起**：由穷困忽然兴起，白手起家之象。
  - **聚兴**：多种有利因素聚集而兴，制杀化权之运。
  - **中兴**：中年后忽然兴起，假杀为权之格。
  - **末兴**：晚年忽然兴起，大器晚成之象。
  - **源清流洁**：格局纯粹无破，运程顺遂如流水。
  - **枯苗得雨**：久困之后逢好运，如枯苗逢甘霖。
  - **勃然而兴**：突然兴起，一飞冲天之势。
  - **虎啸风生**：威势大发，用神得力之象。
  - **假杀为权**：借七杀之力制伏比劫阳刃，化凶为权。

- **规范化释义（primary_lang_explained）**：
  本篇讨论命运"兴旺"的五种模式：
  1. **当兴**（天生富贵）：身旺且用神（财官印食）得令，不偏不杂，无刑冲克害。运程步步皆吉，源清流洁，终身享福。
  2. **崛起**（白手起家）：日主原弱，不能胜任财官，早年穷苦。忽逢帮身运（比劫印绶），日主转强，能胜任财官，勃然而兴。
  3. **聚兴**（制杀化权）：身杀两旺但无制，富贵不成。待运来制伏七杀（食伤运），杀化为权，功名显达。或早年吉，中年逢恶运倾败，恶运去后又如枯苗得雨，再次勃兴。
  4. **中兴**（中年发福）：身旺比劫重，财官虚浮，早年饥寒。中年晚景行七杀运，制伏阳刃，假杀为权而发福。
  5. **末兴**（晚景兴隆）：一生穷困，财官无气。晚年行运助起用神，方成富贵。

- **完整对等诠释（secondary_lang_full）**：
  **Theory of Collective Prosperity**:
  1. **Natural Prosperity (Dāng Xīng)**: Born with glory. Self is strong; Use-Gods (Wealth/Officer/Seal/Food) are commanding and pure. No clashes/harms. Luck cycles are consistently auspicious. "Source clear, stream clean"—lifelong blessing.
  2. **Rising Up (Jué Qǐ)**: Early poverty due to weak Self unable to sustain prosperous Noble Gods. Suddenly meeting assisting Luck (helping Self), Day Master gains strength to harness Use-Gods, rising abruptly like "tiger roaring, wind generating."
  3. **Gathered Prosperity (Jù Xīng)**: Self and Killings both strong but uncontrolled—no success initially. Awaiting Control Luck (Eating God) to transform Killing into Authority, leading to extraordinary success. Or, flourishing early, crashing in middle age due to Evil Stars, then rising again when good luck returns like "withered sprout getting rain."
  4. **Mid-Life Prosperity (Zhōng Xīng)**: Strong Self with abundant Parallels/Blades; Wealth/Officer floating weak. Early life poor. Middle/Late age meeting Killing Luck to control Blades ("Borrowed Killing as Authority"), bringing fame or wealth.
  5. **Late Prosperity (Mò Xīng)**: Lifelong poverty, Use-Gods lifeless. Suddenly rising in late years when Luck arrives.

- **核心要点**：
  - **兴旺五式**：当兴、崛起、聚兴、中兴、末兴
  - **身财平衡**：身旺财官旺为当兴；身弱行扶身运为崛起
  - **制化关键**：身杀两旺需制杀运；比劫重需杀运制刃
  - **运程作用**：命好不如运好，枯苗得雨方能兴

- **详细解说**：  《群兴论》是子平法论述人生兴衰轨迹的重要篇章，以"当兴、崛起、聚兴、中兴、末兴"五种模式概括人生发达的类型。**当兴**——天生富贵，身旺用神得令无刑冲，"源清流洁"终身享福，是上等命造。**崛起**——白手起家，日主原弱不能胜任财官，早年穷苦，忽逢扶身运（比劫印绶）则"勃然而兴"。**聚兴**——制杀化权，身杀两旺但无制，待运来制伏七杀则"杀化为权"；或早年吉后倾败，恶运去后"枯苗得雨"再次兴起。**中兴**——中年发福，身旺比劫重而财官虚浮，早年饥寒，中年行杀运"假杀为权"制伏阳刃而发福。**末兴**——大器晚成，一生穷困财官无气，晚年运至方成富贵。五式皆强调"运程作用"：命好不如运好，关键在于能否在合适的时机遇到合适的大运。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_631]` `[trigger: 当兴源清]` `[factor_trigger: dangxing AND shenwang_yongshen_deling AND yuanqing_liujie]` `[role: 主干]` 当兴者，身主专旺用神得令不偏不杂，源清流洁步步皆吉。 → 《渊海子平·群兴论》
  - `[ns_yhzp_632]` `[trigger: 崛起白手]` `[factor_trigger: jueqi AND rizhuwuli AND yunfu_boran_xing AND fushen_yun]` `[role: 条件分支]` 崛起者，日主无力不能胜任其福；忽逢运扶日干强健，勃然而兴。 → 《渊海子平·群兴论》
  - `[ns_yhzp_633]` `[trigger: 聚兴制杀]` `[factor_trigger: juxing AND shensha_juwang AND yunzhi_huaquan]` `[role: 条件分支]` 聚兴者，身杀俱旺元无制伏；待运来制伏杀神化为权，功名显达。 → 《渊海子平·群兴论》
  - `[ns_yhzp_634]` `[trigger: 枯苗得雨]` `[factor_trigger: eyun_qu AND haoyun_fushen AND boran_xing]` `[role: 条件分支]` 恶运一去又逢好运扶身，譬如枯苗得雨勃然而兴。 → 《渊海子平·群兴论》
  - `[ns_yhzp_635]` `[trigger: 中兴假杀]` `[factor_trigger: zhongxing AND shenwang_bijie AND jiasha_weiquan]` `[role: 条件分支]` 中兴者，身旺比劫争旺财官虚浮；顿逢杀运假杀为权制伏阳刃。 → 《渊海子平·群兴论》
  - `[ns_yhzp_636]` `[trigger: 末兴晚福]` `[factor_trigger: moxing AND yisheng_qiongkun AND wanyun_zhi]` `[role: 条件分支]` 末兴者，一生穷困；忽然兴起于中年晚景，乃得运而然也。 → 《渊海子平·群兴论》
  - `[ns_yhzp_637]` `[trigger: 群兴论纲领]` `[factor_trigger: qunxing_lun AND wushi AND yuncheng_zuoyong]` `[role: 总结]` 群兴论以当兴崛起聚兴中兴末兴五式概括人生兴达轨迹，强调运程作用。 → 《渊海子平·群兴论》"""
    normalized_text_zh: str = """"""
    subject: str = "群兴论"
    factor_refs: list = ['natural_prosperity', 'prosperity', 'withered_sprout_rain', 'source_clear']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_群兴论_001_L1",
    )
    version: str = "1.0.0"
