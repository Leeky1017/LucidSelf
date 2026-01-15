"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.042757
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
    semantic_id="smth_v1.0.0_旺衰循环与盛极必衰_001",
    book_id="sanming",
    engine_id="bazi"
)
class 旺衰循环与盛极必衰(SemanticEntry):
    """
    - **原文（source_text）**：
  观夏月大旱，金石流，水土焦；六月暑气增，寒气灭。秋月金胜，草木黄落；冬月大寒太冷，水结冰，火气顿减，其旺其死，概可见矣。盖四时之序，节满即谢；五行之性...
    """
    
    original_text: str = """- **原文（source_text）**：
  观夏月大旱，金石流，水土焦；六月暑气增，寒气灭。秋月金胜，草木黄落；冬月大寒太冷，水结冰，火气顿减，其旺其死，概可见矣。盖四时之序，节满即谢；五行之性，功成必复：故阳极而降，阴极而升；日中则昃，月盈则亏，此天之常道也。人生天地，势积必损，财聚必散，年少反衰，乐极反悲，此人之常情也。故一盛一衰，或得或失，荣枯进退，难逃此理。经云：「人虽灵于万物，命莫逃乎五行。」斯言尽矣。

- **分字分词释义**：
  - **节满即谢、功成必复**：节令行至极点则转衰，五行之功用至满则必有回转。
  - **阳极而降、阴极而升**：阳长至极则转入阴，阴极至寒则阳萌生，呼应日中则昃、月盈则亏。
  - **势积必损、财聚必散**：用人事比喻五行气机的涨落，以帮助理解命运中盛衰更替的必然性。

- **规范化释义（primary_lang_explained）**：
  作者借夏季大旱金石流、水土焦，秋季金胜草木黄落，冬季大寒水冰火减的自然现象，说明「其旺其死」在现实世界中随处可见：一行之旺，自然伴随另一行之死。进一步指出，四时节序的规律是：节气走到极点就会谢去；五行的性情是：功成之后必然反转，阳极则降，阴极则升，如同太阳到中天便必西斜，月亮盈满之后必然亏损。这是天道的常规。人处天地之间，同样难逃此理：气势积累到极处必有损耗，财富积聚到极点必有散失，少年盛壮之后必然走向衰老，欢乐到了极点往往转成悲伤，荣枯得失、进退起伏，皆是五行盛衰循环的映照。

- **完整对等诠释（secondary_lang_full）**：
  Drawing on scenes of summer drought where metals melt and earth and water are scorched, of autumn when Metal prevails and plants wither, and of deep winter when water freezes and fire dwindles, the author shows that “what is prosperous and what is dead” can be seen everywhere in nature: one element’s strength always implies another’s decline. The sequence of the seasons follows the rule that, when a term has reached its fullness, it begins to fade; the Five Elements behave so that, when their work is complete, they must reverse. Yang, having climbed to its peak, descends; yin, having sunk to its nadir, begins to rise. The sun at noon must tilt west; a full moon must begin to wane. This is Heaven’s ordinary law. Human affairs mirror it: accumulated momentum eventually runs down; amassed wealth eventually disperses; youth inevitably gives way to age; extreme joy often turns into sorrow. Gains and losses, glory and decline, advance and retreat all unfold within this larger cycle of waxing and waning qi.

- **核心要点**：
  - 旺衰循环是命理判断的根本背景：任何一段极旺的运势，都应预期其后的回落；任何一段低迷的状态，也可能是反转前的铺垫。
  - 「盛德乘时曰旺」并不意味着一味追求旺，过旺反而易触发「功成必复」的反转机制，须以中和为最高准则。
  - 在应用与建模上，应避免把某一五行长期设为「恒旺」：应让旺度随时间曲线自然起伏，使模拟结果更接近真实人生中的荣枯进退。

- **详细解说**：
  1) 在长周期运势建模中，为每个大运、流年构建「旺度曲线」，而非简单标记「吉/凶」：运初渐升、中段极旺、后段渐衰；
  2) 推盘解释时，对处于极旺中段的运势，系统同步提示「盛极而衰」的后续风险，引导用户在高峰期保守部分资源与弹性；
  3) 对处于低迷尾声的阶段，系统可提示「阴极阳生」的反转可能，避免将一时困顿绝对化，兼顾心理扶助；
  4) 工程实现时，将「盛极必衰」融入时间序列模型，通过对历史状态的累积与回落参数，模拟气机的起伏而非单调直线。

- 反例与边界：
  - 不宜见一段运势吉利，就断「一路高升无回头」，忽略任何系统都存在资源与耐力的上限；
  - 不能把一段凶运视为「永久低谷」，而忽略后续可能出现的补偿与反弹；
  - 工程上若把五行旺衰视作恒定参数，不随时间更新，模型将无法呈现现实人生的波动性；
  - 反向误区是过度强调「盛极必衰」，在每次好转时都夸大警报，削弱用户对系统积极建议的信心。

- 小例（示意）：
  - 某命局木火为用，行东南木火大运中段已得显贵，系统在给出「事业高峰」判断的同时，会提示其「积谷防饥」，为下一阶段可能转入金水运预留空间；
  - 另一命局早年行忌神运，连续数年失利，系统则根据运势曲线判断其已接近低谷末段，在解释中加入「渐趋回升」的信号，帮助其调整心态与决策节奏。"""
    normalized_text_zh: str = """"""
    subject: str = "旺衰循环与盛极必衰"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_旺衰循环与盛极必衰_001_L1",
    )
    version: str = "1.0.0"
