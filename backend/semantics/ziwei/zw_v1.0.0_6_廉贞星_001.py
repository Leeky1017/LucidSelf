"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725557
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
    semantic_id="zw_v1.0.0_6_廉贞星_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 6廉贞星(SemanticEntry):
    """
    - 原文（source_text）：

  问：廉贞所主若何？

  答曰：廉贞属木，北斗第五星也。在斗司品秩，在数司权令，不临庙旺，更犯官符，故曰化囚为杀，触之不可解其祸，逢之不可测其祥。主人心狼性...
    """
    
    original_text: str = """- 原文（source_text）：

  问：廉贞所主若何？

  答曰：廉贞属木，北斗第五星也。在斗司品秩，在数司权令，不临庙旺，更犯官符，故曰化囚为杀，触之不可解其祸，逢之不可测其祥。主人心狼性狂，不习礼义。逢帝座执威权，遇禄存主富贵，遇文昌好礼乐，遇杀曜显武职。在官禄有威权，在身命为次桃花。若居旺宫，则赌赙迷花而致讼；与巨门交会于陷地，则是非起于官司。逢财星耗合，祖业必破；遇刑忌则脓血不免；遇白虎则刑杖难逃；遇武曲于受制之乡，恐木压蛇伤；同火曜于陷空之地，主投河自缢。

- 原注（原文注解，可无则省略小节）：

  歌曰：廉贪已亥宫，遇吉福盈丰。应过三旬后，须防不善终。

- 分字分词释义：

  - **化囚为杀**：廉贞不得地、又犯官符时，其原本的权令与管束力量转化为主动攻击与破坏力。
  - **次桃花**：不同于纯粹享乐的桃花，更多指与权力、金钱、感情纠葛交织的复杂情欲场景。
  - **木压蛇伤**：比喻木性刚烈之星压制柔弱之势，容易导致内外交困、受伤或极端行为。
  - **陷空之地**：宫位与四杀等星同时失势之处，象征支撑全失、易走向自毁的极端境况。
  - **廉贪巳亥宫**：廉贞与贪狼同居巳亥等宫，吉则福厚，运过中年后若失衡则隐含覆败之机。

- 规范化释义（primary_lang_explained）：

  本条将廉贞刻画成一颗极端敏感的权令之星：得地而受吉星护持时，能代表制度内的执法、稽查与整顿力量；一旦失位、再逢官符与众凶，则原本的约束之力就会转为“化囚为杀”，容易引发官非、刑伤乃至自毁。文本中一方面强调廉贞掌管品秩与权柄，能借帝座、禄存、文昌之力而成威权在握、富贵而不失礼乐；另一方面也不断提醒其在身命为次桃花时，极易因赌赙、酒色、偏情纠纷而惹上讼狱与名声崩塌。

  诸多凶险组合，都是在说明廉贞的“边界条件”：与巨门同处陷地，象征言语与是非纠缠，官讼风险陡增；与武曲在受制之乡相会，像是硬碰硬的资源争夺，“木压蛇伤”多主两败俱伤；与火曜同处陷空，更近似于在压力峰值之下的冲动绝行，如投河、自缢之象。廉贞并非单纯的“坏星”，而是一把高度锋利且带情绪色彩的权力之刃——若有帝座、禄存、文昌等加持，则能转为公正执法、清理积弊；若缺乏规范与自制，只凭一时情绪行事，则极易把自己与他人一同推向深渊。

- 完整对等诠释（secondary_lang_full）：

  This passage presents Lianzhen as a highly charged star of rank and command, whose nature swings sharply between discipline and destruction. When dignified and supported by benefic companions such as the Emperor Seat, Lu or literary stars, it can symbolise the power to enforce laws, expose corruption and take unpopular but necessary decisions. In such charts, Lianzhen stands for people who sit close to the machinery of punishment and reward—judges, inspectors, officers—whose authority, if handled with conscience, can genuinely protect the order of a system.

  When Lianzhen falls from strength, however, its quality of "transforming confinement into killing force" becomes dominant. Instead of structuring behaviour, power turns vindictive: lawsuits proliferate, resentment accumulates and personal impulses override ethical restraint. The text describes combinations with Jumen in a pit as the breeding ground for constant disputes and legal entanglements; with Wuqu under restriction as a scenario where hard, financial or military pressures crush more flexible options, leading to injury for all sides; with Fire Star in an empty, weakened place as a symbol of breakdown under unbearable stress, including self‑destructive acts like drowning or suicide. The so‑called "secondary peach blossom" nature points not only to romance, but to entanglements of sex, money and status that blur boundaries and invite scandal. Overall, Lianzhen does not simply promise high office or disaster; it asks how a person holds sharp authority under emotional strain, and whether they can transform that intensity into principled courage instead of revenge or collapse.

- 核心要点：

  1. **廉贞化囚**：司品秩权令，不临庙旺则化囚为杀。
  2. **次桃花星**：在身命为次桃花，易赌赙迷花致讼。
  3. **凶险组合**：与巨门陷地则官非，与武曲受制则木压蛇伤，与火曜陷空则投河自缢。
  4. **吉星化解**：遇帝座则执威权，遇禄存则富贵，遇文昌则好礼乐。
  5. **三旬后防**：廉贪巳亥宫遇吉则福盈，但三旬后须防不善终。

- 叙事素材（narrative_snippets）：

  - **化囚为杀**："司品秩权令，不临庙旺则化囚为杀"，廉贞失位则约束力转为破坏力。
  - **次桃花**："在身命为次桃花，易赌赙迷花致讼"，非纯粹享乐而是权钱情欲交织的复杂纠葛。
  - **木压蛇伤**："与武曲受制之乡相会，木压蛇伤"，刚烈相碰导致两败俱伤。
  - **吉星化解**："遇帝座则执威权，遇禄存则富贵，遇文昌则好礼乐"，廉贞需吉星护持方能发挥正面力量。
  - **现代应用**：廉贞可作为评估"权力风险"的指标——权力之刃需规范与自制方能正用。"""
    normalized_text_zh: str = """"""
    subject: str = "6 廉贞星"
    factor_refs: list = ['star_lianzhen', 'pattern_huaqiu_weisha', 'pattern_ci_taohua', 'pattern_muya_sheshang', 'combo_liantan_sihai']
    
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
        l1_anchor="zw_v1.0.0_6_廉贞星_001_L1",
    )
    version: str = "1.0.0"
