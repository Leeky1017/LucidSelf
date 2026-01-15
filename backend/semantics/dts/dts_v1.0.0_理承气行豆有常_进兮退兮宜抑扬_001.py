"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.932703
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
    semantic_id="dts_v1.0.0_理承气行豆有常_进兮退兮宜抑扬_001",
    book_id="dts",
    engine_id="bazi"
)
class 理承气行豆有常进兮退兮宜抑扬(SemanticEntry):
    """
    - 原文（source_text）：
  理承气行豆有常，进兮退兮宜抑扬。

- 原注（原文注解）：
  　　翕辟往来皆气，而理行乎其间，行之始而进，进之极。则为退之机，如三月甲木是也，行之盛而退，退...
    """
    
    original_text: str = """- 原文（source_text）：
  理承气行豆有常，进兮退兮宜抑扬。

- 原注（原文注解）：
  　　翕辟往来皆气，而理行乎其间，行之始而进，进之极。则为退之机，如三月甲木是也，行之盛而退，退之极，则为进之机，如九月甲木是也，学者能抑扬其浅深，斯可以言命。

- 分字分词释义：
  - 理：法理、道理、秩序（五行常理）。
  - 承：承接、依凭.
  - 气行：气机运行、升降出入.
  - 豆：原刻或传抄字作“豆/度/也”，此处据原文录为“豆”，义取“法度、节度”。
  - 有常：有其恒常之规律.
  - 进：气之进、生旺之势.
  - 退：气之退、休囚之势.

- 规范化释义（primary_lang_explained）：
  五行运行自有恒常的法度.气机或进或退，断法当抑其太过、扬其不足，使局得其中.

- **次语种完整诠释（secondary_lang_full）**：  
  Principle (Li) sustains and follows the movement of qi (Qi Xing), which operates according to constant rhythms (You Chang). These rhythms manifest as phases of advance (Jin: waxing, gaining strength) and retreat (Tui: waning, losing vigor). Crucially, advance carried to its extreme contains within it the seed of retreat, while retreat at its limit harbors the potential for renewed advance—exemplified by Jia Wood in the third month (peak advance before decline) and ninth month (extreme retreat before revival). The art of regulation (Yi Yang) consists of restraining (Yi) what is excessive and supporting (Yang) what is deficient, thereby maintaining structural balance across cyclical phases. This approach maps the advance-retreat phase to appropriate regulatory actions, yielding stage-adaptive strategies rather than static strength-weakness labels that ignore temporal dynamics.

- **核心要点**：
  - 理指五行运行的恒常法则与秩序
  - 气行指气机的升降出入、翕辟往来
  - 进之极则藏退之机，退之极又伏进之机
  - 抑是抑制过度之处，扬是扶助不足之方
  - 甲木三月为进之极，九月为退之极，进退转换有迹可循
  - 断法当抑其太过、扬其不足，使局得其中

- **详细解说**：
  本条阐明气机运行的进退规律与调节原则。"理承气行"揭示五行运行自有恒常法度，不以人意为转移；"进兮退兮"描述气机的两大阶段——进为生旺之势，退为休囚之势。关键洞见在于：进之极则藏退之机，退之极又伏进之机，如甲木三月（进之极，将退）与九月（退之极，将进）。"宜抑扬"则为操作策略：抑其太过、扬其不足，顺着理的常态去修正偏差。实占时，先判断当前五行处于进中、极进、退中、极退还是交界期，再识别"太过"与"不及"的具体落点，最后按阶段细分执行抑扬策略。

 - **narrative_snippets（叙事片段）**：
  - `[ns_dts_013]` `[trigger: 进退判断]` `[factor_trigger: jin_tui_phase]` `[role: 主干]` 五行之理承载气机运行，自有恒常法度，进退之间当用抑与扬得其中。 → 《滴天髓·通天论》#第5条
  - `[ns_dts_014]` `[trigger: 甲木三月]` `[factor_trigger: jin_tui_phase]` `[role: 条件分支]` 甲木三月为进之极，将退之机已伏其中，宜知止而不过。 → 《滴天髓·通天论》#第5条
  - `[ns_dts_015]` `[trigger: 甲木九月]` `[factor_trigger: jin_tui_phase]` `[role: 条件分支]` 甲木九月为退之极，然进之机已在酝酿，宜蓄力待时。 → 《滴天髓·通天论》#第5条
  - `[ns_dts_105]` `[trigger: 进退相生]` `[factor_trigger: jin_tui_cycle]` `[role: 主干依赖]` 进之极则藏退之机，退之极又伏进之机，进退循环构成完整节律。 → 《滴天髓·通天论》#第5条
  - `[ns_dts_106]` `[trigger: 调节步骤]` `[factor_trigger: yi_yang_strategy]` `[role: 总结]` 断局须先判当前进退阶段，再依阶段抑其太过、扬其不足，以守其中。 → 《滴天髓·通天论》#第5条"""
    normalized_text_zh: str = """"""
    subject: str = "理承气行豆有常，进兮退兮宜抑扬。"
    factor_refs: list = ['li_principle', 'qi_movement', 'jin_tui_phase', 'jin_tui_phase', 'yi_yang_strategy', 'yi_yang_strategy']
    
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
        l1_anchor="dts_v1.0.0_理承气行豆有常_进兮退兮宜抑扬_001_L1",
    )
    version: str = "1.0.0"
