"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.524000
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
    semantic_id="zpzq_v1.0.0_变之不善与变而不失本格_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 变之不善与变而不失本格(SemanticEntry):
    """
    - **原文（source_text）**：
  何谓变之而不善？如丙生寅月，本为印绶，甲不透干而会午会戌，则化为劫。丙生申月，本属偏财，藏庚透壬，会子会辰，则化为煞，如此之类，亦多皆变之不善者也.又...
    """
    
    original_text: str = """- **原文（source_text）**：
  何谓变之而不善？如丙生寅月，本为印绶，甲不透干而会午会戌，则化为劫。丙生申月，本属偏财，藏庚透壬，会子会辰，则化为煞，如此之类，亦多皆变之不善者也.又有变之而不失本格者，如辛生寅月，透丙化官，而又透甲，格成正财，正官乃其兼格也.乙生申月，透壬化印，而又透戊，则财能生官，印逢财而退位，虽通月令，格成伤官，百戊官忌见.丙生寅月，午戌会劫，而又或透甲，或透壬，则仍为印而格不破.丙生申月，逢壬化煞，而又透戊，则食神能制煞生财，仍为财格，不失富贵.如此之类甚多，是皆变而不失本格者也.是故八字非用神不立，用神非变化不灵，善观命者，必于此细详之.

- 原注（原文注解）：
  　　本段分两层：
  1) **变之而不善**：变化方向破坏既有用神结构，使原本可贵之格失衡；
  2) **变而不失本格**：虽有变化，然新旧两股力量形成兼格或辅格关系，主格并未被推翻.
  末句“八字非用神不立，用神非变化不灵”点明：
  - 没有用神则格局无从成立；
  - 不理解变化，则看不出格局的活用之处.

- 分字分词释义：
  - 丙生寅月，本为印绶：
    - 丙火日主生于寅，寅中丙长生，为印绶格的基本结构.
  - 甲不透干而会午会戌，则化为劫：
    - 甲不透，午戌与寅会成火局，寅中甲比之气被引出，化为比劫争权，破坏印格的纯粹.
  - 丙生申月，本属偏财，藏庚透壬，会子会辰，则化为煞：
    - 丙火日主生申，申中庚为偏财；若庚不透而壬透，且会子辰成水局，则水成煞局，偏财之象被转为官煞对身的压力.
  - 百戊官忌见：
    - 今多作“忌官见戊”，或解作“官格忌戊土混杂”，本精校仍从今本旧字，在注中按“官忌见戊土”解释.

- **规范化释义（primary_lang_explained）**：
  首先是“变之而不善”的两例：
  - 丙日生寅，本是印绶当令，一般视为秀气之局；但若寅午戌火局成形，而寅中甲比之气被引动而强盛，甲不透而以比劫之姿参与局势，则原本的印绶之清被比劫夺势，变成比劫过旺，反从印格滑向身旺劫重，格局大减；
  - 丙日生申，本为偏财格；若申中庚不透，反而壬水从申藏透出，再加子辰会局成水，则水气大旺成煞，原本偏财之象被水煞主导，格局重心由“以财生官”倒向“煞重克身”，是典型的“变之不善”。

  接着作者指出，还有一类更微妙的情形——变化发生了，但原本格局并未被推翻，而是形成**兼格**或“本格为主、他格为辅”的状态：
  - 辛日生寅，丙透化财为官，又透甲为财，主格是正财，而透丙之官成其兼格；
  - 乙日生申，壬透化印，再透戊为财，财既能生官，印则退居幕后；虽通月令，却已成为伤官格，以伤官为纲，官印为辅；
  - 丙日生寅，午戌会劫，若又透甲或透壬，印格仍在，比劫或煞只是辅佐，不足以破格；
  - 丙日生申，逢壬化煞，又透戊为食，食神得以制服煞气并生财，终仍为财格，且不失富贵.

  这些例子说明：变化的判断不能只盯“有没有变”，而要看“变到什么程度、变到谁主谁从”。有的变化是推翻格局，有的则只是增加层次.
 - **完整对等诠释（secondary_lang_full）**：  
  This passage distinguishes two very different kinds of change. In the first group, transformation actually harms the pattern. A chart that begins as a clear Resource or Wealth structure can, through later combinations and elemental bureaus, have its centre of gravity seized by Rob Wealth or Seven Killings so that the original Useful God is overturned. What once looked like a clean seal or pure wealth pattern is then re‑read as “robbers taking over the storehouse” or “Killing bearing down on the body”, and the earlier advantages are undone. In the second group, change does not overthrow the main pattern but simply adds another layer. A chart may still be judged primarily as Proper Wealth, for example, even though an emergent Officer line is worth recording as a secondary pattern; or a shift toward Hurting Officer may be confined to a subsidiary strand while the original Resource frame remains in command. The real question is therefore not merely “has there been change?”, but “to what degree has it changed, and who now holds authority?” Some transformations topple the whole structure; others simply enrich it.

  The author ends by stressing that a chart cannot stand without a clearly appointed Useful God, and that a Useful God which never participates in any change is lifeless. Living judgement always pays close attention to how structural shifts either push the centre away from the Useful God, or else bring in auxiliary lines that support it without stealing its seat.


- 详细解说：
  - “变之而不善”多发生在：
    - 忌神借合局之势上位，压制原有用神；
    - 或本来作为辅神的比劫、煞神扩张过度，使主格变质；
  - “变而不失本格”强调主格与兼格的区分：谁作为提纲、谁作为辅佐，必须分明，否则容易误判；
  - 末句把“变化”提升到方法论高度：不懂变化，只看静态格名，命理便变成僵死的分类学，只能粗看而不能深断.

- 核心要点：
  - 判断变化的三层：
    1) 变而破格：原用神被彻底颠覆，格局另立；
    2) 变而兼格：原格为主，新格为辅，相辅相成；
    3) 变而不及：变化力量不足以改动大局，只作背景之用.
  - 观察次序：先看主格是否被动摇，再谈兼格之美；不可倒置.

- 应用推演：
  1) 先按原用神定主格；
  2) 再按透干、会局检查有无“变之不善”的线索：比劫夺印、煞压财官等；
  3) 若变化未能推翻主格，但形成清晰的次格（如财格中有官、印格中见食等），则记为兼格；
  4) 在断人生时，对“主格”与“兼格”分层表述：主格主一生大方向，兼格多主副业、支线经历或特定运程；
  5) 岁运到来时，再看其是强化主格、扶持兼格，还是触发“变之不善”的破局路线.

- 反例与边界：
  - 一见变化便断“原格破坏”，不看原格是否仍有根、有护；
  - 对兼格过度着迷，把次要的变化当成命局主轴；
  - 只按“书上例句”来认变，不在本局整体结构中权衡力量与位置.

- 小例（示意）：
  - 一命原为财格，后因官星透出而成财官双美，若财根深、官有印护，则财格为主、官格为辅；岁运逢官，多主仕途机会；逢财，多主财富扩张，而不宜说成“全改为官格”。

- 校勘与字词辨析：
  - “百戊官忌见”：多本作“忌官见戊”，或解作“官格忌戊土混杂”，本精校仍从今本旧字，在注中按“官忌见戊”解释；
  - “变而不失本格”一语虽未明写于原文，但本段诸例皆以此为旨，本精校据意概括于小节标题."""
    normalized_text_zh: str = """"""
    subject: str = "变之不善与变而不失本格"
    factor_refs: list = ['bianzhibushan', 'bianerbushi', 'jiange', 'yinhuajie', 'caihuasha', 'engine_id', 'bianhua_haobai', 'bazi_rule_engine', 'yuange_baocun', 'bazi_rule_engine', 'zhuge_jiange', 'bazi_rule_engine', 'bianhua_zhiliang', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_111', 'bianhua_haobai', 'rel_zpzq_112', 'yuange_baocun', 'evi_zpzq_103', 'yinhuajie', 'rule_yinhuajie', 'evi_zpzq_104', 'zhuge_jiange', 'rule_jiange_panding', 'concept_degradation', 'concept_coexistence']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_变之不善与变而不失本格_001_L1",
    )
    version: str = "1.0.0"
